"""topping_pattern_classical base 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. The family
focuses on classical chart-pattern QUALITY / SYMMETRY / MEASUREMENT /
PROJECTION metrics — the differentiator vs the 1a `topp` family (which mainly
detects pattern existence). Coverage: Head-and-shoulders variants & timing,
double/triple/quadruple-top variants, broadening / megaphone / diamond,
descending-triangle / wedges, BARR (Bulkowski), Adam/Eve double-top
typology, Lindsay/Schabacker specialist patterns.

Inputs: SEP OHLCV only (open, high, low, close, volume). PIT-clean:
right-anchored rolling, explicit min_periods, no centered windows,
no .shift(N). Self-contained helpers — no cross-family imports.
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


def _pivot_highs_mask(high, k=5):
    """Return float mask 0/1 marking past-only pivot highs: bar t-k is higher
    than the surrounding 2k bars (uses [t-2k .. t]; emit at index t-k means
    we read forward bars... so to stay PIT we set value at index t == bar t).
    Instead: mark a 'confirmed pivot' at index t whenever bar t-k is the max
    of [t-2k .. t]. The label appears at t (when confirmation is possible),
    not at t-k — so it is PIT-clean."""
    h = high.values.astype(float)
    n = len(h)
    win = 2 * k + 1
    out = np.full(n, np.nan)
    if n < win:
        return pd.Series(out, index=high.index)
    for i in range(win - 1, n):
        seg = h[i - 2 * k:i + 1]
        if np.isnan(seg).any():
            out[i] = np.nan
            continue
        mid = seg[k]
        if mid == seg.max() and mid > seg[0] and mid > seg[-1]:
            out[i] = 1.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=high.index)


def _pivot_lows_mask(low, k=5):
    l = low.values.astype(float)
    n = len(l)
    win = 2 * k + 1
    out = np.full(n, np.nan)
    if n < win:
        return pd.Series(out, index=low.index)
    for i in range(win - 1, n):
        seg = l[i - 2 * k:i + 1]
        if np.isnan(seg).any():
            out[i] = np.nan
            continue
        mid = seg[k]
        if mid == seg.min() and mid < seg[0] and mid < seg[-1]:
            out[i] = 1.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=low.index)


def _poly_coef(s, n, deg, idx_coef, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, deg + 1)
    def _co(w):
        if np.isnan(w).any():
            return np.nan
        try:
            return float(np.polyfit(np.arange(len(w)), w, deg)[idx_coef])
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=min_periods).apply(_co, raw=True)


def _poly_r2(s, n, deg, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, deg + 1)
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        try:
            x = np.arange(len(w), dtype=float)
            coefs = np.polyfit(x, w, deg)
            yhat = np.polyval(coefs, x)
            ss_res = float(((w - yhat) ** 2).sum())
            ss_tot = float(((w - w.mean()) ** 2).sum())
            if ss_tot == 0:
                return np.nan
            return 1.0 - ss_res / ss_tot
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=min_periods).apply(_r2, raw=True)


def f03_tpcl_001_complex_hs_shoulder_count_252d_d3(high: pd.Series) -> pd.Series:
    """Count of pivot-highs in 252d within +/-5% of the dominant peak — proxy for
    complex H&S with multiple shoulders (>=4 shoulders signals a "complex" variant)."""
    piv = _pivot_highs_mask(high, k=5)
    def _cnt(idxs_window, vals_window):
        return idxs_window
    def _q(w):
        if np.isnan(w).all():
            return np.nan
        # w holds high values; we need the pivot mask too — done via combined helper below
        return np.nan
    # Vectorised path: compute pivot heights then rolling-count near max
    piv_h = high.where(piv > 0, np.nan)
    def _cnt2(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        mx = v.max()
        return float((v >= 0.95 * mx).sum())
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_cnt2, raw=True)).diff().diff().diff()


def f03_tpcl_002_inverse_symmetric_hs_top_mirror_score_252d_d3(high: pd.Series) -> pd.Series:
    """Mirror-symmetry score: at each bar, fit close-mirror around the 252d
    midpoint and measure highs-vs-mirror correlation — high score signals an
    inverse-symmetric H&S top (left-mirror of right side)."""
    def _ms(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w)
        half = n // 2
        if half < 5:
            return np.nan
        left = w[:half]
        right = w[-half:][::-1]
        if left.std() == 0 or right.std() == 0:
            return np.nan
        return float(np.corrcoef(left, right)[0, 1])
    return (high.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True)).diff().diff().diff()


def f03_tpcl_003_hs_neckline_slope_sign_indicator_252d_d3(low: pd.Series) -> pd.Series:
    """Sign of fitted regression slope on 252d pivot-lows — +1 = upsloping neckline,
    -1 = downsloping. Downsloping neckline is the more bearish H&S variant."""
    sl = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    return (np.sign(sl).where(sl.notna(), np.nan)).diff().diff().diff()


def f03_tpcl_004_hs_neckline_downslope_strength_252d_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Magnitude of negative neckline slope normalised by close — large negative
    value = strongly downsloping neckline (bearish H&S quality boost)."""
    sl = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    neg = -sl.where(sl < 0, 0.0)
    return (_safe_div(neg, close)).diff().diff().diff()


def f03_tpcl_005_hs_head_to_shoulders_height_ratio_252d_d3(high: pd.Series) -> pd.Series:
    """Ratio of (highest pivot - second-highest pivot) to (second-highest pivot -
    median of remaining pivots) in 252d — large ratio = pronounced head, classic H&S."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _r(w):
        v = w[~np.isnan(w)]
        if v.size < 3:
            return np.nan
        sv = np.sort(v)[::-1]
        head = sv[0]
        shoulder = sv[1]
        rest = sv[2:]
        if rest.size == 0:
            return np.nan
        base = float(np.median(rest))
        denom = shoulder - base
        if denom <= 0:
            return np.nan
        return float((head - shoulder) / denom)
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True)).diff().diff().diff()


def f03_tpcl_006_hs_shoulder_time_symmetry_index_252d_d3(high: pd.Series) -> pd.Series:
    """Time-symmetry of left-shoulder-to-head vs head-to-right-shoulder distance,
    normalised so 1.0 = perfectly symmetric, 0.0 = highly asymmetric."""
    piv = _pivot_highs_mask(high, k=5)
    piv_h = high.where(piv > 0, np.nan)
    def _ts(w):
        v_full = w
        mask = ~np.isnan(v_full)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = v_full[mask]
        sv_order = np.argsort(vals)[::-1]
        if sv_order.size < 3:
            return np.nan
        top3 = sv_order[:3]
        positions = np.sort(idxs[top3])
        if len(positions) < 3:
            return np.nan
        d_lh = positions[1] - positions[0]
        d_hr = positions[2] - positions[1]
        if d_lh + d_hr == 0:
            return np.nan
        return 1.0 - abs(d_lh - d_hr) / (d_lh + d_hr)
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_ts, raw=True)).diff().diff().diff()


def f03_tpcl_007_hs_shoulder_amplitude_symmetry_252d_d3(high: pd.Series) -> pd.Series:
    """Amplitude symmetry of left vs right shoulder. 1.0 = identical heights,
    0.0 = highly asymmetric. Computed as 1 - |L-R|/(L+R)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _as(w):
        v_full = w
        mask = ~np.isnan(v_full)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = v_full[mask]
        sv_order = np.argsort(vals)[::-1]
        if sv_order.size < 3:
            return np.nan
        top3_idx = sv_order[:3]
        positions = idxs[top3_idx]
        heights = vals[top3_idx]
        order = np.argsort(positions)
        h_chron = heights[order]
        L, _, R = h_chron[0], h_chron[1], h_chron[2]
        if L + R <= 0:
            return np.nan
        return 1.0 - abs(L - R) / (L + R)
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_as, raw=True)).diff().diff().diff()


def f03_tpcl_008_hs_head_to_neckline_depth_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vertical depth from H&S head (252d max-high) to current neckline
    (252d rolling min-low) — the measured-move base."""
    h = high.rolling(YDAYS, min_periods=QDAYS).max()
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(h - nl, close)).diff().diff().diff()


def f03_tpcl_009_hs_volume_decline_LtoR_signature_252d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-profile signature: avg-vol-near-left-pivot minus avg-vol-near-right-pivot,
    normalised. Positive value confirms classic H&S signature (volume declining L->H->R)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _vd(w_h, w_v):
        mask = ~np.isnan(w_h)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w_h[mask]
        sv_order = np.argsort(vals)[::-1]
        if sv_order.size < 3:
            return np.nan
        top3 = sv_order[:3]
        pos = idxs[top3]
        order = np.argsort(pos)
        positions = pos[order]
        L_pos, R_pos = int(positions[0]), int(positions[2])
        lo_L = max(0, L_pos - 3); hi_L = min(len(w_v), L_pos + 4)
        lo_R = max(0, R_pos - 3); hi_R = min(len(w_v), R_pos + 4)
        vL = w_v[lo_L:hi_L]; vR = w_v[lo_R:hi_R]
        if vL.size == 0 or vR.size == 0:
            return np.nan
        mvL = np.nanmean(vL); mvR = np.nanmean(vR)
        if mvL + mvR == 0:
            return np.nan
        return float((mvL - mvR) / (mvL + mvR))
    n = YDAYS
    # paired rolling: implement via groups
    out = np.full(len(high), np.nan)
    h_vals = piv_h.values; v_vals = volume.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - n + 1)
        out[i] = _vd(h_vals[lo:i + 1], v_vals[lo:i + 1])
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_010_hs_target_to_actual_move_ratio_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of realised drop (close vs 252d-high) to H&S measured-move target
    (head minus neckline projected below neckline). Values >=1.0 = target reached."""
    h = high.rolling(YDAYS, min_periods=QDAYS).max()
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    target_drop = h - nl
    realised = h - close
    return (_safe_div(realised, target_drop)).diff().diff().diff()


def f03_tpcl_011_hs_formation_duration_relative_252d_d3(high: pd.Series) -> pd.Series:
    """Formation duration: bars from first pivot-high to last pivot-high inside the
    252d window, divided by 252 — relative duration of the H&S formation."""
    piv = _pivot_highs_mask(high, k=5)
    def _dur(w):
        idxs = np.where(w > 0)[0]
        if idxs.size < 2:
            return np.nan
        return float(idxs[-1] - idxs[0]) / float(len(w))
    return (piv.rolling(YDAYS, min_periods=QDAYS).apply(_dur, raw=True)).diff().diff().diff()


def f03_tpcl_012_hs_multi_scale_concurrent_overlap_count_d3(high: pd.Series) -> pd.Series:
    """Count of windows (63d, 126d, 252d, 504d) in which H&S-like 3-peak structure
    (mid-pivot is the highest of 3 top pivots) is detectable — multi-scale H&S."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _has_hs(w):
        v = w[~np.isnan(w)]
        if v.size < 3:
            return 0.0
        v_full = w
        mask = ~np.isnan(v_full)
        idxs = np.where(mask)[0]
        vals = v_full[mask]
        sv_order = np.argsort(vals)[::-1]
        if sv_order.size < 3:
            return 0.0
        top3 = sv_order[:3]
        pos = idxs[top3]
        order = np.argsort(pos)
        h_chron = vals[top3][order]
        if h_chron[1] > h_chron[0] and h_chron[1] > h_chron[2]:
            return 1.0
        return 0.0
    pieces = []
    for hz, mp in [(QDAYS, MDAYS), (126, QDAYS), (YDAYS, QDAYS), (DDAYS_2Y, YDAYS)]:
        pieces.append(piv_h.rolling(hz, min_periods=mp).apply(_has_hs, raw=True).rename(f"h{hz}"))
    return (pd.concat(pieces, axis=1).sum(axis=1)).diff().diff().diff()


def f03_tpcl_013_hs_left_shoulder_to_head_bars_252d_d3(high: pd.Series) -> pd.Series:
    """Bars between left-shoulder pivot and head pivot inside the 252d window."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _d(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = np.sort(idxs[sv])
        return float(pos[1] - pos[0])
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_d, raw=True)).diff().diff().diff()


def f03_tpcl_014_hs_head_to_right_shoulder_bars_252d_d3(high: pd.Series) -> pd.Series:
    """Bars between head pivot and right-shoulder pivot inside the 252d window."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _d(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = np.sort(idxs[sv])
        return float(pos[2] - pos[1])
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_d, raw=True)).diff().diff().diff()


def f03_tpcl_015_hs_time_symmetry_ratio_norm_252d_d3(high: pd.Series) -> pd.Series:
    """Normalised time-symmetry ratio: min(LH, HR) / max(LH, HR) — 1.0 perfectly
    symmetric, 0.0 highly asymmetric."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _r(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = np.sort(idxs[sv])
        a, b = pos[1] - pos[0], pos[2] - pos[1]
        if max(a, b) == 0:
            return np.nan
        return float(min(a, b)) / float(max(a, b))
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True)).diff().diff().diff()


def f03_tpcl_016_hs_neckline_angle_in_radians_252d_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Angle (radians) of neckline (252d-low regression) per unit log-price —
    captures both up- and down-sloping neckline orientation."""
    sl = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    norm = _safe_div(sl, close)
    return (np.arctan(norm)).diff().diff().diff()


def f03_tpcl_017_hs_distance_to_neckline_atr_norm_d3(low: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalised distance of current close above the 252d neckline (252d-low)."""
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - nl, atr)).diff().diff().diff()


def f03_tpcl_018_hs_completion_percentage_estimate_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimate of H&S pattern completion: (peak - close) / (peak - neckline).
    1.0 = neckline tagged, >1.0 = broken, <0.0 = price above peak (still forming)."""
    h = high.rolling(YDAYS, min_periods=QDAYS).max()
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(h - close, h - nl)).diff().diff().diff()


def f03_tpcl_019_hs_bars_since_right_shoulder_pivot_252d_d3(high: pd.Series) -> pd.Series:
    """Bars elapsed since the right-shoulder pivot (most recent pivot-high that is
    below the 252d max but above the median of all 252d pivots)."""
    piv = _pivot_highs_mask(high, k=5)
    piv_h = high.where(piv > 0, np.nan)
    def _b(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        m = float(np.median(vals))
        mx = float(vals.max())
        for j in range(idxs.size - 1, -1, -1):
            v = vals[j]
            if v < mx and v > m:
                return float(len(w) - 1 - idxs[j])
        return np.nan
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_b, raw=True)).diff().diff().diff()


def f03_tpcl_020_hs_recognition_confidence_score_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite confidence: product of time-symmetry x amplitude-symmetry x
    head-prominence x downsloping-neckline-indicator. Higher = textbook H&S."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _conf(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = np.sort(idxs[sv])
        heights = vals[sv][np.argsort(idxs[sv])]
        a, b = pos[1] - pos[0], pos[2] - pos[1]
        if max(a, b) == 0:
            return np.nan
        ts = min(a, b) / max(a, b)
        L, _, R = heights[0], heights[1], heights[2]
        if L + R <= 0:
            return np.nan
        amp = 1.0 - abs(L - R) / (L + R)
        head = heights[1]
        if max(L, R) <= 0:
            return np.nan
        prom = (head - max(L, R)) / head
        if prom < 0:
            return 0.0
        return float(ts * amp * prom)
    cf = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_conf, raw=True)
    sl = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    return (cf * (1.0 + (sl < 0).astype(float))).diff().diff().diff()


def f03_tpcl_021_hs_multi_window_consistency_indicator_d3(high: pd.Series) -> pd.Series:
    """Indicator: H&S detected at BOTH 63d AND 126d (rolling 3-peak with mid-peak
    highest). Robust multi-scale confirmation."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _hs(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return 0.0
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = np.sort(idxs[sv])
        heights = vals[sv][np.argsort(idxs[sv])]
        if heights[1] > heights[0] and heights[1] > heights[2]:
            return 1.0
        return 0.0
    a = piv_h.rolling(QDAYS, min_periods=MDAYS).apply(_hs, raw=True)
    b = piv_h.rolling(126, min_periods=QDAYS).apply(_hs, raw=True)
    return (((a > 0) & (b > 0)).astype(float)).diff().diff().diff()


def f03_tpcl_022_hs_neckline_to_close_ratio_252d_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of close to 252d neckline (rolling 252d low). 1.0 = sitting on neckline,
    <1.0 = below neckline (post-completion), >1.0 = above neckline."""
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(close, nl)).diff().diff().diff()


def f03_tpcl_023_twin_peak_asymmetric_right_higher_252d_d3(high: pd.Series) -> pd.Series:
    """Indicator: top-2 pivots present and the chronologically-later peak is higher
    than the earlier. Failed continuation pattern (peak2 > peak1)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _f(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:2]
        pos = idxs[sv]
        ord_ = np.argsort(pos)
        h_chron = vals[sv][ord_]
        return float(1.0 if h_chron[1] > h_chron[0] else 0.0)
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff().diff().diff()


def f03_tpcl_024_double_top_intermediate_higher_low_indicator_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """At a double-top, intermediate trough is HIGHER than prior trough → failed
    continuation setup. Indicator 0/1."""
    piv_h_mask = _pivot_highs_mask(high, k=5)
    piv_l_mask = _pivot_lows_mask(low, k=5)
    piv_h = high.where(piv_h_mask > 0, np.nan)
    piv_l = low.where(piv_l_mask > 0, np.nan)
    def _f(wh, wl):
        mh = ~np.isnan(wh); ml = ~np.isnan(wl)
        if mh.sum() < 2 or ml.sum() < 2:
            return np.nan
        idh = np.where(mh)[0]; vh = wh[mh]
        sv = np.argsort(vh)[::-1][:2]
        pos_h = np.sort(idh[sv])
        idl = np.where(ml)[0]; vl = wl[ml]
        between = (idl > pos_h[0]) & (idl < pos_h[1])
        if not between.any():
            return np.nan
        mid_trough = float(vl[between].min())
        before = idl < pos_h[0]
        if not before.any():
            return np.nan
        prior_trough = float(vl[before].min())
        return float(1.0 if mid_trough > prior_trough else 0.0)
    out = np.full(len(high), np.nan)
    h_v = piv_h.values; l_v = piv_l.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _f(h_v[lo:i + 1], l_v[lo:i + 1])
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_025_double_top_intermediate_lower_low_indicator_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """At a double-top, intermediate trough is LOWER than prior trough → textbook
    completion setup. Indicator 0/1."""
    piv_h_mask = _pivot_highs_mask(high, k=5)
    piv_l_mask = _pivot_lows_mask(low, k=5)
    piv_h = high.where(piv_h_mask > 0, np.nan)
    piv_l = low.where(piv_l_mask > 0, np.nan)
    def _f(wh, wl):
        mh = ~np.isnan(wh); ml = ~np.isnan(wl)
        if mh.sum() < 2 or ml.sum() < 2:
            return np.nan
        idh = np.where(mh)[0]; vh = wh[mh]
        sv = np.argsort(vh)[::-1][:2]
        pos_h = np.sort(idh[sv])
        idl = np.where(ml)[0]; vl = wl[ml]
        between = (idl > pos_h[0]) & (idl < pos_h[1])
        if not between.any():
            return np.nan
        mid_trough = float(vl[between].min())
        before = idl < pos_h[0]
        if not before.any():
            return np.nan
        prior_trough = float(vl[before].min())
        return float(1.0 if mid_trough < prior_trough else 0.0)
    out = np.full(len(high), np.nan)
    h_v = piv_h.values; l_v = piv_l.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _f(h_v[lo:i + 1], l_v[lo:i + 1])
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_026_short_horizon_double_top_peak_spread_21d_d3(high: pd.Series) -> pd.Series:
    """Time-spread (bars) between the top-2 pivot peaks in a 21d window — short-cycle
    double-top spacing (different concept than 1a's 252d top2 separation)."""
    piv_h = high.where(_pivot_highs_mask(high, k=2) > 0, np.nan)
    def _sp(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:2]
        pos = np.sort(idxs[sv])
        return float(pos[1] - pos[0])
    return (piv_h.rolling(MDAYS, min_periods=WDAYS + 4).apply(_sp, raw=True)).diff().diff().diff()


def f03_tpcl_027_double_top_peak_amplitude_symmetry_63d_d3(high: pd.Series) -> pd.Series:
    """Peak-amplitude symmetry score on 63d window: 1 - |P1-P2|/(P1+P2)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _s(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return np.nan
        v = w[mask]
        sv = np.sort(v)[::-1][:2]
        if sv[0] + sv[1] <= 0:
            return np.nan
        return float(1.0 - abs(sv[0] - sv[1]) / (sv[0] + sv[1]))
    return (piv_h.rolling(QDAYS, min_periods=MDAYS).apply(_s, raw=True)).diff().diff().diff()


def f03_tpcl_028_double_top_trough_depth_relative_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth of trough between top-2 peaks relative to peak height — shallow vs deep
    trough quality marker for double-top."""
    out = np.full(len(high), np.nan)
    piv_h_mask = _pivot_highs_mask(high, k=5)
    piv_h = high.where(piv_h_mask > 0, np.nan)
    h_v = piv_h.values; l_v = low.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        wh = h_v[lo:i + 1]; wl = l_v[lo:i + 1]
        mh = ~np.isnan(wh)
        if mh.sum() < 2:
            continue
        idh = np.where(mh)[0]; vh = wh[mh]
        sv = np.argsort(vh)[::-1][:2]
        pos_h = np.sort(idh[sv])
        trough = float(np.nanmin(wl[pos_h[0]:pos_h[1] + 1]))
        peak_avg = float(np.mean(np.sort(vh)[::-1][:2]))
        if peak_avg <= 0:
            continue
        out[i] = (peak_avg - trough) / peak_avg
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_029_double_top_second_peak_volume_divergence_63d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    """At a 63d double-top, ratio of avg-vol near peak2 to avg-vol near peak1.
    <1 = volume divergence at second peak (bearish confirmation)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _f(wh, wv):
        mh = ~np.isnan(wh)
        if mh.sum() < 2:
            return np.nan
        idh = np.where(mh)[0]; vh = wh[mh]
        sv = np.argsort(vh)[::-1][:2]
        pos_h = np.sort(idh[sv])
        p1, p2 = int(pos_h[0]), int(pos_h[1])
        v1 = wv[max(0, p1 - 2):p1 + 3]; v2 = wv[max(0, p2 - 2):p2 + 3]
        if v1.size == 0 or v2.size == 0:
            return np.nan
        m1 = np.nanmean(v1); m2 = np.nanmean(v2)
        if m1 <= 0:
            return np.nan
        return float(m2 / m1)
    out = np.full(len(high), np.nan)
    h_v = piv_h.values; v_v = volume.values
    for i in range(MDAYS, len(high)):
        lo = max(0, i - QDAYS + 1)
        out[i] = _f(h_v[lo:i + 1], v_v[lo:i + 1])
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_030_double_top_first_peak_only_volume_spike_252d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: avg-vol near peak1 > 1.5 * avg-vol near peak2 — first peak had a
    volume spike, second did not (textbook distribution at top)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _f(wh, wv):
        mh = ~np.isnan(wh)
        if mh.sum() < 2:
            return np.nan
        idh = np.where(mh)[0]; vh = wh[mh]
        sv = np.argsort(vh)[::-1][:2]
        pos_h = np.sort(idh[sv])
        p1, p2 = int(pos_h[0]), int(pos_h[1])
        v1 = wv[max(0, p1 - 2):p1 + 3]; v2 = wv[max(0, p2 - 2):p2 + 3]
        if v1.size == 0 or v2.size == 0:
            return np.nan
        m1 = np.nanmean(v1); m2 = np.nanmean(v2)
        if m2 <= 0:
            return np.nan
        return float(1.0 if m1 > 1.5 * m2 else 0.0)
    out = np.full(len(high), np.nan)
    h_v = piv_h.values; v_v = volume.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _f(h_v[lo:i + 1], v_v[lo:i + 1])
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_031_double_top_detected_in_21d_window_d3(high: pd.Series) -> pd.Series:
    """Short-cycle (21d) double-top: top-2 pivots within 3% of each other."""
    piv_h = high.where(_pivot_highs_mask(high, k=2) > 0, np.nan)
    def _f(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return np.nan
        v = w[mask]
        sv = np.sort(v)[::-1][:2]
        if sv[0] <= 0:
            return np.nan
        return float(1.0 if abs(sv[0] - sv[1]) / sv[0] <= 0.03 else 0.0)
    return (piv_h.rolling(MDAYS, min_periods=WDAYS + 4).apply(_f, raw=True)).diff().diff().diff()


def f03_tpcl_032_failed_double_top_breakout_above_252d_d3(high: pd.Series) -> pd.Series:
    """Indicator: after a 252d double-top is in place, price closes above the higher
    of the two peaks — failed double-top (bull-bias). Past-only logic."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _f(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:2]
        pos = np.sort(idxs[sv])
        peak_max = float(np.max(vals[sv]))
        if pos[1] >= len(w) - 1:
            return 0.0
        post = w[pos[1] + 1:]
        if post.size == 0:
            return 0.0
        return float(1.0 if np.nanmax(post) > peak_max else 0.0)
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff().diff().diff()


def f03_tpcl_033_double_top_completion_speed_index_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars from second-peak to neckline tag, divided by typical (21d). Smaller =
    faster completion = stronger pattern."""
    piv_h_mask = _pivot_highs_mask(high, k=5)
    out = np.full(len(high), np.nan)
    h_pv = high.where(piv_h_mask > 0, np.nan).values
    l_v = low.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        wh = h_pv[lo:i + 1]; wl = l_v[lo:i + 1]
        mh = ~np.isnan(wh)
        if mh.sum() < 2:
            continue
        idh = np.where(mh)[0]; vh = wh[mh]
        sv = np.argsort(vh)[::-1][:2]
        pos_h = np.sort(idh[sv])
        trough_pre = float(np.nanmin(wl[pos_h[0]:pos_h[1] + 1])) if pos_h[1] > pos_h[0] else np.nan
        if np.isnan(trough_pre):
            continue
        post = wl[pos_h[1] + 1:]
        if post.size == 0:
            continue
        hit_idx = np.where(post < trough_pre)[0]
        if hit_idx.size == 0:
            continue
        out[i] = float(hit_idx[0] + 1) / float(MDAYS)
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_034_double_top_bullish_failed_pattern_indicator_252d_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bullish-failed double-top: pattern formed but close has recently exceeded the
    higher peak — strong bullish reversal of pattern (opposite of expected)."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rh21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((close >= rh) & (rh21 >= rh)).astype(float).where(close.notna(), np.nan)).diff().diff().diff()


def f03_tpcl_035_triple_top_peak_amplitude_variance_252d_d3(high: pd.Series) -> pd.Series:
    """Variance of the top-3 pivot peaks in 252d — small variance = high quality
    triple-top (peaks at near-equal heights)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _v(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        v = w[mask]
        top3 = np.sort(v)[::-1][:3]
        return float(np.var(top3, ddof=1)) if top3.size > 1 else np.nan
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_v, raw=True)).diff().diff().diff()


def f03_tpcl_036_triple_top_peak_time_consistency_252d_d3(high: pd.Series) -> pd.Series:
    """Time-consistency of triple-top: coefficient-of-variation of inter-peak gaps."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _c(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = np.sort(idxs[sv])
        gaps = np.diff(pos)
        if gaps.mean() == 0:
            return np.nan
        return float(gaps.std(ddof=1) / gaps.mean()) if gaps.size > 1 else np.nan
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_c, raw=True)).diff().diff().diff()


def f03_tpcl_037_triple_top_descending_indicator_252d_d3(high: pd.Series) -> pd.Series:
    """Indicator: top-3 peaks form a strictly descending chronological sequence —
    weakening highs, classic distribution."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _d(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = idxs[sv]
        order = np.argsort(pos)
        h_chron = vals[sv][order]
        return float(1.0 if h_chron[0] > h_chron[1] > h_chron[2] else 0.0)
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_d, raw=True)).diff().diff().diff()


def f03_tpcl_038_triple_top_ascending_indicator_252d_d3(high: pd.Series) -> pd.Series:
    """Indicator: top-3 peaks form a strictly ascending sequence — three-pushes-up,
    Wyckoff-style failure setup."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _a(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = idxs[sv]
        order = np.argsort(pos)
        h_chron = vals[sv][order]
        return float(1.0 if h_chron[0] < h_chron[1] < h_chron[2] else 0.0)
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_a, raw=True)).diff().diff().diff()


def f03_tpcl_039_triple_top_declining_volume_profile_252d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of avg-volume at the top-3 pivots in chronological order — negative =
    classic declining-volume distribution top."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _f(wh, wv):
        mh = ~np.isnan(wh)
        if mh.sum() < 3:
            return np.nan
        idh = np.where(mh)[0]; vh = wh[mh]
        sv = np.argsort(vh)[::-1][:3]
        pos = idh[sv]; order = np.argsort(pos)
        positions = pos[order]
        vols = np.array([np.nanmean(wv[max(0, p - 2):p + 3]) for p in positions])
        x = np.arange(len(vols), dtype=float)
        if vols.std() == 0:
            return 0.0
        xm = x.mean(); vm = vols.mean()
        num = ((x - xm) * (vols - vm)).sum()
        den = ((x - xm) ** 2).sum()
        return float(num / den) if den != 0 else np.nan
    out = np.full(len(high), np.nan)
    h_v = piv_h.values; v_v = volume.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _f(h_v[lo:i + 1], v_v[lo:i + 1])
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_040_triple_top_completion_event_indicator_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: triple-top detected (3 pivots within 3%) AND close has dropped
    below the lowest intervening trough."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    out = np.full(len(high), np.nan)
    h_v = piv_h.values; l_v = low.values; c_v = close.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        wh = h_v[lo:i + 1]; wl = l_v[lo:i + 1]
        mh = ~np.isnan(wh)
        if mh.sum() < 3:
            continue
        idh = np.where(mh)[0]; vh = wh[mh]
        sv = np.argsort(vh)[::-1][:3]
        peaks = vh[sv]
        pos = np.sort(idh[sv])
        if peaks.max() <= 0:
            continue
        if (peaks.max() - peaks.min()) / peaks.max() > 0.03:
            continue
        seg = wl[pos[0]:pos[-1] + 1]
        if seg.size == 0:
            continue
        pat_low = float(np.nanmin(seg))
        out[i] = float(1.0 if c_v[i] < pat_low else 0.0)
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_041_quadruple_top_detection_indicator_252d_d3(high: pd.Series) -> pd.Series:
    """Rare 4-peak top: 4 pivots within 3% of each other in 252d window."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _f(w):
        mask = ~np.isnan(w)
        if mask.sum() < 4:
            return np.nan
        v = w[mask]
        top4 = np.sort(v)[::-1][:4]
        if top4.max() <= 0:
            return np.nan
        return float(1.0 if (top4.max() - top4.min()) / top4.max() <= 0.03 else 0.0)
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff().diff().diff()


def f03_tpcl_042_multi_peak_at_near_equal_level_count_252d_d3(high: pd.Series) -> pd.Series:
    """Count of pivot-highs within 2% of the 252d max. High count = robust
    resistance / multi-touch top."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _f(w):
        mask = ~np.isnan(w)
        if mask.sum() < 1:
            return np.nan
        v = w[mask]
        mx = v.max()
        if mx <= 0:
            return np.nan
        return float((v >= 0.98 * mx).sum())
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff().diff().diff()


def f03_tpcl_043_broadening_top_5point_reversal_indicator_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-point broadening reversal: 3 higher highs and 2 lower lows alternating."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    piv_l = low.where(_pivot_lows_mask(low, k=5) > 0, np.nan)
    out = np.full(len(high), np.nan)
    hv = piv_h.values; lv = piv_l.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        wh = hv[lo:i + 1]; wl = lv[lo:i + 1]
        mh = ~np.isnan(wh); ml = ~np.isnan(wl)
        if mh.sum() < 3 or ml.sum() < 2:
            continue
        ih = np.where(mh)[0]; vh = wh[mh]
        il = np.where(ml)[0]; vl = wl[ml]
        if vh.size < 3 or vl.size < 2:
            continue
        last3_h = vh[-3:]; last2_l = vl[-2:]
        cond_h = last3_h[0] < last3_h[1] < last3_h[2]
        cond_l = last2_l[0] > last2_l[1]
        out[i] = float(1.0 if cond_h and cond_l else 0.0)
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_044_inverted_broadening_bottom_failed_at_top_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inverted broadening bottom showing up at the top (failed bullish broadening):
    3 lower lows + 2 higher highs alternating — indicates broadening pattern in
    'wrong' orientation at price highs (unusual top configuration)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    piv_l = low.where(_pivot_lows_mask(low, k=5) > 0, np.nan)
    out = np.full(len(high), np.nan)
    hv = piv_h.values; lv = piv_l.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        wh = hv[lo:i + 1]; wl = lv[lo:i + 1]
        mh = ~np.isnan(wh); ml = ~np.isnan(wl)
        if mh.sum() < 2 or ml.sum() < 3:
            continue
        vh = wh[mh]; vl = wl[ml]
        if vh.size < 2 or vl.size < 3:
            continue
        last2_h = vh[-2:]; last3_l = vl[-3:]
        cond_h = last2_h[0] < last2_h[1]
        cond_l = last3_l[0] > last3_l[1] > last3_l[2]
        out[i] = float(1.0 if cond_h and cond_l else 0.0)
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_045_megaphone_descending_lower_bound_slope_252d_d3(low: pd.Series) -> pd.Series:
    """Slope of the regression line through 252d pivot-lows — negative slope = the
    lower bound of a megaphone is descending (broadening pattern)."""
    return (_rolling_slope(low.where(_pivot_lows_mask(low, k=5) > 0, np.nan), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f03_tpcl_046_megaphone_ascending_upper_bound_slope_252d_d3(high: pd.Series) -> pd.Series:
    """Slope of the regression line through 252d pivot-highs — positive slope = the
    upper bound of a megaphone is ascending."""
    return (_rolling_slope(high.where(_pivot_highs_mask(high, k=5) > 0, np.nan), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f03_tpcl_047_diamond_top_broaden_then_narrow_score_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Diamond pattern score: range expands in first-half then narrows in second-half.
    Score = (first-half-range-slope > 0) AND (second-half-range-slope < 0)."""
    rng = high - low
    def _d(w):
        if np.isnan(w).any():
            return np.nan
        half = len(w) // 2
        if half < 5:
            return np.nan
        x1 = np.arange(half, dtype=float); y1 = w[:half]
        x2 = np.arange(len(w) - half, dtype=float); y2 = w[half:]
        s1 = np.polyfit(x1, y1, 1)[0]
        s2 = np.polyfit(x2, y2, 1)[0]
        return float(1.0 if (s1 > 0 and s2 < 0) else 0.0)
    return (rng.rolling(YDAYS, min_periods=QDAYS).apply(_d, raw=True)).diff().diff().diff()


def f03_tpcl_048_diamond_top_time_symmetry_index_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """For windows where range expands then contracts, time of peak-range divided
    by total window length; 0.5 = perfectly symmetric diamond."""
    rng = high - low
    def _ts(w):
        if np.isnan(w).any():
            return np.nan
        idx = int(np.argmax(w))
        n = len(w)
        if n <= 1:
            return np.nan
        sym = 1.0 - abs(idx / (n - 1) - 0.5) * 2.0
        return float(sym)
    return (rng.rolling(YDAYS, min_periods=QDAYS).apply(_ts, raw=True)).diff().diff().diff()


def f03_tpcl_049_broadening_apex_distance_to_current_bar_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """For broadening pattern (upper line rising, lower line falling), the apex is
    BEHIND the current bar at increasing distance — proxied by ratio of last-bar
    range to mean range earlier."""
    rng = (high - low).rolling(WDAYS, min_periods=2).mean()
    base = (high - low).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(rng, base) - 1.0).diff().diff().diff()


def f03_tpcl_050_broadening_pattern_amplitude_volatility_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of bar-range over 252d normalised by mean — broadening shows increasing
    amplitude volatility."""
    rng = high - low
    sd = rng.rolling(YDAYS, min_periods=QDAYS).std()
    mn = rng.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(sd, mn)).diff().diff().diff()


def f03_tpcl_051_broadening_volume_increase_with_range_252d_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation of (high-low) bar-range with volume in 252d — positive =
    broadening accompanied by rising volume (capitulation broadening)."""
    rng = high - low
    def _c(w_r, w_v):
        if np.isnan(w_r).any() or np.isnan(w_v).any():
            return np.nan
        if w_r.std() == 0 or w_v.std() == 0:
            return np.nan
        return float(np.corrcoef(w_r, w_v)[0, 1])
    out = np.full(len(high), np.nan)
    r_v = rng.values; v_v = volume.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _c(r_v[lo:i + 1], v_v[lo:i + 1])
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_052_pre_broadening_compression_indicator_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: trailing 21d range is in bottom-25% of 252d range distribution,
    while recent 21d is in top-25% — pre-broadening compression-then-expansion."""
    rng = high - low
    short_avg = rng.rolling(MDAYS, min_periods=WDAYS).mean()
    full_avg = rng.rolling(YDAYS, min_periods=QDAYS).mean()
    q25 = rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    q75 = rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    early_compressed = (rng.shift(MDAYS) <= q25.shift(MDAYS)).astype(float)
    now_expanded = (short_avg >= q75).astype(float)
    return (((early_compressed > 0) & (now_expanded > 0)).astype(float).where(full_avg.notna(), np.nan)).diff().diff().diff()


def f03_tpcl_053_desc_triangle_flat_bottom_slope_tolerance_252d_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """How "flat" the 252d-low regression is: |slope|/close. Small value = textbook
    flat-bottom descending triangle support."""
    sl = _rolling_slope(low, YDAYS, min_periods=QDAYS).abs()
    return (_safe_div(sl, close)).diff().diff().diff()


def f03_tpcl_054_desc_triangle_apex_bars_to_apex_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars to projected apex where upper (declining highs) line meets lower (flat
    lows) line — closer apex = pattern near resolution."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    intercept_h = high - sl_h * (YDAYS - 1)
    flat = low.rolling(YDAYS, min_periods=QDAYS).min()
    bars_to = _safe_div(flat - intercept_h, sl_h)
    return (bars_to.where(sl_h < 0, np.nan)).diff().diff().diff()


def f03_tpcl_055_desc_triangle_volume_trend_signature_252d_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume slope inside descending triangle. Classic signature is declining
    volume into the apex."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS).abs()
    in_dt = (sl_h < 0) & (sl_l / (sl_h.abs() + 1e-12) < 0.2)
    sl_v = _rolling_slope(volume, YDAYS, min_periods=QDAYS)
    return (sl_v.where(in_dt, np.nan)).diff().diff().diff()


def f03_tpcl_056_falling_wedge_bullish_vs_bearish_context_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Falling wedge (both highs and lows falling, highs faster): -1 if formed
    inside a downtrend (bullish), +1 if formed at top (bearish failure variant)."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    sl_c = _rolling_slope(close, DDAYS_2Y, min_periods=YDAYS)
    in_wedge = (sl_h < 0) & (sl_l < 0) & (sl_h < sl_l)
    sign = np.where(sl_c > 0, 1.0, np.where(sl_c < 0, -1.0, 0.0))
    return (pd.Series(sign, index=high.index).where(in_wedge, np.nan)).diff().diff().diff()


def f03_tpcl_057_wedge_convergence_angle_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Wedge convergence: |slope_high - slope_low|. Sharp wedge has large value,
    gentle wedge small."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    return ((sl_h - sl_l).abs()).diff().diff().diff()


def f03_tpcl_058_wedge_breakout_direction_indicator_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For a converging wedge (positive convergence rate), +1 if close broke above
    the upper line, -1 if below lower line, 0 inside."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    in_wedge = (sl_h - sl_l).abs() > 0
    direction = np.where(close > rh, 1.0, np.where(close < rl, -1.0, 0.0))
    return (pd.Series(direction, index=high.index).where(in_wedge, np.nan)).diff().diff().diff()


def f03_tpcl_059_wedge_volume_contraction_during_formation_252d_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Inside-wedge volume slope (should be negative for textbook wedge formation)."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    sl_v = _rolling_slope(volume, YDAYS, min_periods=QDAYS)
    in_wedge = (sl_h - sl_l).abs() > 0
    return (sl_v.where(in_wedge, np.nan)).diff().diff().diff()


def f03_tpcl_060_wedge_upper_bound_slope_alone_252d_d3(high: pd.Series) -> pd.Series:
    """Upper bound (highs) slope of wedge — magnitude of compression on the upper side."""
    return (_rolling_slope(high, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f03_tpcl_061_wedge_throwback_to_upper_line_event_252d_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: prior bar closed above 252d-upper-trendline (proxied by 252d
    max), today closed back below — throwback to upper line."""
    sma = high.rolling(YDAYS, min_periods=QDAYS).max()
    above_prev = close.shift(1) > sma.shift(1)
    below_now = close < sma
    return ((above_prev & below_now).astype(float).where(sma.notna(), np.nan)).diff().diff().diff()


def f03_tpcl_062_wedge_resolution_bars_to_break_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the wedge formed (proxied by convergence rate exceeded zero) and
    a directional break (close outside 252d range) occurred. Lower = faster
    resolution."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    in_wedge = (sl_h - sl_l).abs() > 0
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    broken = (close > rh) | (close < rl)
    enter = in_wedge & ~in_wedge.shift(1, fill_value=False)
    # cumulative bars since enter
    grp = enter.cumsum()
    bars_since = grp.groupby(grp).cumcount().astype(float)
    return (bars_since.where(in_wedge & broken, np.nan)).diff().diff().diff()


def f03_tpcl_063_rising_wedge_bearish_reversal_score_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Rising wedge score: both highs and lows ascending, lows faster than highs
    (converging upward). Higher value = sharper wedge — reversal-prone."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    score = (sl_l - sl_h)
    in_pat = (sl_h > 0) & (sl_l > 0)
    return (score.where(in_pat & (score > 0), np.nan)).diff().diff().diff()


def f03_tpcl_064_rising_wedge_convergence_rate_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Rate at which the rising-wedge bands are converging (ratio of slopes)."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    in_pat = (sl_h > 0) & (sl_l > 0) & (sl_l > sl_h)
    return (_safe_div(sl_l - sl_h, sl_l.abs() + sl_h.abs()).where(in_pat, np.nan)).diff().diff().diff()


def f03_tpcl_065_rising_wedge_with_declining_momentum_signature_63d_d3(close: pd.Series) -> pd.Series:
    """Inside a 63d rising-wedge (close-slope > 0), momentum (1-period return) slope
    is negative — divergence between price and momentum."""
    sl_c = _rolling_slope(close, QDAYS, min_periods=MDAYS)
    ret = close.pct_change()
    sl_r = _rolling_slope(ret, QDAYS, min_periods=MDAYS)
    in_w = sl_c > 0
    return (sl_r.where(in_w & (sl_r < 0), np.nan)).diff().diff().diff()


def f03_tpcl_066_bear_flag_at_top_continuation_failure_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bear flag failure: short-term up-channel inside a down-trend, but the flag
    breaks UP instead of continuing DOWN. Indicator 0/1."""
    sl_long = _rolling_slope(close, QDAYS, min_periods=MDAYS)
    sl_short = _rolling_slope(close, WDAYS, min_periods=2)
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((sl_long < 0) & (sl_short > 0) & (close >= rh)).astype(float).where(close.notna(), np.nan)).diff().diff().diff()


def f03_tpcl_067_bear_pennant_at_top_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bear pennant (small symmetric triangle inside a downtrend) score: range
    contraction in last 21d inside a prior 63d downtrend."""
    rng = high - low
    short_rng = rng.rolling(MDAYS, min_periods=WDAYS).mean()
    long_rng = rng.rolling(QDAYS, min_periods=MDAYS).mean()
    sl_c = _rolling_slope((high + low) / 2.0, QDAYS, min_periods=MDAYS)
    contraction = _safe_div(short_rng, long_rng) - 1.0
    return ((-contraction).where((sl_c < 0), np.nan)).diff().diff().diff()


def f03_tpcl_068_bear_rectangle_at_top_sideways_consolidation_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bear rectangle: prior downtrend, then sideways consolidation defined as
    63d std-of-close / mean-of-close below threshold."""
    mid = (high + low) / 2.0
    sl = _rolling_slope(mid, QDAYS, min_periods=MDAYS)
    cv = mid.rolling(QDAYS, min_periods=MDAYS).std() / mid.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    return (cv.where(sl < 0, np.nan)).diff().diff().diff()


def f03_tpcl_069_rising_channel_break_down_event_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: in a 252d rising channel (both highs and lows up-sloping), close
    has broken below the 21d lower-bound (channel bottom)."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    rl = low.rolling(MDAYS, min_periods=WDAYS).min()
    in_chan = (sl_h > 0) & (sl_l > 0)
    return (((close < rl) & in_chan).astype(float).where(close.notna(), np.nan)).diff().diff().diff()


def f03_tpcl_070_steep_rising_channel_slope_per_atr_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 252d close-regression normalised by ATR — steep rising channel has
    high value (>2 = parabolic-like ascent)."""
    sl = _rolling_slope(close, YDAYS, min_periods=QDAYS)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(sl, atr)).diff().diff().diff()


def f03_tpcl_071_channel_break_magnitude_relative_to_channel_height_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Break-magnitude (distance from close to 252d-low) divided by channel height
    (252d-high minus 252d-low). >0.5 = significant break."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    height = rh - rl
    break_amount = rl - close
    return (_safe_div(break_amount, height)).diff().diff().diff()


def f03_tpcl_072_failed_rising_wedge_broke_up_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: rising-wedge in place (highs and lows up, converging) AND close has
    broken ABOVE the upper bound (failed bearish wedge)."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    in_w = (sl_h > 0) & (sl_l > 0) & (sl_l > sl_h)
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((close > rh) & in_w).astype(float).where(close.notna(), np.nan)).diff().diff().diff()


def f03_tpcl_073_diamond_top_peak_detection_indicator_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Diamond detected: range expands in first half, contracts in second half,
    AND the maximum-range bar occurs at the midpoint (within +/-10% of center)."""
    rng = high - low
    def _f(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w)
        if n < 30:
            return np.nan
        idx_max = int(np.argmax(w))
        mid_dist = abs(idx_max / (n - 1) - 0.5)
        if mid_dist > 0.1:
            return 0.0
        h1, h2 = n // 2, n - n // 2
        s1 = np.polyfit(np.arange(h1), w[:h1], 1)[0]
        s2 = np.polyfit(np.arange(h2), w[h1:], 1)[0]
        return float(1.0 if (s1 > 0 and s2 < 0) else 0.0)
    return (rng.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff().diff().diff()


def f03_tpcl_074_diamond_top_symmetry_score_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Diamond shape symmetry: correlation between first-half-range and
    reversed-second-half-range. 1.0 = perfectly symmetric diamond."""
    rng = high - low
    def _f(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w)
        h = n // 2
        if h < 5:
            return np.nan
        left = w[:h]
        right = w[-h:][::-1]
        if left.std() == 0 or right.std() == 0:
            return np.nan
        return float(np.corrcoef(left, right)[0, 1])
    return (rng.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff().diff().diff()


def f03_tpcl_075_diamond_top_duration_relative_typical_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars from start-of-expansion (first range > 21d-mean*1.2) to
    end-of-contraction (last bar with range < 21d-mean*0.8) within 252d, divided
    by 126 (typical diamond duration)."""
    rng = high - low
    base = rng.rolling(MDAYS, min_periods=WDAYS).mean()
    expanded = rng > 1.2 * base
    contracted = rng < 0.8 * base
    def _f(we, wc):
        idx_e = np.where(we > 0)[0]
        idx_c = np.where(wc > 0)[0]
        if idx_e.size == 0 or idx_c.size == 0:
            return np.nan
        start = idx_e[0]
        end_candidates = idx_c[idx_c > start]
        if end_candidates.size == 0:
            return np.nan
        return float(end_candidates[-1] - start) / 126.0
    out = np.full(len(high), np.nan)
    ev = expanded.astype(float).values
    cv = contracted.astype(float).values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _f(ev[lo:i + 1], cv[lo:i + 1])
    return (pd.Series(out, index=high.index)).diff().diff().diff()


TOPPING_PATTERN_CLASSICAL_D3_REGISTRY_001_075 = {
    "f03_tpcl_001_complex_hs_shoulder_count_252d_d3": {"inputs": ["high"], "func": f03_tpcl_001_complex_hs_shoulder_count_252d_d3},
    "f03_tpcl_002_inverse_symmetric_hs_top_mirror_score_252d_d3": {"inputs": ["high"], "func": f03_tpcl_002_inverse_symmetric_hs_top_mirror_score_252d_d3},
    "f03_tpcl_003_hs_neckline_slope_sign_indicator_252d_d3": {"inputs": ["low"], "func": f03_tpcl_003_hs_neckline_slope_sign_indicator_252d_d3},
    "f03_tpcl_004_hs_neckline_downslope_strength_252d_d3": {"inputs": ["low", "close"], "func": f03_tpcl_004_hs_neckline_downslope_strength_252d_d3},
    "f03_tpcl_005_hs_head_to_shoulders_height_ratio_252d_d3": {"inputs": ["high"], "func": f03_tpcl_005_hs_head_to_shoulders_height_ratio_252d_d3},
    "f03_tpcl_006_hs_shoulder_time_symmetry_index_252d_d3": {"inputs": ["high"], "func": f03_tpcl_006_hs_shoulder_time_symmetry_index_252d_d3},
    "f03_tpcl_007_hs_shoulder_amplitude_symmetry_252d_d3": {"inputs": ["high"], "func": f03_tpcl_007_hs_shoulder_amplitude_symmetry_252d_d3},
    "f03_tpcl_008_hs_head_to_neckline_depth_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_008_hs_head_to_neckline_depth_252d_d3},
    "f03_tpcl_009_hs_volume_decline_LtoR_signature_252d_d3": {"inputs": ["high", "volume"], "func": f03_tpcl_009_hs_volume_decline_LtoR_signature_252d_d3},
    "f03_tpcl_010_hs_target_to_actual_move_ratio_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_010_hs_target_to_actual_move_ratio_252d_d3},
    "f03_tpcl_011_hs_formation_duration_relative_252d_d3": {"inputs": ["high"], "func": f03_tpcl_011_hs_formation_duration_relative_252d_d3},
    "f03_tpcl_012_hs_multi_scale_concurrent_overlap_count_d3": {"inputs": ["high"], "func": f03_tpcl_012_hs_multi_scale_concurrent_overlap_count_d3},
    "f03_tpcl_013_hs_left_shoulder_to_head_bars_252d_d3": {"inputs": ["high"], "func": f03_tpcl_013_hs_left_shoulder_to_head_bars_252d_d3},
    "f03_tpcl_014_hs_head_to_right_shoulder_bars_252d_d3": {"inputs": ["high"], "func": f03_tpcl_014_hs_head_to_right_shoulder_bars_252d_d3},
    "f03_tpcl_015_hs_time_symmetry_ratio_norm_252d_d3": {"inputs": ["high"], "func": f03_tpcl_015_hs_time_symmetry_ratio_norm_252d_d3},
    "f03_tpcl_016_hs_neckline_angle_in_radians_252d_d3": {"inputs": ["low", "close"], "func": f03_tpcl_016_hs_neckline_angle_in_radians_252d_d3},
    "f03_tpcl_017_hs_distance_to_neckline_atr_norm_d3": {"inputs": ["low", "high", "close"], "func": f03_tpcl_017_hs_distance_to_neckline_atr_norm_d3},
    "f03_tpcl_018_hs_completion_percentage_estimate_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_018_hs_completion_percentage_estimate_252d_d3},
    "f03_tpcl_019_hs_bars_since_right_shoulder_pivot_252d_d3": {"inputs": ["high"], "func": f03_tpcl_019_hs_bars_since_right_shoulder_pivot_252d_d3},
    "f03_tpcl_020_hs_recognition_confidence_score_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_020_hs_recognition_confidence_score_252d_d3},
    "f03_tpcl_021_hs_multi_window_consistency_indicator_d3": {"inputs": ["high"], "func": f03_tpcl_021_hs_multi_window_consistency_indicator_d3},
    "f03_tpcl_022_hs_neckline_to_close_ratio_252d_d3": {"inputs": ["low", "close"], "func": f03_tpcl_022_hs_neckline_to_close_ratio_252d_d3},
    "f03_tpcl_023_twin_peak_asymmetric_right_higher_252d_d3": {"inputs": ["high"], "func": f03_tpcl_023_twin_peak_asymmetric_right_higher_252d_d3},
    "f03_tpcl_024_double_top_intermediate_higher_low_indicator_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_024_double_top_intermediate_higher_low_indicator_252d_d3},
    "f03_tpcl_025_double_top_intermediate_lower_low_indicator_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_025_double_top_intermediate_lower_low_indicator_252d_d3},
    "f03_tpcl_026_short_horizon_double_top_peak_spread_21d_d3": {"inputs": ["high"], "func": f03_tpcl_026_short_horizon_double_top_peak_spread_21d_d3},
    "f03_tpcl_027_double_top_peak_amplitude_symmetry_63d_d3": {"inputs": ["high"], "func": f03_tpcl_027_double_top_peak_amplitude_symmetry_63d_d3},
    "f03_tpcl_028_double_top_trough_depth_relative_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_028_double_top_trough_depth_relative_252d_d3},
    "f03_tpcl_029_double_top_second_peak_volume_divergence_63d_d3": {"inputs": ["high", "volume"], "func": f03_tpcl_029_double_top_second_peak_volume_divergence_63d_d3},
    "f03_tpcl_030_double_top_first_peak_only_volume_spike_252d_d3": {"inputs": ["high", "volume"], "func": f03_tpcl_030_double_top_first_peak_only_volume_spike_252d_d3},
    "f03_tpcl_031_double_top_detected_in_21d_window_d3": {"inputs": ["high"], "func": f03_tpcl_031_double_top_detected_in_21d_window_d3},
    "f03_tpcl_032_failed_double_top_breakout_above_252d_d3": {"inputs": ["high"], "func": f03_tpcl_032_failed_double_top_breakout_above_252d_d3},
    "f03_tpcl_033_double_top_completion_speed_index_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_033_double_top_completion_speed_index_252d_d3},
    "f03_tpcl_034_double_top_bullish_failed_pattern_indicator_252d_d3": {"inputs": ["high", "close"], "func": f03_tpcl_034_double_top_bullish_failed_pattern_indicator_252d_d3},
    "f03_tpcl_035_triple_top_peak_amplitude_variance_252d_d3": {"inputs": ["high"], "func": f03_tpcl_035_triple_top_peak_amplitude_variance_252d_d3},
    "f03_tpcl_036_triple_top_peak_time_consistency_252d_d3": {"inputs": ["high"], "func": f03_tpcl_036_triple_top_peak_time_consistency_252d_d3},
    "f03_tpcl_037_triple_top_descending_indicator_252d_d3": {"inputs": ["high"], "func": f03_tpcl_037_triple_top_descending_indicator_252d_d3},
    "f03_tpcl_038_triple_top_ascending_indicator_252d_d3": {"inputs": ["high"], "func": f03_tpcl_038_triple_top_ascending_indicator_252d_d3},
    "f03_tpcl_039_triple_top_declining_volume_profile_252d_d3": {"inputs": ["high", "volume"], "func": f03_tpcl_039_triple_top_declining_volume_profile_252d_d3},
    "f03_tpcl_040_triple_top_completion_event_indicator_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_040_triple_top_completion_event_indicator_252d_d3},
    "f03_tpcl_041_quadruple_top_detection_indicator_252d_d3": {"inputs": ["high"], "func": f03_tpcl_041_quadruple_top_detection_indicator_252d_d3},
    "f03_tpcl_042_multi_peak_at_near_equal_level_count_252d_d3": {"inputs": ["high"], "func": f03_tpcl_042_multi_peak_at_near_equal_level_count_252d_d3},
    "f03_tpcl_043_broadening_top_5point_reversal_indicator_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_043_broadening_top_5point_reversal_indicator_252d_d3},
    "f03_tpcl_044_inverted_broadening_bottom_failed_at_top_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_044_inverted_broadening_bottom_failed_at_top_252d_d3},
    "f03_tpcl_045_megaphone_descending_lower_bound_slope_252d_d3": {"inputs": ["low"], "func": f03_tpcl_045_megaphone_descending_lower_bound_slope_252d_d3},
    "f03_tpcl_046_megaphone_ascending_upper_bound_slope_252d_d3": {"inputs": ["high"], "func": f03_tpcl_046_megaphone_ascending_upper_bound_slope_252d_d3},
    "f03_tpcl_047_diamond_top_broaden_then_narrow_score_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_047_diamond_top_broaden_then_narrow_score_252d_d3},
    "f03_tpcl_048_diamond_top_time_symmetry_index_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_048_diamond_top_time_symmetry_index_252d_d3},
    "f03_tpcl_049_broadening_apex_distance_to_current_bar_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_049_broadening_apex_distance_to_current_bar_252d_d3},
    "f03_tpcl_050_broadening_pattern_amplitude_volatility_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_050_broadening_pattern_amplitude_volatility_252d_d3},
    "f03_tpcl_051_broadening_volume_increase_with_range_252d_d3": {"inputs": ["high", "low", "volume"], "func": f03_tpcl_051_broadening_volume_increase_with_range_252d_d3},
    "f03_tpcl_052_pre_broadening_compression_indicator_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_052_pre_broadening_compression_indicator_252d_d3},
    "f03_tpcl_053_desc_triangle_flat_bottom_slope_tolerance_252d_d3": {"inputs": ["low", "close"], "func": f03_tpcl_053_desc_triangle_flat_bottom_slope_tolerance_252d_d3},
    "f03_tpcl_054_desc_triangle_apex_bars_to_apex_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_054_desc_triangle_apex_bars_to_apex_252d_d3},
    "f03_tpcl_055_desc_triangle_volume_trend_signature_252d_d3": {"inputs": ["high", "low", "volume"], "func": f03_tpcl_055_desc_triangle_volume_trend_signature_252d_d3},
    "f03_tpcl_056_falling_wedge_bullish_vs_bearish_context_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_056_falling_wedge_bullish_vs_bearish_context_252d_d3},
    "f03_tpcl_057_wedge_convergence_angle_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_057_wedge_convergence_angle_252d_d3},
    "f03_tpcl_058_wedge_breakout_direction_indicator_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_058_wedge_breakout_direction_indicator_252d_d3},
    "f03_tpcl_059_wedge_volume_contraction_during_formation_252d_d3": {"inputs": ["high", "low", "volume"], "func": f03_tpcl_059_wedge_volume_contraction_during_formation_252d_d3},
    "f03_tpcl_060_wedge_upper_bound_slope_alone_252d_d3": {"inputs": ["high"], "func": f03_tpcl_060_wedge_upper_bound_slope_alone_252d_d3},
    "f03_tpcl_061_wedge_throwback_to_upper_line_event_252d_d3": {"inputs": ["high", "close"], "func": f03_tpcl_061_wedge_throwback_to_upper_line_event_252d_d3},
    "f03_tpcl_062_wedge_resolution_bars_to_break_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_062_wedge_resolution_bars_to_break_252d_d3},
    "f03_tpcl_063_rising_wedge_bearish_reversal_score_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_063_rising_wedge_bearish_reversal_score_252d_d3},
    "f03_tpcl_064_rising_wedge_convergence_rate_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_064_rising_wedge_convergence_rate_252d_d3},
    "f03_tpcl_065_rising_wedge_with_declining_momentum_signature_63d_d3": {"inputs": ["close"], "func": f03_tpcl_065_rising_wedge_with_declining_momentum_signature_63d_d3},
    "f03_tpcl_066_bear_flag_at_top_continuation_failure_63d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_066_bear_flag_at_top_continuation_failure_63d_d3},
    "f03_tpcl_067_bear_pennant_at_top_63d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_067_bear_pennant_at_top_63d_d3},
    "f03_tpcl_068_bear_rectangle_at_top_sideways_consolidation_63d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_068_bear_rectangle_at_top_sideways_consolidation_63d_d3},
    "f03_tpcl_069_rising_channel_break_down_event_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_069_rising_channel_break_down_event_252d_d3},
    "f03_tpcl_070_steep_rising_channel_slope_per_atr_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_070_steep_rising_channel_slope_per_atr_252d_d3},
    "f03_tpcl_071_channel_break_magnitude_relative_to_channel_height_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_071_channel_break_magnitude_relative_to_channel_height_252d_d3},
    "f03_tpcl_072_failed_rising_wedge_broke_up_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_072_failed_rising_wedge_broke_up_252d_d3},
    "f03_tpcl_073_diamond_top_peak_detection_indicator_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_073_diamond_top_peak_detection_indicator_252d_d3},
    "f03_tpcl_074_diamond_top_symmetry_score_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_074_diamond_top_symmetry_score_252d_d3},
    "f03_tpcl_075_diamond_top_duration_relative_typical_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_075_diamond_top_duration_relative_typical_252d_d3},
}
