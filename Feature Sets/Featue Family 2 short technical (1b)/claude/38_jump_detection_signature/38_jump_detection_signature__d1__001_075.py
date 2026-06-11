"""jump_detection_signature d1 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each feature
encodes a *different concept* in the jump-detection theme: threshold counts,
asymmetric jumps, conditional magnitudes, clustering, statistical jump tests,
gap-vs-intraday decomposition, tail-shape descriptors, jump-volume coupling.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). All sigma estimates used inside jump-event
indicators are constructed from a strictly prior window. Self-contained helpers
— no cross-family imports.
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


def _log_ret(close):
    return _safe_log(close).diff()


def _sigma_prior(r, n):
    """Rolling std of returns, shifted by 1 → strictly causal (excludes day t)."""
    return r.rolling(n, min_periods=max(n // 3, 2)).std().shift(1)


def _mad_prior(r, n):
    """Rolling MAD of returns, shifted by 1 → strictly causal."""
    med = r.rolling(n, min_periods=max(n // 3, 2)).median()
    return (r - med).abs().rolling(n, min_periods=max(n // 3, 2)).median().shift(1)


# ============================================================
# Bucket A — Threshold-count families (001-012)
# Each cell = a distinct timescale + threshold concept
# ============================================================

def f38_jpdt_001_count_abs_ret_above_3sig_21d(close: pd.Series) -> pd.Series:
    """Fresh-shock count: |log-ret| > 3·σ_prior21 events in last 21 bars."""
    r = _log_ret(close)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return jump.rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_002_count_abs_ret_above_4sig_63d(close: pd.Series) -> pd.Series:
    """Intermediate-tail count: |log-ret| > 4·σ_prior63 in last 63 bars."""
    r = _log_ret(close)
    jump = (r.abs() > 4 * _sigma_prior(r, QDAYS)).astype(float)
    return jump.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_003_count_abs_ret_above_5sig_252d(close: pd.Series) -> pd.Series:
    """Annual extreme-tail count: |log-ret| > 5·σ_prior252 in last 252 bars."""
    r = _log_ret(close)
    jump = (r.abs() > 5 * _sigma_prior(r, YDAYS)).astype(float)
    return jump.rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_004_count_abs_ret_above_2sig_5d(close: pd.Series) -> pd.Series:
    """Weekly micro-shock count: |log-ret| > 2·σ_prior5 in last 5 bars."""
    r = _log_ret(close)
    jump = (r.abs() > 2 * _sigma_prior(r, WDAYS)).astype(float)
    return jump.rolling(WDAYS, min_periods=2).sum()


def f38_jpdt_005_count_abs_ret_above_6sig_504d(close: pd.Series) -> pd.Series:
    """Biennial true-outlier count: |log-ret| > 6·σ_prior504 in last 504 bars."""
    r = _log_ret(close)
    jump = (r.abs() > 6 * _sigma_prior(r, DDAYS_2Y)).astype(float)
    return jump.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f38_jpdt_006_singlebar_5sig_252d_prior_indicator(close: pd.Series) -> pd.Series:
    """Today's bar exceeds 5·σ_prior252 → causal Lee-Mykland-style single-bar flag."""
    r = _log_ret(close)
    return (r.abs() > 5 * _sigma_prior(r, YDAYS)).astype(float)


def f38_jpdt_007_singlebar_8sig_504d_prior_indicator(close: pd.Series) -> pd.Series:
    """Today's bar exceeds 8·σ_prior504 → biennial extreme-shock single-bar flag."""
    r = _log_ret(close)
    return (r.abs() > 8 * _sigma_prior(r, DDAYS_2Y)).astype(float)


def f38_jpdt_008_jump_density_3sig_21d(close: pd.Series) -> pd.Series:
    """Density (mean indicator) of |log-ret|>3·σ_prior21 over the trailing 21d window."""
    r = _log_ret(close)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return jump.rolling(MDAYS, min_periods=WDAYS).mean()


def f38_jpdt_009_jump_density_4sig_252d(close: pd.Series) -> pd.Series:
    """Annual jump density: mean indicator |log-ret|>4·σ_prior252 over 252 bars."""
    r = _log_ret(close)
    jump = (r.abs() > 4 * _sigma_prior(r, YDAYS)).astype(float)
    return jump.rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_010_count_abs_ret_above_p99_504d(close: pd.Series) -> pd.Series:
    """Empirical-tail count: |log-ret| above its trailing-504d 99th percentile, summed 63d."""
    r = _log_ret(close).abs()
    p99 = r.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.99).shift(1)
    return (r > p99).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_011_count_abs_ret_above_p995_1260d(close: pd.Series) -> pd.Series:
    """Deep-tail count: |log-ret| above trailing-1260d 99.5th percentile, summed 252d."""
    r = _log_ret(close).abs()
    p = r.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).quantile(0.995).shift(1)
    return (r > p).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_012_count_mad_jump_4mad_63d(close: pd.Series) -> pd.Series:
    """Robust-tail count: |log-ret-median| > 4·MAD_prior63 in last 63 bars."""
    r = _log_ret(close)
    med = r.rolling(QDAYS, min_periods=MDAYS).median().shift(1)
    mad = _mad_prior(r, QDAYS)
    return ((r - med).abs() > 4 * mad).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket B — Asymmetric jump counts (013-022)
# ============================================================

def f38_jpdt_013_pos_jump_count_3sig_21d(close: pd.Series) -> pd.Series:
    """Upward fresh-shock count: r > +3·σ_prior21 in 21d."""
    r = _log_ret(close)
    return (r > 3 * _sigma_prior(r, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_014_neg_jump_count_3sig_21d(close: pd.Series) -> pd.Series:
    """Downward fresh-shock count: r < −3·σ_prior21 in 21d."""
    r = _log_ret(close)
    return (r < -3 * _sigma_prior(r, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_015_pos_jump_count_4sig_63d(close: pd.Series) -> pd.Series:
    """Upward intermediate-shock count: r > +4·σ_prior63 in 63d."""
    r = _log_ret(close)
    return (r > 4 * _sigma_prior(r, QDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_016_neg_jump_count_4sig_63d(close: pd.Series) -> pd.Series:
    """Downward intermediate-shock count: r < −4·σ_prior63 in 63d."""
    r = _log_ret(close)
    return (r < -4 * _sigma_prior(r, QDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_017_ratio_pos_neg_jump_count_252d(close: pd.Series) -> pd.Series:
    """Directional jump asymmetry: positive/negative jump counts (3σ_21d) over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    pos = (r > 3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    neg = (r < -3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(pos, neg)


def f38_jpdt_018_signed_jump_tally_63d(close: pd.Series) -> pd.Series:
    """Net direction of jumps: sum of jump-day signs (3σ_21d) in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sign = np.sign(r).where(r.abs() > 3 * sig, 0.0)
    return sign.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_019_cum_pos_jump_magnitude_63d(close: pd.Series) -> pd.Series:
    """Upside-shock magnitude sum: sum of r on positive 3σ_21d jump days in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    mag = r.where(r > 3 * sig, 0.0)
    return mag.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_020_cum_neg_jump_magnitude_63d(close: pd.Series) -> pd.Series:
    """Downside-shock magnitude sum: sum of r on negative 3σ_21d jump days in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    mag = r.where(r < -3 * sig, 0.0)
    return mag.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_021_asymmetry_index_jumps_252d(close: pd.Series) -> pd.Series:
    """Jump asymmetry index (up-dn)/(up+dn) of 3σ_21d jump counts over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    pos = (r > 3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    neg = (r < -3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(pos - neg, pos + neg)


def f38_jpdt_022_neg_dominance_indicator_63d(close: pd.Series) -> pd.Series:
    """Negative-jump dominance: 1 when neg-jump count > 2× pos-jump count in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    pos = (r > 3 * sig).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    neg = (r < -3 * sig).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return (neg > 2 * pos).astype(float)


# ============================================================
# Bucket C — Magnitude statistics conditional on jump (023-030)
# ============================================================

def f38_jpdt_023_mean_abs_ret_on_jump_days_63d(close: pd.Series) -> pd.Series:
    """Avg jump magnitude: mean |log-ret| on 3σ_21d jump days in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    mag = r.abs().where(r.abs() > 3 * sig, np.nan)
    return mag.rolling(QDAYS, min_periods=MDAYS).mean()


def f38_jpdt_024_max_abs_ret_on_jump_days_63d(close: pd.Series) -> pd.Series:
    """Peak jump magnitude: max |log-ret| on 3σ_21d jump days in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    mag = r.abs().where(r.abs() > 3 * sig, np.nan)
    return mag.rolling(QDAYS, min_periods=MDAYS).max()


def f38_jpdt_025_sum_abs_ret_on_jump_days_252d(close: pd.Series) -> pd.Series:
    """Annual cumulative jump magnitude: sum |log-ret| on 3σ_21d jumps in 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    mag = r.abs().where(r.abs() > 3 * sig, 0.0)
    return mag.rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_026_skew_jump_day_signed_returns_252d(close: pd.Series) -> pd.Series:
    """Jump-day return skew: skewness of signed returns on 3σ_21d jump days in 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sig_r = r.where(r.abs() > 3 * sig, np.nan)
    return sig_r.rolling(YDAYS, min_periods=QDAYS).skew()


def f38_jpdt_027_std_jump_day_signed_returns_252d(close: pd.Series) -> pd.Series:
    """Jump-day return dispersion: std of signed returns on 3σ_21d jumps in 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sig_r = r.where(r.abs() > 3 * sig, np.nan)
    return sig_r.rolling(YDAYS, min_periods=QDAYS).std()


def f38_jpdt_028_ratio_max_mean_jump_magnitude_63d(close: pd.Series) -> pd.Series:
    """Jump-magnitude peakedness: max/mean |log-ret| on jump days in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    mag = r.abs().where(r.abs() > 3 * sig, np.nan)
    return _safe_div(mag.rolling(QDAYS, min_periods=MDAYS).max(),
                     mag.rolling(QDAYS, min_periods=MDAYS).mean())


def f38_jpdt_029_mean_normalized_jump_severity_63d(close: pd.Series) -> pd.Series:
    """Mean |r|/σ_prior21 restricted to 3σ jump days, over 63d → normalized severity."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sev = _safe_div(r.abs(), sig).where(r.abs() > 3 * sig, np.nan)
    return sev.rolling(QDAYS, min_periods=MDAYS).mean()


def f38_jpdt_030_p90_jump_magnitude_252d(close: pd.Series) -> pd.Series:
    """90th-percentile |log-ret| on 3σ_21d jump days over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    mag = r.abs().where(r.abs() > 3 * sig, np.nan)
    return mag.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)


# ============================================================
# Bucket D — Jump clustering (031-040)
# ============================================================

def _bars_since_event(ind: pd.Series) -> pd.Series:
    arr = ind.fillna(0).astype(int).values
    out = np.full(len(arr), np.nan)
    bars = np.nan
    for i, x in enumerate(arr):
        if x:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=ind.index)


def f38_jpdt_031_bars_since_3sig_21d_jump(close: pd.Series) -> pd.Series:
    """Recency of fresh shock: bars since last 3σ_prior21 jump."""
    r = _log_ret(close)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return _bars_since_event(jump)


def f38_jpdt_032_bars_since_4sig_63d_jump(close: pd.Series) -> pd.Series:
    """Recency of intermediate shock: bars since last 4σ_prior63 jump."""
    r = _log_ret(close)
    jump = (r.abs() > 4 * _sigma_prior(r, QDAYS)).astype(float)
    return _bars_since_event(jump)


def f38_jpdt_033_bars_since_5sig_252d_jump(close: pd.Series) -> pd.Series:
    """Recency of annual extreme: bars since last 5σ_prior252 jump."""
    r = _log_ret(close)
    jump = (r.abs() > 5 * _sigma_prior(r, YDAYS)).astype(float)
    return _bars_since_event(jump)


def f38_jpdt_034_max_consecutive_jump_run_63d(close: pd.Series) -> pd.Series:
    """Longest streak of consecutive 3σ_21d jump days within a 63d window."""
    r = _log_ret(close)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5:
                c += 1; m = c if c > m else m
            else:
                c = 0
        return m
    return jump.rolling(QDAYS, min_periods=MDAYS).apply(_run, raw=True)


def f38_jpdt_035_jump_count_in_last_5d(close: pd.Series) -> pd.Series:
    """Very-short-horizon jump cluster: count of 3σ_21d jumps in last 5 bars."""
    r = _log_ret(close)
    return (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).rolling(WDAYS, min_periods=2).sum()


def f38_jpdt_036_mean_inter_jump_time_252d(close: pd.Series) -> pd.Series:
    """Mean spacing of 3σ_21d jumps within trailing 252d window."""
    r = _log_ret(close)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _mean_gap(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 2:
            return np.nan
        return float(np.diff(idx).mean())
    return jump.rolling(YDAYS, min_periods=QDAYS).apply(_mean_gap, raw=True)


def f38_jpdt_037_std_inter_jump_time_252d(close: pd.Series) -> pd.Series:
    """Irregularity of jump arrivals: std of inter-jump times within 252d window."""
    r = _log_ret(close)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _std_gap(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 3:
            return np.nan
        return float(np.diff(idx).std())
    return jump.rolling(YDAYS, min_periods=QDAYS).apply(_std_gap, raw=True)


def f38_jpdt_038_cv_inter_jump_time_252d(close: pd.Series) -> pd.Series:
    """Fano-style index: CV of inter-jump times — burstiness of arrivals — 252d."""
    r = _log_ret(close)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _cv(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 3:
            return np.nan
        g = np.diff(idx)
        m = g.mean()
        return float(g.std() / m) if m != 0 else np.nan
    return jump.rolling(YDAYS, min_periods=QDAYS).apply(_cv, raw=True)


def f38_jpdt_039_back_to_back_jump_pairs_63d(close: pd.Series) -> pd.Series:
    """Echo-shock count: 3σ_21d jump-pairs within 2 bars apart, summed over 63d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)
    pair = ((j > 0.5) & ((j.shift(1) > 0.5) | (j.shift(2) > 0.5))).astype(float)
    return pair.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_040_recent_jump_density_5d_vs_252d(close: pd.Series) -> pd.Series:
    """Recent acceleration: jump density in last 5d / mean density over past 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return _safe_div(j.rolling(WDAYS, min_periods=2).mean(),
                     j.rolling(YDAYS, min_periods=QDAYS).mean())


# ============================================================
# Bucket E — Statistical jump tests (041-052)
# All σ̂ from strictly prior window.
# ============================================================

def _bv(r, n):
    """Bipower variation: π/2 · Σ |r_t|·|r_{t-1}|."""
    pr = r.abs() * r.abs().shift(1)
    return (np.pi / 2.0) * pr.rolling(n, min_periods=max(n // 3, 2)).sum()


def _rv(r, n):
    """Realized variance: Σ r²."""
    return (r ** 2).rolling(n, min_periods=max(n // 3, 2)).sum()


def f38_jpdt_041_bns_bv_over_rv_21d(close: pd.Series) -> pd.Series:
    """BNS BV/RV ratio (21d): low ratio = jump-dominated; high = diffusion."""
    r = _log_ret(close)
    return _safe_div(_bv(r, MDAYS), _rv(r, MDAYS))


def f38_jpdt_042_bns_bv_over_rv_63d(close: pd.Series) -> pd.Series:
    """BNS BV/RV ratio (63d) — intermediate-horizon jump signal."""
    r = _log_ret(close)
    return _safe_div(_bv(r, QDAYS), _rv(r, QDAYS))


def f38_jpdt_043_jump_variance_fraction_63d(close: pd.Series) -> pd.Series:
    """Jump-variance share: max(0, 1 - BV/RV) at 63d."""
    r = _log_ret(close)
    return (1.0 - _safe_div(_bv(r, QDAYS), _rv(r, QDAYS))).clip(lower=0.0)


def f38_jpdt_044_jump_variance_fraction_252d(close: pd.Series) -> pd.Series:
    """Annual jump-variance share: max(0, 1 - BV/RV) at 252d."""
    r = _log_ret(close)
    return (1.0 - _safe_div(_bv(r, YDAYS), _rv(r, YDAYS))).clip(lower=0.0)


def f38_jpdt_045_bvrv_diff_21d_vs_252d(close: pd.Series) -> pd.Series:
    """BV/RV(21d) − BV/RV(252d): short-vs-long jump-share regime delta."""
    r = _log_ret(close)
    return _safe_div(_bv(r, MDAYS), _rv(r, MDAYS)) - _safe_div(_bv(r, YDAYS), _rv(r, YDAYS))


def f38_jpdt_046_lee_mykland_local_stat(close: pd.Series) -> pd.Series:
    """Lee-Mykland-style local jump stat: |r_t| / sqrt(BV_prior21 / 21 * π/2)."""
    r = _log_ret(close)
    bv_prior = _bv(r, MDAYS).shift(1)
    scale = np.sqrt(_safe_div(bv_prior, MDAYS) * (np.pi / 2.0))
    return _safe_div(r.abs(), scale)


def f38_jpdt_047_lee_mykland_event_count_63d(close: pd.Series) -> pd.Series:
    """Count of Lee-Mykland-stat > 4 events within 63d window."""
    r = _log_ret(close)
    bv_prior = _bv(r, MDAYS).shift(1)
    scale = np.sqrt(_safe_div(bv_prior, MDAYS) * (np.pi / 2.0))
    stat = _safe_div(r.abs(), scale)
    return (stat > 4.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_048_max_lee_mykland_stat_21d(close: pd.Series) -> pd.Series:
    """Peak Lee-Mykland test stat within trailing 21d window."""
    r = _log_ret(close)
    bv_prior = _bv(r, MDAYS).shift(1)
    scale = np.sqrt(_safe_div(bv_prior, MDAYS) * (np.pi / 2.0))
    stat = _safe_div(r.abs(), scale)
    return stat.rolling(MDAYS, min_periods=WDAYS).max()


def f38_jpdt_049_aitsahalia_threshold_variation_21d(close: pd.Series) -> pd.Series:
    """Aït-Sahalia threshold variation: Σ r²·1{|r| ≤ 3·σ_prior21} over 21d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    truncated = (r ** 2).where(r.abs() <= 3 * sig, 0.0)
    return truncated.rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_050_abdl_truncated_rv_fraction_63d(close: pd.Series) -> pd.Series:
    """ABDL truncated RV share: 1 − (Σ r²·1{|r|≤4σ_prior63}) / Σ r² over 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, QDAYS)
    rv = _rv(r, QDAYS)
    trv = (r ** 2).where(r.abs() <= 4 * sig, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    return (1.0 - _safe_div(trv, rv)).clip(lower=0.0)


def f38_jpdt_051_corsi_pirino_threshold_bipower_63d(close: pd.Series) -> pd.Series:
    """Corsi-Pirino threshold bipower (TBPV) jump signal: 1 − TBPV/BV at 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, QDAYS)
    a = r.abs().where(r.abs() <= 4 * sig, 0.0)
    tbpv = (np.pi / 2.0) * (a * a.shift(1)).rolling(QDAYS, min_periods=MDAYS).sum()
    return (1.0 - _safe_div(tbpv, _bv(r, QDAYS))).clip(lower=0.0)


def f38_jpdt_052_arch_effect_slope_252d(close: pd.Series) -> pd.Series:
    """ARCH effect proxy: rolling slope of r² regressed on its own time-index over 252d."""
    r = _log_ret(close)
    return _rolling_slope(r ** 2, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket F — Range-vs-close jump asymmetry (053-060)
# ============================================================

def _gap_ret(open: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_log(open) - _safe_log(close.shift(1))


def _intraday_logHL(high: pd.Series, low: pd.Series) -> pd.Series:
    return _safe_log(high) - _safe_log(low)


def f38_jpdt_053_gap_jump_count_3sig_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight-gap jump count: |log(open/prev_close)| > 3·σ_prior21_gap in 21d."""
    g = _gap_ret(open, close)
    return (g.abs() > 3 * _sigma_prior(g, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_054_gap_jump_count_4sig_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Intermediate-horizon gap-jump count: |gap-ret| > 4·σ_prior63_gap in 63d."""
    g = _gap_ret(open, close)
    return (g.abs() > 4 * _sigma_prior(g, QDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_055_intraday_range_jump_count_3sig_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday-range jump count: log(H/L) > 3·σ_prior21_logHL in 21d."""
    hl = _intraday_logHL(high, low)
    return (hl > 3 * _sigma_prior(hl, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_056_ratio_gap_vs_intraday_jumps_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight-vs-intraday regime: gap-jump count / intraday-range-jump count in 63d."""
    g = _gap_ret(open, close)
    hl = _intraday_logHL(high, low)
    gj = (g.abs() > 3 * _sigma_prior(g, MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ij = (hl > 3 * _sigma_prior(hl, MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(gj, ij)


def f38_jpdt_057_mean_gap_share_of_daily_ret_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of daily move attributable to overnight gap: |gap| / |c2c| mean 21d."""
    g = _gap_ret(open, close)
    c2c = _safe_log(close).diff()
    return _safe_div(g.abs(), c2c.abs()).rolling(MDAYS, min_periods=WDAYS).mean()


def f38_jpdt_058_overnight_variance_share_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight variance share: Σ gap² / Σ c2c² over 63d."""
    g = _gap_ret(open, close)
    c2c = _safe_log(close).diff()
    num = (g ** 2).rolling(QDAYS, min_periods=MDAYS).sum()
    den = (c2c ** 2).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den)


def f38_jpdt_059_peak_overnight_shock_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Peak overnight shock: max |gap| / σ_prior252_c2c within 63d."""
    g = _gap_ret(open, close)
    sig = _sigma_prior(_safe_log(close).diff(), YDAYS)
    return _safe_div(g.abs(), sig).rolling(QDAYS, min_periods=MDAYS).max()


def f38_jpdt_060_gap_down_only_count_3sig_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Downside gap-only count: gap-ret < −3·σ_prior21_gap in 21d."""
    g = _gap_ret(open, close)
    return (g < -3 * _sigma_prior(g, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket G — Tail-shape jump descriptors (061-070)
# ============================================================

def _hill_estimator(absr_window: np.ndarray, top_frac: float) -> float:
    arr = absr_window[~np.isnan(absr_window)]
    if len(arr) < 30:
        return np.nan
    k = max(int(len(arr) * top_frac), 5)
    top = np.sort(arr)[-k:]
    th = top[0]
    if th <= 0:
        return np.nan
    lg = np.log(top / th)
    val = lg[1:].mean() if len(lg) > 1 else np.nan
    return float(val) if np.isfinite(val) and val > 0 else np.nan


def f38_jpdt_061_hill_tail_index_top10_252d(close: pd.Series) -> pd.Series:
    """Hill estimator of tail-index (top 10% of |log-ret|) over 252d — heavier tails = larger."""
    r = _log_ret(close).abs()
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _hill_estimator(w, 0.10), raw=True)


def f38_jpdt_062_hill_tail_index_top5_504d(close: pd.Series) -> pd.Series:
    """Extreme-tail Hill estimator (top 5%) over 504d — biennial extreme-tail thickness."""
    r = _log_ret(close).abs()
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(lambda w: _hill_estimator(w, 0.05), raw=True)


def f38_jpdt_063_expected_shortfall_95_252d(close: pd.Series) -> pd.Series:
    """Expected shortfall at 95%: mean |log-ret| above its 252d 95th percentile."""
    r = _log_ret(close).abs()
    p = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return r.where(r > p, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_064_expected_shortfall_99_252d(close: pd.Series) -> pd.Series:
    """Expected shortfall at 99%: mean |log-ret| above its 252d 99th percentile."""
    r = _log_ret(close).abs()
    p = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    return r.where(r > p, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_065_p99_over_p90_abs_ret_252d(close: pd.Series) -> pd.Series:
    """Tail-peakedness ratio: 99th-pct |log-ret| / 90th-pct over 252d."""
    r = _log_ret(close).abs()
    p99 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    p90 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return _safe_div(p99, p90)


def f38_jpdt_066_p995_over_p95_abs_ret_504d(close: pd.Series) -> pd.Series:
    """Deep-tail to outer-tail ratio: 99.5th / 95th |log-ret| pct over 504d."""
    r = _log_ret(close).abs()
    p995 = r.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.995)
    p95 = r.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.95)
    return _safe_div(p995, p95)


def f38_jpdt_067_pickands_tail_index_252d(close: pd.Series) -> pd.Series:
    """Pickands estimator of tail index for |log-ret| over 252d."""
    r = _log_ret(close).abs()

    def _pickands(w):
        a = np.sort(w[~np.isnan(w)])
        n = len(a)
        if n < 60:
            return np.nan
        k = n // 4
        if k < 2:
            return np.nan
        num = a[n - k] - a[n - 2 * k]
        den = a[n - 2 * k] - a[n - 4 * k]
        if den <= 0 or num <= 0:
            return np.nan
        return float(np.log(num / den) / np.log(2.0))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_pickands, raw=True)


def f38_jpdt_068_kurtosis_top_decile_returns_252d(close: pd.Series) -> pd.Series:
    """Kurtosis of returns restricted to top-decile |log-ret| bars over 252d."""
    r = _log_ret(close)
    a = r.abs()
    p90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    sel = r.where(a > p90, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).kurt()


def f38_jpdt_069_ccdf_log_slope_top5_252d(close: pd.Series) -> pd.Series:
    """Empirical CCDF log-slope at top-5% of |log-ret| over 252d (tail-decay steepness)."""
    r = _log_ret(close).abs()

    def _slope(w):
        a = np.sort(w[~np.isnan(w)])
        n = len(a)
        if n < 60:
            return np.nan
        k = max(int(0.05 * n), 5)
        top = a[-k:]
        if top[0] <= 0:
            return np.nan
        x = np.log(top)
        y = np.log(np.arange(k, 0, -1) / n)
        xm = x.mean(); ym = y.mean()
        d = ((x - xm) ** 2).sum()
        return float(((x - xm) * (y - ym)).sum() / d) if d > 0 else np.nan
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_slope, raw=True)


def f38_jpdt_070_max_over_p95_abs_ret_63d(close: pd.Series) -> pd.Series:
    """Extremity ratio: max |log-ret| / 95th-pct |log-ret| over 63d."""
    r = _log_ret(close).abs()
    mx = r.rolling(QDAYS, min_periods=MDAYS).max()
    p95 = r.rolling(QDAYS, min_periods=MDAYS).quantile(0.95)
    return _safe_div(mx, p95)


# ============================================================
# Bucket H — Jump-volume coupling (start; 071-075)
# ============================================================

def f38_jpdt_071_joint_jump_high_vol_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Joint jump+high-volume days: count where |r|>3σ_21d AND vol_z>2 in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    jump = r.abs() > 3 * sig
    volz = _rolling_zscore(volume, QDAYS).shift(1)
    return ((jump) & (volz > 2.0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_072_mean_volz_on_jump_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume z-score on 3σ_21d jump days within 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    volz = _rolling_zscore(volume, QDAYS).shift(1)
    sel = volz.where(r.abs() > 3 * sig, np.nan)
    return sel.rolling(QDAYS, min_periods=MDAYS).mean()


def f38_jpdt_073_jump_vol_amplification_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Jump-volume amplification: mean(vol on jump days) / mean(vol on non-jump days) 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    jmask = r.abs() > 3 * sig
    on = volume.where(jmask, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    off = volume.where(~jmask, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(on, off)


def f38_jpdt_074_corr_absret_logvol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of |log-ret| and log(volume) — short-horizon magnitude-volume link."""
    r = _log_ret(close).abs()
    lv = _safe_log(volume)
    return r.rolling(QDAYS, min_periods=MDAYS).corr(lv)


def f38_jpdt_075_corr_absret_logvol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr of |log-ret| and log(volume) — annual magnitude-volume coupling."""
    r = _log_ret(close).abs()
    lv = _safe_log(volume)
    return r.rolling(YDAYS, min_periods=QDAYS).corr(lv)


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f38_jpdt_001_count_abs_ret_above_3sig_21d_d1(close):
    return f38_jpdt_001_count_abs_ret_above_3sig_21d(close).diff()


def f38_jpdt_002_count_abs_ret_above_4sig_63d_d1(close):
    return f38_jpdt_002_count_abs_ret_above_4sig_63d(close).diff()


def f38_jpdt_003_count_abs_ret_above_5sig_252d_d1(close):
    return f38_jpdt_003_count_abs_ret_above_5sig_252d(close).diff()


def f38_jpdt_004_count_abs_ret_above_2sig_5d_d1(close):
    return f38_jpdt_004_count_abs_ret_above_2sig_5d(close).diff()


def f38_jpdt_005_count_abs_ret_above_6sig_504d_d1(close):
    return f38_jpdt_005_count_abs_ret_above_6sig_504d(close).diff()


def f38_jpdt_006_singlebar_5sig_252d_prior_indicator_d1(close):
    return f38_jpdt_006_singlebar_5sig_252d_prior_indicator(close).diff()


def f38_jpdt_007_singlebar_8sig_504d_prior_indicator_d1(close):
    return f38_jpdt_007_singlebar_8sig_504d_prior_indicator(close).diff()


def f38_jpdt_008_jump_density_3sig_21d_d1(close):
    return f38_jpdt_008_jump_density_3sig_21d(close).diff()


def f38_jpdt_009_jump_density_4sig_252d_d1(close):
    return f38_jpdt_009_jump_density_4sig_252d(close).diff()


def f38_jpdt_010_count_abs_ret_above_p99_504d_d1(close):
    return f38_jpdt_010_count_abs_ret_above_p99_504d(close).diff()


def f38_jpdt_011_count_abs_ret_above_p995_1260d_d1(close):
    return f38_jpdt_011_count_abs_ret_above_p995_1260d(close).diff()


def f38_jpdt_012_count_mad_jump_4mad_63d_d1(close):
    return f38_jpdt_012_count_mad_jump_4mad_63d(close).diff()


def f38_jpdt_013_pos_jump_count_3sig_21d_d1(close):
    return f38_jpdt_013_pos_jump_count_3sig_21d(close).diff()


def f38_jpdt_014_neg_jump_count_3sig_21d_d1(close):
    return f38_jpdt_014_neg_jump_count_3sig_21d(close).diff()


def f38_jpdt_015_pos_jump_count_4sig_63d_d1(close):
    return f38_jpdt_015_pos_jump_count_4sig_63d(close).diff()


def f38_jpdt_016_neg_jump_count_4sig_63d_d1(close):
    return f38_jpdt_016_neg_jump_count_4sig_63d(close).diff()


def f38_jpdt_017_ratio_pos_neg_jump_count_252d_d1(close):
    return f38_jpdt_017_ratio_pos_neg_jump_count_252d(close).diff()


def f38_jpdt_018_signed_jump_tally_63d_d1(close):
    return f38_jpdt_018_signed_jump_tally_63d(close).diff()


def f38_jpdt_019_cum_pos_jump_magnitude_63d_d1(close):
    return f38_jpdt_019_cum_pos_jump_magnitude_63d(close).diff()


def f38_jpdt_020_cum_neg_jump_magnitude_63d_d1(close):
    return f38_jpdt_020_cum_neg_jump_magnitude_63d(close).diff()


def f38_jpdt_021_asymmetry_index_jumps_252d_d1(close):
    return f38_jpdt_021_asymmetry_index_jumps_252d(close).diff()


def f38_jpdt_022_neg_dominance_indicator_63d_d1(close):
    return f38_jpdt_022_neg_dominance_indicator_63d(close).diff()


def f38_jpdt_023_mean_abs_ret_on_jump_days_63d_d1(close):
    return f38_jpdt_023_mean_abs_ret_on_jump_days_63d(close).diff()


def f38_jpdt_024_max_abs_ret_on_jump_days_63d_d1(close):
    return f38_jpdt_024_max_abs_ret_on_jump_days_63d(close).diff()


def f38_jpdt_025_sum_abs_ret_on_jump_days_252d_d1(close):
    return f38_jpdt_025_sum_abs_ret_on_jump_days_252d(close).diff()


def f38_jpdt_026_skew_jump_day_signed_returns_252d_d1(close):
    return f38_jpdt_026_skew_jump_day_signed_returns_252d(close).diff()


def f38_jpdt_027_std_jump_day_signed_returns_252d_d1(close):
    return f38_jpdt_027_std_jump_day_signed_returns_252d(close).diff()


def f38_jpdt_028_ratio_max_mean_jump_magnitude_63d_d1(close):
    return f38_jpdt_028_ratio_max_mean_jump_magnitude_63d(close).diff()


def f38_jpdt_029_mean_normalized_jump_severity_63d_d1(close):
    return f38_jpdt_029_mean_normalized_jump_severity_63d(close).diff()


def f38_jpdt_030_p90_jump_magnitude_252d_d1(close):
    return f38_jpdt_030_p90_jump_magnitude_252d(close).diff()


def f38_jpdt_031_bars_since_3sig_21d_jump_d1(close):
    return f38_jpdt_031_bars_since_3sig_21d_jump(close).diff()


def f38_jpdt_032_bars_since_4sig_63d_jump_d1(close):
    return f38_jpdt_032_bars_since_4sig_63d_jump(close).diff()


def f38_jpdt_033_bars_since_5sig_252d_jump_d1(close):
    return f38_jpdt_033_bars_since_5sig_252d_jump(close).diff()


def f38_jpdt_034_max_consecutive_jump_run_63d_d1(close):
    return f38_jpdt_034_max_consecutive_jump_run_63d(close).diff()


def f38_jpdt_035_jump_count_in_last_5d_d1(close):
    return f38_jpdt_035_jump_count_in_last_5d(close).diff()


def f38_jpdt_036_mean_inter_jump_time_252d_d1(close):
    return f38_jpdt_036_mean_inter_jump_time_252d(close).diff()


def f38_jpdt_037_std_inter_jump_time_252d_d1(close):
    return f38_jpdt_037_std_inter_jump_time_252d(close).diff()


def f38_jpdt_038_cv_inter_jump_time_252d_d1(close):
    return f38_jpdt_038_cv_inter_jump_time_252d(close).diff()


def f38_jpdt_039_back_to_back_jump_pairs_63d_d1(close):
    return f38_jpdt_039_back_to_back_jump_pairs_63d(close).diff()


def f38_jpdt_040_recent_jump_density_5d_vs_252d_d1(close):
    return f38_jpdt_040_recent_jump_density_5d_vs_252d(close).diff()


def f38_jpdt_041_bns_bv_over_rv_21d_d1(close):
    return f38_jpdt_041_bns_bv_over_rv_21d(close).diff()


def f38_jpdt_042_bns_bv_over_rv_63d_d1(close):
    return f38_jpdt_042_bns_bv_over_rv_63d(close).diff()


def f38_jpdt_043_jump_variance_fraction_63d_d1(close):
    return f38_jpdt_043_jump_variance_fraction_63d(close).diff()


def f38_jpdt_044_jump_variance_fraction_252d_d1(close):
    return f38_jpdt_044_jump_variance_fraction_252d(close).diff()


def f38_jpdt_045_bvrv_diff_21d_vs_252d_d1(close):
    return f38_jpdt_045_bvrv_diff_21d_vs_252d(close).diff()


def f38_jpdt_046_lee_mykland_local_stat_d1(close):
    return f38_jpdt_046_lee_mykland_local_stat(close).diff()


def f38_jpdt_047_lee_mykland_event_count_63d_d1(close):
    return f38_jpdt_047_lee_mykland_event_count_63d(close).diff()


def f38_jpdt_048_max_lee_mykland_stat_21d_d1(close):
    return f38_jpdt_048_max_lee_mykland_stat_21d(close).diff()


def f38_jpdt_049_aitsahalia_threshold_variation_21d_d1(close):
    return f38_jpdt_049_aitsahalia_threshold_variation_21d(close).diff()


def f38_jpdt_050_abdl_truncated_rv_fraction_63d_d1(close):
    return f38_jpdt_050_abdl_truncated_rv_fraction_63d(close).diff()


def f38_jpdt_051_corsi_pirino_threshold_bipower_63d_d1(close):
    return f38_jpdt_051_corsi_pirino_threshold_bipower_63d(close).diff()


def f38_jpdt_052_arch_effect_slope_252d_d1(close):
    return f38_jpdt_052_arch_effect_slope_252d(close).diff()


def f38_jpdt_053_gap_jump_count_3sig_21d_d1(open, close):
    return f38_jpdt_053_gap_jump_count_3sig_21d(open, close).diff()


def f38_jpdt_054_gap_jump_count_4sig_63d_d1(open, close):
    return f38_jpdt_054_gap_jump_count_4sig_63d(open, close).diff()


def f38_jpdt_055_intraday_range_jump_count_3sig_21d_d1(high, low):
    return f38_jpdt_055_intraday_range_jump_count_3sig_21d(high, low).diff()


def f38_jpdt_056_ratio_gap_vs_intraday_jumps_63d_d1(open, high, low, close):
    return f38_jpdt_056_ratio_gap_vs_intraday_jumps_63d(open, high, low, close).diff()


def f38_jpdt_057_mean_gap_share_of_daily_ret_21d_d1(open, close):
    return f38_jpdt_057_mean_gap_share_of_daily_ret_21d(open, close).diff()


def f38_jpdt_058_overnight_variance_share_63d_d1(open, close):
    return f38_jpdt_058_overnight_variance_share_63d(open, close).diff()


def f38_jpdt_059_peak_overnight_shock_63d_d1(open, close):
    return f38_jpdt_059_peak_overnight_shock_63d(open, close).diff()


def f38_jpdt_060_gap_down_only_count_3sig_21d_d1(open, close):
    return f38_jpdt_060_gap_down_only_count_3sig_21d(open, close).diff()


def f38_jpdt_061_hill_tail_index_top10_252d_d1(close):
    return f38_jpdt_061_hill_tail_index_top10_252d(close).diff()


def f38_jpdt_062_hill_tail_index_top5_504d_d1(close):
    return f38_jpdt_062_hill_tail_index_top5_504d(close).diff()


def f38_jpdt_063_expected_shortfall_95_252d_d1(close):
    return f38_jpdt_063_expected_shortfall_95_252d(close).diff()


def f38_jpdt_064_expected_shortfall_99_252d_d1(close):
    return f38_jpdt_064_expected_shortfall_99_252d(close).diff()


def f38_jpdt_065_p99_over_p90_abs_ret_252d_d1(close):
    return f38_jpdt_065_p99_over_p90_abs_ret_252d(close).diff()


def f38_jpdt_066_p995_over_p95_abs_ret_504d_d1(close):
    return f38_jpdt_066_p995_over_p95_abs_ret_504d(close).diff()


def f38_jpdt_067_pickands_tail_index_252d_d1(close):
    return f38_jpdt_067_pickands_tail_index_252d(close).diff()


def f38_jpdt_068_kurtosis_top_decile_returns_252d_d1(close):
    return f38_jpdt_068_kurtosis_top_decile_returns_252d(close).diff()


def f38_jpdt_069_ccdf_log_slope_top5_252d_d1(close):
    return f38_jpdt_069_ccdf_log_slope_top5_252d(close).diff()


def f38_jpdt_070_max_over_p95_abs_ret_63d_d1(close):
    return f38_jpdt_070_max_over_p95_abs_ret_63d(close).diff()


def f38_jpdt_071_joint_jump_high_vol_count_63d_d1(close, volume):
    return f38_jpdt_071_joint_jump_high_vol_count_63d(close, volume).diff()


def f38_jpdt_072_mean_volz_on_jump_days_63d_d1(close, volume):
    return f38_jpdt_072_mean_volz_on_jump_days_63d(close, volume).diff()


def f38_jpdt_073_jump_vol_amplification_63d_d1(close, volume):
    return f38_jpdt_073_jump_vol_amplification_63d(close, volume).diff()


def f38_jpdt_074_corr_absret_logvol_63d_d1(close, volume):
    return f38_jpdt_074_corr_absret_logvol_63d(close, volume).diff()


def f38_jpdt_075_corr_absret_logvol_252d_d1(close, volume):
    return f38_jpdt_075_corr_absret_logvol_252d(close, volume).diff()


JUMP_DETECTION_SIGNATURE_D1_REGISTRY_001_075 = {
    "f38_jpdt_001_count_abs_ret_above_3sig_21d_d1": {"inputs": ["close"], "func": f38_jpdt_001_count_abs_ret_above_3sig_21d_d1},
    "f38_jpdt_002_count_abs_ret_above_4sig_63d_d1": {"inputs": ["close"], "func": f38_jpdt_002_count_abs_ret_above_4sig_63d_d1},
    "f38_jpdt_003_count_abs_ret_above_5sig_252d_d1": {"inputs": ["close"], "func": f38_jpdt_003_count_abs_ret_above_5sig_252d_d1},
    "f38_jpdt_004_count_abs_ret_above_2sig_5d_d1": {"inputs": ["close"], "func": f38_jpdt_004_count_abs_ret_above_2sig_5d_d1},
    "f38_jpdt_005_count_abs_ret_above_6sig_504d_d1": {"inputs": ["close"], "func": f38_jpdt_005_count_abs_ret_above_6sig_504d_d1},
    "f38_jpdt_006_singlebar_5sig_252d_prior_indicator_d1": {"inputs": ["close"], "func": f38_jpdt_006_singlebar_5sig_252d_prior_indicator_d1},
    "f38_jpdt_007_singlebar_8sig_504d_prior_indicator_d1": {"inputs": ["close"], "func": f38_jpdt_007_singlebar_8sig_504d_prior_indicator_d1},
    "f38_jpdt_008_jump_density_3sig_21d_d1": {"inputs": ["close"], "func": f38_jpdt_008_jump_density_3sig_21d_d1},
    "f38_jpdt_009_jump_density_4sig_252d_d1": {"inputs": ["close"], "func": f38_jpdt_009_jump_density_4sig_252d_d1},
    "f38_jpdt_010_count_abs_ret_above_p99_504d_d1": {"inputs": ["close"], "func": f38_jpdt_010_count_abs_ret_above_p99_504d_d1},
    "f38_jpdt_011_count_abs_ret_above_p995_1260d_d1": {"inputs": ["close"], "func": f38_jpdt_011_count_abs_ret_above_p995_1260d_d1},
    "f38_jpdt_012_count_mad_jump_4mad_63d_d1": {"inputs": ["close"], "func": f38_jpdt_012_count_mad_jump_4mad_63d_d1},
    "f38_jpdt_013_pos_jump_count_3sig_21d_d1": {"inputs": ["close"], "func": f38_jpdt_013_pos_jump_count_3sig_21d_d1},
    "f38_jpdt_014_neg_jump_count_3sig_21d_d1": {"inputs": ["close"], "func": f38_jpdt_014_neg_jump_count_3sig_21d_d1},
    "f38_jpdt_015_pos_jump_count_4sig_63d_d1": {"inputs": ["close"], "func": f38_jpdt_015_pos_jump_count_4sig_63d_d1},
    "f38_jpdt_016_neg_jump_count_4sig_63d_d1": {"inputs": ["close"], "func": f38_jpdt_016_neg_jump_count_4sig_63d_d1},
    "f38_jpdt_017_ratio_pos_neg_jump_count_252d_d1": {"inputs": ["close"], "func": f38_jpdt_017_ratio_pos_neg_jump_count_252d_d1},
    "f38_jpdt_018_signed_jump_tally_63d_d1": {"inputs": ["close"], "func": f38_jpdt_018_signed_jump_tally_63d_d1},
    "f38_jpdt_019_cum_pos_jump_magnitude_63d_d1": {"inputs": ["close"], "func": f38_jpdt_019_cum_pos_jump_magnitude_63d_d1},
    "f38_jpdt_020_cum_neg_jump_magnitude_63d_d1": {"inputs": ["close"], "func": f38_jpdt_020_cum_neg_jump_magnitude_63d_d1},
    "f38_jpdt_021_asymmetry_index_jumps_252d_d1": {"inputs": ["close"], "func": f38_jpdt_021_asymmetry_index_jumps_252d_d1},
    "f38_jpdt_022_neg_dominance_indicator_63d_d1": {"inputs": ["close"], "func": f38_jpdt_022_neg_dominance_indicator_63d_d1},
    "f38_jpdt_023_mean_abs_ret_on_jump_days_63d_d1": {"inputs": ["close"], "func": f38_jpdt_023_mean_abs_ret_on_jump_days_63d_d1},
    "f38_jpdt_024_max_abs_ret_on_jump_days_63d_d1": {"inputs": ["close"], "func": f38_jpdt_024_max_abs_ret_on_jump_days_63d_d1},
    "f38_jpdt_025_sum_abs_ret_on_jump_days_252d_d1": {"inputs": ["close"], "func": f38_jpdt_025_sum_abs_ret_on_jump_days_252d_d1},
    "f38_jpdt_026_skew_jump_day_signed_returns_252d_d1": {"inputs": ["close"], "func": f38_jpdt_026_skew_jump_day_signed_returns_252d_d1},
    "f38_jpdt_027_std_jump_day_signed_returns_252d_d1": {"inputs": ["close"], "func": f38_jpdt_027_std_jump_day_signed_returns_252d_d1},
    "f38_jpdt_028_ratio_max_mean_jump_magnitude_63d_d1": {"inputs": ["close"], "func": f38_jpdt_028_ratio_max_mean_jump_magnitude_63d_d1},
    "f38_jpdt_029_mean_normalized_jump_severity_63d_d1": {"inputs": ["close"], "func": f38_jpdt_029_mean_normalized_jump_severity_63d_d1},
    "f38_jpdt_030_p90_jump_magnitude_252d_d1": {"inputs": ["close"], "func": f38_jpdt_030_p90_jump_magnitude_252d_d1},
    "f38_jpdt_031_bars_since_3sig_21d_jump_d1": {"inputs": ["close"], "func": f38_jpdt_031_bars_since_3sig_21d_jump_d1},
    "f38_jpdt_032_bars_since_4sig_63d_jump_d1": {"inputs": ["close"], "func": f38_jpdt_032_bars_since_4sig_63d_jump_d1},
    "f38_jpdt_033_bars_since_5sig_252d_jump_d1": {"inputs": ["close"], "func": f38_jpdt_033_bars_since_5sig_252d_jump_d1},
    "f38_jpdt_034_max_consecutive_jump_run_63d_d1": {"inputs": ["close"], "func": f38_jpdt_034_max_consecutive_jump_run_63d_d1},
    "f38_jpdt_035_jump_count_in_last_5d_d1": {"inputs": ["close"], "func": f38_jpdt_035_jump_count_in_last_5d_d1},
    "f38_jpdt_036_mean_inter_jump_time_252d_d1": {"inputs": ["close"], "func": f38_jpdt_036_mean_inter_jump_time_252d_d1},
    "f38_jpdt_037_std_inter_jump_time_252d_d1": {"inputs": ["close"], "func": f38_jpdt_037_std_inter_jump_time_252d_d1},
    "f38_jpdt_038_cv_inter_jump_time_252d_d1": {"inputs": ["close"], "func": f38_jpdt_038_cv_inter_jump_time_252d_d1},
    "f38_jpdt_039_back_to_back_jump_pairs_63d_d1": {"inputs": ["close"], "func": f38_jpdt_039_back_to_back_jump_pairs_63d_d1},
    "f38_jpdt_040_recent_jump_density_5d_vs_252d_d1": {"inputs": ["close"], "func": f38_jpdt_040_recent_jump_density_5d_vs_252d_d1},
    "f38_jpdt_041_bns_bv_over_rv_21d_d1": {"inputs": ["close"], "func": f38_jpdt_041_bns_bv_over_rv_21d_d1},
    "f38_jpdt_042_bns_bv_over_rv_63d_d1": {"inputs": ["close"], "func": f38_jpdt_042_bns_bv_over_rv_63d_d1},
    "f38_jpdt_043_jump_variance_fraction_63d_d1": {"inputs": ["close"], "func": f38_jpdt_043_jump_variance_fraction_63d_d1},
    "f38_jpdt_044_jump_variance_fraction_252d_d1": {"inputs": ["close"], "func": f38_jpdt_044_jump_variance_fraction_252d_d1},
    "f38_jpdt_045_bvrv_diff_21d_vs_252d_d1": {"inputs": ["close"], "func": f38_jpdt_045_bvrv_diff_21d_vs_252d_d1},
    "f38_jpdt_046_lee_mykland_local_stat_d1": {"inputs": ["close"], "func": f38_jpdt_046_lee_mykland_local_stat_d1},
    "f38_jpdt_047_lee_mykland_event_count_63d_d1": {"inputs": ["close"], "func": f38_jpdt_047_lee_mykland_event_count_63d_d1},
    "f38_jpdt_048_max_lee_mykland_stat_21d_d1": {"inputs": ["close"], "func": f38_jpdt_048_max_lee_mykland_stat_21d_d1},
    "f38_jpdt_049_aitsahalia_threshold_variation_21d_d1": {"inputs": ["close"], "func": f38_jpdt_049_aitsahalia_threshold_variation_21d_d1},
    "f38_jpdt_050_abdl_truncated_rv_fraction_63d_d1": {"inputs": ["close"], "func": f38_jpdt_050_abdl_truncated_rv_fraction_63d_d1},
    "f38_jpdt_051_corsi_pirino_threshold_bipower_63d_d1": {"inputs": ["close"], "func": f38_jpdt_051_corsi_pirino_threshold_bipower_63d_d1},
    "f38_jpdt_052_arch_effect_slope_252d_d1": {"inputs": ["close"], "func": f38_jpdt_052_arch_effect_slope_252d_d1},
    "f38_jpdt_053_gap_jump_count_3sig_21d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_053_gap_jump_count_3sig_21d_d1},
    "f38_jpdt_054_gap_jump_count_4sig_63d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_054_gap_jump_count_4sig_63d_d1},
    "f38_jpdt_055_intraday_range_jump_count_3sig_21d_d1": {"inputs": ["high", "low"], "func": f38_jpdt_055_intraday_range_jump_count_3sig_21d_d1},
    "f38_jpdt_056_ratio_gap_vs_intraday_jumps_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_056_ratio_gap_vs_intraday_jumps_63d_d1},
    "f38_jpdt_057_mean_gap_share_of_daily_ret_21d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_057_mean_gap_share_of_daily_ret_21d_d1},
    "f38_jpdt_058_overnight_variance_share_63d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_058_overnight_variance_share_63d_d1},
    "f38_jpdt_059_peak_overnight_shock_63d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_059_peak_overnight_shock_63d_d1},
    "f38_jpdt_060_gap_down_only_count_3sig_21d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_060_gap_down_only_count_3sig_21d_d1},
    "f38_jpdt_061_hill_tail_index_top10_252d_d1": {"inputs": ["close"], "func": f38_jpdt_061_hill_tail_index_top10_252d_d1},
    "f38_jpdt_062_hill_tail_index_top5_504d_d1": {"inputs": ["close"], "func": f38_jpdt_062_hill_tail_index_top5_504d_d1},
    "f38_jpdt_063_expected_shortfall_95_252d_d1": {"inputs": ["close"], "func": f38_jpdt_063_expected_shortfall_95_252d_d1},
    "f38_jpdt_064_expected_shortfall_99_252d_d1": {"inputs": ["close"], "func": f38_jpdt_064_expected_shortfall_99_252d_d1},
    "f38_jpdt_065_p99_over_p90_abs_ret_252d_d1": {"inputs": ["close"], "func": f38_jpdt_065_p99_over_p90_abs_ret_252d_d1},
    "f38_jpdt_066_p995_over_p95_abs_ret_504d_d1": {"inputs": ["close"], "func": f38_jpdt_066_p995_over_p95_abs_ret_504d_d1},
    "f38_jpdt_067_pickands_tail_index_252d_d1": {"inputs": ["close"], "func": f38_jpdt_067_pickands_tail_index_252d_d1},
    "f38_jpdt_068_kurtosis_top_decile_returns_252d_d1": {"inputs": ["close"], "func": f38_jpdt_068_kurtosis_top_decile_returns_252d_d1},
    "f38_jpdt_069_ccdf_log_slope_top5_252d_d1": {"inputs": ["close"], "func": f38_jpdt_069_ccdf_log_slope_top5_252d_d1},
    "f38_jpdt_070_max_over_p95_abs_ret_63d_d1": {"inputs": ["close"], "func": f38_jpdt_070_max_over_p95_abs_ret_63d_d1},
    "f38_jpdt_071_joint_jump_high_vol_count_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_071_joint_jump_high_vol_count_63d_d1},
    "f38_jpdt_072_mean_volz_on_jump_days_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_072_mean_volz_on_jump_days_63d_d1},
    "f38_jpdt_073_jump_vol_amplification_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_073_jump_vol_amplification_63d_d1},
    "f38_jpdt_074_corr_absret_logvol_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_074_corr_absret_logvol_63d_d1},
    "f38_jpdt_075_corr_absret_logvol_252d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_075_corr_absret_logvol_252d_d1},
}
