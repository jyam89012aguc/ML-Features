"""
53_liquidity_collapse — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative illiquidity signals — acceleration of
  velocity of Amihud ratio, bid-ask spread estimators, and composite measures
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — illiquidity acceleration / convexity of distress
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
    """Element-wise division; zero denominator becomes NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _zscore(s: pd.Series, w: int) -> pd.Series:
    mu  = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


def _amihud(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud illiquidity: |ret| / dollar_volume."""
    ret    = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(ret, dolvol)


def _roll_spread(close: pd.Series) -> pd.Series:
    """Roll (1984) effective spread proxy."""
    dp  = close.diff(1)
    cov = dp.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).cov(dp.shift(1))
    return 2.0 * np.sqrt((-cov).clip(lower=0.0))


def _cs_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corwin-Schultz (2012) bid-ask spread estimator."""
    ln_hl  = _log_safe(high) - _log_safe(low)
    beta   = ln_hl ** 2 + (ln_hl.shift(1)) ** 2
    h2     = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2     = pd.concat([low,  low.shift(1)],  axis=1).min(axis=1)
    gamma  = (_log_safe(h2) - _log_safe(l2)) ** 2
    k      = 3.0 - 2.0 * np.sqrt(2.0)
    alpha  = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k - np.sqrt(gamma / k)
    spread = (2.0 * (np.exp(alpha) - 1.0)) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0.0)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi = np.arange(n, dtype=float)
        xm = xi.mean()
        ym = x.mean()
        num = ((xi - xm) * (x - ym)).sum()
        den = ((xi - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=True)


# ── 3rd-derivative feature functions drv3_001-025 ────────────────────────────

# --- Group A (drv3_001-008): Acceleration of Amihud velocity ---

def lqc_drv3_001_amihud_5d_mean_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 5d Amihud mean) — acceleration of short illiq."""
    v = _rolling_mean(_amihud(close, volume), _TD_WEEK).diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


def lqc_drv3_002_amihud_21d_mean_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21d Amihud mean) — acceleration of monthly mean."""
    v = _rolling_mean(_amihud(close, volume), _TD_MON).diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


def lqc_drv3_003_amihud_21d_mean_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 21d Amihud mean) — short acceleration of monthly velocity."""
    v = _rolling_mean(_amihud(close, volume), _TD_MON).diff(_TD_MON)
    return v.diff(_TD_WEEK)


def lqc_drv3_004_amihud_21d_mean_ols_slope_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d Amihud mean over 21d (acceleration of slope)."""
    slope = _linslope(_rolling_mean(_amihud(close, volume), _TD_MON), _TD_MON)
    return slope.diff(_TD_WEEK)


def lqc_drv3_005_amihud_21d_mean_ols_slope_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 21d Amihud mean over 21d (monthly slope change)."""
    slope = _linslope(_rolling_mean(_amihud(close, volume), _TD_MON), _TD_MON)
    return slope.diff(_TD_MON)


def lqc_drv3_006_amihud_zscore_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of Amihud 63d z-score) — z-score acceleration."""
    v = _zscore(_amihud(close, volume), _TD_QTR).diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


def lqc_drv3_007_amihud_zscore_ols_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of Amihud 63d z-score over trailing 21 days (linear rate of z change)."""
    return _linslope(_zscore(_amihud(close, volume), _TD_QTR), _TD_MON)


def lqc_drv3_008_amihud_spike_ratio_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of Amihud spike ratio) — spike acceleration."""
    ami   = _amihud(close, volume)
    ratio = _safe_div(ami, _rolling_mean(ami, _TD_MON))
    v     = ratio.diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


# --- Group B (drv3_009-016): Acceleration of Corwin-Schultz velocity ---

def lqc_drv3_009_cs_spread_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of C-S spread) — bid-ask spread acceleration."""
    v = _cs_spread(high, low, close).diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


def lqc_drv3_010_cs_spread_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of C-S spread) — short acceleration of monthly velocity."""
    v = _cs_spread(high, low, close).diff(_TD_MON)
    return v.diff(_TD_WEEK)


def lqc_drv3_011_cs_spread_mean21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21d C-S mean) — smoothed spread acceleration."""
    v = _rolling_mean(_cs_spread(high, low, close), _TD_MON).diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


def lqc_drv3_012_cs_spread_ols_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d OLS slope of C-S spread (slope acceleration)."""
    slope = _linslope(_cs_spread(high, low, close), _TD_MON)
    return slope.diff(_TD_WEEK)


def lqc_drv3_013_cs_spread_ols_slope_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21d OLS slope of C-S spread (monthly slope acceleration)."""
    slope = _linslope(_cs_spread(high, low, close), _TD_MON)
    return slope.diff(_TD_MON)


def lqc_drv3_014_cs_spread_zscore_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63d C-S z-score) — z-score acceleration."""
    v = _zscore(_cs_spread(high, low, close), _TD_QTR).diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


def lqc_drv3_015_cs_spread_max_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21d max C-S spread) — peak spread acceleration."""
    v = _rolling_max(_cs_spread(high, low, close), _TD_MON).diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


def lqc_drv3_016_cs_spread_ols_slope_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63d OLS slope of C-S spread (acceleration of long-run slope)."""
    slope = _linslope(_cs_spread(high, low, close), _TD_QTR)
    return slope.diff(_TD_WEEK)


# --- Group C (drv3_017-021): Acceleration of Roll spread velocity ---

def lqc_drv3_017_roll_spread_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of Roll spread) — Roll spread acceleration."""
    v = _roll_spread(close).diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


def lqc_drv3_018_roll_spread_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of Roll spread) — short acceleration of monthly velocity."""
    v = _roll_spread(close).diff(_TD_MON)
    return v.diff(_TD_WEEK)


def lqc_drv3_019_roll_spread_ols_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d OLS slope of Roll spread (slope acceleration)."""
    slope = _linslope(_roll_spread(close), _TD_MON)
    return slope.diff(_TD_WEEK)


def lqc_drv3_020_roll_spread_ols_slope_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21d OLS slope of Roll spread (monthly slope change)."""
    slope = _linslope(_roll_spread(close), _TD_MON)
    return slope.diff(_TD_MON)


def lqc_drv3_021_roll_spread_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of Roll 63d z-score) — z-score acceleration."""
    v = _zscore(_roll_spread(close), _TD_QTR).diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


# --- Group D (drv3_022-025): Acceleration of composite and mixed signals ---

def lqc_drv3_022_composite_zscore_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of composite illiq z-score) — composite acceleration."""
    az   = _zscore(_amihud(close, volume), _TD_QTR)
    cz   = _zscore(_cs_spread(high, low, close), _TD_QTR)
    rz   = _zscore(_roll_spread(close), _TD_QTR)
    comp = (az + cz + rz) / 3.0
    v    = comp.diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


def lqc_drv3_023_composite_zscore_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of composite illiq z-score) — acceleration of monthly vel."""
    az   = _zscore(_amihud(close, volume), _TD_QTR)
    cz   = _zscore(_cs_spread(high, low, close), _TD_QTR)
    rz   = _zscore(_roll_spread(close), _TD_QTR)
    comp = (az + cz + rz) / 3.0
    v    = comp.diff(_TD_MON)
    return v.diff(_TD_WEEK)


def lqc_drv3_024_composite_ols_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21d OLS slope of composite z-score (slope acceleration)."""
    az    = _zscore(_amihud(close, volume), _TD_QTR)
    cz    = _zscore(_cs_spread(high, low, close), _TD_QTR)
    rz    = _zscore(_roll_spread(close), _TD_QTR)
    comp  = (az + cz + rz) / 3.0
    slope = _linslope(comp, _TD_MON)
    return slope.diff(_TD_WEEK)


def lqc_drv3_025_amihud_cs_joint_spike_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of joint Amihud+C-S z-score sum) — joint spike acceleration."""
    az = _zscore(_amihud(close, volume), _TD_QTR)
    cz = _zscore(_cs_spread(high, low, close), _TD_QTR)
    s  = az + cz
    v  = s.diff(_TD_WEEK)
    return v.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

LIQUIDITY_COLLAPSE_REGISTRY_3RD_DERIVATIVES = {
    "lqc_drv3_001_amihud_5d_mean_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv3_001_amihud_5d_mean_5d_diff_5d_diff},
    "lqc_drv3_002_amihud_21d_mean_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv3_002_amihud_21d_mean_5d_diff_5d_diff},
    "lqc_drv3_003_amihud_21d_mean_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv3_003_amihud_21d_mean_21d_diff_5d_diff},
    "lqc_drv3_004_amihud_21d_mean_ols_slope_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv3_004_amihud_21d_mean_ols_slope_5d_diff},
    "lqc_drv3_005_amihud_21d_mean_ols_slope_21d_diff": {"inputs": ["close", "volume"], "func": lqc_drv3_005_amihud_21d_mean_ols_slope_21d_diff},
    "lqc_drv3_006_amihud_zscore_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv3_006_amihud_zscore_5d_diff_5d_diff},
    "lqc_drv3_007_amihud_zscore_ols_slope_21d": {"inputs": ["close", "volume"], "func": lqc_drv3_007_amihud_zscore_ols_slope_21d},
    "lqc_drv3_008_amihud_spike_ratio_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv3_008_amihud_spike_ratio_5d_diff_5d_diff},
    "lqc_drv3_009_cs_spread_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv3_009_cs_spread_5d_diff_5d_diff},
    "lqc_drv3_010_cs_spread_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv3_010_cs_spread_21d_diff_5d_diff},
    "lqc_drv3_011_cs_spread_mean21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv3_011_cs_spread_mean21_5d_diff_5d_diff},
    "lqc_drv3_012_cs_spread_ols_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv3_012_cs_spread_ols_slope_5d_diff},
    "lqc_drv3_013_cs_spread_ols_slope_21d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv3_013_cs_spread_ols_slope_21d_diff},
    "lqc_drv3_014_cs_spread_zscore_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv3_014_cs_spread_zscore_5d_diff_5d_diff},
    "lqc_drv3_015_cs_spread_max_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv3_015_cs_spread_max_21d_5d_diff_5d_diff},
    "lqc_drv3_016_cs_spread_ols_slope_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv3_016_cs_spread_ols_slope_63d_5d_diff},
    "lqc_drv3_017_roll_spread_5d_diff_5d_diff": {"inputs": ["close"], "func": lqc_drv3_017_roll_spread_5d_diff_5d_diff},
    "lqc_drv3_018_roll_spread_21d_diff_5d_diff": {"inputs": ["close"], "func": lqc_drv3_018_roll_spread_21d_diff_5d_diff},
    "lqc_drv3_019_roll_spread_ols_slope_5d_diff": {"inputs": ["close"], "func": lqc_drv3_019_roll_spread_ols_slope_5d_diff},
    "lqc_drv3_020_roll_spread_ols_slope_21d_diff": {"inputs": ["close"], "func": lqc_drv3_020_roll_spread_ols_slope_21d_diff},
    "lqc_drv3_021_roll_spread_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": lqc_drv3_021_roll_spread_zscore_5d_diff_5d_diff},
    "lqc_drv3_022_composite_zscore_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": lqc_drv3_022_composite_zscore_5d_diff_5d_diff},
    "lqc_drv3_023_composite_zscore_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": lqc_drv3_023_composite_zscore_21d_diff_5d_diff},
    "lqc_drv3_024_composite_ols_slope_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": lqc_drv3_024_composite_ols_slope_5d_diff},
    "lqc_drv3_025_amihud_cs_joint_spike_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": lqc_drv3_025_amihud_cs_joint_spike_5d_diff_5d_diff},
}
