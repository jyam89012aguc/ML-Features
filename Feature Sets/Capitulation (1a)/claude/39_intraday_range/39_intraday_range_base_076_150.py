"""
39_intraday_range — Base Features 076-150
Domain: daily high-low spread level and day-to-day structure — range regime detection,
range relative to volume, range streaks, range cross-sectional comparisons, range
momentum, range stability ratios, high/low position measures, and composite range indices.
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _hl_range_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily high-low range normalized by close price."""
    return _safe_div(high - low, close)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Range vs volume interaction ---

def idr_076_range_times_volume(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Normalized range multiplied by volume (dollar-like range*volume measure)."""
    r = _hl_range_over_close(high, low, close)
    return r * volume


def idr_077_avg_range_times_volume_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day average of range × volume product."""
    rv = _hl_range_over_close(high, low, close) * volume
    return _rolling_mean(rv, _TD_MON)


def idr_078_range_per_unit_volume_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day average of normalized range divided by normalized volume (illiquidity)."""
    r = _hl_range_over_close(high, low, close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return _rolling_mean(_safe_div(r, vol_norm), _TD_MON)


def idr_079_range_per_unit_volume_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day average of normalized range divided by normalized volume."""
    r = _hl_range_over_close(high, low, close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    return _rolling_mean(_safe_div(r, vol_norm), _TD_QTR)


def idr_080_high_vol_high_range_days_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 21 days with above-avg range AND above-avg volume."""
    r = _hl_range_over_close(high, low, close)
    avg_r = _rolling_mean(r, _TD_MON)
    avg_v = _rolling_mean(volume, _TD_MON)
    flag = ((r > avg_r) & (volume > avg_v)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def idr_081_high_vol_low_range_days_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with above-avg volume but below-avg range (churning signal)."""
    r = _hl_range_over_close(high, low, close)
    avg_r = _rolling_mean(r, _TD_MON)
    avg_v = _rolling_mean(volume, _TD_MON)
    flag = ((r < avg_r) & (volume > avg_v)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def idr_082_range_vol_corr_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling Pearson correlation between normalized range and volume."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).corr(volume)


def idr_083_range_vol_corr_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling correlation between normalized range and volume."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).corr(volume)


def idr_084_vol_normalized_range_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's range divided by 21-day average range, scaled by vol/avg_vol ratio."""
    r = _hl_range_over_close(high, low, close)
    avg_r = _rolling_mean(r, _TD_MON)
    avg_v = _rolling_mean(volume, _TD_MON)
    return _safe_div(r, avg_r) * _safe_div(volume, avg_v)


def idr_085_range_dollar_vol_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day avg of (H-L) / (close * volume) — range per dollar traded."""
    dollar_vol = (close * volume).replace(0, np.nan)
    return _rolling_mean(_safe_div(high - low, dollar_vol), _TD_MON)


# --- Group I (086-095): Range streak features ---

def idr_086_consec_range_up_days(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current streak of consecutive days with range > prior day's range."""
    r = _hl_range_over_close(high, low, close)
    cond = r > r.shift(1)
    return _consec_streak(cond)


def idr_087_consec_range_down_days(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current streak of consecutive days with range < prior day's range."""
    r = _hl_range_over_close(high, low, close)
    cond = r < r.shift(1)
    return _consec_streak(cond)


def idr_088_consec_above_avg_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current streak of days where range > 21-day average range."""
    r = _hl_range_over_close(high, low, close)
    avg = _rolling_mean(r, _TD_MON)
    cond = r > avg
    return _consec_streak(cond)


def idr_089_consec_below_avg_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current streak of days where range < 21-day average range (compression streak)."""
    r = _hl_range_over_close(high, low, close)
    avg = _rolling_mean(r, _TD_MON)
    cond = r < avg
    return _consec_streak(cond)


def idr_090_consec_above_avg_range_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current streak of days where range > 63-day average range."""
    r = _hl_range_over_close(high, low, close)
    avg = _rolling_mean(r, _TD_QTR)
    cond = r > avg
    return _consec_streak(cond)


def idr_091_range_up_streak_norm_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding-range streak length normalized by 21-day average streak length."""
    r = _hl_range_over_close(high, low, close)
    streak = _consec_streak(r > r.shift(1))
    avg = _rolling_mean(streak, _TD_MON)
    return _safe_div(streak, avg)


def idr_092_max_range_up_streak_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive expanding-range run within trailing 63 days."""
    r = _hl_range_over_close(high, low, close)
    cond = r > r.shift(1)
    def _max_run(arr):
        mx = 0; cur = 0
        for v in arr:
            if v: cur += 1; mx = max(mx, cur)
            else: cur = 0
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def idr_093_range_regime_high_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: 5-day avg range > 252-day avg range (elevated range regime)."""
    r = _hl_range_over_close(high, low, close)
    return (_rolling_mean(r, _TD_WEEK) > _rolling_mean(r, _TD_YEAR)).astype(float)


def idr_094_range_regime_low_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: 5-day avg range < 25th pct of 252-day range distribution (suppressed range)."""
    r = _hl_range_over_close(high, low, close)
    p25 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return (_rolling_mean(r, _TD_WEEK) < p25).astype(float)


def idr_095_range_days_since_max_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days since the 252-day maximum normalized range occurred."""
    r = _hl_range_over_close(high, low, close)
    idx = pd.Series(np.arange(len(r)), index=r.index)
    def days_since_max(arr):
        if len(arr) == 0:
            return np.nan
        max_pos = np.argmax(arr)
        return float(len(arr) - 1 - max_pos)
    return r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(days_since_max, raw=True)


# --- Group J (096-105): Range momentum and trend ---

def idr_096_range_5d_21d_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day average range to 21-day average range (short vs medium)."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(_rolling_mean(r, _TD_WEEK), _rolling_mean(r, _TD_MON))


def idr_097_range_21d_63d_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day average range to 63-day average range."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(_rolling_mean(r, _TD_MON), _rolling_mean(r, _TD_QTR))


def idr_098_range_63d_252d_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 63-day average range to 252-day average range."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(_rolling_mean(r, _TD_QTR), _rolling_mean(r, _TD_YEAR))


def idr_099_range_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of normalized range over trailing 21 days."""
    r = _hl_range_over_close(high, low, close)
    return _linslope(r, _TD_MON)


def idr_100_range_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of normalized range over trailing 63 days."""
    r = _hl_range_over_close(high, low, close)
    return _linslope(r, _TD_QTR)


def idr_101_range_momentum_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of normalized range (short-horizon range momentum)."""
    r = _hl_range_over_close(high, low, close)
    return r.diff(_TD_WEEK)


def idr_102_range_momentum_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of normalized range."""
    r = _hl_range_over_close(high, low, close)
    return r.diff(_TD_MON)


def idr_103_range_momentum_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day diff of normalized range."""
    r = _hl_range_over_close(high, low, close)
    return r.diff(_TD_QTR)


def idr_104_avg_range_5d_pct_change_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day percent change in the 5-day average range."""
    avg5 = _rolling_mean(_hl_range_over_close(high, low, close), _TD_WEEK)
    return avg5.pct_change(_TD_MON)


def idr_105_range_ewm_crossover_21_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(63) of normalized range (short vs long EMA spread)."""
    r = _hl_range_over_close(high, low, close)
    return _ewm_mean(r, _TD_MON) - _ewm_mean(r, _TD_QTR)


# --- Group K (106-115): High and low position (daily extremes as structure signals) ---

def idr_106_high_over_prior_high(high: pd.Series) -> pd.Series:
    """Today's high divided by prior day's high (directional high drift)."""
    return _safe_div(high, high.shift(1))


def idr_107_low_over_prior_low(low: pd.Series) -> pd.Series:
    """Today's low divided by prior day's low (directional low drift)."""
    return _safe_div(low, low.shift(1))


def idr_108_high_5d_max_ratio(high: pd.Series, close: pd.Series) -> pd.Series:
    """Today's high as fraction of 5-day rolling high."""
    return _safe_div(high, _rolling_max(high, _TD_WEEK))


def idr_109_low_5d_min_ratio(low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's low as fraction of 5-day rolling low (closeness to recent low)."""
    return _safe_div(low, _rolling_min(low, _TD_WEEK))


def idr_110_high_21d_max_ratio(high: pd.Series, close: pd.Series) -> pd.Series:
    """Today's high as fraction of 21-day rolling high."""
    return _safe_div(high, _rolling_max(high, _TD_MON))


def idr_111_low_21d_min_ratio(low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's low as fraction of 21-day rolling minimum low."""
    return _safe_div(low, _rolling_min(low, _TD_MON))


def idr_112_high_low_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of daily high to daily low (H/L spread ratio)."""
    return _safe_div(high, low.replace(0, np.nan))


def idr_113_avg_high_low_ratio_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average of high/low ratio."""
    return _rolling_mean(_safe_div(high, low.replace(0, np.nan)), _TD_MON)


def idr_114_avg_high_low_ratio_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day average of high/low ratio."""
    return _rolling_mean(_safe_div(high, low.replace(0, np.nan)), _TD_QTR)


def idr_115_log_high_low_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log of high/low ratio (log-price range measure)."""
    return np.log(_safe_div(high, low.replace(0, np.nan)).clip(lower=_EPS))


# --- Group L (116-125): Range normalized by multiple-day price differences ---

def idr_116_range_over_5d_return(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range normalized by absolute 5-day close return."""
    ret5 = close.pct_change(_TD_WEEK).abs().replace(0, np.nan)
    return _safe_div(_hl_range_over_close(high, low, close), ret5)


def idr_117_range_over_21d_return(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range normalized by absolute 21-day close return."""
    ret21 = close.pct_change(_TD_MON).abs().replace(0, np.nan)
    return _safe_div(_hl_range_over_close(high, low, close), ret21)


def idr_118_range_sum_5d_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of raw ranges over trailing 5 days, normalized by today's close."""
    return _safe_div(_rolling_sum(high - low, _TD_WEEK), close)


def idr_119_range_sum_21d_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of raw ranges over trailing 21 days, normalized by today's close."""
    return _safe_div(_rolling_sum(high - low, _TD_MON), close)


def idr_120_range_sum_63d_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of raw ranges over trailing 63 days, normalized by today's close."""
    return _safe_div(_rolling_sum(high - low, _TD_QTR), close)


def idr_121_cum_range_to_price_path_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day summed range to absolute 21-day price change (range vs trend)."""
    sum_range = _rolling_sum(high - low, _TD_MON)
    price_path = close.diff(_TD_MON).abs().replace(0, np.nan)
    return _safe_div(sum_range, price_path)


def idr_122_cum_range_to_price_path_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 63-day summed range to absolute 63-day price change."""
    sum_range = _rolling_sum(high - low, _TD_QTR)
    price_path = close.diff(_TD_QTR).abs().replace(0, np.nan)
    return _safe_div(sum_range, price_path)


def idr_123_range_efficiency_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day absolute price return divided by 21-day summed range (path efficiency)."""
    sum_range = _rolling_sum(high - low, _TD_MON).replace(0, np.nan)
    return _safe_div(close.diff(_TD_MON).abs(), sum_range)


def idr_124_range_efficiency_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day absolute price return divided by 63-day summed range."""
    sum_range = _rolling_sum(high - low, _TD_QTR).replace(0, np.nan)
    return _safe_div(close.diff(_TD_QTR).abs(), sum_range)


def idr_125_rolling_high_low_spread_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day high minus 21-day low, normalized by close (regime spread)."""
    rh = _rolling_max(high, _TD_MON)
    rl = _rolling_min(low, _TD_MON)
    return _safe_div(rh - rl, close)


# --- Group M (126-135): Range stability ratios and composite measures ---

def idr_126_rolling_high_low_spread_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day high minus 63-day low, normalized by close."""
    rh = _rolling_max(high, _TD_QTR)
    rl = _rolling_min(low, _TD_QTR)
    return _safe_div(rh - rl, close)


def idr_127_rolling_high_low_spread_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day high minus 252-day low, normalized by close."""
    rh = _rolling_max(high, _TD_YEAR)
    rl = _rolling_min(low, _TD_YEAR)
    return _safe_div(rh - rl, close)


def idr_128_daily_range_to_period_spread_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's range as fraction of 21-day H-L period spread."""
    period_spread = (_rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)).replace(0, np.nan)
    return _safe_div(high - low, period_spread)


def idr_129_daily_range_to_period_spread_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's range as fraction of 63-day H-L period spread."""
    period_spread = (_rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR)).replace(0, np.nan)
    return _safe_div(high - low, period_spread)


def idr_130_range_stability_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min normalized range over 21 days divided by max (1 = perfectly stable)."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(_rolling_min(r, _TD_MON), _rolling_max(r, _TD_MON).clip(lower=_EPS))


def idr_131_range_stability_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min normalized range over 63 days divided by max."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(_rolling_min(r, _TD_QTR), _rolling_max(r, _TD_QTR).clip(lower=_EPS))


def idr_132_avg_range_21d_vs_252d_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day avg range to 252-day avg range (near-term relative level)."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(_rolling_mean(r, _TD_MON), _rolling_mean(r, _TD_YEAR))


def idr_133_range_mean_reversion_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed deviation of today's range from 21-day mean (raw, not normalized)."""
    r = _hl_range_over_close(high, low, close)
    return r - _rolling_mean(r, _TD_MON)


def idr_134_range_mean_reversion_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed deviation of today's range from 63-day mean."""
    r = _hl_range_over_close(high, low, close)
    return r - _rolling_mean(r, _TD_QTR)


def idr_135_range_high_low_asymmetry_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day avg (high - close) minus avg (close - low), normalized by avg range."""
    upper = _rolling_mean(high - close, _TD_MON)
    lower = _rolling_mean(close - low, _TD_MON)
    avg_r = _rolling_mean(high - low, _TD_MON).replace(0, np.nan)
    return _safe_div(upper - lower, avg_r)


# --- Group N (136-145): Range on specific day types (up days, down days) ---

def idr_136_avg_range_on_up_days_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day average normalized range on days where close > prior close."""
    r = _hl_range_over_close(high, low, close)
    is_up = close > close.shift(1)
    return r.where(is_up, np.nan).rolling(_TD_MON, min_periods=1).mean()


def idr_137_avg_range_on_down_days_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day average normalized range on days where close < prior close."""
    r = _hl_range_over_close(high, low, close)
    is_dn = close < close.shift(1)
    return r.where(is_dn, np.nan).rolling(_TD_MON, min_periods=1).mean()


def idr_138_range_up_vs_down_days_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of avg range on up days to avg range on down days over 21 days."""
    up = idr_136_avg_range_on_up_days_21d(high, low, close)
    dn = idr_137_avg_range_on_down_days_21d(high, low, close)
    return _safe_div(up, dn)


def idr_139_avg_range_on_up_days_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day average normalized range on up days."""
    r = _hl_range_over_close(high, low, close)
    is_up = close > close.shift(1)
    return r.where(is_up, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def idr_140_avg_range_on_down_days_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day average normalized range on down days."""
    r = _hl_range_over_close(high, low, close)
    is_dn = close < close.shift(1)
    return r.where(is_dn, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def idr_141_range_up_vs_down_days_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of avg range on up days to avg range on down days over 63 days."""
    up = idr_139_avg_range_on_up_days_63d(high, low, close)
    dn = idr_140_avg_range_on_down_days_63d(high, low, close)
    return _safe_div(up, dn)


def idr_142_avg_range_gap_up_days_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day avg range on days with gap-up open (open > prior close)."""
    r = _hl_range_over_close(high, low, close)
    gap_up = open > close.shift(1)
    return r.where(gap_up, np.nan).rolling(_TD_MON, min_periods=1).mean()


def idr_143_avg_range_gap_down_days_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day avg range on days with gap-down open (open < prior close)."""
    r = _hl_range_over_close(high, low, close)
    gap_dn = open < close.shift(1)
    return r.where(gap_dn, np.nan).rolling(_TD_MON, min_periods=1).mean()


def idr_144_high_range_down_day_flag_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with above-avg range on a down day (panic sell signal), 21d."""
    r = _hl_range_over_close(high, low, close)
    avg_r = _rolling_mean(r, _TD_MON)
    is_dn = close < close.shift(1)
    flag = ((r > avg_r) & is_dn).astype(float)
    return _rolling_sum(flag, _TD_MON)


def idr_145_high_range_down_day_fraction_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of down days in trailing 63d that had above-avg range."""
    r = _hl_range_over_close(high, low, close)
    avg_r = _rolling_mean(r, _TD_QTR)
    is_dn = (close < close.shift(1)).astype(float)
    high_rng_dn = ((r > avg_r) & (close < close.shift(1))).astype(float)
    dn_count = _rolling_sum(is_dn, _TD_QTR).replace(0, np.nan)
    return _safe_div(_rolling_sum(high_rng_dn, _TD_QTR), dn_count)


# --- Group O (146-150): Composite and cross-feature range indices ---

def idr_146_range_composite_index_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: avg of (range/avg_21d), (range/avg_63d), (range/avg_252d)."""
    r = _hl_range_over_close(high, low, close)
    a = _safe_div(r, _rolling_mean(r, _TD_MON))
    b = _safe_div(r, _rolling_mean(r, _TD_QTR))
    c = _safe_div(r, _rolling_mean(r, _TD_YEAR))
    return (a + b + c) / 3.0


def idr_147_range_zscore_composite(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average of 21d, 63d, 252d z-scores of normalized range."""
    r = _hl_range_over_close(high, low, close)
    z21 = _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON))
    z63 = _safe_div(r - _rolling_mean(r, _TD_QTR), _rolling_std(r, _TD_QTR))
    z252 = _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR))
    return (z21 + z63 + z252) / 3.0


def idr_148_range_expanding_zscore(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding z-score of normalized range (all-history extremity)."""
    r = _hl_range_over_close(high, low, close)
    m = r.expanding(min_periods=5).mean()
    s = r.expanding(min_periods=5).std()
    return _safe_div(r - m, s)


def idr_149_range_percentile_composite(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average of 21d, 63d, 252d percentile ranks of today's range."""
    r = _hl_range_over_close(high, low, close)
    p21 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    p63 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    p252 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return (p21 + p63 + p252) / 3.0


def idr_150_range_distress_index(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite distress: 252d zscore of range × vol_norm, scaled by down-day fraction."""
    r = _hl_range_over_close(high, low, close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    rv = r * vol_norm
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    z = _safe_div(rv - m, s)
    is_dn = (close < close.shift(1)).astype(float)
    dn_frac = _rolling_mean(is_dn, _TD_MON)
    return z * dn_frac


# ── Registry ──────────────────────────────────────────────────────────────────

INTRADAY_RANGE_REGISTRY_076_150 = {
    "idr_076_range_times_volume": {"inputs": ["high", "low", "close", "volume"], "func": idr_076_range_times_volume},
    "idr_077_avg_range_times_volume_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_077_avg_range_times_volume_21d},
    "idr_078_range_per_unit_volume_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_078_range_per_unit_volume_21d},
    "idr_079_range_per_unit_volume_63d": {"inputs": ["high", "low", "close", "volume"], "func": idr_079_range_per_unit_volume_63d},
    "idr_080_high_vol_high_range_days_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_080_high_vol_high_range_days_21d},
    "idr_081_high_vol_low_range_days_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_081_high_vol_low_range_days_21d},
    "idr_082_range_vol_corr_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_082_range_vol_corr_21d},
    "idr_083_range_vol_corr_63d": {"inputs": ["high", "low", "close", "volume"], "func": idr_083_range_vol_corr_63d},
    "idr_084_vol_normalized_range_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_084_vol_normalized_range_21d},
    "idr_085_range_dollar_vol_ratio_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_085_range_dollar_vol_ratio_21d},
    "idr_086_consec_range_up_days": {"inputs": ["high", "low", "close"], "func": idr_086_consec_range_up_days},
    "idr_087_consec_range_down_days": {"inputs": ["high", "low", "close"], "func": idr_087_consec_range_down_days},
    "idr_088_consec_above_avg_range_21d": {"inputs": ["high", "low", "close"], "func": idr_088_consec_above_avg_range_21d},
    "idr_089_consec_below_avg_range_21d": {"inputs": ["high", "low", "close"], "func": idr_089_consec_below_avg_range_21d},
    "idr_090_consec_above_avg_range_63d": {"inputs": ["high", "low", "close"], "func": idr_090_consec_above_avg_range_63d},
    "idr_091_range_up_streak_norm_21d": {"inputs": ["high", "low", "close"], "func": idr_091_range_up_streak_norm_21d},
    "idr_092_max_range_up_streak_63d": {"inputs": ["high", "low", "close"], "func": idr_092_max_range_up_streak_63d},
    "idr_093_range_regime_high_flag": {"inputs": ["high", "low", "close"], "func": idr_093_range_regime_high_flag},
    "idr_094_range_regime_low_flag": {"inputs": ["high", "low", "close"], "func": idr_094_range_regime_low_flag},
    "idr_095_range_days_since_max_252d": {"inputs": ["high", "low", "close"], "func": idr_095_range_days_since_max_252d},
    "idr_096_range_5d_21d_ratio": {"inputs": ["high", "low", "close"], "func": idr_096_range_5d_21d_ratio},
    "idr_097_range_21d_63d_ratio": {"inputs": ["high", "low", "close"], "func": idr_097_range_21d_63d_ratio},
    "idr_098_range_63d_252d_ratio": {"inputs": ["high", "low", "close"], "func": idr_098_range_63d_252d_ratio},
    "idr_099_range_slope_21d": {"inputs": ["high", "low", "close"], "func": idr_099_range_slope_21d},
    "idr_100_range_slope_63d": {"inputs": ["high", "low", "close"], "func": idr_100_range_slope_63d},
    "idr_101_range_momentum_5d": {"inputs": ["high", "low", "close"], "func": idr_101_range_momentum_5d},
    "idr_102_range_momentum_21d": {"inputs": ["high", "low", "close"], "func": idr_102_range_momentum_21d},
    "idr_103_range_momentum_63d": {"inputs": ["high", "low", "close"], "func": idr_103_range_momentum_63d},
    "idr_104_avg_range_5d_pct_change_21d": {"inputs": ["high", "low", "close"], "func": idr_104_avg_range_5d_pct_change_21d},
    "idr_105_range_ewm_crossover_21_63": {"inputs": ["high", "low", "close"], "func": idr_105_range_ewm_crossover_21_63},
    "idr_106_high_over_prior_high": {"inputs": ["high"], "func": idr_106_high_over_prior_high},
    "idr_107_low_over_prior_low": {"inputs": ["low"], "func": idr_107_low_over_prior_low},
    "idr_108_high_5d_max_ratio": {"inputs": ["high", "close"], "func": idr_108_high_5d_max_ratio},
    "idr_109_low_5d_min_ratio": {"inputs": ["low", "close"], "func": idr_109_low_5d_min_ratio},
    "idr_110_high_21d_max_ratio": {"inputs": ["high", "close"], "func": idr_110_high_21d_max_ratio},
    "idr_111_low_21d_min_ratio": {"inputs": ["low", "close"], "func": idr_111_low_21d_min_ratio},
    "idr_112_high_low_ratio": {"inputs": ["high", "low"], "func": idr_112_high_low_ratio},
    "idr_113_avg_high_low_ratio_21d": {"inputs": ["high", "low"], "func": idr_113_avg_high_low_ratio_21d},
    "idr_114_avg_high_low_ratio_63d": {"inputs": ["high", "low"], "func": idr_114_avg_high_low_ratio_63d},
    "idr_115_log_high_low_ratio": {"inputs": ["high", "low"], "func": idr_115_log_high_low_ratio},
    "idr_116_range_over_5d_return": {"inputs": ["high", "low", "close"], "func": idr_116_range_over_5d_return},
    "idr_117_range_over_21d_return": {"inputs": ["high", "low", "close"], "func": idr_117_range_over_21d_return},
    "idr_118_range_sum_5d_over_close": {"inputs": ["high", "low", "close"], "func": idr_118_range_sum_5d_over_close},
    "idr_119_range_sum_21d_over_close": {"inputs": ["high", "low", "close"], "func": idr_119_range_sum_21d_over_close},
    "idr_120_range_sum_63d_over_close": {"inputs": ["high", "low", "close"], "func": idr_120_range_sum_63d_over_close},
    "idr_121_cum_range_to_price_path_21d": {"inputs": ["high", "low", "close"], "func": idr_121_cum_range_to_price_path_21d},
    "idr_122_cum_range_to_price_path_63d": {"inputs": ["high", "low", "close"], "func": idr_122_cum_range_to_price_path_63d},
    "idr_123_range_efficiency_21d": {"inputs": ["high", "low", "close"], "func": idr_123_range_efficiency_21d},
    "idr_124_range_efficiency_63d": {"inputs": ["high", "low", "close"], "func": idr_124_range_efficiency_63d},
    "idr_125_rolling_high_low_spread_21d": {"inputs": ["high", "low", "close"], "func": idr_125_rolling_high_low_spread_21d},
    "idr_126_rolling_high_low_spread_63d": {"inputs": ["high", "low", "close"], "func": idr_126_rolling_high_low_spread_63d},
    "idr_127_rolling_high_low_spread_252d": {"inputs": ["high", "low", "close"], "func": idr_127_rolling_high_low_spread_252d},
    "idr_128_daily_range_to_period_spread_21d": {"inputs": ["high", "low", "close"], "func": idr_128_daily_range_to_period_spread_21d},
    "idr_129_daily_range_to_period_spread_63d": {"inputs": ["high", "low", "close"], "func": idr_129_daily_range_to_period_spread_63d},
    "idr_130_range_stability_ratio_21d": {"inputs": ["high", "low", "close"], "func": idr_130_range_stability_ratio_21d},
    "idr_131_range_stability_ratio_63d": {"inputs": ["high", "low", "close"], "func": idr_131_range_stability_ratio_63d},
    "idr_132_avg_range_21d_vs_252d_ratio": {"inputs": ["high", "low", "close"], "func": idr_132_avg_range_21d_vs_252d_ratio},
    "idr_133_range_mean_reversion_21d": {"inputs": ["high", "low", "close"], "func": idr_133_range_mean_reversion_21d},
    "idr_134_range_mean_reversion_63d": {"inputs": ["high", "low", "close"], "func": idr_134_range_mean_reversion_63d},
    "idr_135_range_high_low_asymmetry_21d": {"inputs": ["high", "low", "close"], "func": idr_135_range_high_low_asymmetry_21d},
    "idr_136_avg_range_on_up_days_21d": {"inputs": ["high", "low", "close"], "func": idr_136_avg_range_on_up_days_21d},
    "idr_137_avg_range_on_down_days_21d": {"inputs": ["high", "low", "close"], "func": idr_137_avg_range_on_down_days_21d},
    "idr_138_range_up_vs_down_days_ratio_21d": {"inputs": ["high", "low", "close"], "func": idr_138_range_up_vs_down_days_ratio_21d},
    "idr_139_avg_range_on_up_days_63d": {"inputs": ["high", "low", "close"], "func": idr_139_avg_range_on_up_days_63d},
    "idr_140_avg_range_on_down_days_63d": {"inputs": ["high", "low", "close"], "func": idr_140_avg_range_on_down_days_63d},
    "idr_141_range_up_vs_down_days_ratio_63d": {"inputs": ["high", "low", "close"], "func": idr_141_range_up_vs_down_days_ratio_63d},
    "idr_142_avg_range_gap_up_days_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_142_avg_range_gap_up_days_21d},
    "idr_143_avg_range_gap_down_days_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_143_avg_range_gap_down_days_21d},
    "idr_144_high_range_down_day_flag_21d": {"inputs": ["high", "low", "close"], "func": idr_144_high_range_down_day_flag_21d},
    "idr_145_high_range_down_day_fraction_63d": {"inputs": ["high", "low", "close"], "func": idr_145_high_range_down_day_fraction_63d},
    "idr_146_range_composite_index_21d": {"inputs": ["high", "low", "close"], "func": idr_146_range_composite_index_21d},
    "idr_147_range_zscore_composite": {"inputs": ["high", "low", "close"], "func": idr_147_range_zscore_composite},
    "idr_148_range_expanding_zscore": {"inputs": ["high", "low", "close"], "func": idr_148_range_expanding_zscore},
    "idr_149_range_percentile_composite": {"inputs": ["high", "low", "close"], "func": idr_149_range_percentile_composite},
    "idr_150_range_distress_index": {"inputs": ["high", "low", "close", "volume"], "func": idr_150_range_distress_index},
}
