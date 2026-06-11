"""
58_trading_intensity — Extended Features 001-075
Domain: trade-frequency / activity-intensity proxies — additional angles: volume
        concentration / clustering, intensity entropy, volume-share of largest days,
        Amihud-style activity, turnover-intensity, directional-activity skew,
        intensity acceleration, weekly-aggregated intensity, quiet-then-active patterns.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — active vs lull regimes, price-discovery intensity
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _zscore(s: pd.Series, w: int) -> pd.Series:
    """Rolling z-score of s over window w."""
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))


def _pct_rank(s: pd.Series, w: int) -> pd.Series:
    """Rolling percentile rank of s within trailing w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def _herfindahl(volume: pd.Series, w: int) -> pd.Series:
    """Herfindahl concentration index of volume shares over trailing w days."""
    def _hhi(arr):
        tot = arr.sum()
        if tot <= 0:
            return np.nan
        shares = arr / tot
        return float((shares ** 2).sum())
    return volume.rolling(w, min_periods=max(2, w // 2)).apply(_hhi, raw=True)


def _shannon_entropy(volume: pd.Series, w: int) -> pd.Series:
    """Shannon entropy of volume-share distribution over trailing w days."""
    def _ent(arr):
        tot = arr.sum()
        if tot <= 0:
            return np.nan
        p = arr / tot
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return volume.rolling(w, min_periods=max(2, w // 2)).apply(_ent, raw=True)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Volume concentration / clustering (Herfindahl) ---

def tin_ext_001_volume_hhi_21d(volume: pd.Series) -> pd.Series:
    """Herfindahl concentration of volume over trailing 21 days (1=one-day dominance)."""
    return _herfindahl(volume, _TD_MON)


def tin_ext_002_volume_hhi_63d(volume: pd.Series) -> pd.Series:
    """Herfindahl concentration of volume over trailing 63 days."""
    return _herfindahl(volume, _TD_QTR)


def tin_ext_003_volume_hhi_252d(volume: pd.Series) -> pd.Series:
    """Herfindahl concentration of volume over trailing 252 days."""
    return _herfindahl(volume, _TD_YEAR)


def tin_ext_004_volume_hhi_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """252-day z-score of 21-day volume Herfindahl concentration."""
    return _zscore(_herfindahl(volume, _TD_MON), _TD_YEAR)


def tin_ext_005_volume_hhi_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """252-day percentile rank of 21-day volume Herfindahl concentration."""
    return _pct_rank(_herfindahl(volume, _TD_MON), _TD_YEAR)


def tin_ext_006_volume_hhi_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day volume HHI to 252-day volume HHI (recent clustering vs history)."""
    return _safe_div(_herfindahl(volume, _TD_MON), _herfindahl(volume, _TD_YEAR))


def tin_ext_007_volume_entropy_21d(volume: pd.Series) -> pd.Series:
    """Shannon entropy of volume distribution over 21 days (high=evenly spread)."""
    return _shannon_entropy(volume, _TD_MON)


def tin_ext_008_volume_entropy_63d(volume: pd.Series) -> pd.Series:
    """Shannon entropy of volume distribution over 63 days."""
    return _shannon_entropy(volume, _TD_QTR)


def tin_ext_009_volume_entropy_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """252-day z-score of 21-day volume entropy."""
    return _zscore(_shannon_entropy(volume, _TD_MON), _TD_YEAR)


def tin_ext_010_volume_entropy_norm_21d(volume: pd.Series) -> pd.Series:
    """21-day volume entropy normalized by log(21) — bounded 0-1 evenness measure."""
    return _shannon_entropy(volume, _TD_MON) / np.log(float(_TD_MON))


def tin_ext_011_top_day_volume_share_21d(volume: pd.Series) -> pd.Series:
    """Share of trailing-21d total volume captured by the single largest day."""
    return _safe_div(_rolling_max(volume, _TD_MON), _rolling_sum(volume, _TD_MON))


def tin_ext_012_top_day_volume_share_63d(volume: pd.Series) -> pd.Series:
    """Share of trailing-63d total volume captured by the single largest day."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))


# --- Group B (013-024): Turnover-intensity and dollar-volume activity ---

def tin_ext_013_dollar_volume_daily(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily dollar volume (close * volume) — raw monetary activity intensity."""
    return close * volume


def tin_ext_014_dollar_volume_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean dollar volume."""
    return _rolling_mean(close * volume, _TD_MON)


def tin_ext_015_dollar_volume_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day z-score of daily dollar volume."""
    return _zscore(close * volume, _TD_YEAR)


def tin_ext_016_dollar_volume_21d_vs_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day mean dollar volume to 252-day mean (recent activity vs history)."""
    dv = close * volume
    return _safe_div(_rolling_mean(dv, _TD_MON), _rolling_mean(dv, _TD_YEAR))


def tin_ext_017_log_dollar_volume_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in log dollar volume (monetary-activity trend)."""
    return _log_safe(close * volume).diff(_TD_MON)


def tin_ext_018_dollar_volume_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day percentile rank of daily dollar volume."""
    return _pct_rank(close * volume, _TD_YEAR)


def tin_ext_019_dollar_volume_spike_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 21d window where dollar volume > 2x its 63d mean."""
    dv = close * volume
    return _rolling_sum((dv > 2.0 * _rolling_mean(dv, _TD_QTR)).astype(float), _TD_MON)


def tin_ext_020_turnover_per_pct_move_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d mean of dollar volume per unit absolute return (activity-per-move intensity)."""
    dv = close * volume
    ret = close.pct_change(1).abs()
    return _rolling_mean(_safe_div(dv, ret.replace(0, np.nan)), _TD_MON)


def tin_ext_021_volume_share_of_largest3_days_21d(volume: pd.Series) -> pd.Series:
    """Share of trailing-21d volume in the 3 highest-volume days (burst concentration)."""
    def _top3(arr):
        tot = arr.sum()
        if tot <= 0:
            return np.nan
        top = np.sort(arr)[-3:]
        return float(top.sum() / tot)
    return volume.rolling(_TD_MON, min_periods=_TD_WEEK).apply(_top3, raw=True)


def tin_ext_022_volume_gini_63d(volume: pd.Series) -> pd.Series:
    """Gini coefficient of volume distribution over 63 days (inequality of activity)."""
    def _gini(arr):
        a = np.sort(arr)
        n = len(a)
        tot = a.sum()
        if tot <= 0 or n < 2:
            return np.nan
        idx = np.arange(1, n + 1)
        return float((2.0 * (idx * a).sum()) / (n * tot) - (n + 1.0) / n)
    return volume.rolling(_TD_QTR, min_periods=_TD_MON).apply(_gini, raw=True)


def tin_ext_023_dollar_volume_drawup_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean dollar volume divided by its trailing 252d minimum (activity drawup)."""
    dv21 = _rolling_mean(close * volume, _TD_MON)
    return _safe_div(dv21, _rolling_min(dv21, _TD_YEAR))


def tin_ext_024_dollar_volume_range_position_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Position of 21d dollar volume in its 252d min-max range (0=min, 1=max)."""
    dv21 = _rolling_mean(close * volume, _TD_MON)
    mn = _rolling_min(dv21, _TD_YEAR)
    mx = _rolling_max(dv21, _TD_YEAR)
    return _safe_div(dv21 - mn, mx - mn)


# --- Group C (025-036): Directional-activity intensity (up vs down volume) ---

def tin_ext_025_up_day_volume_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21d total volume traded on up-close days."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, 0.0)
    return _safe_div(_rolling_sum(up_vol, _TD_MON), _rolling_sum(volume, _TD_MON))


def tin_ext_026_down_day_volume_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21d total volume traded on down-close days."""
    ret = close.pct_change(1)
    dn_vol = volume.where(ret < 0, 0.0)
    return _safe_div(_rolling_sum(dn_vol, _TD_MON), _rolling_sum(volume, _TD_MON))


def tin_ext_027_down_day_volume_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63d total volume traded on down-close days."""
    ret = close.pct_change(1)
    dn_vol = volume.where(ret < 0, 0.0)
    return _safe_div(_rolling_sum(dn_vol, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def tin_ext_028_down_vs_up_volume_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21d down-day volume to up-day volume (sell-side activity dominance)."""
    ret = close.pct_change(1)
    dn = _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON)
    up = _rolling_sum(volume.where(ret > 0, 0.0), _TD_MON)
    return _safe_div(dn, up)


def tin_ext_029_down_vs_up_volume_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63d down-day volume to up-day volume."""
    ret = close.pct_change(1)
    dn = _rolling_sum(volume.where(ret < 0, 0.0), _TD_QTR)
    up = _rolling_sum(volume.where(ret > 0, 0.0), _TD_QTR)
    return _safe_div(dn, up)


def tin_ext_030_down_volume_frac_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day z-score of 21d down-day volume fraction."""
    ret = close.pct_change(1)
    dn = _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON)
    frac = _safe_div(dn, _rolling_sum(volume, _TD_MON))
    return _zscore(frac, _TD_YEAR)


def tin_ext_031_down_volume_frac_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day percentile rank of 21d down-day volume fraction."""
    ret = close.pct_change(1)
    dn = _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON)
    frac = _safe_div(dn, _rolling_sum(volume, _TD_MON))
    return _pct_rank(frac, _TD_YEAR)


def tin_ext_032_signed_volume_intensity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d mean of return-signed volume normalized by mean volume (net order-flow intensity)."""
    ret = close.pct_change(1)
    sv = np.sign(ret) * volume
    return _safe_div(_rolling_mean(sv, _TD_MON), _rolling_mean(volume, _TD_MON))


def tin_ext_033_down_day_volume_concentration_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Largest single-day down-volume share of 63d total down-volume (panic clustering)."""
    ret = close.pct_change(1)
    dn_vol = volume.where(ret < 0, 0.0)
    return _safe_div(_rolling_max(dn_vol, _TD_QTR), _rolling_sum(dn_vol, _TD_QTR))


def tin_ext_034_down_day_count_high_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 21d days that were both down-close AND above-63d-mean volume."""
    ret = close.pct_change(1)
    avg = _rolling_mean(volume, _TD_QTR)
    cond = ((ret < 0) & (volume > avg)).astype(float)
    return _rolling_sum(cond, _TD_MON)


def tin_ext_035_down_vol_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days that were down-close AND above-21d-mean volume (selling streak)."""
    ret = close.pct_change(1)
    avg = _rolling_mean(volume, _TD_MON)
    return _consec_streak((ret < 0) & (volume > avg))


def tin_ext_036_directional_volume_imbalance_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252d (down-volume minus up-volume) / total volume — long-run flow imbalance."""
    ret = close.pct_change(1)
    dn = _rolling_sum(volume.where(ret < 0, 0.0), _TD_YEAR)
    up = _rolling_sum(volume.where(ret > 0, 0.0), _TD_YEAR)
    tot = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(dn - up, tot)


# --- Group D (037-048): Intensity acceleration and momentum of activity ---

def tin_ext_037_volume_intensity_accel_5d(volume: pd.Series) -> pd.Series:
    """5-day change of the 5d-mean volume (short-run activity acceleration)."""
    return _rolling_mean(volume, _TD_WEEK).diff(_TD_WEEK)


def tin_ext_038_volume_intensity_accel_21d(volume: pd.Series) -> pd.Series:
    """21-day change of the 21d-mean volume (monthly activity acceleration)."""
    return _rolling_mean(volume, _TD_MON).diff(_TD_MON)


def tin_ext_039_volume_ewm_fast_vs_slow(volume: pd.Series) -> pd.Series:
    """EWM(5) minus EWM(63) of volume (fast vs slow activity momentum)."""
    return _ewm_mean(volume, _TD_WEEK) - _ewm_mean(volume, _TD_QTR)


def tin_ext_040_volume_ewm_ratio_fast_slow(volume: pd.Series) -> pd.Series:
    """EWM(5) divided by EWM(63) of volume (multiplicative activity momentum)."""
    return _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_QTR))


def tin_ext_041_volume_5d_vs_63d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5d-mean volume to 63d-mean volume (recent surge vs quarter base)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))


def tin_ext_042_volume_accel_zscore_252d(volume: pd.Series) -> pd.Series:
    """252-day z-score of 21-day volume acceleration."""
    return _zscore(_rolling_mean(volume, _TD_MON).diff(_TD_MON), _TD_YEAR)


def tin_ext_043_range_intensity_accel_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day change of the 21d-mean intraday range relative to close (range acceleration)."""
    rng = _safe_div(high - low, close)
    return _rolling_mean(rng, _TD_MON).diff(_TD_MON)


def tin_ext_044_volume_per_range_accel_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change of 21d-mean volume-per-range (trade-intensity acceleration)."""
    rng = (high - low).replace(0, np.nan)
    vpr = _safe_div(volume, rng)
    return _rolling_mean(vpr, _TD_MON).diff(_TD_MON)


def tin_ext_045_volume_surge_consec_streak(volume: pd.Series) -> pd.Series:
    """Consecutive days where 5d-mean volume exceeds 63d-mean volume (sustained surge)."""
    cond = _rolling_mean(volume, _TD_WEEK) > _rolling_mean(volume, _TD_QTR)
    return _consec_streak(cond)


def tin_ext_046_volume_quiet_consec_streak(volume: pd.Series) -> pd.Series:
    """Consecutive days where 5d-mean volume is below 63d-mean volume (sustained lull)."""
    cond = _rolling_mean(volume, _TD_WEEK) < _rolling_mean(volume, _TD_QTR)
    return _consec_streak(cond)


def tin_ext_047_volume_intensity_momentum_21d(volume: pd.Series) -> pd.Series:
    """21-day rate-of-change of volume itself (raw activity momentum)."""
    return _safe_div(volume - volume.shift(_TD_MON), volume.shift(_TD_MON))


def tin_ext_048_volume_accel_positive_frac_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where day-over-day volume increased (rising-activity frequency)."""
    rising = (volume > volume.shift(1)).astype(float)
    return _rolling_sum(rising, _TD_QTR) / _TD_QTR


# --- Group E (049-060): Quiet-then-active patterns and lull-to-burst transitions ---

def tin_ext_049_quiet_before_burst_flag(volume: pd.Series) -> pd.Series:
    """Flag: today volume > 3x 63d mean AND prior 5d all below 63d mean (lull-then-burst)."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    burst = volume > 3.0 * avg63
    prior_quiet = _rolling_sum((volume < avg63).astype(float).shift(1), _TD_WEEK) >= 5.0
    return (burst & prior_quiet).astype(float)


def tin_ext_050_quiet_before_burst_count_63d(volume: pd.Series) -> pd.Series:
    """Count of lull-then-burst events in trailing 63 days."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    burst = volume > 3.0 * avg63
    prior_quiet = _rolling_sum((volume < avg63).astype(float).shift(1), _TD_WEEK) >= 5.0
    return _rolling_sum((burst & prior_quiet).astype(float), _TD_QTR)


def tin_ext_051_days_since_volume_burst(volume: pd.Series) -> pd.Series:
    """Days elapsed since volume last exceeded 3x its 63d mean (0 = burst today)."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    burst = (volume > 3.0 * avg63)
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    last = idx.where(burst).ffill()
    return (idx - last).where(~volume.isna(), np.nan)


def tin_ext_052_days_since_volume_lull(volume: pd.Series) -> pd.Series:
    """Days elapsed since volume last dropped below 30% of its 63d mean."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    lull = (volume < 0.30 * avg63)
    idx = pd.Series(np.arange(len(volume), dtype=float), index=volume.index)
    last = idx.where(lull).ffill()
    return (idx - last).where(~volume.isna(), np.nan)


def tin_ext_053_lull_to_burst_transition_count_63d(volume: pd.Series) -> pd.Series:
    """Count of below-mean to above-mean volume transitions in trailing 63 days."""
    avg = _rolling_mean(volume, _TD_MON)
    above = (volume > avg).astype(int)
    trans = ((above == 1) & (above.shift(1) == 0)).astype(float)
    return _rolling_sum(trans, _TD_QTR)


def tin_ext_054_volume_calm_then_max_flag(volume: pd.Series) -> pd.Series:
    """Flag: today sets a fresh 63d-max volume AND 21d volume std was below its 252d median."""
    is_max = volume >= _rolling_max(volume, _TD_QTR) - _EPS
    vstd = _rolling_std(volume, _TD_MON)
    calm = vstd.shift(1) < _rolling_median(vstd, _TD_YEAR)
    return (is_max & calm).astype(float)


def tin_ext_055_active_after_lull_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21d days that were high-activity following a prior-day low-activity day."""
    avg = _rolling_mean(volume, _TD_MON)
    active = volume > avg
    prior_quiet = (volume.shift(1) < avg)
    cond = (active & prior_quiet).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_ext_056_volume_compression_then_expansion_21d(volume: pd.Series) -> pd.Series:
    """Ratio of recent-5d volume std to prior-21d volume std (volatility-of-activity surge)."""
    vstd5 = _rolling_std(volume, _TD_WEEK)
    vstd21_prior = _rolling_std(volume, _TD_MON).shift(_TD_WEEK)
    return _safe_div(vstd5, vstd21_prior)


def tin_ext_057_intensity_regime_shift_score_63d(volume: pd.Series) -> pd.Series:
    """Difference of recent-21d mean volume and prior-21d mean volume, scaled by 63d std."""
    recent = _rolling_mean(volume, _TD_MON)
    prior = _rolling_mean(volume, _TD_MON).shift(_TD_MON)
    return _safe_div(recent - prior, _rolling_std(volume, _TD_QTR))


def tin_ext_058_volume_low_then_high_252d_pct(volume: pd.Series) -> pd.Series:
    """252d percentile rank of volume conditional on prior-21d-min being a fresh low.
    Plain percentile rank of current volume within trailing 252 days."""
    return _pct_rank(volume, _TD_YEAR)


def tin_ext_059_burst_isolation_score_21d(volume: pd.Series) -> pd.Series:
    """Top-day volume share minus mean of remaining-day shares over 21d (burst isolation)."""
    top_share = _safe_div(_rolling_max(volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    rest_share = (1.0 - top_share) / float(_TD_MON - 1)
    return top_share - rest_share


def tin_ext_060_quiet_day_run_max_63d(volume: pd.Series) -> pd.Series:
    """Longest consecutive run of below-21d-mean volume days within trailing 63 days."""
    cond = (volume < _rolling_mean(volume, _TD_MON))
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            cur = cur + 1 if v else 0
            if cur > mx:
                mx = cur
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


# --- Group F (061-075): Weekly-aggregated intensity, dispersion, composites ---

def tin_ext_061_weekly_volume_sum_5d(volume: pd.Series) -> pd.Series:
    """Trailing 5-day total volume (weekly activity aggregate)."""
    return _rolling_sum(volume, _TD_WEEK)


def tin_ext_062_weekly_volume_zscore_252d(volume: pd.Series) -> pd.Series:
    """252-day z-score of trailing 5-day total volume."""
    return _zscore(_rolling_sum(volume, _TD_WEEK), _TD_YEAR)


def tin_ext_063_weekly_volume_5d_vs_21d_ratio(volume: pd.Series) -> pd.Series:
    """Trailing 5-day volume sum vs (5/21 of) 21-day volume sum — weekly intensity ratio."""
    w5 = _rolling_sum(volume, _TD_WEEK)
    w21 = _rolling_sum(volume, _TD_MON) * (5.0 / 21.0)
    return _safe_div(w5, w21)


def tin_ext_064_volume_dispersion_21d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 21 days (activity dispersion)."""
    return _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))


def tin_ext_065_volume_dispersion_63d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 63 days."""
    return _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))


def tin_ext_066_volume_dispersion_zscore_252d(volume: pd.Series) -> pd.Series:
    """252-day z-score of 21-day volume coefficient of variation."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return _zscore(cv, _TD_YEAR)


def tin_ext_067_volume_skew_63d(volume: pd.Series) -> pd.Series:
    """63-day rolling skewness of volume (right-skew = burst-dominated activity)."""
    return volume.rolling(_TD_QTR, min_periods=_TD_MON).skew()


def tin_ext_068_volume_kurt_63d(volume: pd.Series) -> pd.Series:
    """63-day rolling kurtosis of volume (fat tails = spiky activity)."""
    return volume.rolling(_TD_QTR, min_periods=_TD_MON).kurt()


def tin_ext_069_range_dispersion_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Coefficient of variation of intraday range/close over 21 days."""
    rng = _safe_div(high - low, close)
    return _safe_div(_rolling_std(rng, _TD_MON), _rolling_mean(rng, _TD_MON))


def tin_ext_070_volume_median_to_mean_ratio_63d(volume: pd.Series) -> pd.Series:
    """Ratio of 63d median volume to 63d mean volume (low value = burst-skewed activity)."""
    return _safe_div(_rolling_median(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))


def tin_ext_071_volume_intensity_pct_rank_63d(volume: pd.Series) -> pd.Series:
    """63-day percentile rank of daily volume (short-horizon activity rank)."""
    return _pct_rank(volume, _TD_QTR)


def tin_ext_072_volume_above_q90_count_63d(volume: pd.Series) -> pd.Series:
    """Count of 63d days where volume exceeds its trailing 252d 90th percentile."""
    q90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return _rolling_sum((volume > q90).astype(float), _TD_QTR)


def tin_ext_073_intensity_expanding_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 21-day mean volume."""
    return _rolling_mean(volume, _TD_MON).expanding(min_periods=_TD_MON).rank(pct=True)


def tin_ext_074_volume_range_intensity_product_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """21d mean of volume * (range/close) — joint volume-and-range activity intensity."""
    rng = _safe_div(high - low, close)
    return _rolling_mean(volume * rng, _TD_MON)


def tin_ext_075_intensity_capitulation_composite(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Capitulation composite: avg of normalized volume z-score, volume HHI pct-rank,
    range z-score and down-volume fraction. Higher = more intense distressed activity."""
    vol_z = _zscore(volume, _TD_YEAR).clip(-3.0, 3.0) / 3.0
    hhi_pr = _pct_rank(_herfindahl(volume, _TD_MON), _TD_YEAR).fillna(0.5)
    rng = _safe_div(high - low, close)
    rng_z = _zscore(rng, _TD_YEAR).clip(-3.0, 3.0) / 3.0
    ret = close.pct_change(1)
    dn = _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON)
    dn_frac = _safe_div(dn, _rolling_sum(volume, _TD_MON))
    return (vol_z.fillna(0.0) + hhi_pr + rng_z.fillna(0.0) + dn_frac.fillna(0.5)) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

TRADING_INTENSITY_EXTENDED_REGISTRY_001_075 = {
    "tin_ext_001_volume_hhi_21d": {"inputs": ["volume"], "func": tin_ext_001_volume_hhi_21d},
    "tin_ext_002_volume_hhi_63d": {"inputs": ["volume"], "func": tin_ext_002_volume_hhi_63d},
    "tin_ext_003_volume_hhi_252d": {"inputs": ["volume"], "func": tin_ext_003_volume_hhi_252d},
    "tin_ext_004_volume_hhi_21d_zscore_252d": {"inputs": ["volume"], "func": tin_ext_004_volume_hhi_21d_zscore_252d},
    "tin_ext_005_volume_hhi_21d_pct_rank_252d": {"inputs": ["volume"], "func": tin_ext_005_volume_hhi_21d_pct_rank_252d},
    "tin_ext_006_volume_hhi_21d_vs_252d_ratio": {"inputs": ["volume"], "func": tin_ext_006_volume_hhi_21d_vs_252d_ratio},
    "tin_ext_007_volume_entropy_21d": {"inputs": ["volume"], "func": tin_ext_007_volume_entropy_21d},
    "tin_ext_008_volume_entropy_63d": {"inputs": ["volume"], "func": tin_ext_008_volume_entropy_63d},
    "tin_ext_009_volume_entropy_21d_zscore_252d": {"inputs": ["volume"], "func": tin_ext_009_volume_entropy_21d_zscore_252d},
    "tin_ext_010_volume_entropy_norm_21d": {"inputs": ["volume"], "func": tin_ext_010_volume_entropy_norm_21d},
    "tin_ext_011_top_day_volume_share_21d": {"inputs": ["volume"], "func": tin_ext_011_top_day_volume_share_21d},
    "tin_ext_012_top_day_volume_share_63d": {"inputs": ["volume"], "func": tin_ext_012_top_day_volume_share_63d},
    "tin_ext_013_dollar_volume_daily": {"inputs": ["close", "volume"], "func": tin_ext_013_dollar_volume_daily},
    "tin_ext_014_dollar_volume_21d": {"inputs": ["close", "volume"], "func": tin_ext_014_dollar_volume_21d},
    "tin_ext_015_dollar_volume_zscore_252d": {"inputs": ["close", "volume"], "func": tin_ext_015_dollar_volume_zscore_252d},
    "tin_ext_016_dollar_volume_21d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": tin_ext_016_dollar_volume_21d_vs_252d_ratio},
    "tin_ext_017_log_dollar_volume_slope_21d": {"inputs": ["close", "volume"], "func": tin_ext_017_log_dollar_volume_slope_21d},
    "tin_ext_018_dollar_volume_pct_rank_252d": {"inputs": ["close", "volume"], "func": tin_ext_018_dollar_volume_pct_rank_252d},
    "tin_ext_019_dollar_volume_spike_count_21d": {"inputs": ["close", "volume"], "func": tin_ext_019_dollar_volume_spike_count_21d},
    "tin_ext_020_turnover_per_pct_move_21d": {"inputs": ["close", "volume"], "func": tin_ext_020_turnover_per_pct_move_21d},
    "tin_ext_021_volume_share_of_largest3_days_21d": {"inputs": ["volume"], "func": tin_ext_021_volume_share_of_largest3_days_21d},
    "tin_ext_022_volume_gini_63d": {"inputs": ["volume"], "func": tin_ext_022_volume_gini_63d},
    "tin_ext_023_dollar_volume_drawup_ratio_252d": {"inputs": ["close", "volume"], "func": tin_ext_023_dollar_volume_drawup_ratio_252d},
    "tin_ext_024_dollar_volume_range_position_252d": {"inputs": ["close", "volume"], "func": tin_ext_024_dollar_volume_range_position_252d},
    "tin_ext_025_up_day_volume_frac_21d": {"inputs": ["close", "volume"], "func": tin_ext_025_up_day_volume_frac_21d},
    "tin_ext_026_down_day_volume_frac_21d": {"inputs": ["close", "volume"], "func": tin_ext_026_down_day_volume_frac_21d},
    "tin_ext_027_down_day_volume_frac_63d": {"inputs": ["close", "volume"], "func": tin_ext_027_down_day_volume_frac_63d},
    "tin_ext_028_down_vs_up_volume_ratio_21d": {"inputs": ["close", "volume"], "func": tin_ext_028_down_vs_up_volume_ratio_21d},
    "tin_ext_029_down_vs_up_volume_ratio_63d": {"inputs": ["close", "volume"], "func": tin_ext_029_down_vs_up_volume_ratio_63d},
    "tin_ext_030_down_volume_frac_zscore_252d": {"inputs": ["close", "volume"], "func": tin_ext_030_down_volume_frac_zscore_252d},
    "tin_ext_031_down_volume_frac_pct_rank_252d": {"inputs": ["close", "volume"], "func": tin_ext_031_down_volume_frac_pct_rank_252d},
    "tin_ext_032_signed_volume_intensity_21d": {"inputs": ["close", "volume"], "func": tin_ext_032_signed_volume_intensity_21d},
    "tin_ext_033_down_day_volume_concentration_63d": {"inputs": ["close", "volume"], "func": tin_ext_033_down_day_volume_concentration_63d},
    "tin_ext_034_down_day_count_high_vol_21d": {"inputs": ["close", "volume"], "func": tin_ext_034_down_day_count_high_vol_21d},
    "tin_ext_035_down_vol_streak": {"inputs": ["close", "volume"], "func": tin_ext_035_down_vol_streak},
    "tin_ext_036_directional_volume_imbalance_252d": {"inputs": ["close", "volume"], "func": tin_ext_036_directional_volume_imbalance_252d},
    "tin_ext_037_volume_intensity_accel_5d": {"inputs": ["volume"], "func": tin_ext_037_volume_intensity_accel_5d},
    "tin_ext_038_volume_intensity_accel_21d": {"inputs": ["volume"], "func": tin_ext_038_volume_intensity_accel_21d},
    "tin_ext_039_volume_ewm_fast_vs_slow": {"inputs": ["volume"], "func": tin_ext_039_volume_ewm_fast_vs_slow},
    "tin_ext_040_volume_ewm_ratio_fast_slow": {"inputs": ["volume"], "func": tin_ext_040_volume_ewm_ratio_fast_slow},
    "tin_ext_041_volume_5d_vs_63d_ratio": {"inputs": ["volume"], "func": tin_ext_041_volume_5d_vs_63d_ratio},
    "tin_ext_042_volume_accel_zscore_252d": {"inputs": ["volume"], "func": tin_ext_042_volume_accel_zscore_252d},
    "tin_ext_043_range_intensity_accel_21d": {"inputs": ["high", "low", "close"], "func": tin_ext_043_range_intensity_accel_21d},
    "tin_ext_044_volume_per_range_accel_21d": {"inputs": ["high", "low", "volume"], "func": tin_ext_044_volume_per_range_accel_21d},
    "tin_ext_045_volume_surge_consec_streak": {"inputs": ["volume"], "func": tin_ext_045_volume_surge_consec_streak},
    "tin_ext_046_volume_quiet_consec_streak": {"inputs": ["volume"], "func": tin_ext_046_volume_quiet_consec_streak},
    "tin_ext_047_volume_intensity_momentum_21d": {"inputs": ["volume"], "func": tin_ext_047_volume_intensity_momentum_21d},
    "tin_ext_048_volume_accel_positive_frac_63d": {"inputs": ["volume"], "func": tin_ext_048_volume_accel_positive_frac_63d},
    "tin_ext_049_quiet_before_burst_flag": {"inputs": ["volume"], "func": tin_ext_049_quiet_before_burst_flag},
    "tin_ext_050_quiet_before_burst_count_63d": {"inputs": ["volume"], "func": tin_ext_050_quiet_before_burst_count_63d},
    "tin_ext_051_days_since_volume_burst": {"inputs": ["volume"], "func": tin_ext_051_days_since_volume_burst},
    "tin_ext_052_days_since_volume_lull": {"inputs": ["volume"], "func": tin_ext_052_days_since_volume_lull},
    "tin_ext_053_lull_to_burst_transition_count_63d": {"inputs": ["volume"], "func": tin_ext_053_lull_to_burst_transition_count_63d},
    "tin_ext_054_volume_calm_then_max_flag": {"inputs": ["volume"], "func": tin_ext_054_volume_calm_then_max_flag},
    "tin_ext_055_active_after_lull_frac_21d": {"inputs": ["close", "high", "low", "volume"], "func": tin_ext_055_active_after_lull_frac_21d},
    "tin_ext_056_volume_compression_then_expansion_21d": {"inputs": ["volume"], "func": tin_ext_056_volume_compression_then_expansion_21d},
    "tin_ext_057_intensity_regime_shift_score_63d": {"inputs": ["volume"], "func": tin_ext_057_intensity_regime_shift_score_63d},
    "tin_ext_058_volume_low_then_high_252d_pct": {"inputs": ["volume"], "func": tin_ext_058_volume_low_then_high_252d_pct},
    "tin_ext_059_burst_isolation_score_21d": {"inputs": ["volume"], "func": tin_ext_059_burst_isolation_score_21d},
    "tin_ext_060_quiet_day_run_max_63d": {"inputs": ["volume"], "func": tin_ext_060_quiet_day_run_max_63d},
    "tin_ext_061_weekly_volume_sum_5d": {"inputs": ["volume"], "func": tin_ext_061_weekly_volume_sum_5d},
    "tin_ext_062_weekly_volume_zscore_252d": {"inputs": ["volume"], "func": tin_ext_062_weekly_volume_zscore_252d},
    "tin_ext_063_weekly_volume_5d_vs_21d_ratio": {"inputs": ["volume"], "func": tin_ext_063_weekly_volume_5d_vs_21d_ratio},
    "tin_ext_064_volume_dispersion_21d": {"inputs": ["volume"], "func": tin_ext_064_volume_dispersion_21d},
    "tin_ext_065_volume_dispersion_63d": {"inputs": ["volume"], "func": tin_ext_065_volume_dispersion_63d},
    "tin_ext_066_volume_dispersion_zscore_252d": {"inputs": ["volume"], "func": tin_ext_066_volume_dispersion_zscore_252d},
    "tin_ext_067_volume_skew_63d": {"inputs": ["volume"], "func": tin_ext_067_volume_skew_63d},
    "tin_ext_068_volume_kurt_63d": {"inputs": ["volume"], "func": tin_ext_068_volume_kurt_63d},
    "tin_ext_069_range_dispersion_21d": {"inputs": ["high", "low", "close"], "func": tin_ext_069_range_dispersion_21d},
    "tin_ext_070_volume_median_to_mean_ratio_63d": {"inputs": ["volume"], "func": tin_ext_070_volume_median_to_mean_ratio_63d},
    "tin_ext_071_volume_intensity_pct_rank_63d": {"inputs": ["volume"], "func": tin_ext_071_volume_intensity_pct_rank_63d},
    "tin_ext_072_volume_above_q90_count_63d": {"inputs": ["volume"], "func": tin_ext_072_volume_above_q90_count_63d},
    "tin_ext_073_intensity_expanding_pct_rank": {"inputs": ["volume"], "func": tin_ext_073_intensity_expanding_pct_rank},
    "tin_ext_074_volume_range_intensity_product_21d": {"inputs": ["high", "low", "close", "volume"], "func": tin_ext_074_volume_range_intensity_product_21d},
    "tin_ext_075_intensity_capitulation_composite": {"inputs": ["high", "low", "close", "volume"], "func": tin_ext_075_intensity_capitulation_composite},
}
