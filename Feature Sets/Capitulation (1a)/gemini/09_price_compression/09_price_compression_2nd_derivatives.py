"""
Price Compression — 2nd Derivatives
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

def pcmp_drv2_001_hl_range_ratio_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_001_hl_range_ratio_velocity feature"""
    r = (high - low) / ((high + low) / 2.0)
    return r.diff(5)

def pcmp_drv2_002_vol_compression_ratio_velocity(close: pd.Series) -> pd.Series:
    """pcmp_drv2_002_vol_compression_ratio_velocity feature"""
    v21 = close.pct_change().rolling(21).std()
    v252 = close.pct_change().rolling(252).std()
    ratio = _safe_div(v21, v252)
    return ratio.diff(5)

def pcmp_drv2_003_bb_width_velocity(close: pd.Series) -> pd.Series:
    """pcmp_drv2_003_bb_width_velocity feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    bw = _safe_div(4 * std, ma)
    return bw.diff(5)

def pcmp_drv2_004_close_clustering_velocity(close: pd.Series) -> pd.Series:
    """pcmp_drv2_004_close_clustering_velocity feature"""
    ci = _safe_div(close.rolling(21).std(), close.rolling(21).mean())
    return ci.diff(5)

def pcmp_drv2_005_high_low_overlap_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_005_high_low_overlap_velocity feature"""
    h_min = high.rolling(5).min()
    l_max = low.rolling(5).max()
    common = (h_min - l_max).clip(lower=0)
    total = high.rolling(5).max() - low.rolling(5).min()
    ratio = _safe_div(common, total)
    return ratio.diff(5)

def pcmp_drv2_006_tightness_composite_velocity(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_006_tightness_composite_velocity feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    bbw = _safe_div(4 * std, ma)
    v21 = close.pct_change().rolling(21).std()
    v252 = close.pct_change().rolling(252).std()
    vr = _safe_div(v21, v252)
    hlr = (high - low) / ((high + low) / 2.0)
    comp = (bbw + vr + hlr) / 3.0
    return comp.diff(5)

def pcmp_drv2_007_terminal_range_stability_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_007_terminal_range_stability_velocity feature"""
    r = high - low
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = r.rolling(21).apply(_rsq, raw=True)
    return rs.diff(5)

def pcmp_drv2_008_proximity_to_apex_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_008_proximity_to_apex_velocity feature"""
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sh = high.rolling(21).apply(_slope, raw=True)
    sl = low.rolling(21).apply(_slope, raw=True)
    apex = sh - sl
    return apex.diff(5)

def pcmp_drv2_009_atr_zscore_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_drv2_009_atr_zscore_velocity feature"""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14).mean()
    z = (atr - atr.rolling(252).mean()) / atr.rolling(252).std()
    return z.diff(5)

def pcmp_drv2_010_price_point_density_velocity(close: pd.Series) -> pd.Series:
    """pcmp_drv2_010_price_point_density_velocity feature"""
    pdens = close.rolling(63).apply(lambda x: len(np.unique(x)) / 63.0, raw=True)
    return pdens.diff(5)

def pcmp_drv2_011_parkinson_vol_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_011_parkinson_vol_velocity feature"""
    p = np.sqrt((1 / (4 * np.log(2))) * (np.log(high / low)**2)).rolling(21).mean()
    return p.diff(5)

def pcmp_drv2_012_gk_vol_velocity(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_drv2_012_gk_vol_velocity feature"""
    gk = np.sqrt(0.5 * (np.log(high / low)**2) - (2 * np.log(2) - 1) * (np.log(close / open)**2)).rolling(21).mean()
    return gk.diff(5)

def pcmp_drv2_013_vol_compression_slope_velocity(close: pd.Series) -> pd.Series:
    """pcmp_drv2_013_vol_compression_slope_velocity feature"""
    v = close.pct_change().rolling(21).std()
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = v.rolling(63).apply(_slope, raw=True)
    return sl.diff(5)

def pcmp_drv2_014_range_compression_slope_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_014_range_compression_slope_velocity feature"""
    r = high - low
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = r.rolling(63).apply(_slope, raw=True)
    return sl.diff(5)

def pcmp_drv2_015_volatility_crash_velocity(close: pd.Series) -> pd.Series:
    """pcmp_drv2_015_volatility_crash_velocity feature"""
    v5 = close.pct_change().rolling(5).std()
    v252 = close.pct_change().rolling(252).std()
    vc = _safe_div(v5, v252)
    return vc.diff(5)

def pcmp_drv2_016_mktcap_tightness_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """pcmp_drv2_016_mktcap_tightness_velocity feature"""
    mc = close * sharesbas
    v = mc.pct_change().rolling(21).std()
    ratio = _safe_div(v, v.rolling(63).mean())
    return ratio.diff(5)

def pcmp_drv2_017_underwater_compression_velocity(close: pd.Series) -> pd.Series:
    """pcmp_drv2_017_underwater_compression_velocity feature"""
    h = close.rolling(252).max()
    uw = (close - h) / h
    comp = uw.rolling(63).std()
    return comp.diff(5)

def pcmp_drv2_018_range_fractal_dim_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_018_range_fractal_dim_velocity feature"""
    r = high - low
    fd = _safe_div(np.log(r.rolling(21).sum()), np.log(21))
    return fd.diff(5)

def pcmp_drv2_019_range_oscillation_decay_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_019_range_oscillation_decay_velocity feature"""
    r = high - low
    dec = r.rolling(63).std() / r.rolling(63).mean()
    return dec.diff(5)

def pcmp_drv2_020_terminal_tightness_climax_velocity(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_020_terminal_tightness_climax_velocity feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    bbw = _safe_div(4 * std, ma)
    v = close.pct_change().rolling(21).std()
    l = close.rolling(252).min()
    prox = _safe_div(close, l)
    score = _safe_div(1.0, bbw * v * prox)
    return score.diff(5)

def pcmp_drv2_021_keltner_width_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_drv2_021_keltner_width_velocity feature"""
    ema = close.ewm(span=20).mean()
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(20).mean()
    kw = _safe_div(atr, ema)
    return kw.diff(5)

def pcmp_drv2_022_candle_wick_compression_velocity(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_drv2_022_candle_wick_compression_velocity feature"""
    wick = (high - low) - (close - open).abs()
    ratio = _safe_div(wick.rolling(21).mean(), (high - low).rolling(21).mean())
    return ratio.diff(5)

def pcmp_drv2_023_price_sideways_velocity(close: pd.Series) -> pd.Series:
    """pcmp_drv2_023_price_sideways_velocity feature"""
    near = (close / close.shift(5) - 1).abs() < 0.02
    dur = near.astype(int).groupby((near != near.shift()).cumsum()).cumsum()
    return dur.diff(5)

def pcmp_drv2_024_consecutive_tight_days_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_drv2_024_consecutive_tight_days_velocity feature"""
    r = high - low
    is_tight = (r < 0.5 * r.rolling(252).mean()).astype(int)
    cnt = is_tight.rolling(63).sum()
    return cnt.diff(5)

def pcmp_drv2_025_revenue_ps_compression_velocity(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """pcmp_drv2_025_revenue_ps_compression_velocity feature"""
    revps = _safe_div(revenue, sharesbas)
    v = revps.pct_change().rolling(4).std()
    ratio = _safe_div(v, v.expanding().mean())
    return ratio.diff(1) # diff 1 for quarterly data

# ── Registry ──────────────────────────────────────────────────────────────────

V09_V_REGISTRY = {
    "pcmp_drv2_001_hl_range_ratio_velocity": {"inputs": ["high", "low"], "func": pcmp_drv2_001_hl_range_ratio_velocity},
    "pcmp_drv2_002_vol_compression_ratio_velocity": {"inputs": ["close"], "func": pcmp_drv2_002_vol_compression_ratio_velocity},
    "pcmp_drv2_003_bb_width_velocity": {"inputs": ["close"], "func": pcmp_drv2_003_bb_width_velocity},
    "pcmp_drv2_004_close_clustering_velocity": {"inputs": ["close"], "func": pcmp_drv2_004_close_clustering_velocity},
    "pcmp_drv2_005_high_low_overlap_velocity": {"inputs": ["high", "low"], "func": pcmp_drv2_005_high_low_overlap_velocity},
    "pcmp_drv2_006_tightness_composite_velocity": {"inputs": ["close", "high", "low"], "func": pcmp_drv2_006_tightness_composite_velocity},
    "pcmp_drv2_007_terminal_range_stability_velocity": {"inputs": ["high", "low"], "func": pcmp_drv2_007_terminal_range_stability_velocity},
    "pcmp_drv2_008_proximity_to_apex_velocity": {"inputs": ["high", "low"], "func": pcmp_drv2_008_proximity_to_apex_velocity},
    "pcmp_drv2_009_atr_zscore_velocity": {"inputs": ["high", "low", "close"], "func": pcmp_drv2_009_atr_zscore_velocity},
    "pcmp_drv2_010_price_point_density_velocity": {"inputs": ["close"], "func": pcmp_drv2_010_price_point_density_velocity},
    "pcmp_drv2_011_parkinson_vol_velocity": {"inputs": ["high", "low"], "func": pcmp_drv2_011_parkinson_vol_velocity},
    "pcmp_drv2_012_gk_vol_velocity": {"inputs": ["high", "low", "open", "close"], "func": pcmp_drv2_012_gk_vol_velocity},
    "pcmp_drv2_013_vol_compression_slope_velocity": {"inputs": ["close"], "func": pcmp_drv2_013_vol_compression_slope_velocity},
    "pcmp_drv2_014_range_compression_slope_velocity": {"inputs": ["high", "low"], "func": pcmp_drv2_014_range_compression_slope_velocity},
    "pcmp_drv2_015_volatility_crash_velocity": {"inputs": ["close"], "func": pcmp_drv2_015_volatility_crash_velocity},
    "pcmp_drv2_016_mktcap_tightness_velocity": {"inputs": ["close", "sharesbas"], "func": pcmp_drv2_016_mktcap_tightness_velocity},
    "pcmp_drv2_017_underwater_compression_velocity": {"inputs": ["close"], "func": pcmp_drv2_017_underwater_compression_velocity},
    "pcmp_drv2_018_range_fractal_dim_velocity": {"inputs": ["high", "low"], "func": pcmp_drv2_018_range_fractal_dim_velocity},
    "pcmp_drv2_019_range_oscillation_decay_velocity": {"inputs": ["high", "low"], "func": pcmp_drv2_019_range_oscillation_decay_velocity},
    "pcmp_drv2_020_terminal_tightness_climax_velocity": {"inputs": ["close", "high", "low"], "func": pcmp_drv2_020_terminal_tightness_climax_velocity},
    "pcmp_drv2_021_keltner_width_velocity": {"inputs": ["high", "low", "close"], "func": pcmp_drv2_021_keltner_width_velocity},
    "pcmp_drv2_022_candle_wick_compression_velocity": {"inputs": ["high", "low", "open", "close"], "func": pcmp_drv2_022_candle_wick_compression_velocity},
    "pcmp_drv2_023_price_sideways_velocity": {"inputs": ["close"], "func": pcmp_drv2_023_price_sideways_velocity},
    "pcmp_drv2_024_consecutive_tight_days_velocity": {"inputs": ["high", "low"], "func": pcmp_drv2_024_consecutive_tight_days_velocity},
    "pcmp_drv2_025_revenue_ps_compression_velocity": {"inputs": ["revenue", "sharesbas"], "func": pcmp_drv2_025_revenue_ps_compression_velocity},
}
