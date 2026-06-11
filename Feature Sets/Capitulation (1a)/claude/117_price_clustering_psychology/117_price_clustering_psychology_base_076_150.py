"""
117_price_clustering_psychology — Base Features 076-150
Domain: price-level psychology and digit clustering — proximity to and clustering at round
        numbers (whole dollars, $5/$10 increments), trailing-digit preference, behaviour and
        pinning near psychological round levels, absolute price-level distress zones (sub-$5,
        sub-$1 penny-stock thresholds), fraction of recent closes at round levels, distance to
        the nearest round number.
Includes: open-price clustering, high/low clustering, cross-series round-level confluence,
          volume-at-round-level proxies, additional distress zone dynamics.
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _dist_to_round(price: pd.Series, increment: float) -> pd.Series:
    """Absolute distance from price to the nearest multiple of increment."""
    mod = price % increment
    down = mod
    up = increment - mod
    return np.minimum(down, up)


def _frac_near_round(price: pd.Series, increment: float, tol: float,
                     window: int) -> pd.Series:
    """Rolling fraction of bars where price is within tol of a round increment."""
    near = (_dist_to_round(price, increment) <= tol).astype(float)
    return _rolling_sum(near, window) / window


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Open-price round-level clustering ---

def pcp_076_open_dist_to_nearest_dollar(open: pd.Series) -> pd.Series:
    """Absolute distance from open to nearest whole-dollar level."""
    return _dist_to_round(open, 1.0)


def pcp_077_open_dist_to_nearest_dollar_pct(open: pd.Series) -> pd.Series:
    """Open distance to nearest whole dollar as fraction of open."""
    return _safe_div(_dist_to_round(open, 1.0), open.clip(lower=_EPS))


def pcp_078_open_at_whole_dollar_flag(open: pd.Series) -> pd.Series:
    """Binary flag: open is within $0.05 of a whole-dollar level."""
    return (_dist_to_round(open, 1.0) <= 0.05).astype(float)


def pcp_079_open_dist_to_nearest_5dollar(open: pd.Series) -> pd.Series:
    """Absolute distance from open to nearest $5 level."""
    return _dist_to_round(open, 5.0)


def pcp_080_open_dist_to_nearest_10dollar(open: pd.Series) -> pd.Series:
    """Absolute distance from open to nearest $10 level."""
    return _dist_to_round(open, 10.0)


def pcp_081_open_sub5_flag(open: pd.Series) -> pd.Series:
    """Binary flag: open < $5.00."""
    return (open < 5.0).astype(float)


def pcp_082_open_sub1_flag(open: pd.Series) -> pd.Series:
    """Binary flag: open < $1.00."""
    return (open < 1.0).astype(float)


def pcp_083_frac_open_near_dollar_21d(open: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days open within $0.05 of a whole dollar."""
    return _frac_near_round(open, 1.0, 0.05, _TD_MON)


def pcp_084_open_cents_digit(open: pd.Series) -> pd.Series:
    """Cents component of open (trailing-digit clustering proxy)."""
    return open % 1.0


def pcp_085_open_trailing_zero_flag(open: pd.Series) -> pd.Series:
    """Binary flag: open cents component < $0.05 (round-zero pinning at open)."""
    return (open % 1.0 < 0.05).astype(float)


# --- Group I (086-095): High/low round-level clustering ---

def pcp_086_high_dist_to_nearest_dollar(high: pd.Series) -> pd.Series:
    """Absolute distance from high to nearest whole-dollar level."""
    return _dist_to_round(high, 1.0)


def pcp_087_high_dist_to_nearest_5dollar(high: pd.Series) -> pd.Series:
    """Absolute distance from high to nearest $5 level."""
    return _dist_to_round(high, 5.0)


def pcp_088_high_at_whole_dollar_flag(high: pd.Series) -> pd.Series:
    """Binary flag: high is within $0.05 of a whole-dollar level (resistance pinning)."""
    return (_dist_to_round(high, 1.0) <= 0.05).astype(float)


def pcp_089_low_dist_to_nearest_dollar(low: pd.Series) -> pd.Series:
    """Absolute distance from low to nearest whole-dollar level."""
    return _dist_to_round(low, 1.0)


def pcp_090_low_dist_to_nearest_5dollar(low: pd.Series) -> pd.Series:
    """Absolute distance from low to nearest $5 level."""
    return _dist_to_round(low, 5.0)


def pcp_091_low_at_whole_dollar_flag(low: pd.Series) -> pd.Series:
    """Binary flag: low is within $0.05 of a whole-dollar level (support pinning)."""
    return (_dist_to_round(low, 1.0) <= 0.05).astype(float)


def pcp_092_low_at_5dollar_flag(low: pd.Series) -> pd.Series:
    """Binary flag: low is within $0.10 of a $5 level."""
    return (_dist_to_round(low, 5.0) <= 0.10).astype(float)


def pcp_093_high_cents_digit(high: pd.Series) -> pd.Series:
    """Cents component of high (trailing-digit clustering proxy for intraday high)."""
    return high % 1.0


def pcp_094_low_cents_digit(low: pd.Series) -> pd.Series:
    """Cents component of low (trailing-digit clustering proxy for intraday low)."""
    return low % 1.0


def pcp_095_frac_low_near_dollar_21d(low: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days low within $0.05 of a whole dollar."""
    return _frac_near_round(low, 1.0, 0.05, _TD_MON)


# --- Group J (096-105): Cross-series round-level confluence ---

def pcp_096_open_close_both_near_dollar_flag(open: pd.Series,
                                              close: pd.Series) -> pd.Series:
    """Binary flag: both open and close are within $0.05 of a whole dollar."""
    o_near = (_dist_to_round(open, 1.0) <= 0.05)
    c_near = (_dist_to_round(close, 1.0) <= 0.05)
    return (o_near & c_near).astype(float)


def pcp_097_high_low_both_near_dollar_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: both high and low are within $0.05 of a whole dollar."""
    h_near = (_dist_to_round(high, 1.0) <= 0.05)
    l_near = (_dist_to_round(low, 1.0) <= 0.05)
    return (h_near & l_near).astype(float)


def pcp_098_all_four_near_dollar_flag(open: pd.Series, high: pd.Series,
                                       low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: open, high, low, close all within $0.05 of a whole dollar."""
    return (
        (_dist_to_round(open, 1.0) <= 0.05) &
        (_dist_to_round(high, 1.0) <= 0.05) &
        (_dist_to_round(low, 1.0) <= 0.05) &
        (_dist_to_round(close, 1.0) <= 0.05)
    ).astype(float)


def pcp_099_close_below_open_round_flag(open: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: close < floor whole dollar of open (broke round level from open)."""
    open_floor = (open / 1.0).apply(np.floor) * 1.0
    return (close < open_floor).astype(float)


def pcp_100_open_close_same_dollar_zone_flag(open: pd.Series,
                                              close: pd.Series) -> pd.Series:
    """Binary flag: open and close are in the same whole-dollar zone."""
    return ((open.apply(np.floor) == close.apply(np.floor))).astype(float)


def pcp_101_frac_open_close_near_dollar_21d(open: pd.Series,
                                             close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days both open and close within $0.05 of a dollar."""
    flag = (
        (_dist_to_round(open, 1.0) <= 0.05) &
        (_dist_to_round(close, 1.0) <= 0.05)
    ).astype(float)
    return _rolling_sum(flag, _TD_MON) / _TD_MON


def pcp_102_close_dist_dollar_vs_open_dist_dollar(open: pd.Series,
                                                   close: pd.Series) -> pd.Series:
    """Difference: close distance to nearest dollar minus open distance to nearest dollar."""
    return _dist_to_round(close, 1.0) - _dist_to_round(open, 1.0)


def pcp_103_high_at_5dollar_flag(high: pd.Series) -> pd.Series:
    """Binary flag: high is within $0.10 of a $5 level."""
    return (_dist_to_round(high, 5.0) <= 0.10).astype(float)


def pcp_104_open_close_both_sub5_flag(open: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: both open and close are below $5 (deep distress)."""
    return ((open < 5.0) & (close < 5.0)).astype(float)


def pcp_105_high_sub5_flag(high: pd.Series) -> pd.Series:
    """Binary flag: intraday high still below $5 (no recovery above distress level)."""
    return (high < 5.0).astype(float)


# --- Group K (106-115): Volume around round levels (volume-at-price proxies) ---

def pcp_106_vol_on_near_dollar_days_21d(close: pd.Series,
                                         volume: pd.Series) -> pd.Series:
    """Sum of volume on days close was within $0.05 of a whole dollar (trailing 21d)."""
    near = (_dist_to_round(close, 1.0) <= 0.05).astype(float)
    return _rolling_sum(near * volume, _TD_MON)


def pcp_107_vol_on_sub5_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on days close < $5 (trailing 21d)."""
    flag = (close < 5.0).astype(float)
    return _rolling_sum(flag * volume, _TD_MON)


def pcp_108_vol_on_sub5_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on days close < $5 (trailing 63d)."""
    flag = (close < 5.0).astype(float)
    return _rolling_sum(flag * volume, _TD_QTR)


def pcp_109_vol_fraction_near_dollar_21d(close: pd.Series,
                                          volume: pd.Series) -> pd.Series:
    """Fraction of total volume occurring on near-dollar days (trailing 21d)."""
    near = (_dist_to_round(close, 1.0) <= 0.05).astype(float)
    vol_near = _rolling_sum(near * volume, _TD_MON)
    vol_total = _rolling_sum(volume, _TD_MON)
    return _safe_div(vol_near, vol_total.clip(lower=_EPS))


def pcp_110_vol_fraction_sub5_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total volume occurring on sub-$5 days (trailing 21d)."""
    flag = (close < 5.0).astype(float)
    vol_flag = _rolling_sum(flag * volume, _TD_MON)
    vol_total = _rolling_sum(volume, _TD_MON)
    return _safe_div(vol_flag, vol_total.clip(lower=_EPS))


def pcp_111_vol_fraction_sub10_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total volume occurring on sub-$10 days (trailing 21d)."""
    flag = (close < 10.0).astype(float)
    vol_flag = _rolling_sum(flag * volume, _TD_MON)
    vol_total = _rolling_sum(volume, _TD_MON)
    return _safe_div(vol_flag, vol_total.clip(lower=_EPS))


def pcp_112_avg_vol_near_dollar_vs_overall(close: pd.Series,
                                            volume: pd.Series) -> pd.Series:
    """Average volume on near-dollar days divided by overall 21d avg volume."""
    near = (_dist_to_round(close, 1.0) <= 0.05).astype(float)
    avg_near = _safe_div(_rolling_sum(near * volume, _TD_MON),
                         _rolling_sum(near, _TD_MON).clip(lower=_EPS))
    avg_all = _rolling_mean(volume, _TD_MON)
    return _safe_div(avg_near, avg_all.clip(lower=_EPS))


def pcp_113_vol_on_sub1_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on days close < $1 (trailing 63d — penny-stock desperation)."""
    flag = (close < 1.0).astype(float)
    return _rolling_sum(flag * volume, _TD_QTR)


def pcp_114_vol_near_5dollar_fraction_63d(close: pd.Series,
                                           volume: pd.Series) -> pd.Series:
    """Fraction of 63-day volume on days close within $0.10 of $5 level."""
    near = (_dist_to_round(close, 5.0) <= 0.10).astype(float)
    vol_near = _rolling_sum(near * volume, _TD_QTR)
    vol_total = _rolling_sum(volume, _TD_QTR)
    return _safe_div(vol_near, vol_total.clip(lower=_EPS))


def pcp_115_vol_on_at_5dollar_flag_days_252d(close: pd.Series,
                                              volume: pd.Series) -> pd.Series:
    """Sum of volume on days close within $0.05 of the $5 level (trailing 252d)."""
    near = (close.sub(5.0).abs() <= 0.05).astype(float)
    return _rolling_sum(near * volume, _TD_YEAR)


# --- Group L (116-125): Dollar-zone retention and crossing dynamics ---

def pcp_116_days_since_close_crossed_above_5dollar(close: pd.Series) -> pd.Series:
    """Days since close last crossed upward through $5 (0 = crossed today)."""
    crossed = ((close >= 5.0) & (close.shift(1) < 5.0)).astype(float)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_cross = idx.where(crossed == 1.0).ffill().fillna(0.0)
    return (idx - last_cross).where(~close.isna(), np.nan)


def pcp_117_days_since_close_crossed_below_5dollar(close: pd.Series) -> pd.Series:
    """Days since close last crossed downward through $5 (0 = crossed today)."""
    crossed = ((close < 5.0) & (close.shift(1) >= 5.0)).astype(float)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_cross = idx.where(crossed == 1.0).ffill().fillna(0.0)
    return (idx - last_cross).where(~close.isna(), np.nan)


def pcp_118_days_since_close_crossed_below_10dollar(close: pd.Series) -> pd.Series:
    """Days since close last crossed downward through $10."""
    crossed = ((close < 10.0) & (close.shift(1) >= 10.0)).astype(float)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_cross = idx.where(crossed == 1.0).ffill().fillna(0.0)
    return (idx - last_cross).where(~close.isna(), np.nan)


def pcp_119_days_since_close_crossed_below_1dollar(close: pd.Series) -> pd.Series:
    """Days since close last crossed downward through $1."""
    crossed = ((close < 1.0) & (close.shift(1) >= 1.0)).astype(float)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_cross = idx.where(crossed == 1.0).ffill().fillna(0.0)
    return (idx - last_cross).where(~close.isna(), np.nan)


def pcp_120_dollar_zone_flag_change(close: pd.Series) -> pd.Series:
    """Binary flag: close crossed into a new whole-dollar zone from prior bar."""
    return (close.apply(np.floor) != close.shift(1).apply(np.floor)).astype(float)


def pcp_121_5dollar_zone_flag_change(close: pd.Series) -> pd.Series:
    """Binary flag: close crossed into a new $5 zone from prior bar."""
    return ((close / 5.0).apply(np.floor) != (close.shift(1) / 5.0).apply(np.floor)).astype(float)


def pcp_122_consec_days_same_dollar_zone(close: pd.Series) -> pd.Series:
    """Consecutive days close has stayed in the same whole-dollar zone."""
    same_zone = (close.apply(np.floor) == close.shift(1).apply(np.floor))
    same_zone.iloc[0] = False
    return _consec_streak(same_zone)


def pcp_123_dollar_zone_descent_streak(close: pd.Series) -> pd.Series:
    """Consecutive days close has fallen to a strictly lower whole-dollar zone."""
    lower = (close.apply(np.floor) < close.shift(1).apply(np.floor))
    lower.iloc[0] = False
    return _consec_streak(lower)


def pcp_124_5dollar_zone_descent_streak(close: pd.Series) -> pd.Series:
    """Consecutive days close has fallen to a strictly lower $5 zone."""
    lower = ((close / 5.0).apply(np.floor) < (close.shift(1) / 5.0).apply(np.floor))
    lower.iloc[0] = False
    return _consec_streak(lower)


def pcp_125_num_dollar_zones_crossed_21d(close: pd.Series) -> pd.Series:
    """Number of distinct whole-dollar zones visited in trailing 21 days."""
    def count_zones(x):
        vals = x.dropna()
        if len(vals) == 0:
            return np.nan
        return float(len(set(np.floor(vals))))
    return close.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        count_zones, raw=False)


# --- Group M (126-135): Absolute price level as signal ---

def pcp_126_log_price_level(close: pd.Series) -> pd.Series:
    """Natural log of close price (absolute level signal)."""
    return np.log(close.clip(lower=_EPS))


def pcp_127_price_below_52wk_low_proximity(close: pd.Series) -> pd.Series:
    """Ratio: close / 252-day rolling minimum close (1 = at 52-week low)."""
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(close, mn.clip(lower=_EPS))


def pcp_128_close_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum close price (all-time low proxy)."""
    return close.expanding(min_periods=1).min()


def pcp_129_close_vs_expanding_min_ratio(close: pd.Series) -> pd.Series:
    """Ratio: close / expanding minimum close (1.0 = at all-time low)."""
    exp_min = close.expanding(min_periods=1).min()
    return _safe_div(close, exp_min.clip(lower=_EPS))


def pcp_130_close_min_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day minimum close (quarterly low)."""
    return _rolling_min(close, _TD_QTR)


def pcp_131_close_at_63d_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: today's close equals the 63-day minimum close."""
    mn63 = _rolling_min(close, _TD_QTR)
    return (close <= mn63 + _EPS).astype(float)


def pcp_132_close_at_252d_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: today's close equals the 252-day minimum close."""
    mn252 = _rolling_min(close, _TD_YEAR)
    return (close <= mn252 + _EPS).astype(float)


def pcp_133_close_pct_from_52wk_low(close: pd.Series) -> pd.Series:
    """Percentage above 252-day minimum: (close - min) / min."""
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - mn, mn.clip(lower=_EPS))


def pcp_134_close_pct_from_63d_low(close: pd.Series) -> pd.Series:
    """Percentage above 63-day minimum: (close - min63) / min63."""
    mn = _rolling_min(close, _TD_QTR)
    return _safe_div(close - mn, mn.clip(lower=_EPS))


def pcp_135_abs_price_level_distress_score(close: pd.Series) -> pd.Series:
    """Composite distress score: 1*(close<$10) + 2*(close<$5) + 3*(close<$2) + 4*(close<$1)."""
    return (
        (close < 10.0).astype(float) +
        2.0 * (close < 5.0).astype(float) +
        3.0 * (close < 2.0).astype(float) +
        4.0 * (close < 1.0).astype(float)
    )


# --- Group N (136-150): Additional clustering & distress features ---

def pcp_136_round_level_magnet_score_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d mean of (1 - dist_to_dollar/0.5): higher = more pinned to round levels."""
    normalized = 1.0 - (_dist_to_round(close, 1.0) / 0.5).clip(upper=1.0)
    return _rolling_mean(normalized, _TD_MON)


def pcp_137_round_level_magnet_score_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d mean of round-level magnet score."""
    normalized = 1.0 - (_dist_to_round(close, 1.0) / 0.5).clip(upper=1.0)
    return _rolling_mean(normalized, _TD_QTR)


def pcp_138_5dollar_magnet_score_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d mean of (1 - dist_to_5dollar/2.5): higher = more pinned to $5 levels."""
    normalized = 1.0 - (_dist_to_round(close, 5.0) / 2.5).clip(upper=1.0)
    return _rolling_mean(normalized, _TD_MON)


def pcp_139_dist_dollar_normalized_by_atr_proxy(close: pd.Series,
                                                  high: pd.Series,
                                                  low: pd.Series) -> pd.Series:
    """Distance to nearest whole dollar normalized by 14-day ATR proxy (H-L range)."""
    atr_proxy = _rolling_mean(high - low, 14)
    return _safe_div(_dist_to_round(close, 1.0), atr_proxy.clip(lower=_EPS))


def pcp_140_dist_5dollar_normalized_by_atr_proxy(close: pd.Series,
                                                   high: pd.Series,
                                                   low: pd.Series) -> pd.Series:
    """Distance to nearest $5 level normalized by 14-day ATR proxy."""
    atr_proxy = _rolling_mean(high - low, 14)
    return _safe_div(_dist_to_round(close, 5.0), atr_proxy.clip(lower=_EPS))


def pcp_141_close_round_level_oscillator(close: pd.Series) -> pd.Series:
    """Oscillator: signed distance from nearest whole dollar (positive = above, negative = below)."""
    cents = close % 1.0
    return cents - 0.5


def pcp_142_5dollar_round_level_oscillator(close: pd.Series) -> pd.Series:
    """Signed distance from nearest $5 level (positive = above midpoint, negative = below)."""
    mod = close % 5.0
    return mod - 2.5


def pcp_143_price_cluster_entropy_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d: entropy of close prices binned to whole-dollar zones (lower = more clustering)."""
    def dollar_entropy(x):
        vals = x.dropna()
        if len(vals) < 2:
            return np.nan
        zones = np.floor(vals).astype(int)
        counts = np.bincount(zones - zones.min())
        counts = counts[counts > 0]
        probs = counts / counts.sum()
        return float(-np.sum(probs * np.log(probs + _EPS)))
    return close.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(
        dollar_entropy, raw=False)


def pcp_144_price_cluster_entropy_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d: entropy of close prices binned to whole-dollar zones."""
    def dollar_entropy(x):
        vals = x[~np.isnan(x)]
        if len(vals) < 2:
            return np.nan
        zones = np.floor(vals).astype(int)
        counts = np.bincount(zones - zones.min())
        counts = counts[counts > 0]
        probs = counts / counts.sum()
        return float(-np.sum(probs * np.log(probs + _EPS)))
    return close.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(
        dollar_entropy, raw=True)


def pcp_145_frac_closes_in_same_dollar_as_today_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days close is in the same whole-dollar zone as current close."""
    today_zone = close.apply(np.floor)
    def frac_same(x):
        if len(x) < 1:
            return np.nan
        return float(np.sum(np.floor(x) == np.floor(x[-1]))) / len(x)
    return close.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        frac_same, raw=True)


def pcp_146_frac_closes_in_same_5dollar_as_today_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days close is in the same $5 zone as current close."""
    def frac_same5(x):
        if len(x) < 1:
            return np.nan
        return float(np.sum(np.floor(x / 5.0) == np.floor(x[-1] / 5.0))) / len(x)
    return close.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        frac_same5, raw=True)


def pcp_147_close_below_prior_round_dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close broke below the prior day's whole-dollar floor."""
    return (close.apply(np.floor) < close.shift(1).apply(np.floor)).astype(float)


def pcp_148_close_above_prior_round_dollar_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close rose above the prior day's whole-dollar ceiling."""
    return (close.apply(np.floor) > close.shift(1).apply(np.floor)).astype(float)


def pcp_149_num_5dollar_zones_crossed_63d(close: pd.Series) -> pd.Series:
    """Number of distinct $5 zones visited in trailing 63 days."""
    def count_5zones(x):
        vals = x[~np.isnan(x)]
        if len(vals) == 0:
            return np.nan
        return float(len(set(np.floor(vals / 5.0).astype(int))))
    return close.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        count_5zones, raw=True)


def pcp_150_round_level_capitulation_composite(close: pd.Series) -> pd.Series:
    """Composite: sub-$5 flag*2 + sub-$1 flag*3 + dist-to-dollar percentile rank 252d (inverted).
    Higher = more psychologically distressed at round levels."""
    dist_rank = _dist_to_round(close, 1.0).rolling(
        _TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    sub5 = (close < 5.0).astype(float) * 2.0
    sub1 = (close < 1.0).astype(float) * 3.0
    return sub5 + sub1 + dist_rank.fillna(0.5)


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_CLUSTERING_PSYCHOLOGY_REGISTRY_076_150 = {
    "pcp_076_open_dist_to_nearest_dollar": {"inputs": ["open"], "func": pcp_076_open_dist_to_nearest_dollar},
    "pcp_077_open_dist_to_nearest_dollar_pct": {"inputs": ["open"], "func": pcp_077_open_dist_to_nearest_dollar_pct},
    "pcp_078_open_at_whole_dollar_flag": {"inputs": ["open"], "func": pcp_078_open_at_whole_dollar_flag},
    "pcp_079_open_dist_to_nearest_5dollar": {"inputs": ["open"], "func": pcp_079_open_dist_to_nearest_5dollar},
    "pcp_080_open_dist_to_nearest_10dollar": {"inputs": ["open"], "func": pcp_080_open_dist_to_nearest_10dollar},
    "pcp_081_open_sub5_flag": {"inputs": ["open"], "func": pcp_081_open_sub5_flag},
    "pcp_082_open_sub1_flag": {"inputs": ["open"], "func": pcp_082_open_sub1_flag},
    "pcp_083_frac_open_near_dollar_21d": {"inputs": ["open"], "func": pcp_083_frac_open_near_dollar_21d},
    "pcp_084_open_cents_digit": {"inputs": ["open"], "func": pcp_084_open_cents_digit},
    "pcp_085_open_trailing_zero_flag": {"inputs": ["open"], "func": pcp_085_open_trailing_zero_flag},
    "pcp_086_high_dist_to_nearest_dollar": {"inputs": ["high"], "func": pcp_086_high_dist_to_nearest_dollar},
    "pcp_087_high_dist_to_nearest_5dollar": {"inputs": ["high"], "func": pcp_087_high_dist_to_nearest_5dollar},
    "pcp_088_high_at_whole_dollar_flag": {"inputs": ["high"], "func": pcp_088_high_at_whole_dollar_flag},
    "pcp_089_low_dist_to_nearest_dollar": {"inputs": ["low"], "func": pcp_089_low_dist_to_nearest_dollar},
    "pcp_090_low_dist_to_nearest_5dollar": {"inputs": ["low"], "func": pcp_090_low_dist_to_nearest_5dollar},
    "pcp_091_low_at_whole_dollar_flag": {"inputs": ["low"], "func": pcp_091_low_at_whole_dollar_flag},
    "pcp_092_low_at_5dollar_flag": {"inputs": ["low"], "func": pcp_092_low_at_5dollar_flag},
    "pcp_093_high_cents_digit": {"inputs": ["high"], "func": pcp_093_high_cents_digit},
    "pcp_094_low_cents_digit": {"inputs": ["low"], "func": pcp_094_low_cents_digit},
    "pcp_095_frac_low_near_dollar_21d": {"inputs": ["low"], "func": pcp_095_frac_low_near_dollar_21d},
    "pcp_096_open_close_both_near_dollar_flag": {"inputs": ["open", "close"], "func": pcp_096_open_close_both_near_dollar_flag},
    "pcp_097_high_low_both_near_dollar_flag": {"inputs": ["high", "low"], "func": pcp_097_high_low_both_near_dollar_flag},
    "pcp_098_all_four_near_dollar_flag": {"inputs": ["open", "high", "low", "close"], "func": pcp_098_all_four_near_dollar_flag},
    "pcp_099_close_below_open_round_flag": {"inputs": ["open", "close"], "func": pcp_099_close_below_open_round_flag},
    "pcp_100_open_close_same_dollar_zone_flag": {"inputs": ["open", "close"], "func": pcp_100_open_close_same_dollar_zone_flag},
    "pcp_101_frac_open_close_near_dollar_21d": {"inputs": ["open", "close"], "func": pcp_101_frac_open_close_near_dollar_21d},
    "pcp_102_close_dist_dollar_vs_open_dist_dollar": {"inputs": ["open", "close"], "func": pcp_102_close_dist_dollar_vs_open_dist_dollar},
    "pcp_103_high_at_5dollar_flag": {"inputs": ["high"], "func": pcp_103_high_at_5dollar_flag},
    "pcp_104_open_close_both_sub5_flag": {"inputs": ["open", "close"], "func": pcp_104_open_close_both_sub5_flag},
    "pcp_105_high_sub5_flag": {"inputs": ["high"], "func": pcp_105_high_sub5_flag},
    "pcp_106_vol_on_near_dollar_days_21d": {"inputs": ["close", "volume"], "func": pcp_106_vol_on_near_dollar_days_21d},
    "pcp_107_vol_on_sub5_days_21d": {"inputs": ["close", "volume"], "func": pcp_107_vol_on_sub5_days_21d},
    "pcp_108_vol_on_sub5_days_63d": {"inputs": ["close", "volume"], "func": pcp_108_vol_on_sub5_days_63d},
    "pcp_109_vol_fraction_near_dollar_21d": {"inputs": ["close", "volume"], "func": pcp_109_vol_fraction_near_dollar_21d},
    "pcp_110_vol_fraction_sub5_21d": {"inputs": ["close", "volume"], "func": pcp_110_vol_fraction_sub5_21d},
    "pcp_111_vol_fraction_sub10_21d": {"inputs": ["close", "volume"], "func": pcp_111_vol_fraction_sub10_21d},
    "pcp_112_avg_vol_near_dollar_vs_overall": {"inputs": ["close", "volume"], "func": pcp_112_avg_vol_near_dollar_vs_overall},
    "pcp_113_vol_on_sub1_days_63d": {"inputs": ["close", "volume"], "func": pcp_113_vol_on_sub1_days_63d},
    "pcp_114_vol_near_5dollar_fraction_63d": {"inputs": ["close", "volume"], "func": pcp_114_vol_near_5dollar_fraction_63d},
    "pcp_115_vol_on_at_5dollar_flag_days_252d": {"inputs": ["close", "volume"], "func": pcp_115_vol_on_at_5dollar_flag_days_252d},
    "pcp_116_days_since_close_crossed_above_5dollar": {"inputs": ["close"], "func": pcp_116_days_since_close_crossed_above_5dollar},
    "pcp_117_days_since_close_crossed_below_5dollar": {"inputs": ["close"], "func": pcp_117_days_since_close_crossed_below_5dollar},
    "pcp_118_days_since_close_crossed_below_10dollar": {"inputs": ["close"], "func": pcp_118_days_since_close_crossed_below_10dollar},
    "pcp_119_days_since_close_crossed_below_1dollar": {"inputs": ["close"], "func": pcp_119_days_since_close_crossed_below_1dollar},
    "pcp_120_dollar_zone_flag_change": {"inputs": ["close"], "func": pcp_120_dollar_zone_flag_change},
    "pcp_121_5dollar_zone_flag_change": {"inputs": ["close"], "func": pcp_121_5dollar_zone_flag_change},
    "pcp_122_consec_days_same_dollar_zone": {"inputs": ["close"], "func": pcp_122_consec_days_same_dollar_zone},
    "pcp_123_dollar_zone_descent_streak": {"inputs": ["close"], "func": pcp_123_dollar_zone_descent_streak},
    "pcp_124_5dollar_zone_descent_streak": {"inputs": ["close"], "func": pcp_124_5dollar_zone_descent_streak},
    "pcp_125_num_dollar_zones_crossed_21d": {"inputs": ["close"], "func": pcp_125_num_dollar_zones_crossed_21d},
    "pcp_126_log_price_level": {"inputs": ["close"], "func": pcp_126_log_price_level},
    "pcp_127_price_below_52wk_low_proximity": {"inputs": ["close"], "func": pcp_127_price_below_52wk_low_proximity},
    "pcp_128_close_expanding_min": {"inputs": ["close"], "func": pcp_128_close_expanding_min},
    "pcp_129_close_vs_expanding_min_ratio": {"inputs": ["close"], "func": pcp_129_close_vs_expanding_min_ratio},
    "pcp_130_close_min_63d": {"inputs": ["close"], "func": pcp_130_close_min_63d},
    "pcp_131_close_at_63d_low_flag": {"inputs": ["close"], "func": pcp_131_close_at_63d_low_flag},
    "pcp_132_close_at_252d_low_flag": {"inputs": ["close"], "func": pcp_132_close_at_252d_low_flag},
    "pcp_133_close_pct_from_52wk_low": {"inputs": ["close"], "func": pcp_133_close_pct_from_52wk_low},
    "pcp_134_close_pct_from_63d_low": {"inputs": ["close"], "func": pcp_134_close_pct_from_63d_low},
    "pcp_135_abs_price_level_distress_score": {"inputs": ["close"], "func": pcp_135_abs_price_level_distress_score},
    "pcp_136_round_level_magnet_score_21d": {"inputs": ["close"], "func": pcp_136_round_level_magnet_score_21d},
    "pcp_137_round_level_magnet_score_63d": {"inputs": ["close"], "func": pcp_137_round_level_magnet_score_63d},
    "pcp_138_5dollar_magnet_score_21d": {"inputs": ["close"], "func": pcp_138_5dollar_magnet_score_21d},
    "pcp_139_dist_dollar_normalized_by_atr_proxy": {"inputs": ["close", "high", "low"], "func": pcp_139_dist_dollar_normalized_by_atr_proxy},
    "pcp_140_dist_5dollar_normalized_by_atr_proxy": {"inputs": ["close", "high", "low"], "func": pcp_140_dist_5dollar_normalized_by_atr_proxy},
    "pcp_141_close_round_level_oscillator": {"inputs": ["close"], "func": pcp_141_close_round_level_oscillator},
    "pcp_142_5dollar_round_level_oscillator": {"inputs": ["close"], "func": pcp_142_5dollar_round_level_oscillator},
    "pcp_143_price_cluster_entropy_21d": {"inputs": ["close"], "func": pcp_143_price_cluster_entropy_21d},
    "pcp_144_price_cluster_entropy_63d": {"inputs": ["close"], "func": pcp_144_price_cluster_entropy_63d},
    "pcp_145_frac_closes_in_same_dollar_as_today_21d": {"inputs": ["close"], "func": pcp_145_frac_closes_in_same_dollar_as_today_21d},
    "pcp_146_frac_closes_in_same_5dollar_as_today_21d": {"inputs": ["close"], "func": pcp_146_frac_closes_in_same_5dollar_as_today_21d},
    "pcp_147_close_below_prior_round_dollar_flag": {"inputs": ["close"], "func": pcp_147_close_below_prior_round_dollar_flag},
    "pcp_148_close_above_prior_round_dollar_flag": {"inputs": ["close"], "func": pcp_148_close_above_prior_round_dollar_flag},
    "pcp_149_num_5dollar_zones_crossed_63d": {"inputs": ["close"], "func": pcp_149_num_5dollar_zones_crossed_63d},
    "pcp_150_round_level_capitulation_composite": {"inputs": ["close"], "func": pcp_150_round_level_capitulation_composite},
}
