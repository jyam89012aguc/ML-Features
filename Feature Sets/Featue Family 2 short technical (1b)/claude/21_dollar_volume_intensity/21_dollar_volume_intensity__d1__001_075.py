"""dollar_volume_intensity d1 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across base__001_075 and base__076_150. Each feature
encodes a *different concept* in the dollar-volume-intensity theme:
extremes / regime / concentration / dispersion / persistence / divergence —
all in $-volume units (close × volume).

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


def _dollar_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (close * volume).astype(float)


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


def _rolling_topn_share(s, window, n, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, n + 1)
    def _sh(w):
        v = w[~np.isnan(w)]
        if v.size < n or v.sum() <= 0:
            return np.nan
        return float(np.sort(v)[-n:].sum() / v.sum())
    return s.rolling(window, min_periods=min_periods).apply(_sh, raw=True)


def _rolling_gini(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 5)
    def _g(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        v = np.sort(v)
        n = v.size
        idx = np.arange(1, n + 1)
        ss = v.sum()
        if ss <= 0:
            return np.nan
        return float((2.0 * (idx * v).sum() / ss - (n + 1)) / n)
    return s.rolling(window, min_periods=min_periods).apply(_g, raw=True)


def _rolling_hhi_norm(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 5)
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        ss = v.sum()
        if ss <= 0:
            return np.nan
        p = v / ss
        return float((p * p).sum())
    return s.rolling(window, min_periods=min_periods).apply(_h, raw=True)


def _rolling_theil(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 5)
    def _t(w):
        v = w[~np.isnan(w)]
        if v.size < 5 or np.any(v <= 0):
            return np.nan
        m = v.mean()
        if m <= 0:
            return np.nan
        return float(np.mean((v / m) * np.log(v / m)))
    return s.rolling(window, min_periods=min_periods).apply(_t, raw=True)


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


# ============================================================
# Bucket A — $-vol z-scores at multiple horizons (001-008)
# ============================================================

def f21_dvit_001_log_dv_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log dollar-volume z-score vs 252d rolling — annual intensity extreme."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_zscore(ldv, YDAYS)


def f21_dvit_002_log_dv_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log dollar-volume z-score vs 63d rolling — quarterly intensity burst."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_zscore(ldv, QDAYS)


def f21_dvit_003_log_dv_zscore_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log dollar-volume z-score vs 504d rolling — biennial intensity extreme."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_zscore(ldv, DDAYS_2Y)


def f21_dvit_004_log_dv_zscore_5y(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log dollar-volume z-score vs 5-year rolling — multi-year structural extreme."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_zscore(ldv, DDAYS_5Y)


def f21_dvit_005_log_dv_robust_mad_z_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Robust (median/MAD) z-score of log dollar-volume over 252d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _robust_zscore_mad(ldv, YDAYS)


def f21_dvit_006_log_dv_robust_mad_z_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Robust (median/MAD) z-score of log dollar-volume over 63d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _robust_zscore_mad(ldv, QDAYS)


def f21_dvit_007_log_dv_zscore_252d_gated_at_252h(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-dv z-score(252d) masked to bars where high == 252d trailing max — intensity exactly at the high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(high >= rmax, np.nan)


def f21_dvit_008_log_dv_zscore_252d_minus_pre_baseline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current log-dv z(252d) minus z(504d) — recent intensity vs longer-baseline intensity."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_zscore(ldv, YDAYS) - _rolling_zscore(ldv, DDAYS_2Y)


# ============================================================
# Bucket B — Percentile ranks (009-014)
# ============================================================

def f21_dvit_009_log_dv_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current log dollar-volume in trailing 252d distribution."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_pct_rank(ldv, YDAYS)


def f21_dvit_010_log_dv_pct_rank_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current log dollar-volume in trailing 504d distribution."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_pct_rank(ldv, DDAYS_2Y)


def f21_dvit_011_log_dv_pct_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current log dollar-volume in trailing 63d distribution."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_pct_rank(ldv, QDAYS)


def f21_dvit_012_log_dv_pct_rank_5y(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current log dollar-volume in trailing 5y distribution."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_pct_rank(ldv, DDAYS_5Y)


def f21_dvit_013_log_dv_pct_rank_diff_63_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """pct rank(63d) minus pct rank(252d) of log-dv — short-vs-long rank shift."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_pct_rank(ldv, QDAYS) - _rolling_pct_rank(ldv, YDAYS)


def f21_dvit_014_log_dv_pct_rank_inv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 minus pct rank(252d) of log-dv — symmetric rank measure focused on low extreme."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return 1.0 - _rolling_pct_rank(ldv, YDAYS)


# ============================================================
# Bucket C — $-vol vs reference ratios (015-022)
# ============================================================

def f21_dvit_015_dv_to_median_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar-volume divided by 252d trailing median dollar-volume."""
    dv = _dollar_vol(close, volume)
    med = dv.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(dv, med)


def f21_dvit_016_dv_to_median_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar-volume divided by 63d trailing median dollar-volume."""
    dv = _dollar_vol(close, volume)
    med = dv.rolling(QDAYS, min_periods=MDAYS).median()
    return _safe_div(dv, med)


def f21_dvit_017_dv_to_trimmed_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar-volume divided by 10-90 trimmed mean of dollar-volume over 252d."""
    dv = _dollar_vol(close, volume)
    def _tm(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        lo = np.quantile(v, 0.10); hi = np.quantile(v, 0.90)
        m = v[(v >= lo) & (v <= hi)]
        return m.mean() if m.size > 0 else np.nan
    tm = dv.rolling(YDAYS, min_periods=QDAYS).apply(_tm, raw=True)
    return _safe_div(dv, tm)


def f21_dvit_018_dv_to_geomean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar-volume divided by geometric mean over 252d."""
    dv = _dollar_vol(close, volume)
    gm = np.exp(_safe_log(dv).rolling(YDAYS, min_periods=QDAYS).mean())
    return _safe_div(dv, gm)


def f21_dvit_019_dv_to_max252_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar-volume divided by 252d trailing max — fraction-of-peak."""
    dv = _dollar_vol(close, volume)
    rmax = dv.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(dv, rmax)


def f21_dvit_020_dv_to_min252_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar-volume divided by 252d trailing minimum."""
    dv = _dollar_vol(close, volume)
    rmin = dv.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(dv, rmin)


def f21_dvit_021_dv_to_q75_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar-volume divided by 75%-quantile of trailing 252d."""
    dv = _dollar_vol(close, volume)
    q = _rolling_quantile(dv, YDAYS, 0.75)
    return _safe_div(dv, q)


def f21_dvit_022_dv_to_q25_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar-volume divided by 25%-quantile of trailing 252d."""
    dv = _dollar_vol(close, volume)
    q = _rolling_quantile(dv, YDAYS, 0.25)
    return _safe_div(dv, q)


# ============================================================
# Bucket D — Regime ratios (023-028)
# ============================================================

def f21_dvit_023_ratio_dv_mean_21d_to_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dollar-volume(21d) divided by mean dollar-volume(252d) — monthly vs annual regime."""
    dv = _dollar_vol(close, volume)
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    m252 = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(m21, m252)


def f21_dvit_024_ratio_dv_mean_63d_to_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dollar-volume(63d) divided by mean dollar-volume(504d) — quarterly vs biennial."""
    dv = _dollar_vol(close, volume)
    m63 = dv.rolling(QDAYS, min_periods=MDAYS).mean()
    m504 = dv.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _safe_div(m63, m504)


def f21_dvit_025_ratio_dv_mean_5d_to_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dollar-volume(5d) divided by mean dollar-volume(63d) — weekly burst vs quarterly base."""
    dv = _dollar_vol(close, volume)
    m5 = dv.rolling(WDAYS, min_periods=2).mean()
    m63 = dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(m5, m63)


def f21_dvit_026_ratio_dv_mean_21d_to_5y(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dollar-volume(21d) divided by mean dollar-volume(5y) — recent vs structural regime."""
    dv = _dollar_vol(close, volume)
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    m5y = dv.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return _safe_div(m21, m5y)


def f21_dvit_027_ratio_dv_median_21d_to_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median dollar-volume(21d) divided by median dollar-volume(252d) — robust regime ratio."""
    dv = _dollar_vol(close, volume)
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).median()
    m252 = dv.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(m21, m252)


def f21_dvit_028_regime_shift_indicator_3sigma_up_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when log-dv z(252d) > 3, summed over trailing 21d (count of 3-sigma days in the past month)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    z = _rolling_zscore(ldv, YDAYS)
    return (z > 3.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket E — Concentration / top-N share (029-036)
# ============================================================

def f21_dvit_029_top1_dv_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-1 dollar-volume day in trailing 252d as share of total trailing-252d dollar-volume."""
    dv = _dollar_vol(close, volume)
    return _rolling_topn_share(dv, YDAYS, 1)


def f21_dvit_030_top5_dv_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-5 dollar-volume days in trailing 252d as share of total."""
    dv = _dollar_vol(close, volume)
    return _rolling_topn_share(dv, YDAYS, 5)


def f21_dvit_031_top10_dv_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-10 dollar-volume days in trailing 252d as share of total."""
    dv = _dollar_vol(close, volume)
    return _rolling_topn_share(dv, YDAYS, 10)


def f21_dvit_032_top25_dv_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-25 dollar-volume days in trailing 252d as share of total."""
    dv = _dollar_vol(close, volume)
    return _rolling_topn_share(dv, YDAYS, 25)


def f21_dvit_033_top1_dv_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-1 dollar-volume day in trailing 63d as share of total."""
    dv = _dollar_vol(close, volume)
    return _rolling_topn_share(dv, QDAYS, 1)


def f21_dvit_034_top5_dv_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-5 dollar-volume days in trailing 63d as share of total."""
    dv = _dollar_vol(close, volume)
    return _rolling_topn_share(dv, QDAYS, 5)


def f21_dvit_035_top10_to_bottom10_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of top-10 / sum of bottom-10 dollar-volume days in trailing 252d — concentration ratio."""
    dv = _dollar_vol(close, volume)
    def _r(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        v = np.sort(v)
        bot = v[:10].sum()
        top = v[-10:].sum()
        if bot <= 0:
            return np.nan
        return float(top / bot)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True)


def f21_dvit_036_top10_share_252_minus_504(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-10 dv share(252d) minus top-10 dv share(504d) — concentration shift."""
    dv = _dollar_vol(close, volume)
    return _rolling_topn_share(dv, YDAYS, 10) - _rolling_topn_share(dv, DDAYS_2Y, 10)


# ============================================================
# Bucket F — Inequality / entropy measures (037-044)
# ============================================================

def f21_dvit_037_gini_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling Gini coefficient of dollar-volume over 252d — distribution inequality."""
    return _rolling_gini(_dollar_vol(close, volume), YDAYS)


def f21_dvit_038_hhi_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling Herfindahl-Hirschman index of dollar-volume shares over 252d."""
    return _rolling_hhi_norm(_dollar_vol(close, volume), YDAYS)


def f21_dvit_039_theil_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling Theil index of dollar-volume over 252d."""
    return _rolling_theil(_dollar_vol(close, volume), YDAYS)


def f21_dvit_040_shannon_entropy_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling Shannon entropy of binned log-dollar-volume over 252d."""
    return _rolling_entropy_bins(_safe_log(_dollar_vol(close, volume)), YDAYS, bins=10)


def f21_dvit_041_shannon_entropy_log_dv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling Shannon entropy of binned log-dollar-volume over 63d."""
    return _rolling_entropy_bins(_safe_log(_dollar_vol(close, volume)), QDAYS, bins=8)


def f21_dvit_042_lorenz_area_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lorenz curve area under (1 - Lorenz) for dollar-volume over 252d — alternative inequality measure."""
    dv = _dollar_vol(close, volume)
    def _l(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        v = np.sort(v)
        cum = np.cumsum(v) / v.sum() if v.sum() > 0 else None
        if cum is None:
            return np.nan
        return float(0.5 - cum.mean() + 0.5 / v.size)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_l, raw=True)


def f21_dvit_043_entropy_change_63_minus_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy(63d) minus Shannon entropy(252d) of log dollar-volume."""
    ldv = _safe_log(_dollar_vol(close, volume))
    e63 = _rolling_entropy_bins(ldv, QDAYS, bins=8)
    e252 = _rolling_entropy_bins(ldv, YDAYS, bins=10)
    return e63 - e252


def f21_dvit_044_entropy_change_21_minus_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy(21d) minus Shannon entropy(252d) of log dollar-volume."""
    ldv = _safe_log(_dollar_vol(close, volume))
    e21 = _rolling_entropy_bins(ldv, MDAYS, bins=5)
    e252 = _rolling_entropy_bins(ldv, YDAYS, bins=10)
    return e21 - e252


# ============================================================
# Bucket G — Spike counts (045-052)
# ============================================================

def f21_dvit_045_count_dv_above_2sigma_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with log-dv z(252d) > 2."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_046_count_dv_above_3sigma_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with log-dv z(252d) > 3."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_047_count_dv_above_4sigma_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with log-dv z(252d) > 4 — extreme bursts."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z > 4.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_048_count_dv_above_2sigma_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars with log-dv z(63d) > 2."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), QDAYS)
    return (z > 2.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_049_count_dv_above_3sigma_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars with log-dv z(63d) > 3."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), QDAYS)
    return (z > 3.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_050_dv_spike_intensity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (z - 2)+ — total excess intensity above 2-sigma threshold."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z - 2.0).clip(lower=0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_051_dv_spike_intensity_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d sum of (z - 2)+ — quarterly excess intensity."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), QDAYS)
    return (z - 2.0).clip(lower=0.0).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_052_bars_since_last_3sigma_dv_spike_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last 3-sigma log-dv spike (capped at 252)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    flag = (z > 3.0).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


# ============================================================
# Bucket H — Breadth above long-run averages (053-058)
# ============================================================

def f21_dvit_053_frac_dv_above_252d_avg_in_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63d with dv above 252d trailing average."""
    dv = _dollar_vol(close, volume)
    avg = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return (dv > avg).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f21_dvit_054_frac_dv_above_252d_med_in_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63d with dv above 252d trailing median."""
    dv = _dollar_vol(close, volume)
    med = dv.rolling(YDAYS, min_periods=QDAYS).median()
    return (dv > med).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f21_dvit_055_frac_dv_above_504d_avg_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252d with dv above 504d trailing average — sustained-elevation breadth."""
    dv = _dollar_vol(close, volume)
    avg = dv.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return (dv > avg).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_056_frac_dv_above_5y_avg_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252d with dv above 5y trailing average — multi-year elevation breadth."""
    dv = _dollar_vol(close, volume)
    avg = dv.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return (dv > avg).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_057_breadth_above_LR_diff_short_long(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Frac(above 252d avg in 21d) minus frac(above 252d avg in 252d) — short-vs-long breadth shift."""
    dv = _dollar_vol(close, volume)
    avg = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (dv > avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean() - flag.rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_058_count_dv_above_long_avg_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d with dv above 5y average."""
    dv = _dollar_vol(close, volume)
    avg = dv.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return (dv > avg).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket I — Slope / momentum (059-066)
# ============================================================

def f21_dvit_059_slope_log_dv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of log dollar-volume over trailing 63d."""
    return _rolling_slope(_safe_log(_dollar_vol(close, volume)), QDAYS)


def f21_dvit_060_slope_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of log dollar-volume over trailing 252d."""
    return _rolling_slope(_safe_log(_dollar_vol(close, volume)), YDAYS)


def f21_dvit_061_slope_log_dv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of log dollar-volume over trailing 21d."""
    return _rolling_slope(_safe_log(_dollar_vol(close, volume)), MDAYS)


def f21_dvit_062_r2_log_dv_trend_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """R² of linear regression of log-dv over 252d — trend cleanliness."""
    ldv = _safe_log(_dollar_vol(close, volume))
    def _r2(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        x = np.arange(v.size, dtype=float)
        xm = x.mean(); ym = v.mean()
        sxx = ((x - xm) ** 2).sum()
        syy = ((v - ym) ** 2).sum()
        sxy = ((x - xm) * (v - ym)).sum()
        if sxx <= 0 or syy <= 0:
            return np.nan
        r = sxy / np.sqrt(sxx * syy)
        return float(r * r)
    return ldv.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)


def f21_dvit_063_roc_dv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of change of dollar-volume over 63d (current/63d-ago - 1)."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.shift(QDAYS)) - 1.0


def f21_dvit_064_roc_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of change of dollar-volume over 252d."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.shift(YDAYS)) - 1.0


def f21_dvit_065_cusum_pos_excess_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CUSUM of (log_dv - 252d median) clipped to positive side, summed over 252d — cumulative excess intensity."""
    ldv = _safe_log(_dollar_vol(close, volume))
    med = ldv.rolling(YDAYS, min_periods=QDAYS).median()
    return (ldv - med).clip(lower=0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_066_drawdown_from_running_max_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log_dv minus 252d trailing max log_dv — always <= 0; magnitude of post-peak deficit."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ldv - ldv.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket J — Divergence with price (067-072)
# ============================================================

def f21_dvit_067_ratio_price_roc_to_dv_roc_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """ROC of close(252d) divided by ROC of dollar-volume(252d) — high = price up more than dv up."""
    dv = _dollar_vol(close, volume)
    pr = _safe_div(close, close.shift(YDAYS)) - 1.0
    dr = _safe_div(dv, dv.shift(YDAYS)) - 1.0
    return _safe_div(pr, dr)


def f21_dvit_068_dv_minus_price_roc_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """ROC(dv, 252d) minus ROC(close, 252d) — negative = $-vol failing to confirm price."""
    dv = _dollar_vol(close, volume)
    return (_safe_div(dv, dv.shift(YDAYS)) - 1.0) - (_safe_div(close, close.shift(YDAYS)) - 1.0)


def f21_dvit_069_spearman_corr_dv_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spearman rank correlation between dollar-volume and close over 252d."""
    dv = _dollar_vol(close, volume)
    ra = dv.rolling(YDAYS, min_periods=QDAYS).rank()
    rb = close.rolling(YDAYS, min_periods=QDAYS).rank()
    return ra.rolling(YDAYS, min_periods=QDAYS).corr(rb)


def f21_dvit_070_spearman_corr_dv_price_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spearman rank correlation between dollar-volume and close over 63d."""
    dv = _dollar_vol(close, volume)
    ra = dv.rolling(QDAYS, min_periods=MDAYS).rank()
    rb = close.rolling(QDAYS, min_periods=MDAYS).rank()
    return ra.rolling(QDAYS, min_periods=MDAYS).corr(rb)


def f21_dvit_071_regression_residual_dv_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing-252d rolling residual: log-dv minus (a + b * log-close), where a/b are 252d OLS fits."""
    ldv = _safe_log(_dollar_vol(close, volume))
    lp = _safe_log(close)
    def _res(idx):
        x = lp.iloc[idx]; y = ldv.iloc[idx]
        mask = x.notna() & y.notna()
        if mask.sum() < 30:
            return np.nan
        xv = x[mask].values; yv = y[mask].values
        xm = xv.mean(); ym = yv.mean()
        sxx = ((xv - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        b = ((xv - xm) * (yv - ym)).sum() / sxx
        a = ym - b * xm
        last_x = x.iloc[-1]; last_y = y.iloc[-1]
        if not (np.isfinite(last_x) and np.isfinite(last_y)):
            return np.nan
        return float(last_y - (a + b * last_x))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _res(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_072_pct_rank_diff_dv_minus_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """pct_rank(dv, 252d) minus pct_rank(close, 252d) — negative = dv lagging price."""
    dv = _dollar_vol(close, volume)
    return _rolling_pct_rank(dv, YDAYS) - _rolling_pct_rank(close, YDAYS)


# ============================================================
# Bucket K — Autocorrelation / persistence (073-075)
# ============================================================

def f21_dvit_073_autocorr_lag1_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log dollar-volume over 252d."""
    return _safe_log(_dollar_vol(close, volume)).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _np_autocorr_lag(w, 1), raw=True)


def f21_dvit_074_autocorr_lag5_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of log dollar-volume over 252d."""
    return _safe_log(_dollar_vol(close, volume)).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _np_autocorr_lag(w, 5), raw=True)


def f21_dvit_075_autocorr_lag1_log_dv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log dollar-volume over 63d."""
    return _safe_log(_dollar_vol(close, volume)).rolling(QDAYS, min_periods=MDAYS).apply(lambda w: _np_autocorr_lag(w, 1), raw=True)


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f21_dvit_001_log_dv_zscore_252d_d1(close, volume):
    return f21_dvit_001_log_dv_zscore_252d(close, volume).diff()


def f21_dvit_002_log_dv_zscore_63d_d1(close, volume):
    return f21_dvit_002_log_dv_zscore_63d(close, volume).diff()


def f21_dvit_003_log_dv_zscore_504d_d1(close, volume):
    return f21_dvit_003_log_dv_zscore_504d(close, volume).diff()


def f21_dvit_004_log_dv_zscore_5y_d1(close, volume):
    return f21_dvit_004_log_dv_zscore_5y(close, volume).diff()


def f21_dvit_005_log_dv_robust_mad_z_252d_d1(close, volume):
    return f21_dvit_005_log_dv_robust_mad_z_252d(close, volume).diff()


def f21_dvit_006_log_dv_robust_mad_z_63d_d1(close, volume):
    return f21_dvit_006_log_dv_robust_mad_z_63d(close, volume).diff()


def f21_dvit_007_log_dv_zscore_252d_gated_at_252h_d1(high, close, volume):
    return f21_dvit_007_log_dv_zscore_252d_gated_at_252h(high, close, volume).diff()


def f21_dvit_008_log_dv_zscore_252d_minus_pre_baseline_d1(close, volume):
    return f21_dvit_008_log_dv_zscore_252d_minus_pre_baseline(close, volume).diff()


def f21_dvit_009_log_dv_pct_rank_252d_d1(close, volume):
    return f21_dvit_009_log_dv_pct_rank_252d(close, volume).diff()


def f21_dvit_010_log_dv_pct_rank_504d_d1(close, volume):
    return f21_dvit_010_log_dv_pct_rank_504d(close, volume).diff()


def f21_dvit_011_log_dv_pct_rank_63d_d1(close, volume):
    return f21_dvit_011_log_dv_pct_rank_63d(close, volume).diff()


def f21_dvit_012_log_dv_pct_rank_5y_d1(close, volume):
    return f21_dvit_012_log_dv_pct_rank_5y(close, volume).diff()


def f21_dvit_013_log_dv_pct_rank_diff_63_252_d1(close, volume):
    return f21_dvit_013_log_dv_pct_rank_diff_63_252(close, volume).diff()


def f21_dvit_014_log_dv_pct_rank_inv_252d_d1(close, volume):
    return f21_dvit_014_log_dv_pct_rank_inv_252d(close, volume).diff()


def f21_dvit_015_dv_to_median_252d_d1(close, volume):
    return f21_dvit_015_dv_to_median_252d(close, volume).diff()


def f21_dvit_016_dv_to_median_63d_d1(close, volume):
    return f21_dvit_016_dv_to_median_63d(close, volume).diff()


def f21_dvit_017_dv_to_trimmed_mean_252d_d1(close, volume):
    return f21_dvit_017_dv_to_trimmed_mean_252d(close, volume).diff()


def f21_dvit_018_dv_to_geomean_252d_d1(close, volume):
    return f21_dvit_018_dv_to_geomean_252d(close, volume).diff()


def f21_dvit_019_dv_to_max252_ratio_d1(close, volume):
    return f21_dvit_019_dv_to_max252_ratio(close, volume).diff()


def f21_dvit_020_dv_to_min252_ratio_d1(close, volume):
    return f21_dvit_020_dv_to_min252_ratio(close, volume).diff()


def f21_dvit_021_dv_to_q75_252d_d1(close, volume):
    return f21_dvit_021_dv_to_q75_252d(close, volume).diff()


def f21_dvit_022_dv_to_q25_252d_d1(close, volume):
    return f21_dvit_022_dv_to_q25_252d(close, volume).diff()


def f21_dvit_023_ratio_dv_mean_21d_to_252d_d1(close, volume):
    return f21_dvit_023_ratio_dv_mean_21d_to_252d(close, volume).diff()


def f21_dvit_024_ratio_dv_mean_63d_to_504d_d1(close, volume):
    return f21_dvit_024_ratio_dv_mean_63d_to_504d(close, volume).diff()


def f21_dvit_025_ratio_dv_mean_5d_to_63d_d1(close, volume):
    return f21_dvit_025_ratio_dv_mean_5d_to_63d(close, volume).diff()


def f21_dvit_026_ratio_dv_mean_21d_to_5y_d1(close, volume):
    return f21_dvit_026_ratio_dv_mean_21d_to_5y(close, volume).diff()


def f21_dvit_027_ratio_dv_median_21d_to_252d_d1(close, volume):
    return f21_dvit_027_ratio_dv_median_21d_to_252d(close, volume).diff()


def f21_dvit_028_regime_shift_indicator_3sigma_up_252d_d1(close, volume):
    return f21_dvit_028_regime_shift_indicator_3sigma_up_252d(close, volume).diff()


def f21_dvit_029_top1_dv_share_252d_d1(close, volume):
    return f21_dvit_029_top1_dv_share_252d(close, volume).diff()


def f21_dvit_030_top5_dv_share_252d_d1(close, volume):
    return f21_dvit_030_top5_dv_share_252d(close, volume).diff()


def f21_dvit_031_top10_dv_share_252d_d1(close, volume):
    return f21_dvit_031_top10_dv_share_252d(close, volume).diff()


def f21_dvit_032_top25_dv_share_252d_d1(close, volume):
    return f21_dvit_032_top25_dv_share_252d(close, volume).diff()


def f21_dvit_033_top1_dv_share_63d_d1(close, volume):
    return f21_dvit_033_top1_dv_share_63d(close, volume).diff()


def f21_dvit_034_top5_dv_share_63d_d1(close, volume):
    return f21_dvit_034_top5_dv_share_63d(close, volume).diff()


def f21_dvit_035_top10_to_bottom10_ratio_252d_d1(close, volume):
    return f21_dvit_035_top10_to_bottom10_ratio_252d(close, volume).diff()


def f21_dvit_036_top10_share_252_minus_504_d1(close, volume):
    return f21_dvit_036_top10_share_252_minus_504(close, volume).diff()


def f21_dvit_037_gini_dv_252d_d1(close, volume):
    return f21_dvit_037_gini_dv_252d(close, volume).diff()


def f21_dvit_038_hhi_dv_252d_d1(close, volume):
    return f21_dvit_038_hhi_dv_252d(close, volume).diff()


def f21_dvit_039_theil_dv_252d_d1(close, volume):
    return f21_dvit_039_theil_dv_252d(close, volume).diff()


def f21_dvit_040_shannon_entropy_log_dv_252d_d1(close, volume):
    return f21_dvit_040_shannon_entropy_log_dv_252d(close, volume).diff()


def f21_dvit_041_shannon_entropy_log_dv_63d_d1(close, volume):
    return f21_dvit_041_shannon_entropy_log_dv_63d(close, volume).diff()


def f21_dvit_042_lorenz_area_dv_252d_d1(close, volume):
    return f21_dvit_042_lorenz_area_dv_252d(close, volume).diff()


def f21_dvit_043_entropy_change_63_minus_252_d1(close, volume):
    return f21_dvit_043_entropy_change_63_minus_252(close, volume).diff()


def f21_dvit_044_entropy_change_21_minus_252_d1(close, volume):
    return f21_dvit_044_entropy_change_21_minus_252(close, volume).diff()


def f21_dvit_045_count_dv_above_2sigma_252d_d1(close, volume):
    return f21_dvit_045_count_dv_above_2sigma_252d(close, volume).diff()


def f21_dvit_046_count_dv_above_3sigma_252d_d1(close, volume):
    return f21_dvit_046_count_dv_above_3sigma_252d(close, volume).diff()


def f21_dvit_047_count_dv_above_4sigma_252d_d1(close, volume):
    return f21_dvit_047_count_dv_above_4sigma_252d(close, volume).diff()


def f21_dvit_048_count_dv_above_2sigma_63d_d1(close, volume):
    return f21_dvit_048_count_dv_above_2sigma_63d(close, volume).diff()


def f21_dvit_049_count_dv_above_3sigma_63d_d1(close, volume):
    return f21_dvit_049_count_dv_above_3sigma_63d(close, volume).diff()


def f21_dvit_050_dv_spike_intensity_252d_d1(close, volume):
    return f21_dvit_050_dv_spike_intensity_252d(close, volume).diff()


def f21_dvit_051_dv_spike_intensity_63d_d1(close, volume):
    return f21_dvit_051_dv_spike_intensity_63d(close, volume).diff()


def f21_dvit_052_bars_since_last_3sigma_dv_spike_252d_d1(close, volume):
    return f21_dvit_052_bars_since_last_3sigma_dv_spike_252d(close, volume).diff()


def f21_dvit_053_frac_dv_above_252d_avg_in_63d_d1(close, volume):
    return f21_dvit_053_frac_dv_above_252d_avg_in_63d(close, volume).diff()


def f21_dvit_054_frac_dv_above_252d_med_in_63d_d1(close, volume):
    return f21_dvit_054_frac_dv_above_252d_med_in_63d(close, volume).diff()


def f21_dvit_055_frac_dv_above_504d_avg_in_252d_d1(close, volume):
    return f21_dvit_055_frac_dv_above_504d_avg_in_252d(close, volume).diff()


def f21_dvit_056_frac_dv_above_5y_avg_in_252d_d1(close, volume):
    return f21_dvit_056_frac_dv_above_5y_avg_in_252d(close, volume).diff()


def f21_dvit_057_breadth_above_LR_diff_short_long_d1(close, volume):
    return f21_dvit_057_breadth_above_LR_diff_short_long(close, volume).diff()


def f21_dvit_058_count_dv_above_long_avg_252d_d1(close, volume):
    return f21_dvit_058_count_dv_above_long_avg_252d(close, volume).diff()


def f21_dvit_059_slope_log_dv_63d_d1(close, volume):
    return f21_dvit_059_slope_log_dv_63d(close, volume).diff()


def f21_dvit_060_slope_log_dv_252d_d1(close, volume):
    return f21_dvit_060_slope_log_dv_252d(close, volume).diff()


def f21_dvit_061_slope_log_dv_21d_d1(close, volume):
    return f21_dvit_061_slope_log_dv_21d(close, volume).diff()


def f21_dvit_062_r2_log_dv_trend_252d_d1(close, volume):
    return f21_dvit_062_r2_log_dv_trend_252d(close, volume).diff()


def f21_dvit_063_roc_dv_63d_d1(close, volume):
    return f21_dvit_063_roc_dv_63d(close, volume).diff()


def f21_dvit_064_roc_dv_252d_d1(close, volume):
    return f21_dvit_064_roc_dv_252d(close, volume).diff()


def f21_dvit_065_cusum_pos_excess_log_dv_252d_d1(close, volume):
    return f21_dvit_065_cusum_pos_excess_log_dv_252d(close, volume).diff()


def f21_dvit_066_drawdown_from_running_max_log_dv_252d_d1(close, volume):
    return f21_dvit_066_drawdown_from_running_max_log_dv_252d(close, volume).diff()


def f21_dvit_067_ratio_price_roc_to_dv_roc_252d_d1(close, volume):
    return f21_dvit_067_ratio_price_roc_to_dv_roc_252d(close, volume).diff()


def f21_dvit_068_dv_minus_price_roc_252d_d1(close, volume):
    return f21_dvit_068_dv_minus_price_roc_252d(close, volume).diff()


def f21_dvit_069_spearman_corr_dv_price_252d_d1(close, volume):
    return f21_dvit_069_spearman_corr_dv_price_252d(close, volume).diff()


def f21_dvit_070_spearman_corr_dv_price_63d_d1(close, volume):
    return f21_dvit_070_spearman_corr_dv_price_63d(close, volume).diff()


def f21_dvit_071_regression_residual_dv_price_252d_d1(close, volume):
    return f21_dvit_071_regression_residual_dv_price_252d(close, volume).diff()


def f21_dvit_072_pct_rank_diff_dv_minus_price_252d_d1(close, volume):
    return f21_dvit_072_pct_rank_diff_dv_minus_price_252d(close, volume).diff()


def f21_dvit_073_autocorr_lag1_log_dv_252d_d1(close, volume):
    return f21_dvit_073_autocorr_lag1_log_dv_252d(close, volume).diff()


def f21_dvit_074_autocorr_lag5_log_dv_252d_d1(close, volume):
    return f21_dvit_074_autocorr_lag5_log_dv_252d(close, volume).diff()


def f21_dvit_075_autocorr_lag1_log_dv_63d_d1(close, volume):
    return f21_dvit_075_autocorr_lag1_log_dv_63d(close, volume).diff()


DOLLAR_VOLUME_INTENSITY_D1_REGISTRY_001_075 = {
    "f21_dvit_001_log_dv_zscore_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_001_log_dv_zscore_252d_d1},
    "f21_dvit_002_log_dv_zscore_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_002_log_dv_zscore_63d_d1},
    "f21_dvit_003_log_dv_zscore_504d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_003_log_dv_zscore_504d_d1},
    "f21_dvit_004_log_dv_zscore_5y_d1": {"inputs": ["close", "volume"], "func": f21_dvit_004_log_dv_zscore_5y_d1},
    "f21_dvit_005_log_dv_robust_mad_z_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_005_log_dv_robust_mad_z_252d_d1},
    "f21_dvit_006_log_dv_robust_mad_z_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_006_log_dv_robust_mad_z_63d_d1},
    "f21_dvit_007_log_dv_zscore_252d_gated_at_252h_d1": {"inputs": ["high", "close", "volume"], "func": f21_dvit_007_log_dv_zscore_252d_gated_at_252h_d1},
    "f21_dvit_008_log_dv_zscore_252d_minus_pre_baseline_d1": {"inputs": ["close", "volume"], "func": f21_dvit_008_log_dv_zscore_252d_minus_pre_baseline_d1},
    "f21_dvit_009_log_dv_pct_rank_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_009_log_dv_pct_rank_252d_d1},
    "f21_dvit_010_log_dv_pct_rank_504d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_010_log_dv_pct_rank_504d_d1},
    "f21_dvit_011_log_dv_pct_rank_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_011_log_dv_pct_rank_63d_d1},
    "f21_dvit_012_log_dv_pct_rank_5y_d1": {"inputs": ["close", "volume"], "func": f21_dvit_012_log_dv_pct_rank_5y_d1},
    "f21_dvit_013_log_dv_pct_rank_diff_63_252_d1": {"inputs": ["close", "volume"], "func": f21_dvit_013_log_dv_pct_rank_diff_63_252_d1},
    "f21_dvit_014_log_dv_pct_rank_inv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_014_log_dv_pct_rank_inv_252d_d1},
    "f21_dvit_015_dv_to_median_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_015_dv_to_median_252d_d1},
    "f21_dvit_016_dv_to_median_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_016_dv_to_median_63d_d1},
    "f21_dvit_017_dv_to_trimmed_mean_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_017_dv_to_trimmed_mean_252d_d1},
    "f21_dvit_018_dv_to_geomean_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_018_dv_to_geomean_252d_d1},
    "f21_dvit_019_dv_to_max252_ratio_d1": {"inputs": ["close", "volume"], "func": f21_dvit_019_dv_to_max252_ratio_d1},
    "f21_dvit_020_dv_to_min252_ratio_d1": {"inputs": ["close", "volume"], "func": f21_dvit_020_dv_to_min252_ratio_d1},
    "f21_dvit_021_dv_to_q75_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_021_dv_to_q75_252d_d1},
    "f21_dvit_022_dv_to_q25_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_022_dv_to_q25_252d_d1},
    "f21_dvit_023_ratio_dv_mean_21d_to_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_023_ratio_dv_mean_21d_to_252d_d1},
    "f21_dvit_024_ratio_dv_mean_63d_to_504d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_024_ratio_dv_mean_63d_to_504d_d1},
    "f21_dvit_025_ratio_dv_mean_5d_to_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_025_ratio_dv_mean_5d_to_63d_d1},
    "f21_dvit_026_ratio_dv_mean_21d_to_5y_d1": {"inputs": ["close", "volume"], "func": f21_dvit_026_ratio_dv_mean_21d_to_5y_d1},
    "f21_dvit_027_ratio_dv_median_21d_to_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_027_ratio_dv_median_21d_to_252d_d1},
    "f21_dvit_028_regime_shift_indicator_3sigma_up_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_028_regime_shift_indicator_3sigma_up_252d_d1},
    "f21_dvit_029_top1_dv_share_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_029_top1_dv_share_252d_d1},
    "f21_dvit_030_top5_dv_share_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_030_top5_dv_share_252d_d1},
    "f21_dvit_031_top10_dv_share_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_031_top10_dv_share_252d_d1},
    "f21_dvit_032_top25_dv_share_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_032_top25_dv_share_252d_d1},
    "f21_dvit_033_top1_dv_share_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_033_top1_dv_share_63d_d1},
    "f21_dvit_034_top5_dv_share_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_034_top5_dv_share_63d_d1},
    "f21_dvit_035_top10_to_bottom10_ratio_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_035_top10_to_bottom10_ratio_252d_d1},
    "f21_dvit_036_top10_share_252_minus_504_d1": {"inputs": ["close", "volume"], "func": f21_dvit_036_top10_share_252_minus_504_d1},
    "f21_dvit_037_gini_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_037_gini_dv_252d_d1},
    "f21_dvit_038_hhi_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_038_hhi_dv_252d_d1},
    "f21_dvit_039_theil_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_039_theil_dv_252d_d1},
    "f21_dvit_040_shannon_entropy_log_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_040_shannon_entropy_log_dv_252d_d1},
    "f21_dvit_041_shannon_entropy_log_dv_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_041_shannon_entropy_log_dv_63d_d1},
    "f21_dvit_042_lorenz_area_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_042_lorenz_area_dv_252d_d1},
    "f21_dvit_043_entropy_change_63_minus_252_d1": {"inputs": ["close", "volume"], "func": f21_dvit_043_entropy_change_63_minus_252_d1},
    "f21_dvit_044_entropy_change_21_minus_252_d1": {"inputs": ["close", "volume"], "func": f21_dvit_044_entropy_change_21_minus_252_d1},
    "f21_dvit_045_count_dv_above_2sigma_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_045_count_dv_above_2sigma_252d_d1},
    "f21_dvit_046_count_dv_above_3sigma_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_046_count_dv_above_3sigma_252d_d1},
    "f21_dvit_047_count_dv_above_4sigma_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_047_count_dv_above_4sigma_252d_d1},
    "f21_dvit_048_count_dv_above_2sigma_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_048_count_dv_above_2sigma_63d_d1},
    "f21_dvit_049_count_dv_above_3sigma_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_049_count_dv_above_3sigma_63d_d1},
    "f21_dvit_050_dv_spike_intensity_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_050_dv_spike_intensity_252d_d1},
    "f21_dvit_051_dv_spike_intensity_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_051_dv_spike_intensity_63d_d1},
    "f21_dvit_052_bars_since_last_3sigma_dv_spike_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_052_bars_since_last_3sigma_dv_spike_252d_d1},
    "f21_dvit_053_frac_dv_above_252d_avg_in_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_053_frac_dv_above_252d_avg_in_63d_d1},
    "f21_dvit_054_frac_dv_above_252d_med_in_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_054_frac_dv_above_252d_med_in_63d_d1},
    "f21_dvit_055_frac_dv_above_504d_avg_in_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_055_frac_dv_above_504d_avg_in_252d_d1},
    "f21_dvit_056_frac_dv_above_5y_avg_in_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_056_frac_dv_above_5y_avg_in_252d_d1},
    "f21_dvit_057_breadth_above_LR_diff_short_long_d1": {"inputs": ["close", "volume"], "func": f21_dvit_057_breadth_above_LR_diff_short_long_d1},
    "f21_dvit_058_count_dv_above_long_avg_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_058_count_dv_above_long_avg_252d_d1},
    "f21_dvit_059_slope_log_dv_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_059_slope_log_dv_63d_d1},
    "f21_dvit_060_slope_log_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_060_slope_log_dv_252d_d1},
    "f21_dvit_061_slope_log_dv_21d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_061_slope_log_dv_21d_d1},
    "f21_dvit_062_r2_log_dv_trend_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_062_r2_log_dv_trend_252d_d1},
    "f21_dvit_063_roc_dv_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_063_roc_dv_63d_d1},
    "f21_dvit_064_roc_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_064_roc_dv_252d_d1},
    "f21_dvit_065_cusum_pos_excess_log_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_065_cusum_pos_excess_log_dv_252d_d1},
    "f21_dvit_066_drawdown_from_running_max_log_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_066_drawdown_from_running_max_log_dv_252d_d1},
    "f21_dvit_067_ratio_price_roc_to_dv_roc_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_067_ratio_price_roc_to_dv_roc_252d_d1},
    "f21_dvit_068_dv_minus_price_roc_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_068_dv_minus_price_roc_252d_d1},
    "f21_dvit_069_spearman_corr_dv_price_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_069_spearman_corr_dv_price_252d_d1},
    "f21_dvit_070_spearman_corr_dv_price_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_070_spearman_corr_dv_price_63d_d1},
    "f21_dvit_071_regression_residual_dv_price_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_071_regression_residual_dv_price_252d_d1},
    "f21_dvit_072_pct_rank_diff_dv_minus_price_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_072_pct_rank_diff_dv_minus_price_252d_d1},
    "f21_dvit_073_autocorr_lag1_log_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_073_autocorr_lag1_log_dv_252d_d1},
    "f21_dvit_074_autocorr_lag5_log_dv_252d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_074_autocorr_lag5_log_dv_252d_d1},
    "f21_dvit_075_autocorr_lag1_log_dv_63d_d1": {"inputs": ["close", "volume"], "func": f21_dvit_075_autocorr_lag1_log_dv_63d_d1},
}
