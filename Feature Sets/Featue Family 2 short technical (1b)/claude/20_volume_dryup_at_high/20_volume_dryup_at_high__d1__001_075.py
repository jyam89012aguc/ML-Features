"""volume_dryup_at_high d1 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across base__001_075 and base__076_150. Each feature
encodes a *different concept* in the volume-dryup-at-high theme: declining
participation while price sits near multi-year extremes — z-score / dispersion /
entropy / regime / compound-state / decay.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
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


# ---------------------------- family helpers ----------------------------

def _robust_zscore_mad(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    mad = (s - med).abs().rolling(window, min_periods=min_periods).median()
    return _safe_div(s - med, 1.4826 * mad)


def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _rolling_entropy_bins(s, window, bins=10, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 2, 5)
    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < min_periods:
            return np.nan
        lo = v.min(); hi = v.max()
        if hi <= lo:
            return 0.0
        edges = np.linspace(lo, hi, bins + 1)
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return s.rolling(window, min_periods=min_periods).apply(_ent, raw=True)


def _rolling_hurst(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 2, 20)
    def _h(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < min_periods:
            return np.nan
        lags = [2, 4, 8, 16, 32]
        lags = [l for l in lags if l < n // 2]
        if len(lags) < 2:
            return np.nan
        tau = []
        for lag in lags:
            d = v[lag:] - v[:-lag]
            sd = d.std()
            if sd <= 0 or not np.isfinite(sd):
                return np.nan
            tau.append(sd)
        try:
            return float(np.polyfit(np.log(lags), np.log(tau), 1)[0])
        except Exception:
            return np.nan
    return s.rolling(window, min_periods=min_periods).apply(_h, raw=True)


def _rolling_dfa_alpha(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 2, 32)
    def _dfa(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < min_periods:
            return np.nan
        y = np.cumsum(v - v.mean())
        scales = [4, 8, 16, 32, 64]
        scales = [s for s in scales if s <= n // 4]
        if len(scales) < 2:
            return np.nan
        F = []
        for sc in scales:
            nb = n // sc
            if nb < 1:
                return np.nan
            seg = y[: nb * sc].reshape(nb, sc)
            x = np.arange(sc, dtype=float)
            xm = x.mean()
            dx = x - xm
            denom = (dx * dx).sum()
            fluct = []
            for i in range(nb):
                ym = seg[i].mean()
                slope = ((dx * (seg[i] - ym)).sum()) / denom if denom > 0 else 0.0
                resid = seg[i] - (ym + slope * dx)
                fluct.append((resid * resid).mean())
            F.append(np.sqrt(np.mean(fluct)))
        try:
            return float(np.polyfit(np.log(scales), np.log(F), 1)[0])
        except Exception:
            return np.nan
    return s.rolling(window, min_periods=min_periods).apply(_dfa, raw=True)


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    """For each bar, length of trailing consecutive-True streak ending at that bar."""
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _rolling_corr(a, b, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 5)
    return a.rolling(window, min_periods=min_periods).corr(b)


def _rolling_autocorr(s, lag, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, lag + 3)
    return s.rolling(window, min_periods=min_periods).apply(
        lambda w: _np_autocorr_lag(w, lag), raw=True
    )


def _np_autocorr_lag(w, lag):
    v = w[~np.isnan(w)]
    if v.size < lag + 3:
        return np.nan
    a = v[:-lag] - v[:-lag].mean()
    b = v[lag:] - v[lag:].mean()
    den = np.sqrt((a * a).sum() * (b * b).sum())
    if den <= 0:
        return np.nan
    return float((a * b).sum() / den)


# ============================================================
# Bucket A — Volume z-score regimes (001-008)
# ============================================================

def f20_vdah_001_log_vol_zscore_252d_d1(volume: pd.Series) -> pd.Series:
    """Log-volume z-score vs 252d rolling — annual participation regime."""
    lv = _safe_log(volume)
    return (_rolling_zscore(lv, YDAYS)).diff()


def f20_vdah_002_log_vol_zscore_63d_d1(volume: pd.Series) -> pd.Series:
    """Log-volume z-score vs 63d rolling — quarterly regime shift."""
    lv = _safe_log(volume)
    return (_rolling_zscore(lv, QDAYS)).diff()


def f20_vdah_003_log_vol_zscore_504d_d1(volume: pd.Series) -> pd.Series:
    """Log-volume z-score vs 504d rolling — biennial structural extreme."""
    lv = _safe_log(volume)
    return (_rolling_zscore(lv, DDAYS_2Y)).diff()


def f20_vdah_004_log_vol_robust_mad_z_252d_d1(volume: pd.Series) -> pd.Series:
    """Robust (median/MAD) z-score of log-volume over 252d."""
    return (_robust_zscore_mad(_safe_log(volume), YDAYS)).diff()


def f20_vdah_005_log_vol_robust_mad_z_63d_d1(volume: pd.Series) -> pd.Series:
    """Robust (median/MAD) z-score of log-volume over 63d."""
    return (_robust_zscore_mad(_safe_log(volume), QDAYS)).diff()


def f20_vdah_006_log_vol_pct_rank_252d_d1(volume: pd.Series) -> pd.Series:
    """Percentile rank of current log-vol in trailing 252d distribution."""
    return (_rolling_pct_rank(_safe_log(volume), YDAYS)).diff()


def f20_vdah_007_log_vol_pct_rank_504d_d1(volume: pd.Series) -> pd.Series:
    """Percentile rank of current log-vol in trailing 504d distribution."""
    return (_rolling_pct_rank(_safe_log(volume), DDAYS_2Y)).diff()


def f20_vdah_008_log_vol_pct_rank_63d_d1(volume: pd.Series) -> pd.Series:
    """Percentile rank of current log-vol in trailing 63d distribution."""
    return (_rolling_pct_rank(_safe_log(volume), QDAYS)).diff()


# ============================================================
# Bucket B — Volume / N-day reference ratios (009-014)
# ============================================================

def f20_vdah_009_vol_ratio_to_median_252d_d1(volume: pd.Series) -> pd.Series:
    """Current volume divided by 252d trailing median — relative regime."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(volume, med)).diff()


def f20_vdah_010_vol_ratio_to_median_63d_d1(volume: pd.Series) -> pd.Series:
    """Current volume divided by 63d trailing median — short-term regime."""
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    return (_safe_div(volume, med)).diff()


def f20_vdah_011_vol_ratio_to_trimmed_mean_252d_d1(volume: pd.Series) -> pd.Series:
    """Current volume divided by 10-90 trimmed mean over 252d — outlier-robust regime."""
    def _trimmean(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        lo = np.quantile(v, 0.10); hi = np.quantile(v, 0.90)
        m = v[(v >= lo) & (v <= hi)]
        return m.mean() if m.size > 0 else np.nan
    tm = volume.rolling(YDAYS, min_periods=QDAYS).apply(_trimmean, raw=True)
    return (_safe_div(volume, tm)).diff()


def f20_vdah_012_vol_ratio_to_geomean_252d_d1(volume: pd.Series) -> pd.Series:
    """Current volume divided by geometric mean over 252d."""
    lv = _safe_log(volume)
    gm = np.exp(lv.rolling(YDAYS, min_periods=QDAYS).mean())
    return (_safe_div(volume, gm)).diff()


def f20_vdah_013_vol_ratio_to_min21d_in_252d_d1(volume: pd.Series) -> pd.Series:
    """Current volume divided by 21d-rolling-minimum's trailing 252d minimum-of-minimums."""
    rmin = volume.rolling(MDAYS, min_periods=WDAYS).min()
    base = rmin.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(volume, base)).diff()


def f20_vdah_014_log_vol_minus_median_log_vol_252d_d1(volume: pd.Series) -> pd.Series:
    """Log-volume minus rolling-median log-volume over 252d — log-distance from median."""
    lv = _safe_log(volume)
    med = lv.rolling(YDAYS, min_periods=QDAYS).median()
    return (lv - med).diff()


# ============================================================
# Bucket C — Compound state: low vol while at high (015-024)
# ============================================================

def f20_vdah_015_low_vol_at_252d_high_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close in top 5% of 252d range AND volume below 252d median, else 0."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    top5 = pos >= 0.95
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    lowv = volume < med
    return ((top5 & lowv).astype(float)).diff()


def f20_vdah_016_below_q20_vol_at_252d_high_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close in top decile of 252d range AND volume below 20% quantile of 252d, else 0."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    top10 = pos >= 0.90
    q20 = _rolling_quantile(volume, YDAYS, 0.20)
    lowv = volume <= q20
    return ((top10 & lowv).astype(float)).diff()


def f20_vdah_017_log_vol_zscore_in_top_decile_range_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-vol z-score (252d) but masked to bars when close is in top decile of 252d range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return (z.where(pos >= 0.90, np.nan)).diff()


def f20_vdah_018_log_vol_pct_rank_in_top_decile_range_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-vol pct rank (252d) masked to bars when close is in top decile of 252d range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    pr = _rolling_pct_rank(_safe_log(volume), YDAYS)
    return (pr.where(pos >= 0.90, np.nan)).diff()


def f20_vdah_019_vol_quintile_x_price_quintile_score_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite score: (price_quintile_252d) - (vol_quintile_252d). High = high price, low vol."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    p_q = (pos * 5.0).clip(upper=4.999).fillna(np.nan)
    v_rank = _rolling_pct_rank(volume, YDAYS)
    v_q = (v_rank * 5.0).clip(upper=4.999)
    return (p_q - v_q).diff()


def f20_vdah_020_vol_to_med252_gated_top_decile_range_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol/median252 ratio gated to bars when close is in top decile of 252d range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    ratio = _safe_div(volume, med)
    return (ratio.where(pos >= 0.90, np.nan)).diff()


def f20_vdah_021_count_low_vol_days_in_21d_at_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d count of bars where close in top decile of 252d range AND vol < 252d median."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((pos >= 0.90) & (volume < med)).astype(float)
    return (flag.rolling(MDAYS, min_periods=WDAYS).sum()).diff()


def f20_vdah_022_count_low_vol_days_in_63d_at_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars where close in top decile of 252d range AND vol < 252d median."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((pos >= 0.90) & (volume < med)).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f20_vdah_023_fraction_low_vol_days_in_63d_at_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d fraction of bars where close in top decile of 252d range AND vol < 252d median."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((pos >= 0.90) & (volume < med)).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f20_vdah_024_streak_below_med_vol_at_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak satisfying: close in top decile of 252d range AND vol < med252."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    cond = (pos >= 0.90) & (volume < med)
    return (_consecutive_true_streak(cond).astype(float)).diff()


# ============================================================
# Bucket D — Streak / persistence (025-030)
# ============================================================

def f20_vdah_025_streak_below_median_vol_21d_d1(volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with vol < 21d trailing median — short-term thinning."""
    med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return (_consecutive_true_streak(volume < med).astype(float)).diff()


def f20_vdah_026_streak_below_median_vol_63d_d1(volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with vol < 63d trailing median — quarterly thinning."""
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    return (_consecutive_true_streak(volume < med).astype(float)).diff()


def f20_vdah_027_streak_below_q25_vol_63d_d1(volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with vol below 25%-quantile over trailing 63d."""
    q = _rolling_quantile(volume, QDAYS, 0.25)
    return (_consecutive_true_streak(volume <= q).astype(float)).diff()


def f20_vdah_028_count_below_median_runs_252d_d1(volume: pd.Series) -> pd.Series:
    """Number of distinct below-median-vol runs in trailing 252d window."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (volume < med).astype(int)
    # Count run starts: 1 where flag becomes 1 from 0
    starts = (flag.diff().fillna(flag.iloc[0] if len(flag) > 0 else 0) == 1).astype(float)
    return (starts.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f20_vdah_029_max_run_length_below_median_vol_252d_d1(volume: pd.Series) -> pd.Series:
    """Max consecutive-bar below-median-vol run length in trailing 252d."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    streak = _consecutive_true_streak(volume < med).astype(float)
    return (streak.rolling(YDAYS, min_periods=QDAYS).max()).diff()


def f20_vdah_030_avg_run_length_below_median_vol_252d_d1(volume: pd.Series) -> pd.Series:
    """Mean consecutive-bar below-median-vol run length in trailing 252d (non-zero bars only)."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    streak = _consecutive_true_streak(volume < med).astype(float)
    masked = streak.where(streak > 0, np.nan)
    return (masked.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


# ============================================================
# Bucket E — Entropy collapse (031-036)
# ============================================================

def f20_vdah_031_shannon_entropy_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Rolling Shannon entropy of binned log-volume over 252d — high entropy = diverse participation."""
    return (_rolling_entropy_bins(_safe_log(volume), YDAYS, bins=10)).diff()


def f20_vdah_032_shannon_entropy_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Rolling Shannon entropy of binned log-volume over 63d — short-term diversity."""
    return (_rolling_entropy_bins(_safe_log(volume), QDAYS, bins=8)).diff()


def f20_vdah_033_entropy_collapse_63_minus_252_d1(volume: pd.Series) -> pd.Series:
    """Entropy(63d) minus entropy(252d) — negative = short-term collapse vs long-term."""
    e63 = _rolling_entropy_bins(_safe_log(volume), QDAYS, bins=8)
    e252 = _rolling_entropy_bins(_safe_log(volume), YDAYS, bins=10)
    return (e63 - e252).diff()


def f20_vdah_034_perm_entropy_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Permutation entropy (order-3) of log-volume over 63d — ordinal-pattern diversity."""
    lv = _safe_log(volume)
    def _pe(w):
        v = w[~np.isnan(w)]
        if v.size < 12:
            return np.nan
        order = 3
        n = v.size - order + 1
        patterns = {}
        for i in range(n):
            pat = tuple(np.argsort(v[i:i+order]))
            patterns[pat] = patterns.get(pat, 0) + 1
        total = sum(patterns.values())
        p = np.array(list(patterns.values()), dtype=float) / total
        return float(-(p * np.log(p)).sum())
    return (lv.rolling(QDAYS, min_periods=MDAYS).apply(_pe, raw=True)).diff()


def f20_vdah_035_approx_entropy_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Approximate entropy (m=2, r=0.2*sd) on log-vol over 63d — regularity proxy."""
    lv = _safe_log(volume)
    def _apen(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 15:
            return np.nan
        m = 2
        r = 0.2 * np.std(v)
        if r <= 0:
            return np.nan
        def phi(mm):
            xs = np.array([v[i:i+mm] for i in range(n - mm + 1)])
            C = []
            for x in xs:
                d = np.max(np.abs(xs - x), axis=1)
                C.append(np.sum(d <= r) / (n - mm + 1))
            C = np.array(C)
            C = C[C > 0]
            if C.size == 0:
                return np.nan
            return float(np.mean(np.log(C)))
        p1 = phi(m); p2 = phi(m + 1)
        if np.isnan(p1) or np.isnan(p2):
            return np.nan
        return float(p1 - p2)
    return (lv.rolling(QDAYS, min_periods=MDAYS).apply(_apen, raw=True)).diff()


def f20_vdah_036_perm_entropy_change_63_minus_252_d1(volume: pd.Series) -> pd.Series:
    """Permutation entropy(63d) minus permutation entropy(252d) — short collapse vs long baseline."""
    lv = _safe_log(volume)
    def _pe(w, order=3):
        v = w[~np.isnan(w)]
        if v.size < 4 * order:
            return np.nan
        n = v.size - order + 1
        patterns = {}
        for i in range(n):
            pat = tuple(np.argsort(v[i:i+order]))
            patterns[pat] = patterns.get(pat, 0) + 1
        total = sum(patterns.values())
        p = np.array(list(patterns.values()), dtype=float) / total
        return float(-(p * np.log(p)).sum())
    e63 = lv.rolling(QDAYS, min_periods=MDAYS).apply(_pe, raw=True)
    e252 = lv.rolling(YDAYS, min_periods=QDAYS).apply(_pe, raw=True)
    return (e63 - e252).diff()


# ============================================================
# Bucket F — Dispersion collapse (037-044)
# ============================================================

def f20_vdah_037_std_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Rolling std of log-volume over 252d — annual participation dispersion."""
    return (_safe_log(volume).rolling(YDAYS, min_periods=QDAYS).std()).diff()


def f20_vdah_038_std_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Rolling std of log-volume over 63d — quarterly dispersion."""
    return (_safe_log(volume).rolling(QDAYS, min_periods=MDAYS).std()).diff()


def f20_vdah_039_iqr_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Rolling inter-quartile range of log-volume over 252d."""
    lv = _safe_log(volume)
    q75 = _rolling_quantile(lv, YDAYS, 0.75)
    q25 = _rolling_quantile(lv, YDAYS, 0.25)
    return (q75 - q25).diff()


def f20_vdah_040_iqr_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Rolling inter-quartile range of log-volume over 63d."""
    lv = _safe_log(volume)
    q75 = _rolling_quantile(lv, QDAYS, 0.75)
    q25 = _rolling_quantile(lv, QDAYS, 0.25)
    return (q75 - q25).diff()


def f20_vdah_041_mad_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Rolling median absolute deviation of log-volume over 252d."""
    lv = _safe_log(volume)
    med = lv.rolling(YDAYS, min_periods=QDAYS).median()
    return ((lv - med).abs().rolling(YDAYS, min_periods=QDAYS).median()).diff()


def f20_vdah_042_ratio_std_logvol_63_to_252_d1(volume: pd.Series) -> pd.Series:
    """Ratio of 63d std to 252d std of log-volume — <1 = recent dispersion has collapsed."""
    lv = _safe_log(volume)
    s63 = lv.rolling(QDAYS, min_periods=MDAYS).std()
    s252 = lv.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(s63, s252)).diff()


def f20_vdah_043_cv_vol_252d_d1(volume: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of raw volume over 252d."""
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(sd, m)).diff()


def f20_vdah_044_range_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Max minus min of log-volume over 63d window."""
    lv = _safe_log(volume)
    return (lv.rolling(QDAYS, min_periods=MDAYS).max() - lv.rolling(QDAYS, min_periods=MDAYS).min()).diff()


# ============================================================
# Bucket G — Participation thinning (045-050)
# ============================================================

def f20_vdah_045_frac_below_med252_in_63d_d1(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63d bars with volume below 252d trailing median."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (volume < med).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f20_vdah_046_frac_below_q20_252_in_63d_d1(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63d bars with volume below 20%-quantile over trailing 252d."""
    q = _rolling_quantile(volume, YDAYS, 0.20)
    flag = (volume <= q).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f20_vdah_047_frac_above_med_in_63d_d1(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63d bars with volume above 252d trailing median — inverse participation."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (volume > med).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f20_vdah_048_count_logvol_below_m1sigma_63d_d1(volume: pd.Series) -> pd.Series:
    """Trailing-63d count of bars with log-vol z (vs 252d) below -1."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return ((z < -1.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f20_vdah_049_count_logvol_below_m2sigma_63d_d1(volume: pd.Series) -> pd.Series:
    """Trailing-63d count of bars with log-vol z (vs 252d) below -2 — extreme thinning."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return ((z < -2.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f20_vdah_050_tail_asymmetry_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Fraction of 63d bars with logvol below -1 sigma minus fraction above +1 sigma — left-tail dominance."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    left = (z < -1.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    right = (z > 1.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    return (left - right).diff()


# ============================================================
# Bucket H — Dryup after climax (051-060)
# ============================================================

def f20_vdah_051_bars_since_252d_vol_peak_d1(volume: pd.Series) -> pd.Series:
    """Trailing 252d bars-since-volume-peak (0 at peak, increasing each bar away)."""
    def _bsp(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        idx = int(np.argmax(w))
        return float(len(w) - 1 - idx)
    return (volume.rolling(YDAYS, min_periods=QDAYS).apply(_bsp, raw=True)).diff()


def f20_vdah_052_vol_decay_ratio_since_252d_peak_d1(volume: pd.Series) -> pd.Series:
    """Current volume / 252d trailing-max volume — fraction-of-peak (post-climax decay)."""
    rmax = volume.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(volume, rmax)).diff()


def f20_vdah_053_vol_slope_post_252d_peak_21d_d1(volume: pd.Series) -> pd.Series:
    """Rolling 21d slope of log-volume, masked to bars in the trailing 21 days after a 252d-vol-peak event."""
    rmax = volume.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = volume >= rmax
    peak_age = (~is_peak).astype(int)
    peak_age = peak_age.groupby((is_peak).cumsum()).cumsum()
    slope = _rolling_slope(_safe_log(volume), MDAYS)
    return (slope.where(peak_age <= MDAYS, np.nan)).diff()


def f20_vdah_054_half_life_vol_decay_after_252d_peak_d1(volume: pd.Series) -> pd.Series:
    """Estimated half-life (in days) for volume decay since most recent 252d peak."""
    rmax = volume.rolling(YDAYS, min_periods=QDAYS).max()
    def _hl(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak) or peak <= 0:
            return np.nan
        target = peak / 2.0
        for j in range(peak_idx + 1, len(w)):
            if not np.isnan(w[j]) and w[j] <= target:
                return float(j - peak_idx)
        return float(len(w) - peak_idx)
    return (volume.rolling(YDAYS, min_periods=QDAYS).apply(_hl, raw=True)).diff()


def f20_vdah_055_cum_post_peak_vol_deficit_252d_d1(volume: pd.Series) -> pd.Series:
    """Sum of (peak - vol) over the trailing window since the 252d peak — cumulative volume deficit."""
    def _cd(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak):
            return np.nan
        seg = w[peak_idx + 1 :]
        seg = seg[~np.isnan(seg)]
        return float(np.sum(peak - seg))
    return (volume.rolling(YDAYS, min_periods=QDAYS).apply(_cd, raw=True)).diff()


def f20_vdah_056_bars_since_63d_vol_peak_d1(volume: pd.Series) -> pd.Series:
    """Trailing 63d bars-since-volume-peak."""
    def _bsp(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        idx = int(np.argmax(w))
        return float(len(w) - 1 - idx)
    return (volume.rolling(QDAYS, min_periods=MDAYS).apply(_bsp, raw=True)).diff()


def f20_vdah_057_vol_decay_ratio_since_63d_peak_d1(volume: pd.Series) -> pd.Series:
    """Current volume / 63d trailing-max volume."""
    rmax = volume.rolling(QDAYS, min_periods=MDAYS).max()
    return (_safe_div(volume, rmax)).diff()


def f20_vdah_058_post_peak_vol_to_pre_peak_med_ratio_d1(volume: pd.Series) -> pd.Series:
    """Current vol / pre-peak median over the trailing 252d (how much below the 'normal' pre-peak baseline)."""
    def _r(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        peak_idx = int(np.argmax(w))
        pre = w[:peak_idx]
        pre = pre[~np.isnan(pre)]
        if pre.size < 10:
            return np.nan
        base = np.median(pre)
        cur = w[-1]
        if not np.isfinite(cur) or base <= 0:
            return np.nan
        return float(cur / base)
    return (volume.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True)).diff()


def f20_vdah_059_max_consec_below_pre_peak_median_after_peak_d1(volume: pd.Series) -> pd.Series:
    """Max consecutive-bar run length where post-peak vol stays below pre-peak median, in 252d window."""
    def _mc(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        peak_idx = int(np.argmax(w))
        pre = w[:peak_idx]
        pre = pre[~np.isnan(pre)]
        if pre.size < 10:
            return np.nan
        thresh = np.median(pre)
        seg = w[peak_idx + 1 :]
        if seg.size == 0:
            return 0.0
        best = cur = 0
        for x in seg:
            if not np.isnan(x) and x < thresh:
                cur += 1; best = max(best, cur)
            else:
                cur = 0
        return float(best)
    return (volume.rolling(YDAYS, min_periods=QDAYS).apply(_mc, raw=True)).diff()


def f20_vdah_060_vol_recovery_failure_indicator_252d_d1(volume: pd.Series) -> pd.Series:
    """1 if since the 252d-peak, vol has not returned to within 50% of the peak, else 0."""
    def _vrf(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak) or peak <= 0:
            return np.nan
        seg = w[peak_idx + 1 :]
        seg = seg[~np.isnan(seg)]
        if seg.size == 0:
            return 0.0
        return 1.0 if seg.max() < 0.5 * peak else 0.0
    return (volume.rolling(YDAYS, min_periods=QDAYS).apply(_vrf, raw=True)).diff()


# ============================================================
# Bucket I — No-supply bars (wide range, thin volume) (061-066)
# ============================================================

def f20_vdah_061_ratio_truerange_to_log_vol_63d_mean_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 63d of (true_range / log_volume) — range per unit log-vol; high = range without supply."""
    tr = _true_range(high, low, close)
    ratio = _safe_div(tr, _safe_log(volume))
    return (ratio.rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f20_vdah_062_count_wide_range_low_vol_bars_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d count of bars where true_range > 1.5*ATR21 AND vol < 252d median."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((tr > 1.5 * atr) & (volume < med)).astype(float)
    return (flag.rolling(MDAYS, min_periods=WDAYS).sum()).diff()


def f20_vdah_063_count_wide_range_low_vol_bars_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d count of bars where true_range > 1.5*ATR21 AND vol < 252d median."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((tr > 1.5 * atr) & (volume < med)).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f20_vdah_064_streak_wide_range_low_vol_at_high_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current streak of consecutive bars with wide-range and below-median vol AND close in top decile of 252d range."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    cond = (tr > 1.5 * atr) & (volume < med) & (pos >= 0.90)
    return (_consecutive_true_streak(cond).astype(float)).diff()


def f20_vdah_065_range_to_vol_zscore_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (252d) of (true_range / log_volume) — range-per-supply extreme."""
    tr = _true_range(high, low, close)
    ratio = _safe_div(tr, _safe_log(volume))
    return (_rolling_zscore(ratio, YDAYS)).diff()


def f20_vdah_066_range_per_log_vol_252d_mean_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 252d of (true_range / log_volume) — long-term range-per-supply baseline."""
    tr = _true_range(high, low, close)
    ratio = _safe_div(tr, _safe_log(volume))
    return (ratio.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


# ============================================================
# Bucket J — Breakout-on-no-volume (anti-confirmation) (067-072)
# ============================================================

def f20_vdah_067_new_252d_high_with_below_med_vol_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when current high is the 252d-trailing max AND volume below 252d median, else 0."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_new = high >= rmax
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((is_new & (volume < med)).astype(float)).diff()


def f20_vdah_068_count_new_21d_high_low_vol_63d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing-63d count of bars that print a new 21d high with vol below 63d median."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_new = high >= rmax21
    med63 = volume.rolling(QDAYS, min_periods=MDAYS).median()
    flag = (is_new & (volume < med63)).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f20_vdah_069_count_new_63d_high_low_vol_252d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing-252d count of bars that print a new 63d high with vol below 252d median."""
    rmax63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    is_new = high >= rmax63
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (is_new & (volume < med)).astype(float)
    return (flag.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f20_vdah_070_frac_new_252d_high_low_vol_in_252d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Of all 252d-high-print bars in trailing 252d, fraction that occurred with vol below 252d median."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_new = (high >= rmax).astype(float)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    lowflag = ((high >= rmax) & (volume < med)).astype(float)
    n_new = is_new.rolling(YDAYS, min_periods=QDAYS).sum()
    n_low = lowflag.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(n_low, n_new)).diff()


def f20_vdah_071_mean_log_vol_zscore_on_new_252d_high_bars_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing-252d mean of log-vol z-score on bars that printed a new 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_new = high >= rmax
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    z_on = z.where(is_new, np.nan)
    return (z_on.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f20_vdah_072_max_low_vol_new_high_streak_252d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar run length of new-21d-high + below-median-vol bars in 252d."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    cond = (high >= rmax) & (volume < med)
    streak = _consecutive_true_streak(cond).astype(float)
    return (streak.rolling(YDAYS, min_periods=QDAYS).max()).diff()


# ============================================================
# Bucket K — Hurst / DFA on log-vol (073-075)
# ============================================================

def f20_vdah_073_hurst_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Rolling Hurst exponent of log-volume over 252d — persistence of vol regime."""
    return (_rolling_hurst(_safe_log(volume), YDAYS)).diff()


def f20_vdah_074_hurst_logvol_504d_d1(volume: pd.Series) -> pd.Series:
    """Rolling Hurst exponent of log-volume over 504d — long-horizon persistence."""
    return (_rolling_hurst(_safe_log(volume), DDAYS_2Y)).diff()


def f20_vdah_075_dfa_alpha_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Detrended-fluctuation-analysis alpha exponent of log-vol over 252d."""
    return (_rolling_dfa_alpha(_safe_log(volume), YDAYS)).diff()


# ============================================================
#                         REGISTRY 001-075
# ============================================================

VOLUME_DRYUP_AT_HIGH_D1_REGISTRY_001_075 = {
    "f20_vdah_001_log_vol_zscore_252d_d1": {"inputs": ["volume"], "func": f20_vdah_001_log_vol_zscore_252d_d1},
    "f20_vdah_002_log_vol_zscore_63d_d1": {"inputs": ["volume"], "func": f20_vdah_002_log_vol_zscore_63d_d1},
    "f20_vdah_003_log_vol_zscore_504d_d1": {"inputs": ["volume"], "func": f20_vdah_003_log_vol_zscore_504d_d1},
    "f20_vdah_004_log_vol_robust_mad_z_252d_d1": {"inputs": ["volume"], "func": f20_vdah_004_log_vol_robust_mad_z_252d_d1},
    "f20_vdah_005_log_vol_robust_mad_z_63d_d1": {"inputs": ["volume"], "func": f20_vdah_005_log_vol_robust_mad_z_63d_d1},
    "f20_vdah_006_log_vol_pct_rank_252d_d1": {"inputs": ["volume"], "func": f20_vdah_006_log_vol_pct_rank_252d_d1},
    "f20_vdah_007_log_vol_pct_rank_504d_d1": {"inputs": ["volume"], "func": f20_vdah_007_log_vol_pct_rank_504d_d1},
    "f20_vdah_008_log_vol_pct_rank_63d_d1": {"inputs": ["volume"], "func": f20_vdah_008_log_vol_pct_rank_63d_d1},
    "f20_vdah_009_vol_ratio_to_median_252d_d1": {"inputs": ["volume"], "func": f20_vdah_009_vol_ratio_to_median_252d_d1},
    "f20_vdah_010_vol_ratio_to_median_63d_d1": {"inputs": ["volume"], "func": f20_vdah_010_vol_ratio_to_median_63d_d1},
    "f20_vdah_011_vol_ratio_to_trimmed_mean_252d_d1": {"inputs": ["volume"], "func": f20_vdah_011_vol_ratio_to_trimmed_mean_252d_d1},
    "f20_vdah_012_vol_ratio_to_geomean_252d_d1": {"inputs": ["volume"], "func": f20_vdah_012_vol_ratio_to_geomean_252d_d1},
    "f20_vdah_013_vol_ratio_to_min21d_in_252d_d1": {"inputs": ["volume"], "func": f20_vdah_013_vol_ratio_to_min21d_in_252d_d1},
    "f20_vdah_014_log_vol_minus_median_log_vol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_014_log_vol_minus_median_log_vol_252d_d1},
    "f20_vdah_015_low_vol_at_252d_high_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_015_low_vol_at_252d_high_indicator_d1},
    "f20_vdah_016_below_q20_vol_at_252d_high_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_016_below_q20_vol_at_252d_high_indicator_d1},
    "f20_vdah_017_log_vol_zscore_in_top_decile_range_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_017_log_vol_zscore_in_top_decile_range_d1},
    "f20_vdah_018_log_vol_pct_rank_in_top_decile_range_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_018_log_vol_pct_rank_in_top_decile_range_d1},
    "f20_vdah_019_vol_quintile_x_price_quintile_score_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_019_vol_quintile_x_price_quintile_score_d1},
    "f20_vdah_020_vol_to_med252_gated_top_decile_range_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_020_vol_to_med252_gated_top_decile_range_d1},
    "f20_vdah_021_count_low_vol_days_in_21d_at_252d_high_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_021_count_low_vol_days_in_21d_at_252d_high_d1},
    "f20_vdah_022_count_low_vol_days_in_63d_at_252d_high_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_022_count_low_vol_days_in_63d_at_252d_high_d1},
    "f20_vdah_023_fraction_low_vol_days_in_63d_at_252d_high_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_023_fraction_low_vol_days_in_63d_at_252d_high_d1},
    "f20_vdah_024_streak_below_med_vol_at_252d_high_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_024_streak_below_med_vol_at_252d_high_d1},
    "f20_vdah_025_streak_below_median_vol_21d_d1": {"inputs": ["volume"], "func": f20_vdah_025_streak_below_median_vol_21d_d1},
    "f20_vdah_026_streak_below_median_vol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_026_streak_below_median_vol_63d_d1},
    "f20_vdah_027_streak_below_q25_vol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_027_streak_below_q25_vol_63d_d1},
    "f20_vdah_028_count_below_median_runs_252d_d1": {"inputs": ["volume"], "func": f20_vdah_028_count_below_median_runs_252d_d1},
    "f20_vdah_029_max_run_length_below_median_vol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_029_max_run_length_below_median_vol_252d_d1},
    "f20_vdah_030_avg_run_length_below_median_vol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_030_avg_run_length_below_median_vol_252d_d1},
    "f20_vdah_031_shannon_entropy_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_031_shannon_entropy_logvol_252d_d1},
    "f20_vdah_032_shannon_entropy_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_032_shannon_entropy_logvol_63d_d1},
    "f20_vdah_033_entropy_collapse_63_minus_252_d1": {"inputs": ["volume"], "func": f20_vdah_033_entropy_collapse_63_minus_252_d1},
    "f20_vdah_034_perm_entropy_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_034_perm_entropy_logvol_63d_d1},
    "f20_vdah_035_approx_entropy_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_035_approx_entropy_logvol_63d_d1},
    "f20_vdah_036_perm_entropy_change_63_minus_252_d1": {"inputs": ["volume"], "func": f20_vdah_036_perm_entropy_change_63_minus_252_d1},
    "f20_vdah_037_std_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_037_std_logvol_252d_d1},
    "f20_vdah_038_std_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_038_std_logvol_63d_d1},
    "f20_vdah_039_iqr_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_039_iqr_logvol_252d_d1},
    "f20_vdah_040_iqr_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_040_iqr_logvol_63d_d1},
    "f20_vdah_041_mad_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_041_mad_logvol_252d_d1},
    "f20_vdah_042_ratio_std_logvol_63_to_252_d1": {"inputs": ["volume"], "func": f20_vdah_042_ratio_std_logvol_63_to_252_d1},
    "f20_vdah_043_cv_vol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_043_cv_vol_252d_d1},
    "f20_vdah_044_range_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_044_range_logvol_63d_d1},
    "f20_vdah_045_frac_below_med252_in_63d_d1": {"inputs": ["volume"], "func": f20_vdah_045_frac_below_med252_in_63d_d1},
    "f20_vdah_046_frac_below_q20_252_in_63d_d1": {"inputs": ["volume"], "func": f20_vdah_046_frac_below_q20_252_in_63d_d1},
    "f20_vdah_047_frac_above_med_in_63d_d1": {"inputs": ["volume"], "func": f20_vdah_047_frac_above_med_in_63d_d1},
    "f20_vdah_048_count_logvol_below_m1sigma_63d_d1": {"inputs": ["volume"], "func": f20_vdah_048_count_logvol_below_m1sigma_63d_d1},
    "f20_vdah_049_count_logvol_below_m2sigma_63d_d1": {"inputs": ["volume"], "func": f20_vdah_049_count_logvol_below_m2sigma_63d_d1},
    "f20_vdah_050_tail_asymmetry_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_050_tail_asymmetry_logvol_63d_d1},
    "f20_vdah_051_bars_since_252d_vol_peak_d1": {"inputs": ["volume"], "func": f20_vdah_051_bars_since_252d_vol_peak_d1},
    "f20_vdah_052_vol_decay_ratio_since_252d_peak_d1": {"inputs": ["volume"], "func": f20_vdah_052_vol_decay_ratio_since_252d_peak_d1},
    "f20_vdah_053_vol_slope_post_252d_peak_21d_d1": {"inputs": ["volume"], "func": f20_vdah_053_vol_slope_post_252d_peak_21d_d1},
    "f20_vdah_054_half_life_vol_decay_after_252d_peak_d1": {"inputs": ["volume"], "func": f20_vdah_054_half_life_vol_decay_after_252d_peak_d1},
    "f20_vdah_055_cum_post_peak_vol_deficit_252d_d1": {"inputs": ["volume"], "func": f20_vdah_055_cum_post_peak_vol_deficit_252d_d1},
    "f20_vdah_056_bars_since_63d_vol_peak_d1": {"inputs": ["volume"], "func": f20_vdah_056_bars_since_63d_vol_peak_d1},
    "f20_vdah_057_vol_decay_ratio_since_63d_peak_d1": {"inputs": ["volume"], "func": f20_vdah_057_vol_decay_ratio_since_63d_peak_d1},
    "f20_vdah_058_post_peak_vol_to_pre_peak_med_ratio_d1": {"inputs": ["volume"], "func": f20_vdah_058_post_peak_vol_to_pre_peak_med_ratio_d1},
    "f20_vdah_059_max_consec_below_pre_peak_median_after_peak_d1": {"inputs": ["volume"], "func": f20_vdah_059_max_consec_below_pre_peak_median_after_peak_d1},
    "f20_vdah_060_vol_recovery_failure_indicator_252d_d1": {"inputs": ["volume"], "func": f20_vdah_060_vol_recovery_failure_indicator_252d_d1},
    "f20_vdah_061_ratio_truerange_to_log_vol_63d_mean_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_061_ratio_truerange_to_log_vol_63d_mean_d1},
    "f20_vdah_062_count_wide_range_low_vol_bars_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_062_count_wide_range_low_vol_bars_21d_d1},
    "f20_vdah_063_count_wide_range_low_vol_bars_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_063_count_wide_range_low_vol_bars_63d_d1},
    "f20_vdah_064_streak_wide_range_low_vol_at_high_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_064_streak_wide_range_low_vol_at_high_d1},
    "f20_vdah_065_range_to_vol_zscore_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_065_range_to_vol_zscore_252d_d1},
    "f20_vdah_066_range_per_log_vol_252d_mean_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_066_range_per_log_vol_252d_mean_d1},
    "f20_vdah_067_new_252d_high_with_below_med_vol_d1": {"inputs": ["high", "volume"], "func": f20_vdah_067_new_252d_high_with_below_med_vol_d1},
    "f20_vdah_068_count_new_21d_high_low_vol_63d_d1": {"inputs": ["high", "volume"], "func": f20_vdah_068_count_new_21d_high_low_vol_63d_d1},
    "f20_vdah_069_count_new_63d_high_low_vol_252d_d1": {"inputs": ["high", "volume"], "func": f20_vdah_069_count_new_63d_high_low_vol_252d_d1},
    "f20_vdah_070_frac_new_252d_high_low_vol_in_252d_d1": {"inputs": ["high", "volume"], "func": f20_vdah_070_frac_new_252d_high_low_vol_in_252d_d1},
    "f20_vdah_071_mean_log_vol_zscore_on_new_252d_high_bars_d1": {"inputs": ["high", "volume"], "func": f20_vdah_071_mean_log_vol_zscore_on_new_252d_high_bars_d1},
    "f20_vdah_072_max_low_vol_new_high_streak_252d_d1": {"inputs": ["high", "volume"], "func": f20_vdah_072_max_low_vol_new_high_streak_252d_d1},
    "f20_vdah_073_hurst_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_073_hurst_logvol_252d_d1},
    "f20_vdah_074_hurst_logvol_504d_d1": {"inputs": ["volume"], "func": f20_vdah_074_hurst_logvol_504d_d1},
    "f20_vdah_075_dfa_alpha_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_075_dfa_alpha_logvol_252d_d1},
}
