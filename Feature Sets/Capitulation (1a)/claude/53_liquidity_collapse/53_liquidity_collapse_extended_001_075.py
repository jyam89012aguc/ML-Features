"""
53_liquidity_collapse -- Extended Features 001-075
Domain: illiquidity spikes -- deeper variants: Amihud skew/kurtosis, momentum,
        log-Amihud cross-window ratios, dollar-volume inverse proxies,
        CS spread and Roll spread variants, HL spread deepening,
        multi-spread composites, volume-side illiquidity z-scores.
Asset class: US equities | Daily OHLCV (price/volume ONLY -- SEP folder)
Target context: capitulation -- liquidity drying up / price-impact spikes
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9


def _safe_div(num, den):
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
    mu = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)

def _pct_rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)

def _consec_streak(cond):
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)

def _amihud(close, volume):
    ret = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(ret, dolvol)

def _safe_skew(arr):
    a = arr[~np.isnan(arr)]
    if len(a) < 3:
        return np.nan
    mu = a.mean()
    sig = a.std(ddof=1)
    if sig < _EPS:
        return 0.0
    return float(((a - mu) ** 3).mean() / sig ** 3)

def _safe_kurt(arr):
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    mu = a.mean()
    sig = a.std(ddof=1)
    if sig < _EPS:
        return 0.0
    return float(((a - mu) ** 4).mean() / sig ** 4 - 3.0)

def _roll_skew(s, w):
    return s.rolling(w, min_periods=max(3, w // 2)).apply(_safe_skew, raw=True)

def _roll_kurt(s, w):
    return s.rolling(w, min_periods=max(4, w // 2)).apply(_safe_kurt, raw=True)

def _cs_spread(high, low, close):
    h = _log_safe(high)
    l = _log_safe(low)
    beta = (h - l) ** 2
    beta2 = (h.shift(1) - l.shift(1)) ** 2
    gamma = (pd.concat([high, high.shift(1)], axis=1).max(axis=1).pipe(_log_safe) -
             pd.concat([low, low.shift(1)], axis=1).min(axis=1).pipe(_log_safe)) ** 2
    with np.errstate(invalid="ignore"):
        alpha = ((np.sqrt(2.0 * (beta + beta2)) - np.sqrt(beta + beta2)) /
                 (3.0 - 2.0 * np.sqrt(2.0)) -
                 np.sqrt(gamma / (3.0 - 2.0 * np.sqrt(2.0))))
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0.0)

def _roll_spread(close):
    ret = close.pct_change(1)
    cov = ret.rolling(21, min_periods=11).cov(ret.shift(1))
    return 2.0 * np.sqrt((-cov).clip(lower=0.0))

def _hl_spread(close, high, low):
    return _safe_div(high - low, close.clip(lower=_EPS))


# --- Group A (001-005): Amihud skew and kurtosis ---

def lqc_ext_001_amihud_skew_21d(close, volume):
    """21-day rolling skewness of Amihud illiquidity."""
    return _roll_skew(_amihud(close, volume), _TD_MON)

def lqc_ext_002_amihud_skew_63d(close, volume):
    """63-day rolling skewness of Amihud illiquidity."""
    return _roll_skew(_amihud(close, volume), _TD_QTR)

def lqc_ext_003_amihud_skew_126d(close, volume):
    """126-day rolling skewness of Amihud illiquidity."""
    return _roll_skew(_amihud(close, volume), _TD_HALF)

def lqc_ext_004_amihud_kurt_63d(close, volume):
    """63-day rolling excess kurtosis of Amihud illiquidity."""
    return _roll_kurt(_amihud(close, volume), _TD_QTR)

def lqc_ext_005_amihud_kurt_126d(close, volume):
    """126-day rolling excess kurtosis of Amihud illiquidity."""
    return _roll_kurt(_amihud(close, volume), _TD_HALF)


# --- Group B (006-010): Amihud momentum and EWM ---

def lqc_ext_006_amihud_mom5(close, volume):
    """5-day change in Amihud illiquidity."""
    a = _amihud(close, volume)
    return a - a.shift(5)

def lqc_ext_007_amihud_mom21(close, volume):
    """21-day change in Amihud illiquidity."""
    a = _amihud(close, volume)
    return a - a.shift(_TD_MON)

def lqc_ext_008_amihud_ewma5(close, volume):
    """5-day EWM of Amihud illiquidity."""
    return _ewm_mean(_amihud(close, volume), _TD_WEEK)

def lqc_ext_009_amihud_ewma5_vs_ewma63(close, volume):
    """EWM5 / EWM63 of Amihud illiquidity."""
    a = _amihud(close, volume)
    return _safe_div(_ewm_mean(a, _TD_WEEK), _ewm_mean(a, _TD_QTR))

def lqc_ext_010_amihud_ewma21_vs_sma252(close, volume):
    """EWM21 / SMA252 of Amihud illiquidity."""
    a = _amihud(close, volume)
    return _safe_div(_ewm_mean(a, _TD_MON), _rolling_mean(a, _TD_YEAR))


# --- Group C (011-015): Log Amihud variants ---

def lqc_ext_011_amihud_log_skew_63d(close, volume):
    """63-day rolling skewness of log(Amihud)."""
    return _roll_skew(_log_safe(_amihud(close, volume) + _EPS), _TD_QTR)

def lqc_ext_012_amihud_log_zscore_63d(close, volume):
    """63-day z-score of log(Amihud)."""
    return _zscore(_log_safe(_amihud(close, volume) + _EPS), _TD_QTR)

def lqc_ext_013_amihud_log_pctrank_63d(close, volume):
    """63-day percentile rank of log(Amihud)."""
    return _pct_rank(_log_safe(_amihud(close, volume) + _EPS), _TD_QTR)

def lqc_ext_014_amihud_log_ewma_ratio_5_21(close, volume):
    """EWM5 / EWM21 of log(Amihud)."""
    la = _log_safe(_amihud(close, volume) + _EPS)
    return _safe_div(_ewm_mean(la, _TD_WEEK), _ewm_mean(la, _TD_MON))

def lqc_ext_015_amihud_log_sma5_vs_sma63(close, volume):
    """SMA5 / SMA63 of log(Amihud)."""
    la = _log_safe(_amihud(close, volume) + _EPS)
    return _safe_div(_rolling_mean(la, _TD_WEEK), _rolling_mean(la, _TD_QTR))


# --- Group D (016-020): Inverse dollar-volume ---

def lqc_ext_016_inv_dolvol_sma5(close, volume):
    """5-day SMA of 1/dollar_volume."""
    return _rolling_mean(_safe_div(pd.Series(1.0, index=close.index), close * volume), _TD_WEEK)

def lqc_ext_017_inv_dolvol_sma21(close, volume):
    """21-day SMA of 1/dollar_volume."""
    return _rolling_mean(_safe_div(pd.Series(1.0, index=close.index), close * volume), _TD_MON)

def lqc_ext_018_inv_dolvol_sma63(close, volume):
    """63-day SMA of 1/dollar_volume."""
    return _rolling_mean(_safe_div(pd.Series(1.0, index=close.index), close * volume), _TD_QTR)

def lqc_ext_019_inv_dolvol_zscore_252d(close, volume):
    """252-day z-score of 1/dollar_volume."""
    return _zscore(_safe_div(pd.Series(1.0, index=close.index), close * volume), _TD_YEAR)

def lqc_ext_020_inv_dolvol_pctrank_252d(close, volume):
    """252-day percentile rank of 1/dollar_volume."""
    return _pct_rank(_safe_div(pd.Series(1.0, index=close.index), close * volume), _TD_YEAR)


# --- Group E (021-025): Absolute return per volume ---

def lqc_ext_021_abret_per_vol_sma5(close, volume):
    """5-day SMA of |daily return| / volume."""
    return _rolling_mean(_safe_div(close.pct_change(1).abs(), volume), _TD_WEEK)

def lqc_ext_022_abret_per_vol_sma21(close, volume):
    """21-day SMA of |daily return| / volume."""
    return _rolling_mean(_safe_div(close.pct_change(1).abs(), volume), _TD_MON)

def lqc_ext_023_abret_per_vol_zscore_252d(close, volume):
    """252-day z-score of |ret|/volume."""
    return _zscore(_safe_div(close.pct_change(1).abs(), volume), _TD_YEAR)

def lqc_ext_024_abret_per_vol_pctrank_252d(close, volume):
    """252-day percentile rank of |ret|/volume."""
    return _pct_rank(_safe_div(close.pct_change(1).abs(), volume), _TD_YEAR)

def lqc_ext_025_abret_per_vol_skew_63d(close, volume):
    """63-day skewness of |ret|/volume."""
    return _roll_skew(_safe_div(close.pct_change(1).abs(), volume), _TD_QTR)


# --- Group F (026-035): CS spread deepening ---

def lqc_ext_026_cs_spread_pctrank_21d(close, high, low):
    """21-day percentile rank of CS spread."""
    return _pct_rank(_cs_spread(high, low, close), _TD_MON)

def lqc_ext_027_cs_spread_pctrank_63d(close, high, low):
    """63-day percentile rank of CS spread."""
    return _pct_rank(_cs_spread(high, low, close), _TD_QTR)

def lqc_ext_028_cs_spread_skew_63d(close, high, low):
    """63-day skewness of CS spread."""
    return _roll_skew(_cs_spread(high, low, close), _TD_QTR)

def lqc_ext_029_cs_spread_kurt_63d(close, high, low):
    """63-day kurtosis of CS spread."""
    return _roll_kurt(_cs_spread(high, low, close), _TD_QTR)

def lqc_ext_030_cs_spread_ewma21(close, high, low):
    """21-day EWM of CS spread."""
    return _ewm_mean(_cs_spread(high, low, close), _TD_MON)

def lqc_ext_031_cs_spread_ewma63(close, high, low):
    """63-day EWM of CS spread."""
    return _ewm_mean(_cs_spread(high, low, close), _TD_QTR)

def lqc_ext_032_cs_spread_mom21(close, high, low):
    """21-day change in CS spread."""
    cs = _cs_spread(high, low, close)
    return cs - cs.shift(_TD_MON)

def lqc_ext_033_cs_spread_zscore_21d(close, high, low):
    """21-day z-score of CS spread."""
    return _zscore(_cs_spread(high, low, close), _TD_MON)

def lqc_ext_034_cs_spread_max_252d(close, high, low):
    """252-day maximum of CS spread."""
    return _rolling_max(_cs_spread(high, low, close), _TD_YEAR)

def lqc_ext_035_cs_spread_sma21_vs_sma252(close, high, low):
    """SMA21 / SMA252 of CS spread."""
    cs = _cs_spread(high, low, close)
    return _safe_div(_rolling_mean(cs, _TD_MON), _rolling_mean(cs, _TD_YEAR))


# --- Group G (036-040): Roll spread deepening ---

def lqc_ext_036_roll_spread_pctrank_21d(close):
    """21-day percentile rank of Roll spread."""
    return _pct_rank(_roll_spread(close), _TD_MON)

def lqc_ext_037_roll_spread_pctrank_63d(close):
    """63-day percentile rank of Roll spread."""
    return _pct_rank(_roll_spread(close), _TD_QTR)

def lqc_ext_038_roll_spread_skew_63d(close):
    """63-day skewness of Roll spread."""
    return _roll_skew(_roll_spread(close), _TD_QTR)

def lqc_ext_039_roll_spread_ewma21(close):
    """21-day EWM of Roll spread."""
    return _ewm_mean(_roll_spread(close), _TD_MON)

def lqc_ext_040_roll_spread_mom21(close):
    """21-day change in Roll spread."""
    rs = _roll_spread(close)
    return rs - rs.shift(_TD_MON)


# --- Group H (041-050): HL spread proxy deepening ---

def lqc_ext_041_hl_spread_pctrank_21d(close, high, low):
    """21-day percentile rank of HL spread proxy."""
    return _pct_rank(_hl_spread(close, high, low), _TD_MON)

def lqc_ext_042_hl_spread_pctrank_252d(close, high, low):
    """252-day percentile rank of HL spread proxy."""
    return _pct_rank(_hl_spread(close, high, low), _TD_YEAR)

def lqc_ext_043_hl_spread_skew_63d(close, high, low):
    """63-day skewness of HL spread proxy."""
    return _roll_skew(_hl_spread(close, high, low), _TD_QTR)

def lqc_ext_044_hl_spread_kurt_63d(close, high, low):
    """63-day kurtosis of HL spread proxy."""
    return _roll_kurt(_hl_spread(close, high, low), _TD_QTR)

def lqc_ext_045_hl_spread_ewma5_vs_sma252(close, high, low):
    """EWM5 / SMA252 of HL spread proxy."""
    hl = _hl_spread(close, high, low)
    return _safe_div(_ewm_mean(hl, _TD_WEEK), _rolling_mean(hl, _TD_YEAR))

def lqc_ext_046_hl_spread_zscore_21d(close, high, low):
    """21-day z-score of HL spread proxy."""
    return _zscore(_hl_spread(close, high, low), _TD_MON)

def lqc_ext_047_hl_spread_consec_above_mean(close, high, low):
    """Consecutive days HL spread > its 63d mean."""
    hl = _hl_spread(close, high, low)
    return _consec_streak(hl > _rolling_mean(hl, _TD_QTR))

def lqc_ext_048_hl_spread_mom21(close, high, low):
    """21-day change in HL spread proxy."""
    hl = _hl_spread(close, high, low)
    return hl - hl.shift(_TD_MON)

def lqc_ext_049_hl_spread_sma5_vs_sma63(close, high, low):
    """SMA5 / SMA63 of HL spread proxy."""
    hl = _hl_spread(close, high, low)
    return _safe_div(_rolling_mean(hl, _TD_WEEK), _rolling_mean(hl, _TD_QTR))

def lqc_ext_050_hl_spread_sma21_vs_sma252(close, high, low):
    """SMA21 / SMA252 of HL spread proxy."""
    hl = _hl_spread(close, high, low)
    return _safe_div(_rolling_mean(hl, _TD_MON), _rolling_mean(hl, _TD_YEAR))


# --- Group I (051-055): Multi-spread composites ---

def lqc_ext_051_illiq_composite_sma5(close, high, low, volume):
    """5-day SMA of composite illiquidity (amihud + hl_spread)."""
    comp = _amihud(close, volume) + _hl_spread(close, high, low)
    return _rolling_mean(comp, _TD_WEEK)

def lqc_ext_052_illiq_composite_skew_63d(close, high, low, volume):
    """63-day skewness of composite illiquidity."""
    comp = _amihud(close, volume) + _hl_spread(close, high, low)
    return _roll_skew(comp, _TD_QTR)

def lqc_ext_053_illiq_composite_ewma21(close, high, low, volume):
    """21-day EWM of composite illiquidity."""
    comp = _amihud(close, volume) + _hl_spread(close, high, low)
    return _ewm_mean(comp, _TD_MON)

def lqc_ext_054_illiq_composite_mom21(close, high, low, volume):
    """21-day change in composite illiquidity."""
    comp = _amihud(close, volume) + _hl_spread(close, high, low)
    return comp - comp.shift(_TD_MON)

def lqc_ext_055_illiq_composite_pctrank_63d(close, high, low, volume):
    """63-day percentile rank of composite illiquidity."""
    comp = _amihud(close, volume) + _hl_spread(close, high, low)
    return _pct_rank(comp, _TD_QTR)


# --- Group J (056-060): Amihud-volume interaction ---

def lqc_ext_056_amihud_times_vol_spike(close, volume):
    """Amihud * volume-to-median ratio (amplified illiquidity spike)."""
    a = _amihud(close, volume)
    vm = _safe_div(volume, _rolling_median(volume, _TD_MON))
    return a * vm

def lqc_ext_057_amihud_down_day_mean_63d(close, volume):
    """Mean Amihud on down days over 63 days."""
    a = _amihud(close, volume)
    dn = (close.pct_change(1) < 0).astype(float)
    return _safe_div(_rolling_sum(a * dn, _TD_QTR), _rolling_sum(dn, _TD_QTR))

def lqc_ext_058_amihud_up_day_mean_63d(close, volume):
    """Mean Amihud on up days over 63 days."""
    a = _amihud(close, volume)
    up = (close.pct_change(1) >= 0).astype(float)
    return _safe_div(_rolling_sum(a * up, _TD_QTR), _rolling_sum(up, _TD_QTR))

def lqc_ext_059_amihud_down_vs_up_ratio_63d(close, volume):
    """63-day ratio: mean Amihud on down days / mean Amihud on up days."""
    a = _amihud(close, volume)
    dn = (close.pct_change(1) < 0).astype(float)
    up = 1.0 - dn
    dm = _safe_div(_rolling_sum(a * dn, _TD_QTR), _rolling_sum(dn, _TD_QTR))
    um = _safe_div(_rolling_sum(a * up, _TD_QTR), _rolling_sum(up, _TD_QTR))
    return _safe_div(dm, um)

def lqc_ext_060_amihud_high_vol_mean_21d(close, volume):
    """Mean Amihud on high-volume days (> median) over 21 days."""
    a = _amihud(close, volume)
    hv = (volume > _rolling_median(volume, _TD_MON)).astype(float)
    return _safe_div(_rolling_sum(a * hv, _TD_MON), _rolling_sum(hv, _TD_MON))


# --- Group K (061-065): Regime flags and streaks ---

def lqc_ext_061_amihud_pctrank_5d(close, volume):
    """5-day percentile rank of Amihud illiquidity."""
    return _pct_rank(_amihud(close, volume), _TD_WEEK)

def lqc_ext_062_amihud_spike_gt1std_21d(close, volume):
    """Count of days Amihud > mean+1std over 21 days."""
    a = _amihud(close, volume)
    mu = _rolling_mean(a, _TD_MON)
    sig = _rolling_std(a, _TD_MON)
    return (a > mu + sig).astype(float).rolling(_TD_MON, min_periods=1).sum()

def lqc_ext_063_amihud_spike_gt4std_252d(close, volume):
    """Count of days Amihud > mean+4std over 252 days (extreme event)."""
    a = _amihud(close, volume)
    mu = _rolling_mean(a, _TD_YEAR)
    sig = _rolling_std(a, _TD_YEAR)
    return (a > mu + 4.0 * sig).astype(float).rolling(_TD_YEAR, min_periods=1).sum()

def lqc_ext_064_amihud_consec_pctrank_above90(close, volume):
    """Consecutive days Amihud pctrank(252d) > 0.9."""
    return _consec_streak(_pct_rank(_amihud(close, volume), _TD_YEAR) > 0.9)

def lqc_ext_065_amihud_sma21_consec_above_sma252(close, volume):
    """Consecutive days where Amihud SMA21 > Amihud SMA252."""
    a = _amihud(close, volume)
    return _consec_streak(_rolling_mean(a, _TD_MON) > _rolling_mean(a, _TD_YEAR))


# --- Group L (066-070): Volume-side illiquidity ---

def lqc_ext_066_log_volume_zscore_21d(close, volume):
    """21-day z-score of log(volume)."""
    return _zscore(_log_safe(volume), _TD_MON)

def lqc_ext_067_log_volume_zscore_252d(close, volume):
    """252-day z-score of log(volume)."""
    return _zscore(_log_safe(volume), _TD_YEAR)

def lqc_ext_068_log_volume_pctrank_252d(close, volume):
    """252-day percentile rank of log(volume)."""
    return _pct_rank(_log_safe(volume), _TD_YEAR)

def lqc_ext_069_log_dolvol_zscore_252d(close, volume):
    """252-day z-score of log(dollar_volume)."""
    return _zscore(_log_safe(close * volume), _TD_YEAR)

def lqc_ext_070_log_dolvol_pctrank_252d(close, volume):
    """252-day percentile rank of log(dollar_volume)."""
    return _pct_rank(_log_safe(close * volume), _TD_YEAR)


# --- Group M (071-075): Multi-spread correlations and composite regime ---

def lqc_ext_071_amihud_cs_spread_corr_21d(close, high, low, volume):
    """21-day rolling correlation between Amihud and CS spread."""
    a = _amihud(close, volume)
    cs = _cs_spread(high, low, close)
    return a.rolling(_TD_MON, min_periods=5).corr(cs)

def lqc_ext_072_amihud_cs_combined_zscore_252d(close, high, low, volume):
    """252-day z-score of (amihud + cs_spread)."""
    return _zscore(_amihud(close, volume) + _cs_spread(high, low, close), _TD_YEAR)

def lqc_ext_073_amihud_cs_sum_pctrank_252d(close, high, low, volume):
    """252-day pctrank of (amihud + cs_spread)."""
    return _pct_rank(_amihud(close, volume) + _cs_spread(high, low, close), _TD_YEAR)

def lqc_ext_074_cs_spread_above_2x_21d_flag(close, high, low):
    """Flag: CS spread > 2x its 21d mean."""
    cs = _cs_spread(high, low, close)
    return (cs > 2.0 * _rolling_mean(cs, _TD_MON)).astype(float)

def lqc_ext_075_illiq_regime_score_21d(close, high, low, volume):
    """Composite regime score: sum of z-scores of amihud, hl_spread, inv_dolvol (21d)."""
    za = _zscore(_amihud(close, volume), _TD_MON)
    zhl = _zscore(_hl_spread(close, high, low), _TD_MON)
    inv = _safe_div(pd.Series(1.0, index=close.index), close * volume)
    ziv = _zscore(inv, _TD_MON)
    return za.fillna(0.0) + zhl.fillna(0.0) + ziv.fillna(0.0)


LIQUIDITY_COLLAPSE_EXTENDED_REGISTRY_001_075 = {
    "lqc_ext_001_amihud_skew_21d": {"inputs": ["close", "volume"], "func": lqc_ext_001_amihud_skew_21d},
    "lqc_ext_002_amihud_skew_63d": {"inputs": ["close", "volume"], "func": lqc_ext_002_amihud_skew_63d},
    "lqc_ext_003_amihud_skew_126d": {"inputs": ["close", "volume"], "func": lqc_ext_003_amihud_skew_126d},
    "lqc_ext_004_amihud_kurt_63d": {"inputs": ["close", "volume"], "func": lqc_ext_004_amihud_kurt_63d},
    "lqc_ext_005_amihud_kurt_126d": {"inputs": ["close", "volume"], "func": lqc_ext_005_amihud_kurt_126d},
    "lqc_ext_006_amihud_mom5": {"inputs": ["close", "volume"], "func": lqc_ext_006_amihud_mom5},
    "lqc_ext_007_amihud_mom21": {"inputs": ["close", "volume"], "func": lqc_ext_007_amihud_mom21},
    "lqc_ext_008_amihud_ewma5": {"inputs": ["close", "volume"], "func": lqc_ext_008_amihud_ewma5},
    "lqc_ext_009_amihud_ewma5_vs_ewma63": {"inputs": ["close", "volume"], "func": lqc_ext_009_amihud_ewma5_vs_ewma63},
    "lqc_ext_010_amihud_ewma21_vs_sma252": {"inputs": ["close", "volume"], "func": lqc_ext_010_amihud_ewma21_vs_sma252},
    "lqc_ext_011_amihud_log_skew_63d": {"inputs": ["close", "volume"], "func": lqc_ext_011_amihud_log_skew_63d},
    "lqc_ext_012_amihud_log_zscore_63d": {"inputs": ["close", "volume"], "func": lqc_ext_012_amihud_log_zscore_63d},
    "lqc_ext_013_amihud_log_pctrank_63d": {"inputs": ["close", "volume"], "func": lqc_ext_013_amihud_log_pctrank_63d},
    "lqc_ext_014_amihud_log_ewma_ratio_5_21": {"inputs": ["close", "volume"], "func": lqc_ext_014_amihud_log_ewma_ratio_5_21},
    "lqc_ext_015_amihud_log_sma5_vs_sma63": {"inputs": ["close", "volume"], "func": lqc_ext_015_amihud_log_sma5_vs_sma63},
    "lqc_ext_016_inv_dolvol_sma5": {"inputs": ["close", "volume"], "func": lqc_ext_016_inv_dolvol_sma5},
    "lqc_ext_017_inv_dolvol_sma21": {"inputs": ["close", "volume"], "func": lqc_ext_017_inv_dolvol_sma21},
    "lqc_ext_018_inv_dolvol_sma63": {"inputs": ["close", "volume"], "func": lqc_ext_018_inv_dolvol_sma63},
    "lqc_ext_019_inv_dolvol_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_ext_019_inv_dolvol_zscore_252d},
    "lqc_ext_020_inv_dolvol_pctrank_252d": {"inputs": ["close", "volume"], "func": lqc_ext_020_inv_dolvol_pctrank_252d},
    "lqc_ext_021_abret_per_vol_sma5": {"inputs": ["close", "volume"], "func": lqc_ext_021_abret_per_vol_sma5},
    "lqc_ext_022_abret_per_vol_sma21": {"inputs": ["close", "volume"], "func": lqc_ext_022_abret_per_vol_sma21},
    "lqc_ext_023_abret_per_vol_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_ext_023_abret_per_vol_zscore_252d},
    "lqc_ext_024_abret_per_vol_pctrank_252d": {"inputs": ["close", "volume"], "func": lqc_ext_024_abret_per_vol_pctrank_252d},
    "lqc_ext_025_abret_per_vol_skew_63d": {"inputs": ["close", "volume"], "func": lqc_ext_025_abret_per_vol_skew_63d},
    "lqc_ext_026_cs_spread_pctrank_21d": {"inputs": ["close", "high", "low"], "func": lqc_ext_026_cs_spread_pctrank_21d},
    "lqc_ext_027_cs_spread_pctrank_63d": {"inputs": ["close", "high", "low"], "func": lqc_ext_027_cs_spread_pctrank_63d},
    "lqc_ext_028_cs_spread_skew_63d": {"inputs": ["close", "high", "low"], "func": lqc_ext_028_cs_spread_skew_63d},
    "lqc_ext_029_cs_spread_kurt_63d": {"inputs": ["close", "high", "low"], "func": lqc_ext_029_cs_spread_kurt_63d},
    "lqc_ext_030_cs_spread_ewma21": {"inputs": ["close", "high", "low"], "func": lqc_ext_030_cs_spread_ewma21},
    "lqc_ext_031_cs_spread_ewma63": {"inputs": ["close", "high", "low"], "func": lqc_ext_031_cs_spread_ewma63},
    "lqc_ext_032_cs_spread_mom21": {"inputs": ["close", "high", "low"], "func": lqc_ext_032_cs_spread_mom21},
    "lqc_ext_033_cs_spread_zscore_21d": {"inputs": ["close", "high", "low"], "func": lqc_ext_033_cs_spread_zscore_21d},
    "lqc_ext_034_cs_spread_max_252d": {"inputs": ["close", "high", "low"], "func": lqc_ext_034_cs_spread_max_252d},
    "lqc_ext_035_cs_spread_sma21_vs_sma252": {"inputs": ["close", "high", "low"], "func": lqc_ext_035_cs_spread_sma21_vs_sma252},
    "lqc_ext_036_roll_spread_pctrank_21d": {"inputs": ["close"], "func": lqc_ext_036_roll_spread_pctrank_21d},
    "lqc_ext_037_roll_spread_pctrank_63d": {"inputs": ["close"], "func": lqc_ext_037_roll_spread_pctrank_63d},
    "lqc_ext_038_roll_spread_skew_63d": {"inputs": ["close"], "func": lqc_ext_038_roll_spread_skew_63d},
    "lqc_ext_039_roll_spread_ewma21": {"inputs": ["close"], "func": lqc_ext_039_roll_spread_ewma21},
    "lqc_ext_040_roll_spread_mom21": {"inputs": ["close"], "func": lqc_ext_040_roll_spread_mom21},
    "lqc_ext_041_hl_spread_pctrank_21d": {"inputs": ["close", "high", "low"], "func": lqc_ext_041_hl_spread_pctrank_21d},
    "lqc_ext_042_hl_spread_pctrank_252d": {"inputs": ["close", "high", "low"], "func": lqc_ext_042_hl_spread_pctrank_252d},
    "lqc_ext_043_hl_spread_skew_63d": {"inputs": ["close", "high", "low"], "func": lqc_ext_043_hl_spread_skew_63d},
    "lqc_ext_044_hl_spread_kurt_63d": {"inputs": ["close", "high", "low"], "func": lqc_ext_044_hl_spread_kurt_63d},
    "lqc_ext_045_hl_spread_ewma5_vs_sma252": {"inputs": ["close", "high", "low"], "func": lqc_ext_045_hl_spread_ewma5_vs_sma252},
    "lqc_ext_046_hl_spread_zscore_21d": {"inputs": ["close", "high", "low"], "func": lqc_ext_046_hl_spread_zscore_21d},
    "lqc_ext_047_hl_spread_consec_above_mean": {"inputs": ["close", "high", "low"], "func": lqc_ext_047_hl_spread_consec_above_mean},
    "lqc_ext_048_hl_spread_mom21": {"inputs": ["close", "high", "low"], "func": lqc_ext_048_hl_spread_mom21},
    "lqc_ext_049_hl_spread_sma5_vs_sma63": {"inputs": ["close", "high", "low"], "func": lqc_ext_049_hl_spread_sma5_vs_sma63},
    "lqc_ext_050_hl_spread_sma21_vs_sma252": {"inputs": ["close", "high", "low"], "func": lqc_ext_050_hl_spread_sma21_vs_sma252},
    "lqc_ext_051_illiq_composite_sma5": {"inputs": ["close", "high", "low", "volume"], "func": lqc_ext_051_illiq_composite_sma5},
    "lqc_ext_052_illiq_composite_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_ext_052_illiq_composite_skew_63d},
    "lqc_ext_053_illiq_composite_ewma21": {"inputs": ["close", "high", "low", "volume"], "func": lqc_ext_053_illiq_composite_ewma21},
    "lqc_ext_054_illiq_composite_mom21": {"inputs": ["close", "high", "low", "volume"], "func": lqc_ext_054_illiq_composite_mom21},
    "lqc_ext_055_illiq_composite_pctrank_63d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_ext_055_illiq_composite_pctrank_63d},
    "lqc_ext_056_amihud_times_vol_spike": {"inputs": ["close", "volume"], "func": lqc_ext_056_amihud_times_vol_spike},
    "lqc_ext_057_amihud_down_day_mean_63d": {"inputs": ["close", "volume"], "func": lqc_ext_057_amihud_down_day_mean_63d},
    "lqc_ext_058_amihud_up_day_mean_63d": {"inputs": ["close", "volume"], "func": lqc_ext_058_amihud_up_day_mean_63d},
    "lqc_ext_059_amihud_down_vs_up_ratio_63d": {"inputs": ["close", "volume"], "func": lqc_ext_059_amihud_down_vs_up_ratio_63d},
    "lqc_ext_060_amihud_high_vol_mean_21d": {"inputs": ["close", "volume"], "func": lqc_ext_060_amihud_high_vol_mean_21d},
    "lqc_ext_061_amihud_pctrank_5d": {"inputs": ["close", "volume"], "func": lqc_ext_061_amihud_pctrank_5d},
    "lqc_ext_062_amihud_spike_gt1std_21d": {"inputs": ["close", "volume"], "func": lqc_ext_062_amihud_spike_gt1std_21d},
    "lqc_ext_063_amihud_spike_gt4std_252d": {"inputs": ["close", "volume"], "func": lqc_ext_063_amihud_spike_gt4std_252d},
    "lqc_ext_064_amihud_consec_pctrank_above90": {"inputs": ["close", "volume"], "func": lqc_ext_064_amihud_consec_pctrank_above90},
    "lqc_ext_065_amihud_sma21_consec_above_sma252": {"inputs": ["close", "volume"], "func": lqc_ext_065_amihud_sma21_consec_above_sma252},
    "lqc_ext_066_log_volume_zscore_21d": {"inputs": ["close", "volume"], "func": lqc_ext_066_log_volume_zscore_21d},
    "lqc_ext_067_log_volume_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_ext_067_log_volume_zscore_252d},
    "lqc_ext_068_log_volume_pctrank_252d": {"inputs": ["close", "volume"], "func": lqc_ext_068_log_volume_pctrank_252d},
    "lqc_ext_069_log_dolvol_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_ext_069_log_dolvol_zscore_252d},
    "lqc_ext_070_log_dolvol_pctrank_252d": {"inputs": ["close", "volume"], "func": lqc_ext_070_log_dolvol_pctrank_252d},
    "lqc_ext_071_amihud_cs_spread_corr_21d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_ext_071_amihud_cs_spread_corr_21d},
    "lqc_ext_072_amihud_cs_combined_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_ext_072_amihud_cs_combined_zscore_252d},
    "lqc_ext_073_amihud_cs_sum_pctrank_252d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_ext_073_amihud_cs_sum_pctrank_252d},
    "lqc_ext_074_cs_spread_above_2x_21d_flag": {"inputs": ["close", "high", "low"], "func": lqc_ext_074_cs_spread_above_2x_21d_flag},
    "lqc_ext_075_illiq_regime_score_21d": {"inputs": ["close", "high", "low", "volume"], "func": lqc_ext_075_illiq_regime_score_21d},
}
