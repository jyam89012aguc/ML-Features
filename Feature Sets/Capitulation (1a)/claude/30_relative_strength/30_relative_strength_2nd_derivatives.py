"""
30_relative_strength — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change / velocity of base relative-strength concepts —
        Mansfield RS velocity, DEMA/TEMA distance velocity, Hull MA slope
        changes, MA ribbon dynamics, SMA/EMA distance diffs and slopes.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _sma(close: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(close, w)


def _ema(close: pd.Series, span: int) -> pd.Series:
    return _ewm_mean(close, span)


def _dema(close: pd.Series, span: int) -> pd.Series:
    e1 = _ema(close, span)
    e2 = _ema(e1, span)
    return 2.0 * e1 - e2


def _tema(close: pd.Series, span: int) -> pd.Series:
    e1 = _ema(close, span)
    e2 = _ema(e1, span)
    e3 = _ema(e2, span)
    return 3.0 * e1 - 3.0 * e2 + e3


def _wma(close: pd.Series, w: int) -> pd.Series:
    mp = max(1, w // 2)
    def _wma_window(x):
        n = len(x)
        if n < mp:
            return np.nan
        wt = np.arange(1, n + 1, dtype=float)
        return float(np.dot(x, wt) / wt.sum())
    return close.rolling(w, min_periods=mp).apply(_wma_window, raw=True)


def _hma(close: pd.Series, n: int) -> pd.Series:
    half   = max(2, n // 2)
    sqrtn  = max(2, int(np.floor(np.sqrt(n))))
    raw    = 2.0 * _wma(close, half) - _wma(close, n)
    return _wma(raw, sqrtn)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (raw=False to work with NaN)."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


_RIBBON_PERIODS = [5, 10, 20, 30, 40, 50, 100, 200]


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

# --- Mansfield RS velocity ---

def rst_drv2_001_mansfield_raw_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Mansfield RS (126d base) — velocity of short RS."""
    raw = _safe_div(close - _sma(close, _TD_HALF), _sma(close, _TD_HALF))
    return raw.diff(_TD_WEEK)


def rst_drv2_002_mansfield_raw_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Mansfield RS (252d base) — velocity of long RS."""
    raw = _safe_div(close - _sma(close, _TD_YEAR), _sma(close, _TD_YEAR))
    return raw.diff(_TD_WEEK)


def rst_drv2_003_mansfield_raw_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of Mansfield RS (252d base) — monthly velocity."""
    raw = _safe_div(close - _sma(close, _TD_YEAR), _sma(close, _TD_YEAR))
    return raw.diff(_TD_MON)


def rst_drv2_004_mansfield_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of z-scored Mansfield RS (252d base)."""
    raw = _safe_div(close - _sma(close, _TD_YEAR), _sma(close, _TD_YEAR))
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    z = _safe_div(raw - m, s)
    return z.diff(_TD_WEEK)


def rst_drv2_005_mansfield_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of Mansfield RS (252d base) over trailing 21 days."""
    raw = _safe_div(close - _sma(close, _TD_YEAR), _sma(close, _TD_YEAR))
    return _linslope(raw, _TD_MON)


# --- DEMA / TEMA velocity ---

def rst_drv2_006_pct_dist_dema21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-DEMA21 pct-distance."""
    d = _safe_div(close - _dema(close, _TD_MON), _dema(close, _TD_MON))
    return d.diff(_TD_WEEK)


def rst_drv2_007_pct_dist_dema200_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-DEMA200 pct-distance."""
    d = _safe_div(close - _dema(close, 200), _dema(close, 200))
    return d.diff(_TD_WEEK)


def rst_drv2_008_pct_dist_tema50_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-TEMA50 pct-distance."""
    d = _safe_div(close - _tema(close, 50), _tema(close, 50))
    return d.diff(_TD_WEEK)


def rst_drv2_009_pct_dist_tema200_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of close-to-TEMA200 pct-distance."""
    d = _safe_div(close - _tema(close, 200), _tema(close, 200))
    return d.diff(_TD_MON)


def rst_drv2_010_dema_vs_ema200_spread_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of DEMA200-EMA200 spread as pct of close."""
    sp = _safe_div(_dema(close, 200) - _ema(close, 200), close)
    return sp.diff(_TD_WEEK)


# --- Hull MA velocity ---

def rst_drv2_011_pct_dist_hma16_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-HMA16 pct-distance."""
    d = _safe_div(close - _hma(close, 16), _hma(close, 16))
    return d.diff(_TD_WEEK)


def rst_drv2_012_pct_dist_hma49_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-HMA49 pct-distance."""
    d = _safe_div(close - _hma(close, 49), _hma(close, 49))
    return d.diff(_TD_WEEK)


def rst_drv2_013_hma16_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of HMA16 slope (acceleration of HMA momentum)."""
    slope = _hma(close, 16).diff(_TD_WEEK)
    return slope.diff(_TD_WEEK)


def rst_drv2_014_hma49_slope_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of HMA49 slope."""
    slope = _hma(close, 49).diff(_TD_WEEK)
    return slope.diff(_TD_MON)


def rst_drv2_015_pct_dist_hma49_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of close-to-HMA49 pct-distance over trailing 21 days."""
    d = _safe_div(close - _hma(close, 49), _hma(close, 49))
    return _linslope(d, _TD_MON)


# --- MA ribbon velocity ---

def rst_drv2_016_ribbon_frac_below_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ribbon fraction-below (8-SMA ribbon)."""
    mas   = [_sma(close, p) for p in _RIBBON_PERIODS]
    frac  = sum((close < m).astype(float) for m in mas) / float(len(_RIBBON_PERIODS))
    return frac.diff(_TD_WEEK)


def rst_drv2_017_ribbon_frac_below_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of ribbon fraction-below."""
    mas  = [_sma(close, p) for p in _RIBBON_PERIODS]
    frac = sum((close < m).astype(float) for m in mas) / float(len(_RIBBON_PERIODS))
    return frac.diff(_TD_MON)


def rst_drv2_018_ribbon_spread_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ribbon spread (SMA200-SMA5)/SMA5."""
    sp = _safe_div(_sma(close, 200) - _sma(close, 5), _sma(close, 5))
    return sp.diff(_TD_WEEK)


def rst_drv2_019_ribbon_count_declining_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of count of ribbon SMAs with negative 21-day slope."""
    cnt = sum((m.diff(_TD_MON) < 0).astype(float) for m in [_sma(close, p) for p in _RIBBON_PERIODS])
    return cnt.diff(_TD_WEEK)


def rst_drv2_020_ribbon_ordered_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ribbon bearish-ordering score."""
    mas = [_sma(close, p) for p in _RIBBON_PERIODS]
    score = sum((mas[i] < mas[i + 1]).astype(float) for i in range(len(mas) - 1))
    return score.diff(_TD_WEEK)


# --- SMA/EMA distance velocity (retained core) ---

def rst_drv2_021_pct_dist_sma21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-SMA21 pct-distance (velocity of short-MA gap)."""
    d = _safe_div(close - _sma(close, _TD_MON), _sma(close, _TD_MON))
    return d.diff(_TD_WEEK)


def rst_drv2_022_pct_dist_sma200_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-SMA200 pct-distance (velocity of long-MA gap)."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    return d.diff(_TD_WEEK)


def rst_drv2_023_pct_dist_sma200_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of close-to-SMA200 pct-distance (monthly velocity)."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    return d.diff(_TD_MON)


def rst_drv2_024_pct_dist_sma200_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of close-to-SMA200 pct-distance over trailing 21 days."""
    d = _safe_div(close - _sma(close, 200), _sma(close, 200))
    return _linslope(d, _TD_MON)


def rst_drv2_025_sum_depth_12mas_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of sum-of-depth-below-12-MAs composite."""
    spans = [10, _TD_MON, 50, _TD_QTR, 100, 200]
    sma_d = [_safe_div(close - _sma(close, w), _sma(close, w)).clip(upper=0.0) for w in spans]
    ema_d = [_safe_div(close - _ema(close, w), _ema(close, w)).clip(upper=0.0) for w in spans]
    depth = sum(sma_d) + sum(ema_d)
    return depth.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_STRENGTH_REGISTRY_2ND_DERIVATIVES = {
    "rst_drv2_001_mansfield_raw_126d_5d_diff": {"inputs": ["close"], "func": rst_drv2_001_mansfield_raw_126d_5d_diff},
    "rst_drv2_002_mansfield_raw_252d_5d_diff": {"inputs": ["close"], "func": rst_drv2_002_mansfield_raw_252d_5d_diff},
    "rst_drv2_003_mansfield_raw_252d_21d_diff": {"inputs": ["close"], "func": rst_drv2_003_mansfield_raw_252d_21d_diff},
    "rst_drv2_004_mansfield_zscore_252d_5d_diff": {"inputs": ["close"], "func": rst_drv2_004_mansfield_zscore_252d_5d_diff},
    "rst_drv2_005_mansfield_slope_21d": {"inputs": ["close"], "func": rst_drv2_005_mansfield_slope_21d},
    "rst_drv2_006_pct_dist_dema21_5d_diff": {"inputs": ["close"], "func": rst_drv2_006_pct_dist_dema21_5d_diff},
    "rst_drv2_007_pct_dist_dema200_5d_diff": {"inputs": ["close"], "func": rst_drv2_007_pct_dist_dema200_5d_diff},
    "rst_drv2_008_pct_dist_tema50_5d_diff": {"inputs": ["close"], "func": rst_drv2_008_pct_dist_tema50_5d_diff},
    "rst_drv2_009_pct_dist_tema200_21d_diff": {"inputs": ["close"], "func": rst_drv2_009_pct_dist_tema200_21d_diff},
    "rst_drv2_010_dema_vs_ema200_spread_5d_diff": {"inputs": ["close"], "func": rst_drv2_010_dema_vs_ema200_spread_5d_diff},
    "rst_drv2_011_pct_dist_hma16_5d_diff": {"inputs": ["close"], "func": rst_drv2_011_pct_dist_hma16_5d_diff},
    "rst_drv2_012_pct_dist_hma49_5d_diff": {"inputs": ["close"], "func": rst_drv2_012_pct_dist_hma49_5d_diff},
    "rst_drv2_013_hma16_slope_5d_diff": {"inputs": ["close"], "func": rst_drv2_013_hma16_slope_5d_diff},
    "rst_drv2_014_hma49_slope_21d_diff": {"inputs": ["close"], "func": rst_drv2_014_hma49_slope_21d_diff},
    "rst_drv2_015_pct_dist_hma49_slope_21d": {"inputs": ["close"], "func": rst_drv2_015_pct_dist_hma49_slope_21d},
    "rst_drv2_016_ribbon_frac_below_5d_diff": {"inputs": ["close"], "func": rst_drv2_016_ribbon_frac_below_5d_diff},
    "rst_drv2_017_ribbon_frac_below_21d_diff": {"inputs": ["close"], "func": rst_drv2_017_ribbon_frac_below_21d_diff},
    "rst_drv2_018_ribbon_spread_5d_diff": {"inputs": ["close"], "func": rst_drv2_018_ribbon_spread_5d_diff},
    "rst_drv2_019_ribbon_count_declining_5d_diff": {"inputs": ["close"], "func": rst_drv2_019_ribbon_count_declining_5d_diff},
    "rst_drv2_020_ribbon_ordered_score_5d_diff": {"inputs": ["close"], "func": rst_drv2_020_ribbon_ordered_score_5d_diff},
    "rst_drv2_021_pct_dist_sma21_5d_diff": {"inputs": ["close"], "func": rst_drv2_021_pct_dist_sma21_5d_diff},
    "rst_drv2_022_pct_dist_sma200_5d_diff": {"inputs": ["close"], "func": rst_drv2_022_pct_dist_sma200_5d_diff},
    "rst_drv2_023_pct_dist_sma200_21d_diff": {"inputs": ["close"], "func": rst_drv2_023_pct_dist_sma200_21d_diff},
    "rst_drv2_024_pct_dist_sma200_slope_21d": {"inputs": ["close"], "func": rst_drv2_024_pct_dist_sma200_slope_21d},
    "rst_drv2_025_sum_depth_12mas_5d_diff": {"inputs": ["close"], "func": rst_drv2_025_sum_depth_12mas_5d_diff},
}
