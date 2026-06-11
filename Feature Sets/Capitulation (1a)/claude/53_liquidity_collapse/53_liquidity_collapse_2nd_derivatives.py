"""
53_liquidity_collapse — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base illiquidity concepts — velocity/acceleration
  of Amihud ratio, bid-ask spread estimators, and illiquidity streaks
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — illiquidity worsening rapidly
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
    """Rolling OLS slope over w periods (rate of change via regression)."""
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


# ── 2nd-derivative feature functions drv2_001-025 ────────────────────────────

# --- Group A (drv2_001-008): Rate of change of Amihud rolling means ---

def lqc_drv2_001_amihud_5d_mean_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day Amihud mean (velocity of short-run illiquidity level)."""
    return _rolling_mean(_amihud(close, volume), _TD_WEEK).diff(_TD_WEEK)


def lqc_drv2_002_amihud_21d_mean_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day Amihud mean (velocity of monthly illiquidity trend)."""
    return _rolling_mean(_amihud(close, volume), _TD_MON).diff(_TD_WEEK)


def lqc_drv2_003_amihud_21d_mean_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day Amihud mean (month-over-month illiquidity change)."""
    return _rolling_mean(_amihud(close, volume), _TD_MON).diff(_TD_MON)


def lqc_drv2_004_amihud_63d_mean_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day Amihud mean (acceleration of quarterly trend)."""
    return _rolling_mean(_amihud(close, volume), _TD_QTR).diff(_TD_MON)


def lqc_drv2_005_amihud_21d_mean_ols_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day Amihud mean over trailing 21-day window."""
    return _linslope(_rolling_mean(_amihud(close, volume), _TD_MON), _TD_MON)


def lqc_drv2_006_amihud_21d_mean_ols_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day Amihud mean over trailing 63-day window."""
    return _linslope(_rolling_mean(_amihud(close, volume), _TD_MON), _TD_QTR)


def lqc_drv2_007_amihud_zscore_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of Amihud 63d z-score (velocity of z-score level)."""
    return _zscore(_amihud(close, volume), _TD_QTR).diff(_TD_WEEK)


def lqc_drv2_008_amihud_zscore_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of Amihud 63d z-score (monthly velocity of illiq z-score)."""
    return _zscore(_amihud(close, volume), _TD_QTR).diff(_TD_MON)


# --- Group B (drv2_009-016): Rate of change of Corwin-Schultz spread ---

def lqc_drv2_009_cs_spread_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Corwin-Schultz spread (velocity of bid-ask widening)."""
    return _cs_spread(high, low, close).diff(_TD_WEEK)


def lqc_drv2_010_cs_spread_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of Corwin-Schultz spread (monthly bid-ask spread change)."""
    return _cs_spread(high, low, close).diff(_TD_MON)


def lqc_drv2_011_cs_spread_mean21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day C-S spread mean (velocity of smoothed bid-ask)."""
    return _rolling_mean(_cs_spread(high, low, close), _TD_MON).diff(_TD_WEEK)


def lqc_drv2_012_cs_spread_mean21_ols_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 21-day C-S spread mean over trailing 21 days."""
    return _linslope(_rolling_mean(_cs_spread(high, low, close), _TD_MON), _TD_MON)


def lqc_drv2_013_cs_spread_zscore_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63d z-score of C-S spread (velocity of bid-ask z-score)."""
    return _zscore(_cs_spread(high, low, close), _TD_QTR).diff(_TD_WEEK)


def lqc_drv2_014_cs_spread_zscore_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63d z-score of C-S spread (monthly acceleration)."""
    return _zscore(_cs_spread(high, low, close), _TD_QTR).diff(_TD_MON)


def lqc_drv2_015_cs_spread_ols_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of daily C-S spread over trailing 63 days."""
    return _linslope(_cs_spread(high, low, close), _TD_QTR)


def lqc_drv2_016_cs_spread_max_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling max C-S spread (spike-maximum velocity)."""
    return _rolling_max(_cs_spread(high, low, close), _TD_MON).diff(_TD_WEEK)


# --- Group C (drv2_017-021): Rate of change of Roll spread ---

def lqc_drv2_017_roll_spread_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Roll spread estimate (velocity of effective-spread widening)."""
    return _roll_spread(close).diff(_TD_WEEK)


def lqc_drv2_018_roll_spread_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of Roll spread estimate (monthly effective-spread velocity)."""
    return _roll_spread(close).diff(_TD_MON)


def lqc_drv2_019_roll_spread_ols_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of Roll spread over trailing 21 days."""
    return _linslope(_roll_spread(close), _TD_MON)


def lqc_drv2_020_roll_spread_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d z-score of Roll spread (velocity of z-score)."""
    return _zscore(_roll_spread(close), _TD_QTR).diff(_TD_WEEK)


def lqc_drv2_021_roll_spread_ols_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of Roll spread over trailing 63 days (quarterly velocity)."""
    return _linslope(_roll_spread(close), _TD_QTR)


# --- Group D (drv2_022-025): Rate of change of composite and streak signals ---

def lqc_drv2_022_composite_zscore_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of composite illiq z-score (Amihud+C-S+Roll, 63d window)."""
    az   = _zscore(_amihud(close, volume), _TD_QTR)
    cz   = _zscore(_cs_spread(high, low, close), _TD_QTR)
    rz   = _zscore(_roll_spread(close), _TD_QTR)
    comp = (az + cz + rz) / 3.0
    return comp.diff(_TD_WEEK)


def lqc_drv2_023_composite_zscore_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of composite illiq z-score (monthly velocity)."""
    az   = _zscore(_amihud(close, volume), _TD_QTR)
    cz   = _zscore(_cs_spread(high, low, close), _TD_QTR)
    rz   = _zscore(_roll_spread(close), _TD_QTR)
    comp = (az + cz + rz) / 3.0
    return comp.diff(_TD_MON)


def lqc_drv2_024_amihud_spike_ratio_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of Amihud/21d-mean spike ratio (velocity of spike intensity)."""
    ami   = _amihud(close, volume)
    ratio = _safe_div(ami, _rolling_mean(ami, _TD_MON))
    return ratio.diff(_TD_WEEK)


def lqc_drv2_025_amihud_above_mean_streak_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of above-21d-mean Amihud streak length (streak velocity)."""
    ami    = _amihud(close, volume)
    mu     = _rolling_mean(ami, _TD_MON)
    cond   = ami > mu
    c      = cond.astype(int)
    group  = (~cond).cumsum()
    streak = c.groupby(group).cumsum().astype(float)
    return streak.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

LIQUIDITY_COLLAPSE_REGISTRY_2ND_DERIVATIVES = {
    "lqc_drv2_001_amihud_5d_mean_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv2_001_amihud_5d_mean_5d_diff},
    "lqc_drv2_002_amihud_21d_mean_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv2_002_amihud_21d_mean_5d_diff},
    "lqc_drv2_003_amihud_21d_mean_21d_diff": {"inputs": ["close", "volume"], "func": lqc_drv2_003_amihud_21d_mean_21d_diff},
    "lqc_drv2_004_amihud_63d_mean_21d_diff": {"inputs": ["close", "volume"], "func": lqc_drv2_004_amihud_63d_mean_21d_diff},
    "lqc_drv2_005_amihud_21d_mean_ols_slope_21d": {"inputs": ["close", "volume"], "func": lqc_drv2_005_amihud_21d_mean_ols_slope_21d},
    "lqc_drv2_006_amihud_21d_mean_ols_slope_63d": {"inputs": ["close", "volume"], "func": lqc_drv2_006_amihud_21d_mean_ols_slope_63d},
    "lqc_drv2_007_amihud_zscore_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv2_007_amihud_zscore_5d_diff},
    "lqc_drv2_008_amihud_zscore_21d_diff": {"inputs": ["close", "volume"], "func": lqc_drv2_008_amihud_zscore_21d_diff},
    "lqc_drv2_009_cs_spread_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv2_009_cs_spread_5d_diff},
    "lqc_drv2_010_cs_spread_21d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv2_010_cs_spread_21d_diff},
    "lqc_drv2_011_cs_spread_mean21_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv2_011_cs_spread_mean21_5d_diff},
    "lqc_drv2_012_cs_spread_mean21_ols_slope_21d": {"inputs": ["close", "high", "low"], "func": lqc_drv2_012_cs_spread_mean21_ols_slope_21d},
    "lqc_drv2_013_cs_spread_zscore_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv2_013_cs_spread_zscore_5d_diff},
    "lqc_drv2_014_cs_spread_zscore_21d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv2_014_cs_spread_zscore_21d_diff},
    "lqc_drv2_015_cs_spread_ols_slope_63d": {"inputs": ["close", "high", "low"], "func": lqc_drv2_015_cs_spread_ols_slope_63d},
    "lqc_drv2_016_cs_spread_max_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": lqc_drv2_016_cs_spread_max_21d_5d_diff},
    "lqc_drv2_017_roll_spread_5d_diff": {"inputs": ["close"], "func": lqc_drv2_017_roll_spread_5d_diff},
    "lqc_drv2_018_roll_spread_21d_diff": {"inputs": ["close"], "func": lqc_drv2_018_roll_spread_21d_diff},
    "lqc_drv2_019_roll_spread_ols_slope_21d": {"inputs": ["close"], "func": lqc_drv2_019_roll_spread_ols_slope_21d},
    "lqc_drv2_020_roll_spread_zscore_5d_diff": {"inputs": ["close"], "func": lqc_drv2_020_roll_spread_zscore_5d_diff},
    "lqc_drv2_021_roll_spread_ols_slope_63d": {"inputs": ["close"], "func": lqc_drv2_021_roll_spread_ols_slope_63d},
    "lqc_drv2_022_composite_zscore_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": lqc_drv2_022_composite_zscore_5d_diff},
    "lqc_drv2_023_composite_zscore_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": lqc_drv2_023_composite_zscore_21d_diff},
    "lqc_drv2_024_amihud_spike_ratio_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv2_024_amihud_spike_ratio_5d_diff},
    "lqc_drv2_025_amihud_above_mean_streak_5d_diff": {"inputs": ["close", "volume"], "func": lqc_drv2_025_amihud_above_mean_streak_5d_diff},
}
