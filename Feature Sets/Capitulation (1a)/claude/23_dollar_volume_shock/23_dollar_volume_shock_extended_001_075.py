"""
23_dollar_volume_shock — Extended Features 001-075
Domain: dollar-volume spikes and turnover extremes — VWAP, Amihud illiquidity, deeper signals
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Prefix: dvs_ext
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _dv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume: close * volume."""
    return close * volume


def _typical_price(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Typical price: (high + low + close) / 3."""
    return (high + low + close) / 3.0


def _vwap_rolling(high: pd.Series, low: pd.Series, close: pd.Series,
                  volume: pd.Series, w: int) -> pd.Series:
    """Rolling VWAP: sum(typical_price * volume, w) / sum(volume, w)."""
    tp = _typical_price(high, low, close)
    tp_vol = tp * volume
    return _safe_div(_rolling_sum(tp_vol, w), _rolling_sum(volume, w))


def _amihud_daily(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud illiquidity ratio: |return| / dollar_volume."""
    ret = close.pct_change(1).abs()
    dv = _dv(close, volume)
    return _safe_div(ret, dv.replace(0, np.nan))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Rolling VWAP — levels and price distance ---

def dvs_ext_001_vwap_5d(high: pd.Series, low: pd.Series, close: pd.Series,
                         volume: pd.Series) -> pd.Series:
    """5-day rolling VWAP (typical-price-weighted)."""
    return _vwap_rolling(high, low, close, volume, _TD_WEEK)


def dvs_ext_002_vwap_21d(high: pd.Series, low: pd.Series, close: pd.Series,
                          volume: pd.Series) -> pd.Series:
    """21-day rolling VWAP."""
    return _vwap_rolling(high, low, close, volume, _TD_MON)


def dvs_ext_003_vwap_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                          volume: pd.Series) -> pd.Series:
    """63-day rolling VWAP."""
    return _vwap_rolling(high, low, close, volume, _TD_QTR)


def dvs_ext_004_vwap_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                           volume: pd.Series) -> pd.Series:
    """252-day rolling VWAP."""
    return _vwap_rolling(high, low, close, volume, _TD_YEAR)


def dvs_ext_005_price_dist_vwap_5d(high: pd.Series, low: pd.Series, close: pd.Series,
                                    volume: pd.Series) -> pd.Series:
    """Price distance from 5-day VWAP: close / VWAP_5d - 1."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_WEEK)
    return _safe_div(close, vwap) - 1.0


def dvs_ext_006_price_dist_vwap_21d(high: pd.Series, low: pd.Series, close: pd.Series,
                                     volume: pd.Series) -> pd.Series:
    """Price distance from 21-day VWAP: close / VWAP_21d - 1."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_MON)
    return _safe_div(close, vwap) - 1.0


def dvs_ext_007_price_dist_vwap_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                     volume: pd.Series) -> pd.Series:
    """Price distance from 63-day VWAP: close / VWAP_63d - 1."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_QTR)
    return _safe_div(close, vwap) - 1.0


def dvs_ext_008_price_dist_vwap_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                      volume: pd.Series) -> pd.Series:
    """Price distance from 252-day VWAP: close / VWAP_252d - 1."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_YEAR)
    return _safe_div(close, vwap) - 1.0


def dvs_ext_009_depth_below_vwap_21d(high: pd.Series, low: pd.Series, close: pd.Series,
                                      volume: pd.Series) -> pd.Series:
    """Depth below 21-day VWAP: max(0, VWAP_21d - close) / VWAP_21d (floor at 0)."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_MON)
    below = (vwap - close).clip(lower=0.0)
    return _safe_div(below, vwap)


def dvs_ext_010_depth_below_vwap_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                      volume: pd.Series) -> pd.Series:
    """Depth below 63-day VWAP: max(0, VWAP_63d - close) / VWAP_63d."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_QTR)
    below = (vwap - close).clip(lower=0.0)
    return _safe_div(below, vwap)


# --- Group B (011-018): VWAP slope, streak, z-score ---

def dvs_ext_011_vwap_21d_slope(high: pd.Series, low: pd.Series, close: pd.Series,
                                volume: pd.Series) -> pd.Series:
    """5-day percent change of 21-day VWAP (VWAP trend/slope)."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_MON)
    return vwap.pct_change(_TD_WEEK)


def dvs_ext_012_vwap_63d_slope(high: pd.Series, low: pd.Series, close: pd.Series,
                                volume: pd.Series) -> pd.Series:
    """21-day percent change of 63-day VWAP."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_QTR)
    return vwap.pct_change(_TD_MON)


def dvs_ext_013_days_below_vwap_21d_streak(high: pd.Series, low: pd.Series, close: pd.Series,
                                            volume: pd.Series) -> pd.Series:
    """Consecutive days where close < 21-day VWAP (below-VWAP streak)."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_MON)
    cond = close < vwap
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dvs_ext_014_days_below_vwap_63d_streak(high: pd.Series, low: pd.Series, close: pd.Series,
                                            volume: pd.Series) -> pd.Series:
    """Consecutive days where close < 63-day VWAP."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_QTR)
    cond = close < vwap
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dvs_ext_015_vwap_21d_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                     volume: pd.Series) -> pd.Series:
    """Z-score of price-distance-from-21d-VWAP over 63-day rolling window."""
    dist = dvs_ext_006_price_dist_vwap_21d(high, low, close, volume)
    m = _rolling_mean(dist, _TD_QTR)
    s = _rolling_std(dist, _TD_QTR)
    return _safe_div(dist - m, s)


def dvs_ext_016_vwap_63d_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                      volume: pd.Series) -> pd.Series:
    """Z-score of price-distance-from-63d-VWAP over 252-day rolling window."""
    dist = dvs_ext_007_price_dist_vwap_63d(high, low, close, volume)
    m = _rolling_mean(dist, _TD_YEAR)
    s = _rolling_std(dist, _TD_YEAR)
    return _safe_div(dist - m, s)


def dvs_ext_017_count_below_vwap_21d_in_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                              volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where close was below 21-day VWAP."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_MON)
    below = (close < vwap).astype(float)
    return _rolling_sum(below, _TD_QTR)


def dvs_ext_018_vwap_band_position_21d(high: pd.Series, low: pd.Series, close: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """Close position within [VWAP_21d - 1std, VWAP_21d + 1std] band; 0=bottom, 1=top."""
    vwap = _vwap_rolling(high, low, close, volume, _TD_MON)
    dist = close - vwap
    s = _rolling_std(dist, _TD_MON)
    band_low = vwap - s
    band_high = vwap + s
    return _safe_div(close - band_low, band_high - band_low)


# --- Group C (019-030): Amihud illiquidity ratio ---

def dvs_ext_019_amihud_daily(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud illiquidity: |return| / dollar_volume (raw, unaveraged)."""
    return _amihud_daily(close, volume)


def dvs_ext_020_amihud_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity ratio averaged over trailing 21 days."""
    daily = _amihud_daily(close, volume)
    return _rolling_mean(daily, _TD_MON)


def dvs_ext_021_amihud_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity ratio averaged over trailing 63 days."""
    daily = _amihud_daily(close, volume)
    return _rolling_mean(daily, _TD_QTR)


def dvs_ext_022_amihud_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity ratio averaged over trailing 252 days."""
    daily = _amihud_daily(close, volume)
    return _rolling_mean(daily, _TD_YEAR)


def dvs_ext_023_amihud_log_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of 21-day average Amihud illiquidity (log scale for skewed distribution)."""
    return _log_safe(dvs_ext_020_amihud_21d(close, volume))


def dvs_ext_024_amihud_log_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of 63-day average Amihud illiquidity."""
    return _log_safe(dvs_ext_021_amihud_63d(close, volume))


def dvs_ext_025_amihud_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day Amihud vs its own 63-day distribution."""
    amihud21 = dvs_ext_020_amihud_21d(close, volume)
    m = _rolling_mean(amihud21, _TD_QTR)
    s = _rolling_std(amihud21, _TD_QTR)
    return _safe_div(amihud21 - m, s)


def dvs_ext_026_amihud_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day Amihud vs its own 252-day distribution."""
    amihud21 = dvs_ext_020_amihud_21d(close, volume)
    m = _rolling_mean(amihud21, _TD_YEAR)
    s = _rolling_std(amihud21, _TD_YEAR)
    return _safe_div(amihud21 - m, s)


def dvs_ext_027_amihud_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Amihud within trailing 252-day distribution."""
    amihud21 = dvs_ext_020_amihud_21d(close, volume)
    return amihud21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dvs_ext_028_amihud_spike_flag_2x(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: daily Amihud > 2x its 63-day mean (illiquidity spike)."""
    daily = _amihud_daily(close, volume)
    baseline = _rolling_mean(daily, _TD_QTR)
    return (daily > 2.0 * baseline).astype(float)


def dvs_ext_029_amihud_spike_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Amihud 2x-spike days in trailing 21 days."""
    daily = _amihud_daily(close, volume)
    baseline = _rolling_mean(daily, _TD_QTR)
    spike = (daily > 2.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_MON)


def dvs_ext_030_amihud_spike_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Amihud 2x-spike days in trailing 63 days."""
    daily = _amihud_daily(close, volume)
    baseline = _rolling_mean(daily, _TD_QTR)
    spike = (daily > 2.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_QTR)


# --- Group D (031-040): Amihud deeper signals and interactions ---

def dvs_ext_031_amihud_21d_vs_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day Amihud to 252-day Amihud (recent illiquidity vs long baseline)."""
    return _safe_div(dvs_ext_020_amihud_21d(close, volume),
                     dvs_ext_022_amihud_252d(close, volume))


def dvs_ext_032_amihud_expanding_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of daily Amihud (all-history illiquidity rank)."""
    daily = _amihud_daily(close, volume)
    return daily.expanding(min_periods=5).rank(pct=True)


def dvs_ext_033_amihud_on_down_day_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean Amihud illiquidity on down-price days over trailing 21 days."""
    daily = _amihud_daily(close, volume)
    ret = close.pct_change(1)
    amihud_dn = daily.where(ret < 0, np.nan)
    return amihud_dn.rolling(_TD_MON, min_periods=1).mean()


def dvs_ext_034_amihud_63d_slope(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day percent change in 63-day Amihud (trend in illiquidity)."""
    amihud63 = dvs_ext_021_amihud_63d(close, volume)
    return amihud63.pct_change(_TD_MON)


def dvs_ext_035_amihud_21d_mad_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Robust z-score of 21-day Amihud: (amihud - median) / MAD over 63 days."""
    amihud21 = dvs_ext_020_amihud_21d(close, volume)
    med = _rolling_median(amihud21, _TD_QTR)
    mad = (amihud21 - med).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).median()
    return _safe_div(amihud21 - med, mad)


def dvs_ext_036_amihud_price_collapse_interaction(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud times magnitude of daily return (distress intensity = illiq * move)."""
    daily_amihud = _amihud_daily(close, volume)
    ret = close.pct_change(1).abs()
    return daily_amihud * ret


def dvs_ext_037_amihud_21d_top_decile_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 21-day Amihud is in top 10% of its 252-day distribution (extreme illiquidity)."""
    amihud21 = dvs_ext_020_amihud_21d(close, volume)
    rank = amihud21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (rank >= 0.90).astype(float)


def dvs_ext_038_amihud_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Exponentially weighted 21-span mean of daily Amihud illiquidity."""
    daily = _amihud_daily(close, volume)
    return _ewm_mean(daily, _TD_MON)


def dvs_ext_039_amihud_trend_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day Amihud (velocity of illiquidity change)."""
    amihud21 = dvs_ext_020_amihud_21d(close, volume)
    return amihud21.diff(_TD_WEEK)


def dvs_ext_040_amihud_spike_on_down_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 63d with Amihud 2x-spike AND price decline (illiquid sell-off)."""
    daily = _amihud_daily(close, volume)
    baseline = _rolling_mean(daily, _TD_QTR)
    ret = close.pct_change(1)
    spike_dn = ((daily > 2.0 * baseline) & (ret < 0)).astype(float)
    return _rolling_sum(spike_dn, _TD_QTR)


# --- Group E (041-050): Dollar-volume vs extended baselines ---

def dvs_ext_041_dv_ratio_10d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 10-day trailing mean (very short baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_mean(dv, 10))


def dvs_ext_042_dv_ratio_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 42-day trailing mean (2-month baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_mean(dv, 42))


def dvs_ext_043_dv_zscore_10d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar volume over 10-day rolling window."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, 10)
    s = _rolling_std(dv, 10)
    return _safe_div(dv - m, s)


def dvs_ext_044_dv_ratio_ewm5(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 5-day EWM mean (ultra-short exponential baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _ewm_mean(dv, _TD_WEEK))


def dvs_ext_045_dv_ratio_ewm126(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 126-day EWM mean (half-year exponential baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _ewm_mean(dv, _TD_HALF))


def dvs_ext_046_dv_ratio_ewm252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 252-day EWM mean (annual exponential baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _ewm_mean(dv, _TD_YEAR))


def dvs_ext_047_dv_log_ratio_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of dollar volume divided by 126-day mean (log-scale half-year comparison)."""
    dv = _dv(close, volume)
    return _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_HALF))


def dvs_ext_048_dv_turnover_shock_zscore_21d_vs_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day mean DV relative to 63-day distribution of 21d means."""
    dv = _dv(close, volume)
    mean21 = _rolling_mean(dv, _TD_MON)
    m = _rolling_mean(mean21, _TD_QTR)
    s = _rolling_std(mean21, _TD_QTR)
    return _safe_div(mean21 - m, s)


def dvs_ext_049_dv_turnover_shock_zscore_5d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 5-day mean DV relative to 252-day distribution of 5d means."""
    dv = _dv(close, volume)
    mean5 = _rolling_mean(dv, _TD_WEEK)
    m = _rolling_mean(mean5, _TD_YEAR)
    s = _rolling_std(mean5, _TD_YEAR)
    return _safe_div(mean5 - m, s)


def dvs_ext_050_dv_10d_vs_126d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 10-day mean DV to 126-day mean DV (acute vs semi-annual baseline)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_mean(dv, 10), _rolling_mean(dv, _TD_HALF))


# --- Group F (051-060): Dollar-volume drought (collapse) signals ---

def dvs_ext_051_dv_drought_flag_below50pct_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current DV is below 50% of its 252-day mean (DV drought / collapse)."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_YEAR)
    return (dv < 0.5 * baseline).astype(float)


def dvs_ext_052_dv_drought_flag_below25pct_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current DV is below 25% of its 252-day mean (severe DV drought)."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_YEAR)
    return (dv < 0.25 * baseline).astype(float)


def dvs_ext_053_dv_drought_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of DV-drought days (DV < 50% of 252d mean) in trailing 21 days."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_YEAR)
    drought = (dv < 0.5 * baseline).astype(float)
    return _rolling_sum(drought, _TD_MON)


def dvs_ext_054_dv_drought_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of DV-drought days (DV < 50% of 252d mean) in trailing 63 days."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_YEAR)
    drought = (dv < 0.5 * baseline).astype(float)
    return _rolling_sum(drought, _TD_QTR)


def dvs_ext_055_dv_min_vs_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day minimum DV divided by 63-day mean DV (drought severity ratio)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_min(dv, _TD_QTR), _rolling_mean(dv, _TD_QTR))


def dvs_ext_056_dv_collapse_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent change in 5-day mean DV from 5 days ago (acute collapse detector)."""
    dv = _dv(close, volume)
    mean5 = _rolling_mean(dv, _TD_WEEK)
    return mean5.pct_change(_TD_WEEK)


def dvs_ext_057_dv_collapse_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 5-day DV collapse signal vs 252-day distribution."""
    dv = _dv(close, volume)
    mean5 = _rolling_mean(dv, _TD_WEEK)
    chg = mean5.pct_change(_TD_WEEK)
    m = _rolling_mean(chg, _TD_YEAR)
    s = _rolling_std(chg, _TD_YEAR)
    return _safe_div(chg - m, s)


def dvs_ext_058_dv_below_ewm63_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days where DV < its 63-day EWM (sustained volume drought)."""
    dv = _dv(close, volume)
    ewm63 = _ewm_mean(dv, _TD_QTR)
    cond = dv < ewm63
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dvs_ext_059_dv_low_pct_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current DV is in the bottom 10% of its 252-day distribution (drought extreme)."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (rank <= 0.10).astype(float)


def dvs_ext_060_dv_drought_then_spike_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current day is a 2x-DV spike following 5+ drought days (reversal signature)."""
    dv = _dv(close, volume)
    baseline_252 = _rolling_mean(dv, _TD_YEAR)
    baseline_63 = _rolling_mean(dv, _TD_QTR)
    drought = (dv < 0.5 * baseline_252).astype(float)
    drought_streak = drought.rolling(_TD_WEEK, min_periods=_TD_WEEK).sum()
    recent_drought = drought_streak.shift(1) >= 5.0
    spike_today = dv > 2.0 * baseline_63
    return (spike_today & recent_drought).astype(float)


# --- Group G (061-068): Cumulative dollar volume and concentration ---

def dvs_ext_061_dv_cumsum_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding cumulative dollar volume (total dollar value traded since inception)."""
    dv = _dv(close, volume)
    return dv.expanding(min_periods=1).sum()


def dvs_ext_062_dv_sum_5d_vs_sum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day cumulative DV to 21-day cumulative DV (recency concentration, short)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_sum(dv, _TD_WEEK), _rolling_sum(dv, _TD_MON))


def dvs_ext_063_dv_sum_5d_vs_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day cumulative DV to 63-day cumulative DV."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_sum(dv, _TD_WEEK), _rolling_sum(dv, _TD_QTR))


def dvs_ext_064_dv_concentration_top1_in_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day total DV accounted for by the single largest day."""
    dv = _dv(close, volume)
    max21 = _rolling_max(dv, _TD_MON)
    sum21 = _rolling_sum(dv, _TD_MON)
    return _safe_div(max21, sum21)


def dvs_ext_065_dv_concentration_top1_in_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day total DV accounted for by the single largest day."""
    dv = _dv(close, volume)
    max63 = _rolling_max(dv, _TD_QTR)
    sum63 = _rolling_sum(dv, _TD_QTR)
    return _safe_div(max63, sum63)


def dvs_ext_066_dv_cumsum_252d_pct_change_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day percent change in rolling 252-day cumulative DV (annual DV trend)."""
    dv = _dv(close, volume)
    sum252 = _rolling_sum(dv, _TD_YEAR)
    return sum252.pct_change(_TD_QTR)


def dvs_ext_067_dv_cumsum_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day cumulative DV vs 252-day distribution of 21d sums."""
    dv = _dv(close, volume)
    sum21 = _rolling_sum(dv, _TD_MON)
    m = _rolling_mean(sum21, _TD_YEAR)
    s = _rolling_std(sum21, _TD_YEAR)
    return _safe_div(sum21 - m, s)


def dvs_ext_068_dv_cumsum_63d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day cumulative DV vs 252-day distribution of 63d sums."""
    dv = _dv(close, volume)
    sum63 = _rolling_sum(dv, _TD_QTR)
    m = _rolling_mean(sum63, _TD_YEAR)
    s = _rolling_std(sum63, _TD_YEAR)
    return _safe_div(sum63 - m, s)


# --- Group H (069-075): Return-per-dollar-volume sensitivity and composite ---

def dvs_ext_069_return_per_dv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean of |daily return| / dollar_volume — price sensitivity per dollar traded."""
    return dvs_ext_020_amihud_21d(close, volume)


def dvs_ext_070_return_per_dv_sensitivity_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day mean Amihud to 63-day mean Amihud (sensitivity spike vs baseline)."""
    daily = _amihud_daily(close, volume)
    mean5 = _rolling_mean(daily, _TD_WEEK)
    mean63 = _rolling_mean(daily, _TD_QTR)
    return _safe_div(mean5, mean63)


def dvs_ext_071_dv_trend_ewm_crossover(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM5 minus EWM63 of dollar volume normalized by EWM63 (trend crossover signal)."""
    dv = _dv(close, volume)
    e5 = _ewm_mean(dv, _TD_WEEK)
    e63 = _ewm_mean(dv, _TD_QTR)
    return _safe_div(e5 - e63, e63)


def dvs_ext_072_dv_roc_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of change of dollar volume over 21 days: (dv - dv_21ago) / dv_21ago."""
    dv = _dv(close, volume)
    return _safe_div(dv - dv.shift(_TD_MON), dv.shift(_TD_MON).replace(0, np.nan))


def dvs_ext_073_dv_roc_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of change of dollar volume over 63 days: (dv - dv_63ago) / dv_63ago."""
    dv = _dv(close, volume)
    return _safe_div(dv - dv.shift(_TD_QTR), dv.shift(_TD_QTR).replace(0, np.nan))


def dvs_ext_074_amihud_vwap_interaction_21d(close: pd.Series, high: pd.Series,
                                             low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean of (Amihud * depth_below_vwap_21d): joint illiquidity + price dislocation."""
    daily_amihud = _amihud_daily(close, volume)
    vwap = _vwap_rolling(high, low, close, volume, _TD_MON)
    below = (vwap - close).clip(lower=0.0)
    depth = _safe_div(below, vwap)
    return _rolling_mean(daily_amihud * depth, _TD_MON)


def dvs_ext_075_dv_illiquidity_composite(close: pd.Series, high: pd.Series,
                                          low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite illiquidity: Amihud_zscore_252d * depth_below_vwap_63d (fragility score)."""
    amihud21 = dvs_ext_020_amihud_21d(close, volume)
    m = _rolling_mean(amihud21, _TD_YEAR)
    s = _rolling_std(amihud21, _TD_YEAR)
    amihud_z = _safe_div(amihud21 - m, s)
    vwap63 = _vwap_rolling(high, low, close, volume, _TD_QTR)
    below = (vwap63 - close).clip(lower=0.0)
    depth = _safe_div(below, vwap63)
    return amihud_z * (1.0 + depth)


# ── Registry ──────────────────────────────────────────────────────────────────

DOLLAR_VOLUME_SHOCK_EXTENDED_REGISTRY_001_075 = {
    "dvs_ext_001_vwap_5d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_001_vwap_5d},
    "dvs_ext_002_vwap_21d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_002_vwap_21d},
    "dvs_ext_003_vwap_63d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_003_vwap_63d},
    "dvs_ext_004_vwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_004_vwap_252d},
    "dvs_ext_005_price_dist_vwap_5d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_005_price_dist_vwap_5d},
    "dvs_ext_006_price_dist_vwap_21d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_006_price_dist_vwap_21d},
    "dvs_ext_007_price_dist_vwap_63d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_007_price_dist_vwap_63d},
    "dvs_ext_008_price_dist_vwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_008_price_dist_vwap_252d},
    "dvs_ext_009_depth_below_vwap_21d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_009_depth_below_vwap_21d},
    "dvs_ext_010_depth_below_vwap_63d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_010_depth_below_vwap_63d},
    "dvs_ext_011_vwap_21d_slope": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_011_vwap_21d_slope},
    "dvs_ext_012_vwap_63d_slope": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_012_vwap_63d_slope},
    "dvs_ext_013_days_below_vwap_21d_streak": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_013_days_below_vwap_21d_streak},
    "dvs_ext_014_days_below_vwap_63d_streak": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_014_days_below_vwap_63d_streak},
    "dvs_ext_015_vwap_21d_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_015_vwap_21d_zscore_63d},
    "dvs_ext_016_vwap_63d_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_016_vwap_63d_zscore_252d},
    "dvs_ext_017_count_below_vwap_21d_in_63d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_017_count_below_vwap_21d_in_63d},
    "dvs_ext_018_vwap_band_position_21d": {"inputs": ["high", "low", "close", "volume"], "func": dvs_ext_018_vwap_band_position_21d},
    "dvs_ext_019_amihud_daily": {"inputs": ["close", "volume"], "func": dvs_ext_019_amihud_daily},
    "dvs_ext_020_amihud_21d": {"inputs": ["close", "volume"], "func": dvs_ext_020_amihud_21d},
    "dvs_ext_021_amihud_63d": {"inputs": ["close", "volume"], "func": dvs_ext_021_amihud_63d},
    "dvs_ext_022_amihud_252d": {"inputs": ["close", "volume"], "func": dvs_ext_022_amihud_252d},
    "dvs_ext_023_amihud_log_21d": {"inputs": ["close", "volume"], "func": dvs_ext_023_amihud_log_21d},
    "dvs_ext_024_amihud_log_63d": {"inputs": ["close", "volume"], "func": dvs_ext_024_amihud_log_63d},
    "dvs_ext_025_amihud_zscore_63d": {"inputs": ["close", "volume"], "func": dvs_ext_025_amihud_zscore_63d},
    "dvs_ext_026_amihud_zscore_252d": {"inputs": ["close", "volume"], "func": dvs_ext_026_amihud_zscore_252d},
    "dvs_ext_027_amihud_pct_rank_252d": {"inputs": ["close", "volume"], "func": dvs_ext_027_amihud_pct_rank_252d},
    "dvs_ext_028_amihud_spike_flag_2x": {"inputs": ["close", "volume"], "func": dvs_ext_028_amihud_spike_flag_2x},
    "dvs_ext_029_amihud_spike_count_21d": {"inputs": ["close", "volume"], "func": dvs_ext_029_amihud_spike_count_21d},
    "dvs_ext_030_amihud_spike_count_63d": {"inputs": ["close", "volume"], "func": dvs_ext_030_amihud_spike_count_63d},
    "dvs_ext_031_amihud_21d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": dvs_ext_031_amihud_21d_vs_252d_ratio},
    "dvs_ext_032_amihud_expanding_pct_rank": {"inputs": ["close", "volume"], "func": dvs_ext_032_amihud_expanding_pct_rank},
    "dvs_ext_033_amihud_on_down_day_21d": {"inputs": ["close", "volume"], "func": dvs_ext_033_amihud_on_down_day_21d},
    "dvs_ext_034_amihud_63d_slope": {"inputs": ["close", "volume"], "func": dvs_ext_034_amihud_63d_slope},
    "dvs_ext_035_amihud_21d_mad_zscore": {"inputs": ["close", "volume"], "func": dvs_ext_035_amihud_21d_mad_zscore},
    "dvs_ext_036_amihud_price_collapse_interaction": {"inputs": ["close", "volume"], "func": dvs_ext_036_amihud_price_collapse_interaction},
    "dvs_ext_037_amihud_21d_top_decile_flag_252d": {"inputs": ["close", "volume"], "func": dvs_ext_037_amihud_21d_top_decile_flag_252d},
    "dvs_ext_038_amihud_ewm21": {"inputs": ["close", "volume"], "func": dvs_ext_038_amihud_ewm21},
    "dvs_ext_039_amihud_trend_5d_diff": {"inputs": ["close", "volume"], "func": dvs_ext_039_amihud_trend_5d_diff},
    "dvs_ext_040_amihud_spike_on_down_day_count_63d": {"inputs": ["close", "volume"], "func": dvs_ext_040_amihud_spike_on_down_day_count_63d},
    "dvs_ext_041_dv_ratio_10d": {"inputs": ["close", "volume"], "func": dvs_ext_041_dv_ratio_10d},
    "dvs_ext_042_dv_ratio_42d": {"inputs": ["close", "volume"], "func": dvs_ext_042_dv_ratio_42d},
    "dvs_ext_043_dv_zscore_10d": {"inputs": ["close", "volume"], "func": dvs_ext_043_dv_zscore_10d},
    "dvs_ext_044_dv_ratio_ewm5": {"inputs": ["close", "volume"], "func": dvs_ext_044_dv_ratio_ewm5},
    "dvs_ext_045_dv_ratio_ewm126": {"inputs": ["close", "volume"], "func": dvs_ext_045_dv_ratio_ewm126},
    "dvs_ext_046_dv_ratio_ewm252": {"inputs": ["close", "volume"], "func": dvs_ext_046_dv_ratio_ewm252},
    "dvs_ext_047_dv_log_ratio_126d": {"inputs": ["close", "volume"], "func": dvs_ext_047_dv_log_ratio_126d},
    "dvs_ext_048_dv_turnover_shock_zscore_21d_vs_63d": {"inputs": ["close", "volume"], "func": dvs_ext_048_dv_turnover_shock_zscore_21d_vs_63d},
    "dvs_ext_049_dv_turnover_shock_zscore_5d_vs_252d": {"inputs": ["close", "volume"], "func": dvs_ext_049_dv_turnover_shock_zscore_5d_vs_252d},
    "dvs_ext_050_dv_10d_vs_126d_ratio": {"inputs": ["close", "volume"], "func": dvs_ext_050_dv_10d_vs_126d_ratio},
    "dvs_ext_051_dv_drought_flag_below50pct_21d": {"inputs": ["close", "volume"], "func": dvs_ext_051_dv_drought_flag_below50pct_21d},
    "dvs_ext_052_dv_drought_flag_below25pct_21d": {"inputs": ["close", "volume"], "func": dvs_ext_052_dv_drought_flag_below25pct_21d},
    "dvs_ext_053_dv_drought_count_21d": {"inputs": ["close", "volume"], "func": dvs_ext_053_dv_drought_count_21d},
    "dvs_ext_054_dv_drought_count_63d": {"inputs": ["close", "volume"], "func": dvs_ext_054_dv_drought_count_63d},
    "dvs_ext_055_dv_min_vs_mean_63d": {"inputs": ["close", "volume"], "func": dvs_ext_055_dv_min_vs_mean_63d},
    "dvs_ext_056_dv_collapse_5d": {"inputs": ["close", "volume"], "func": dvs_ext_056_dv_collapse_5d},
    "dvs_ext_057_dv_collapse_zscore_21d": {"inputs": ["close", "volume"], "func": dvs_ext_057_dv_collapse_zscore_21d},
    "dvs_ext_058_dv_below_ewm63_streak": {"inputs": ["close", "volume"], "func": dvs_ext_058_dv_below_ewm63_streak},
    "dvs_ext_059_dv_low_pct_rank_21d": {"inputs": ["close", "volume"], "func": dvs_ext_059_dv_low_pct_rank_21d},
    "dvs_ext_060_dv_drought_then_spike_flag": {"inputs": ["close", "volume"], "func": dvs_ext_060_dv_drought_then_spike_flag},
    "dvs_ext_061_dv_cumsum_expanding": {"inputs": ["close", "volume"], "func": dvs_ext_061_dv_cumsum_expanding},
    "dvs_ext_062_dv_sum_5d_vs_sum_21d": {"inputs": ["close", "volume"], "func": dvs_ext_062_dv_sum_5d_vs_sum_21d},
    "dvs_ext_063_dv_sum_5d_vs_sum_63d": {"inputs": ["close", "volume"], "func": dvs_ext_063_dv_sum_5d_vs_sum_63d},
    "dvs_ext_064_dv_concentration_top1_in_21d": {"inputs": ["close", "volume"], "func": dvs_ext_064_dv_concentration_top1_in_21d},
    "dvs_ext_065_dv_concentration_top1_in_63d": {"inputs": ["close", "volume"], "func": dvs_ext_065_dv_concentration_top1_in_63d},
    "dvs_ext_066_dv_cumsum_252d_pct_change_63d": {"inputs": ["close", "volume"], "func": dvs_ext_066_dv_cumsum_252d_pct_change_63d},
    "dvs_ext_067_dv_cumsum_21d_zscore_252d": {"inputs": ["close", "volume"], "func": dvs_ext_067_dv_cumsum_21d_zscore_252d},
    "dvs_ext_068_dv_cumsum_63d_zscore_252d": {"inputs": ["close", "volume"], "func": dvs_ext_068_dv_cumsum_63d_zscore_252d},
    "dvs_ext_069_return_per_dv_21d": {"inputs": ["close", "volume"], "func": dvs_ext_069_return_per_dv_21d},
    "dvs_ext_070_return_per_dv_sensitivity_ratio": {"inputs": ["close", "volume"], "func": dvs_ext_070_return_per_dv_sensitivity_ratio},
    "dvs_ext_071_dv_trend_ewm_crossover": {"inputs": ["close", "volume"], "func": dvs_ext_071_dv_trend_ewm_crossover},
    "dvs_ext_072_dv_roc_21d": {"inputs": ["close", "volume"], "func": dvs_ext_072_dv_roc_21d},
    "dvs_ext_073_dv_roc_63d": {"inputs": ["close", "volume"], "func": dvs_ext_073_dv_roc_63d},
    "dvs_ext_074_amihud_vwap_interaction_21d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_ext_074_amihud_vwap_interaction_21d},
    "dvs_ext_075_dv_illiquidity_composite": {"inputs": ["close", "high", "low", "volume"], "func": dvs_ext_075_dv_illiquidity_composite},
}
