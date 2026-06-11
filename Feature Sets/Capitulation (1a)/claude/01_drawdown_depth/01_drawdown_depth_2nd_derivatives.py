"""
01_drawdown_depth — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base drawdown features — captures acceleration of decline
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature computes a .diff(n) or slope/pct-change of a base-feature concept.
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (normalized by window length)."""
    idx = np.arange(w, dtype=float)
    idx_mean = idx.mean()
    idx_var = ((idx - idx_mean) ** 2).sum()

    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        num = ((xi - xi_m) * (x - x.mean())).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den

    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def dd_drv2_001_dd_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day first difference of the 252-day drawdown (velocity of deterioration)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dd.diff(5)


def dd_drv2_002_dd_ath_5d_diff(close: pd.Series) -> pd.Series:
    """5-day first difference of the ATH drawdown (velocity of ATH distress)."""
    h = close.expanding(min_periods=1).max()
    dd = _safe_div(close - h, h)
    return dd.diff(5)


def dd_drv2_003_dd_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day first difference of the 63-day drawdown."""
    dd = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    return dd.diff(5)


def dd_drv2_004_log_dd_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of log-space 252-day drawdown (log-velocity of decline)."""
    h = _rolling_max(close, _TD_YEAR)
    log_dd = _log_safe(close) - _log_safe(h)
    return log_dd.diff(5)


def dd_drv2_005_log_dd_ath_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of log ATH drawdown (monthly worsening in log-distance from peak)."""
    h = close.expanding(min_periods=1).max()
    log_dd = _log_safe(close) - _log_safe(h)
    return log_dd.diff(_TD_MON)


def dd_drv2_006_dd_vol_adj_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of volatility-adjusted 252-day drawdown."""
    h = _rolling_max(close, _TD_YEAR)
    dd = _safe_div(close - h, h)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    dd_v = _safe_div(dd, vol)
    return dd_v.diff(5)


def dd_drv2_007_underwater_frac_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day underwater fraction (pace of increasing distress days)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    below = (dd < 0).astype(float)
    frac = _rolling_mean(below, _TD_YEAR)
    return frac.diff(5)


def dd_drv2_008_avg_dd_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of rolling-mean 252-day drawdown (pace of worsening average)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    avg = _rolling_mean(dd, _TD_YEAR)
    return avg.diff(5)


def dd_drv2_009_dd_area_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day drawdown area (acceleration of area accumulation)."""
    dd = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    area = _rolling_sum(dd, _TD_QTR)
    return area.diff(5)


def dd_drv2_010_sma_cascade_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of SMA cascade alignment (fraction of SMAs below which close sits)."""
    below = (
        (close < _rolling_mean(close, _TD_MON)).astype(float) +
        (close < _rolling_mean(close, _TD_QTR)).astype(float) +
        (close < _rolling_mean(close, _TD_HALF)).astype(float) +
        (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    ) / 4.0
    return below.diff(5)


def dd_drv2_011_dd_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day drawdown z-score (acceleration of statistical extremity)."""
    h = _rolling_max(close, _TD_YEAR)
    dd = _safe_div(close - h, h)
    z = _zscore_rolling(dd, _TD_YEAR)
    return z.diff(5)


def dd_drv2_012_dd_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of 252-day drawdown."""
    h = _rolling_max(close, _TD_YEAR)
    dd = _safe_div(close - h, h)
    rank = dd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(5)


def dd_drv2_013_close_vs_sma200_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-vs-SMA200 ratio (speed of MA breakdown)."""
    ma200 = _rolling_mean(close, 200)
    dev = _safe_div(close - ma200, ma200)
    return dev.diff(5)


def dd_drv2_014_ema_cascade_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA cascade alignment fraction."""
    below = (
        (close < _ewm_mean(close, _TD_MON)).astype(float) +
        (close < _ewm_mean(close, _TD_QTR)).astype(float) +
        (close < _ewm_mean(close, 200)).astype(float)
    ) / 3.0
    return below.diff(5)


def dd_drv2_015_atr_norm_dd_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR-normalized 252-day drawdown."""
    atr = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    h = _rolling_max(close, _TD_YEAR)
    ratio = _safe_div(close - h, atr)
    return ratio.diff(5)


def dd_drv2_016_pct_b_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day Bollinger %B (speed of band breakdown)."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    upper = ma + 2 * sd
    lower = ma - 2 * sd
    pct_b = _safe_div(close - lower, upper - lower)
    return pct_b.diff(5)


def dd_drv2_017_rsi_14d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 14-day RSI (acceleration of momentum loss)."""
    delta = close.diff(1)
    up = delta.clip(lower=0)
    down = (-delta).clip(lower=0)
    avg_up = up.ewm(alpha=1 / 14, min_periods=7).mean()
    avg_dn = down.ewm(alpha=1 / 14, min_periods=7).mean()
    rs = _safe_div(avg_up, avg_dn)
    rsi = 100.0 - _safe_div(100.0, 1.0 + rs)
    return rsi.diff(5)


def dd_drv2_018_dd_252d_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 252-day drawdown over trailing 21 days (short-term trend)."""
    h = _rolling_max(close, _TD_YEAR)
    dd = _safe_div(close - h, h)
    return _linslope(dd, _TD_MON)


def dd_drv2_019_dd_ath_63d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of ATH drawdown over trailing 63 days."""
    h = close.expanding(min_periods=1).max()
    dd = _safe_div(close - h, h)
    return _linslope(dd, _TD_QTR)


def dd_drv2_020_log_dd_ath_5d_pct_change(close: pd.Series) -> pd.Series:
    """5-day percent change in ATH log-drawdown magnitude (relative worsening rate)."""
    h = close.expanding(min_periods=1).max()
    log_dd = (_log_safe(h) - _log_safe(close)).clip(lower=_EPS)
    return _safe_div(log_dd - log_dd.shift(5), log_dd.shift(5).abs())


def dd_drv2_021_vol_weighted_dd_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of volume-weighted 252-day drawdown."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    v_norm = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    vw_dd = _rolling_mean(dd * v_norm, _TD_YEAR)
    return vw_dd.diff(5)


def dd_drv2_022_dd_convexity_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of drawdown convexity (avg-dd / max-dd ratio evolution)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    avg_dd = _rolling_mean(dd, _TD_YEAR)
    max_dd = _rolling_min(dd, _TD_YEAR)
    convex = _safe_div(avg_dd, max_dd)
    return convex.diff(5)


def dd_drv2_023_dd_entropy_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day dd entropy (volatility-of-dd-changes)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    entropy = _rolling_std(dd.diff(1), _TD_YEAR)
    return entropy.diff(5)


def dd_drv2_024_dd_intensity_ath_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ATH drawdown intensity (current/max ATH dd ratio)."""
    dd = _safe_div(close - close.expanding(min_periods=1).max(), close.expanding(min_periods=1).max())
    mdd = dd.expanding(min_periods=1).min()
    intensity = _safe_div(dd, mdd)
    return intensity.diff(5)


def dd_drv2_025_composite_dd_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite weighted drawdown (50% 21d + 30% 63d + 20% 252d)."""
    dd21 = _safe_div(close - _rolling_max(close, _TD_MON), _rolling_max(close, _TD_MON))
    dd63 = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    dd252 = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    composite = 0.5 * dd21 + 0.3 * dd63 + 0.2 * dd252
    return composite.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DEPTH_REGISTRY_2ND_DERIVATIVES = {
    "dd_drv2_001_dd_252d_5d_diff": {"inputs": ["close"], "func": dd_drv2_001_dd_252d_5d_diff},
    "dd_drv2_002_dd_ath_5d_diff": {"inputs": ["close"], "func": dd_drv2_002_dd_ath_5d_diff},
    "dd_drv2_003_dd_63d_5d_diff": {"inputs": ["close"], "func": dd_drv2_003_dd_63d_5d_diff},
    "dd_drv2_004_log_dd_252d_5d_diff": {"inputs": ["close"], "func": dd_drv2_004_log_dd_252d_5d_diff},
    "dd_drv2_005_log_dd_ath_21d_diff": {"inputs": ["close"], "func": dd_drv2_005_log_dd_ath_21d_diff},
    "dd_drv2_006_dd_vol_adj_252d_5d_diff": {"inputs": ["close"], "func": dd_drv2_006_dd_vol_adj_252d_5d_diff},
    "dd_drv2_007_underwater_frac_252d_5d_diff": {"inputs": ["close"], "func": dd_drv2_007_underwater_frac_252d_5d_diff},
    "dd_drv2_008_avg_dd_252d_5d_diff": {"inputs": ["close"], "func": dd_drv2_008_avg_dd_252d_5d_diff},
    "dd_drv2_009_dd_area_63d_5d_diff": {"inputs": ["close"], "func": dd_drv2_009_dd_area_63d_5d_diff},
    "dd_drv2_010_sma_cascade_5d_diff": {"inputs": ["close"], "func": dd_drv2_010_sma_cascade_5d_diff},
    "dd_drv2_011_dd_zscore_252d_5d_diff": {"inputs": ["close"], "func": dd_drv2_011_dd_zscore_252d_5d_diff},
    "dd_drv2_012_dd_pct_rank_252d_5d_diff": {"inputs": ["close"], "func": dd_drv2_012_dd_pct_rank_252d_5d_diff},
    "dd_drv2_013_close_vs_sma200_5d_diff": {"inputs": ["close"], "func": dd_drv2_013_close_vs_sma200_5d_diff},
    "dd_drv2_014_ema_cascade_5d_diff": {"inputs": ["close"], "func": dd_drv2_014_ema_cascade_5d_diff},
    "dd_drv2_015_atr_norm_dd_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": dd_drv2_015_atr_norm_dd_252d_5d_diff},
    "dd_drv2_016_pct_b_21d_5d_diff": {"inputs": ["close"], "func": dd_drv2_016_pct_b_21d_5d_diff},
    "dd_drv2_017_rsi_14d_5d_diff": {"inputs": ["close"], "func": dd_drv2_017_rsi_14d_5d_diff},
    "dd_drv2_018_dd_252d_21d_slope": {"inputs": ["close"], "func": dd_drv2_018_dd_252d_21d_slope},
    "dd_drv2_019_dd_ath_63d_slope": {"inputs": ["close"], "func": dd_drv2_019_dd_ath_63d_slope},
    "dd_drv2_020_log_dd_ath_5d_pct_change": {"inputs": ["close"], "func": dd_drv2_020_log_dd_ath_5d_pct_change},
    "dd_drv2_021_vol_weighted_dd_252d_5d_diff": {"inputs": ["close", "volume"], "func": dd_drv2_021_vol_weighted_dd_252d_5d_diff},
    "dd_drv2_022_dd_convexity_252d_5d_diff": {"inputs": ["close"], "func": dd_drv2_022_dd_convexity_252d_5d_diff},
    "dd_drv2_023_dd_entropy_252d_5d_diff": {"inputs": ["close"], "func": dd_drv2_023_dd_entropy_252d_5d_diff},
    "dd_drv2_024_dd_intensity_ath_5d_diff": {"inputs": ["close"], "func": dd_drv2_024_dd_intensity_ath_5d_diff},
    "dd_drv2_025_composite_dd_5d_diff": {"inputs": ["close"], "func": dd_drv2_025_composite_dd_5d_diff},
}
