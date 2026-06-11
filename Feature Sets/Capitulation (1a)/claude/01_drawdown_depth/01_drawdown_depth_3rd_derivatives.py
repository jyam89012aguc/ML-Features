"""
01_drawdown_depth — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative drawdown features
         captures exhaustion, inflection, and curvature of decline
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature takes a 2nd-derivative concept and computes its own .diff(n) or slope.
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
    """Rolling OLS slope over w periods."""
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


# ── 2nd-derivative helpers (inline) ──────────────────────────────────────────
# Each 3rd-derivative feature builds its own 2nd-derivative intermediate
# and then diffs/slopes it again — fully self-contained.

def _dd_252d_velocity(close: pd.Series, lag: int = 5) -> pd.Series:
    """2nd-deriv: lag-day diff of 252-day drawdown."""
    h = _rolling_max(close, _TD_YEAR)
    dd = _safe_div(close - h, h)
    return dd.diff(lag)


def _dd_ath_velocity(close: pd.Series, lag: int = 5) -> pd.Series:
    """2nd-deriv: lag-day diff of ATH drawdown."""
    h = close.expanding(min_periods=1).max()
    dd = _safe_div(close - h, h)
    return dd.diff(lag)


def _log_dd_ath_velocity(close: pd.Series, lag: int = 5) -> pd.Series:
    """2nd-deriv: lag-day diff of log ATH drawdown."""
    h = close.expanding(min_periods=1).max()
    log_dd = _log_safe(close) - _log_safe(h)
    return log_dd.diff(lag)


def _underwater_frac_velocity(close: pd.Series, lag: int = 5) -> pd.Series:
    """2nd-deriv: lag-day diff of underwater fraction."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    below = (dd < 0).astype(float)
    frac = _rolling_mean(below, _TD_YEAR)
    return frac.diff(lag)


def _avg_dd_velocity(close: pd.Series, lag: int = 5) -> pd.Series:
    """2nd-deriv: lag-day diff of rolling avg 252-day drawdown."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    avg = _rolling_mean(dd, _TD_YEAR)
    return avg.diff(lag)


def _sma_cascade_velocity(close: pd.Series, lag: int = 5) -> pd.Series:
    """2nd-deriv: lag-day diff of SMA cascade alignment score."""
    below = (
        (close < _rolling_mean(close, _TD_MON)).astype(float) +
        (close < _rolling_mean(close, _TD_QTR)).astype(float) +
        (close < _rolling_mean(close, _TD_HALF)).astype(float) +
        (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    ) / 4.0
    return below.diff(lag)


def _dd_zscore_velocity(close: pd.Series, lag: int = 5) -> pd.Series:
    """2nd-deriv: lag-day diff of 252-day drawdown z-score."""
    h = _rolling_max(close, _TD_YEAR)
    dd = _safe_div(close - h, h)
    z = _zscore_rolling(dd, _TD_YEAR)
    return z.diff(lag)


def _rsi_14d_velocity(close: pd.Series, lag: int = 5) -> pd.Series:
    """2nd-deriv: lag-day diff of RSI-14."""
    delta = close.diff(1)
    up = delta.clip(lower=0)
    down = (-delta).clip(lower=0)
    avg_up = up.ewm(alpha=1 / 14, min_periods=7).mean()
    avg_dn = down.ewm(alpha=1 / 14, min_periods=7).mean()
    rs = _safe_div(avg_up, avg_dn)
    rsi = 100.0 - _safe_div(100.0, 1.0 + rs)
    return rsi.diff(lag)


def _composite_dd_velocity(close: pd.Series, lag: int = 5) -> pd.Series:
    """2nd-deriv: lag-day diff of composite weighted drawdown."""
    dd21 = _safe_div(close - _rolling_max(close, _TD_MON), _rolling_max(close, _TD_MON))
    dd63 = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    dd252 = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    composite = 0.5 * dd21 + 0.3 * dd63 + 0.2 * dd252
    return composite.diff(lag)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def dd_drv3_001_dd_252d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of the 252d-drawdown velocity (acceleration of drawdown worsening)."""
    vel = _dd_252d_velocity(close, lag=5)
    return vel.diff(5)


def dd_drv3_002_dd_ath_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of ATH-drawdown velocity (acceleration of ATH distress)."""
    vel = _dd_ath_velocity(close, lag=5)
    return vel.diff(5)


def dd_drv3_003_log_dd_ath_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of log-ATH-drawdown velocity (log-space acceleration)."""
    vel = _log_dd_ath_velocity(close, lag=5)
    return vel.diff(5)


def dd_drv3_004_underwater_frac_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of underwater-fraction velocity (acceleration of distress-day increase)."""
    vel = _underwater_frac_velocity(close, lag=5)
    return vel.diff(5)


def dd_drv3_005_avg_dd_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of avg-drawdown velocity (acceleration of average deterioration)."""
    vel = _avg_dd_velocity(close, lag=5)
    return vel.diff(5)


def dd_drv3_006_sma_cascade_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of SMA cascade velocity (acceleration of trend-breakdown)."""
    vel = _sma_cascade_velocity(close, lag=5)
    return vel.diff(5)


def dd_drv3_007_dd_zscore_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of z-score velocity (acceleration of statistical extremity change)."""
    vel = _dd_zscore_velocity(close, lag=5)
    return vel.diff(5)


def dd_drv3_008_rsi_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of RSI velocity (RSI curvature — does the slide slow or speed up)."""
    vel = _rsi_14d_velocity(close, lag=5)
    return vel.diff(5)


def dd_drv3_009_composite_dd_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of composite drawdown velocity (multi-scale exhaustion signal)."""
    vel = _composite_dd_velocity(close, lag=5)
    return vel.diff(5)


def dd_drv3_010_dd_252d_accel_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 252d-drawdown velocity (monthly acceleration of decline)."""
    vel = _dd_252d_velocity(close, lag=5)
    return vel.diff(_TD_MON)


def dd_drv3_011_dd_ath_slope_of_velocity_21d(close: pd.Series) -> pd.Series:
    """OLS slope of ATH-drawdown velocity over 21 days (trend in the rate of worsening)."""
    vel = _dd_ath_velocity(close, lag=5)
    return _linslope(vel, _TD_MON)


def dd_drv3_012_log_dd_ath_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of log-ATH velocity over 63 days (sustained acceleration detection)."""
    vel = _log_dd_ath_velocity(close, lag=5)
    return _linslope(vel, _TD_QTR)


def dd_drv3_013_underwater_frac_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of underwater-fraction velocity over 21 days."""
    vel = _underwater_frac_velocity(close, lag=5)
    return _linslope(vel, _TD_MON)


def dd_drv3_014_sma_cascade_accel_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of SMA-cascade acceleration over 21 days."""
    vel = _sma_cascade_velocity(close, lag=5)
    accel = vel.diff(5)
    return _linslope(accel, _TD_MON)


def dd_drv3_015_dd_zscore_accel_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of z-score acceleration over 21 days (curvature of statistical distress)."""
    vel = _dd_zscore_velocity(close, lag=5)
    accel = vel.diff(5)
    return _linslope(accel, _TD_MON)


def dd_drv3_016_dd_252d_vel_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 252d drawdown velocity over trailing 63 days (how extreme is the pace)."""
    vel = _dd_252d_velocity(close, lag=5)
    return _zscore_rolling(vel, _TD_QTR)


def dd_drv3_017_dd_ath_vel_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of ATH drawdown velocity over trailing 252 days."""
    vel = _dd_ath_velocity(close, lag=5)
    return _zscore_rolling(vel, _TD_YEAR)


def dd_drv3_018_composite_vel_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of composite drawdown velocity over 63 days."""
    vel = _composite_dd_velocity(close, lag=5)
    return _zscore_rolling(vel, _TD_QTR)


def dd_drv3_019_rsi_vel_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of RSI velocity over trailing 63 days."""
    vel = _rsi_14d_velocity(close, lag=5)
    return _zscore_rolling(vel, _TD_QTR)


def dd_drv3_020_dd_252d_accel_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252-day drawdown acceleration within 63-day window."""
    vel = _dd_252d_velocity(close, lag=5)
    accel = vel.diff(5)
    return accel.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def dd_drv3_021_dd_ath_vel_sign_changes_21d(close: pd.Series) -> pd.Series:
    """Count of sign changes in ATH-drawdown velocity over 21 days (inflection counting)."""
    vel = _dd_ath_velocity(close, lag=5)
    signs = np.sign(vel)
    changes = (signs.diff(1) != 0).astype(float)
    return _rolling_sum(changes, _TD_MON)


def dd_drv3_022_composite_vel_sign_changes_21d(close: pd.Series) -> pd.Series:
    """Count of sign changes in composite dd velocity over 21 days."""
    vel = _composite_dd_velocity(close, lag=5)
    signs = np.sign(vel)
    changes = (signs.diff(1) != 0).astype(float)
    return _rolling_sum(changes, _TD_MON)


def dd_drv3_023_dd_252d_vel_ewm_vs_raw_21d(close: pd.Series) -> pd.Series:
    """21-day EMA of dd velocity minus raw dd velocity (smoothed vs noisy divergence)."""
    vel = _dd_252d_velocity(close, lag=5)
    smooth = _ewm_mean(vel, _TD_MON)
    return smooth - vel


def dd_drv3_024_log_dd_ath_accel_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of log-ATH drawdown acceleration (long-run extremity)."""
    vel = _log_dd_ath_velocity(close, lag=5)
    accel = vel.diff(5)
    return accel.expanding(min_periods=_TD_MON).rank(pct=True)


def dd_drv3_025_curvature_signal_composite(close: pd.Series) -> pd.Series:
    """Composite 3rd-derivative signal: avg of normalized accelerations from dd252, ath, composite."""
    vel_252 = _dd_252d_velocity(close, lag=5)
    accel_252 = vel_252.diff(5)
    z_252 = _zscore_rolling(accel_252, _TD_QTR)

    vel_ath = _dd_ath_velocity(close, lag=5)
    accel_ath = vel_ath.diff(5)
    z_ath = _zscore_rolling(accel_ath, _TD_QTR)

    vel_comp = _composite_dd_velocity(close, lag=5)
    accel_comp = vel_comp.diff(5)
    z_comp = _zscore_rolling(accel_comp, _TD_QTR)

    return (z_252 + z_ath + z_comp) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DEPTH_REGISTRY_3RD_DERIVATIVES = {
    "dd_drv3_001_dd_252d_accel_5d": {"inputs": ["close"], "func": dd_drv3_001_dd_252d_accel_5d},
    "dd_drv3_002_dd_ath_accel_5d": {"inputs": ["close"], "func": dd_drv3_002_dd_ath_accel_5d},
    "dd_drv3_003_log_dd_ath_accel_5d": {"inputs": ["close"], "func": dd_drv3_003_log_dd_ath_accel_5d},
    "dd_drv3_004_underwater_frac_accel_5d": {"inputs": ["close"], "func": dd_drv3_004_underwater_frac_accel_5d},
    "dd_drv3_005_avg_dd_accel_5d": {"inputs": ["close"], "func": dd_drv3_005_avg_dd_accel_5d},
    "dd_drv3_006_sma_cascade_accel_5d": {"inputs": ["close"], "func": dd_drv3_006_sma_cascade_accel_5d},
    "dd_drv3_007_dd_zscore_accel_5d": {"inputs": ["close"], "func": dd_drv3_007_dd_zscore_accel_5d},
    "dd_drv3_008_rsi_accel_5d": {"inputs": ["close"], "func": dd_drv3_008_rsi_accel_5d},
    "dd_drv3_009_composite_dd_accel_5d": {"inputs": ["close"], "func": dd_drv3_009_composite_dd_accel_5d},
    "dd_drv3_010_dd_252d_accel_21d": {"inputs": ["close"], "func": dd_drv3_010_dd_252d_accel_21d},
    "dd_drv3_011_dd_ath_slope_of_velocity_21d": {"inputs": ["close"], "func": dd_drv3_011_dd_ath_slope_of_velocity_21d},
    "dd_drv3_012_log_dd_ath_slope_63d": {"inputs": ["close"], "func": dd_drv3_012_log_dd_ath_slope_63d},
    "dd_drv3_013_underwater_frac_slope_21d": {"inputs": ["close"], "func": dd_drv3_013_underwater_frac_slope_21d},
    "dd_drv3_014_sma_cascade_accel_slope_21d": {"inputs": ["close"], "func": dd_drv3_014_sma_cascade_accel_slope_21d},
    "dd_drv3_015_dd_zscore_accel_slope_21d": {"inputs": ["close"], "func": dd_drv3_015_dd_zscore_accel_slope_21d},
    "dd_drv3_016_dd_252d_vel_zscore_63d": {"inputs": ["close"], "func": dd_drv3_016_dd_252d_vel_zscore_63d},
    "dd_drv3_017_dd_ath_vel_zscore_252d": {"inputs": ["close"], "func": dd_drv3_017_dd_ath_vel_zscore_252d},
    "dd_drv3_018_composite_vel_zscore_63d": {"inputs": ["close"], "func": dd_drv3_018_composite_vel_zscore_63d},
    "dd_drv3_019_rsi_vel_zscore_63d": {"inputs": ["close"], "func": dd_drv3_019_rsi_vel_zscore_63d},
    "dd_drv3_020_dd_252d_accel_pct_rank_63d": {"inputs": ["close"], "func": dd_drv3_020_dd_252d_accel_pct_rank_63d},
    "dd_drv3_021_dd_ath_vel_sign_changes_21d": {"inputs": ["close"], "func": dd_drv3_021_dd_ath_vel_sign_changes_21d},
    "dd_drv3_022_composite_vel_sign_changes_21d": {"inputs": ["close"], "func": dd_drv3_022_composite_vel_sign_changes_21d},
    "dd_drv3_023_dd_252d_vel_ewm_vs_raw_21d": {"inputs": ["close"], "func": dd_drv3_023_dd_252d_vel_ewm_vs_raw_21d},
    "dd_drv3_024_log_dd_ath_accel_pct_rank_252d": {"inputs": ["close"], "func": dd_drv3_024_log_dd_ath_accel_pct_rank_252d},
    "dd_drv3_025_curvature_signal_composite": {"inputs": ["close"], "func": dd_drv3_025_curvature_signal_composite},
}
