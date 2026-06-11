"""
44_atr_normalized_move — 3rd Derivatives (Features atr_drv3_001-025)
Domain: rate of change of 2nd-derivative ATR-normalized move concepts — acceleration of velocity
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def atr_drv3_001_daily_move_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of daily ATR14-move (acceleration of move velocity)."""
    m = _daily_move_atr14(close, high, low)
    vel = m.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_002_daily_move_atr14_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day-velocity of daily ATR14-move (jerk in monthly pace)."""
    m = _daily_move_atr14(close, high, low)
    vel21 = m.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def atr_drv3_003_5d_move_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day ATR14-move (2nd acceleration of weekly move)."""
    atr = _atr(close, high, low, 14)
    m5 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_WEEK)), atr)
    vel = m5.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_004_dist_below_sma200_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of SMA200 ATR14-distance (acceleration of MA breakdown pace)."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_005_drawdown_52wk_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day high ATR14-drawdown (jerk in drawdown rate)."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dd = _safe_div(close - high_252, atr)
    vel = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_006_atr_velocity_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day ATR-velocity (acceleration of velocity)."""
    m = _daily_move_atr14(close, high, low)
    v21 = _rolling_mean(m, _TD_MON)
    vel = v21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_007_cum_down_atr_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day cumulative downward ATR-units (jerk in down accumulation)."""
    m = _daily_move_atr14(close, high, low)
    cum_dn = m.where(m < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    vel = cum_dn.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_008_net_atr14_move_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of net 21-day ATR14-unit move."""
    m = _daily_move_atr14(close, high, low)
    net21 = _rolling_sum(m, _TD_MON)
    vel = net21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_009_dist_below_sma200_atr14_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of SMA200 ATR14-distance (rate of slope change)."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    slp = _linslope(dist, _TD_MON)
    return slp.diff(_TD_WEEK)


def atr_drv3_010_dist_from_52wk_high_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day high ATR14-distance."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - high_252, atr)
    slp = _linslope(dist, _TD_MON)
    return slp.diff(_TD_WEEK)


def atr_drv3_011_down_vs_up_atr_ratio_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day down/up ATR-unit ratio."""
    m = _daily_move_atr14(close, high, low)
    down = m.where(m < 0, 0.0).rolling(_TD_MON, min_periods=1).sum().abs()
    up = m.where(m > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    ratio = _safe_div(down, up)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_012_count_gt2atr_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day extreme-move count (jerk in extreme frequency)."""
    m = _daily_move_atr14(close, high, low).abs()
    cnt = _rolling_sum((m > 2).astype(float), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_013_atr_speed_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day ATR14-speed."""
    speed = _rolling_mean(_daily_move_atr14(close, high, low).abs(), _TD_MON)
    vel = speed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_014_composite_ma_dist_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of composite MA ATR14-distance score."""
    atr = _atr(close, high, low, 14)
    d21 = _safe_div(close - _rolling_mean(close, _TD_MON), atr)
    d63 = _safe_div(close - _rolling_mean(close, _TD_QTR), atr)
    d200 = _safe_div(close - _rolling_mean(close, 200), atr)
    composite = (d21 + d63 + d200) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_015_intraday_range_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of intraday range in ATR14 units."""
    rng = _safe_div(high - low, _atr(close, high, low, 14))
    vel = rng.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_016_21d_move_atr14_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day ATR14-move."""
    atr = _atr(close, high, low, 14)
    m21 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_MON)), atr)
    vel21 = m21.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def atr_drv3_017_drawdown_52wk_atr14_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day high ATR14-drawdown."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dd = _safe_div(close - high_252, atr)
    vel21 = dd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def atr_drv3_018_dist_below_sma21_atr14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of SMA21 ATR14-distance."""
    ma = _rolling_mean(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_019_down_vs_total_speed_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day down-fraction of ATR14-speed."""
    m = _daily_move_atr14(close, high, low)
    down_sum = m.where(m < 0, 0.0).rolling(_TD_MON, min_periods=1).sum().abs()
    total_sum = m.abs().rolling(_TD_MON, min_periods=1).sum()
    ratio = _safe_div(down_sum, total_sum)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_020_net_vs_gross_atr14_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of net/gross ATR14 directionality ratio."""
    m = _daily_move_atr14(close, high, low)
    net = _rolling_sum(m, _TD_MON)
    gross = _rolling_sum(m.abs(), _TD_MON)
    ratio = _safe_div(net, gross)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_021_cum_atr_traveled_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day cumulative ATR14-path length."""
    m = _daily_move_atr14(close, high, low).abs()
    path = _rolling_sum(m, _TD_MON)
    vel = path.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def atr_drv3_022_daily_move_atr14_slope_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of daily ATR14-move over 21 days."""
    m = _daily_move_atr14(close, high, low)
    slp = _linslope(m, _TD_MON)
    return slp.diff(_TD_WEEK)


def atr_drv3_023_dist_below_sma200_atr14_slope_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of SMA200 ATR14-distance over 63 days."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    slp = _linslope(dist, _TD_QTR)
    return slp.diff(_TD_WEEK)


def atr_drv3_024_atr_velocity_21d_5d_diff_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-diff of 21-day ATR-velocity."""
    m = _daily_move_atr14(close, high, low)
    v21 = _rolling_mean(m, _TD_MON)
    vel = v21.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def atr_drv3_025_63d_move_atr21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day ATR21-normalized move."""
    atr = _atr(close, high, low, _TD_MON)
    m63 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_QTR)), atr)
    vel = m63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

ATR_NORMALIZED_MOVE_REGISTRY_3RD_DERIVATIVES = {
    "atr_drv3_001_daily_move_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_001_daily_move_atr14_5d_diff_5d_diff},
    "atr_drv3_002_daily_move_atr14_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_002_daily_move_atr14_21d_diff_5d_diff},
    "atr_drv3_003_5d_move_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_003_5d_move_atr14_5d_diff_5d_diff},
    "atr_drv3_004_dist_below_sma200_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_004_dist_below_sma200_atr14_5d_diff_5d_diff},
    "atr_drv3_005_drawdown_52wk_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_005_drawdown_52wk_atr14_5d_diff_5d_diff},
    "atr_drv3_006_atr_velocity_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_006_atr_velocity_21d_5d_diff_5d_diff},
    "atr_drv3_007_cum_down_atr_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_007_cum_down_atr_21d_5d_diff_5d_diff},
    "atr_drv3_008_net_atr14_move_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_008_net_atr14_move_21d_5d_diff_5d_diff},
    "atr_drv3_009_dist_below_sma200_atr14_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_009_dist_below_sma200_atr14_slope_5d_diff},
    "atr_drv3_010_dist_from_52wk_high_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_010_dist_from_52wk_high_slope_5d_diff},
    "atr_drv3_011_down_vs_up_atr_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_011_down_vs_up_atr_ratio_21d_5d_diff_5d_diff},
    "atr_drv3_012_count_gt2atr_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_012_count_gt2atr_21d_5d_diff_5d_diff},
    "atr_drv3_013_atr_speed_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_013_atr_speed_21d_5d_diff_5d_diff},
    "atr_drv3_014_composite_ma_dist_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_014_composite_ma_dist_atr14_5d_diff_5d_diff},
    "atr_drv3_015_intraday_range_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_015_intraday_range_atr14_5d_diff_5d_diff},
    "atr_drv3_016_21d_move_atr14_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_016_21d_move_atr14_21d_diff_5d_diff},
    "atr_drv3_017_drawdown_52wk_atr14_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_017_drawdown_52wk_atr14_21d_diff_5d_diff},
    "atr_drv3_018_dist_below_sma21_atr14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_018_dist_below_sma21_atr14_5d_diff_5d_diff},
    "atr_drv3_019_down_vs_total_speed_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_019_down_vs_total_speed_21d_5d_diff_5d_diff},
    "atr_drv3_020_net_vs_gross_atr14_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_020_net_vs_gross_atr14_21d_5d_diff_5d_diff},
    "atr_drv3_021_cum_atr_traveled_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_021_cum_atr_traveled_21d_5d_diff_5d_diff},
    "atr_drv3_022_daily_move_atr14_slope_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_022_daily_move_atr14_slope_21d_5d_diff},
    "atr_drv3_023_dist_below_sma200_atr14_slope_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_023_dist_below_sma200_atr14_slope_63d_5d_diff},
    "atr_drv3_024_atr_velocity_21d_5d_diff_slope_21d": {"inputs": ["close", "high", "low"], "func": atr_drv3_024_atr_velocity_21d_5d_diff_slope_21d},
    "atr_drv3_025_63d_move_atr21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv3_025_63d_move_atr21_5d_diff_5d_diff},
}
