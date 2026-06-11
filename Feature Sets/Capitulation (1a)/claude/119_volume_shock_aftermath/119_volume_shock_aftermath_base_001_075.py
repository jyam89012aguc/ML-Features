"""
119_volume_shock_aftermath — Base Features 001-075
Domain: volume-shock aftermath — behavior of volume and price in the days following
        a prior high-volume shock day, measured backward from t
Includes: volume decay rates, persistence flags, days-since-shock, price drift
          after shocks, shock count aggregates
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
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


def _vol_zscore(volume: pd.Series, w: int) -> pd.Series:
    """Z-score of volume relative to its rolling mean/std over w days."""
    m = _rolling_mean(volume, w)
    s = _rolling_std(volume, w)
    return _safe_div(volume - m, s.clip(lower=_EPS))


def _shock_flag(volume: pd.Series, w: int, z_thresh: float = 2.0) -> pd.Series:
    """Binary flag: volume z-score > z_thresh within rolling w-day window."""
    return (_vol_zscore(volume, w) > z_thresh).astype(float)


def _days_since_last_shock(volume: pd.Series, w: int, z_thresh: float = 2.0) -> pd.Series:
    """Days elapsed since the most recent shock day (0 = today is shock)."""
    flag = _shock_flag(volume, w, z_thresh)
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag == 1.0).ffill().fillna(-1.0)
    elapsed = idx - last
    # where no shock has ever occurred, elapsed will be large; cap at series length
    return elapsed.where(last >= 0.0, np.nan)


def _price_return_since_shock(close: pd.Series, volume: pd.Series,
                               w: int, z_thresh: float = 2.0) -> pd.Series:
    """Cumulative close return from the most recent shock day to today."""
    flag = _shock_flag(volume, w, z_thresh)
    shock_close = close.where(flag == 1.0).ffill()
    return _safe_div(close - shock_close, shock_close.clip(lower=_EPS))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Shock identification & raw volume z-score ---

def vsa_001_vol_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score relative to trailing 21-day mean/std."""
    return _vol_zscore(volume, _TD_MON)


def vsa_002_vol_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score relative to trailing 63-day mean/std."""
    return _vol_zscore(volume, _TD_QTR)


def vsa_003_vol_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score relative to trailing 126-day mean/std."""
    return _vol_zscore(volume, _TD_HALF)


def vsa_004_vol_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score relative to trailing 252-day mean/std."""
    return _vol_zscore(volume, _TD_YEAR)


def vsa_005_shock_flag_21d_z2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today is a volume shock (z-score > 2 vs 21-day window)."""
    return _shock_flag(volume, _TD_MON, 2.0)


def vsa_006_shock_flag_63d_z2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today is a volume shock (z-score > 2 vs 63-day window)."""
    return _shock_flag(volume, _TD_QTR, 2.0)


def vsa_007_shock_flag_21d_z3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today is a severe volume shock (z-score > 3 vs 21-day)."""
    return _shock_flag(volume, _TD_MON, 3.0)


def vsa_008_shock_flag_63d_z3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today is a severe volume shock (z-score > 3 vs 63-day)."""
    return _shock_flag(volume, _TD_QTR, 3.0)


def vsa_009_vol_ratio_to_21d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of today's volume to its 21-day rolling mean."""
    return _safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS))


def vsa_010_vol_ratio_to_63d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of today's volume to its 63-day rolling mean."""
    return _safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))


# --- Group B (011-020): Days since last shock ---

def vsa_011_days_since_shock_21d_z2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days elapsed since last volume-shock day (21d window, z>2)."""
    return _days_since_last_shock(volume, _TD_MON, 2.0)


def vsa_012_days_since_shock_63d_z2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days elapsed since last volume-shock day (63d window, z>2)."""
    return _days_since_last_shock(volume, _TD_QTR, 2.0)


def vsa_013_days_since_shock_21d_z3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days elapsed since last severe volume-shock day (21d window, z>3)."""
    return _days_since_last_shock(volume, _TD_MON, 3.0)


def vsa_014_days_since_shock_63d_z3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days elapsed since last severe volume-shock day (63d window, z>3)."""
    return _days_since_last_shock(volume, _TD_QTR, 3.0)


def vsa_015_days_since_shock_252d_z2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days elapsed since last volume-shock day (252d window, z>2)."""
    return _days_since_last_shock(volume, _TD_YEAR, 2.0)


def vsa_016_shock_recency_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Inverse of days-since-shock (21d/z2); higher = shock more recent."""
    d = _days_since_last_shock(volume, _TD_MON, 2.0)
    return _safe_div(pd.Series(1.0, index=d.index), (d + 1.0).clip(lower=_EPS))


def vsa_017_shock_recency_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Inverse of days-since-shock (63d/z2); higher = shock more recent."""
    d = _days_since_last_shock(volume, _TD_QTR, 2.0)
    return _safe_div(pd.Series(1.0, index=d.index), (d + 1.0).clip(lower=_EPS))


def vsa_018_in_aftermath_window_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: last shock occurred within the past 5 trading days (21d/z2)."""
    d = _days_since_last_shock(volume, _TD_MON, 2.0)
    return (d <= _TD_WEEK).astype(float)


def vsa_019_in_aftermath_window_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: last shock occurred within the past 21 trading days (63d/z2)."""
    d = _days_since_last_shock(volume, _TD_QTR, 2.0)
    return (d <= _TD_MON).astype(float)


def vsa_020_in_aftermath_window_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: last shock occurred within the past 63 trading days (63d/z2)."""
    d = _days_since_last_shock(volume, _TD_QTR, 2.0)
    return (d <= _TD_QTR).astype(float)


# --- Group C (021-030): Volume decay rate after shock ---

def vsa_021_vol_decay_ratio_5d_since_shock(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of current volume to volume on the shock day (21d/z2 shock)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    return _safe_div(volume, shock_vol.clip(lower=_EPS))


def vsa_022_vol_decay_ratio_63d_shock(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of current volume to volume on the shock day (63d/z2 shock)."""
    flag = _shock_flag(volume, _TD_QTR, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    return _safe_div(volume, shock_vol.clip(lower=_EPS))


def vsa_023_post_shock_vol_5d_mean_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day mean volume divided by shock-day volume (21d/z2); decay measure."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    post_mean = _rolling_mean(volume, _TD_WEEK)
    return _safe_div(post_mean, shock_vol.clip(lower=_EPS))


def vsa_024_post_shock_vol_21d_mean_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean volume divided by shock-day volume (63d/z2)."""
    flag = _shock_flag(volume, _TD_QTR, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    post_mean = _rolling_mean(volume, _TD_MON)
    return _safe_div(post_mean, shock_vol.clip(lower=_EPS))


def vsa_025_vol_half_life_decay_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day EMA of volume divided by its 21-day mean; captures quick vol decay."""
    ema5 = _ewm_mean(volume, _TD_WEEK)
    mean21 = _rolling_mean(volume, _TD_MON)
    return _safe_div(ema5, mean21.clip(lower=_EPS))


def vsa_026_vol_21d_trend_post_shock(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day linear slope of volume (negative = volume decaying after shock)."""
    def slope(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); xm = x.mean()
        num = ((xi - xi_m) * (x - xm)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(slope, raw=True)


def vsa_027_vol_5d_trend_post_shock(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day linear slope of volume."""
    def slope(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); xm = x.mean()
        num = ((xi - xi_m) * (x - xm)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return volume.rolling(_TD_WEEK, min_periods=2).apply(slope, raw=True)


def vsa_028_vol_elevated_consec_days_post_shock(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days volume > 1.5x its 21-day mean (elevated persistence)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    return _consec_streak(ratio > 1.5)


def vsa_029_vol_collapse_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: volume dropped > 50% from its 5-day peak (vol collapse after shock)."""
    peak5 = _rolling_max(volume, _TD_WEEK)
    return (volume < 0.5 * peak5).astype(float)


def vsa_030_vol_5d_sum_vs_21d_avg_sum(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day volume sum divided by (21-day average 5-day sum); > 1 = still elevated."""
    sum5 = _rolling_sum(volume, _TD_WEEK)
    mean21 = _rolling_mean(sum5, _TD_MON)
    return _safe_div(sum5, mean21.clip(lower=_EPS))


# --- Group D (031-040): Shock count within windows ---

def vsa_031_shock_count_21d_z2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of volume-shock days in trailing 21 days (z>2 vs 21d window)."""
    return _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON)


def vsa_032_shock_count_63d_z2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of volume-shock days in trailing 63 days (z>2 vs 63d window)."""
    return _rolling_sum(_shock_flag(volume, _TD_QTR, 2.0), _TD_QTR)


def vsa_033_shock_count_252d_z2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of volume-shock days in trailing 252 days (z>2 vs 63d window)."""
    return _rolling_sum(_shock_flag(volume, _TD_QTR, 2.0), _TD_YEAR)


def vsa_034_shock_count_21d_z3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of severe shock days (z>3 vs 21d) in trailing 21 days."""
    return _rolling_sum(_shock_flag(volume, _TD_MON, 3.0), _TD_MON)


def vsa_035_shock_count_63d_z3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of severe shock days (z>3 vs 63d) in trailing 63 days."""
    return _rolling_sum(_shock_flag(volume, _TD_QTR, 3.0), _TD_QTR)


def vsa_036_shock_density_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days that were shock days (21d/z2)."""
    return _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON) / _TD_MON


def vsa_037_shock_density_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days that were shock days (63d/z2)."""
    return _rolling_sum(_shock_flag(volume, _TD_QTR, 2.0), _TD_QTR) / _TD_QTR


def vsa_038_shock_density_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days that were shock days (63d/z2)."""
    return _rolling_sum(_shock_flag(volume, _TD_QTR, 2.0), _TD_YEAR) / _TD_YEAR


def vsa_039_multi_shock_in_5d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 2+ shock days in the trailing 5 days (21d/z2)."""
    cnt = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_WEEK)
    return (cnt >= 2.0).astype(float)


def vsa_040_shock_cluster_consec(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive shock days ending today (21d/z2)."""
    return _consec_streak(_shock_flag(volume, _TD_MON, 2.0).astype(bool))


# --- Group E (041-050): Price drift after shocks ---

def vsa_041_price_return_since_shock_21dz2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative close return from last shock day to today (21d/z2)."""
    return _price_return_since_shock(close, volume, _TD_MON, 2.0)


def vsa_042_price_return_since_shock_63dz2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative close return from last shock day to today (63d/z2)."""
    return _price_return_since_shock(close, volume, _TD_QTR, 2.0)


def vsa_043_price_return_since_shock_21dz3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative close return from last severe shock day (21d/z3)."""
    return _price_return_since_shock(close, volume, _TD_MON, 3.0)


def vsa_044_post_shock_price_drawdown_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max drawdown of close since last shock day (21d/z2); always negative or zero."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_close = close.where(flag == 1.0).ffill()
    ret = _safe_div(close - shock_close, shock_close.clip(lower=_EPS))
    return ret.clip(upper=0.0)


def vsa_045_post_shock_close_below_shock_close_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close is below the shock-day close (continued decline after shock)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_close = close.where(flag == 1.0).ffill()
    return (close < shock_close).astype(float)


def vsa_046_shocks_followed_by_decline_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of shock days in last 63d where close 5d later was lower (already elapsed)."""
    shock = _shock_flag(volume, _TD_QTR, 2.0)
    # For each day, check if 5 days AGO was a shock day and close declined since then
    shock_5d_ago = shock.shift(5).fillna(0.0)
    declined = (close < close.shift(5)).astype(float)
    event = (shock_5d_ago == 1.0) & (declined == 1.0)
    return _rolling_sum(event.astype(float), _TD_QTR)


def vsa_047_shocks_followed_by_decline_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of shock days in last 252d where close 5d later was lower."""
    shock_5d_ago = _shock_flag(volume, _TD_QTR, 2.0).shift(5).fillna(0.0)
    declined = (close < close.shift(5)).astype(float)
    event = (shock_5d_ago == 1.0) & (declined == 1.0)
    return _rolling_sum(event.astype(float), _TD_YEAR)


def vsa_048_post_shock_5d_return_avg_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average 5-day forward return across shocks in trailing 63d (fully elapsed)."""
    shock = _shock_flag(volume, _TD_QTR, 2.0)
    ret5 = close.pct_change(5)
    # 5-day return starting from a shock day: shift ret5 back by 5 to align
    post_ret = ret5.shift(-5).shift(5)  # net shift=0 but applied only at shock days
    weighted = shock * ret5.shift(0).shift(5)
    cnt = _rolling_sum(shock, _TD_QTR)
    total = _rolling_sum(shock * close.pct_change(5).shift(-5 + 5), _TD_QTR)
    # Simpler backward-safe version: 5d-ago shock day's subsequent 5d return
    shock_5ago = shock.shift(5).fillna(0.0)
    ret_post = close.pct_change(5)
    product = shock_5ago * ret_post
    cnt2 = _rolling_sum(shock_5ago, _TD_QTR)
    return _safe_div(_rolling_sum(product, _TD_QTR), cnt2.clip(lower=_EPS))


def vsa_049_post_shock_price_gap_pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentage gap of close from shock-day close, signed (negative = below)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_close = close.where(flag == 1.0).ffill()
    return _safe_div(close - shock_close, shock_close.clip(lower=_EPS)) * 100.0


def vsa_050_price_change_on_shock_day_21dz2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close return on the most recent shock day (positive or negative momentum)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    ret = close.pct_change(1)
    shock_ret = ret.where(flag == 1.0).ffill()
    return shock_ret


# --- Group F (051-060): Volume level relative to shock-day level over time ---

def vsa_051_vol_pct_of_shock_day_5d_ewm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day EWM of volume as % of shock-day volume (21d/z2); decay curve."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    ratio = _safe_div(volume, shock_vol.clip(lower=_EPS))
    return _ewm_mean(ratio, _TD_WEEK)


def vsa_052_vol_above_shock_day_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: today's volume still exceeds shock-day volume (no decay yet)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    return (volume >= shock_vol).astype(float)


def vsa_053_vol_half_shock_day_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: today's volume < 50% of shock-day volume (volume halved)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    return (volume < 0.5 * shock_vol).astype(float)


def vsa_054_vol_normalized_by_shock_21d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume / (21d mean at last shock day); measures post-shock vol level."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    mean21 = _rolling_mean(volume, _TD_MON)
    shock_mean = mean21.where(flag == 1.0).ffill()
    return _safe_div(volume, shock_mean.clip(lower=_EPS))


def vsa_055_vol_regime_post_shock_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day EWM of volume ratio to 63-day mean (captures sustained elevated vol)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    return _ewm_mean(ratio, _TD_MON)


def vsa_056_vol_elevated_days_in_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in trailing 21d where volume > 1.5x its 63-day mean."""
    elevated = (_safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS)) > 1.5).astype(float)
    return _rolling_sum(elevated, _TD_MON)


def vsa_057_vol_elevated_days_in_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in trailing 63d where volume > 1.5x its 63-day mean."""
    elevated = (_safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS)) > 1.5).astype(float)
    return _rolling_sum(elevated, _TD_QTR)


def vsa_058_vol_dry_up_consec_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days volume < 0.7x its 21-day mean (volume drying up)."""
    return _consec_streak(
        (_safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS)) < 0.7).astype(bool)
    )


def vsa_059_vol_21d_cv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 21 days (std/mean)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    return _safe_div(s, m.clip(lower=_EPS))


def vsa_060_vol_63d_cv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 63 days."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    return _safe_div(s, m.clip(lower=_EPS))


# --- Group G (061-075): Composite aftermath scores and multi-day metrics ---

def vsa_061_vol_shock_price_impact_21dz2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute return on shock day * shock z-score (impact severity)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    z = _vol_zscore(volume, _TD_MON)
    ret = close.pct_change(1).abs()
    shock_impact = z * ret
    return shock_impact.where(flag == 1.0).ffill().fillna(0.0)


def vsa_062_vol_shock_negative_return_21dz2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: last shock day had a negative close return (panic selling signal)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    ret = close.pct_change(1)
    neg_shock = (flag == 1.0) & (ret < 0.0)
    return neg_shock.astype(float).where(flag == 1.0).ffill().fillna(0.0)


def vsa_063_vol_5d_sum_decay_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day volume sum / 5-to-10-day volume sum (recent vs prior week — decay ratio)."""
    sum_5 = _rolling_sum(volume, _TD_WEEK)
    sum_5_10 = volume.rolling(10, min_periods=5).sum() - sum_5
    return _safe_div(sum_5, sum_5_10.clip(lower=_EPS))


def vsa_064_vol_21d_sum_decay_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume sum / 21-to-42-day volume sum (monthly decay ratio)."""
    sum_21 = _rolling_sum(volume, _TD_MON)
    sum_42 = volume.rolling(42, min_periods=_TD_MON).sum()
    prior = sum_42 - sum_21
    return _safe_div(sum_21, prior.clip(lower=_EPS))


def vsa_065_post_shock_vol_trend_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Normalized slope of volume over 21d (slope/mean); negative = decaying."""
    def slope(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); xm = x.mean()
        num = ((xi - xi_m) * (x - xm)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0 or xm == 0:
            return np.nan
        return (num / den) / abs(xm)
    return volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(slope, raw=True)


def vsa_066_post_shock_price_21d_return(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day trailing return of close (price drift in aftermath window)."""
    return close.pct_change(_TD_MON)


def vsa_067_post_shock_price_5d_return(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day trailing return of close (short-term drift after shock)."""
    return close.pct_change(_TD_WEEK)


def vsa_068_shock_vol_x_neg_return_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 63d of (shock_flag * negative_return); capitulation pressure."""
    flag = _shock_flag(volume, _TD_QTR, 2.0)
    neg_ret = close.pct_change(1).clip(upper=0.0)
    return _rolling_sum(flag * neg_ret.abs(), _TD_QTR)


def vsa_069_vol_max_21d_vs_mean_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max volume in 21 days divided by mean volume in 21 days (spike factor)."""
    mx = _rolling_max(volume, _TD_MON)
    mn = _rolling_mean(volume, _TD_MON)
    return _safe_div(mx, mn.clip(lower=_EPS))


def vsa_070_vol_max_63d_vs_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max volume in 63 days divided by mean volume in 63 days."""
    mx = _rolling_max(volume, _TD_QTR)
    mn = _rolling_mean(volume, _TD_QTR)
    return _safe_div(mx, mn.clip(lower=_EPS))


def vsa_071_vol_percentile_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 21-day distribution."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def vsa_072_vol_percentile_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 63-day distribution."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vsa_073_vol_percentile_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 252-day distribution."""
    return volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vsa_074_shocks_followed_by_new_low_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of shocks in 63d where close 5d later hit a 21d low (backward-safe)."""
    shock_5ago = _shock_flag(volume, _TD_QTR, 2.0).shift(5).fillna(0.0)
    close_5ago = close.shift(5)
    close_min_5ago = close.rolling(_TD_MON, min_periods=5).min().shift(5)
    at_low = (close_5ago <= close_min_5ago * 1.001).astype(float)
    event = shock_5ago * at_low
    return _rolling_sum(event, _TD_QTR)


def vsa_075_vol_shock_aftermath_composite_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: shock count (21d) * vol decay * post-shock negative drift sign."""
    shock_cnt = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON)
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    decay = _safe_div(volume, shock_vol.clip(lower=_EPS)).fillna(1.0)
    drift = close.pct_change(_TD_MON).fillna(0.0)
    neg_drift = (drift < 0.0).astype(float)
    return shock_cnt * decay * neg_drift


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_SHOCK_AFTERMATH_REGISTRY_001_075 = {
    "vsa_001_vol_zscore_21d": {"inputs": ["close", "volume"], "func": vsa_001_vol_zscore_21d},
    "vsa_002_vol_zscore_63d": {"inputs": ["close", "volume"], "func": vsa_002_vol_zscore_63d},
    "vsa_003_vol_zscore_126d": {"inputs": ["close", "volume"], "func": vsa_003_vol_zscore_126d},
    "vsa_004_vol_zscore_252d": {"inputs": ["close", "volume"], "func": vsa_004_vol_zscore_252d},
    "vsa_005_shock_flag_21d_z2": {"inputs": ["close", "volume"], "func": vsa_005_shock_flag_21d_z2},
    "vsa_006_shock_flag_63d_z2": {"inputs": ["close", "volume"], "func": vsa_006_shock_flag_63d_z2},
    "vsa_007_shock_flag_21d_z3": {"inputs": ["close", "volume"], "func": vsa_007_shock_flag_21d_z3},
    "vsa_008_shock_flag_63d_z3": {"inputs": ["close", "volume"], "func": vsa_008_shock_flag_63d_z3},
    "vsa_009_vol_ratio_to_21d_mean": {"inputs": ["close", "volume"], "func": vsa_009_vol_ratio_to_21d_mean},
    "vsa_010_vol_ratio_to_63d_mean": {"inputs": ["close", "volume"], "func": vsa_010_vol_ratio_to_63d_mean},
    "vsa_011_days_since_shock_21d_z2": {"inputs": ["close", "volume"], "func": vsa_011_days_since_shock_21d_z2},
    "vsa_012_days_since_shock_63d_z2": {"inputs": ["close", "volume"], "func": vsa_012_days_since_shock_63d_z2},
    "vsa_013_days_since_shock_21d_z3": {"inputs": ["close", "volume"], "func": vsa_013_days_since_shock_21d_z3},
    "vsa_014_days_since_shock_63d_z3": {"inputs": ["close", "volume"], "func": vsa_014_days_since_shock_63d_z3},
    "vsa_015_days_since_shock_252d_z2": {"inputs": ["close", "volume"], "func": vsa_015_days_since_shock_252d_z2},
    "vsa_016_shock_recency_score_21d": {"inputs": ["close", "volume"], "func": vsa_016_shock_recency_score_21d},
    "vsa_017_shock_recency_score_63d": {"inputs": ["close", "volume"], "func": vsa_017_shock_recency_score_63d},
    "vsa_018_in_aftermath_window_5d": {"inputs": ["close", "volume"], "func": vsa_018_in_aftermath_window_5d},
    "vsa_019_in_aftermath_window_21d": {"inputs": ["close", "volume"], "func": vsa_019_in_aftermath_window_21d},
    "vsa_020_in_aftermath_window_63d": {"inputs": ["close", "volume"], "func": vsa_020_in_aftermath_window_63d},
    "vsa_021_vol_decay_ratio_5d_since_shock": {"inputs": ["close", "volume"], "func": vsa_021_vol_decay_ratio_5d_since_shock},
    "vsa_022_vol_decay_ratio_63d_shock": {"inputs": ["close", "volume"], "func": vsa_022_vol_decay_ratio_63d_shock},
    "vsa_023_post_shock_vol_5d_mean_ratio": {"inputs": ["close", "volume"], "func": vsa_023_post_shock_vol_5d_mean_ratio},
    "vsa_024_post_shock_vol_21d_mean_ratio": {"inputs": ["close", "volume"], "func": vsa_024_post_shock_vol_21d_mean_ratio},
    "vsa_025_vol_half_life_decay_5d": {"inputs": ["close", "volume"], "func": vsa_025_vol_half_life_decay_5d},
    "vsa_026_vol_21d_trend_post_shock": {"inputs": ["close", "volume"], "func": vsa_026_vol_21d_trend_post_shock},
    "vsa_027_vol_5d_trend_post_shock": {"inputs": ["close", "volume"], "func": vsa_027_vol_5d_trend_post_shock},
    "vsa_028_vol_elevated_consec_days_post_shock": {"inputs": ["close", "volume"], "func": vsa_028_vol_elevated_consec_days_post_shock},
    "vsa_029_vol_collapse_flag": {"inputs": ["close", "volume"], "func": vsa_029_vol_collapse_flag},
    "vsa_030_vol_5d_sum_vs_21d_avg_sum": {"inputs": ["close", "volume"], "func": vsa_030_vol_5d_sum_vs_21d_avg_sum},
    "vsa_031_shock_count_21d_z2": {"inputs": ["close", "volume"], "func": vsa_031_shock_count_21d_z2},
    "vsa_032_shock_count_63d_z2": {"inputs": ["close", "volume"], "func": vsa_032_shock_count_63d_z2},
    "vsa_033_shock_count_252d_z2": {"inputs": ["close", "volume"], "func": vsa_033_shock_count_252d_z2},
    "vsa_034_shock_count_21d_z3": {"inputs": ["close", "volume"], "func": vsa_034_shock_count_21d_z3},
    "vsa_035_shock_count_63d_z3": {"inputs": ["close", "volume"], "func": vsa_035_shock_count_63d_z3},
    "vsa_036_shock_density_21d": {"inputs": ["close", "volume"], "func": vsa_036_shock_density_21d},
    "vsa_037_shock_density_63d": {"inputs": ["close", "volume"], "func": vsa_037_shock_density_63d},
    "vsa_038_shock_density_252d": {"inputs": ["close", "volume"], "func": vsa_038_shock_density_252d},
    "vsa_039_multi_shock_in_5d_flag": {"inputs": ["close", "volume"], "func": vsa_039_multi_shock_in_5d_flag},
    "vsa_040_shock_cluster_consec": {"inputs": ["close", "volume"], "func": vsa_040_shock_cluster_consec},
    "vsa_041_price_return_since_shock_21dz2": {"inputs": ["close", "volume"], "func": vsa_041_price_return_since_shock_21dz2},
    "vsa_042_price_return_since_shock_63dz2": {"inputs": ["close", "volume"], "func": vsa_042_price_return_since_shock_63dz2},
    "vsa_043_price_return_since_shock_21dz3": {"inputs": ["close", "volume"], "func": vsa_043_price_return_since_shock_21dz3},
    "vsa_044_post_shock_price_drawdown_21d": {"inputs": ["close", "volume"], "func": vsa_044_post_shock_price_drawdown_21d},
    "vsa_045_post_shock_close_below_shock_close_flag": {"inputs": ["close", "volume"], "func": vsa_045_post_shock_close_below_shock_close_flag},
    "vsa_046_shocks_followed_by_decline_count_63d": {"inputs": ["close", "volume"], "func": vsa_046_shocks_followed_by_decline_count_63d},
    "vsa_047_shocks_followed_by_decline_count_252d": {"inputs": ["close", "volume"], "func": vsa_047_shocks_followed_by_decline_count_252d},
    "vsa_048_post_shock_5d_return_avg_63d": {"inputs": ["close", "volume"], "func": vsa_048_post_shock_5d_return_avg_63d},
    "vsa_049_post_shock_price_gap_pct": {"inputs": ["close", "volume"], "func": vsa_049_post_shock_price_gap_pct},
    "vsa_050_price_change_on_shock_day_21dz2": {"inputs": ["close", "volume"], "func": vsa_050_price_change_on_shock_day_21dz2},
    "vsa_051_vol_pct_of_shock_day_5d_ewm": {"inputs": ["close", "volume"], "func": vsa_051_vol_pct_of_shock_day_5d_ewm},
    "vsa_052_vol_above_shock_day_flag": {"inputs": ["close", "volume"], "func": vsa_052_vol_above_shock_day_flag},
    "vsa_053_vol_half_shock_day_flag": {"inputs": ["close", "volume"], "func": vsa_053_vol_half_shock_day_flag},
    "vsa_054_vol_normalized_by_shock_21d_mean": {"inputs": ["close", "volume"], "func": vsa_054_vol_normalized_by_shock_21d_mean},
    "vsa_055_vol_regime_post_shock_ewm21": {"inputs": ["close", "volume"], "func": vsa_055_vol_regime_post_shock_ewm21},
    "vsa_056_vol_elevated_days_in_21d": {"inputs": ["close", "volume"], "func": vsa_056_vol_elevated_days_in_21d},
    "vsa_057_vol_elevated_days_in_63d": {"inputs": ["close", "volume"], "func": vsa_057_vol_elevated_days_in_63d},
    "vsa_058_vol_dry_up_consec_days": {"inputs": ["close", "volume"], "func": vsa_058_vol_dry_up_consec_days},
    "vsa_059_vol_21d_cv": {"inputs": ["close", "volume"], "func": vsa_059_vol_21d_cv},
    "vsa_060_vol_63d_cv": {"inputs": ["close", "volume"], "func": vsa_060_vol_63d_cv},
    "vsa_061_vol_shock_price_impact_21dz2": {"inputs": ["close", "volume"], "func": vsa_061_vol_shock_price_impact_21dz2},
    "vsa_062_vol_shock_negative_return_21dz2": {"inputs": ["close", "volume"], "func": vsa_062_vol_shock_negative_return_21dz2},
    "vsa_063_vol_5d_sum_decay_ratio": {"inputs": ["close", "volume"], "func": vsa_063_vol_5d_sum_decay_ratio},
    "vsa_064_vol_21d_sum_decay_ratio": {"inputs": ["close", "volume"], "func": vsa_064_vol_21d_sum_decay_ratio},
    "vsa_065_post_shock_vol_trend_slope_21d": {"inputs": ["close", "volume"], "func": vsa_065_post_shock_vol_trend_slope_21d},
    "vsa_066_post_shock_price_21d_return": {"inputs": ["close", "volume"], "func": vsa_066_post_shock_price_21d_return},
    "vsa_067_post_shock_price_5d_return": {"inputs": ["close", "volume"], "func": vsa_067_post_shock_price_5d_return},
    "vsa_068_shock_vol_x_neg_return_sum_63d": {"inputs": ["close", "volume"], "func": vsa_068_shock_vol_x_neg_return_sum_63d},
    "vsa_069_vol_max_21d_vs_mean_21d": {"inputs": ["close", "volume"], "func": vsa_069_vol_max_21d_vs_mean_21d},
    "vsa_070_vol_max_63d_vs_mean_63d": {"inputs": ["close", "volume"], "func": vsa_070_vol_max_63d_vs_mean_63d},
    "vsa_071_vol_percentile_rank_21d": {"inputs": ["close", "volume"], "func": vsa_071_vol_percentile_rank_21d},
    "vsa_072_vol_percentile_rank_63d": {"inputs": ["close", "volume"], "func": vsa_072_vol_percentile_rank_63d},
    "vsa_073_vol_percentile_rank_252d": {"inputs": ["close", "volume"], "func": vsa_073_vol_percentile_rank_252d},
    "vsa_074_shocks_followed_by_new_low_count_63d": {"inputs": ["close", "volume"], "func": vsa_074_shocks_followed_by_new_low_count_63d},
    "vsa_075_vol_shock_aftermath_composite_score": {"inputs": ["close", "volume"], "func": vsa_075_vol_shock_aftermath_composite_score},
}
