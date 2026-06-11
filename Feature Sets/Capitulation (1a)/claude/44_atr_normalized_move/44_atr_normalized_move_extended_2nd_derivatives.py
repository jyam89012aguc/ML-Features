"""
44_atr_normalized_move — Extended 2nd Derivatives (Features atr_extdrv2_001-025)
Domain: rate of change of extended ATR-normalized move concepts — diff/pct_change/OLS-slope
        applied to the new ATR periods, multi-horizon moves, expanded drawdown references,
        and gap/wick aggregates introduced in the extended_001_075 file.
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


# ── Extended 2nd-Derivative Feature Functions ─────────────────────────────────

def atr_extdrv2_001_daily_move_atr7_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of daily ATR7-normalized move (velocity using ultra-short ATR)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    m = _safe_div(ret, _atr(close, high, low, 7))
    return m.diff(_TD_WEEK)


def atr_extdrv2_002_daily_move_atr7_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of daily ATR7-normalized move."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    m = _safe_div(ret, _atr(close, high, low, 7))
    return m.diff(_TD_MON)


def atr_extdrv2_003_daily_move_atr30_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of daily ATR30-normalized move."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    m = _safe_div(ret, _atr(close, high, low, 30))
    return m.diff(_TD_WEEK)


def atr_extdrv2_004_3d_move_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 3-day ATR14-normalized move (acceleration of 3d burst)."""
    ret = _log_safe(close) - _log_safe(close.shift(3))
    m = _safe_div(ret, _atr(close, high, low, 14))
    return m.diff(_TD_WEEK)


def atr_extdrv2_005_42d_move_atr14_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 42-day ATR14-normalized move."""
    ret = _log_safe(close) - _log_safe(close.shift(42))
    m = _safe_div(ret, _atr(close, high, low, 14))
    return m.diff(_TD_MON)


def atr_extdrv2_006_dist_alltime_high_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of all-time-high ATR14-distance (rate of all-time-low deepening)."""
    exp_high = close.expanding(min_periods=1).max()
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - exp_high, atr)
    return dist.diff(_TD_WEEK)


def atr_extdrv2_007_dist_alltime_high_atr14_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of all-time-high ATR14-distance."""
    exp_high = close.expanding(min_periods=1).max()
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - exp_high, atr)
    return dist.diff(_TD_MON)


def atr_extdrv2_008_dist_2yr_high_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 2-year high ATR14-distance."""
    high_504 = _rolling_max(close, 504)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - high_504, atr)
    return dist.diff(_TD_WEEK)


def atr_extdrv2_009_daily_move_atr14_zscore_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR14-move z-score (63d window)."""
    m = _daily_move_atr14(close, high, low)
    mu = _rolling_mean(m, _TD_QTR)
    sd = _rolling_std(m, _TD_QTR)
    z = _safe_div(m - mu, sd)
    return z.diff(_TD_WEEK)


def atr_extdrv2_010_daily_move_atr7_zscore_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR7-move z-score (252d window)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    m = _safe_div(ret, _atr(close, high, low, 7))
    mu = _rolling_mean(m, _TD_YEAR)
    sd = _rolling_std(m, _TD_YEAR)
    z = _safe_div(m - mu, sd)
    return z.diff(_TD_WEEK)


def atr_extdrv2_011_daily_move_atr14_pct_rank_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR14-move percentile rank (63d window)."""
    m = _daily_move_atr14(close, high, low)
    pr = m.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return pr.diff(_TD_WEEK)


def atr_extdrv2_012_cum_down_atr_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63-day cumulative downward ATR14-units (velocity of down accumulation)."""
    m = _daily_move_atr14(close, high, low)
    cum_dn = m.where(m < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    return cum_dn.diff(_TD_WEEK)


def atr_extdrv2_013_lower_wick_atr14_21d_mean_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day mean lower wick in ATR14 units."""
    atr = _atr(close, high, low, 14)
    lw = _safe_div(close - low, atr)
    lw_mean = _rolling_mean(lw, _TD_MON)
    return lw_mean.diff(_TD_WEEK)


def atr_extdrv2_014_wick_imbalance_atr14_21d_mean_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day mean wick imbalance in ATR14 units."""
    atr = _atr(close, high, low, 14)
    wi = _safe_div(close - low, atr) - _safe_div(high - close, atr)
    wi_mean = _rolling_mean(wi, _TD_MON)
    return wi_mean.diff(_TD_WEEK)


def atr_extdrv2_015_count_gt1atr_down_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day count of moves < -1 ATR14 (rate of moderate down-frequency)."""
    m = _daily_move_atr14(close, high, low)
    cnt = _rolling_sum((m < -1).astype(float), _TD_MON)
    return cnt.diff(_TD_WEEK)


def atr_extdrv2_016_drawdown_252d_atr7_zscore_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of expanding z-score of 252d-high drawdown in ATR7 units."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 7)
    dd = _safe_div(close - high_252, atr)
    mu = dd.expanding(min_periods=5).mean()
    sd = dd.expanding(min_periods=5).std()
    z = _safe_div(dd - mu, sd)
    return z.diff(_TD_WEEK)


def atr_extdrv2_017_126d_move_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 126-day ATR14-normalized move."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_HALF))
    m = _safe_div(ret, _atr(close, high, low, 14))
    return m.diff(_TD_WEEK)


def atr_extdrv2_018_dist_below_sma200_atr14_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of SMA200 ATR14-distance (medium-term rate of breakdown)."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return _linslope(dist, _TD_MON)


def atr_extdrv2_019_atr_velocity_63d_ewm_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of EWM(63)-smoothed ATR14-velocity."""
    m = _daily_move_atr14(close, high, low)
    vel_ewm = _ewm_mean(m, _TD_QTR)
    return vel_ewm.diff(_TD_WEEK)


def atr_extdrv2_020_composite_distress_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of composite distress score (sum of drawdowns from 5/21/63-day highs in ATR14)."""
    atr = _atr(close, high, low, 14)
    d5 = _safe_div(close - _rolling_max(close, _TD_WEEK), atr).clip(upper=0)
    d21 = _safe_div(close - _rolling_max(close, _TD_MON), atr).clip(upper=0)
    d63 = _safe_div(close - _rolling_max(close, _TD_QTR), atr).clip(upper=0)
    composite = d5 + d21 + d63
    return composite.diff(_TD_WEEK)


def atr_extdrv2_021_dist_alltime_high_atr14_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of all-time-high ATR14-distance."""
    exp_high = close.expanding(min_periods=1).max()
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - exp_high, atr)
    return _linslope(dist, _TD_MON)


def atr_extdrv2_022_intraday_range_atr14_21d_mean_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day mean intraday range in ATR14 units."""
    rng = _safe_div(high - low, _atr(close, high, low, 14))
    rng_mean = _rolling_mean(rng, _TD_MON)
    return rng_mean.diff(_TD_WEEK)


def atr_extdrv2_023_consec_down_atr14_days_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of consecutive down-day ATR14 streak length."""
    m = _daily_move_atr14(close, high, low)
    cond = m < 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum().astype(float)
    return streak.diff(_TD_WEEK)


def atr_extdrv2_024_dist_below_sma21_atr14_pct_rank_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of SMA21 ATR14-distance percentile rank (252d window)."""
    ma = _rolling_mean(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    pr = dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pr.diff(_TD_WEEK)


def atr_extdrv2_025_atr14_capitulation_composite_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR14 capitulation composite (SMA200-dist + 252d-drawdown + 21d-velocity)."""
    atr = _atr(close, high, low, 14)
    ma_dist = _safe_div(close - _rolling_mean(close, 200), atr)
    dd_252 = _safe_div(close - _rolling_max(close, _TD_YEAR), atr)
    vel_21 = _rolling_mean(_daily_move_atr14(close, high, low), _TD_MON)
    composite = ma_dist + dd_252 + vel_21
    return composite.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

ATR_NORMALIZED_MOVE_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "atr_extdrv2_001_daily_move_atr7_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_001_daily_move_atr7_5d_diff},
    "atr_extdrv2_002_daily_move_atr7_21d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_002_daily_move_atr7_21d_diff},
    "atr_extdrv2_003_daily_move_atr30_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_003_daily_move_atr30_5d_diff},
    "atr_extdrv2_004_3d_move_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_004_3d_move_atr14_5d_diff},
    "atr_extdrv2_005_42d_move_atr14_21d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_005_42d_move_atr14_21d_diff},
    "atr_extdrv2_006_dist_alltime_high_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_006_dist_alltime_high_atr14_5d_diff},
    "atr_extdrv2_007_dist_alltime_high_atr14_21d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_007_dist_alltime_high_atr14_21d_diff},
    "atr_extdrv2_008_dist_2yr_high_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_008_dist_2yr_high_atr14_5d_diff},
    "atr_extdrv2_009_daily_move_atr14_zscore_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_009_daily_move_atr14_zscore_63d_5d_diff},
    "atr_extdrv2_010_daily_move_atr7_zscore_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_010_daily_move_atr7_zscore_252d_5d_diff},
    "atr_extdrv2_011_daily_move_atr14_pct_rank_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_011_daily_move_atr14_pct_rank_63d_5d_diff},
    "atr_extdrv2_012_cum_down_atr_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_012_cum_down_atr_63d_5d_diff},
    "atr_extdrv2_013_lower_wick_atr14_21d_mean_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_013_lower_wick_atr14_21d_mean_5d_diff},
    "atr_extdrv2_014_wick_imbalance_atr14_21d_mean_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_014_wick_imbalance_atr14_21d_mean_5d_diff},
    "atr_extdrv2_015_count_gt1atr_down_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_015_count_gt1atr_down_21d_5d_diff},
    "atr_extdrv2_016_drawdown_252d_atr7_zscore_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_016_drawdown_252d_atr7_zscore_5d_diff},
    "atr_extdrv2_017_126d_move_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_017_126d_move_atr14_5d_diff},
    "atr_extdrv2_018_dist_below_sma200_atr14_slope_21d": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_018_dist_below_sma200_atr14_slope_21d},
    "atr_extdrv2_019_atr_velocity_63d_ewm_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_019_atr_velocity_63d_ewm_5d_diff},
    "atr_extdrv2_020_composite_distress_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_020_composite_distress_atr14_5d_diff},
    "atr_extdrv2_021_dist_alltime_high_atr14_slope_21d": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_021_dist_alltime_high_atr14_slope_21d},
    "atr_extdrv2_022_intraday_range_atr14_21d_mean_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_022_intraday_range_atr14_21d_mean_5d_diff},
    "atr_extdrv2_023_consec_down_atr14_days_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_023_consec_down_atr14_days_5d_diff},
    "atr_extdrv2_024_dist_below_sma21_atr14_pct_rank_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_024_dist_below_sma21_atr14_pct_rank_252d_5d_diff},
    "atr_extdrv2_025_atr14_capitulation_composite_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_extdrv2_025_atr14_capitulation_composite_5d_diff},
}
