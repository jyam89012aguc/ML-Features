"""
51_shadow_wick_analysis — Base Features 076-150
Domain: upper/lower wick (shadow) geometry — total wick fraction, wick ratios at price
        lows, wick-volume interaction, wick ratios on down days, wick body ratio,
        wick trend measures, wick consistency, rolling wick composites.
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _lower_wick(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick = distance from low to the lower of open/close."""
    body_low = pd.concat([open, close], axis=1).min(axis=1)
    return (body_low - low).clip(lower=0.0)


def _upper_wick(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper wick = distance from high to the upper of open/close."""
    body_high = pd.concat([open, close], axis=1).max(axis=1)
    return (high - body_high).clip(lower=0.0)


def _candle_range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Full high-low range of the candle."""
    return (high - low).clip(lower=_EPS)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Total wick and wick-as-fraction-of-range ---

def swk_076_total_wick_abs(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Total wick length (lower + upper) in price units."""
    return _lower_wick(open, high, low, close) + _upper_wick(open, high, low, close)


def swk_077_total_wick_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Total wick (lower + upper) as fraction of full range."""
    tw = swk_076_total_wick_abs(open, high, low, close)
    rng = _candle_range(high, low)
    return _safe_div(tw, rng)


def swk_078_total_wick_ratio_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of total-wick-to-range ratio."""
    twr = swk_077_total_wick_ratio(open, high, low, close)
    return _rolling_mean(twr, _TD_MON)


def swk_079_total_wick_ratio_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of total-wick-to-range ratio."""
    twr = swk_077_total_wick_ratio(open, high, low, close)
    return _rolling_mean(twr, _TD_QTR)


def swk_080_total_wick_ratio_sma252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling mean of total-wick-to-range ratio."""
    twr = swk_077_total_wick_ratio(open, high, low, close)
    return _rolling_mean(twr, _TD_YEAR)


def swk_081_total_wick_ratio_max_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling max of total-wick-to-range ratio."""
    twr = swk_077_total_wick_ratio(open, high, low, close)
    return _rolling_max(twr, _TD_QTR)


def swk_082_total_wick_ratio_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of total-wick ratio vs 252-day distribution."""
    twr = swk_077_total_wick_ratio(open, high, low, close)
    m = _rolling_mean(twr, _TD_YEAR)
    s = _rolling_std(twr, _TD_YEAR)
    return _safe_div(twr - m, s)


def swk_083_total_wick_pct_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of total-wick ratio in trailing 252 days."""
    twr = swk_077_total_wick_ratio(open, high, low, close)
    return twr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def swk_084_body_fraction_of_range(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Candle body as fraction of high-low range (complement of total-wick ratio)."""
    body = (close - open).abs()
    rng = _candle_range(high, low)
    return _safe_div(body, rng)


def swk_085_body_fraction_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of body-to-range ratio."""
    bf = swk_084_body_fraction_of_range(open, high, low, close)
    return _rolling_mean(bf, _TD_MON)


def swk_086_body_fraction_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of body-to-range ratio."""
    bf = swk_084_body_fraction_of_range(open, high, low, close)
    return _rolling_mean(bf, _TD_QTR)


def swk_087_lower_wick_to_body_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower wick length divided by body length (large = hammer/spinning-top)."""
    lw = _lower_wick(open, high, low, close)
    body = (close - open).abs().clip(lower=_EPS)
    return _safe_div(lw, body)


def swk_088_lower_wick_to_body_ratio_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of lower-wick-to-body ratio."""
    r = swk_087_lower_wick_to_body_ratio(open, high, low, close)
    return _rolling_mean(r, _TD_MON)


def swk_089_upper_wick_to_body_ratio(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper wick length divided by body length."""
    uw = _upper_wick(open, high, low, close)
    body = (close - open).abs().clip(lower=_EPS)
    return _safe_div(uw, body)


def swk_090_upper_wick_to_body_ratio_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of upper-wick-to-body ratio."""
    r = swk_089_upper_wick_to_body_ratio(open, high, low, close)
    return _rolling_mean(r, _TD_MON)


# --- Group G (091-105): Wick measures conditioned on price near lows ---

def swk_091_lower_wick_ratio_at_21d_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-wick ratio on days when close is at or near 21-day low (bottom quintile)."""
    rng21 = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    pos = _safe_div(close - _rolling_min(close, _TD_MON), rng21)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return lwr.where(pos <= 0.20, np.nan).ffill()


def swk_092_avg_lower_wick_ratio_near_21d_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean lower-wick ratio only on days in bottom 20% of 21-day price range."""
    rng21 = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    pos = _safe_div(close - _rolling_min(close, _TD_MON), rng21)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond_lwr = lwr.where(pos <= 0.20, np.nan)
    return cond_lwr.rolling(_TD_MON, min_periods=1).mean()


def swk_093_lower_wick_ratio_near_52wk_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-wick ratio EWM, restricted to days where close < 1.05 * 252-day low."""
    low252 = _rolling_min(close, _TD_YEAR)
    near_low = close < low252 * 1.05
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond_lwr = lwr.where(near_low, np.nan).ffill()
    return _ewm_mean(cond_lwr, _TD_MON)


def swk_094_wick_asym_near_52wk_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower/upper wick ratio EWM on days near 52-week low (< 1.05 * 252d low)."""
    low252 = _rolling_min(close, _TD_YEAR)
    near_low = close < low252 * 1.05
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    cond_asym = asym.where(near_low, np.nan).ffill()
    return _ewm_mean(cond_asym, _TD_MON)


def swk_095_long_lower_wick_at_21d_low_count_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day count of long-lower-wick days (ratio>0.33) while close is in bottom quintile."""
    rng21 = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    pos = _safe_div(close - _rolling_min(close, _TD_MON), rng21)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    flag = ((lwr > 0.33) & (pos <= 0.20)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def swk_096_lower_wick_ratio_below_sma21_days(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean lower-wick ratio only on days where close < 21-day SMA."""
    sma21 = _rolling_mean(close, _TD_MON)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond_lwr = lwr.where(close < sma21, np.nan)
    return cond_lwr.rolling(_TD_MON, min_periods=1).mean()


def swk_097_lower_wick_ratio_below_sma200_days(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day mean lower-wick ratio only on days where close < 200-day SMA."""
    sma200 = _rolling_mean(close, 200)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond_lwr = lwr.where(close < sma200, np.nan)
    return cond_lwr.rolling(_TD_QTR, min_periods=1).mean()


def swk_098_lower_wick_ratio_on_down_days(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean lower-wick ratio on down-close days only."""
    ret = close.pct_change(1)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond_lwr = lwr.where(ret < 0, np.nan)
    return cond_lwr.rolling(_TD_MON, min_periods=1).mean()


def swk_099_lower_wick_ratio_on_up_days(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean lower-wick ratio on up-close days only."""
    ret = close.pct_change(1)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond_lwr = lwr.where(ret > 0, np.nan)
    return cond_lwr.rolling(_TD_MON, min_periods=1).mean()


def swk_100_lower_wick_down_vs_up_ratio_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21d avg lower-wick ratio on down days to that on up days."""
    dn = swk_098_lower_wick_ratio_on_down_days(open, high, low, close)
    up = swk_099_lower_wick_ratio_on_up_days(open, high, low, close)
    return _safe_div(dn, up.clip(lower=_EPS))


def swk_101_upper_wick_ratio_on_down_days(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean upper-wick ratio on down-close days (resistance overhead)."""
    ret = close.pct_change(1)
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    cond_uwr = uwr.where(ret < 0, np.nan)
    return cond_uwr.rolling(_TD_MON, min_periods=1).mean()


def swk_102_upper_wick_ratio_on_up_days(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean upper-wick ratio on up-close days (bearish rejection of gains)."""
    ret = close.pct_change(1)
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    cond_uwr = uwr.where(ret > 0, np.nan)
    return cond_uwr.rolling(_TD_MON, min_periods=1).mean()


def swk_103_wick_asym_on_down_days_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean lower/upper wick ratio on down-close days."""
    ret = close.pct_change(1)
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    cond_asym = asym.where(ret < 0, np.nan)
    return cond_asym.rolling(_TD_MON, min_periods=1).mean()


def swk_104_wick_asym_on_up_days_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean lower/upper wick ratio on up-close days."""
    ret = close.pct_change(1)
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    cond_asym = asym.where(ret > 0, np.nan)
    return cond_asym.rolling(_TD_MON, min_periods=1).mean()


def swk_105_lower_wick_ratio_at_63d_low(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day mean lower-wick ratio on days where close is in bottom 20% of 63-day range."""
    rng63 = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR), rng63)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond_lwr = lwr.where(pos <= 0.20, np.nan)
    return cond_lwr.rolling(_TD_QTR, min_periods=1).mean()


# --- Group H (106-120): Volume-weighted wick measures ---

def swk_106_vol_weighted_lower_wick_ratio_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume-weighted average lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    vwlwr = lwr * volume
    return _safe_div(_rolling_sum(vwlwr, _TD_MON), _rolling_sum(volume, _TD_MON))


def swk_107_vol_weighted_lower_wick_ratio_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day volume-weighted average lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    vwlwr = lwr * volume
    return _safe_div(_rolling_sum(vwlwr, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def swk_108_vol_weighted_upper_wick_ratio_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume-weighted average upper-wick ratio."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    vwuwr = uwr * volume
    return _safe_div(_rolling_sum(vwuwr, _TD_MON), _rolling_sum(volume, _TD_MON))


def swk_109_high_vol_long_lower_wick_count_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day count of high-volume long-lower-wick days (ratio>0.33 AND vol>21d avg)."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    flag = ((lwr > 0.33) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def swk_110_high_vol_long_lower_wick_count_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day count of high-volume long-lower-wick days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    flag = ((lwr > 0.33) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def swk_111_lower_wick_times_vol_norm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day sum of lower-wick ratio times volume-normalized (rejection intensity)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return _rolling_sum(lwr * vol_norm, _TD_MON)


def swk_112_lower_wick_times_vol_norm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day sum of lower-wick ratio times volume-normalized."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    return _rolling_sum(lwr * vol_norm, _TD_QTR)


def swk_113_consec_long_lower_wick_high_vol(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current streak: long lower wick (>0.33) AND above-21d-avg volume simultaneously."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond = (lwr > 0.33) & (volume > avg_vol)
    return _consec_streak(cond)


def swk_114_avg_lower_wick_ratio_on_high_vol_days(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day avg lower-wick ratio on high-volume days (vol > 21d avg)."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond_lwr = lwr.where(volume > avg_vol, np.nan)
    return cond_lwr.rolling(_TD_MON, min_periods=1).mean()


def swk_115_avg_lower_wick_ratio_on_low_vol_days(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day avg lower-wick ratio on low-volume days (vol < 21d avg)."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond_lwr = lwr.where(volume < avg_vol, np.nan)
    return cond_lwr.rolling(_TD_MON, min_periods=1).mean()


# --- Group I (116-135): Wick regime level, percentile, and structural state ---

def swk_116_lower_wick_ratio_pct_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's lower-wick ratio within its trailing 63-day distribution."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return lwr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def swk_117_lower_wick_ratio_pct_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's lower-wick ratio within its trailing 126-day distribution."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return lwr.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def swk_118_upper_wick_ratio_pct_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's upper-wick ratio within its trailing 63-day distribution."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    return uwr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def swk_119_upper_wick_ratio_pct_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's upper-wick ratio within its trailing 126-day distribution."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    return uwr.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def swk_120_wick_asym_pct_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's lower/upper wick asymmetry within its 63-day distribution."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    return asym.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def swk_121_wick_asym_pct_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's lower/upper wick asymmetry within its 252-day distribution."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    return asym.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def swk_122_lower_wick_sma21_vs_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day SMA lower-wick ratio to 63-day SMA (short vs medium trend)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sma21 = _rolling_mean(lwr, _TD_MON)
    sma63 = _rolling_mean(lwr, _TD_QTR)
    return _safe_div(sma21, sma63)


def swk_123_lower_wick_sma21_vs_sma252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day SMA lower-wick ratio to 252-day SMA (short vs long trend)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    sma21 = _rolling_mean(lwr, _TD_MON)
    sma252 = _rolling_mean(lwr, _TD_YEAR)
    return _safe_div(sma21, sma252)


def swk_124_upper_wick_sma21_vs_sma63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day SMA upper-wick ratio to 63-day SMA."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    sma21 = _rolling_mean(uwr, _TD_MON)
    sma63 = _rolling_mean(uwr, _TD_QTR)
    return _safe_div(sma21, sma63)


def swk_125_lower_wick_ewm21_vs_ewm63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of EWM21 to EWM63 of lower-wick ratio (short vs medium EWM trend)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    e21 = _ewm_mean(lwr, _TD_MON)
    e63 = _ewm_mean(lwr, _TD_QTR)
    return _safe_div(e21, e63)


def swk_126_lower_wick_ratio_above_sma21_flag(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: today's lower-wick ratio exceeds its own 21-day SMA."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return (lwr > _rolling_mean(lwr, _TD_MON)).astype(float)


def swk_127_lower_wick_consec_above_sma21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Streak: lower-wick ratio consecutively above its 21-day SMA."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    cond = lwr > _rolling_mean(lwr, _TD_MON)
    return _consec_streak(cond)


def swk_128_lower_wick_ratio_std_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling std of lower-wick ratio (wick consistency; low = stable rejection)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return _rolling_std(lwr, _TD_MON)


def swk_129_lower_wick_ratio_std_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling std of lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return _rolling_std(lwr, _TD_QTR)


def swk_130_lower_wick_ratio_cv_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of lower-wick ratio over 63 days."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    m = _rolling_mean(lwr, _TD_QTR)
    s = _rolling_std(lwr, _TD_QTR)
    return _safe_div(s, m.clip(lower=_EPS))


def swk_131_lower_wick_ratio_min_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling minimum lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return _rolling_min(lwr, _TD_MON)


def swk_132_lower_wick_ratio_min_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling minimum lower-wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return _rolling_min(lwr, _TD_QTR)


def swk_133_upper_wick_ratio_std_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling std of upper-wick ratio."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    return _rolling_std(uwr, _TD_QTR)


def swk_134_wick_asym_std_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling std of lower/upper wick ratio (consistency of rejection signal)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    return _rolling_std(asym, _TD_QTR)


def swk_135_lower_wick_ratio_range_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day range (max - min) of lower-wick ratio (intra-period variability)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return _rolling_max(lwr, _TD_MON) - _rolling_min(lwr, _TD_MON)


# --- Group J (136-150): Composite, conditional, and cross-wick features ---

def swk_136_wick_composite_score_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: avg of normalized lower-wick ratio, wick-asymmetry, and long-wick freq."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close).clip(lower=_EPS)
    asym = lw / uw
    long_flag = (lwr > 0.33).astype(float)
    lwr_n = _safe_div(lwr, _rolling_mean(lwr, _TD_YEAR).clip(lower=_EPS))
    asym_n = _safe_div(asym, _rolling_mean(asym, _TD_YEAR).clip(lower=_EPS))
    freq_n = _safe_div(_rolling_mean(long_flag, _TD_MON),
                       _rolling_mean(long_flag, _TD_YEAR).clip(lower=_EPS))
    return (lwr_n + asym_n + freq_n) / 3.0


def swk_137_lower_wick_ratio_rolling_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling skewness of lower-wick ratio distribution."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return lwr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).skew()


def swk_138_hammer_day_flag(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: classic hammer pattern (lower wick >2x body AND close > open AND small upper wick)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    body = (close - open).abs().clip(lower=_EPS)
    rng = _candle_range(high, low)
    cond = (lw > 2.0 * body) & (close >= open) & (_safe_div(uw, rng) < 0.10)
    return cond.astype(float)


def swk_139_hammer_count_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day count of hammer days (classic hammer pattern)."""
    flag = swk_138_hammer_day_flag(open, high, low, close)
    return _rolling_sum(flag, _TD_MON)


def swk_140_hammer_count_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day count of hammer days."""
    flag = swk_138_hammer_day_flag(open, high, low, close)
    return _rolling_sum(flag, _TD_QTR)


def swk_141_inverted_hammer_flag(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: inverted hammer (upper wick > 2x body AND small lower wick)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    body = (close - open).abs().clip(lower=_EPS)
    rng = _candle_range(high, low)
    cond = (uw > 2.0 * body) & (_safe_div(lw, rng) < 0.10)
    return cond.astype(float)


def swk_142_inverted_hammer_count_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day count of inverted hammer days."""
    flag = swk_141_inverted_hammer_flag(open, high, low, close)
    return _rolling_sum(flag, _TD_MON)


def swk_143_shooting_star_flag(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: shooting star (upper wick > 2x body, close <= open, small lower wick)."""
    lw = _lower_wick(open, high, low, close)
    uw = _upper_wick(open, high, low, close)
    body = (close - open).abs().clip(lower=_EPS)
    rng = _candle_range(high, low)
    cond = (uw > 2.0 * body) & (close <= open) & (_safe_div(lw, rng) < 0.10)
    return cond.astype(float)


def swk_144_shooting_star_count_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day count of shooting star days."""
    flag = swk_143_shooting_star_flag(open, high, low, close)
    return _rolling_sum(flag, _TD_MON)


def swk_145_lower_wick_ratio_pct_rank_vs_1yr(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-wick ratio vs its own 252-day rolling mean (normalized deviation)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    m252 = _rolling_mean(lwr, _TD_YEAR)
    return _safe_div(lwr, m252.clip(lower=_EPS))


def swk_146_lower_wick_sum_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day cumulative sum of lower wick ratio (total rejection over period)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return _rolling_sum(lwr, _TD_MON)


def swk_147_lower_wick_sum_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day cumulative sum of lower wick ratio."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    return _rolling_sum(lwr, _TD_QTR)


def swk_148_upper_wick_sum_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day cumulative sum of upper wick ratio."""
    uwr = _safe_div(_upper_wick(open, high, low, close), _candle_range(high, low))
    return _rolling_sum(uwr, _TD_MON)


def swk_149_lower_over_upper_wick_sum_ratio_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21d sum of lower-wick ratio to 21d sum of upper-wick ratio."""
    lwr_sum = swk_146_lower_wick_sum_21d(open, high, low, close)
    uwr_sum = swk_148_upper_wick_sum_21d(open, high, low, close)
    return _safe_div(lwr_sum, uwr_sum.clip(lower=_EPS))


def swk_150_lower_wick_ratio_ema_cross_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM21 minus EWM63 of lower-wick ratio (momentum of rejection signal)."""
    lwr = _safe_div(_lower_wick(open, high, low, close), _candle_range(high, low))
    e21 = _ewm_mean(lwr, _TD_MON)
    e63 = _ewm_mean(lwr, _TD_QTR)
    return e21 - e63


# ── Registry ──────────────────────────────────────────────────────────────────

SHADOW_WICK_ANALYSIS_REGISTRY_076_150 = {
    "swk_076_total_wick_abs": {"inputs": ["open", "high", "low", "close"], "func": swk_076_total_wick_abs},
    "swk_077_total_wick_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_077_total_wick_ratio},
    "swk_078_total_wick_ratio_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_078_total_wick_ratio_sma21},
    "swk_079_total_wick_ratio_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_079_total_wick_ratio_sma63},
    "swk_080_total_wick_ratio_sma252": {"inputs": ["open", "high", "low", "close"], "func": swk_080_total_wick_ratio_sma252},
    "swk_081_total_wick_ratio_max_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_081_total_wick_ratio_max_63d},
    "swk_082_total_wick_ratio_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_082_total_wick_ratio_zscore_252d},
    "swk_083_total_wick_pct_rank_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_083_total_wick_pct_rank_252d},
    "swk_084_body_fraction_of_range": {"inputs": ["open", "high", "low", "close"], "func": swk_084_body_fraction_of_range},
    "swk_085_body_fraction_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_085_body_fraction_sma21},
    "swk_086_body_fraction_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_086_body_fraction_sma63},
    "swk_087_lower_wick_to_body_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_087_lower_wick_to_body_ratio},
    "swk_088_lower_wick_to_body_ratio_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_088_lower_wick_to_body_ratio_sma21},
    "swk_089_upper_wick_to_body_ratio": {"inputs": ["open", "high", "low", "close"], "func": swk_089_upper_wick_to_body_ratio},
    "swk_090_upper_wick_to_body_ratio_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_090_upper_wick_to_body_ratio_sma21},
    "swk_091_lower_wick_ratio_at_21d_low": {"inputs": ["open", "high", "low", "close"], "func": swk_091_lower_wick_ratio_at_21d_low},
    "swk_092_avg_lower_wick_ratio_near_21d_low": {"inputs": ["open", "high", "low", "close"], "func": swk_092_avg_lower_wick_ratio_near_21d_low},
    "swk_093_lower_wick_ratio_near_52wk_low": {"inputs": ["open", "high", "low", "close"], "func": swk_093_lower_wick_ratio_near_52wk_low},
    "swk_094_wick_asym_near_52wk_low": {"inputs": ["open", "high", "low", "close"], "func": swk_094_wick_asym_near_52wk_low},
    "swk_095_long_lower_wick_at_21d_low_count_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_095_long_lower_wick_at_21d_low_count_63d},
    "swk_096_lower_wick_ratio_below_sma21_days": {"inputs": ["open", "high", "low", "close"], "func": swk_096_lower_wick_ratio_below_sma21_days},
    "swk_097_lower_wick_ratio_below_sma200_days": {"inputs": ["open", "high", "low", "close"], "func": swk_097_lower_wick_ratio_below_sma200_days},
    "swk_098_lower_wick_ratio_on_down_days": {"inputs": ["open", "high", "low", "close"], "func": swk_098_lower_wick_ratio_on_down_days},
    "swk_099_lower_wick_ratio_on_up_days": {"inputs": ["open", "high", "low", "close"], "func": swk_099_lower_wick_ratio_on_up_days},
    "swk_100_lower_wick_down_vs_up_ratio_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_100_lower_wick_down_vs_up_ratio_21d},
    "swk_101_upper_wick_ratio_on_down_days": {"inputs": ["open", "high", "low", "close"], "func": swk_101_upper_wick_ratio_on_down_days},
    "swk_102_upper_wick_ratio_on_up_days": {"inputs": ["open", "high", "low", "close"], "func": swk_102_upper_wick_ratio_on_up_days},
    "swk_103_wick_asym_on_down_days_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_103_wick_asym_on_down_days_21d},
    "swk_104_wick_asym_on_up_days_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_104_wick_asym_on_up_days_21d},
    "swk_105_lower_wick_ratio_at_63d_low": {"inputs": ["open", "high", "low", "close"], "func": swk_105_lower_wick_ratio_at_63d_low},
    "swk_106_vol_weighted_lower_wick_ratio_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_106_vol_weighted_lower_wick_ratio_21d},
    "swk_107_vol_weighted_lower_wick_ratio_63d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_107_vol_weighted_lower_wick_ratio_63d},
    "swk_108_vol_weighted_upper_wick_ratio_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_108_vol_weighted_upper_wick_ratio_21d},
    "swk_109_high_vol_long_lower_wick_count_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_109_high_vol_long_lower_wick_count_21d},
    "swk_110_high_vol_long_lower_wick_count_63d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_110_high_vol_long_lower_wick_count_63d},
    "swk_111_lower_wick_times_vol_norm_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_111_lower_wick_times_vol_norm_21d},
    "swk_112_lower_wick_times_vol_norm_63d": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_112_lower_wick_times_vol_norm_63d},
    "swk_113_consec_long_lower_wick_high_vol": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_113_consec_long_lower_wick_high_vol},
    "swk_114_avg_lower_wick_ratio_on_high_vol_days": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_114_avg_lower_wick_ratio_on_high_vol_days},
    "swk_115_avg_lower_wick_ratio_on_low_vol_days": {"inputs": ["open", "high", "low", "close", "volume"], "func": swk_115_avg_lower_wick_ratio_on_low_vol_days},
    "swk_116_lower_wick_ratio_pct_rank_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_116_lower_wick_ratio_pct_rank_63d},
    "swk_117_lower_wick_ratio_pct_rank_126d": {"inputs": ["open", "high", "low", "close"], "func": swk_117_lower_wick_ratio_pct_rank_126d},
    "swk_118_upper_wick_ratio_pct_rank_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_118_upper_wick_ratio_pct_rank_63d},
    "swk_119_upper_wick_ratio_pct_rank_126d": {"inputs": ["open", "high", "low", "close"], "func": swk_119_upper_wick_ratio_pct_rank_126d},
    "swk_120_wick_asym_pct_rank_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_120_wick_asym_pct_rank_63d},
    "swk_121_wick_asym_pct_rank_252d": {"inputs": ["open", "high", "low", "close"], "func": swk_121_wick_asym_pct_rank_252d},
    "swk_122_lower_wick_sma21_vs_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_122_lower_wick_sma21_vs_sma63},
    "swk_123_lower_wick_sma21_vs_sma252": {"inputs": ["open", "high", "low", "close"], "func": swk_123_lower_wick_sma21_vs_sma252},
    "swk_124_upper_wick_sma21_vs_sma63": {"inputs": ["open", "high", "low", "close"], "func": swk_124_upper_wick_sma21_vs_sma63},
    "swk_125_lower_wick_ewm21_vs_ewm63": {"inputs": ["open", "high", "low", "close"], "func": swk_125_lower_wick_ewm21_vs_ewm63},
    "swk_126_lower_wick_ratio_above_sma21_flag": {"inputs": ["open", "high", "low", "close"], "func": swk_126_lower_wick_ratio_above_sma21_flag},
    "swk_127_lower_wick_consec_above_sma21": {"inputs": ["open", "high", "low", "close"], "func": swk_127_lower_wick_consec_above_sma21},
    "swk_128_lower_wick_ratio_std_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_128_lower_wick_ratio_std_21d},
    "swk_129_lower_wick_ratio_std_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_129_lower_wick_ratio_std_63d},
    "swk_130_lower_wick_ratio_cv_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_130_lower_wick_ratio_cv_63d},
    "swk_131_lower_wick_ratio_min_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_131_lower_wick_ratio_min_21d},
    "swk_132_lower_wick_ratio_min_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_132_lower_wick_ratio_min_63d},
    "swk_133_upper_wick_ratio_std_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_133_upper_wick_ratio_std_63d},
    "swk_134_wick_asym_std_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_134_wick_asym_std_63d},
    "swk_135_lower_wick_ratio_range_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_135_lower_wick_ratio_range_21d},
    "swk_136_wick_composite_score_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_136_wick_composite_score_21d},
    "swk_137_lower_wick_ratio_rolling_skew_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_137_lower_wick_ratio_rolling_skew_63d},
    "swk_138_hammer_day_flag": {"inputs": ["open", "high", "low", "close"], "func": swk_138_hammer_day_flag},
    "swk_139_hammer_count_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_139_hammer_count_21d},
    "swk_140_hammer_count_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_140_hammer_count_63d},
    "swk_141_inverted_hammer_flag": {"inputs": ["open", "high", "low", "close"], "func": swk_141_inverted_hammer_flag},
    "swk_142_inverted_hammer_count_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_142_inverted_hammer_count_21d},
    "swk_143_shooting_star_flag": {"inputs": ["open", "high", "low", "close"], "func": swk_143_shooting_star_flag},
    "swk_144_shooting_star_count_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_144_shooting_star_count_21d},
    "swk_145_lower_wick_ratio_pct_rank_vs_1yr": {"inputs": ["open", "high", "low", "close"], "func": swk_145_lower_wick_ratio_pct_rank_vs_1yr},
    "swk_146_lower_wick_sum_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_146_lower_wick_sum_21d},
    "swk_147_lower_wick_sum_63d": {"inputs": ["open", "high", "low", "close"], "func": swk_147_lower_wick_sum_63d},
    "swk_148_upper_wick_sum_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_148_upper_wick_sum_21d},
    "swk_149_lower_over_upper_wick_sum_ratio_21d": {"inputs": ["open", "high", "low", "close"], "func": swk_149_lower_over_upper_wick_sum_ratio_21d},
    "swk_150_lower_wick_ratio_ema_cross_signal": {"inputs": ["open", "high", "low", "close"], "func": swk_150_lower_wick_ratio_ema_cross_signal},
}
