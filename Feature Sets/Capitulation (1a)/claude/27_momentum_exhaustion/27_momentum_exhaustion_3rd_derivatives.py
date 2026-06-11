"""
27_momentum_exhaustion — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative momentum-exhaustion features — acceleration of velocity
Includes 3rd-order derivatives of ROC, Kaufman ER, TD/DeMark, and legacy signals.
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


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _down_ret_abs(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    return r.abs().where(r < 0, np.nan)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


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


def _roc(close: pd.Series, n: int) -> pd.Series:
    """Rate of Change over n periods."""
    return _safe_div(close, close.shift(n).replace(0, np.nan)) * 100.0 - 100.0


def _kaufman_er(close: pd.Series, n: int) -> pd.Series:
    """Kaufman Efficiency Ratio over n periods."""
    direction = (close - close.shift(n)).abs()
    volatility = close.diff(1).abs().rolling(n, min_periods=max(2, n // 2)).sum()
    return _safe_div(direction, volatility)


def _td_buy_setup_count(close: pd.Series) -> pd.Series:
    """TD/DeMark buy-setup running count (backward-looking); capped at 13."""
    condition = (close < close.shift(4)).astype(int).values
    n = len(condition)
    counts = np.zeros(n, dtype=float)
    counts[:] = np.nan
    running = 0
    for i in range(4, n):
        if np.isnan(close.iloc[i]) or np.isnan(close.iloc[i - 4]):
            running = 0
            counts[i] = np.nan
        elif condition[i] == 1:
            running = min(running + 1, 13)
            counts[i] = float(running)
        else:
            running = 0
            counts[i] = 0.0
    return pd.Series(counts, index=close.index)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def mex_drv3_001_down_ret_mag_ratio_5d_vs_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (5d/21d down-magnitude ratio): acceleration of mag decel."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    ratio = _safe_div(abs_dn.rolling(_TD_WEEK, min_periods=1).mean(),
                      abs_dn.rolling(_TD_MON, min_periods=1).mean())
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_002_roc_5d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day ROC: acceleration of momentum recovery from lows."""
    roc5 = _roc(close, _TD_WEEK)
    vel = roc5.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_003_roc_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day ROC: jerk of medium-term momentum."""
    roc21 = _roc(close, _TD_MON)
    vel = roc21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_004_roc_5d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 5-day ROC over 21 days: acceleration of ROC trend."""
    roc5 = _roc(close, _TD_WEEK)
    slp = _linslope(roc5, _TD_MON)
    return slp.diff(_TD_WEEK)


def mex_drv3_005_kaufman_er_10d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of Kaufman ER (10d): acceleration of efficiency ratio change."""
    er10 = _kaufman_er(close, 10)
    vel = er10.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_006_kaufman_er_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of Kaufman ER (21d)."""
    er21 = _kaufman_er(close, _TD_MON)
    vel = er21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_007_td_setup_count_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of TD buy-setup count: jerk in exhaustion count accumulation."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    vel = counts.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_008_td_buy_condition_rate_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (5-day diff of TD buy-condition rate)."""
    cond = (close < close.shift(4)).astype(float)
    rate21 = _rolling_mean(cond, _TD_MON)
    vel = rate21.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def mex_drv3_009_price_velocity_ratio_5d_vs_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of velocity ratio (5d/21d log-velocity)."""
    lc = _log_safe(close)
    v5 = lc.diff(_TD_WEEK) / _TD_WEEK
    v21 = lc.diff(_TD_MON) / _TD_MON
    ratio = _safe_div(v5, v21)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_010_atr_ratio_5d_vs_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of (5d/21d ATR ratio)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_011_new_low_increment_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (5d/21d new-low increment ratio)."""
    rl_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    increment = (rl_min - close).clip(lower=0.0)
    ratio = _safe_div(_rolling_mean(increment, _TD_WEEK),
                      _rolling_mean(increment, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_012_down_vol_ratio_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (5d/21d down-volume ratio)."""
    r = _log_ret(close)
    dn_vol = volume.where(r < 0, np.nan)
    ratio = _safe_div(dn_vol.rolling(_TD_WEEK, min_periods=1).mean(),
                      dn_vol.rolling(_TD_MON, min_periods=1).mean())
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_013_roc_5d_zscore_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of 5-day ROC: acceleration of zscore recovery."""
    roc5 = _roc(close, _TD_WEEK)
    m = _rolling_mean(roc5, _TD_QTR)
    s = _rolling_std(roc5, _TD_QTR)
    z = _safe_div(roc5 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_014_kaufman_er_10d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of Kaufman ER (10d) over 21 days."""
    er10 = _kaufman_er(close, 10)
    slp = _linslope(er10, _TD_MON)
    return slp.diff(_TD_WEEK)


def mex_drv3_015_down_ret_mag_slope_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of OLS slope of down-magnitude over 21 days."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    slp = _linslope(abs_dn, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_016_macd_slope_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of OLS slope of MACD over 21 days."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    macd = ema12 - ema26
    slp = _linslope(macd, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_017_drawdown_speed_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day drawdown speed (3rd-order drawdown acceleration)."""
    max252 = _rolling_max(close, _TD_YEAR)
    dd = _safe_div(close - max252, max252.replace(0, np.nan))
    spd = dd.diff(_TD_WEEK) / _TD_WEEK
    vel = spd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_018_cum_loss_5d_vs_prior_5d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d/prior-5d cumulative-loss ratio (jerk of loss pace)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    sum5 = _rolling_sum(dn, _TD_WEEK)
    ratio = _safe_div(sum5, sum5.shift(_TD_WEEK))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_019_roc_21d_vs_63d_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d ROC / 63d ROC) ratio: acceleration of cross-period momentum shift."""
    roc21 = _roc(close, _TD_MON)
    roc63 = _roc(close, _TD_QTR)
    ratio = _safe_div(roc21, roc63.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_020_bear_body_ratio_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of (5d/21d bear body size ratio)."""
    r = _log_ret(close)
    body = (close - open).abs()
    dn_body = body.where(r < 0, np.nan)
    ratio = _safe_div(dn_body.rolling(_TD_WEEK, min_periods=1).mean(),
                      dn_body.rolling(_TD_MON, min_periods=1).mean())
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_021_td_setup_count_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of TD buy-setup count over 21 days."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    slp = _linslope(counts, _TD_MON)
    return slp.diff(_TD_WEEK)


def mex_drv3_022_kaufman_er_21d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of Kaufman ER (21d) over 63 days."""
    er21 = _kaufman_er(close, _TD_MON)
    slp = _linslope(er21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def mex_drv3_023_close_position_slope_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of OLS slope of close-position-in-range over 21 days."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    slp = _linslope(pos, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_024_down_day_frac_decay_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (5d/21d down-day fraction ratio)."""
    r = _log_ret(close)
    is_dn = (r < 0).astype(float)
    ratio = _safe_div(_rolling_mean(is_dn, _TD_WEEK), _rolling_mean(is_dn, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mex_drv3_025_roc_5d_range_position_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5d ROC position within 63d min-max range): recovery from bottom signal."""
    roc5 = _roc(close, _TD_WEEK)
    rmin = _rolling_min(roc5, _TD_QTR)
    rmax = _rolling_max(roc5, _TD_QTR)
    pos = _safe_div(roc5 - rmin, (rmax - rmin).replace(0, np.nan))
    return pos.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_EXHAUSTION_REGISTRY_3RD_DERIVATIVES = {
    "mex_drv3_001_down_ret_mag_ratio_5d_vs_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_001_down_ret_mag_ratio_5d_vs_21d_5d_diff_5d_diff},
    "mex_drv3_002_roc_5d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_002_roc_5d_5d_diff_5d_diff},
    "mex_drv3_003_roc_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_003_roc_21d_5d_diff_5d_diff},
    "mex_drv3_004_roc_5d_slope_21d_5d_diff": {"inputs": ["close"], "func": mex_drv3_004_roc_5d_slope_21d_5d_diff},
    "mex_drv3_005_kaufman_er_10d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_005_kaufman_er_10d_5d_diff_5d_diff},
    "mex_drv3_006_kaufman_er_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_006_kaufman_er_21d_5d_diff_5d_diff},
    "mex_drv3_007_td_setup_count_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_007_td_setup_count_5d_diff_5d_diff},
    "mex_drv3_008_td_buy_condition_rate_5d_diff_slope_21d": {"inputs": ["close"], "func": mex_drv3_008_td_buy_condition_rate_5d_diff_slope_21d},
    "mex_drv3_009_price_velocity_ratio_5d_vs_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_009_price_velocity_ratio_5d_vs_21d_5d_diff_5d_diff},
    "mex_drv3_010_atr_ratio_5d_vs_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": mex_drv3_010_atr_ratio_5d_vs_21d_5d_diff_5d_diff},
    "mex_drv3_011_new_low_increment_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_011_new_low_increment_ratio_5d_diff_5d_diff},
    "mex_drv3_012_down_vol_ratio_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mex_drv3_012_down_vol_ratio_5d_diff_5d_diff},
    "mex_drv3_013_roc_5d_zscore_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_013_roc_5d_zscore_63d_5d_diff_5d_diff},
    "mex_drv3_014_kaufman_er_10d_slope_21d_5d_diff": {"inputs": ["close"], "func": mex_drv3_014_kaufman_er_10d_slope_21d_5d_diff},
    "mex_drv3_015_down_ret_mag_slope_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_015_down_ret_mag_slope_21d_5d_diff_5d_diff},
    "mex_drv3_016_macd_slope_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_016_macd_slope_21d_5d_diff_5d_diff},
    "mex_drv3_017_drawdown_speed_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_017_drawdown_speed_5d_diff_5d_diff},
    "mex_drv3_018_cum_loss_5d_vs_prior_5d_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_018_cum_loss_5d_vs_prior_5d_5d_diff_5d_diff},
    "mex_drv3_019_roc_21d_vs_63d_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_019_roc_21d_vs_63d_ratio_5d_diff_5d_diff},
    "mex_drv3_020_bear_body_ratio_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": mex_drv3_020_bear_body_ratio_5d_diff_5d_diff},
    "mex_drv3_021_td_setup_count_slope_21d_5d_diff": {"inputs": ["close"], "func": mex_drv3_021_td_setup_count_slope_21d_5d_diff},
    "mex_drv3_022_kaufman_er_21d_slope_63d_5d_diff": {"inputs": ["close"], "func": mex_drv3_022_kaufman_er_21d_slope_63d_5d_diff},
    "mex_drv3_023_close_position_slope_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": mex_drv3_023_close_position_slope_5d_diff_5d_diff},
    "mex_drv3_024_down_day_frac_decay_5d_diff_5d_diff": {"inputs": ["close"], "func": mex_drv3_024_down_day_frac_decay_5d_diff_5d_diff},
    "mex_drv3_025_roc_5d_range_position_63d_5d_diff": {"inputs": ["close"], "func": mex_drv3_025_roc_5d_range_position_63d_5d_diff},
}
