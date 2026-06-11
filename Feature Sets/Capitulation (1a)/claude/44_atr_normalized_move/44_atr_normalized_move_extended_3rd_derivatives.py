"""
44_atr_normalized_move — Extended 3rd Derivatives (Features atr_extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative ATR concepts — second diff, diff-of-slope,
        slope-of-diff applied to the new-period and new-horizon ATR features.
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low - prev_c).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(_tr(close, high, low), w)


def _daily_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    ret = _log_safe(close) - _log_safe(close.shift(1))
    return _safe_div(ret, _atr(close, high, low, 14))


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


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────

def atr_extdrv3_001_daily_move_atr7_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of daily ATR7-normalized move (acceleration of ultra-short-ATR velocity)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    m = _safe_div(ret, _atr(close, high, low, 7))
    vel = m.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_002_daily_move_atr7_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of daily ATR7-move (jerk in monthly ATR7 pace)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    m = _safe_div(ret, _atr(close, high, low, 7))
    vel21 = m.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def atr_extdrv3_003_daily_move_atr30_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of daily ATR30-normalized move."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    m = _safe_div(ret, _atr(close, high, low, 30))
    vel = m.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_004_3d_move_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 3-day ATR14-normalized move."""
    ret = _log_safe(close) - _log_safe(close.shift(3))
    m = _safe_div(ret, _atr(close, high, low, 14))
    vel = m.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_005_42d_move_atr14_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 42-day ATR14-move."""
    ret = _log_safe(close) - _log_safe(close.shift(42))
    m = _safe_div(ret, _atr(close, high, low, 14))
    vel21 = m.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def atr_extdrv3_006_dist_alltime_high_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of all-time-high ATR14-distance (jerk in deepening rate)."""
    exp_high = close.expanding(min_periods=1).max()
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - exp_high, atr)
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_007_dist_alltime_high_atr14_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of all-time-high ATR14-distance."""
    exp_high = close.expanding(min_periods=1).max()
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - exp_high, atr)
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def atr_extdrv3_008_dist_2yr_high_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 2-year high ATR14-distance (acceleration of 2yr breakdown pace)."""
    high_504 = _rolling_max(close, 504)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - high_504, atr)
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_009_daily_move_atr14_zscore_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR14-move z-score (63d window) — jerk in z-score velocity."""
    m = _daily_move_atr14(close, high, low)
    mu = _rolling_mean(m, _TD_QTR)
    sd = _rolling_std(m, _TD_QTR)
    z = _safe_div(m - mu, sd)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_010_daily_move_atr7_zscore_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR7-move z-score (252d window)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    m = _safe_div(ret, _atr(close, high, low, 7))
    mu = _rolling_mean(m, _TD_YEAR)
    sd = _rolling_std(m, _TD_YEAR)
    z = _safe_div(m - mu, sd)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_011_cum_down_atr_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day cumulative downward ATR14-units."""
    m = _daily_move_atr14(close, high, low)
    cum_dn = m.where(m < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    vel = cum_dn.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_012_lower_wick_atr14_21d_mean_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day mean lower wick in ATR14 units."""
    atr = _atr(close, high, low, 14)
    lw = _safe_div(close - low, atr)
    lw_mean = _rolling_mean(lw, _TD_MON)
    vel = lw_mean.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_013_count_gt1atr_down_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day count of moves < -1 ATR14."""
    m = _daily_move_atr14(close, high, low)
    cnt = _rolling_sum((m < -1).astype(float), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_014_composite_distress_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of composite distress score (drawdowns from 5/21/63-day highs)."""
    atr = _atr(close, high, low, 14)
    d5 = _safe_div(close - _rolling_max(close, _TD_WEEK), atr).clip(upper=0)
    d21 = _safe_div(close - _rolling_max(close, _TD_MON), atr).clip(upper=0)
    d63 = _safe_div(close - _rolling_max(close, _TD_QTR), atr).clip(upper=0)
    composite = d5 + d21 + d63
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_015_atr_velocity_63d_ewm_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM(63)-smoothed ATR14-velocity."""
    m = _daily_move_atr14(close, high, low)
    vel_ewm = _ewm_mean(m, _TD_QTR)
    vel = vel_ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_016_dist_below_sma200_atr14_slope_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of SMA200 ATR14-distance (rate of slope change)."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    slp = _linslope(dist, _TD_MON)
    return slp.diff(_TD_WEEK)


def atr_extdrv3_017_dist_alltime_high_atr14_slope_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of all-time-high ATR14-distance."""
    exp_high = close.expanding(min_periods=1).max()
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - exp_high, atr)
    slp = _linslope(dist, _TD_MON)
    return slp.diff(_TD_WEEK)


def atr_extdrv3_018_126d_move_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 126-day ATR14-normalized move."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_HALF))
    m = _safe_div(ret, _atr(close, high, low, 14))
    vel = m.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_019_wick_imbalance_atr14_21d_mean_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day mean wick imbalance in ATR14 units."""
    atr = _atr(close, high, low, 14)
    wi = _safe_div(close - low, atr) - _safe_div(high - close, atr)
    wi_mean = _rolling_mean(wi, _TD_MON)
    vel = wi_mean.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_020_drawdown_252d_atr7_zscore_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of expanding z-score of 252d-high drawdown in ATR7 units."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 7)
    dd = _safe_div(close - high_252, atr)
    mu = dd.expanding(min_periods=5).mean()
    sd = dd.expanding(min_periods=5).std()
    z = _safe_div(dd - mu, sd)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_021_atr14_capitulation_composite_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR14 capitulation composite (SMA200-dist + 252d-dd + 21d-velocity)."""
    atr = _atr(close, high, low, 14)
    ma_dist = _safe_div(close - _rolling_mean(close, 200), atr)
    dd_252 = _safe_div(close - _rolling_max(close, _TD_YEAR), atr)
    vel_21 = _rolling_mean(_daily_move_atr14(close, high, low), _TD_MON)
    composite = ma_dist + dd_252 + vel_21
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_022_intraday_range_atr14_21d_mean_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day mean intraday range in ATR14 units."""
    rng = _safe_div(high - low, _atr(close, high, low, 14))
    rng_mean = _rolling_mean(rng, _TD_MON)
    vel = rng_mean.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_023_consec_down_atr14_days_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive down-day ATR14 streak."""
    m = _daily_move_atr14(close, high, low)
    cond = m < 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum().astype(float)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_024_dist_below_sma21_atr14_pct_rank_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of SMA21 ATR14-distance percentile rank (252d window)."""
    ma = _rolling_mean(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    pr = dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_extdrv3_025_cum_down_atr_63d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of 63-day cumulative downward ATR14-units."""
    m = _daily_move_atr14(close, high, low)
    cum_dn = m.where(m < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    vel = cum_dn.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

ATR_NORMALIZED_MOVE_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "atr_extdrv3_001_daily_move_atr7_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_001_daily_move_atr7_5d_diff_5d_diff},
    "atr_extdrv3_002_daily_move_atr7_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_002_daily_move_atr7_21d_diff_5d_diff},
    "atr_extdrv3_003_daily_move_atr30_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_003_daily_move_atr30_5d_diff_5d_diff},
    "atr_extdrv3_004_3d_move_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_004_3d_move_atr14_5d_diff_5d_diff},
    "atr_extdrv3_005_42d_move_atr14_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_005_42d_move_atr14_21d_diff_5d_diff},
    "atr_extdrv3_006_dist_alltime_high_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_006_dist_alltime_high_atr14_5d_diff_5d_diff},
    "atr_extdrv3_007_dist_alltime_high_atr14_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_007_dist_alltime_high_atr14_21d_diff_5d_diff},
    "atr_extdrv3_008_dist_2yr_high_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_008_dist_2yr_high_atr14_5d_diff_5d_diff},
    "atr_extdrv3_009_daily_move_atr14_zscore_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_009_daily_move_atr14_zscore_63d_5d_diff_5d_diff},
    "atr_extdrv3_010_daily_move_atr7_zscore_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_010_daily_move_atr7_zscore_252d_5d_diff_5d_diff},
    "atr_extdrv3_011_cum_down_atr_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_011_cum_down_atr_63d_5d_diff_5d_diff},
    "atr_extdrv3_012_lower_wick_atr14_21d_mean_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_012_lower_wick_atr14_21d_mean_5d_diff_5d_diff},
    "atr_extdrv3_013_count_gt1atr_down_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_013_count_gt1atr_down_21d_5d_diff_5d_diff},
    "atr_extdrv3_014_composite_distress_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_014_composite_distress_atr14_5d_diff_5d_diff},
    "atr_extdrv3_015_atr_velocity_63d_ewm_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_015_atr_velocity_63d_ewm_5d_diff_5d_diff},
    "atr_extdrv3_016_dist_below_sma200_atr14_slope_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_016_dist_below_sma200_atr14_slope_21d_5d_diff},
    "atr_extdrv3_017_dist_alltime_high_atr14_slope_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_017_dist_alltime_high_atr14_slope_21d_5d_diff},
    "atr_extdrv3_018_126d_move_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_018_126d_move_atr14_5d_diff_5d_diff},
    "atr_extdrv3_019_wick_imbalance_atr14_21d_mean_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_019_wick_imbalance_atr14_21d_mean_5d_diff_5d_diff},
    "atr_extdrv3_020_drawdown_252d_atr7_zscore_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_020_drawdown_252d_atr7_zscore_5d_diff_5d_diff},
    "atr_extdrv3_021_atr14_capitulation_composite_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_021_atr14_capitulation_composite_5d_diff_5d_diff},
    "atr_extdrv3_022_intraday_range_atr14_21d_mean_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_022_intraday_range_atr14_21d_mean_5d_diff_5d_diff},
    "atr_extdrv3_023_consec_down_atr14_days_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_023_consec_down_atr14_days_5d_diff_5d_diff},
    "atr_extdrv3_024_dist_below_sma21_atr14_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_024_dist_below_sma21_atr14_pct_rank_252d_5d_diff_5d_diff},
    "atr_extdrv3_025_cum_down_atr_63d_slope_21d": {"inputs": ["close", "high", "low"], "func": atr_extdrv3_025_cum_down_atr_63d_slope_21d},
}
