"""
34_velocity_inflection — 2nd Derivatives (Features vif_drv2_001-025)
Domain: rate of change of base velocity-inflection concepts — velocity / acceleration
of inflection frequency, regime duration change, flip-magnitude velocity, days-since
change rate, curvature-count velocity.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _velocity(close: pd.Series, span: int) -> pd.Series:
    """EMA-smoothed 1-day log-return (price velocity)."""
    lr = _log_safe(close).diff(1)
    return _ewm_mean(lr, span)


def _sign_flip(s: pd.Series) -> pd.Series:
    """Binary: 1 where sign of s differs from prior row."""
    sg = np.sign(s)
    return ((sg != sg.shift(1)) & sg.notna() & sg.shift(1).notna()).astype(float)


def _days_since_flip(flip: pd.Series) -> pd.Series:
    """Bars elapsed since last 1 in binary flip series (backward-looking)."""
    idx = np.arange(len(flip))
    last_flip_idx = pd.Series(np.where(flip.values == 1, idx, np.nan))
    last_flip_idx = last_flip_idx.ffill()
    result = pd.Series(idx, index=flip.index, dtype=float) - last_flip_idx.values
    result[last_flip_idx.isna().values] = np.nan
    return result


def _rolling_count(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _consec_true(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vif_drv2_001_inflection_count_ema5_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day EMA-5 flip count (velocity of inflection frequency)."""
    cnt = _rolling_count(_sign_flip(_velocity(close, 5)), _TD_MON)
    return cnt.diff(_TD_WEEK)


def vif_drv2_002_inflection_count_ema5_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day EMA-5 flip count (monthly change in flip rate)."""
    cnt = _rolling_count(_sign_flip(_velocity(close, 5)), _TD_QTR)
    return cnt.diff(_TD_MON)


def vif_drv2_003_inflection_count_ema21_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day EMA-21 flip count (monthly flip-rate velocity)."""
    cnt = _rolling_count(_sign_flip(_velocity(close, _TD_MON)), _TD_QTR)
    return cnt.diff(_TD_MON)


def vif_drv2_004_days_since_ema5_flip_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of days-since-EMA-5-flip (staleness velocity)."""
    d = _days_since_flip(_sign_flip(_velocity(close, 5)))
    return d.diff(_TD_WEEK)


def vif_drv2_005_days_since_ema21_flip_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of days-since-EMA-21-flip."""
    d = _days_since_flip(_sign_flip(_velocity(close, _TD_MON)))
    return d.diff(_TD_MON)


def vif_drv2_006_neg_regime_ema21_streak_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive negative EMA-21 regime streak."""
    streak = _consec_true(_velocity(close, _TD_MON) < 0)
    return streak.diff(_TD_WEEK)


def vif_drv2_007_neg_regime_ema5_streak_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive negative EMA-5 regime streak."""
    streak = _consec_true(_velocity(close, 5) < 0)
    return streak.diff(_TD_WEEK)


def vif_drv2_008_vel_ema5_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-5 velocity z-score (acceleration of extremity)."""
    v = _velocity(close, 5)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_WEEK)


def vif_drv2_009_vel_ema21_zscore_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of EMA-21 velocity z-score."""
    v = _velocity(close, _TD_MON)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_MON)


def vif_drv2_010_roc5_flip_count_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day 5-day ROC zero-crossing count."""
    roc = close.pct_change(_TD_WEEK)
    cnt = _rolling_count(_sign_flip(roc), _TD_QTR)
    return cnt.diff(_TD_MON)


def vif_drv2_011_vel_ema5_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of EMA-5 velocity over trailing 21 days (acceleration of velocity)."""
    v = _velocity(close, 5)
    return _linslope(v, _TD_MON)


def vif_drv2_012_vel_ema21_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of EMA-21 velocity over trailing 63 days."""
    v = _velocity(close, _TD_MON)
    return _linslope(v, _TD_QTR)


def vif_drv2_013_ols5_flip_count_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day count of 5-day OLS slope sign-flips."""
    slp = _linslope(_log_safe(close), _TD_WEEK)
    cnt = _rolling_count(_sign_flip(slp), _TD_QTR)
    return cnt.diff(_TD_MON)


def vif_drv2_014_neg_inflection_count_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day bearish EMA-21 inflection count."""
    neg_flips = ((np.sign(_velocity(close, _TD_MON)) < 0) &
                 (np.sign(_velocity(close, _TD_MON)).shift(1) > 0)).astype(float)
    cnt = _rolling_count(neg_flips, _TD_YEAR)
    return cnt.diff(_TD_MON)


def vif_drv2_015_vel_ema5_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of EMA-5 velocity over 21 days."""
    v = _velocity(close, 5)
    slp = _linslope(v, _TD_MON)
    return slp.diff(_TD_WEEK)


def vif_drv2_016_curvature_zero_cross_count_ema5_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day EMA-5 curvature zero-crossing count."""
    v = _velocity(close, 5)
    curv = v.diff(1)
    cnt = _rolling_count(_sign_flip(curv), _TD_MON)
    return cnt.diff(_TD_WEEK)


def vif_drv2_017_days_since_macd_cross_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of days-since-MACD-zero-cross (time since inflection changing)."""
    macd = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    d = _days_since_flip(_sign_flip(macd))
    return d.diff(_TD_WEEK)


def vif_drv2_018_vel_ema5_ema21_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (EMA-5 velocity - EMA-21 velocity) spread."""
    spread = _velocity(close, 5) - _velocity(close, _TD_MON)
    return spread.diff(_TD_WEEK)


def vif_drv2_019_roc21_sign_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day ROC sign (+1/-1), detects recent regime switch."""
    sg = np.sign(close.pct_change(_TD_MON)).astype(float)
    return sg.diff(_TD_WEEK)


def vif_drv2_020_neg_regime_ema21_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of negative-EMA-21-regime streak over trailing 21 days."""
    streak = _consec_true(_velocity(close, _TD_MON) < 0)
    return _linslope(streak, _TD_MON)


def vif_drv2_021_inflection_freq_21d_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21d flip count / 252d avg flip count) ratio."""
    cnt21 = _rolling_count(_sign_flip(_velocity(close, 5)), _TD_MON)
    avg = _rolling_mean(cnt21, _TD_YEAR)
    ratio = _safe_div(cnt21, avg)
    return ratio.diff(_TD_WEEK)


def vif_drv2_022_vel_composite_neg_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite negative-velocity regime score (0-3)."""
    v5 = (_velocity(close, 5) < 0).astype(float)
    v21 = (_velocity(close, _TD_MON) < 0).astype(float)
    v63 = (_velocity(close, _TD_QTR) < 0).astype(float)
    score = v5 + v21 + v63
    return score.diff(_TD_WEEK)


def vif_drv2_023_ols21_flip_count_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day count of 21-day OLS slope sign-flips."""
    slp = _linslope(_log_safe(close), _TD_MON)
    cnt = _rolling_count(_sign_flip(slp), _TD_YEAR)
    return cnt.diff(_TD_MON)


def vif_drv2_024_vel_ema5_pct_rank_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-5 velocity percentile rank (rank momentum)."""
    v = _velocity(close, 5)
    rank = v.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vif_drv2_025_days_since_neg_ema21_flip_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of days-since-last-bearish-EMA-21-flip."""
    neg_flip = ((np.sign(_velocity(close, _TD_MON)) < 0) &
                (np.sign(_velocity(close, _TD_MON)).shift(1) > 0)).astype(float)
    d = _days_since_flip(neg_flip)
    return d.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VELOCITY_INFLECTION_REGISTRY_2ND_DERIVATIVES = {
    "vif_drv2_001_inflection_count_ema5_21d_5d_diff": {"inputs": ["close"], "func": vif_drv2_001_inflection_count_ema5_21d_5d_diff},
    "vif_drv2_002_inflection_count_ema5_63d_21d_diff": {"inputs": ["close"], "func": vif_drv2_002_inflection_count_ema5_63d_21d_diff},
    "vif_drv2_003_inflection_count_ema21_63d_21d_diff": {"inputs": ["close"], "func": vif_drv2_003_inflection_count_ema21_63d_21d_diff},
    "vif_drv2_004_days_since_ema5_flip_5d_diff": {"inputs": ["close"], "func": vif_drv2_004_days_since_ema5_flip_5d_diff},
    "vif_drv2_005_days_since_ema21_flip_21d_diff": {"inputs": ["close"], "func": vif_drv2_005_days_since_ema21_flip_21d_diff},
    "vif_drv2_006_neg_regime_ema21_streak_5d_diff": {"inputs": ["close"], "func": vif_drv2_006_neg_regime_ema21_streak_5d_diff},
    "vif_drv2_007_neg_regime_ema5_streak_5d_diff": {"inputs": ["close"], "func": vif_drv2_007_neg_regime_ema5_streak_5d_diff},
    "vif_drv2_008_vel_ema5_zscore_5d_diff": {"inputs": ["close"], "func": vif_drv2_008_vel_ema5_zscore_5d_diff},
    "vif_drv2_009_vel_ema21_zscore_21d_diff": {"inputs": ["close"], "func": vif_drv2_009_vel_ema21_zscore_21d_diff},
    "vif_drv2_010_roc5_flip_count_63d_21d_diff": {"inputs": ["close"], "func": vif_drv2_010_roc5_flip_count_63d_21d_diff},
    "vif_drv2_011_vel_ema5_slope_21d": {"inputs": ["close"], "func": vif_drv2_011_vel_ema5_slope_21d},
    "vif_drv2_012_vel_ema21_slope_63d": {"inputs": ["close"], "func": vif_drv2_012_vel_ema21_slope_63d},
    "vif_drv2_013_ols5_flip_count_63d_21d_diff": {"inputs": ["close"], "func": vif_drv2_013_ols5_flip_count_63d_21d_diff},
    "vif_drv2_014_neg_inflection_count_252d_21d_diff": {"inputs": ["close"], "func": vif_drv2_014_neg_inflection_count_252d_21d_diff},
    "vif_drv2_015_vel_ema5_slope_5d_diff": {"inputs": ["close"], "func": vif_drv2_015_vel_ema5_slope_5d_diff},
    "vif_drv2_016_curvature_zero_cross_count_ema5_21d_5d_diff": {"inputs": ["close"], "func": vif_drv2_016_curvature_zero_cross_count_ema5_21d_5d_diff},
    "vif_drv2_017_days_since_macd_cross_5d_diff": {"inputs": ["close"], "func": vif_drv2_017_days_since_macd_cross_5d_diff},
    "vif_drv2_018_vel_ema5_ema21_diff_5d_diff": {"inputs": ["close"], "func": vif_drv2_018_vel_ema5_ema21_diff_5d_diff},
    "vif_drv2_019_roc21_sign_5d_diff": {"inputs": ["close"], "func": vif_drv2_019_roc21_sign_5d_diff},
    "vif_drv2_020_neg_regime_ema21_slope_21d": {"inputs": ["close"], "func": vif_drv2_020_neg_regime_ema21_slope_21d},
    "vif_drv2_021_inflection_freq_21d_ratio_5d_diff": {"inputs": ["close"], "func": vif_drv2_021_inflection_freq_21d_ratio_5d_diff},
    "vif_drv2_022_vel_composite_neg_score_5d_diff": {"inputs": ["close"], "func": vif_drv2_022_vel_composite_neg_score_5d_diff},
    "vif_drv2_023_ols21_flip_count_252d_21d_diff": {"inputs": ["close"], "func": vif_drv2_023_ols21_flip_count_252d_21d_diff},
    "vif_drv2_024_vel_ema5_pct_rank_5d_diff": {"inputs": ["close"], "func": vif_drv2_024_vel_ema5_pct_rank_5d_diff},
    "vif_drv2_025_days_since_neg_ema21_flip_21d_diff": {"inputs": ["close"], "func": vif_drv2_025_days_since_neg_ema21_flip_21d_diff},
}
