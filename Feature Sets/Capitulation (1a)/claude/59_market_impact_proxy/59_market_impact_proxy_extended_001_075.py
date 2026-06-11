"""
59_market_impact_proxy — Extended Features 001-075
Domain: market-impact / return-per-volume sensitivity — additional angles: Amihud
  illiquidity (|return| / dollar volume) family, range-based impact, gap impact per
  volume, intraday-impact decomposition, impact convexity, impact persistence /
  autocorrelation, impact-vs-volatility ratios, impact drawup, weekly-aggregated impact.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — price-impact elasticity spiking, market depth collapsing
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# -- Constants -----------------------------------------------------------------
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# -- Utility helpers -----------------------------------------------------------

def _safe_div(num, den):
    """Element-wise division; zero denominator becomes NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s):
    return np.log(s.clip(lower=_EPS))


def _zscore(s, w):
    """Rolling z-score of s over window w."""
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))


def _pct_rank(s, w):
    """Rolling percentile rank of s within trailing w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _consec_streak(cond):
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def _amihud(close, volume):
    """Daily Amihud illiquidity: |return| / dollar_volume (price impact per dollar)."""
    ret = close.pct_change(1).abs()
    dolvol = (close * volume).replace(0, np.nan)
    return _safe_div(ret, dolvol)


def _range_impact(high, low, close, volume):
    """Range-based impact: (high-low)/prior_close per dollar volume."""
    rng = _safe_div(high - low, close.shift(1).replace(0, np.nan))
    dolvol = (close * volume).replace(0, np.nan)
    return _safe_div(rng, dolvol)


def _gap_impact(close, open_, volume):
    """Overnight-gap impact: |open - prior_close|/prior_close per dollar volume."""
    prior = close.shift(1)
    gap = _safe_div((open_ - prior).abs(), prior)
    dolvol = (close * volume).replace(0, np.nan)
    return _safe_div(gap, dolvol)


# -- Feature functions 001-075 ------------------------------------------------

# --- Group A (001-014): Amihud illiquidity ratio family ---

def mip_ext_001_amihud_daily(close, volume):
    """Daily Amihud illiquidity ratio: |return| / dollar volume."""
    return _amihud(close, volume)


def mip_ext_002_amihud_log(close, volume):
    """Log of (1 + Amihud illiquidity ratio) — compressed-tail impact measure."""
    return np.log1p(_amihud(close, volume))


def mip_ext_003_amihud_roll_mean_5d(close, volume):
    """5-day rolling mean of Amihud illiquidity ratio."""
    return _rolling_mean(_amihud(close, volume), _TD_WEEK)


def mip_ext_004_amihud_roll_mean_21d(close, volume):
    """21-day rolling mean of Amihud illiquidity ratio (monthly impact level)."""
    return _rolling_mean(_amihud(close, volume), _TD_MON)


def mip_ext_005_amihud_roll_mean_63d(close, volume):
    """63-day rolling mean of Amihud illiquidity ratio."""
    return _rolling_mean(_amihud(close, volume), _TD_QTR)


def mip_ext_006_amihud_roll_mean_252d(close, volume):
    """252-day rolling mean of Amihud illiquidity ratio (annual baseline)."""
    return _rolling_mean(_amihud(close, volume), _TD_YEAR)


def mip_ext_007_amihud_zscore_63d(close, volume):
    """63-day z-score of Amihud illiquidity ratio."""
    return _zscore(_amihud(close, volume), _TD_QTR)


def mip_ext_008_amihud_zscore_252d(close, volume):
    """252-day z-score of Amihud illiquidity ratio."""
    return _zscore(_amihud(close, volume), _TD_YEAR)


def mip_ext_009_amihud_pct_rank_63d(close, volume):
    """63-day percentile rank of Amihud illiquidity ratio."""
    return _pct_rank(_amihud(close, volume), _TD_QTR)


def mip_ext_010_amihud_pct_rank_252d(close, volume):
    """252-day percentile rank of Amihud illiquidity ratio."""
    return _pct_rank(_amihud(close, volume), _TD_YEAR)


def mip_ext_011_amihud_21d_vs_252d_ratio(close, volume):
    """Ratio of 21d-mean Amihud to 252d-mean Amihud (recent illiquidity vs history)."""
    a = _amihud(close, volume)
    return _safe_div(_rolling_mean(a, _TD_MON), _rolling_mean(a, _TD_YEAR))


def mip_ext_012_amihud_spike_gt2std_252d(close, volume):
    """Flag: daily Amihud ratio > 2 std above its 252-day mean (illiquidity spike)."""
    a = _amihud(close, volume)
    mu = _rolling_mean(a, _TD_YEAR)
    sig = _rolling_std(a, _TD_YEAR)
    return (a > mu + 2.0 * sig).astype(float)


def mip_ext_013_amihud_above_mean_streak_63d(close, volume):
    """Consecutive days Amihud illiquidity exceeds its 63-day rolling mean."""
    a = _amihud(close, volume)
    return _consec_streak(a > _rolling_mean(a, _TD_QTR))


def mip_ext_014_amihud_expanding_pct_rank(close, volume):
    """Expanding all-history percentile rank of 21d-mean Amihud illiquidity."""
    a21 = _rolling_mean(_amihud(close, volume), _TD_MON)
    return a21.expanding(min_periods=_TD_MON).rank(pct=True)


# --- Group B (015-026): Range-based impact (intraday impact width per volume) ---

def mip_ext_015_range_impact_daily(close, high, low, volume):
    """Daily range-based impact: (high-low)/prior_close per dollar volume."""
    return _range_impact(high, low, close, volume)


def mip_ext_016_range_impact_roll_mean_21d(close, high, low, volume):
    """21-day rolling mean of range-based impact."""
    return _rolling_mean(_range_impact(high, low, close, volume), _TD_MON)


def mip_ext_017_range_impact_roll_mean_63d(close, high, low, volume):
    """63-day rolling mean of range-based impact."""
    return _rolling_mean(_range_impact(high, low, close, volume), _TD_QTR)


def mip_ext_018_range_impact_zscore_63d(close, high, low, volume):
    """63-day z-score of range-based impact."""
    return _zscore(_range_impact(high, low, close, volume), _TD_QTR)


def mip_ext_019_range_impact_zscore_252d(close, high, low, volume):
    """252-day z-score of range-based impact."""
    return _zscore(_range_impact(high, low, close, volume), _TD_YEAR)


def mip_ext_020_range_impact_pct_rank_252d(close, high, low, volume):
    """252-day percentile rank of range-based impact."""
    return _pct_rank(_range_impact(high, low, close, volume), _TD_YEAR)


def mip_ext_021_range_impact_vs_252d_baseline(close, high, low, volume):
    """Range-based impact divided by its 252-day rolling mean baseline."""
    r = _range_impact(high, low, close, volume)
    return _safe_div(r, _rolling_mean(r, _TD_YEAR))


def mip_ext_022_range_impact_roll_max_63d(close, high, low, volume):
    """63-day rolling max of range-based impact (worst intraday impact in quarter)."""
    return _rolling_max(_range_impact(high, low, close, volume), _TD_QTR)


def mip_ext_023_range_impact_above_mean_streak_63d(close, high, low, volume):
    """Consecutive days range-based impact exceeds its 63-day rolling mean."""
    r = _range_impact(high, low, close, volume)
    return _consec_streak(r > _rolling_mean(r, _TD_QTR))


def mip_ext_024_range_vs_ret_impact_ratio_21d(close, high, low, volume):
    """Ratio of 21d range-impact to 21d Amihud impact (intraday vs close-to-close impact)."""
    ri = _rolling_mean(_range_impact(high, low, close, volume), _TD_MON)
    ai = _rolling_mean(_amihud(close, volume), _TD_MON)
    return _safe_div(ri, ai)


def mip_ext_025_range_impact_ewm_21d(close, high, low, volume):
    """EWM(span=21) of range-based impact (smoothed intraday impact width)."""
    return _ewm_mean(_range_impact(high, low, close, volume), _TD_MON)


def mip_ext_026_range_impact_spike_gt2std_252d(close, high, low, volume):
    """Flag: range-based impact > 2 std above its 252-day mean (intraday impact spike)."""
    r = _range_impact(high, low, close, volume)
    mu = _rolling_mean(r, _TD_YEAR)
    sig = _rolling_std(r, _TD_YEAR)
    return (r > mu + 2.0 * sig).astype(float)


# --- Group C (027-038): Gap impact and impact convexity ---

def mip_ext_027_gap_impact_daily(close, open, volume):
    """Daily overnight-gap impact: |open-prior_close|/prior_close per dollar volume."""
    return _gap_impact(close, open, volume)


def mip_ext_028_gap_impact_roll_mean_21d(close, open, volume):
    """21-day rolling mean of overnight-gap impact."""
    return _rolling_mean(_gap_impact(close, open, volume), _TD_MON)


def mip_ext_029_gap_impact_roll_mean_63d(close, open, volume):
    """63-day rolling mean of overnight-gap impact."""
    return _rolling_mean(_gap_impact(close, open, volume), _TD_QTR)


def mip_ext_030_gap_impact_zscore_63d(close, open, volume):
    """63-day z-score of overnight-gap impact."""
    return _zscore(_gap_impact(close, open, volume), _TD_QTR)


def mip_ext_031_gap_impact_pct_rank_252d(close, open, volume):
    """252-day percentile rank of overnight-gap impact."""
    return _pct_rank(_gap_impact(close, open, volume), _TD_YEAR)


def mip_ext_032_gap_vs_intraday_impact_ratio_21d(close, high, low, open, volume):
    """Ratio of 21d gap impact to 21d range impact (overnight vs intraday impact)."""
    gi = _rolling_mean(_gap_impact(close, open, volume), _TD_MON)
    ri = _rolling_mean(_range_impact(high, low, close, volume), _TD_MON)
    return _safe_div(gi, ri)


def mip_ext_033_impact_convexity_21d(close, volume):
    """Ratio of mean squared Amihud to squared mean Amihud over 21d (impact convexity)."""
    a = _amihud(close, volume)
    msq = _rolling_mean(a ** 2, _TD_MON)
    sqm = _rolling_mean(a, _TD_MON) ** 2
    return _safe_div(msq, sqm)


def mip_ext_034_impact_convexity_63d(close, volume):
    """Ratio of mean squared Amihud to squared mean Amihud over 63d."""
    a = _amihud(close, volume)
    msq = _rolling_mean(a ** 2, _TD_QTR)
    sqm = _rolling_mean(a, _TD_QTR) ** 2
    return _safe_div(msq, sqm)


def mip_ext_035_amihud_skew_63d(close, volume):
    """63-day rolling skewness of Amihud illiquidity ratio (impact-tail asymmetry)."""
    return _amihud(close, volume).rolling(_TD_QTR, min_periods=_TD_MON).skew()


def mip_ext_036_amihud_kurt_63d(close, volume):
    """63-day rolling kurtosis of Amihud illiquidity ratio (fat-tailed impact risk)."""
    return _amihud(close, volume).rolling(_TD_QTR, min_periods=_TD_MON).kurt()


def mip_ext_037_amihud_q90_63d(close, volume):
    """63-day rolling 90th percentile of Amihud illiquidity ratio."""
    return _amihud(close, volume).rolling(_TD_QTR, min_periods=_TD_MON).quantile(0.90)


def mip_ext_038_amihud_q90_vs_median_63d(close, volume):
    """Ratio of 63d Amihud 90th percentile to its 63d median (impact tail-to-center)."""
    a = _amihud(close, volume)
    q90 = a.rolling(_TD_QTR, min_periods=_TD_MON).quantile(0.90)
    med = _rolling_median(a, _TD_QTR)
    return _safe_div(q90, med)


# --- Group D (039-050): Impact persistence and autocorrelation ---

def mip_ext_039_amihud_autocorr_lag1_63d(close, volume):
    """63-day rolling lag-1 autocorrelation of Amihud illiquidity (impact persistence)."""
    a = _amihud(close, volume)
    return a.rolling(_TD_QTR, min_periods=_TD_MON).corr(a.shift(1))


def mip_ext_040_amihud_autocorr_lag1_252d(close, volume):
    """252-day rolling lag-1 autocorrelation of Amihud illiquidity."""
    a = _amihud(close, volume)
    return a.rolling(_TD_YEAR, min_periods=_TD_QTR).corr(a.shift(1))


def mip_ext_041_amihud_autocorr_lag5_63d(close, volume):
    """63-day rolling lag-5 autocorrelation of Amihud illiquidity."""
    a = _amihud(close, volume)
    return a.rolling(_TD_QTR, min_periods=_TD_MON).corr(a.shift(_TD_WEEK))


def mip_ext_042_impact_persistence_streak_63d(close, volume):
    """Consecutive days Amihud illiquidity stays above its 63-day median."""
    a = _amihud(close, volume)
    return _consec_streak(a > _rolling_median(a, _TD_QTR))


def mip_ext_043_amihud_above_median_frac_63d(close, volume):
    """Fraction of last 63 days Amihud illiquidity stayed above its 252d median."""
    a = _amihud(close, volume)
    med = _rolling_median(a, _TD_YEAR)
    return _rolling_sum((a > med).astype(float), _TD_QTR) / _TD_QTR


def mip_ext_044_amihud_above_median_frac_21d(close, volume):
    """Fraction of last 21 days Amihud illiquidity stayed above its 63d median."""
    a = _amihud(close, volume)
    med = _rolling_median(a, _TD_QTR)
    return _rolling_sum((a > med).astype(float), _TD_MON) / _TD_MON


def mip_ext_045_amihud_ewm_fast_vs_slow(close, volume):
    """EWM(5) minus EWM(63) of Amihud illiquidity (fast vs slow impact momentum)."""
    a = _amihud(close, volume)
    return _ewm_mean(a, _TD_WEEK) - _ewm_mean(a, _TD_QTR)


def mip_ext_046_amihud_ewm_ratio_fast_slow(close, volume):
    """EWM(5) divided by EWM(63) of Amihud illiquidity (multiplicative impact momentum)."""
    a = _amihud(close, volume)
    return _safe_div(_ewm_mean(a, _TD_WEEK), _ewm_mean(a, _TD_QTR))


def mip_ext_047_amihud_accel_21d(close, volume):
    """21-day change of 21d-mean Amihud illiquidity (impact acceleration)."""
    return _rolling_mean(_amihud(close, volume), _TD_MON).diff(_TD_MON)


def mip_ext_048_amihud_5d_vs_63d_ratio(close, volume):
    """Ratio of 5d-mean Amihud to 63d-mean Amihud (acute vs quarter impact)."""
    a = _amihud(close, volume)
    return _safe_div(_rolling_mean(a, _TD_WEEK), _rolling_mean(a, _TD_QTR))


def mip_ext_049_amihud_rising_streak(close, volume):
    """Consecutive days 5d-mean Amihud illiquidity exceeds its prior value."""
    a5 = _rolling_mean(_amihud(close, volume), _TD_WEEK)
    return _consec_streak(a5 > a5.shift(1))


def mip_ext_050_amihud_drawup_ratio_252d(close, volume):
    """21d-mean Amihud illiquidity divided by its trailing 252d minimum (impact drawup)."""
    a21 = _rolling_mean(_amihud(close, volume), _TD_MON)
    return _safe_div(a21, _rolling_min(a21, _TD_YEAR))


# --- Group E (051-062): Impact-vs-volatility ratios and depth deterioration ---

def mip_ext_051_amihud_per_volatility_21d(close, volume):
    """21d-mean Amihud illiquidity divided by 21d return volatility (impact per vol unit)."""
    a21 = _rolling_mean(_amihud(close, volume), _TD_MON)
    vol = _rolling_std(close.pct_change(1), _TD_MON)
    return _safe_div(a21, vol)


def mip_ext_052_amihud_per_volatility_63d(close, volume):
    """63d-mean Amihud illiquidity divided by 63d return volatility."""
    a63 = _rolling_mean(_amihud(close, volume), _TD_QTR)
    vol = _rolling_std(close.pct_change(1), _TD_QTR)
    return _safe_div(a63, vol)


def mip_ext_053_amihud_per_volatility_zscore_252d(close, volume):
    """252-day z-score of 21d impact-per-volatility ratio."""
    a21 = _rolling_mean(_amihud(close, volume), _TD_MON)
    vol = _rolling_std(close.pct_change(1), _TD_MON)
    return _zscore(_safe_div(a21, vol), _TD_YEAR)


def mip_ext_054_inverse_amihud_depth_21d(close, volume):
    """Inverse Amihud (dollar volume / |return|) 21d mean — market-depth proxy."""
    ret = close.pct_change(1).abs().replace(0, np.nan)
    dolvol = close * volume
    return _rolling_mean(_safe_div(dolvol, ret), _TD_MON)


def mip_ext_055_depth_collapse_ratio_252d(close, volume):
    """21d market-depth proxy divided by its 252d max (1=peak depth, low=collapse)."""
    ret = close.pct_change(1).abs().replace(0, np.nan)
    depth = _rolling_mean(_safe_div(close * volume, ret), _TD_MON)
    return _safe_div(depth, _rolling_max(depth, _TD_YEAR))


def mip_ext_056_depth_pct_rank_252d(close, volume):
    """252-day percentile rank of 21d market-depth proxy (low rank = thin market)."""
    ret = close.pct_change(1).abs().replace(0, np.nan)
    depth = _rolling_mean(_safe_div(close * volume, ret), _TD_MON)
    return _pct_rank(depth, _TD_YEAR)


def mip_ext_057_depth_collapse_streak(close, volume):
    """Consecutive days market-depth proxy stays below its 63-day rolling mean."""
    ret = close.pct_change(1).abs().replace(0, np.nan)
    depth = _safe_div(close * volume, ret)
    return _consec_streak(depth < _rolling_mean(depth, _TD_QTR))


def mip_ext_058_amihud_vs_dollar_volume_21d(close, volume):
    """21d-mean Amihud illiquidity times 21d-mean dollar volume (vol-adjusted impact)."""
    a21 = _rolling_mean(_amihud(close, volume), _TD_MON)
    dv21 = _rolling_mean(close * volume, _TD_MON)
    return a21 * dv21


def mip_ext_059_impact_volatility_divergence_63d(close, volume):
    """63d z-score of Amihud minus 63d z-score of return volatility (impact-vol divergence)."""
    a = _rolling_mean(_amihud(close, volume), _TD_MON)
    vol = _rolling_std(close.pct_change(1), _TD_MON)
    return _zscore(a, _TD_QTR) - _zscore(vol, _TD_QTR)


def mip_ext_060_amihud_per_range_21d(close, high, low, volume):
    """21d-mean Amihud illiquidity divided by 21d-mean intraday range (impact per range)."""
    a21 = _rolling_mean(_amihud(close, volume), _TD_MON)
    rng = _rolling_mean(_safe_div(high - low, close), _TD_MON)
    return _safe_div(a21, rng)


def mip_ext_061_depth_drawdown_from_252d_max(close, volume):
    """Drawdown of 21d market-depth proxy from its trailing 252d max (fractional loss)."""
    ret = close.pct_change(1).abs().replace(0, np.nan)
    depth = _rolling_mean(_safe_div(close * volume, ret), _TD_MON)
    return 1.0 - _safe_div(depth, _rolling_max(depth, _TD_YEAR))


def mip_ext_062_amihud_per_volatility_pct_rank_252d(close, volume):
    """252-day percentile rank of 21d impact-per-volatility ratio."""
    a21 = _rolling_mean(_amihud(close, volume), _TD_MON)
    vol = _rolling_std(close.pct_change(1), _TD_MON)
    return _pct_rank(_safe_div(a21, vol), _TD_YEAR)


# --- Group F (063-075): Weekly-aggregated impact, down-day impact, composites ---

def mip_ext_063_weekly_amihud_5d(close, volume):
    """Weekly-aggregated Amihud: 5d sum of |return| over 5d sum of dollar volume."""
    ret = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(_rolling_sum(ret, _TD_WEEK), _rolling_sum(dolvol, _TD_WEEK))


def mip_ext_064_monthly_amihud_21d(close, volume):
    """Monthly-aggregated Amihud: 21d sum of |return| over 21d sum of dollar volume."""
    ret = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(_rolling_sum(ret, _TD_MON), _rolling_sum(dolvol, _TD_MON))


def mip_ext_065_weekly_amihud_zscore_252d(close, volume):
    """252-day z-score of weekly-aggregated Amihud illiquidity."""
    ret = close.pct_change(1).abs()
    dolvol = close * volume
    wa = _safe_div(_rolling_sum(ret, _TD_WEEK), _rolling_sum(dolvol, _TD_WEEK))
    return _zscore(wa, _TD_YEAR)


def mip_ext_066_monthly_amihud_pct_rank_252d(close, volume):
    """252-day percentile rank of monthly-aggregated Amihud illiquidity."""
    ret = close.pct_change(1).abs()
    dolvol = close * volume
    ma = _safe_div(_rolling_sum(ret, _TD_MON), _rolling_sum(dolvol, _TD_MON))
    return _pct_rank(ma, _TD_YEAR)


def mip_ext_067_amihud_down_day_mean_21d(close, volume):
    """Mean Amihud illiquidity on down-close days over trailing 21 days."""
    a = _amihud(close, volume)
    ret = close.pct_change(1)
    return a.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def mip_ext_068_amihud_up_day_mean_21d(close, volume):
    """Mean Amihud illiquidity on up-close days over trailing 21 days."""
    a = _amihud(close, volume)
    ret = close.pct_change(1)
    return a.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def mip_ext_069_amihud_down_vs_up_ratio_21d(close, volume):
    """Ratio of 21d down-day to up-day mean Amihud impact (>1 = crashes impact more)."""
    return _safe_div(
        mip_ext_067_amihud_down_day_mean_21d(close, volume),
        mip_ext_068_amihud_up_day_mean_21d(close, volume),
    )


def mip_ext_070_amihud_down_vs_up_ratio_63d(close, volume):
    """Ratio of 63d down-day to up-day mean Amihud impact."""
    a = _amihud(close, volume)
    ret = close.pct_change(1)
    dn = a.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    up = a.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return _safe_div(dn, up)


def mip_ext_071_amihud_down_day_zscore_63d(close, volume):
    """63-day z-score of 21d down-day mean Amihud impact."""
    return _zscore(mip_ext_067_amihud_down_day_mean_21d(close, volume), _TD_QTR)


def mip_ext_072_signed_amihud_21d(close, volume):
    """21d mean of return-signed Amihud impact (net directional price-impact pressure)."""
    a = _amihud(close, volume)
    ret = close.pct_change(1)
    return _rolling_mean(np.sign(ret) * a, _TD_MON)


def mip_ext_073_amihud_roll_max_63d(close, volume):
    """63-day rolling maximum of daily Amihud illiquidity (worst impact in quarter)."""
    return _rolling_max(_amihud(close, volume), _TD_QTR)


def mip_ext_074_amihud_high_impact_day_count_21d(close, volume):
    """Count of 21d days where Amihud illiquidity exceeds its 252d 90th percentile."""
    a = _amihud(close, volume)
    q90 = a.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return _rolling_sum((a > q90).astype(float), _TD_MON)


def mip_ext_075_impact_capitulation_composite(close, high, low, volume):
    """Capitulation composite: avg of normalized Amihud z-score, range-impact z-score,
    depth pct-rank-inverted and down-vs-up impact ratio. Higher = more extreme distress."""
    a_z = _zscore(_rolling_mean(_amihud(close, volume), _TD_MON), _TD_YEAR).clip(-3.0, 3.0) / 3.0
    ri_z = _zscore(_rolling_mean(_range_impact(high, low, close, volume), _TD_MON), _TD_YEAR).clip(-3.0, 3.0) / 3.0
    ret = close.pct_change(1).abs().replace(0, np.nan)
    depth = _rolling_mean(_safe_div(close * volume, ret), _TD_MON)
    depth_inv = 1.0 - _pct_rank(depth, _TD_YEAR).fillna(0.5)
    asym = mip_ext_069_amihud_down_vs_up_ratio_21d(close, volume)
    asym_n = (asym.clip(0.0, 3.0) / 3.0).fillna(0.5)
    return (a_z.fillna(0.0) + ri_z.fillna(0.0) + depth_inv + asym_n) / 4.0


# -- Registry ------------------------------------------------------------------

MARKET_IMPACT_PROXY_EXTENDED_REGISTRY_001_075 = {
    "mip_ext_001_amihud_daily": {"inputs": ["close", "volume"], "func": mip_ext_001_amihud_daily},
    "mip_ext_002_amihud_log": {"inputs": ["close", "volume"], "func": mip_ext_002_amihud_log},
    "mip_ext_003_amihud_roll_mean_5d": {"inputs": ["close", "volume"], "func": mip_ext_003_amihud_roll_mean_5d},
    "mip_ext_004_amihud_roll_mean_21d": {"inputs": ["close", "volume"], "func": mip_ext_004_amihud_roll_mean_21d},
    "mip_ext_005_amihud_roll_mean_63d": {"inputs": ["close", "volume"], "func": mip_ext_005_amihud_roll_mean_63d},
    "mip_ext_006_amihud_roll_mean_252d": {"inputs": ["close", "volume"], "func": mip_ext_006_amihud_roll_mean_252d},
    "mip_ext_007_amihud_zscore_63d": {"inputs": ["close", "volume"], "func": mip_ext_007_amihud_zscore_63d},
    "mip_ext_008_amihud_zscore_252d": {"inputs": ["close", "volume"], "func": mip_ext_008_amihud_zscore_252d},
    "mip_ext_009_amihud_pct_rank_63d": {"inputs": ["close", "volume"], "func": mip_ext_009_amihud_pct_rank_63d},
    "mip_ext_010_amihud_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_ext_010_amihud_pct_rank_252d},
    "mip_ext_011_amihud_21d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": mip_ext_011_amihud_21d_vs_252d_ratio},
    "mip_ext_012_amihud_spike_gt2std_252d": {"inputs": ["close", "volume"], "func": mip_ext_012_amihud_spike_gt2std_252d},
    "mip_ext_013_amihud_above_mean_streak_63d": {"inputs": ["close", "volume"], "func": mip_ext_013_amihud_above_mean_streak_63d},
    "mip_ext_014_amihud_expanding_pct_rank": {"inputs": ["close", "volume"], "func": mip_ext_014_amihud_expanding_pct_rank},
    "mip_ext_015_range_impact_daily": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_015_range_impact_daily},
    "mip_ext_016_range_impact_roll_mean_21d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_016_range_impact_roll_mean_21d},
    "mip_ext_017_range_impact_roll_mean_63d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_017_range_impact_roll_mean_63d},
    "mip_ext_018_range_impact_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_018_range_impact_zscore_63d},
    "mip_ext_019_range_impact_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_019_range_impact_zscore_252d},
    "mip_ext_020_range_impact_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_020_range_impact_pct_rank_252d},
    "mip_ext_021_range_impact_vs_252d_baseline": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_021_range_impact_vs_252d_baseline},
    "mip_ext_022_range_impact_roll_max_63d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_022_range_impact_roll_max_63d},
    "mip_ext_023_range_impact_above_mean_streak_63d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_023_range_impact_above_mean_streak_63d},
    "mip_ext_024_range_vs_ret_impact_ratio_21d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_024_range_vs_ret_impact_ratio_21d},
    "mip_ext_025_range_impact_ewm_21d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_025_range_impact_ewm_21d},
    "mip_ext_026_range_impact_spike_gt2std_252d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_026_range_impact_spike_gt2std_252d},
    "mip_ext_027_gap_impact_daily": {"inputs": ["close", "open", "volume"], "func": mip_ext_027_gap_impact_daily},
    "mip_ext_028_gap_impact_roll_mean_21d": {"inputs": ["close", "open", "volume"], "func": mip_ext_028_gap_impact_roll_mean_21d},
    "mip_ext_029_gap_impact_roll_mean_63d": {"inputs": ["close", "open", "volume"], "func": mip_ext_029_gap_impact_roll_mean_63d},
    "mip_ext_030_gap_impact_zscore_63d": {"inputs": ["close", "open", "volume"], "func": mip_ext_030_gap_impact_zscore_63d},
    "mip_ext_031_gap_impact_pct_rank_252d": {"inputs": ["close", "open", "volume"], "func": mip_ext_031_gap_impact_pct_rank_252d},
    "mip_ext_032_gap_vs_intraday_impact_ratio_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": mip_ext_032_gap_vs_intraday_impact_ratio_21d},
    "mip_ext_033_impact_convexity_21d": {"inputs": ["close", "volume"], "func": mip_ext_033_impact_convexity_21d},
    "mip_ext_034_impact_convexity_63d": {"inputs": ["close", "volume"], "func": mip_ext_034_impact_convexity_63d},
    "mip_ext_035_amihud_skew_63d": {"inputs": ["close", "volume"], "func": mip_ext_035_amihud_skew_63d},
    "mip_ext_036_amihud_kurt_63d": {"inputs": ["close", "volume"], "func": mip_ext_036_amihud_kurt_63d},
    "mip_ext_037_amihud_q90_63d": {"inputs": ["close", "volume"], "func": mip_ext_037_amihud_q90_63d},
    "mip_ext_038_amihud_q90_vs_median_63d": {"inputs": ["close", "volume"], "func": mip_ext_038_amihud_q90_vs_median_63d},
    "mip_ext_039_amihud_autocorr_lag1_63d": {"inputs": ["close", "volume"], "func": mip_ext_039_amihud_autocorr_lag1_63d},
    "mip_ext_040_amihud_autocorr_lag1_252d": {"inputs": ["close", "volume"], "func": mip_ext_040_amihud_autocorr_lag1_252d},
    "mip_ext_041_amihud_autocorr_lag5_63d": {"inputs": ["close", "volume"], "func": mip_ext_041_amihud_autocorr_lag5_63d},
    "mip_ext_042_impact_persistence_streak_63d": {"inputs": ["close", "volume"], "func": mip_ext_042_impact_persistence_streak_63d},
    "mip_ext_043_amihud_above_median_frac_63d": {"inputs": ["close", "volume"], "func": mip_ext_043_amihud_above_median_frac_63d},
    "mip_ext_044_amihud_above_median_frac_21d": {"inputs": ["close", "volume"], "func": mip_ext_044_amihud_above_median_frac_21d},
    "mip_ext_045_amihud_ewm_fast_vs_slow": {"inputs": ["close", "volume"], "func": mip_ext_045_amihud_ewm_fast_vs_slow},
    "mip_ext_046_amihud_ewm_ratio_fast_slow": {"inputs": ["close", "volume"], "func": mip_ext_046_amihud_ewm_ratio_fast_slow},
    "mip_ext_047_amihud_accel_21d": {"inputs": ["close", "volume"], "func": mip_ext_047_amihud_accel_21d},
    "mip_ext_048_amihud_5d_vs_63d_ratio": {"inputs": ["close", "volume"], "func": mip_ext_048_amihud_5d_vs_63d_ratio},
    "mip_ext_049_amihud_rising_streak": {"inputs": ["close", "volume"], "func": mip_ext_049_amihud_rising_streak},
    "mip_ext_050_amihud_drawup_ratio_252d": {"inputs": ["close", "volume"], "func": mip_ext_050_amihud_drawup_ratio_252d},
    "mip_ext_051_amihud_per_volatility_21d": {"inputs": ["close", "volume"], "func": mip_ext_051_amihud_per_volatility_21d},
    "mip_ext_052_amihud_per_volatility_63d": {"inputs": ["close", "volume"], "func": mip_ext_052_amihud_per_volatility_63d},
    "mip_ext_053_amihud_per_volatility_zscore_252d": {"inputs": ["close", "volume"], "func": mip_ext_053_amihud_per_volatility_zscore_252d},
    "mip_ext_054_inverse_amihud_depth_21d": {"inputs": ["close", "volume"], "func": mip_ext_054_inverse_amihud_depth_21d},
    "mip_ext_055_depth_collapse_ratio_252d": {"inputs": ["close", "volume"], "func": mip_ext_055_depth_collapse_ratio_252d},
    "mip_ext_056_depth_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_ext_056_depth_pct_rank_252d},
    "mip_ext_057_depth_collapse_streak": {"inputs": ["close", "volume"], "func": mip_ext_057_depth_collapse_streak},
    "mip_ext_058_amihud_vs_dollar_volume_21d": {"inputs": ["close", "volume"], "func": mip_ext_058_amihud_vs_dollar_volume_21d},
    "mip_ext_059_impact_volatility_divergence_63d": {"inputs": ["close", "volume"], "func": mip_ext_059_impact_volatility_divergence_63d},
    "mip_ext_060_amihud_per_range_21d": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_060_amihud_per_range_21d},
    "mip_ext_061_depth_drawdown_from_252d_max": {"inputs": ["close", "volume"], "func": mip_ext_061_depth_drawdown_from_252d_max},
    "mip_ext_062_amihud_per_volatility_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_ext_062_amihud_per_volatility_pct_rank_252d},
    "mip_ext_063_weekly_amihud_5d": {"inputs": ["close", "volume"], "func": mip_ext_063_weekly_amihud_5d},
    "mip_ext_064_monthly_amihud_21d": {"inputs": ["close", "volume"], "func": mip_ext_064_monthly_amihud_21d},
    "mip_ext_065_weekly_amihud_zscore_252d": {"inputs": ["close", "volume"], "func": mip_ext_065_weekly_amihud_zscore_252d},
    "mip_ext_066_monthly_amihud_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_ext_066_monthly_amihud_pct_rank_252d},
    "mip_ext_067_amihud_down_day_mean_21d": {"inputs": ["close", "volume"], "func": mip_ext_067_amihud_down_day_mean_21d},
    "mip_ext_068_amihud_up_day_mean_21d": {"inputs": ["close", "volume"], "func": mip_ext_068_amihud_up_day_mean_21d},
    "mip_ext_069_amihud_down_vs_up_ratio_21d": {"inputs": ["close", "volume"], "func": mip_ext_069_amihud_down_vs_up_ratio_21d},
    "mip_ext_070_amihud_down_vs_up_ratio_63d": {"inputs": ["close", "volume"], "func": mip_ext_070_amihud_down_vs_up_ratio_63d},
    "mip_ext_071_amihud_down_day_zscore_63d": {"inputs": ["close", "volume"], "func": mip_ext_071_amihud_down_day_zscore_63d},
    "mip_ext_072_signed_amihud_21d": {"inputs": ["close", "volume"], "func": mip_ext_072_signed_amihud_21d},
    "mip_ext_073_amihud_roll_max_63d": {"inputs": ["close", "volume"], "func": mip_ext_073_amihud_roll_max_63d},
    "mip_ext_074_amihud_high_impact_day_count_21d": {"inputs": ["close", "volume"], "func": mip_ext_074_amihud_high_impact_day_count_21d},
    "mip_ext_075_impact_capitulation_composite": {"inputs": ["close", "high", "low", "volume"], "func": mip_ext_075_impact_capitulation_composite},
}
