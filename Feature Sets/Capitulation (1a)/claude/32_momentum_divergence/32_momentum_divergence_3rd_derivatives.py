"""
32_momentum_divergence — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative divergence features — acceleration of velocity
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — jerk/acceleration of divergence velocity signals
All features are backward-looking only; no forward information.

Coverage:
  drv3_001-008  Acceleration of regular divergence velocity features
  drv3_009-015  Acceleration of hidden bullish divergence velocity features
  drv3_016-020  Acceleration of OBV divergence velocity features
  drv3_021-025  Acceleration of composite strength grading velocity
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


def _rsi(close: pd.Series, period: int) -> pd.Series:
    """Wilder RSI, returns 0-100 series."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period // 2, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period // 2, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - _safe_div(pd.Series(100.0, index=close.index), 1.0 + rs)


def _macd_line(close: pd.Series, fast: int = 12, slow: int = 26) -> pd.Series:
    return _ewm_mean(close, fast) - _ewm_mean(close, slow)


def _roc(close: pd.Series, period: int) -> pd.Series:
    return _safe_div(close - close.shift(period), close.shift(period))


def _stoch_k(close: pd.Series, high: pd.Series, low: pd.Series, period: int = 14) -> pd.Series:
    lo = _rolling_min(low, period)
    hi = _rolling_max(high, period)
    return _safe_div(close - lo, hi - lo) * 100.0


def _price_new_low(close: pd.Series, w: int) -> pd.Series:
    prior_min = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (close < prior_min).astype(float)


def _price_higher_low(close: pd.Series, w: int) -> pd.Series:
    prior_min = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (close > prior_min).astype(float)


def _osc_lower_low(osc: pd.Series, w: int) -> pd.Series:
    prior_min = osc.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (osc < prior_min).astype(float)


def _pct_rank(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


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


def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    direction = np.sign(close.diff(1)).fillna(0.0)
    return (direction * volume).cumsum()


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = second diff / slope of slope applied to a 2nd-derivative concept.

# --- Group 1 (drv3_001-008): Acceleration of regular divergence velocity ---

def mdv_drv3_001_rsi14_pctrank_spread_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI(14)-price pct-rank spread (acceleration of spread velocity)."""
    rsi = _rsi(close, 14)
    spread = _pct_rank(rsi, _TD_QTR) - _pct_rank(close, _TD_QTR)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_002_rsi14_pctrank_spread_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in RSI(14)-price pct-rank spread (252d)."""
    rsi = _rsi(close, 14)
    spread = _pct_rank(rsi, _TD_YEAR) - _pct_rank(close, _TD_YEAR)
    vel21 = spread.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def mdv_drv3_003_macd_pctrank_spread_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of MACD-price pct-rank spread (63d)."""
    macd = _macd_line(close)
    spread = _pct_rank(macd, _TD_QTR) - _pct_rank(close, _TD_QTR)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_004_rsi14_gap_at_low_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI gap at price-new-low (acceleration of gap change)."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_floor = rsi.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    gap = (rsi - rsi_floor).clip(lower=0.0) * price_nl
    vel = gap.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_005_macd_gap_at_low_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of MACD gap at price-new-low bars."""
    price_nl = _price_new_low(close, _TD_QTR)
    macd = _macd_line(close)
    macd_floor = macd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    gap = (macd - macd_floor) * price_nl
    vel = gap.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_006_rsi14_divg_magnitude_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI(14) drawdown divergence magnitude (63d)."""
    rsi = _rsi(close, 14)
    price_hi = _rolling_max(close, _TD_QTR)
    rsi_hi = _rolling_max(rsi, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    rsi_dd = _safe_div(rsi_hi - rsi, rsi_hi.clip(lower=_EPS))
    mag = price_dd - rsi_dd
    vel = mag.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_007_rsi14_pctrank_spread_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of RSI(14)-price pct-rank spread (21d slope)."""
    rsi = _rsi(close, 14)
    spread = _pct_rank(rsi, _TD_QTR) - _pct_rank(close, _TD_QTR)
    slp = _linslope(spread, _TD_MON)
    return slp.diff(_TD_WEEK)


def mdv_drv3_008_composite_divg_score_63d_5d_diff_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of composite divergence score."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    roc = _roc(close, 10)
    sk = _stoch_k(close, high, low, 14)
    price_nl = _price_new_low(close, _TD_QTR)

    def _flag(ind):
        ind_nl = (ind < ind.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
        return price_nl * (1.0 - ind_nl)

    score = _flag(rsi) + _flag(macd) + _flag(roc) + _flag(sk)
    vel = score.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# --- Group 2 (drv3_009-015): Acceleration of hidden bullish divergence velocity ---

def mdv_drv3_009_rsi14_hidden_bull_flag_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI(14) hidden bullish divergence flag (acceleration)."""
    rsi = _rsi(close, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(rsi, _TD_QTR)
    flag = price_hl * osc_ll
    vel = flag.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_010_macd_hidden_bull_flag_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of MACD hidden bullish divergence flag (acceleration)."""
    macd = _macd_line(close)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(macd, _TD_QTR)
    flag = price_hl * osc_ll
    vel = flag.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_011_stoch_hidden_bull_flag_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Stoch hidden bullish divergence flag (acceleration)."""
    sk = _stoch_k(close, high, low, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(sk, _TD_QTR)
    flag = price_hl * osc_ll
    vel = flag.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_012_composite_hidden_score_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of composite hidden bullish divergence score (RSI+MACD+Stoch, 63d)."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    score = (
        price_hl * _osc_lower_low(rsi, _TD_QTR)
        + price_hl * _osc_lower_low(macd, _TD_QTR)
        + price_hl * _osc_lower_low(sk, _TD_QTR)
    )
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_013_rsi14_hidden_bull_magnitude_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in RSI(14) hidden bullish divergence magnitude."""
    rsi = _rsi(close, 14)
    price_floor = _rolling_min(close, _TD_QTR)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    price_lift = _safe_div(close - price_floor, price_floor.clip(lower=_EPS))
    rsi_drop = _safe_div(rsi_floor - rsi, rsi_floor.clip(lower=_EPS))
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(rsi, _TD_QTR)
    mag = (price_lift + rsi_drop) * price_hl * osc_ll
    vel21 = mag.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def mdv_drv3_014_rsi14_hidden_bull_count_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in RSI(14) hidden bull count over 252 days."""
    rsi = _rsi(close, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(rsi, _TD_QTR)
    flag = price_hl * osc_ll
    count = _rolling_sum(flag, _TD_YEAR)
    vel21 = count.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def mdv_drv3_015_composite_hidden_score_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of composite hidden bullish divergence score (21d slope)."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    score = (
        price_hl * _osc_lower_low(rsi, _TD_QTR)
        + price_hl * _osc_lower_low(macd, _TD_QTR)
        + price_hl * _osc_lower_low(sk, _TD_QTR)
    )
    slp = _linslope(score, _TD_MON)
    return slp.diff(_TD_WEEK)


# --- Group 3 (drv3_016-020): Acceleration of OBV divergence velocity ---

def mdv_drv3_016_obv_regular_divg_flag_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of OBV regular divergence flag (acceleration)."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_QTR)
    obv_nl = _osc_lower_low(obv, _TD_QTR)
    flag = price_nl * (1.0 - obv_nl)
    vel = flag.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_017_obv_pctrank_spread_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of OBV-price pct-rank spread (63d)."""
    obv = _obv(close, volume)
    spread = _pct_rank(obv, _TD_QTR) - _pct_rank(close, _TD_QTR)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_018_obv_hidden_bull_flag_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of OBV hidden bullish divergence flag (acceleration)."""
    obv = _obv(close, volume)
    price_hl = _price_higher_low(close, _TD_QTR)
    obv_ll = _osc_lower_low(obv, _TD_QTR)
    flag = price_hl * obv_ll
    vel = flag.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_019_obv_pctrank_spread_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in OBV-price pct-rank spread (252d)."""
    obv = _obv(close, volume)
    spread = _pct_rank(obv, _TD_YEAR) - _pct_rank(close, _TD_YEAR)
    vel21 = spread.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def mdv_drv3_020_obv_divg_count_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in OBV divergence count (252d window)."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_QTR)
    obv_nl = _osc_lower_low(obv, _TD_QTR)
    flag = price_nl * (1.0 - obv_nl)
    count = _rolling_sum(flag, _TD_YEAR)
    vel21 = count.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# --- Group 4 (drv3_021-025): Acceleration of composite strength grading velocity ---

def mdv_drv3_021_multi_osc_agreement_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of multi-oscillator divergence agreement score (acceleration)."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    roc = _roc(close, 10)
    price_nl = _price_new_low(close, _TD_QTR)
    score = (
        price_nl * (1.0 - _osc_lower_low(rsi, _TD_QTR))
        + price_nl * (1.0 - _osc_lower_low(macd, _TD_QTR))
        + price_nl * (1.0 - _osc_lower_low(sk, _TD_QTR))
        + price_nl * (1.0 - _osc_lower_low(roc, _TD_QTR))
    )
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_022_rsi14_hidden_bull_score_252d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (63d) of RSI(14) hidden bull count over 252 days."""
    rsi = _rsi(close, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(rsi, _TD_QTR)
    flag = price_hl * osc_ll
    count = _rolling_sum(flag, _TD_YEAR)
    slp = _linslope(count, _TD_QTR)
    return slp.diff(_TD_WEEK)


def mdv_drv3_023_obv_rsi_joint_count_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in OBV+RSI joint divergence count (252d)."""
    obv = _obv(close, volume)
    rsi = _rsi(close, 14)
    price_nl = _price_new_low(close, _TD_QTR)
    obv_flag = price_nl * (1.0 - _osc_lower_low(obv, _TD_QTR))
    rsi_flag = price_nl * (1.0 - _osc_lower_low(rsi, _TD_QTR))
    joint = obv_flag * rsi_flag
    count = _rolling_sum(joint, _TD_YEAR)
    vel21 = count.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def mdv_drv3_024_composite_strength_grade_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of composite divergence strength grade (63d agreement * gap)."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    roc = _roc(close, 10)
    price_nl = _price_new_low(close, _TD_QTR)
    agreement = (
        price_nl * (1.0 - _osc_lower_low(rsi, _TD_QTR))
        + price_nl * (1.0 - _osc_lower_low(macd, _TD_QTR))
        + price_nl * (1.0 - _osc_lower_low(sk, _TD_QTR))
        + price_nl * (1.0 - _osc_lower_low(roc, _TD_QTR))
    )
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    rsi_gap = (rsi - rsi_floor).clip(lower=0.0) * price_nl
    grade = agreement * rsi_gap.clip(lower=0.0)
    vel = grade.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdv_drv3_025_composite_hidden_plus_obv_acceleration(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of composite hidden+OBV divergence total count (252d)."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    obv = _obv(close, volume)
    price_hl = _price_higher_low(close, _TD_QTR)
    price_nl = _price_new_low(close, _TD_QTR)
    hidden_score = (
        price_hl * _osc_lower_low(rsi, _TD_QTR)
        + price_hl * _osc_lower_low(macd, _TD_QTR)
        + price_hl * _osc_lower_low(sk, _TD_QTR)
    )
    obv_divg = price_nl * (1.0 - _osc_lower_low(obv, _TD_QTR))
    combined = hidden_score + obv_divg
    count = _rolling_sum(combined, _TD_YEAR)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DIVERGENCE_REGISTRY_3RD_DERIVATIVES = {
    "mdv_drv3_001_rsi14_pctrank_spread_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_001_rsi14_pctrank_spread_63d_5d_diff_5d_diff},
    "mdv_drv3_002_rsi14_pctrank_spread_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_002_rsi14_pctrank_spread_252d_21d_diff_5d_diff},
    "mdv_drv3_003_macd_pctrank_spread_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_003_macd_pctrank_spread_63d_5d_diff_5d_diff},
    "mdv_drv3_004_rsi14_gap_at_low_5d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_004_rsi14_gap_at_low_5d_diff_5d_diff},
    "mdv_drv3_005_macd_gap_at_low_5d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_005_macd_gap_at_low_5d_diff_5d_diff},
    "mdv_drv3_006_rsi14_divg_magnitude_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_006_rsi14_divg_magnitude_63d_5d_diff_5d_diff},
    "mdv_drv3_007_rsi14_pctrank_spread_slope_5d_diff": {"inputs": ["close"], "func": mdv_drv3_007_rsi14_pctrank_spread_slope_5d_diff},
    "mdv_drv3_008_composite_divg_score_63d_5d_diff_slope": {"inputs": ["close", "high", "low"], "func": mdv_drv3_008_composite_divg_score_63d_5d_diff_slope},
    "mdv_drv3_009_rsi14_hidden_bull_flag_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_009_rsi14_hidden_bull_flag_63d_5d_diff_5d_diff},
    "mdv_drv3_010_macd_hidden_bull_flag_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_010_macd_hidden_bull_flag_63d_5d_diff_5d_diff},
    "mdv_drv3_011_stoch_hidden_bull_flag_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv3_011_stoch_hidden_bull_flag_63d_5d_diff_5d_diff},
    "mdv_drv3_012_composite_hidden_score_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv3_012_composite_hidden_score_63d_5d_diff_5d_diff},
    "mdv_drv3_013_rsi14_hidden_bull_magnitude_21d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_013_rsi14_hidden_bull_magnitude_21d_diff_5d_diff},
    "mdv_drv3_014_rsi14_hidden_bull_count_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": mdv_drv3_014_rsi14_hidden_bull_count_252d_21d_diff_5d_diff},
    "mdv_drv3_015_composite_hidden_score_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv3_015_composite_hidden_score_slope_5d_diff},
    "mdv_drv3_016_obv_regular_divg_flag_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv3_016_obv_regular_divg_flag_63d_5d_diff_5d_diff},
    "mdv_drv3_017_obv_pctrank_spread_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv3_017_obv_pctrank_spread_63d_5d_diff_5d_diff},
    "mdv_drv3_018_obv_hidden_bull_flag_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv3_018_obv_hidden_bull_flag_63d_5d_diff_5d_diff},
    "mdv_drv3_019_obv_pctrank_spread_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv3_019_obv_pctrank_spread_252d_21d_diff_5d_diff},
    "mdv_drv3_020_obv_divg_count_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv3_020_obv_divg_count_252d_21d_diff_5d_diff},
    "mdv_drv3_021_multi_osc_agreement_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv3_021_multi_osc_agreement_63d_5d_diff_5d_diff},
    "mdv_drv3_022_rsi14_hidden_bull_score_252d_slope_5d_diff": {"inputs": ["close"], "func": mdv_drv3_022_rsi14_hidden_bull_score_252d_slope_5d_diff},
    "mdv_drv3_023_obv_rsi_joint_count_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv3_023_obv_rsi_joint_count_21d_diff_5d_diff},
    "mdv_drv3_024_composite_strength_grade_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv3_024_composite_strength_grade_63d_5d_diff_5d_diff},
    "mdv_drv3_025_composite_hidden_plus_obv_acceleration": {"inputs": ["close", "high", "low", "volume"], "func": mdv_drv3_025_composite_hidden_plus_obv_acceleration},
}
