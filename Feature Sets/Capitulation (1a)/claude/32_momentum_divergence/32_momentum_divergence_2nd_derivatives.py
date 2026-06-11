"""
32_momentum_divergence — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base divergence features — velocity of divergence behavior
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — acceleration/velocity of price-momentum mismatch
All features are backward-looking only; no forward information.

Coverage:
  drv2_001-010  Velocity of regular (regular bullish) divergence features
  drv2_011-017  Velocity of hidden bullish divergence features
  drv2_018-022  Velocity of OBV divergence features
  drv2_023-025  Velocity of composite strength grading features
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

# --- Group 1 (drv2_001-010): Velocity of regular bullish divergence features ---

def mdv_drv2_001_rsi14_pctrank_spread_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI(14)-price pct-rank spread over 63-day window (velocity)."""
    rsi = _rsi(close, 14)
    spread = _pct_rank(rsi, _TD_QTR) - _pct_rank(close, _TD_QTR)
    return spread.diff(_TD_WEEK)


def mdv_drv2_002_rsi14_pctrank_spread_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of RSI(14)-price pct-rank spread over 252-day window."""
    rsi = _rsi(close, 14)
    spread = _pct_rank(rsi, _TD_YEAR) - _pct_rank(close, _TD_YEAR)
    return spread.diff(_TD_MON)


def mdv_drv2_003_macd_pctrank_spread_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of MACD-price pct-rank spread over 63-day window."""
    macd = _macd_line(close)
    spread = _pct_rank(macd, _TD_QTR) - _pct_rank(close, _TD_QTR)
    return spread.diff(_TD_WEEK)


def mdv_drv2_004_macd_pctrank_spread_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of MACD-price pct-rank spread over 252-day window."""
    macd = _macd_line(close)
    spread = _pct_rank(macd, _TD_YEAR) - _pct_rank(close, _TD_YEAR)
    return spread.diff(_TD_MON)


def mdv_drv2_005_rsi14_gap_at_low_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI(14) gap above its 63-day min at price-new-low bars."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_floor = rsi.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    gap = (rsi - rsi_floor).clip(lower=0.0) * price_nl
    return gap.diff(_TD_WEEK)


def mdv_drv2_006_macd_gap_at_low_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of MACD gap above its 63-day min at price-new-low bars."""
    price_nl = _price_new_low(close, _TD_QTR)
    macd = _macd_line(close)
    macd_floor = macd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    gap = (macd - macd_floor) * price_nl
    return gap.diff(_TD_WEEK)


def mdv_drv2_007_rsi14_divg_magnitude_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI(14) drawdown divergence magnitude (63-day)."""
    rsi = _rsi(close, 14)
    price_hi = _rolling_max(close, _TD_QTR)
    rsi_hi = _rolling_max(rsi, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    rsi_dd = _safe_div(rsi_hi - rsi, rsi_hi.clip(lower=_EPS))
    mag = price_dd - rsi_dd
    return mag.diff(_TD_WEEK)


def mdv_drv2_008_rsi14_divg_count_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI divergence event count in trailing 63-day window."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_nl = (rsi < rsi.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    flag = price_nl * (1.0 - rsi_nl)
    count = _rolling_sum(flag, _TD_QTR)
    return count.diff(_TD_WEEK)


def mdv_drv2_009_composite_divg_score_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of composite multi-indicator divergence score at 63-day lows."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    roc = _roc(close, 10)
    sk = _stoch_k(close, high, low, 14)
    price_nl = _price_new_low(close, _TD_QTR)

    def _flag(ind):
        ind_nl = (ind < ind.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
        return price_nl * (1.0 - ind_nl)

    score = _flag(rsi) + _flag(macd) + _flag(roc) + _flag(sk)
    return score.diff(_TD_WEEK)


def mdv_drv2_010_rsi14_pctrank_spread_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of RSI(14)-price pct-rank spread over 21-day window."""
    rsi = _rsi(close, 14)
    spread = _pct_rank(rsi, _TD_QTR) - _pct_rank(close, _TD_QTR)
    return _linslope(spread, _TD_MON)


# --- Group 2 (drv2_011-017): Velocity of hidden bullish divergence features ---

def mdv_drv2_011_rsi14_hidden_bull_divg_flag_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI(14) hidden bullish divergence flag (63-day window)."""
    rsi = _rsi(close, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(rsi, _TD_QTR)
    flag = price_hl * osc_ll
    return flag.diff(_TD_WEEK)


def mdv_drv2_012_rsi14_hidden_bull_count_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI(14) hidden bullish divergence count (63-day window)."""
    rsi = _rsi(close, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(rsi, _TD_QTR)
    flag = price_hl * osc_ll
    count = _rolling_sum(flag, _TD_QTR)
    return count.diff(_TD_WEEK)


def mdv_drv2_013_macd_hidden_bull_divg_flag_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of MACD hidden bullish divergence flag (63-day window)."""
    macd = _macd_line(close)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(macd, _TD_QTR)
    flag = price_hl * osc_ll
    return flag.diff(_TD_WEEK)


def mdv_drv2_014_stoch_hidden_bull_divg_flag_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Stoch hidden bullish divergence flag (63-day window)."""
    sk = _stoch_k(close, high, low, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(sk, _TD_QTR)
    flag = price_hl * osc_ll
    return flag.diff(_TD_WEEK)


def mdv_drv2_015_composite_hidden_bull_score_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of composite hidden bullish divergence score (RSI+MACD+Stoch, 63d)."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    score = (
        price_hl * _osc_lower_low(rsi, _TD_QTR)
        + price_hl * _osc_lower_low(macd, _TD_QTR)
        + price_hl * _osc_lower_low(sk, _TD_QTR)
    )
    return score.diff(_TD_WEEK)


def mdv_drv2_016_rsi14_hidden_bull_magnitude_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of RSI(14) hidden bullish divergence magnitude (63d)."""
    rsi = _rsi(close, 14)
    price_floor = _rolling_min(close, _TD_QTR)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    price_lift = _safe_div(close - price_floor, price_floor.clip(lower=_EPS))
    rsi_drop = _safe_div(rsi_floor - rsi, rsi_floor.clip(lower=_EPS))
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(rsi, _TD_QTR)
    mag = (price_lift + rsi_drop) * price_hl * osc_ll
    return mag.diff(_TD_MON)


def mdv_drv2_017_composite_hidden_count_252d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of composite hidden bullish divergence count (252-day window)."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    price_hl_63 = _price_higher_low(close, _TD_QTR)
    score_63 = (
        price_hl_63 * _osc_lower_low(rsi, _TD_QTR)
        + price_hl_63 * _osc_lower_low(macd, _TD_QTR)
        + price_hl_63 * _osc_lower_low(sk, _TD_QTR)
    )
    count = _rolling_sum(score_63, _TD_YEAR)
    return count.diff(_TD_MON)


# --- Group 3 (drv2_018-022): Velocity of OBV divergence features ---

def mdv_drv2_018_obv_regular_divg_flag_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OBV regular bullish divergence flag (63-day window)."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_QTR)
    obv_nl = _osc_lower_low(obv, _TD_QTR)
    flag = price_nl * (1.0 - obv_nl)
    return flag.diff(_TD_WEEK)


def mdv_drv2_019_obv_pctrank_spread_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OBV-price pct-rank spread over 63-day window."""
    obv = _obv(close, volume)
    spread = _pct_rank(obv, _TD_QTR) - _pct_rank(close, _TD_QTR)
    return spread.diff(_TD_WEEK)


def mdv_drv2_020_obv_divg_count_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OBV divergence count in trailing 63 days."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_QTR)
    obv_nl = _osc_lower_low(obv, _TD_QTR)
    flag = price_nl * (1.0 - obv_nl)
    count = _rolling_sum(flag, _TD_QTR)
    return count.diff(_TD_WEEK)


def mdv_drv2_021_obv_hidden_bull_flag_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OBV hidden bullish divergence flag (63-day window)."""
    obv = _obv(close, volume)
    price_hl = _price_higher_low(close, _TD_QTR)
    obv_ll = _osc_lower_low(obv, _TD_QTR)
    flag = price_hl * obv_ll
    return flag.diff(_TD_WEEK)


def mdv_drv2_022_obv_pctrank_spread_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of OBV-price pct-rank spread over 252-day window."""
    obv = _obv(close, volume)
    spread = _pct_rank(obv, _TD_YEAR) - _pct_rank(close, _TD_YEAR)
    return spread.diff(_TD_MON)


# --- Group 4 (drv2_023-025): Velocity of composite strength grading ---

def mdv_drv2_023_multi_osc_agreement_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of multi-oscillator divergence agreement score (63-day window)."""
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
    return score.diff(_TD_WEEK)


def mdv_drv2_024_divg_gap_zscore_rsi_5d_slope(close: pd.Series) -> pd.Series:
    """OLS slope (21d) of RSI divergence gap z-score (63d)."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    gap = (rsi - rsi_floor).clip(lower=0.0) * price_nl
    m = _rolling_mean(gap, _TD_QTR)
    s = _rolling_std(gap, _TD_QTR)
    z = _safe_div(gap - m, s)
    return _linslope(z, _TD_MON)


def mdv_drv2_025_obv_rsi_joint_divg_count_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of OBV+RSI joint divergence count over 252-day window."""
    obv = _obv(close, volume)
    rsi = _rsi(close, 14)
    price_nl = _price_new_low(close, _TD_QTR)
    obv_flag = price_nl * (1.0 - _osc_lower_low(obv, _TD_QTR))
    rsi_flag = price_nl * (1.0 - _osc_lower_low(rsi, _TD_QTR))
    joint = obv_flag * rsi_flag
    count = _rolling_sum(joint, _TD_YEAR)
    return count.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DIVERGENCE_REGISTRY_2ND_DERIVATIVES = {
    "mdv_drv2_001_rsi14_pctrank_spread_63d_5d_diff": {"inputs": ["close"], "func": mdv_drv2_001_rsi14_pctrank_spread_63d_5d_diff},
    "mdv_drv2_002_rsi14_pctrank_spread_252d_21d_diff": {"inputs": ["close"], "func": mdv_drv2_002_rsi14_pctrank_spread_252d_21d_diff},
    "mdv_drv2_003_macd_pctrank_spread_63d_5d_diff": {"inputs": ["close"], "func": mdv_drv2_003_macd_pctrank_spread_63d_5d_diff},
    "mdv_drv2_004_macd_pctrank_spread_252d_21d_diff": {"inputs": ["close"], "func": mdv_drv2_004_macd_pctrank_spread_252d_21d_diff},
    "mdv_drv2_005_rsi14_gap_at_low_5d_diff": {"inputs": ["close"], "func": mdv_drv2_005_rsi14_gap_at_low_5d_diff},
    "mdv_drv2_006_macd_gap_at_low_5d_diff": {"inputs": ["close"], "func": mdv_drv2_006_macd_gap_at_low_5d_diff},
    "mdv_drv2_007_rsi14_divg_magnitude_63d_5d_diff": {"inputs": ["close"], "func": mdv_drv2_007_rsi14_divg_magnitude_63d_5d_diff},
    "mdv_drv2_008_rsi14_divg_count_63d_5d_diff": {"inputs": ["close"], "func": mdv_drv2_008_rsi14_divg_count_63d_5d_diff},
    "mdv_drv2_009_composite_divg_score_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv2_009_composite_divg_score_63d_5d_diff},
    "mdv_drv2_010_rsi14_pctrank_spread_slope_21d": {"inputs": ["close"], "func": mdv_drv2_010_rsi14_pctrank_spread_slope_21d},
    "mdv_drv2_011_rsi14_hidden_bull_divg_flag_63d_5d_diff": {"inputs": ["close"], "func": mdv_drv2_011_rsi14_hidden_bull_divg_flag_63d_5d_diff},
    "mdv_drv2_012_rsi14_hidden_bull_count_63d_5d_diff": {"inputs": ["close"], "func": mdv_drv2_012_rsi14_hidden_bull_count_63d_5d_diff},
    "mdv_drv2_013_macd_hidden_bull_divg_flag_63d_5d_diff": {"inputs": ["close"], "func": mdv_drv2_013_macd_hidden_bull_divg_flag_63d_5d_diff},
    "mdv_drv2_014_stoch_hidden_bull_divg_flag_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv2_014_stoch_hidden_bull_divg_flag_63d_5d_diff},
    "mdv_drv2_015_composite_hidden_bull_score_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv2_015_composite_hidden_bull_score_63d_5d_diff},
    "mdv_drv2_016_rsi14_hidden_bull_magnitude_63d_21d_diff": {"inputs": ["close"], "func": mdv_drv2_016_rsi14_hidden_bull_magnitude_63d_21d_diff},
    "mdv_drv2_017_composite_hidden_count_252d_21d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv2_017_composite_hidden_count_252d_21d_diff},
    "mdv_drv2_018_obv_regular_divg_flag_63d_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv2_018_obv_regular_divg_flag_63d_5d_diff},
    "mdv_drv2_019_obv_pctrank_spread_63d_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv2_019_obv_pctrank_spread_63d_5d_diff},
    "mdv_drv2_020_obv_divg_count_63d_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv2_020_obv_divg_count_63d_5d_diff},
    "mdv_drv2_021_obv_hidden_bull_flag_63d_5d_diff": {"inputs": ["close", "volume"], "func": mdv_drv2_021_obv_hidden_bull_flag_63d_5d_diff},
    "mdv_drv2_022_obv_pctrank_spread_252d_21d_diff": {"inputs": ["close", "volume"], "func": mdv_drv2_022_obv_pctrank_spread_252d_21d_diff},
    "mdv_drv2_023_multi_osc_agreement_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_drv2_023_multi_osc_agreement_63d_5d_diff},
    "mdv_drv2_024_divg_gap_zscore_rsi_5d_slope": {"inputs": ["close"], "func": mdv_drv2_024_divg_gap_zscore_rsi_5d_slope},
    "mdv_drv2_025_obv_rsi_joint_divg_count_252d_21d_diff": {"inputs": ["close", "volume"], "func": mdv_drv2_025_obv_rsi_joint_divg_count_252d_21d_diff},
}
