"""
44_atr_normalized_move — 2nd Derivatives (Features atr_drv2_001-025)
Domain: rate of change of ATR-normalized move base concepts — velocity of ATR-unit moves
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def atr_drv2_001_daily_move_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of daily ATR14-normalized move (velocity of move size)."""
    m = _daily_move_atr14(close, high, low)
    return m.diff(_TD_WEEK)


def atr_drv2_002_daily_move_atr14_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of daily ATR14-normalized move (monthly velocity)."""
    m = _daily_move_atr14(close, high, low)
    return m.diff(_TD_MON)


def atr_drv2_003_5d_move_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5-day ATR14-normalized move (acceleration of weekly move)."""
    atr = _atr(close, high, low, 14)
    m5 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_WEEK)), atr)
    return m5.diff(_TD_WEEK)


def atr_drv2_004_21d_move_atr14_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21-day ATR14-normalized move."""
    atr = _atr(close, high, low, 14)
    m21 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_MON)), atr)
    return m21.diff(_TD_MON)


def atr_drv2_005_cum_down_atr_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative downward ATR14-units (velocity of down accumulation)."""
    m = _daily_move_atr14(close, high, low)
    cum_dn = m.where(m < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    return cum_dn.diff(_TD_WEEK)


def atr_drv2_006_dist_below_sma200_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of SMA200 ATR14-distance (rate of MA dislocation change)."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return dist.diff(_TD_WEEK)


def atr_drv2_007_dist_below_sma200_atr14_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of SMA200 ATR14-distance."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return dist.diff(_TD_MON)


def atr_drv2_008_dist_below_sma21_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of SMA21 ATR14-distance."""
    ma = _rolling_mean(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return dist.diff(_TD_WEEK)


def atr_drv2_009_drawdown_52wk_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 252-day high ATR14-drawdown (rate of drawdown deepening)."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dd = _safe_div(close - high_252, atr)
    return dd.diff(_TD_WEEK)


def atr_drv2_010_drawdown_52wk_atr14_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 252-day high ATR14-drawdown."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dd = _safe_div(close - high_252, atr)
    return dd.diff(_TD_MON)


def atr_drv2_011_atr_velocity_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day ATR-velocity (rate of velocity change)."""
    m = _daily_move_atr14(close, high, low)
    v21 = _rolling_mean(m, _TD_MON)
    return v21.diff(_TD_WEEK)


def atr_drv2_012_atr_velocity_21d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21-day ATR-velocity."""
    m = _daily_move_atr14(close, high, low)
    v21 = _rolling_mean(m, _TD_MON)
    return v21.diff(_TD_MON)


def atr_drv2_013_cum_atr_traveled_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative ATR14-units traveled."""
    m = _daily_move_atr14(close, high, low).abs()
    path = _rolling_sum(m, _TD_MON)
    return path.diff(_TD_WEEK)


def atr_drv2_014_down_vs_up_atr_ratio_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day down/up ATR-unit ratio."""
    m = _daily_move_atr14(close, high, low)
    down = m.where(m < 0, 0.0).rolling(_TD_MON, min_periods=1).sum().abs()
    up = m.where(m > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    ratio = _safe_div(down, up)
    return ratio.diff(_TD_WEEK)


def atr_drv2_015_dist_from_52wk_high_atr14_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 252-day high ATR14-distance."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - high_252, atr)
    return _linslope(dist, _TD_MON)


def atr_drv2_016_net_atr14_move_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of net 21-day ATR14-unit move."""
    m = _daily_move_atr14(close, high, low)
    net21 = _rolling_sum(m, _TD_MON)
    return net21.diff(_TD_WEEK)


def atr_drv2_017_net_vs_gross_atr14_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of net/gross ATR14 directionality ratio over 21 days."""
    m = _daily_move_atr14(close, high, low)
    net = _rolling_sum(m, _TD_MON)
    gross = _rolling_sum(m.abs(), _TD_MON)
    ratio = _safe_div(net, gross)
    return ratio.diff(_TD_WEEK)


def atr_drv2_018_count_gt2atr_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day count of |move| > 2 ATR14 (rate of extreme-day frequency change)."""
    m = _daily_move_atr14(close, high, low).abs()
    cnt = _rolling_sum((m > 2).astype(float), _TD_MON)
    return cnt.diff(_TD_WEEK)


def atr_drv2_019_intraday_range_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of intraday range in ATR14 units."""
    rng = _safe_div(high - low, _atr(close, high, low, 14))
    return rng.diff(_TD_WEEK)


def atr_drv2_020_dist_below_sma200_atr14_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 63 days of SMA200 ATR14-distance."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return _linslope(dist, _TD_QTR)


def atr_drv2_021_atr_speed_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day ATR14-speed (|move|)."""
    speed = _rolling_mean(_daily_move_atr14(close, high, low).abs(), _TD_MON)
    return speed.diff(_TD_WEEK)


def atr_drv2_022_down_vs_total_speed_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day down-fraction of ATR14-speed."""
    m = _daily_move_atr14(close, high, low)
    down_sum = m.where(m < 0, 0.0).rolling(_TD_MON, min_periods=1).sum().abs()
    total_sum = m.abs().rolling(_TD_MON, min_periods=1).sum()
    ratio = _safe_div(down_sum, total_sum)
    return ratio.diff(_TD_WEEK)


def atr_drv2_023_63d_move_atr21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63-day ATR21-normalized move."""
    atr = _atr(close, high, low, _TD_MON)
    m63 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_QTR)), atr)
    return m63.diff(_TD_WEEK)


def atr_drv2_024_composite_ma_dist_atr14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of composite MA ATR14-distance score."""
    atr = _atr(close, high, low, 14)
    d21 = _safe_div(close - _rolling_mean(close, _TD_MON), atr)
    d63 = _safe_div(close - _rolling_mean(close, _TD_QTR), atr)
    d200 = _safe_div(close - _rolling_mean(close, 200), atr)
    composite = (d21 + d63 + d200) / 3.0
    return composite.diff(_TD_WEEK)


def atr_drv2_025_daily_move_atr14_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of daily ATR14-normalized move."""
    m = _daily_move_atr14(close, high, low)
    return _linslope(m, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

ATR_NORMALIZED_MOVE_REGISTRY_2ND_DERIVATIVES = {
    "atr_drv2_001_daily_move_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_001_daily_move_atr14_5d_diff},
    "atr_drv2_002_daily_move_atr14_21d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_002_daily_move_atr14_21d_diff},
    "atr_drv2_003_5d_move_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_003_5d_move_atr14_5d_diff},
    "atr_drv2_004_21d_move_atr14_21d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_004_21d_move_atr14_21d_diff},
    "atr_drv2_005_cum_down_atr_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_005_cum_down_atr_21d_5d_diff},
    "atr_drv2_006_dist_below_sma200_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_006_dist_below_sma200_atr14_5d_diff},
    "atr_drv2_007_dist_below_sma200_atr14_21d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_007_dist_below_sma200_atr14_21d_diff},
    "atr_drv2_008_dist_below_sma21_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_008_dist_below_sma21_atr14_5d_diff},
    "atr_drv2_009_drawdown_52wk_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_009_drawdown_52wk_atr14_5d_diff},
    "atr_drv2_010_drawdown_52wk_atr14_21d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_010_drawdown_52wk_atr14_21d_diff},
    "atr_drv2_011_atr_velocity_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_011_atr_velocity_21d_5d_diff},
    "atr_drv2_012_atr_velocity_21d_21d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_012_atr_velocity_21d_21d_diff},
    "atr_drv2_013_cum_atr_traveled_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_013_cum_atr_traveled_21d_5d_diff},
    "atr_drv2_014_down_vs_up_atr_ratio_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_014_down_vs_up_atr_ratio_21d_5d_diff},
    "atr_drv2_015_dist_from_52wk_high_atr14_slope_21d": {"inputs": ["close", "high", "low"], "func": atr_drv2_015_dist_from_52wk_high_atr14_slope_21d},
    "atr_drv2_016_net_atr14_move_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_016_net_atr14_move_21d_5d_diff},
    "atr_drv2_017_net_vs_gross_atr14_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_017_net_vs_gross_atr14_21d_5d_diff},
    "atr_drv2_018_count_gt2atr_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_018_count_gt2atr_21d_5d_diff},
    "atr_drv2_019_intraday_range_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_019_intraday_range_atr14_5d_diff},
    "atr_drv2_020_dist_below_sma200_atr14_slope_63d": {"inputs": ["close", "high", "low"], "func": atr_drv2_020_dist_below_sma200_atr14_slope_63d},
    "atr_drv2_021_atr_speed_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_021_atr_speed_21d_5d_diff},
    "atr_drv2_022_down_vs_total_speed_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_022_down_vs_total_speed_21d_5d_diff},
    "atr_drv2_023_63d_move_atr21_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_023_63d_move_atr21_5d_diff},
    "atr_drv2_024_composite_ma_dist_atr14_5d_diff": {"inputs": ["close", "high", "low"], "func": atr_drv2_024_composite_ma_dist_atr14_5d_diff},
    "atr_drv2_025_daily_move_atr14_slope_21d": {"inputs": ["close", "high", "low"], "func": atr_drv2_025_daily_move_atr14_slope_21d},
}
