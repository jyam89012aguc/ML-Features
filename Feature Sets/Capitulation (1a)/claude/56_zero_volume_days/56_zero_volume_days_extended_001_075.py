"""
56_zero_volume_days -- Extended Features 001-075
Domain: zero-volume / near-zero-volume days and stale-price sessions -- deeper variants:
        multi-window z-scores and percentile ranks of zero/near-zero frequency,
        stale-price run lengths, volume drought streaks, EWM ratios, distributional
        shape of illiquid-day frequency, composite dead-session scores, threshold
        variants (1%, 2%, 10% of median), zero-vol coincidence with price moves.
Asset class: US equities | Daily OHLCV (price/volume ONLY -- SEP folder)
Target context: capitulation -- dead/illiquid sessions, no-trade and stale-price frequency
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
_NEAR_ZERO_K  = 0.05   # volume < 5% of trailing median
_NEAR_ZERO_K2 = 0.01   # volume < 1% of trailing median (extreme)
_NEAR_ZERO_K3 = 0.10   # volume < 10% of trailing median (mild)
_NEAR_ZERO_K4 = 0.02   # volume < 2% of trailing median
_STALE_TOL    = 1e-8   # |close - prior_close| < this


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

def _zero_vol(volume):
    return (volume == 0).astype(float)

def _near_zero(volume, k=_NEAR_ZERO_K):
    med = _rolling_median(volume, _TD_MON)
    return (volume < k * med).astype(float)

def _stale(close):
    return (close.diff(1).abs() < _STALE_TOL).astype(float)

def _dead_session(close, volume):
    return ((_zero_vol(volume) + _stale(close)) > 0).astype(float)


# --- Group A (001-010): Z-score of zero/near-zero frequency ---

def zvd_ext_001_zero_vol_frac_zscore_63d(close, high, low, open, volume):
    """63-day z-score of 21d zero-volume fraction."""
    zf = _rolling_sum(_zero_vol(volume), _TD_MON) / _TD_MON
    return _zscore(zf, _TD_QTR)

def zvd_ext_002_zero_vol_frac_zscore_252d(close, high, low, open, volume):
    """252-day z-score of 21d zero-volume fraction."""
    zf = _rolling_sum(_zero_vol(volume), _TD_MON) / _TD_MON
    return _zscore(zf, _TD_YEAR)

def zvd_ext_003_near_zero_frac_zscore_63d(close, high, low, open, volume):
    """63-day z-score of 21d near-zero-volume fraction."""
    nzf = _rolling_sum(_near_zero(volume), _TD_MON) / _TD_MON
    return _zscore(nzf, _TD_QTR)

def zvd_ext_004_near_zero_frac_zscore_252d(close, high, low, open, volume):
    """252-day z-score of 21d near-zero fraction."""
    nzf = _rolling_sum(_near_zero(volume), _TD_MON) / _TD_MON
    return _zscore(nzf, _TD_YEAR)

def zvd_ext_005_stale_frac_zscore_252d(close, high, low, open, volume):
    """252-day z-score of 21d stale-price fraction."""
    sf = _rolling_sum(_stale(close), _TD_MON) / _TD_MON
    return _zscore(sf, _TD_YEAR)

def zvd_ext_006_dead_session_frac_zscore_63d(close, high, low, open, volume):
    """63-day z-score of 21d dead-session fraction."""
    df = _rolling_sum(_dead_session(close, volume), _TD_MON) / _TD_MON
    return _zscore(df, _TD_QTR)

def zvd_ext_007_dead_session_frac_zscore_252d(close, high, low, open, volume):
    """252-day z-score of 21d dead-session fraction."""
    df = _rolling_sum(_dead_session(close, volume), _TD_MON) / _TD_MON
    return _zscore(df, _TD_YEAR)

def zvd_ext_008_zero_vol_frac_pctrank_63d(close, high, low, open, volume):
    """63-day percentile rank of zero-volume fraction (21d)."""
    zf = _rolling_sum(_zero_vol(volume), _TD_MON) / _TD_MON
    return _pct_rank(zf, _TD_QTR)

def zvd_ext_009_near_zero_frac_pctrank_252d(close, high, low, open, volume):
    """252-day percentile rank of near-zero fraction (21d)."""
    nzf = _rolling_sum(_near_zero(volume), _TD_MON) / _TD_MON
    return _pct_rank(nzf, _TD_YEAR)

def zvd_ext_010_stale_frac_pctrank_252d(close, high, low, open, volume):
    """252-day percentile rank of stale-price fraction (21d)."""
    sf = _rolling_sum(_stale(close), _TD_MON) / _TD_MON
    return _pct_rank(sf, _TD_YEAR)


# --- Group B (011-020): Additional threshold variants ---

def zvd_ext_011_extreme_near_zero_1pct_flag(close, high, low, open, volume):
    """Flag: volume < 1% of 21d median (extreme liquidity drought)."""
    return _near_zero(volume, _NEAR_ZERO_K2)

def zvd_ext_012_extreme_near_zero_1pct_count_21d(close, high, low, open, volume):
    """21-day count of extreme near-zero volume days (<1% of median)."""
    return _rolling_sum(_near_zero(volume, _NEAR_ZERO_K2), _TD_MON)

def zvd_ext_013_extreme_near_zero_1pct_count_63d(close, high, low, open, volume):
    """63-day count of extreme near-zero volume days (<1% of median)."""
    return _rolling_sum(_near_zero(volume, _NEAR_ZERO_K2), _TD_QTR)

def zvd_ext_014_mild_near_zero_10pct_flag(close, high, low, open, volume):
    """Flag: volume < 10% of 21d median (mild drought)."""
    return _near_zero(volume, _NEAR_ZERO_K3)

def zvd_ext_015_mild_near_zero_10pct_count_21d(close, high, low, open, volume):
    """21-day count of mild near-zero volume days (<10% of median)."""
    return _rolling_sum(_near_zero(volume, _NEAR_ZERO_K3), _TD_MON)

def zvd_ext_016_mild_near_zero_10pct_count_63d(close, high, low, open, volume):
    """63-day count of mild near-zero days."""
    return _rolling_sum(_near_zero(volume, _NEAR_ZERO_K3), _TD_QTR)

def zvd_ext_017_mild_near_zero_10pct_frac_252d(close, high, low, open, volume):
    """Fraction of 252d days with volume < 10% of 21d median."""
    return _rolling_sum(_near_zero(volume, _NEAR_ZERO_K3), _TD_YEAR) / _TD_YEAR

def zvd_ext_018_near_zero_2pct_flag(close, high, low, open, volume):
    """Flag: volume < 2% of 21d median."""
    return _near_zero(volume, _NEAR_ZERO_K4)

def zvd_ext_019_near_zero_2pct_count_63d(close, high, low, open, volume):
    """63-day count of near-zero 2% threshold days."""
    return _rolling_sum(_near_zero(volume, _NEAR_ZERO_K4), _TD_QTR)

def zvd_ext_020_near_zero_2pct_zscore_252d(close, high, low, open, volume):
    """252-day z-score of 21d near-zero-2% fraction."""
    nzf = _rolling_sum(_near_zero(volume, _NEAR_ZERO_K4), _TD_MON) / _TD_MON
    return _zscore(nzf, _TD_YEAR)


# --- Group C (021-030): Streak and run length deepening ---

def zvd_ext_021_near_zero_consec_streak(close, high, low, open, volume):
    """Consecutive near-zero-volume days (<5% of 21d median)."""
    return _consec_streak(_near_zero(volume) == 1.0)

def zvd_ext_022_stale_consec_streak(close, high, low, open, volume):
    """Consecutive stale-price days."""
    return _consec_streak(_stale(close) == 1.0)

def zvd_ext_023_dead_session_consec_streak(close, high, low, open, volume):
    """Consecutive dead-session days (zero or stale)."""
    return _consec_streak(_dead_session(close, volume) == 1.0)

def zvd_ext_024_vol_drought_consec_below_median(close, high, low, open, volume):
    """Consecutive days where volume < its 63d median."""
    med = _rolling_median(volume, _TD_QTR)
    return _consec_streak(volume < med)

def zvd_ext_025_vol_drought_consec_below_252d_mean(close, high, low, open, volume):
    """Consecutive days where volume < its 252d mean."""
    return _consec_streak(volume < _rolling_mean(volume, _TD_YEAR))

def zvd_ext_026_near_zero_max_streak_21d(close, high, low, open, volume):
    """Maximum near-zero-volume run length over 21 days."""
    nz = _near_zero(volume).astype(bool)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return nz.rolling(_TD_MON, min_periods=1).apply(_max_run, raw=True)

def zvd_ext_027_near_zero_max_streak_63d(close, high, low, open, volume):
    """Maximum near-zero-volume run length over 63 days."""
    nz = _near_zero(volume).astype(bool)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return nz.rolling(_TD_QTR, min_periods=1).apply(_max_run, raw=True)

def zvd_ext_028_stale_max_streak_63d(close, high, low, open, volume):
    """Maximum stale-price run length over 63 days."""
    st = _stale(close).astype(bool)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return st.rolling(_TD_QTR, min_periods=1).apply(_max_run, raw=True)

def zvd_ext_029_dead_session_max_streak_252d(close, high, low, open, volume):
    """Maximum dead-session run length over 252 days."""
    ds = _dead_session(close, volume).astype(bool)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return ds.rolling(_TD_YEAR, min_periods=1).apply(_max_run, raw=True)

def zvd_ext_030_zero_vol_pctrank_63d(close, high, low, open, volume):
    """63-day percentile rank of zero-volume count (21d)."""
    zc = _rolling_sum(_zero_vol(volume), _TD_MON)
    return _pct_rank(zc, _TD_QTR)


# --- Group D (031-040): EWM ratio deepening ---

def zvd_ext_031_near_zero_ewma5_vs_ewma63(close, high, low, open, volume):
    """EWM5 / EWM63 of near-zero-volume flag."""
    nz = _near_zero(volume)
    return _safe_div(_ewm_mean(nz, _TD_WEEK), _ewm_mean(nz, _TD_QTR))

def zvd_ext_032_stale_ewma5_vs_ewma63(close, high, low, open, volume):
    """EWM5 / EWM63 of stale-price flag."""
    st = _stale(close)
    return _safe_div(_ewm_mean(st, _TD_WEEK), _ewm_mean(st, _TD_QTR))

def zvd_ext_033_dead_session_ewma21(close, high, low, open, volume):
    """21-day EWM of dead-session flag."""
    return _ewm_mean(_dead_session(close, volume), _TD_MON)

def zvd_ext_034_dead_session_ewma63(close, high, low, open, volume):
    """63-day EWM of dead-session flag."""
    return _ewm_mean(_dead_session(close, volume), _TD_QTR)

def zvd_ext_035_vol_to_median_ratio_ewma5(close, high, low, open, volume):
    """EWM5 of volume/median_vol ratio (smoothed turnover signal)."""
    med = _rolling_median(volume, _TD_MON)
    ratio = _safe_div(volume, med)
    return _ewm_mean(ratio, _TD_WEEK)

def zvd_ext_036_vol_to_median_ratio_ewma21(close, high, low, open, volume):
    """EWM21 of volume/median_vol ratio."""
    med = _rolling_median(volume, _TD_MON)
    ratio = _safe_div(volume, med)
    return _ewm_mean(ratio, _TD_MON)

def zvd_ext_037_vol_to_median_zscore_252d(close, high, low, open, volume):
    """252-day z-score of volume/21d-median ratio."""
    med = _rolling_median(volume, _TD_MON)
    ratio = _safe_div(volume, med)
    return _zscore(ratio, _TD_YEAR)

def zvd_ext_038_vol_to_median_pctrank_252d(close, high, low, open, volume):
    """252-day pctrank of volume/21d-median ratio."""
    med = _rolling_median(volume, _TD_MON)
    ratio = _safe_div(volume, med)
    return _pct_rank(ratio, _TD_YEAR)

def zvd_ext_039_near_zero_frac_sma21_vs_sma252(close, high, low, open, volume):
    """SMA21 / SMA252 of near-zero flag (trend in illiquid-day rate)."""
    nz = _near_zero(volume)
    return _safe_div(_rolling_mean(nz, _TD_MON), _rolling_mean(nz, _TD_YEAR))

def zvd_ext_040_stale_frac_sma21_vs_sma252(close, high, low, open, volume):
    """SMA21 / SMA252 of stale-price flag."""
    st = _stale(close)
    return _safe_div(_rolling_mean(st, _TD_MON), _rolling_mean(st, _TD_YEAR))


# --- Group E (041-050): Coincidence with price moves ---

def zvd_ext_041_near_zero_on_down_day_count_21d(close, high, low, open, volume):
    """21-day count of near-zero volume on down days."""
    nz = _near_zero(volume)
    dn = (close.pct_change(1) < 0).astype(float)
    return _rolling_sum(nz * dn, _TD_MON)

def zvd_ext_042_near_zero_on_down_day_frac_63d(close, high, low, open, volume):
    """Fraction of 63d near-zero days that are also down days."""
    nz = _near_zero(volume)
    dn = (close.pct_change(1) < 0).astype(float)
    num = _rolling_sum(nz * dn, _TD_QTR)
    denom = _rolling_sum(nz, _TD_QTR)
    return _safe_div(num, denom)

def zvd_ext_043_stale_then_gap_count_21d(close, high, low, open, volume):
    """21-day count of large-move days following a stale-price day."""
    st = _stale(close)
    big_move = (close.pct_change(1).abs() > 0.05).astype(float)
    following_stale = st.shift(1).fillna(0.0) * big_move
    return _rolling_sum(following_stale, _TD_MON)

def zvd_ext_044_zero_vol_large_gap_coincidence_21d(close, high, low, open, volume):
    """21-day count of zero-volume days with a large next-day move (>5%)."""
    zv = _zero_vol(volume)
    big_next = (close.pct_change(1).abs().shift(-1).fillna(0.0) > 0.05).astype(float)
    return _rolling_sum(zv * big_next, _TD_MON)

def zvd_ext_045_near_zero_price_change_mean_21d(close, high, low, open, volume):
    """Mean absolute price change on near-zero-volume days over 21d."""
    nz = _near_zero(volume)
    abs_ret = close.pct_change(1).abs()
    return _safe_div(_rolling_sum(abs_ret * nz, _TD_MON), _rolling_sum(nz, _TD_MON))

def zvd_ext_046_zero_vol_then_high_vol_flag(close, high, low, open, volume):
    """Flag: zero-volume yesterday followed by high-volume today (>2x median)."""
    zv_lag = _zero_vol(volume).shift(1).fillna(0.0)
    med = _rolling_median(volume, _TD_MON)
    high_vol_today = (volume > 2.0 * med).astype(float)
    return zv_lag * high_vol_today

def zvd_ext_047_near_zero_vol_below5_close_21d(close, high, low, open, volume):
    """21-day count of days that are both near-zero AND close < $5."""
    nz = _near_zero(volume)
    sub5 = (close < 5.0).astype(float)
    return _rolling_sum(nz * sub5, _TD_MON)

def zvd_ext_048_stale_and_below5_count_21d(close, high, low, open, volume):
    """21-day count of stale-price days with close < $5."""
    st = _stale(close)
    sub5 = (close < 5.0).astype(float)
    return _rolling_sum(st * sub5, _TD_MON)

def zvd_ext_049_vol_drought_and_penny_streak(close, high, low, open, volume):
    """Consecutive days where volume < 10% of 63d median AND close < $5."""
    nz = _near_zero(volume, _NEAR_ZERO_K3)
    sub5 = (close < 5.0).astype(float)
    return _consec_streak((nz * sub5) == 1.0)

def zvd_ext_050_near_zero_count_252d(close, high, low, open, volume):
    """252-day count of near-zero volume days."""
    return _rolling_sum(_near_zero(volume), _TD_YEAR)


# --- Group F (051-060): Distributional shape ---

def zvd_ext_051_near_zero_frac_skew_63d(close, high, low, open, volume):
    """63-day rolling skewness of 5d near-zero volume fraction."""
    nzf = _rolling_sum(_near_zero(volume), _TD_WEEK) / _TD_WEEK
    return _roll_skew(nzf, _TD_QTR)

def zvd_ext_052_near_zero_frac_kurt_63d(close, high, low, open, volume):
    """63-day rolling kurtosis of 5d near-zero volume fraction."""
    nzf = _rolling_sum(_near_zero(volume), _TD_WEEK) / _TD_WEEK
    return _roll_kurt(nzf, _TD_QTR)

def zvd_ext_053_dead_session_frac_skew_63d(close, high, low, open, volume):
    """63-day skewness of 5d dead-session fraction."""
    dsf = _rolling_sum(_dead_session(close, volume), _TD_WEEK) / _TD_WEEK
    return _roll_skew(dsf, _TD_QTR)

def zvd_ext_054_vol_to_median_skew_63d(close, high, low, open, volume):
    """63-day skewness of volume/21d-median ratio."""
    med = _rolling_median(volume, _TD_MON)
    ratio = _safe_div(volume, med)
    return _roll_skew(ratio, _TD_QTR)

def zvd_ext_055_vol_to_median_kurt_63d(close, high, low, open, volume):
    """63-day kurtosis of volume/21d-median ratio."""
    med = _rolling_median(volume, _TD_MON)
    ratio = _safe_div(volume, med)
    return _roll_kurt(ratio, _TD_QTR)

def zvd_ext_056_stale_frac_63d(close, high, low, open, volume):
    """63-day fraction of stale-price days."""
    return _rolling_sum(_stale(close), _TD_QTR) / _TD_QTR

def zvd_ext_057_zero_vol_frac_skew_252d(close, high, low, open, volume):
    """252-day skewness of 21d zero-volume fraction."""
    zf = _rolling_sum(_zero_vol(volume), _TD_MON) / _TD_MON
    return _roll_skew(zf, _TD_YEAR)

def zvd_ext_058_zero_vol_count_63d_pctrank_252d(close, high, low, open, volume):
    """252-day pctrank of 63-day zero-volume count."""
    return _pct_rank(_rolling_sum(_zero_vol(volume), _TD_QTR), _TD_YEAR)

def zvd_ext_059_near_zero_count_126d(close, high, low, open, volume):
    """126-day count of near-zero volume days."""
    return _rolling_sum(_near_zero(volume), _TD_HALF)

def zvd_ext_060_dead_session_count_126d(close, high, low, open, volume):
    """126-day count of dead-session days."""
    return _rolling_sum(_dead_session(close, volume), _TD_HALF)


# --- Group G (061-070): OHLC range on illiquid days ---

def zvd_ext_061_range_on_near_zero_vol_mean_21d(close, high, low, open, volume):
    """Mean high-low range on near-zero-volume days over 21 days."""
    nz = _near_zero(volume)
    rng = high - low
    return _safe_div(_rolling_sum(rng * nz, _TD_MON), _rolling_sum(nz, _TD_MON))

def zvd_ext_062_range_on_near_zero_vol_mean_63d(close, high, low, open, volume):
    """Mean high-low range on near-zero-volume days over 63 days."""
    nz = _near_zero(volume)
    rng = high - low
    return _safe_div(_rolling_sum(rng * nz, _TD_QTR), _rolling_sum(nz, _TD_QTR))

def zvd_ext_063_flat_range_near_zero_flag(close, high, low, open, volume):
    """Flag: near-zero volume AND high == low (completely frozen session)."""
    nz = _near_zero(volume)
    flat = ((high - low).abs() < 1e-8).astype(float)
    return (nz * flat)

def zvd_ext_064_flat_range_near_zero_count_21d(close, high, low, open, volume):
    """21-day count of frozen near-zero sessions (flat range + near-zero vol)."""
    nz = _near_zero(volume)
    flat = ((high - low).abs() < 1e-8).astype(float)
    return _rolling_sum(nz * flat, _TD_MON)

def zvd_ext_065_open_eq_close_near_zero_flag(close, high, low, open, volume):
    """Flag: near-zero vol AND |close - open| < 1e-8 (body-less near-zero session)."""
    nz = _near_zero(volume)
    no_body = ((close - open).abs() < 1e-8).astype(float)
    return nz * no_body

def zvd_ext_066_near_zero_open_gap_mean_21d(close, high, low, open, volume):
    """Mean |open - prior_close| on near-zero-volume days over 21 days."""
    nz = _near_zero(volume)
    gap = (open - close.shift(1)).abs()
    return _safe_div(_rolling_sum(gap * nz, _TD_MON), _rolling_sum(nz, _TD_MON))

def zvd_ext_067_vol_drought_range_ratio(close, high, low, open, volume):
    """Mean (high-low)/close on near-zero days / mean (high-low)/close overall (21d)."""
    nz = _near_zero(volume)
    rng_pct = _safe_div(high - low, close.clip(lower=_EPS))
    near_zero_rng = _safe_div(_rolling_sum(rng_pct * nz, _TD_MON), _rolling_sum(nz, _TD_MON))
    overall_rng = _rolling_mean(rng_pct, _TD_MON)
    return _safe_div(near_zero_rng, overall_rng)

def zvd_ext_068_near_zero_vol_pctrank_252d(close, high, low, open, volume):
    """252-day pctrank of near-zero count (21d)."""
    nzc = _rolling_sum(_near_zero(volume), _TD_MON)
    return _pct_rank(nzc, _TD_YEAR)

def zvd_ext_069_stale_price_count_252d_pctrank(close, high, low, open, volume):
    """Expanding pctrank of 252d stale-price count."""
    sc = _rolling_sum(_stale(close), _TD_YEAR)
    return sc.expanding(min_periods=1).rank(pct=True)

def zvd_ext_070_composite_illiquid_score_21d(close, high, low, open, volume):
    """Composite: near-zero-count + stale-count + zero-count over 21d."""
    return (
        _rolling_sum(_zero_vol(volume), _TD_MON) +
        _rolling_sum(_near_zero(volume), _TD_MON) +
        _rolling_sum(_stale(close), _TD_MON)
    )


# --- Group H (071-075): Multi-window composite and normalization ---

def zvd_ext_071_composite_illiquid_zscore_252d(close, high, low, open, volume):
    """252-day z-score of composite illiquid score (21d window)."""
    comp = (
        _rolling_sum(_zero_vol(volume), _TD_MON) +
        _rolling_sum(_near_zero(volume), _TD_MON) +
        _rolling_sum(_stale(close), _TD_MON)
    )
    return _zscore(comp, _TD_YEAR)

def zvd_ext_072_composite_illiquid_pctrank_252d(close, high, low, open, volume):
    """252-day pctrank of composite illiquid score (21d)."""
    comp = (
        _rolling_sum(_zero_vol(volume), _TD_MON) +
        _rolling_sum(_near_zero(volume), _TD_MON) +
        _rolling_sum(_stale(close), _TD_MON)
    )
    return _pct_rank(comp, _TD_YEAR)

def zvd_ext_073_near_zero_10pct_frac_pctrank_252d(close, high, low, open, volume):
    """252-day pctrank of 21d mild near-zero fraction (<10% of median)."""
    nzf = _rolling_sum(_near_zero(volume, _NEAR_ZERO_K3), _TD_MON) / _TD_MON
    return _pct_rank(nzf, _TD_YEAR)

def zvd_ext_074_vol_to_median_min_21d(close, high, low, open, volume):
    """21-day rolling minimum of volume/21d-median ratio (most illiquid session)."""
    med = _rolling_median(volume, _TD_MON)
    ratio = _safe_div(volume, med)
    return _rolling_min(ratio, _TD_MON)

def zvd_ext_075_vol_to_median_min_252d(close, high, low, open, volume):
    """252-day rolling minimum of volume/21d-median ratio."""
    med = _rolling_median(volume, _TD_MON)
    ratio = _safe_div(volume, med)
    return _rolling_min(ratio, _TD_YEAR)


ZERO_VOLUME_DAYS_EXTENDED_REGISTRY_001_075 = {
    "zvd_ext_001_zero_vol_frac_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_001_zero_vol_frac_zscore_63d},
    "zvd_ext_002_zero_vol_frac_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_002_zero_vol_frac_zscore_252d},
    "zvd_ext_003_near_zero_frac_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_003_near_zero_frac_zscore_63d},
    "zvd_ext_004_near_zero_frac_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_004_near_zero_frac_zscore_252d},
    "zvd_ext_005_stale_frac_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_005_stale_frac_zscore_252d},
    "zvd_ext_006_dead_session_frac_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_006_dead_session_frac_zscore_63d},
    "zvd_ext_007_dead_session_frac_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_007_dead_session_frac_zscore_252d},
    "zvd_ext_008_zero_vol_frac_pctrank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_008_zero_vol_frac_pctrank_63d},
    "zvd_ext_009_near_zero_frac_pctrank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_009_near_zero_frac_pctrank_252d},
    "zvd_ext_010_stale_frac_pctrank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_010_stale_frac_pctrank_252d},
    "zvd_ext_011_extreme_near_zero_1pct_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_011_extreme_near_zero_1pct_flag},
    "zvd_ext_012_extreme_near_zero_1pct_count_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_012_extreme_near_zero_1pct_count_21d},
    "zvd_ext_013_extreme_near_zero_1pct_count_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_013_extreme_near_zero_1pct_count_63d},
    "zvd_ext_014_mild_near_zero_10pct_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_014_mild_near_zero_10pct_flag},
    "zvd_ext_015_mild_near_zero_10pct_count_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_015_mild_near_zero_10pct_count_21d},
    "zvd_ext_016_mild_near_zero_10pct_count_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_016_mild_near_zero_10pct_count_63d},
    "zvd_ext_017_mild_near_zero_10pct_frac_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_017_mild_near_zero_10pct_frac_252d},
    "zvd_ext_018_near_zero_2pct_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_018_near_zero_2pct_flag},
    "zvd_ext_019_near_zero_2pct_count_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_019_near_zero_2pct_count_63d},
    "zvd_ext_020_near_zero_2pct_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_020_near_zero_2pct_zscore_252d},
    "zvd_ext_021_near_zero_consec_streak": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_021_near_zero_consec_streak},
    "zvd_ext_022_stale_consec_streak": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_022_stale_consec_streak},
    "zvd_ext_023_dead_session_consec_streak": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_023_dead_session_consec_streak},
    "zvd_ext_024_vol_drought_consec_below_median": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_024_vol_drought_consec_below_median},
    "zvd_ext_025_vol_drought_consec_below_252d_mean": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_025_vol_drought_consec_below_252d_mean},
    "zvd_ext_026_near_zero_max_streak_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_026_near_zero_max_streak_21d},
    "zvd_ext_027_near_zero_max_streak_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_027_near_zero_max_streak_63d},
    "zvd_ext_028_stale_max_streak_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_028_stale_max_streak_63d},
    "zvd_ext_029_dead_session_max_streak_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_029_dead_session_max_streak_252d},
    "zvd_ext_030_zero_vol_pctrank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_030_zero_vol_pctrank_63d},
    "zvd_ext_031_near_zero_ewma5_vs_ewma63": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_031_near_zero_ewma5_vs_ewma63},
    "zvd_ext_032_stale_ewma5_vs_ewma63": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_032_stale_ewma5_vs_ewma63},
    "zvd_ext_033_dead_session_ewma21": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_033_dead_session_ewma21},
    "zvd_ext_034_dead_session_ewma63": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_034_dead_session_ewma63},
    "zvd_ext_035_vol_to_median_ratio_ewma5": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_035_vol_to_median_ratio_ewma5},
    "zvd_ext_036_vol_to_median_ratio_ewma21": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_036_vol_to_median_ratio_ewma21},
    "zvd_ext_037_vol_to_median_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_037_vol_to_median_zscore_252d},
    "zvd_ext_038_vol_to_median_pctrank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_038_vol_to_median_pctrank_252d},
    "zvd_ext_039_near_zero_frac_sma21_vs_sma252": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_039_near_zero_frac_sma21_vs_sma252},
    "zvd_ext_040_stale_frac_sma21_vs_sma252": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_040_stale_frac_sma21_vs_sma252},
    "zvd_ext_041_near_zero_on_down_day_count_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_041_near_zero_on_down_day_count_21d},
    "zvd_ext_042_near_zero_on_down_day_frac_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_042_near_zero_on_down_day_frac_63d},
    "zvd_ext_043_stale_then_gap_count_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_043_stale_then_gap_count_21d},
    "zvd_ext_044_zero_vol_large_gap_coincidence_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_044_zero_vol_large_gap_coincidence_21d},
    "zvd_ext_045_near_zero_price_change_mean_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_045_near_zero_price_change_mean_21d},
    "zvd_ext_046_zero_vol_then_high_vol_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_046_zero_vol_then_high_vol_flag},
    "zvd_ext_047_near_zero_vol_below5_close_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_047_near_zero_vol_below5_close_21d},
    "zvd_ext_048_stale_and_below5_count_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_048_stale_and_below5_count_21d},
    "zvd_ext_049_vol_drought_and_penny_streak": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_049_vol_drought_and_penny_streak},
    "zvd_ext_050_near_zero_count_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_050_near_zero_count_252d},
    "zvd_ext_051_near_zero_frac_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_051_near_zero_frac_skew_63d},
    "zvd_ext_052_near_zero_frac_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_052_near_zero_frac_kurt_63d},
    "zvd_ext_053_dead_session_frac_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_053_dead_session_frac_skew_63d},
    "zvd_ext_054_vol_to_median_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_054_vol_to_median_skew_63d},
    "zvd_ext_055_vol_to_median_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_055_vol_to_median_kurt_63d},
    "zvd_ext_056_stale_frac_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_056_stale_frac_63d},
    "zvd_ext_057_zero_vol_frac_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_057_zero_vol_frac_skew_252d},
    "zvd_ext_058_zero_vol_count_63d_pctrank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_058_zero_vol_count_63d_pctrank_252d},
    "zvd_ext_059_near_zero_count_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_059_near_zero_count_126d},
    "zvd_ext_060_dead_session_count_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_060_dead_session_count_126d},
    "zvd_ext_061_range_on_near_zero_vol_mean_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_061_range_on_near_zero_vol_mean_21d},
    "zvd_ext_062_range_on_near_zero_vol_mean_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_062_range_on_near_zero_vol_mean_63d},
    "zvd_ext_063_flat_range_near_zero_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_063_flat_range_near_zero_flag},
    "zvd_ext_064_flat_range_near_zero_count_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_064_flat_range_near_zero_count_21d},
    "zvd_ext_065_open_eq_close_near_zero_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_065_open_eq_close_near_zero_flag},
    "zvd_ext_066_near_zero_open_gap_mean_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_066_near_zero_open_gap_mean_21d},
    "zvd_ext_067_vol_drought_range_ratio": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_067_vol_drought_range_ratio},
    "zvd_ext_068_near_zero_vol_pctrank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_068_near_zero_vol_pctrank_252d},
    "zvd_ext_069_stale_price_count_252d_pctrank": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_069_stale_price_count_252d_pctrank},
    "zvd_ext_070_composite_illiquid_score_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_070_composite_illiquid_score_21d},
    "zvd_ext_071_composite_illiquid_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_071_composite_illiquid_zscore_252d},
    "zvd_ext_072_composite_illiquid_pctrank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_072_composite_illiquid_pctrank_252d},
    "zvd_ext_073_near_zero_10pct_frac_pctrank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_073_near_zero_10pct_frac_pctrank_252d},
    "zvd_ext_074_vol_to_median_min_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_074_vol_to_median_min_21d},
    "zvd_ext_075_vol_to_median_min_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": zvd_ext_075_vol_to_median_min_252d},
}
