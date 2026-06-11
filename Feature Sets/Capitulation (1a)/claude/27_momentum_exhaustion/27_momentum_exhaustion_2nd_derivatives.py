"""
27_momentum_exhaustion — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base momentum-exhaustion features — velocity of exhaustion signals
Includes derivatives of ROC oscillator, Kaufman ER, TD/DeMark sequential, and legacy features.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def mex_drv2_001_down_ret_mag_ratio_5d_vs_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5d/21d down-magnitude ratio): velocity of magnitude deceleration."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    ratio = _safe_div(abs_dn.rolling(_TD_WEEK, min_periods=1).mean(),
                      abs_dn.rolling(_TD_MON, min_periods=1).mean())
    return ratio.diff(_TD_WEEK)


def mex_drv2_002_down_ret_mag_ratio_21d_vs_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (21d/63d down-magnitude ratio)."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    ratio = _safe_div(abs_dn.rolling(_TD_MON, min_periods=1).mean(),
                      abs_dn.rolling(_TD_QTR, min_periods=1).mean())
    return ratio.diff(_TD_MON)


def mex_drv2_003_down_ret_mag_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of down-magnitude over 21 days."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    slp = _linslope(abs_dn, _TD_MON)
    return slp.diff(_TD_WEEK)


def mex_drv2_004_cum_loss_5d_vs_prior_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5d cumulative-loss ratio to prior 5d)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    sum5 = _rolling_sum(dn, _TD_WEEK)
    ratio = _safe_div(sum5, sum5.shift(_TD_WEEK))
    return ratio.diff(_TD_WEEK)


def mex_drv2_005_roc_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day ROC: velocity of momentum recovery from lows."""
    roc5 = _roc(close, _TD_WEEK)
    return roc5.diff(_TD_WEEK)


def mex_drv2_006_roc_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day ROC: velocity of medium-term momentum change."""
    roc21 = _roc(close, _TD_MON)
    return roc21.diff(_TD_WEEK)


def mex_drv2_007_roc_5d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day ROC over 21 days: sustained ROC deceleration signal."""
    roc5 = _roc(close, _TD_WEEK)
    return _linslope(roc5, _TD_MON)


def mex_drv2_008_roc_21d_vs_63d_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21d ROC / 63d ROC) ratio."""
    roc21 = _roc(close, _TD_MON)
    roc63 = _roc(close, _TD_QTR)
    ratio = _safe_div(roc21, roc63.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def mex_drv2_009_kaufman_er_10d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Kaufman ER (10d): rising ER = momentum re-establishing direction."""
    er10 = _kaufman_er(close, 10)
    return er10.diff(_TD_WEEK)


def mex_drv2_010_kaufman_er_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Kaufman ER (21d)."""
    er21 = _kaufman_er(close, _TD_MON)
    return er21.diff(_TD_WEEK)


def mex_drv2_011_kaufman_er_10d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of Kaufman ER (10d) over 21 days."""
    er10 = _kaufman_er(close, 10)
    return _linslope(er10, _TD_MON)


def mex_drv2_012_td_setup_count_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of TD buy-setup count: rapidly rising count = potential exhaustion building."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    return counts.diff(_TD_WEEK)


def mex_drv2_013_td_buy_condition_rate_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of rolling 21-day TD buy-condition rate."""
    cond = (close < close.shift(4)).astype(float)
    rate21 = _rolling_mean(cond, _TD_MON)
    return rate21.diff(_TD_WEEK)


def mex_drv2_014_td_setup_count_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of TD buy-setup count over 21 days."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    return _linslope(counts, _TD_MON)


def mex_drv2_015_price_velocity_ratio_5d_vs_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5d/21d log-velocity ratio)."""
    lc = _log_safe(close)
    v5 = lc.diff(_TD_WEEK) / _TD_WEEK
    v21 = lc.diff(_TD_MON) / _TD_MON
    ratio = _safe_div(v5, v21)
    return ratio.diff(_TD_WEEK)


def mex_drv2_016_atr_ratio_5d_vs_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5d ATR / 21d ATR) ratio."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_MON))
    return ratio.diff(_TD_WEEK)


def mex_drv2_017_new_low_increment_5d_vs_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5d/21d new-low increment ratio)."""
    rl_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    increment = (rl_min - close).clip(lower=0.0)
    ratio = _safe_div(_rolling_mean(increment, _TD_WEEK),
                      _rolling_mean(increment, _TD_MON))
    return ratio.diff(_TD_WEEK)


def mex_drv2_018_down_vol_ratio_5d_vs_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5d/21d down-day volume ratio)."""
    r = _log_ret(close)
    dn_vol = volume.where(r < 0, np.nan)
    ratio = _safe_div(dn_vol.rolling(_TD_WEEK, min_periods=1).mean(),
                      dn_vol.rolling(_TD_MON, min_periods=1).mean())
    return ratio.diff(_TD_WEEK)


def mex_drv2_019_macd_signal_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of MACD over 21 days."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    macd = ema12 - ema26
    slp = _linslope(macd, _TD_MON)
    return slp.diff(_TD_WEEK)


def mex_drv2_020_drawdown_speed_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day drawdown speed (acceleration of drawdown pace)."""
    max252 = _rolling_max(close, _TD_YEAR)
    dd = _safe_div(close - max252, max252.replace(0, np.nan))
    spd = dd.diff(_TD_WEEK) / _TD_WEEK
    return spd.diff(_TD_WEEK)


def mex_drv2_021_roc_5d_zscore_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of z-score of 5-day ROC within 63-day distribution."""
    roc5 = _roc(close, _TD_WEEK)
    m = _rolling_mean(roc5, _TD_QTR)
    s = _rolling_std(roc5, _TD_QTR)
    z = _safe_div(roc5 - m, s)
    return z.diff(_TD_WEEK)


def mex_drv2_022_kaufman_er_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Kaufman ER (63d): slow ER change reveals regime shift."""
    er63 = _kaufman_er(close, _TD_QTR)
    return er63.diff(_TD_WEEK)


def mex_drv2_023_bear_body_ratio_5d_vs_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of (5d/21d bear body size ratio)."""
    r = _log_ret(close)
    body = (close - open).abs()
    dn_body = body.where(r < 0, np.nan)
    ratio = _safe_div(dn_body.rolling(_TD_WEEK, min_periods=1).mean(),
                      dn_body.rolling(_TD_MON, min_periods=1).mean())
    return ratio.diff(_TD_WEEK)


def mex_drv2_024_down_day_fraction_decay_5d_vs_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5d/21d down-day fraction decay ratio)."""
    r = _log_ret(close)
    is_dn = (r < 0).astype(float)
    ratio = _safe_div(_rolling_mean(is_dn, _TD_WEEK), _rolling_mean(is_dn, _TD_MON))
    return ratio.diff(_TD_WEEK)


def mex_drv2_025_close_position_in_range_slope_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of close-position-in-range over 21 days."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    slp = _linslope(pos, _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_EXHAUSTION_REGISTRY_2ND_DERIVATIVES = {
    "mex_drv2_001_down_ret_mag_ratio_5d_vs_21d_5d_diff": {"inputs": ["close"], "func": mex_drv2_001_down_ret_mag_ratio_5d_vs_21d_5d_diff},
    "mex_drv2_002_down_ret_mag_ratio_21d_vs_63d_21d_diff": {"inputs": ["close"], "func": mex_drv2_002_down_ret_mag_ratio_21d_vs_63d_21d_diff},
    "mex_drv2_003_down_ret_mag_slope_21d_5d_diff": {"inputs": ["close"], "func": mex_drv2_003_down_ret_mag_slope_21d_5d_diff},
    "mex_drv2_004_cum_loss_5d_vs_prior_5d_5d_diff": {"inputs": ["close"], "func": mex_drv2_004_cum_loss_5d_vs_prior_5d_5d_diff},
    "mex_drv2_005_roc_5d_5d_diff": {"inputs": ["close"], "func": mex_drv2_005_roc_5d_5d_diff},
    "mex_drv2_006_roc_21d_5d_diff": {"inputs": ["close"], "func": mex_drv2_006_roc_21d_5d_diff},
    "mex_drv2_007_roc_5d_slope_21d": {"inputs": ["close"], "func": mex_drv2_007_roc_5d_slope_21d},
    "mex_drv2_008_roc_21d_vs_63d_ratio_5d_diff": {"inputs": ["close"], "func": mex_drv2_008_roc_21d_vs_63d_ratio_5d_diff},
    "mex_drv2_009_kaufman_er_10d_5d_diff": {"inputs": ["close"], "func": mex_drv2_009_kaufman_er_10d_5d_diff},
    "mex_drv2_010_kaufman_er_21d_5d_diff": {"inputs": ["close"], "func": mex_drv2_010_kaufman_er_21d_5d_diff},
    "mex_drv2_011_kaufman_er_10d_slope_21d": {"inputs": ["close"], "func": mex_drv2_011_kaufman_er_10d_slope_21d},
    "mex_drv2_012_td_setup_count_5d_diff": {"inputs": ["close"], "func": mex_drv2_012_td_setup_count_5d_diff},
    "mex_drv2_013_td_buy_condition_rate_5d_diff": {"inputs": ["close"], "func": mex_drv2_013_td_buy_condition_rate_5d_diff},
    "mex_drv2_014_td_setup_count_slope_21d": {"inputs": ["close"], "func": mex_drv2_014_td_setup_count_slope_21d},
    "mex_drv2_015_price_velocity_ratio_5d_vs_21d_5d_diff": {"inputs": ["close"], "func": mex_drv2_015_price_velocity_ratio_5d_vs_21d_5d_diff},
    "mex_drv2_016_atr_ratio_5d_vs_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": mex_drv2_016_atr_ratio_5d_vs_21d_5d_diff},
    "mex_drv2_017_new_low_increment_5d_vs_21d_5d_diff": {"inputs": ["close"], "func": mex_drv2_017_new_low_increment_5d_vs_21d_5d_diff},
    "mex_drv2_018_down_vol_ratio_5d_vs_21d_5d_diff": {"inputs": ["close", "volume"], "func": mex_drv2_018_down_vol_ratio_5d_vs_21d_5d_diff},
    "mex_drv2_019_macd_signal_slope_21d_5d_diff": {"inputs": ["close"], "func": mex_drv2_019_macd_signal_slope_21d_5d_diff},
    "mex_drv2_020_drawdown_speed_5d_5d_diff": {"inputs": ["close"], "func": mex_drv2_020_drawdown_speed_5d_5d_diff},
    "mex_drv2_021_roc_5d_zscore_63d_5d_diff": {"inputs": ["close"], "func": mex_drv2_021_roc_5d_zscore_63d_5d_diff},
    "mex_drv2_022_kaufman_er_63d_5d_diff": {"inputs": ["close"], "func": mex_drv2_022_kaufman_er_63d_5d_diff},
    "mex_drv2_023_bear_body_ratio_5d_vs_21d_5d_diff": {"inputs": ["close", "open"], "func": mex_drv2_023_bear_body_ratio_5d_vs_21d_5d_diff},
    "mex_drv2_024_down_day_fraction_decay_5d_vs_21d_5d_diff": {"inputs": ["close"], "func": mex_drv2_024_down_day_fraction_decay_5d_vs_21d_5d_diff},
    "mex_drv2_025_close_position_in_range_slope_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": mex_drv2_025_close_position_in_range_slope_21d_5d_diff},
}
