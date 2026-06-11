"""
Price Compression — 3rd Derivatives
Domain: range contraction and expansion
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=1).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))

def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change().fillna(0)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).median()

# Domain Specific Additions
def _days_since_high(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)

def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    new_highs = (s == cummax)
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(new_highs).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices

def _pct_change(s: pd.Series, periods: int = 1) -> pd.Series:
    prev = s.shift(periods)
    return _safe_div(s - prev, prev.abs())

# ── Feature functions ────────────────────────────────────────────────────────

def pcmp_drv3_001_hl_range_ratio_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_001_hl_range_ratio_jerk feature"""
    r = (high - low) / ((high + low) / 2.0)
    accel = r.diff(5)
    return accel.diff(5)

def pcmp_drv3_002_vol_compression_ratio_jerk(close: pd.Series) -> pd.Series:
    """pcmp_drv3_002_vol_compression_ratio_jerk feature"""
    v21 = close.pct_change().rolling(21).std()
    v252 = close.pct_change().rolling(252).std()
    ratio = _safe_div(v21, v252)
    accel = ratio.diff(5)
    return accel.diff(5)

def pcmp_drv3_003_bb_width_jerk(close: pd.Series) -> pd.Series:
    """pcmp_drv3_003_bb_width_jerk feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    bw = _safe_div(4 * std, ma)
    accel = bw.diff(5)
    return accel.diff(5)

def pcmp_drv3_004_close_clustering_jerk(close: pd.Series) -> pd.Series:
    """pcmp_drv3_004_close_clustering_jerk feature"""
    ci = _safe_div(close.rolling(21).std(), close.rolling(21).mean())
    accel = ci.diff(5)
    return accel.diff(5)

def pcmp_drv3_005_high_low_overlap_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_005_high_low_overlap_jerk feature"""
    h_min = high.rolling(5).min()
    l_max = low.rolling(5).max()
    common = (h_min - l_max).clip(lower=0)
    total = high.rolling(5).max() - low.rolling(5).min()
    ratio = _safe_div(common, total)
    accel = ratio.diff(5)
    return accel.diff(5)

def pcmp_drv3_006_tightness_composite_jerk(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_006_tightness_composite_jerk feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    bbw = _safe_div(4 * std, ma)
    v21 = close.pct_change().rolling(21).std()
    v252 = close.pct_change().rolling(252).std()
    vr = _safe_div(v21, v252)
    hlr = (high - low) / ((high + low) / 2.0)
    comp = (bbw + vr + hlr) / 3.0
    accel = comp.diff(5)
    return accel.diff(5)

def pcmp_drv3_007_terminal_range_stability_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_007_terminal_range_stability_jerk feature"""
    r = high - low
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = r.rolling(21).apply(_rsq, raw=True)
    accel = rs.diff(5)
    return accel.diff(5)

def pcmp_drv3_008_proximity_to_apex_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_008_proximity_to_apex_jerk feature"""
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sh = high.rolling(21).apply(_slope, raw=True)
    sl = low.rolling(21).apply(_slope, raw=True)
    apex = sh - sl
    accel = apex.diff(5)
    return accel.diff(5)

def pcmp_drv3_009_atr_zscore_jerk(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_drv3_009_atr_zscore_jerk feature"""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14).mean()
    z = (atr - atr.rolling(252).mean()) / atr.rolling(252).std()
    accel = z.diff(5)
    return accel.diff(5)

def pcmp_drv3_010_price_point_density_jerk(close: pd.Series) -> pd.Series:
    """pcmp_drv3_010_price_point_density_jerk feature"""
    pdens = close.rolling(63).apply(lambda x: len(np.unique(x)) / 63.0, raw=True)
    accel = pdens.diff(5)
    return accel.diff(5)

def pcmp_drv3_011_parkinson_vol_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_011_parkinson_vol_jerk feature"""
    p = np.sqrt((1 / (4 * np.log(2))) * (np.log(high / low)**2)).rolling(21).mean()
    accel = p.diff(5)
    return accel.diff(5)

def pcmp_drv3_012_gk_vol_jerk(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_drv3_012_gk_vol_jerk feature"""
    gk = np.sqrt(0.5 * (np.log(high / low)**2) - (2 * np.log(2) - 1) * (np.log(close / open)**2)).rolling(21).mean()
    accel = gk.diff(5)
    return accel.diff(5)

def pcmp_drv3_013_vol_compression_slope_jerk(close: pd.Series) -> pd.Series:
    """pcmp_drv3_013_vol_compression_slope_jerk feature"""
    v = close.pct_change().rolling(21).std()
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = v.rolling(63).apply(_slope, raw=True)
    accel = sl.diff(5)
    return accel.diff(5)

def pcmp_drv3_014_range_compression_slope_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_014_range_compression_slope_jerk feature"""
    r = high - low
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = r.rolling(63).apply(_slope, raw=True)
    accel = sl.diff(5)
    return accel.diff(5)

def pcmp_drv3_015_volatility_crash_jerk(close: pd.Series) -> pd.Series:
    """pcmp_drv3_015_volatility_crash_jerk feature"""
    v5 = close.pct_change().rolling(5).std()
    v252 = close.pct_change().rolling(252).std()
    vc = _safe_div(v5, v252)
    accel = vc.diff(5)
    return accel.diff(5)

def pcmp_drv3_016_mktcap_tightness_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """pcmp_drv3_016_mktcap_tightness_jerk feature"""
    mc = close * sharesbas
    v = mc.pct_change().rolling(21).std()
    ratio = _safe_div(v, v.rolling(63).mean())
    accel = ratio.diff(5)
    return accel.diff(5)

def pcmp_drv3_017_underwater_compression_jerk(close: pd.Series) -> pd.Series:
    """pcmp_drv3_017_underwater_compression_jerk feature"""
    h = close.rolling(252).max()
    uw = (close - h) / h
    comp = uw.rolling(63).std()
    accel = comp.diff(5)
    return accel.diff(5)

def pcmp_drv3_018_range_fractal_dim_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_018_range_fractal_dim_jerk feature"""
    r = high - low
    fd = _safe_div(np.log(r.rolling(21).sum()), np.log(21))
    accel = fd.diff(5)
    return accel.diff(5)

def pcmp_drv3_019_range_oscillation_decay_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_019_range_oscillation_decay_jerk feature"""
    r = high - low
    dec = r.rolling(63).std() / r.rolling(63).mean()
    accel = dec.diff(5)
    return accel.diff(5)

def pcmp_drv3_020_terminal_tightness_climax_jerk(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_020_terminal_tightness_climax_jerk feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    bbw = _safe_div(4 * std, ma)
    v = close.pct_change().rolling(21).std()
    l = close.rolling(252).min()
    prox = _safe_div(close, l)
    score = _safe_div(1.0, bbw * v * prox)
    accel = score.diff(5)
    return accel.diff(5)

def pcmp_drv3_021_keltner_width_jerk(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_drv3_021_keltner_width_jerk feature"""
    ema = close.ewm(span=20).mean()
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(20).mean()
    kw = _safe_div(atr, ema)
    accel = kw.diff(5)
    return accel.diff(5)

def pcmp_drv3_022_candle_wick_compression_jerk(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_drv3_022_candle_wick_compression_jerk feature"""
    wick = (high - low) - (close - open).abs()
    ratio = _safe_div(wick.rolling(21).mean(), (high - low).rolling(21).mean())
    accel = ratio.diff(5)
    return accel.diff(5)

def pcmp_drv3_023_price_sideways_jerk(close: pd.Series) -> pd.Series:
    """pcmp_drv3_023_price_sideways_jerk feature"""
    near = (close / close.shift(5) - 1).abs() < 0.02
    dur = near.astype(int).groupby((near != near.shift()).cumsum()).cumsum()
    accel = dur.diff(5)
    return accel.diff(5)

def pcmp_drv3_024_consecutive_tight_days_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv3_024_consecutive_tight_days_jerk feature"""
    r = high - low
    is_tight = (r < 0.5 * r.rolling(252).mean()).astype(int)
    cnt = is_tight.rolling(63).sum()
    accel = cnt.diff(5)
    return accel.diff(5)

def pcmp_drv3_025_revenue_ps_compression_jerk(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """pcmp_drv3_025_revenue_ps_compression_jerk feature"""
    revps = _safe_div(revenue, sharesbas)
    v = revps.pct_change().rolling(4).std()
    ratio = _safe_div(v, v.expanding().mean())
    accel = ratio.diff(1)
    return accel.diff(1)

# ── Registry ──────────────────────────────────────────────────────────────────

V09_A_REGISTRY = {
    "pcmp_drv3_001_hl_range_ratio_jerk": {"inputs": ["high", "low"], "func": pcmp_drv3_001_hl_range_ratio_jerk},
    "pcmp_drv3_002_vol_compression_ratio_jerk": {"inputs": ["close"], "func": pcmp_drv3_002_vol_compression_ratio_jerk},
    "pcmp_drv3_003_bb_width_jerk": {"inputs": ["close"], "func": pcmp_drv3_003_bb_width_jerk},
    "pcmp_drv3_004_close_clustering_jerk": {"inputs": ["close"], "func": pcmp_drv3_004_close_clustering_jerk},
    "pcmp_drv3_005_high_low_overlap_jerk": {"inputs": ["high", "low"], "func": pcmp_drv3_005_high_low_overlap_jerk},
    "pcmp_drv3_006_tightness_composite_jerk": {"inputs": ["close", "high", "low"], "func": pcmp_drv3_006_tightness_composite_jerk},
    "pcmp_drv3_007_terminal_range_stability_jerk": {"inputs": ["high", "low"], "func": pcmp_drv3_007_terminal_range_stability_jerk},
    "pcmp_drv3_008_proximity_to_apex_jerk": {"inputs": ["high", "low"], "func": pcmp_drv3_008_proximity_to_apex_jerk},
    "pcmp_drv3_009_atr_zscore_jerk": {"inputs": ["high", "low", "close"], "func": pcmp_drv3_009_atr_zscore_jerk},
    "pcmp_drv3_010_price_point_density_jerk": {"inputs": ["close"], "func": pcmp_drv3_010_price_point_density_jerk},
    "pcmp_drv3_011_parkinson_vol_jerk": {"inputs": ["high", "low"], "func": pcmp_drv3_011_parkinson_vol_jerk},
    "pcmp_drv3_012_gk_vol_jerk": {"inputs": ["high", "low", "open", "close"], "func": pcmp_drv3_012_gk_vol_jerk},
    "pcmp_drv3_013_vol_compression_slope_jerk": {"inputs": ["close"], "func": pcmp_drv3_013_vol_compression_slope_jerk},
    "pcmp_drv3_014_range_compression_slope_jerk": {"inputs": ["high", "low"], "func": pcmp_drv3_014_range_compression_slope_jerk},
    "pcmp_drv3_015_volatility_crash_jerk": {"inputs": ["close"], "func": pcmp_drv3_015_volatility_crash_jerk},
    "pcmp_drv3_016_mktcap_tightness_jerk": {"inputs": ["close", "sharesbas"], "func": pcmp_drv3_016_mktcap_tightness_jerk},
    "pcmp_drv3_017_underwater_compression_jerk": {"inputs": ["close"], "func": pcmp_drv3_017_underwater_compression_jerk},
    "pcmp_drv3_018_range_fractal_dim_jerk": {"inputs": ["high", "low"], "func": pcmp_drv3_018_range_fractal_dim_jerk},
    "pcmp_drv3_019_range_oscillation_decay_jerk": {"inputs": ["high", "low"], "func": pcmp_drv3_019_range_oscillation_decay_jerk},
    "pcmp_drv3_020_terminal_tightness_climax_jerk": {"inputs": ["close", "high", "low"], "func": pcmp_drv3_020_terminal_tightness_climax_jerk},
    "pcmp_drv3_021_keltner_width_jerk": {"inputs": ["high", "low", "close"], "func": pcmp_drv3_021_keltner_width_jerk},
    "pcmp_drv3_022_candle_wick_compression_jerk": {"inputs": ["high", "low", "open", "close"], "func": pcmp_drv3_022_candle_wick_compression_jerk},
    "pcmp_drv3_023_price_sideways_jerk": {"inputs": ["close"], "func": pcmp_drv3_023_price_sideways_jerk},
    "pcmp_drv3_024_consecutive_tight_days_jerk": {"inputs": ["high", "low"], "func": pcmp_drv3_024_consecutive_tight_days_jerk},
    "pcmp_drv3_025_revenue_ps_compression_jerk": {"inputs": ["revenue", "sharesbas"], "func": pcmp_drv3_025_revenue_ps_compression_jerk},
}
