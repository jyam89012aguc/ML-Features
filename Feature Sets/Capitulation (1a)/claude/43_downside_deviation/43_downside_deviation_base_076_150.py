"""
43_downside_deviation — Base Features 076-150
Domain: semi-variance and downside-only dispersion magnitude
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_ret(s: pd.Series) -> pd.Series:
    """Daily log-return series."""
    return np.log(s.clip(lower=_EPS)).diff(1)


def _pct_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _lpm(r: pd.Series, w: int, order: int, threshold: float = 0.0) -> pd.Series:
    """Rolling lower partial moment of given order."""
    below = ((threshold - r).clip(lower=0.0) ** order)
    return below.rolling(w, min_periods=max(1, w // 2)).mean()


def _semi_dev_w(r: pd.Series, w: int) -> pd.Series:
    """Semi-deviation of log-returns below zero over window w."""
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(w, min_periods=max(1, w // 2)).mean())


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): High/Low-based downside dispersion ---

def dsd_076_low_return_semi_dev_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day semi-deviation of daily low-to-close returns (low-return dispersion)."""
    r = np.log((low / close.shift(1)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_077_low_return_semi_dev_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """63-day semi-deviation of daily low-to-prior-close returns."""
    r = np.log((low / close.shift(1)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_078_low_return_semi_dev_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """252-day semi-deviation of daily low-to-prior-close returns."""
    r = np.log((low / close.shift(1)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())


def dsd_079_intraday_downside_range_semi_dev_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day semi-deviation of negative daily open-to-low moves (close used as proxy)."""
    r = np.log((low / high).clip(lower=_EPS))
    sq = (r ** 2)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_080_intraday_downside_range_semi_dev_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day semi-deviation of log(low/high) (intraday downside range magnitude)."""
    r = np.log((low / high).clip(lower=_EPS))
    sq = (r ** 2)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_081_close_to_low_semi_dev_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day semi-deviation of log(low/close): within-day downside move from close."""
    r = np.log((low / close).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_082_close_to_low_semi_dev_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """63-day semi-deviation of log(low/close)."""
    r = np.log((low / close).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_083_open_to_low_semi_dev_21d(open: pd.Series, low: pd.Series) -> pd.Series:
    """21-day semi-deviation of log(low/open): worst intraday drawdown from open."""
    r = np.log((low / open.clip(lower=_EPS)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_084_open_to_low_semi_dev_63d(open: pd.Series, low: pd.Series) -> pd.Series:
    """63-day semi-deviation of log(low/open)."""
    r = np.log((low / open.clip(lower=_EPS)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_085_open_to_low_vs_open_to_high_semi_dev_ratio_63d(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 63-day semi-dev of open-to-low vs semi-dev of open-to-high moves."""
    r_dn = np.log((low / open.clip(lower=_EPS)).clip(lower=_EPS))
    r_up = np.log((high / open.clip(lower=_EPS)).clip(lower=_EPS))
    sq_dn = (r_dn ** 2).where(r_dn < 0.0, 0.0)
    sq_up = (r_up ** 2).where(r_up > 0.0, 0.0)
    sd_dn = np.sqrt(sq_dn.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    sd_up = np.sqrt(sq_up.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return _safe_div(sd_dn, sd_up)


# --- Group I (086-095): Volume-weighted downside dispersion ---

def dsd_086_vol_weighted_semi_dev_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume-weighted semi-deviation: down-day squared returns weighted by volume."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol.replace(0, np.nan)).fillna(1.0)
    sq = (r ** 2 * vol_norm).where(r < 0.0, 0.0)
    wt = vol_norm.where(r < 0.0, 0.0)
    num = sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    den = wt.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    return np.sqrt(_safe_div(num, den).clip(lower=0.0))


def dsd_087_vol_weighted_semi_dev_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day volume-weighted semi-deviation."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol.replace(0, np.nan)).fillna(1.0)
    sq = (r ** 2 * vol_norm).where(r < 0.0, 0.0)
    wt = vol_norm.where(r < 0.0, 0.0)
    num = sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    den = wt.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    return np.sqrt(_safe_div(num, den).clip(lower=0.0))


def dsd_088_high_vol_down_day_semi_dev_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day semi-deviation computed only on high-volume (>21d avg) down days."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    mask = (r < 0.0) & (volume > avg_vol)
    sq = (r ** 2).where(mask, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_089_high_vol_down_day_semi_dev_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day semi-deviation on high-volume (>21d avg) down days only."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    mask = (r < 0.0) & (volume > avg_vol)
    sq = (r ** 2).where(mask, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_090_vol_times_down_return_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day sum of (volume * |negative return|): aggregate downside dollar pain proxy."""
    r = _log_ret(close)
    pain = (volume * r.abs()).where(r < 0.0, 0.0)
    return _rolling_sum(pain, _TD_MON)


def dsd_091_vol_times_down_return_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day sum of volume * |negative return| (downside dollar pain)."""
    r = _log_ret(close)
    pain = (volume * r.abs()).where(r < 0.0, 0.0)
    return _rolling_sum(pain, _TD_QTR)


def dsd_092_vol_times_down_return_norm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day downside dollar pain normalized by 252-day average."""
    pain21 = dsd_090_vol_times_down_return_21d(close, volume)
    avg = _rolling_mean(pain21, _TD_YEAR)
    return _safe_div(pain21, avg)


def dsd_093_down_vol_lpm1_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day LPM1 vs 0 weighted by normalized daily volume."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol.replace(0, np.nan)).fillna(1.0)
    below = ((0.0 - r).clip(lower=0.0) * vol_norm)
    wt = vol_norm
    num = below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    den = wt.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    return _safe_div(num, den)


def dsd_094_down_vol_lpm1_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day volume-weighted LPM1 vs 0."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol.replace(0, np.nan)).fillna(1.0)
    below = ((0.0 - r).clip(lower=0.0) * vol_norm)
    wt = vol_norm
    num = below.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    den = wt.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    return _safe_div(num, den)


def dsd_095_vol_scaled_semi_dev_ratio_21_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day volume-weighted semi-deviation (recent vs medium)."""
    sd21 = dsd_086_vol_weighted_semi_dev_21d(close, volume)
    sd63 = dsd_087_vol_weighted_semi_dev_63d(close, volume)
    return _safe_div(sd21, sd63)


# --- Group J (096-105): Multi-target LPM and threshold sensitivity ---

def dsd_096_lpm1_vs_neg1pct_21d(close: pd.Series) -> pd.Series:
    """21-day LPM1 with target = -1% (shortfall below -1% daily return)."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.01)
    below = (threshold - r).clip(lower=0.0)
    return below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_097_lpm1_vs_neg2pct_21d(close: pd.Series) -> pd.Series:
    """21-day LPM1 with target = -2% daily return."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.02)
    below = (threshold - r).clip(lower=0.0)
    return below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_098_lpm2_vs_neg1pct_21d(close: pd.Series) -> pd.Series:
    """21-day LPM2 with target = -1% (squared shortfall below -1%)."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.01)
    below = ((threshold - r).clip(lower=0.0) ** 2)
    return below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_099_lpm2_vs_neg2pct_63d(close: pd.Series) -> pd.Series:
    """63-day LPM2 with target = -2% daily return."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.02)
    below = ((threshold - r).clip(lower=0.0) ** 2)
    return below.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_100_lpm1_vs_neg1pct_63d(close: pd.Series) -> pd.Series:
    """63-day LPM1 with target = -1%."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.01)
    below = (threshold - r).clip(lower=0.0)
    return below.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_101_lpm1_vs_neg1pct_252d(close: pd.Series) -> pd.Series:
    """252-day LPM1 with target = -1%."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.01)
    below = (threshold - r).clip(lower=0.0)
    return below.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def dsd_102_lpm3_vs_neg1pct_21d(close: pd.Series) -> pd.Series:
    """21-day LPM3 with target = -1% (emphasises extreme tail events)."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.01)
    below = ((threshold - r).clip(lower=0.0) ** 3)
    return below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_103_lpm3_vs_neg2pct_63d(close: pd.Series) -> pd.Series:
    """63-day LPM3 with target = -2%."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.02)
    below = ((threshold - r).clip(lower=0.0) ** 3)
    return below.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_104_lpm2_tail_above_2sigma_21d(close: pd.Series) -> pd.Series:
    """21-day LPM2 restricted to returns more than 2 sigma below mean (tail semi-var)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    sig = _rolling_std(r, _TD_MON)
    threshold = mu - 2.0 * sig
    sq = ((r - threshold) ** 2).where(r < threshold, 0.0)
    return sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_105_lpm2_tail_above_2sigma_63d(close: pd.Series) -> pd.Series:
    """63-day LPM2 restricted to returns more than 2 sigma below mean."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_QTR)
    sig = _rolling_std(r, _TD_QTR)
    threshold = mu - 2.0 * sig
    sq = ((r - threshold) ** 2).where(r < threshold, 0.0)
    return sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


# --- Group K (106-115): Semi-deviation across time-scale ratios ---

def dsd_106_semi_dev_ratio_5d_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day semi-dev to 21-day semi-dev (short-term to medium-term)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd5 = np.sqrt(sq.rolling(_TD_WEEK, min_periods=1).mean())
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return _safe_div(sd5, sd21)


def dsd_107_semi_dev_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day semi-dev to 63-day semi-dev."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return _safe_div(sd21, sd63)


def dsd_108_semi_dev_ratio_63d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day semi-dev to 252-day semi-dev."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return _safe_div(sd63, sd252)


def dsd_109_semi_dev_ratio_21d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day semi-dev to 252-day semi-dev (short-vs-long regime)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return _safe_div(sd21, sd252)


def dsd_110_semi_dev_ewm_span21_vs_span126(close: pd.Series) -> pd.Series:
    """Ratio of EWM semi-dev span=21 to span=126 (short vs long EWM)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    fast = np.sqrt(sq.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    slow = np.sqrt(sq.ewm(span=_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean())
    return _safe_div(fast, slow)


def dsd_111_lpm1_ratio_21d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day LPM1 (vs 0) to 252-day LPM1 (recent vs long-run shortfall)."""
    r = _log_ret(close)
    lpm21 = _lpm(r, _TD_MON, 1, 0.0)
    lpm252 = _lpm(r, _TD_YEAR, 1, 0.0)
    return _safe_div(lpm21, lpm252)


def dsd_112_lpm2_ratio_21d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day LPM2 to 252-day LPM2."""
    r = _log_ret(close)
    lpm21 = _lpm(r, _TD_MON, 2, 0.0)
    lpm252 = _lpm(r, _TD_YEAR, 2, 0.0)
    return _safe_div(lpm21, lpm252)


def dsd_113_lpm2_ratio_63d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day LPM2 to 252-day LPM2."""
    r = _log_ret(close)
    lpm63 = _lpm(r, _TD_QTR, 2, 0.0)
    lpm252 = _lpm(r, _TD_YEAR, 2, 0.0)
    return _safe_div(lpm63, lpm252)


def dsd_114_semi_dev_5d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5-day semi-dev to 252-day semi-dev (extreme short-vs-long)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd5 = np.sqrt(sq.rolling(_TD_WEEK, min_periods=1).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return _safe_div(sd5, sd252)


def dsd_115_semi_dev_126d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 126-day semi-dev to 252-day semi-dev (half-year vs year)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd126 = np.sqrt(sq.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return _safe_div(sd126, sd252)


# --- Group L (116-125): Conditional semi-deviation by market regime ---

def dsd_116_semi_dev_21d_below_sma200(close: pd.Series) -> pd.Series:
    """21-day semi-dev computed only when close < SMA200 (bear regime downside vol)."""
    r = _log_ret(close)
    sma200 = _rolling_mean(close, 200)
    mask = (r < 0.0) & (close < sma200)
    sq = (r ** 2).where(mask, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_117_semi_dev_63d_below_sma200(close: pd.Series) -> pd.Series:
    """63-day semi-dev computed only when close < SMA200."""
    r = _log_ret(close)
    sma200 = _rolling_mean(close, 200)
    mask = (r < 0.0) & (close < sma200)
    sq = (r ** 2).where(mask, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_118_semi_dev_bear_vs_all_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of bear-regime semi-dev to overall semi-dev over 21 days."""
    sd_bear = dsd_116_semi_dev_21d_below_sma200(close)
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd_all = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return _safe_div(sd_bear, sd_all)


def dsd_119_semi_dev_21d_below_sma63(close: pd.Series) -> pd.Series:
    """21-day semi-dev restricted to days when close < SMA63."""
    r = _log_ret(close)
    sma63 = _rolling_mean(close, _TD_QTR)
    mask = (r < 0.0) & (close < sma63)
    sq = (r ** 2).where(mask, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_120_semi_dev_21d_above_sma200(close: pd.Series) -> pd.Series:
    """21-day semi-dev restricted to days when close > SMA200 (bull regime downside)."""
    r = _log_ret(close)
    sma200 = _rolling_mean(close, 200)
    mask = (r < 0.0) & (close > sma200)
    sq = (r ** 2).where(mask, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_121_semi_dev_bear_vs_bull_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of bear-regime semi-dev to bull-regime semi-dev over 21 days."""
    sd_bear = dsd_116_semi_dev_21d_below_sma200(close)
    sd_bull = dsd_120_semi_dev_21d_above_sma200(close)
    return _safe_div(sd_bear, sd_bull)


def dsd_122_high_vol_regime_semi_dev_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day semi-dev on high-volume-regime days (volume > 252d avg)."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    mask = (r < 0.0) & (volume > avg_vol)
    sq = (r ** 2).where(mask, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_123_low_vol_regime_semi_dev_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day semi-dev on low-volume-regime days (volume < 252d avg)."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    mask = (r < 0.0) & (volume < avg_vol)
    sq = (r ** 2).where(mask, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_124_hi_vol_vs_lo_vol_semi_dev_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of high-volume-regime to low-volume-regime 63-day semi-deviation."""
    sd_hi = dsd_122_high_vol_regime_semi_dev_63d(close, volume)
    sd_lo = dsd_123_low_vol_regime_semi_dev_63d(close, volume)
    return _safe_div(sd_hi, sd_lo)


def dsd_125_gap_down_semi_dev_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day semi-dev of gap-down opens (log(open/prior_close) when negative)."""
    r = np.log((open / close.shift(1)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


# --- Group M (126-135): Expanding and long-horizon downside dispersion ---

def dsd_126_semi_dev_expanding_mean(close: pd.Series) -> pd.Series:
    """Expanding (all-history) mean of daily squared negative log-returns."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.expanding(min_periods=5).mean())


def dsd_127_lpm2_vs0_expanding(close: pd.Series) -> pd.Series:
    """Expanding LPM2 vs 0 (all-history downside semi-variance)."""
    r = _log_ret(close)
    below_sq = ((0.0 - r).clip(lower=0.0) ** 2)
    return below_sq.expanding(min_periods=5).mean()


def dsd_128_semi_dev_504d(close: pd.Series) -> pd.Series:
    """504-day (2-year) semi-deviation of log-returns."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(504, min_periods=252).mean())


def dsd_129_lpm1_vs0_504d(close: pd.Series) -> pd.Series:
    """504-day LPM1 vs 0 (2-year expected shortfall below zero)."""
    r = _log_ret(close)
    below = (0.0 - r).clip(lower=0.0)
    return below.rolling(504, min_periods=252).mean()


def dsd_130_semi_dev_21d_vs_504d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day semi-dev to 504-day semi-dev (very short vs very long)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd504 = np.sqrt(sq.rolling(504, min_periods=252).mean())
    return _safe_div(sd21, sd504)


def dsd_131_semi_dev_126d_vs_504d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 126-day semi-dev to 504-day semi-dev."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd126 = np.sqrt(sq.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean())
    sd504 = np.sqrt(sq.rolling(504, min_periods=252).mean())
    return _safe_div(sd126, sd504)


def dsd_132_expanding_semi_dev_pct_rank_10yr(close: pd.Series) -> pd.Series:
    """Percentile rank of 252-day semi-dev within trailing 504-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return sd252.rolling(504, min_periods=252).rank(pct=True)


def dsd_133_semi_dev_252d_vs_expanding_mean(close: pd.Series) -> pd.Series:
    """252-day semi-dev normalized by its all-history expanding mean."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    exp_mu = sd252.expanding(min_periods=5).mean()
    return _safe_div(sd252, exp_mu)


def dsd_134_lpm2_vs_mean_252d_vs_expanding(close: pd.Series) -> pd.Series:
    """252-day below-mean LPM2 normalized by expanding mean of that LPM2."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_YEAR)
    below_sq = ((mu - r).clip(lower=0.0) ** 2)
    lpm = below_sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()
    exp_mu = lpm.expanding(min_periods=5).mean()
    return _safe_div(lpm, exp_mu)


def dsd_135_lpm3_vs0_252d_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252-day LPM3 within trailing 504-day distribution."""
    r = _log_ret(close)
    lpm3 = _lpm(r, _TD_YEAR, 3, 0.0)
    return lpm3.rolling(504, min_periods=252).rank(pct=True)


# --- Group N (136-145): Cross-period downside dispersion composites ---

def dsd_136_semi_dev_composite_3window(close: pd.Series) -> pd.Series:
    """Average of normalized 21d, 63d, 252d semi-deviations (composite downside vol)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    n21 = _safe_div(sd21, _rolling_mean(sd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(sd63, _rolling_mean(sd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(sd252, _rolling_mean(sd252, _TD_YEAR).clip(lower=_EPS))
    return (n21 + n63 + n252) / 3.0


def dsd_137_lpm_composite_3order(close: pd.Series) -> pd.Series:
    """Average of normalized LPM1, LPM2, LPM3 (vs 0, 21d window)."""
    r = _log_ret(close)
    lpm1 = _lpm(r, _TD_MON, 1, 0.0)
    lpm2 = _lpm(r, _TD_MON, 2, 0.0)
    lpm3 = _lpm(r, _TD_MON, 3, 0.0)
    n1 = _safe_div(lpm1, _rolling_mean(lpm1, _TD_YEAR).clip(lower=_EPS))
    n2 = _safe_div(lpm2, _rolling_mean(lpm2, _TD_YEAR).clip(lower=_EPS))
    n3 = _safe_div(lpm3, _rolling_mean(lpm3, _TD_YEAR).clip(lower=_EPS))
    return (n1 + n2 + n3) / 3.0


def dsd_138_downside_vol_zscore_composite(close: pd.Series) -> pd.Series:
    """Composite z-score: average of z-scores of semi-dev over 21d, 63d, 252d."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    def zscore(s):
        mu = _rolling_mean(s, _TD_YEAR)
        sig = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - mu, sig)
    return (zscore(sd21) + zscore(sd63) + zscore(sd252)) / 3.0


def dsd_139_semi_dev_21d_gt_252d_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day semi-dev > 252-day semi-dev (short-term downside vol elevated)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return (sd21 > sd252).astype(float)


def dsd_140_semi_dev_63d_gt_252d_flag(close: pd.Series) -> pd.Series:
    """Flag: 63-day semi-dev > 252-day semi-dev."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return (sd63 > sd252).astype(float)


def dsd_141_lpm1_composite_21_63_252(close: pd.Series) -> pd.Series:
    """Average of 21d, 63d, 252d LPM1 vs 0 (multi-horizon shortfall composite)."""
    r = _log_ret(close)
    lpm21 = _lpm(r, _TD_MON, 1, 0.0)
    lpm63 = _lpm(r, _TD_QTR, 1, 0.0)
    lpm252 = _lpm(r, _TD_YEAR, 1, 0.0)
    return (lpm21 + lpm63 + lpm252) / 3.0


def dsd_142_semi_dev_vol_interaction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day semi-dev times normalized volume (downside vol intensity)."""
    sd = _semi_dev_w(_log_ret(close), _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return sd * vol_norm


def dsd_143_semi_dev_vol_interaction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day semi-dev times normalized volume."""
    sd = _semi_dev_w(_log_ret(close), _TD_QTR)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    return sd * vol_norm


def dsd_144_lpm2_vs0_21d_vs_lpm2_mean_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of LPM2 vs 0 to LPM2 vs rolling mean (excess tail vs mean shortfall)."""
    r = _log_ret(close)
    lpm2_0 = _lpm(r, _TD_MON, 2, 0.0)
    mu = _rolling_mean(r, _TD_MON)
    below = ((mu - r).clip(lower=0.0) ** 2)
    lpm2_mu = below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return _safe_div(lpm2_0, lpm2_mu)


def dsd_145_semi_dev_21d_ewm_div_21d_rolling(close: pd.Series) -> pd.Series:
    """Ratio of EWM semi-dev (span=21) to rolling 21-day semi-dev (EWM vs equal-weight)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd_ewm = np.sqrt(sq.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd_roll = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return _safe_div(sd_ewm, sd_roll)


# --- Group O (146-150): Extreme downside deviation flags and composites ---

def dsd_146_semi_dev_expanding_zscore_21d(close: pd.Series) -> pd.Series:
    """Expanding z-score of 21-day semi-dev (all-history perspective)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    mu = sd21.expanding(min_periods=5).mean()
    sig = sd21.expanding(min_periods=5).std()
    return _safe_div(sd21 - mu, sig)


def dsd_147_lpm2_expanding_zscore_63d(close: pd.Series) -> pd.Series:
    """Expanding z-score of 63-day LPM2 vs 0."""
    r = _log_ret(close)
    lpm2 = _lpm(r, _TD_QTR, 2, 0.0)
    mu = lpm2.expanding(min_periods=5).mean()
    sig = lpm2.expanding(min_periods=5).std()
    return _safe_div(lpm2 - mu, sig)


def dsd_148_semi_dev_21d_acceleration(close: pd.Series) -> pd.Series:
    """5-day change in 21-day semi-dev (velocity of downside vol expansion)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return sd21.diff(_TD_WEEK)


def dsd_149_semi_dev_distress_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite distress: (21d semi-dev z-score) * (vol-normalized downside count)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    mu = _rolling_mean(sd21, _TD_YEAR)
    sig = _rolling_std(sd21, _TD_YEAR)
    z = _safe_div(sd21 - mu, sig)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    dn_count = (r < 0.0).astype(float).rolling(_TD_MON, min_periods=1).mean()
    return z * vol_norm * dn_count


def dsd_150_semi_dev_21d_log(close: pd.Series) -> pd.Series:
    """Log1p of 21-day semi-deviation (compresses large values)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return np.log1p(sd21)


# ── Registry ──────────────────────────────────────────────────────────────────

DOWNSIDE_DEVIATION_REGISTRY_076_150 = {
    "dsd_076_low_return_semi_dev_21d": {"inputs": ["close", "low"], "func": dsd_076_low_return_semi_dev_21d},
    "dsd_077_low_return_semi_dev_63d": {"inputs": ["close", "low"], "func": dsd_077_low_return_semi_dev_63d},
    "dsd_078_low_return_semi_dev_252d": {"inputs": ["close", "low"], "func": dsd_078_low_return_semi_dev_252d},
    "dsd_079_intraday_downside_range_semi_dev_21d": {"inputs": ["close", "high", "low"], "func": dsd_079_intraday_downside_range_semi_dev_21d},
    "dsd_080_intraday_downside_range_semi_dev_63d": {"inputs": ["close", "high", "low"], "func": dsd_080_intraday_downside_range_semi_dev_63d},
    "dsd_081_close_to_low_semi_dev_21d": {"inputs": ["close", "low"], "func": dsd_081_close_to_low_semi_dev_21d},
    "dsd_082_close_to_low_semi_dev_63d": {"inputs": ["close", "low"], "func": dsd_082_close_to_low_semi_dev_63d},
    "dsd_083_open_to_low_semi_dev_21d": {"inputs": ["open", "low"], "func": dsd_083_open_to_low_semi_dev_21d},
    "dsd_084_open_to_low_semi_dev_63d": {"inputs": ["open", "low"], "func": dsd_084_open_to_low_semi_dev_63d},
    "dsd_085_open_to_low_vs_open_to_high_semi_dev_ratio_63d": {"inputs": ["open", "high", "low"], "func": dsd_085_open_to_low_vs_open_to_high_semi_dev_ratio_63d},
    "dsd_086_vol_weighted_semi_dev_21d": {"inputs": ["close", "volume"], "func": dsd_086_vol_weighted_semi_dev_21d},
    "dsd_087_vol_weighted_semi_dev_63d": {"inputs": ["close", "volume"], "func": dsd_087_vol_weighted_semi_dev_63d},
    "dsd_088_high_vol_down_day_semi_dev_21d": {"inputs": ["close", "volume"], "func": dsd_088_high_vol_down_day_semi_dev_21d},
    "dsd_089_high_vol_down_day_semi_dev_63d": {"inputs": ["close", "volume"], "func": dsd_089_high_vol_down_day_semi_dev_63d},
    "dsd_090_vol_times_down_return_21d": {"inputs": ["close", "volume"], "func": dsd_090_vol_times_down_return_21d},
    "dsd_091_vol_times_down_return_63d": {"inputs": ["close", "volume"], "func": dsd_091_vol_times_down_return_63d},
    "dsd_092_vol_times_down_return_norm_21d": {"inputs": ["close", "volume"], "func": dsd_092_vol_times_down_return_norm_21d},
    "dsd_093_down_vol_lpm1_21d": {"inputs": ["close", "volume"], "func": dsd_093_down_vol_lpm1_21d},
    "dsd_094_down_vol_lpm1_63d": {"inputs": ["close", "volume"], "func": dsd_094_down_vol_lpm1_63d},
    "dsd_095_vol_scaled_semi_dev_ratio_21_63d": {"inputs": ["close", "volume"], "func": dsd_095_vol_scaled_semi_dev_ratio_21_63d},
    "dsd_096_lpm1_vs_neg1pct_21d": {"inputs": ["close"], "func": dsd_096_lpm1_vs_neg1pct_21d},
    "dsd_097_lpm1_vs_neg2pct_21d": {"inputs": ["close"], "func": dsd_097_lpm1_vs_neg2pct_21d},
    "dsd_098_lpm2_vs_neg1pct_21d": {"inputs": ["close"], "func": dsd_098_lpm2_vs_neg1pct_21d},
    "dsd_099_lpm2_vs_neg2pct_63d": {"inputs": ["close"], "func": dsd_099_lpm2_vs_neg2pct_63d},
    "dsd_100_lpm1_vs_neg1pct_63d": {"inputs": ["close"], "func": dsd_100_lpm1_vs_neg1pct_63d},
    "dsd_101_lpm1_vs_neg1pct_252d": {"inputs": ["close"], "func": dsd_101_lpm1_vs_neg1pct_252d},
    "dsd_102_lpm3_vs_neg1pct_21d": {"inputs": ["close"], "func": dsd_102_lpm3_vs_neg1pct_21d},
    "dsd_103_lpm3_vs_neg2pct_63d": {"inputs": ["close"], "func": dsd_103_lpm3_vs_neg2pct_63d},
    "dsd_104_lpm2_tail_above_2sigma_21d": {"inputs": ["close"], "func": dsd_104_lpm2_tail_above_2sigma_21d},
    "dsd_105_lpm2_tail_above_2sigma_63d": {"inputs": ["close"], "func": dsd_105_lpm2_tail_above_2sigma_63d},
    "dsd_106_semi_dev_ratio_5d_21d": {"inputs": ["close"], "func": dsd_106_semi_dev_ratio_5d_21d},
    "dsd_107_semi_dev_ratio_21d_63d": {"inputs": ["close"], "func": dsd_107_semi_dev_ratio_21d_63d},
    "dsd_108_semi_dev_ratio_63d_252d": {"inputs": ["close"], "func": dsd_108_semi_dev_ratio_63d_252d},
    "dsd_109_semi_dev_ratio_21d_252d": {"inputs": ["close"], "func": dsd_109_semi_dev_ratio_21d_252d},
    "dsd_110_semi_dev_ewm_span21_vs_span126": {"inputs": ["close"], "func": dsd_110_semi_dev_ewm_span21_vs_span126},
    "dsd_111_lpm1_ratio_21d_252d": {"inputs": ["close"], "func": dsd_111_lpm1_ratio_21d_252d},
    "dsd_112_lpm2_ratio_21d_252d": {"inputs": ["close"], "func": dsd_112_lpm2_ratio_21d_252d},
    "dsd_113_lpm2_ratio_63d_252d": {"inputs": ["close"], "func": dsd_113_lpm2_ratio_63d_252d},
    "dsd_114_semi_dev_5d_vs_252d_ratio": {"inputs": ["close"], "func": dsd_114_semi_dev_5d_vs_252d_ratio},
    "dsd_115_semi_dev_126d_vs_252d_ratio": {"inputs": ["close"], "func": dsd_115_semi_dev_126d_vs_252d_ratio},
    "dsd_116_semi_dev_21d_below_sma200": {"inputs": ["close"], "func": dsd_116_semi_dev_21d_below_sma200},
    "dsd_117_semi_dev_63d_below_sma200": {"inputs": ["close"], "func": dsd_117_semi_dev_63d_below_sma200},
    "dsd_118_semi_dev_bear_vs_all_ratio_21d": {"inputs": ["close"], "func": dsd_118_semi_dev_bear_vs_all_ratio_21d},
    "dsd_119_semi_dev_21d_below_sma63": {"inputs": ["close"], "func": dsd_119_semi_dev_21d_below_sma63},
    "dsd_120_semi_dev_21d_above_sma200": {"inputs": ["close"], "func": dsd_120_semi_dev_21d_above_sma200},
    "dsd_121_semi_dev_bear_vs_bull_ratio_21d": {"inputs": ["close"], "func": dsd_121_semi_dev_bear_vs_bull_ratio_21d},
    "dsd_122_high_vol_regime_semi_dev_63d": {"inputs": ["close", "volume"], "func": dsd_122_high_vol_regime_semi_dev_63d},
    "dsd_123_low_vol_regime_semi_dev_63d": {"inputs": ["close", "volume"], "func": dsd_123_low_vol_regime_semi_dev_63d},
    "dsd_124_hi_vol_vs_lo_vol_semi_dev_ratio_63d": {"inputs": ["close", "volume"], "func": dsd_124_hi_vol_vs_lo_vol_semi_dev_ratio_63d},
    "dsd_125_gap_down_semi_dev_63d": {"inputs": ["close", "open"], "func": dsd_125_gap_down_semi_dev_63d},
    "dsd_126_semi_dev_expanding_mean": {"inputs": ["close"], "func": dsd_126_semi_dev_expanding_mean},
    "dsd_127_lpm2_vs0_expanding": {"inputs": ["close"], "func": dsd_127_lpm2_vs0_expanding},
    "dsd_128_semi_dev_504d": {"inputs": ["close"], "func": dsd_128_semi_dev_504d},
    "dsd_129_lpm1_vs0_504d": {"inputs": ["close"], "func": dsd_129_lpm1_vs0_504d},
    "dsd_130_semi_dev_21d_vs_504d_ratio": {"inputs": ["close"], "func": dsd_130_semi_dev_21d_vs_504d_ratio},
    "dsd_131_semi_dev_126d_vs_504d_ratio": {"inputs": ["close"], "func": dsd_131_semi_dev_126d_vs_504d_ratio},
    "dsd_132_expanding_semi_dev_pct_rank_10yr": {"inputs": ["close"], "func": dsd_132_expanding_semi_dev_pct_rank_10yr},
    "dsd_133_semi_dev_252d_vs_expanding_mean": {"inputs": ["close"], "func": dsd_133_semi_dev_252d_vs_expanding_mean},
    "dsd_134_lpm2_vs_mean_252d_vs_expanding": {"inputs": ["close"], "func": dsd_134_lpm2_vs_mean_252d_vs_expanding},
    "dsd_135_lpm3_vs0_252d_pct_rank_504d": {"inputs": ["close"], "func": dsd_135_lpm3_vs0_252d_pct_rank_504d},
    "dsd_136_semi_dev_composite_3window": {"inputs": ["close"], "func": dsd_136_semi_dev_composite_3window},
    "dsd_137_lpm_composite_3order": {"inputs": ["close"], "func": dsd_137_lpm_composite_3order},
    "dsd_138_downside_vol_zscore_composite": {"inputs": ["close"], "func": dsd_138_downside_vol_zscore_composite},
    "dsd_139_semi_dev_21d_gt_252d_flag": {"inputs": ["close"], "func": dsd_139_semi_dev_21d_gt_252d_flag},
    "dsd_140_semi_dev_63d_gt_252d_flag": {"inputs": ["close"], "func": dsd_140_semi_dev_63d_gt_252d_flag},
    "dsd_141_lpm1_composite_21_63_252": {"inputs": ["close"], "func": dsd_141_lpm1_composite_21_63_252},
    "dsd_142_semi_dev_vol_interaction_21d": {"inputs": ["close", "volume"], "func": dsd_142_semi_dev_vol_interaction_21d},
    "dsd_143_semi_dev_vol_interaction_63d": {"inputs": ["close", "volume"], "func": dsd_143_semi_dev_vol_interaction_63d},
    "dsd_144_lpm2_vs0_21d_vs_lpm2_mean_21d_ratio": {"inputs": ["close"], "func": dsd_144_lpm2_vs0_21d_vs_lpm2_mean_21d_ratio},
    "dsd_145_semi_dev_21d_ewm_div_21d_rolling": {"inputs": ["close"], "func": dsd_145_semi_dev_21d_ewm_div_21d_rolling},
    "dsd_146_semi_dev_expanding_zscore_21d": {"inputs": ["close"], "func": dsd_146_semi_dev_expanding_zscore_21d},
    "dsd_147_lpm2_expanding_zscore_63d": {"inputs": ["close"], "func": dsd_147_lpm2_expanding_zscore_63d},
    "dsd_148_semi_dev_21d_acceleration": {"inputs": ["close"], "func": dsd_148_semi_dev_21d_acceleration},
    "dsd_149_semi_dev_distress_index": {"inputs": ["close", "volume"], "func": dsd_149_semi_dev_distress_index},
    "dsd_150_semi_dev_21d_log": {"inputs": ["close"], "func": dsd_150_semi_dev_21d_log},
}
