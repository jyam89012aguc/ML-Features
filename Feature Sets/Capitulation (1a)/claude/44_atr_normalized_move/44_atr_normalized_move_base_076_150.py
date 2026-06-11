"""
44_atr_normalized_move — Base Features 076-150
Domain: price moves expressed in ATR units — volatility-standardized move magnitudes
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
    """Rolling mean ATR over w periods."""
    return _rolling_mean(_tr(close, high, low), w)


def _atr_ewm(close: pd.Series, high: pd.Series, low: pd.Series, span: int) -> pd.Series:
    """EWM-smoothed ATR."""
    return _ewm_mean(_tr(close, high, low), span)


def _daily_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log-return in ATR14 units (shared helper)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, 14)
    return _safe_div(ret, atr)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): ATR-unit velocity (rolling mean of normalized move) ---

def atr_076_atr_velocity_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling mean of ATR14-normalized daily moves (medium-term velocity)."""
    m = _daily_move_atr14(close, high, low)
    return _rolling_mean(m, _TD_MON)


def atr_077_atr_velocity_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling mean of ATR14-normalized daily moves (quarterly velocity)."""
    m = _daily_move_atr14(close, high, low)
    return _rolling_mean(m, _TD_QTR)


def atr_078_atr_velocity_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day rolling mean of ATR14-normalized daily moves (annual velocity)."""
    m = _daily_move_atr14(close, high, low)
    return _rolling_mean(m, _TD_YEAR)


def atr_079_atr_speed_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling mean of absolute ATR14-normalized moves (speed, direction-free)."""
    m = _daily_move_atr14(close, high, low).abs()
    return _rolling_mean(m, _TD_MON)


def atr_080_atr_speed_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling mean of absolute ATR14-normalized moves."""
    m = _daily_move_atr14(close, high, low).abs()
    return _rolling_mean(m, _TD_QTR)


def atr_081_atr_velocity_down_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of ATR14-normalized moves on down days only."""
    m = _daily_move_atr14(close, high, low)
    dn = m.where(m < 0, np.nan)
    return dn.rolling(_TD_MON, min_periods=1).mean()


def atr_082_atr_velocity_down_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day mean of ATR14-normalized moves on down days only."""
    m = _daily_move_atr14(close, high, low)
    dn = m.where(m < 0, np.nan)
    return dn.rolling(_TD_QTR, min_periods=1).mean()


def atr_083_atr_velocity_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day ATR-velocity to 252-day ATR-velocity (recent vs long-run pace)."""
    m = _daily_move_atr14(close, high, low)
    v21 = _rolling_mean(m, _TD_MON)
    v252 = _rolling_mean(m, _TD_YEAR)
    return _safe_div(v21, v252.abs() + _EPS)


def atr_084_atr_speed_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day ATR-speed to 252-day ATR-speed."""
    m = _daily_move_atr14(close, high, low).abs()
    s21 = _rolling_mean(m, _TD_MON)
    s252 = _rolling_mean(m, _TD_YEAR)
    return _safe_div(s21, s252)


def atr_085_atr_velocity_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day ATR-velocity within 252-day distribution."""
    m = _daily_move_atr14(close, high, low)
    v21 = _rolling_mean(m, _TD_MON)
    mu = _rolling_mean(v21, _TD_YEAR)
    sd = _rolling_std(v21, _TD_YEAR)
    return _safe_div(v21 - mu, sd)


# --- Group I (086-095): Open-to-close and gap moves in ATR units ---

def atr_086_open_to_close_atr14(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Intraday open-to-close move in ATR14 units."""
    move = _log_safe(close) - _log_safe(open)
    atr = _atr(close, high, low, 14)
    return _safe_div(move, atr)


def atr_087_gap_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Gap move (open vs prior close) in ATR14 units."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, 14)
    return _safe_div(gap, atr)


def atr_088_gap_down_atr14(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Downward gap move in ATR14 units; zero on gap-up days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, 14)
    raw = _safe_div(gap, atr)
    return raw.where(raw < 0, 0.0)


def atr_089_cum_gap_down_atr_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative gap-down ATR14-units over 21 days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, 14)
    raw = _safe_div(gap, atr)
    dn = raw.where(raw < 0, 0.0)
    return _rolling_sum(dn, _TD_MON)


def atr_090_intraday_range_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday high-low range divided by ATR14 (how large today's range is)."""
    rng = high - low
    atr = _atr(close, high, low, 14)
    return _safe_div(rng, atr)


def atr_091_intraday_range_atr14_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of intraday range in ATR14 units."""
    rng = atr_090_intraday_range_atr14(close, high, low)
    return _rolling_mean(rng, _TD_MON)


def atr_092_lower_wick_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lower wick (close - low) in ATR14 units."""
    atr = _atr(close, high, low, 14)
    return _safe_div(close - low, atr)


def atr_093_upper_wick_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Upper wick (high - close) in ATR14 units."""
    atr = _atr(close, high, low, 14)
    return _safe_div(high - close, atr)


def atr_094_wick_imbalance_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lower wick minus upper wick in ATR14 units (negative = upper wick dominant)."""
    atr = _atr(close, high, low, 14)
    lower = _safe_div(close - low, atr)
    upper = _safe_div(high - close, atr)
    return lower - upper


def atr_095_open_to_close_abs_atr14_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day mean of |open-to-close| in ATR14 units."""
    m = atr_086_open_to_close_atr14(close, high, low, open).abs()
    return _rolling_mean(m, _TD_MON)


# --- Group J (096-105): ATR-normalized move z-scores and ranks ---

def atr_096_5d_move_atr14_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 5-day ATR14-move within 252-day window."""
    m5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    atr = _atr(close, high, low, 14)
    nm = _safe_div(m5, atr)
    mu = _rolling_mean(nm, _TD_YEAR)
    sd = _rolling_std(nm, _TD_YEAR)
    return _safe_div(nm - mu, sd)


def atr_097_21d_move_atr14_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day ATR14-move within 252-day window."""
    m21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    atr = _atr(close, high, low, 14)
    nm = _safe_div(m21, atr)
    mu = _rolling_mean(nm, _TD_YEAR)
    sd = _rolling_std(nm, _TD_YEAR)
    return _safe_div(nm - mu, sd)


def atr_098_63d_move_atr21_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 63-day ATR21-move within 252-day window."""
    m63 = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    atr = _atr(close, high, low, _TD_MON)
    nm = _safe_div(m63, atr)
    mu = _rolling_mean(nm, _TD_YEAR)
    sd = _rolling_std(nm, _TD_YEAR)
    return _safe_div(nm - mu, sd)


def atr_099_5d_move_atr14_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 5-day ATR14-move in trailing 252-day distribution."""
    m5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    atr = _atr(close, high, low, 14)
    nm = _safe_div(m5, atr)
    return nm.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def atr_100_21d_move_atr14_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day ATR14-move in trailing 252-day distribution."""
    m21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    atr = _atr(close, high, low, 14)
    nm = _safe_div(m21, atr)
    return nm.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def atr_101_dist_below_sma200_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of SMA200 ATR14-distance in trailing 252-day distribution."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    mu = _rolling_mean(dist, _TD_YEAR)
    sd = _rolling_std(dist, _TD_YEAR)
    return _safe_div(dist - mu, sd)


def atr_102_dist_below_sma21_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of SMA21 ATR14-distance in trailing 252-day distribution."""
    ma = _rolling_mean(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    mu = _rolling_mean(dist, _TD_YEAR)
    sd = _rolling_std(dist, _TD_YEAR)
    return _safe_div(dist - mu, sd)


def atr_103_drawdown_52wk_atr14_zscore(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 252-day drawdown in ATR14 units within expanding history."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dd = _safe_div(close - high_252, atr)
    mu = dd.expanding(min_periods=5).mean()
    sd = dd.expanding(min_periods=5).std()
    return _safe_div(dd - mu, sd)


def atr_104_speed_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's |ATR14-move| relative to 252-day speed distribution."""
    m = _daily_move_atr14(close, high, low).abs()
    mu = _rolling_mean(m, _TD_YEAR)
    sd = _rolling_std(m, _TD_YEAR)
    return _safe_div(m - mu, sd)


def atr_105_intraday_range_atr14_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of intraday range in ATR14 units vs 252-day history."""
    rng = atr_090_intraday_range_atr14(close, high, low)
    mu = _rolling_mean(rng, _TD_YEAR)
    sd = _rolling_std(rng, _TD_YEAR)
    return _safe_div(rng - mu, sd)


# --- Group K (106-115): ATR-normalized move with volume weighting ---

def atr_106_vol_weighted_atr14_move_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average ATR14-move over 21 days (VWAP-style in ATR units)."""
    m = _daily_move_atr14(close, high, low)
    wt_m = m * volume
    return _safe_div(_rolling_sum(wt_m, _TD_MON), _rolling_sum(volume, _TD_MON))


def atr_107_vol_weighted_atr14_move_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average ATR14-move over 63 days."""
    m = _daily_move_atr14(close, high, low)
    wt_m = m * volume
    return _safe_div(_rolling_sum(wt_m, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def atr_108_vol_weighted_down_atr14_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average downward ATR14-move over 21 days."""
    m = _daily_move_atr14(close, high, low)
    dn_m = m.where(m < 0, 0.0)
    wt = dn_m * volume
    return _safe_div(_rolling_sum(wt, _TD_MON), _rolling_sum(volume, _TD_MON))


def atr_109_high_vol_day_atr14_move_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean ATR14-move on days with above-average volume, over 21 days."""
    m = _daily_move_atr14(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    m_hv = m.where(volume > avg_vol, np.nan)
    return m_hv.rolling(_TD_MON, min_periods=1).mean()


def atr_110_low_vol_day_atr14_move_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean ATR14-move on days with below-average volume, over 21 days."""
    m = _daily_move_atr14(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    m_lv = m.where(volume <= avg_vol, np.nan)
    return m_lv.rolling(_TD_MON, min_periods=1).mean()


def atr_111_atr14_move_vol_correlation_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling correlation between ATR14-move and volume (panic signal)."""
    m = _daily_move_atr14(close, high, low)
    return m.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).corr(volume)


def atr_112_atr14_move_vol_correlation_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling correlation between ATR14-move and volume."""
    m = _daily_move_atr14(close, high, low)
    return m.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).corr(volume)


def atr_113_down_day_vol_atr14_product_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (|ATR14-down-move| * norm-volume) on down days over 21 days."""
    m = _daily_move_atr14(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    prod = m.where(m < 0, 0.0).abs() * vol_norm
    return _rolling_sum(prod, _TD_MON)


def atr_114_down_day_vol_atr14_product_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (|ATR14-down-move| * norm-volume) on down days over 63 days."""
    m = _daily_move_atr14(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    prod = m.where(m < 0, 0.0).abs() * vol_norm
    return _rolling_sum(prod, _TD_QTR)


def atr_115_extreme_down_vol_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with move < -2 ATR14 AND volume > avg_vol in trailing 21 days."""
    m = _daily_move_atr14(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((m < -2) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


# --- Group L (116-125): ATR-normalized moves relative to SMA/EMA distances ---

def atr_116_dist_below_sma50_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 50-day SMA in ATR21 units."""
    ma = _rolling_mean(close, 50)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - ma, atr)


def atr_117_dist_below_sma63_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 63-day SMA in ATR21 units."""
    ma = _rolling_mean(close, _TD_QTR)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - ma, atr)


def atr_118_dist_below_ema50_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 50-day EMA in ATR14 units."""
    ema = _ewm_mean(close, 50)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - ema, atr)


def atr_119_ma_gap_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Gap between SMA21 and SMA200 expressed in ATR14 units."""
    sma21 = _rolling_mean(close, _TD_MON)
    sma200 = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    return _safe_div(sma21 - sma200, atr)


def atr_120_ma_cross_spread_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """SMA50 minus SMA200 in ATR14 units (death-cross depth)."""
    sma50 = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    return _safe_div(sma50 - sma200, atr)


def atr_121_dist_below_sma200_atr14_max_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Most negative SMA200 ATR14-distance in trailing 63 days."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return _rolling_min(dist, _TD_QTR)


def atr_122_dist_below_sma200_atr14_max_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Most negative SMA200 ATR14-distance in trailing 252 days."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return _rolling_min(dist, _TD_YEAR)


def atr_123_ema12_ema26_spread_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EMA12 minus EMA26 (MACD line) in ATR14 units."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    atr = _atr(close, high, low, 14)
    return _safe_div(ema12 - ema26, atr)


def atr_124_dist_below_ema63_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 63-day EMA in ATR21 units."""
    ema = _ewm_mean(close, _TD_QTR)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - ema, atr)


def atr_125_composite_ma_dist_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR14-distance below SMA21, SMA63, SMA200 (composite MA dislocation)."""
    atr = _atr(close, high, low, 14)
    d21 = _safe_div(close - _rolling_mean(close, _TD_MON), atr)
    d63 = _safe_div(close - _rolling_mean(close, _TD_QTR), atr)
    d200 = _safe_div(close - _rolling_mean(close, 200), atr)
    return (d21 + d63 + d200) / 3.0


# --- Group M (126-135): Multi-period normalized return ratios ---

def atr_126_5d_vs_1d_atr14_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day ATR14-move to 1-day ATR14-move (persistence signal)."""
    atr = _atr(close, high, low, 14)
    m1 = _safe_div(_log_safe(close) - _log_safe(close.shift(1)), atr)
    m5 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_WEEK)), atr)
    return _safe_div(m5, m1.abs() + _EPS)


def atr_127_21d_vs_5d_atr14_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day ATR14-move to 5-day ATR14-move."""
    atr = _atr(close, high, low, 14)
    m5 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_WEEK)), atr)
    m21 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_MON)), atr)
    return _safe_div(m21, m5.abs() + _EPS)


def atr_128_63d_vs_21d_atr14_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 63-day ATR14-move to 21-day ATR14-move."""
    atr = _atr(close, high, low, 14)
    m21 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_MON)), atr)
    m63 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_QTR)), atr)
    return _safe_div(m63, m21.abs() + _EPS)


def atr_129_252d_vs_63d_atr14_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 252-day ATR14-move to 63-day ATR14-move."""
    atr = _atr(close, high, low, 14)
    m63 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_QTR)), atr)
    m252 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_YEAR)), atr)
    return _safe_div(m252, m63.abs() + _EPS)


def atr_130_down_vs_total_atr14_speed_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of total ATR14-speed (path) that was downward over 21 days."""
    m = _daily_move_atr14(close, high, low)
    down_sum = m.where(m < 0, 0.0).rolling(_TD_MON, min_periods=1).sum().abs()
    total_sum = m.abs().rolling(_TD_MON, min_periods=1).sum()
    return _safe_div(down_sum, total_sum)


def atr_131_down_vs_total_atr14_speed_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of total ATR14-speed that was downward over 63 days."""
    m = _daily_move_atr14(close, high, low)
    down_sum = m.where(m < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum().abs()
    total_sum = m.abs().rolling(_TD_QTR, min_periods=1).sum()
    return _safe_div(down_sum, total_sum)


def atr_132_net_atr14_move_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Net directional ATR14-units over 21 days (sum of signed moves)."""
    m = _daily_move_atr14(close, high, low)
    return _rolling_sum(m, _TD_MON)


def atr_133_net_atr14_move_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Net directional ATR14-units over 63 days."""
    m = _daily_move_atr14(close, high, low)
    return _rolling_sum(m, _TD_QTR)


def atr_134_net_vs_gross_atr14_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of net to gross ATR14-units over 21 days (directionality index)."""
    m = _daily_move_atr14(close, high, low)
    net = _rolling_sum(m, _TD_MON)
    gross = _rolling_sum(m.abs(), _TD_MON)
    return _safe_div(net, gross)


def atr_135_net_vs_gross_atr14_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of net to gross ATR14-units over 63 days."""
    m = _daily_move_atr14(close, high, low)
    net = _rolling_sum(m, _TD_QTR)
    gross = _rolling_sum(m.abs(), _TD_QTR)
    return _safe_div(net, gross)


# --- Group N (136-145): Intraday position in range as ATR fraction ---

def atr_136_close_position_in_daily_range_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position in day's H-L range, expressed as ATR14 fraction (0=low, >0=above low)."""
    atr = _atr(close, high, low, 14)
    return _safe_div(close - low, atr)


def atr_137_high_above_prior_close_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's high above prior close in ATR14 units."""
    atr = _atr(close, high, low, 14)
    return _safe_div(high - close.shift(1), atr)


def atr_138_low_below_prior_close_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's low below prior close in ATR14 units (negative = below)."""
    atr = _atr(close, high, low, 14)
    return _safe_div(low - close.shift(1), atr)


def atr_139_true_range_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's true range as multiple of ATR14 (>1 = wider than average)."""
    tr = _tr(close, high, low)
    atr = _atr(close, high, low, 14)
    return _safe_div(tr, atr)


def atr_140_true_range_atr14_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of true-range/ATR14 ratio."""
    return _rolling_mean(atr_139_true_range_atr14(close, high, low), _TD_MON)


def atr_141_cum_tr_atr14_traveled_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative true-range in ATR14 units over 21 days (total volatility consumed)."""
    tr = _tr(close, high, low)
    atr = _atr(close, high, low, 14)
    tr_norm = _safe_div(tr, atr)
    return _rolling_sum(tr_norm, _TD_MON)


def atr_142_cum_tr_atr14_traveled_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative true-range in ATR14 units over 63 days."""
    tr = _tr(close, high, low)
    atr = _atr(close, high, low, 14)
    tr_norm = _safe_div(tr, atr)
    return _rolling_sum(tr_norm, _TD_QTR)


def atr_143_worst_intraday_low_atr14_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Most extreme low-below-prior-close in ATR14 units over trailing 5 days."""
    atr = _atr(close, high, low, 14)
    low_dist = _safe_div(low - close.shift(1), atr)
    return _rolling_min(low_dist, _TD_WEEK)


def atr_144_worst_intraday_low_atr14_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Most extreme low-below-prior-close in ATR14 units over trailing 21 days."""
    atr = _atr(close, high, low, 14)
    low_dist = _safe_div(low - close.shift(1), atr)
    return _rolling_min(low_dist, _TD_MON)


def atr_145_close_vs_high_atr14_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of close-minus-daily-high in ATR14 units (consistent sell-off into close)."""
    atr = _atr(close, high, low, 14)
    ch = _safe_div(close - high, atr)
    return _rolling_mean(ch, _TD_MON)


# --- Group O (146-150): Composite ATR-normalized distress scores ---

def atr_146_composite_down_move_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: mean of 5-day, 21-day, 63-day ATR14-moves (multi-horizon dislocation)."""
    atr = _atr(close, high, low, 14)
    m5 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_WEEK)), atr)
    m21 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_MON)), atr)
    m63 = _safe_div(_log_safe(close) - _log_safe(close.shift(_TD_QTR)), atr)
    return (m5 + m21 + m63) / 3.0


def atr_147_ma_dislocation_atr14_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR14-weighted dislocation below SMA21+SMA63+SMA200 combined."""
    atr = _atr(close, high, low, 14)
    d21 = _safe_div(close - _rolling_mean(close, _TD_MON), atr).clip(upper=0)
    d63 = _safe_div(close - _rolling_mean(close, _TD_QTR), atr).clip(upper=0)
    d200 = _safe_div(close - _rolling_mean(close, 200), atr).clip(upper=0)
    return d21 + d63 + d200


def atr_148_dist_from_52wk_high_atr14_expanding_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day high ATR14-distance (all-history extremity)."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - high_252, atr)
    return dist.expanding(min_periods=5).rank(pct=True)


def atr_149_extreme_down_count_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day extreme-down-move count within 252-day distribution."""
    m = _daily_move_atr14(close, high, low)
    cnt21 = _rolling_sum((m < -2).astype(float), _TD_MON)
    return cnt21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def atr_150_atr_distress_index(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined ATR-unit distress: cum_down_atr_21d * extreme_count_21d * vol_norm."""
    m = _daily_move_atr14(close, high, low)
    cum_dn = m.where(m < 0, 0.0).rolling(_TD_MON, min_periods=1).sum().abs()
    extreme_cnt = _rolling_sum((m < -2).astype(float), _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return cum_dn * (1 + extreme_cnt) * vol_norm


# ── Registry ──────────────────────────────────────────────────────────────────

ATR_NORMALIZED_MOVE_REGISTRY_076_150 = {
    "atr_076_atr_velocity_21d": {"inputs": ["close", "high", "low"], "func": atr_076_atr_velocity_21d},
    "atr_077_atr_velocity_63d": {"inputs": ["close", "high", "low"], "func": atr_077_atr_velocity_63d},
    "atr_078_atr_velocity_252d": {"inputs": ["close", "high", "low"], "func": atr_078_atr_velocity_252d},
    "atr_079_atr_speed_21d": {"inputs": ["close", "high", "low"], "func": atr_079_atr_speed_21d},
    "atr_080_atr_speed_63d": {"inputs": ["close", "high", "low"], "func": atr_080_atr_speed_63d},
    "atr_081_atr_velocity_down_21d": {"inputs": ["close", "high", "low"], "func": atr_081_atr_velocity_down_21d},
    "atr_082_atr_velocity_down_63d": {"inputs": ["close", "high", "low"], "func": atr_082_atr_velocity_down_63d},
    "atr_083_atr_velocity_21d_vs_252d": {"inputs": ["close", "high", "low"], "func": atr_083_atr_velocity_21d_vs_252d},
    "atr_084_atr_speed_21d_vs_252d": {"inputs": ["close", "high", "low"], "func": atr_084_atr_speed_21d_vs_252d},
    "atr_085_atr_velocity_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_085_atr_velocity_zscore_252d},
    "atr_086_open_to_close_atr14": {"inputs": ["close", "high", "low", "open"], "func": atr_086_open_to_close_atr14},
    "atr_087_gap_move_atr14": {"inputs": ["close", "high", "low", "open"], "func": atr_087_gap_move_atr14},
    "atr_088_gap_down_atr14": {"inputs": ["close", "high", "low", "open"], "func": atr_088_gap_down_atr14},
    "atr_089_cum_gap_down_atr_21d": {"inputs": ["close", "high", "low", "open"], "func": atr_089_cum_gap_down_atr_21d},
    "atr_090_intraday_range_atr14": {"inputs": ["close", "high", "low"], "func": atr_090_intraday_range_atr14},
    "atr_091_intraday_range_atr14_21d_mean": {"inputs": ["close", "high", "low"], "func": atr_091_intraday_range_atr14_21d_mean},
    "atr_092_lower_wick_atr14": {"inputs": ["close", "high", "low"], "func": atr_092_lower_wick_atr14},
    "atr_093_upper_wick_atr14": {"inputs": ["close", "high", "low"], "func": atr_093_upper_wick_atr14},
    "atr_094_wick_imbalance_atr14": {"inputs": ["close", "high", "low"], "func": atr_094_wick_imbalance_atr14},
    "atr_095_open_to_close_abs_atr14_21d_mean": {"inputs": ["close", "high", "low", "open"], "func": atr_095_open_to_close_abs_atr14_21d_mean},
    "atr_096_5d_move_atr14_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_096_5d_move_atr14_zscore_252d},
    "atr_097_21d_move_atr14_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_097_21d_move_atr14_zscore_252d},
    "atr_098_63d_move_atr21_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_098_63d_move_atr21_zscore_252d},
    "atr_099_5d_move_atr14_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_099_5d_move_atr14_pct_rank_252d},
    "atr_100_21d_move_atr14_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_100_21d_move_atr14_pct_rank_252d},
    "atr_101_dist_below_sma200_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_101_dist_below_sma200_zscore_252d},
    "atr_102_dist_below_sma21_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_102_dist_below_sma21_zscore_252d},
    "atr_103_drawdown_52wk_atr14_zscore": {"inputs": ["close", "high", "low"], "func": atr_103_drawdown_52wk_atr14_zscore},
    "atr_104_speed_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_104_speed_zscore_252d},
    "atr_105_intraday_range_atr14_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_105_intraday_range_atr14_zscore_252d},
    "atr_106_vol_weighted_atr14_move_21d": {"inputs": ["close", "high", "low", "volume"], "func": atr_106_vol_weighted_atr14_move_21d},
    "atr_107_vol_weighted_atr14_move_63d": {"inputs": ["close", "high", "low", "volume"], "func": atr_107_vol_weighted_atr14_move_63d},
    "atr_108_vol_weighted_down_atr14_21d": {"inputs": ["close", "high", "low", "volume"], "func": atr_108_vol_weighted_down_atr14_21d},
    "atr_109_high_vol_day_atr14_move_21d": {"inputs": ["close", "high", "low", "volume"], "func": atr_109_high_vol_day_atr14_move_21d},
    "atr_110_low_vol_day_atr14_move_21d": {"inputs": ["close", "high", "low", "volume"], "func": atr_110_low_vol_day_atr14_move_21d},
    "atr_111_atr14_move_vol_correlation_21d": {"inputs": ["close", "high", "low", "volume"], "func": atr_111_atr14_move_vol_correlation_21d},
    "atr_112_atr14_move_vol_correlation_63d": {"inputs": ["close", "high", "low", "volume"], "func": atr_112_atr14_move_vol_correlation_63d},
    "atr_113_down_day_vol_atr14_product_21d": {"inputs": ["close", "high", "low", "volume"], "func": atr_113_down_day_vol_atr14_product_21d},
    "atr_114_down_day_vol_atr14_product_63d": {"inputs": ["close", "high", "low", "volume"], "func": atr_114_down_day_vol_atr14_product_63d},
    "atr_115_extreme_down_vol_flag_21d": {"inputs": ["close", "high", "low", "volume"], "func": atr_115_extreme_down_vol_flag_21d},
    "atr_116_dist_below_sma50_atr21": {"inputs": ["close", "high", "low"], "func": atr_116_dist_below_sma50_atr21},
    "atr_117_dist_below_sma63_atr21": {"inputs": ["close", "high", "low"], "func": atr_117_dist_below_sma63_atr21},
    "atr_118_dist_below_ema50_atr14": {"inputs": ["close", "high", "low"], "func": atr_118_dist_below_ema50_atr14},
    "atr_119_ma_gap_atr14": {"inputs": ["close", "high", "low"], "func": atr_119_ma_gap_atr14},
    "atr_120_ma_cross_spread_atr14": {"inputs": ["close", "high", "low"], "func": atr_120_ma_cross_spread_atr14},
    "atr_121_dist_below_sma200_atr14_max_63d": {"inputs": ["close", "high", "low"], "func": atr_121_dist_below_sma200_atr14_max_63d},
    "atr_122_dist_below_sma200_atr14_max_252d": {"inputs": ["close", "high", "low"], "func": atr_122_dist_below_sma200_atr14_max_252d},
    "atr_123_ema12_ema26_spread_atr14": {"inputs": ["close", "high", "low"], "func": atr_123_ema12_ema26_spread_atr14},
    "atr_124_dist_below_ema63_atr21": {"inputs": ["close", "high", "low"], "func": atr_124_dist_below_ema63_atr21},
    "atr_125_composite_ma_dist_atr14": {"inputs": ["close", "high", "low"], "func": atr_125_composite_ma_dist_atr14},
    "atr_126_5d_vs_1d_atr14_ratio": {"inputs": ["close", "high", "low"], "func": atr_126_5d_vs_1d_atr14_ratio},
    "atr_127_21d_vs_5d_atr14_ratio": {"inputs": ["close", "high", "low"], "func": atr_127_21d_vs_5d_atr14_ratio},
    "atr_128_63d_vs_21d_atr14_ratio": {"inputs": ["close", "high", "low"], "func": atr_128_63d_vs_21d_atr14_ratio},
    "atr_129_252d_vs_63d_atr14_ratio": {"inputs": ["close", "high", "low"], "func": atr_129_252d_vs_63d_atr14_ratio},
    "atr_130_down_vs_total_atr14_speed_21d": {"inputs": ["close", "high", "low"], "func": atr_130_down_vs_total_atr14_speed_21d},
    "atr_131_down_vs_total_atr14_speed_63d": {"inputs": ["close", "high", "low"], "func": atr_131_down_vs_total_atr14_speed_63d},
    "atr_132_net_atr14_move_21d": {"inputs": ["close", "high", "low"], "func": atr_132_net_atr14_move_21d},
    "atr_133_net_atr14_move_63d": {"inputs": ["close", "high", "low"], "func": atr_133_net_atr14_move_63d},
    "atr_134_net_vs_gross_atr14_21d": {"inputs": ["close", "high", "low"], "func": atr_134_net_vs_gross_atr14_21d},
    "atr_135_net_vs_gross_atr14_63d": {"inputs": ["close", "high", "low"], "func": atr_135_net_vs_gross_atr14_63d},
    "atr_136_close_position_in_daily_range_atr": {"inputs": ["close", "high", "low"], "func": atr_136_close_position_in_daily_range_atr},
    "atr_137_high_above_prior_close_atr14": {"inputs": ["close", "high", "low"], "func": atr_137_high_above_prior_close_atr14},
    "atr_138_low_below_prior_close_atr14": {"inputs": ["close", "high", "low"], "func": atr_138_low_below_prior_close_atr14},
    "atr_139_true_range_atr14": {"inputs": ["close", "high", "low"], "func": atr_139_true_range_atr14},
    "atr_140_true_range_atr14_21d_mean": {"inputs": ["close", "high", "low"], "func": atr_140_true_range_atr14_21d_mean},
    "atr_141_cum_tr_atr14_traveled_21d": {"inputs": ["close", "high", "low"], "func": atr_141_cum_tr_atr14_traveled_21d},
    "atr_142_cum_tr_atr14_traveled_63d": {"inputs": ["close", "high", "low"], "func": atr_142_cum_tr_atr14_traveled_63d},
    "atr_143_worst_intraday_low_atr14_5d": {"inputs": ["close", "high", "low"], "func": atr_143_worst_intraday_low_atr14_5d},
    "atr_144_worst_intraday_low_atr14_21d": {"inputs": ["close", "high", "low"], "func": atr_144_worst_intraday_low_atr14_21d},
    "atr_145_close_vs_high_atr14_21d_mean": {"inputs": ["close", "high", "low"], "func": atr_145_close_vs_high_atr14_21d_mean},
    "atr_146_composite_down_move_score": {"inputs": ["close", "high", "low"], "func": atr_146_composite_down_move_score},
    "atr_147_ma_dislocation_atr14_score": {"inputs": ["close", "high", "low"], "func": atr_147_ma_dislocation_atr14_score},
    "atr_148_dist_from_52wk_high_atr14_expanding_rank": {"inputs": ["close", "high", "low"], "func": atr_148_dist_from_52wk_high_atr14_expanding_rank},
    "atr_149_extreme_down_count_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_149_extreme_down_count_pct_rank_252d},
    "atr_150_atr_distress_index": {"inputs": ["close", "high", "low", "volume"], "func": atr_150_atr_distress_index},
}
