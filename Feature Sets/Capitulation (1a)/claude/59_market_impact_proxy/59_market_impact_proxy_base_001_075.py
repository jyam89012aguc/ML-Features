"""
59_market_impact_proxy — Base Features 001-075
Domain: market-impact / return-per-dollar-volume sensitivity — Kyle lambda proxy
  (rolling slope of return on signed volume), Amivest liquidity ratio (dollar volume /
  |return|), return-per-dollar-volume, range-per-dollar-volume, Pastor-Stambaugh-style
  signed-volume return reversal, impact asymmetry on up vs down days.
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
    mu  = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


def _pct_rank(s, w):
    """Rolling percentile rank of s within trailing w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _consec_streak(cond):
    """Count consecutive True values up to each row (backward-looking)."""
    c      = cond.astype(int)
    group  = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond, w):
    """Maximum consecutive-True run over trailing w periods."""
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
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _amivest(close, volume):
    """Daily Amivest liquidity ratio: dollar_volume / |return|."""
    ret    = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(dolvol, ret.replace(0, np.nan))


def _ret_per_dolvol(close, volume):
    """Daily return-per-dollar-volume: |return| / dollar_volume."""
    ret    = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(ret, dolvol)


def _kyle_lambda_fast(close, volume, w):
    """Efficient rolling Kyle lambda: OLS slope of daily return on signed dollar volume."""
    ret      = close.pct_change(1)
    dolvol   = close * volume
    sign_vol = np.sign(ret) * dolvol
    df = pd.DataFrame({"sv": sign_vol, "rt": ret}).dropna()
    sv_vals = df["sv"].values
    rt_vals = df["rt"].values
    sv_idx  = df.index
    min_p   = max(2, w // 2)
    results = pd.Series(np.nan, index=close.index, dtype=float)
    for i in range(len(sv_vals)):
        start = max(0, i - w + 1)
        x = sv_vals[start: i + 1]
        y = rt_vals[start: i + 1]
        if len(x) < min_p:
            continue
        xm = x.mean(); ym = y.mean()
        num = ((x - xm) * (y - ym)).sum()
        den = ((x - xm) ** 2).sum()
        results.loc[sv_idx[i]] = num / den if abs(den) > _EPS else np.nan
    return results


def _range_per_dolvol(high, low, close, volume):
    """Intraday range per dollar volume: (H-L)/close / dollar_volume."""
    rng    = (high - low) / close.replace(0, np.nan)
    dolvol = close * volume
    return _safe_div(rng, dolvol)


def _sqrt_impact(close, volume):
    """Square-root impact proxy: |return| / sqrt(dollar_volume)."""
    ret    = close.pct_change(1).abs()
    dolvol = (close * volume).clip(lower=_EPS)
    return ret / np.sqrt(dolvol)


# -- Feature functions 001-075 ------------------------------------------------

# --- Group A (001-015): Kyle lambda --- rolling slope of return on signed volume ---

def mip_001_kyle_lambda_21d(close, volume):
    """Rolling 21-day Kyle lambda: price impact per unit signed dollar volume."""
    return _kyle_lambda_fast(close, volume, _TD_MON)


def mip_002_kyle_lambda_63d(close, volume):
    """Rolling 63-day Kyle lambda: quarterly price-impact sensitivity."""
    return _kyle_lambda_fast(close, volume, _TD_QTR)


def mip_003_kyle_lambda_126d(close, volume):
    """Rolling 126-day Kyle lambda: half-year price-impact elasticity."""
    return _kyle_lambda_fast(close, volume, _TD_HALF)


def mip_004_kyle_lambda_252d(close, volume):
    """Rolling 252-day Kyle lambda: annual price-impact sensitivity baseline."""
    return _kyle_lambda_fast(close, volume, _TD_YEAR)


def mip_005_kyle_lambda_5d(close, volume):
    """Rolling 5-day Kyle lambda: very short-run price-impact sensitivity."""
    return _kyle_lambda_fast(close, volume, _TD_WEEK)


def mip_006_kyle_lambda_21d_zscore_63d(close, volume):
    """Z-score of 21d Kyle lambda within trailing 63-day window."""
    return _zscore(_kyle_lambda_fast(close, volume, _TD_MON), _TD_QTR)


def mip_007_kyle_lambda_21d_zscore_252d(close, volume):
    """Z-score of 21d Kyle lambda within trailing 252-day window."""
    return _zscore(_kyle_lambda_fast(close, volume, _TD_MON), _TD_YEAR)


def mip_008_kyle_lambda_21d_pct_rank_252d(close, volume):
    """Percentile rank of 21d Kyle lambda within trailing 252 days."""
    return _pct_rank(_kyle_lambda_fast(close, volume, _TD_MON), _TD_YEAR)


def mip_009_kyle_lambda_21d_spike_ratio_252d(close, volume):
    """21d Kyle lambda divided by its 252d rolling mean (spike ratio)."""
    kl = _kyle_lambda_fast(close, volume, _TD_MON)
    return _safe_div(kl, _rolling_mean(kl, _TD_YEAR))


def mip_010_kyle_lambda_21d_vs_63d_ratio(close, volume):
    """Ratio of 21d Kyle lambda to 63d Kyle lambda (short vs medium-run impact)."""
    return _safe_div(
        _kyle_lambda_fast(close, volume, _TD_MON),
        _kyle_lambda_fast(close, volume, _TD_QTR)
    )


def mip_011_kyle_lambda_21d_roll_max_63d(close, volume):
    """63-day rolling max of 21d Kyle lambda (worst impact sensitivity in quarter)."""
    return _rolling_max(_kyle_lambda_fast(close, volume, _TD_MON), _TD_QTR)


def mip_012_kyle_lambda_21d_ewm(close, volume):
    """EWM span=21 of 21d Kyle lambda (smoothed impact sensitivity)."""
    return _ewm_mean(_kyle_lambda_fast(close, volume, _TD_MON), _TD_MON)


def mip_013_kyle_lambda_above_mean_streak_63d(close, volume):
    """Consecutive days where 21d Kyle lambda exceeds its 63-day mean."""
    kl   = _kyle_lambda_fast(close, volume, _TD_MON)
    mu   = _rolling_mean(kl, _TD_QTR)
    cond = kl > mu
    return _consec_streak(cond)


def mip_014_kyle_lambda_21d_spike_gt2std_63d(close, volume):
    """Flag: 21d Kyle lambda > 2 std above its 63-day mean (impact spike)."""
    kl  = _kyle_lambda_fast(close, volume, _TD_MON)
    mu  = _rolling_mean(kl, _TD_QTR)
    sig = _rolling_std(kl, _TD_QTR)
    return (kl > mu + 2.0 * sig).astype(float)


def mip_015_kyle_lambda_63d_pct_rank_252d(close, volume):
    """Percentile rank of 63d Kyle lambda within trailing 252 days."""
    return _pct_rank(_kyle_lambda_fast(close, volume, _TD_QTR), _TD_YEAR)


# --- Group B (016-030): Amivest ratio (dollar volume / |return|) ---

def mip_016_amivest_daily(close, volume):
    """Daily Amivest liquidity ratio: dollar_volume / |return| (depth proxy)."""
    return _amivest(close, volume)


def mip_017_amivest_log(close, volume):
    """Log of daily Amivest ratio (compresses right tail)."""
    return _log_safe(_amivest(close, volume))


def mip_018_amivest_roll_mean_5d(close, volume):
    """5-day rolling mean of Amivest ratio (short-run liquidity depth)."""
    return _rolling_mean(_amivest(close, volume), _TD_WEEK)


def mip_019_amivest_roll_mean_21d(close, volume):
    """21-day rolling mean of Amivest ratio (monthly liquidity depth)."""
    return _rolling_mean(_amivest(close, volume), _TD_MON)


def mip_020_amivest_roll_mean_63d(close, volume):
    """63-day rolling mean of Amivest ratio (quarterly liquidity depth)."""
    return _rolling_mean(_amivest(close, volume), _TD_QTR)


def mip_021_amivest_roll_mean_252d(close, volume):
    """252-day rolling mean of Amivest ratio (annual liquidity depth baseline)."""
    return _rolling_mean(_amivest(close, volume), _TD_YEAR)


def mip_022_amivest_zscore_21d(close, volume):
    """Z-score of daily Amivest ratio within trailing 21-day window."""
    return _zscore(_amivest(close, volume), _TD_MON)


def mip_023_amivest_zscore_63d(close, volume):
    """Z-score of daily Amivest ratio within trailing 63-day window."""
    return _zscore(_amivest(close, volume), _TD_QTR)


def mip_024_amivest_zscore_252d(close, volume):
    """Z-score of daily Amivest ratio within trailing 252-day window."""
    return _zscore(_amivest(close, volume), _TD_YEAR)


def mip_025_amivest_pct_rank_21d(close, volume):
    """Percentile rank of daily Amivest ratio within trailing 21 days."""
    return _pct_rank(_amivest(close, volume), _TD_MON)


def mip_026_amivest_pct_rank_63d(close, volume):
    """Percentile rank of daily Amivest ratio within trailing 63 days."""
    return _pct_rank(_amivest(close, volume), _TD_QTR)


def mip_027_amivest_pct_rank_252d(close, volume):
    """Percentile rank of daily Amivest ratio within trailing 252 days."""
    return _pct_rank(_amivest(close, volume), _TD_YEAR)


def mip_028_amivest_collapse_flag_21d(close, volume):
    """Flag: Amivest ratio below 10th percentile of trailing 21d (liquidity collapse)."""
    av  = _amivest(close, volume)
    p10 = av.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.10)
    return (av < p10).astype(float)


def mip_029_amivest_collapse_flag_252d(close, volume):
    """Flag: Amivest ratio below 5th percentile of trailing 252d (annual depth collapse)."""
    av = _amivest(close, volume)
    p5 = av.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.05)
    return (av < p5).astype(float)


def mip_030_amivest_below_mean_streak_63d(close, volume):
    """Consecutive days where Amivest is below its 63-day rolling mean."""
    av   = _amivest(close, volume)
    mu   = _rolling_mean(av, _TD_QTR)
    cond = av < mu
    return _consec_streak(cond)


# --- Group C (031-045): Return-per-dollar-volume and sqrt-impact measures ---

def mip_031_ret_per_dolvol_daily(close, volume):
    """Daily return-per-dollar-volume: |return| / dollar_volume."""
    return _ret_per_dolvol(close, volume)


def mip_032_ret_per_dolvol_roll_mean_5d(close, volume):
    """5-day rolling mean of return-per-dollar-volume."""
    return _rolling_mean(_ret_per_dolvol(close, volume), _TD_WEEK)


def mip_033_ret_per_dolvol_roll_mean_21d(close, volume):
    """21-day rolling mean of return-per-dollar-volume."""
    return _rolling_mean(_ret_per_dolvol(close, volume), _TD_MON)


def mip_034_ret_per_dolvol_roll_mean_63d(close, volume):
    """63-day rolling mean of return-per-dollar-volume."""
    return _rolling_mean(_ret_per_dolvol(close, volume), _TD_QTR)


def mip_035_ret_per_dolvol_zscore_63d(close, volume):
    """Z-score of return-per-dollar-volume within trailing 63 days."""
    return _zscore(_ret_per_dolvol(close, volume), _TD_QTR)


def mip_036_ret_per_dolvol_zscore_252d(close, volume):
    """Z-score of return-per-dollar-volume within trailing 252 days."""
    return _zscore(_ret_per_dolvol(close, volume), _TD_YEAR)


def mip_037_ret_per_dolvol_pct_rank_252d(close, volume):
    """Percentile rank of return-per-dollar-volume within trailing 252 days."""
    return _pct_rank(_ret_per_dolvol(close, volume), _TD_YEAR)


def mip_038_ret_per_dolvol_spike_ratio_21d(close, volume):
    """Return-per-dolvol divided by its 21-day mean (relative spike magnitude)."""
    r = _ret_per_dolvol(close, volume)
    return _safe_div(r, _rolling_mean(r, _TD_MON))


def mip_039_ret_per_dolvol_spike_ratio_63d(close, volume):
    """Return-per-dolvol divided by its 63-day mean (quarterly spike ratio)."""
    r = _ret_per_dolvol(close, volume)
    return _safe_div(r, _rolling_mean(r, _TD_QTR))


def mip_040_ret_per_dolvol_spike_ratio_252d(close, volume):
    """Return-per-dolvol divided by its 252-day mean (annual spike ratio)."""
    r = _ret_per_dolvol(close, volume)
    return _safe_div(r, _rolling_mean(r, _TD_YEAR))


def mip_041_sqrt_impact_daily(close, volume):
    """Daily sqrt-impact: |return| / sqrt(dollar_volume) — square-root model proxy."""
    return _sqrt_impact(close, volume)


def mip_042_sqrt_impact_roll_mean_21d(close, volume):
    """21-day rolling mean of sqrt-impact proxy."""
    return _rolling_mean(_sqrt_impact(close, volume), _TD_MON)


def mip_043_sqrt_impact_roll_mean_63d(close, volume):
    """63-day rolling mean of sqrt-impact proxy."""
    return _rolling_mean(_sqrt_impact(close, volume), _TD_QTR)


def mip_044_sqrt_impact_zscore_63d(close, volume):
    """Z-score of sqrt-impact proxy within trailing 63 days."""
    return _zscore(_sqrt_impact(close, volume), _TD_QTR)


def mip_045_sqrt_impact_pct_rank_252d(close, volume):
    """Percentile rank of sqrt-impact proxy within trailing 252 days."""
    return _pct_rank(_sqrt_impact(close, volume), _TD_YEAR)


# --- Group D (046-055): Range-per-dollar-volume (intraday impact width) ---

def mip_046_range_per_dolvol_daily(close, high, low, volume):
    """Daily intraday range per dollar volume: (H-L)/close / dollar_volume."""
    return _range_per_dolvol(high, low, close, volume)


def mip_047_range_per_dolvol_roll_mean_5d(close, high, low, volume):
    """5-day rolling mean of range-per-dollar-volume."""
    return _rolling_mean(_range_per_dolvol(high, low, close, volume), _TD_WEEK)


def mip_048_range_per_dolvol_roll_mean_21d(close, high, low, volume):
    """21-day rolling mean of range-per-dollar-volume."""
    return _rolling_mean(_range_per_dolvol(high, low, close, volume), _TD_MON)


def mip_049_range_per_dolvol_roll_mean_63d(close, high, low, volume):
    """63-day rolling mean of range-per-dollar-volume."""
    return _rolling_mean(_range_per_dolvol(high, low, close, volume), _TD_QTR)


def mip_050_range_per_dolvol_zscore_63d(close, high, low, volume):
    """Z-score of range-per-dollar-volume within trailing 63 days."""
    return _zscore(_range_per_dolvol(high, low, close, volume), _TD_QTR)


def mip_051_range_per_dolvol_zscore_252d(close, high, low, volume):
    """Z-score of range-per-dollar-volume within trailing 252 days."""
    return _zscore(_range_per_dolvol(high, low, close, volume), _TD_YEAR)


def mip_052_range_per_dolvol_pct_rank_252d(close, high, low, volume):
    """Percentile rank of range-per-dollar-volume within trailing 252 days."""
    return _pct_rank(_range_per_dolvol(high, low, close, volume), _TD_YEAR)


def mip_053_range_per_dolvol_spike_ratio_63d(close, high, low, volume):
    """Range-per-dolvol divided by its 63-day mean (quarterly spike ratio)."""
    r = _range_per_dolvol(high, low, close, volume)
    return _safe_div(r, _rolling_mean(r, _TD_QTR))


def mip_054_range_per_dolvol_roll_max_21d(close, high, low, volume):
    """21-day rolling max of range-per-dollar-volume (worst intraday impact in month)."""
    return _rolling_max(_range_per_dolvol(high, low, close, volume), _TD_MON)


def mip_055_range_per_dolvol_above_mean_streak(close, high, low, volume):
    """Consecutive days where range-per-dolvol exceeds its 63-day rolling mean."""
    r    = _range_per_dolvol(high, low, close, volume)
    mu   = _rolling_mean(r, _TD_QTR)
    cond = r > mu
    return _consec_streak(cond)


# --- Group E (056-065): Up-day vs down-day impact asymmetry ---

def mip_056_ret_per_dolvol_down_mean_21d(close, volume):
    """Mean return-per-dolvol on down-price days over trailing 21 days."""
    r      = _ret_per_dolvol(close, volume)
    ret    = close.pct_change(1)
    masked = r.where(ret < 0, np.nan)
    return masked.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def mip_057_ret_per_dolvol_up_mean_21d(close, volume):
    """Mean return-per-dolvol on up-price days over trailing 21 days."""
    r      = _ret_per_dolvol(close, volume)
    ret    = close.pct_change(1)
    masked = r.where(ret > 0, np.nan)
    return masked.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def mip_058_impact_asymmetry_down_vs_up_21d(close, volume):
    """Ratio of down-day to up-day mean impact (21d): >1 means crashes move price more."""
    return _safe_div(
        mip_056_ret_per_dolvol_down_mean_21d(close, volume),
        mip_057_ret_per_dolvol_up_mean_21d(close, volume)
    )


def mip_059_impact_asymmetry_down_vs_up_63d(close, volume):
    """Ratio of down-day to up-day mean impact (63d): quarterly asymmetry."""
    r   = _ret_per_dolvol(close, volume)
    ret = close.pct_change(1)
    down_mean = r.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    up_mean   = r.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return _safe_div(down_mean, up_mean)


def mip_060_impact_asymmetry_zscore_63d(close, volume):
    """Z-score of 21d impact asymmetry ratio within trailing 63 days."""
    return _zscore(mip_058_impact_asymmetry_down_vs_up_21d(close, volume), _TD_QTR)


def mip_061_impact_asymmetry_pct_rank_252d(close, volume):
    """Percentile rank of 21d impact asymmetry ratio within trailing 252 days."""
    return _pct_rank(mip_058_impact_asymmetry_down_vs_up_21d(close, volume), _TD_YEAR)


def mip_062_down_day_impact_zscore_63d(close, volume):
    """Z-score of down-day mean impact within trailing 63 days."""
    return _zscore(mip_056_ret_per_dolvol_down_mean_21d(close, volume), _TD_QTR)


def mip_063_up_day_impact_zscore_63d(close, volume):
    """Z-score of up-day mean impact within trailing 63 days."""
    return _zscore(mip_057_ret_per_dolvol_up_mean_21d(close, volume), _TD_QTR)


def mip_064_impact_asym_spike_gt2std_252d(close, volume):
    """Flag: 21d impact asymmetry > 2 std above 252-day mean (extreme asymmetry spike)."""
    asym = mip_058_impact_asymmetry_down_vs_up_21d(close, volume)
    mu   = _rolling_mean(asym, _TD_YEAR)
    sig  = _rolling_std(asym, _TD_YEAR)
    return (asym > mu + 2.0 * sig).astype(float)


def mip_065_impact_asym_above_mean_streak_63d(close, volume):
    """Consecutive days where 21d impact asymmetry ratio exceeds its 63-day mean."""
    asym = mip_058_impact_asymmetry_down_vs_up_21d(close, volume)
    mu   = _rolling_mean(asym, _TD_QTR)
    cond = asym > mu
    return _consec_streak(cond)


# --- Group F (066-075): Rolling correlation of |return| with volume ---

def mip_066_abs_ret_vol_corr_21d(close, volume):
    """Rolling 21d correlation of |return| with volume (impact-volume linkage)."""
    ret = close.pct_change(1).abs()
    return ret.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).corr(volume)


def mip_067_abs_ret_vol_corr_63d(close, volume):
    """Rolling 63d correlation of |return| with volume."""
    ret = close.pct_change(1).abs()
    return ret.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).corr(volume)


def mip_068_abs_ret_vol_corr_126d(close, volume):
    """Rolling 126d correlation of |return| with volume."""
    ret = close.pct_change(1).abs()
    return ret.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).corr(volume)


def mip_069_abs_ret_vol_corr_252d(close, volume):
    """Rolling 252d correlation of |return| with volume."""
    ret = close.pct_change(1).abs()
    return ret.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).corr(volume)


def mip_070_abs_ret_vol_corr_21d_zscore_63d(close, volume):
    """Z-score of 21d |ret|-volume correlation within trailing 63-day window."""
    return _zscore(mip_066_abs_ret_vol_corr_21d(close, volume), _TD_QTR)


def mip_071_abs_ret_vol_corr_21d_pct_rank_252d(close, volume):
    """Percentile rank of 21d |ret|-volume correlation within trailing 252 days."""
    return _pct_rank(mip_066_abs_ret_vol_corr_21d(close, volume), _TD_YEAR)


def mip_072_abs_ret_logvol_corr_63d(close, volume):
    """Rolling 63d correlation of |return| with log(volume)."""
    ret    = close.pct_change(1).abs()
    logvol = _log_safe(volume)
    return ret.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).corr(logvol)


def mip_073_ret_vol_corr_high_impact_flag(close, volume):
    """Flag: 21d |ret|-volume correlation above 0.5 (strong impact-volume link)."""
    return (mip_066_abs_ret_vol_corr_21d(close, volume) > 0.5).astype(float)


def mip_074_abs_ret_vol_corr_21d_spike_ratio(close, volume):
    """21d |ret|-volume correlation divided by its 252d mean (relative elevation)."""
    c = mip_066_abs_ret_vol_corr_21d(close, volume)
    return _safe_div(c, _rolling_mean(c, _TD_YEAR))


def mip_075_abs_ret_vol_corr_above_mean_streak(close, volume):
    """Consecutive days where 21d |ret|-volume corr exceeds its 63-day mean."""
    c    = mip_066_abs_ret_vol_corr_21d(close, volume)
    mu   = _rolling_mean(c, _TD_QTR)
    cond = c > mu
    return _consec_streak(cond)


# -- Registry ------------------------------------------------------------------

MARKET_IMPACT_PROXY_REGISTRY_001_075 = {
    "mip_001_kyle_lambda_21d": {"inputs": ["close", "volume"], "func": mip_001_kyle_lambda_21d},
    "mip_002_kyle_lambda_63d": {"inputs": ["close", "volume"], "func": mip_002_kyle_lambda_63d},
    "mip_003_kyle_lambda_126d": {"inputs": ["close", "volume"], "func": mip_003_kyle_lambda_126d},
    "mip_004_kyle_lambda_252d": {"inputs": ["close", "volume"], "func": mip_004_kyle_lambda_252d},
    "mip_005_kyle_lambda_5d": {"inputs": ["close", "volume"], "func": mip_005_kyle_lambda_5d},
    "mip_006_kyle_lambda_21d_zscore_63d": {"inputs": ["close", "volume"], "func": mip_006_kyle_lambda_21d_zscore_63d},
    "mip_007_kyle_lambda_21d_zscore_252d": {"inputs": ["close", "volume"], "func": mip_007_kyle_lambda_21d_zscore_252d},
    "mip_008_kyle_lambda_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_008_kyle_lambda_21d_pct_rank_252d},
    "mip_009_kyle_lambda_21d_spike_ratio_252d": {"inputs": ["close", "volume"], "func": mip_009_kyle_lambda_21d_spike_ratio_252d},
    "mip_010_kyle_lambda_21d_vs_63d_ratio": {"inputs": ["close", "volume"], "func": mip_010_kyle_lambda_21d_vs_63d_ratio},
    "mip_011_kyle_lambda_21d_roll_max_63d": {"inputs": ["close", "volume"], "func": mip_011_kyle_lambda_21d_roll_max_63d},
    "mip_012_kyle_lambda_21d_ewm": {"inputs": ["close", "volume"], "func": mip_012_kyle_lambda_21d_ewm},
    "mip_013_kyle_lambda_above_mean_streak_63d": {"inputs": ["close", "volume"], "func": mip_013_kyle_lambda_above_mean_streak_63d},
    "mip_014_kyle_lambda_21d_spike_gt2std_63d": {"inputs": ["close", "volume"], "func": mip_014_kyle_lambda_21d_spike_gt2std_63d},
    "mip_015_kyle_lambda_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_015_kyle_lambda_63d_pct_rank_252d},
    "mip_016_amivest_daily": {"inputs": ["close", "volume"], "func": mip_016_amivest_daily},
    "mip_017_amivest_log": {"inputs": ["close", "volume"], "func": mip_017_amivest_log},
    "mip_018_amivest_roll_mean_5d": {"inputs": ["close", "volume"], "func": mip_018_amivest_roll_mean_5d},
    "mip_019_amivest_roll_mean_21d": {"inputs": ["close", "volume"], "func": mip_019_amivest_roll_mean_21d},
    "mip_020_amivest_roll_mean_63d": {"inputs": ["close", "volume"], "func": mip_020_amivest_roll_mean_63d},
    "mip_021_amivest_roll_mean_252d": {"inputs": ["close", "volume"], "func": mip_021_amivest_roll_mean_252d},
    "mip_022_amivest_zscore_21d": {"inputs": ["close", "volume"], "func": mip_022_amivest_zscore_21d},
    "mip_023_amivest_zscore_63d": {"inputs": ["close", "volume"], "func": mip_023_amivest_zscore_63d},
    "mip_024_amivest_zscore_252d": {"inputs": ["close", "volume"], "func": mip_024_amivest_zscore_252d},
    "mip_025_amivest_pct_rank_21d": {"inputs": ["close", "volume"], "func": mip_025_amivest_pct_rank_21d},
    "mip_026_amivest_pct_rank_63d": {"inputs": ["close", "volume"], "func": mip_026_amivest_pct_rank_63d},
    "mip_027_amivest_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_027_amivest_pct_rank_252d},
    "mip_028_amivest_collapse_flag_21d": {"inputs": ["close", "volume"], "func": mip_028_amivest_collapse_flag_21d},
    "mip_029_amivest_collapse_flag_252d": {"inputs": ["close", "volume"], "func": mip_029_amivest_collapse_flag_252d},
    "mip_030_amivest_below_mean_streak_63d": {"inputs": ["close", "volume"], "func": mip_030_amivest_below_mean_streak_63d},
    "mip_031_ret_per_dolvol_daily": {"inputs": ["close", "volume"], "func": mip_031_ret_per_dolvol_daily},
    "mip_032_ret_per_dolvol_roll_mean_5d": {"inputs": ["close", "volume"], "func": mip_032_ret_per_dolvol_roll_mean_5d},
    "mip_033_ret_per_dolvol_roll_mean_21d": {"inputs": ["close", "volume"], "func": mip_033_ret_per_dolvol_roll_mean_21d},
    "mip_034_ret_per_dolvol_roll_mean_63d": {"inputs": ["close", "volume"], "func": mip_034_ret_per_dolvol_roll_mean_63d},
    "mip_035_ret_per_dolvol_zscore_63d": {"inputs": ["close", "volume"], "func": mip_035_ret_per_dolvol_zscore_63d},
    "mip_036_ret_per_dolvol_zscore_252d": {"inputs": ["close", "volume"], "func": mip_036_ret_per_dolvol_zscore_252d},
    "mip_037_ret_per_dolvol_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_037_ret_per_dolvol_pct_rank_252d},
    "mip_038_ret_per_dolvol_spike_ratio_21d": {"inputs": ["close", "volume"], "func": mip_038_ret_per_dolvol_spike_ratio_21d},
    "mip_039_ret_per_dolvol_spike_ratio_63d": {"inputs": ["close", "volume"], "func": mip_039_ret_per_dolvol_spike_ratio_63d},
    "mip_040_ret_per_dolvol_spike_ratio_252d": {"inputs": ["close", "volume"], "func": mip_040_ret_per_dolvol_spike_ratio_252d},
    "mip_041_sqrt_impact_daily": {"inputs": ["close", "volume"], "func": mip_041_sqrt_impact_daily},
    "mip_042_sqrt_impact_roll_mean_21d": {"inputs": ["close", "volume"], "func": mip_042_sqrt_impact_roll_mean_21d},
    "mip_043_sqrt_impact_roll_mean_63d": {"inputs": ["close", "volume"], "func": mip_043_sqrt_impact_roll_mean_63d},
    "mip_044_sqrt_impact_zscore_63d": {"inputs": ["close", "volume"], "func": mip_044_sqrt_impact_zscore_63d},
    "mip_045_sqrt_impact_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_045_sqrt_impact_pct_rank_252d},
    "mip_046_range_per_dolvol_daily": {"inputs": ["close", "high", "low", "volume"], "func": mip_046_range_per_dolvol_daily},
    "mip_047_range_per_dolvol_roll_mean_5d": {"inputs": ["close", "high", "low", "volume"], "func": mip_047_range_per_dolvol_roll_mean_5d},
    "mip_048_range_per_dolvol_roll_mean_21d": {"inputs": ["close", "high", "low", "volume"], "func": mip_048_range_per_dolvol_roll_mean_21d},
    "mip_049_range_per_dolvol_roll_mean_63d": {"inputs": ["close", "high", "low", "volume"], "func": mip_049_range_per_dolvol_roll_mean_63d},
    "mip_050_range_per_dolvol_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mip_050_range_per_dolvol_zscore_63d},
    "mip_051_range_per_dolvol_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mip_051_range_per_dolvol_zscore_252d},
    "mip_052_range_per_dolvol_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mip_052_range_per_dolvol_pct_rank_252d},
    "mip_053_range_per_dolvol_spike_ratio_63d": {"inputs": ["close", "high", "low", "volume"], "func": mip_053_range_per_dolvol_spike_ratio_63d},
    "mip_054_range_per_dolvol_roll_max_21d": {"inputs": ["close", "high", "low", "volume"], "func": mip_054_range_per_dolvol_roll_max_21d},
    "mip_055_range_per_dolvol_above_mean_streak": {"inputs": ["close", "high", "low", "volume"], "func": mip_055_range_per_dolvol_above_mean_streak},
    "mip_056_ret_per_dolvol_down_mean_21d": {"inputs": ["close", "volume"], "func": mip_056_ret_per_dolvol_down_mean_21d},
    "mip_057_ret_per_dolvol_up_mean_21d": {"inputs": ["close", "volume"], "func": mip_057_ret_per_dolvol_up_mean_21d},
    "mip_058_impact_asymmetry_down_vs_up_21d": {"inputs": ["close", "volume"], "func": mip_058_impact_asymmetry_down_vs_up_21d},
    "mip_059_impact_asymmetry_down_vs_up_63d": {"inputs": ["close", "volume"], "func": mip_059_impact_asymmetry_down_vs_up_63d},
    "mip_060_impact_asymmetry_zscore_63d": {"inputs": ["close", "volume"], "func": mip_060_impact_asymmetry_zscore_63d},
    "mip_061_impact_asymmetry_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_061_impact_asymmetry_pct_rank_252d},
    "mip_062_down_day_impact_zscore_63d": {"inputs": ["close", "volume"], "func": mip_062_down_day_impact_zscore_63d},
    "mip_063_up_day_impact_zscore_63d": {"inputs": ["close", "volume"], "func": mip_063_up_day_impact_zscore_63d},
    "mip_064_impact_asym_spike_gt2std_252d": {"inputs": ["close", "volume"], "func": mip_064_impact_asym_spike_gt2std_252d},
    "mip_065_impact_asym_above_mean_streak_63d": {"inputs": ["close", "volume"], "func": mip_065_impact_asym_above_mean_streak_63d},
    "mip_066_abs_ret_vol_corr_21d": {"inputs": ["close", "volume"], "func": mip_066_abs_ret_vol_corr_21d},
    "mip_067_abs_ret_vol_corr_63d": {"inputs": ["close", "volume"], "func": mip_067_abs_ret_vol_corr_63d},
    "mip_068_abs_ret_vol_corr_126d": {"inputs": ["close", "volume"], "func": mip_068_abs_ret_vol_corr_126d},
    "mip_069_abs_ret_vol_corr_252d": {"inputs": ["close", "volume"], "func": mip_069_abs_ret_vol_corr_252d},
    "mip_070_abs_ret_vol_corr_21d_zscore_63d": {"inputs": ["close", "volume"], "func": mip_070_abs_ret_vol_corr_21d_zscore_63d},
    "mip_071_abs_ret_vol_corr_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": mip_071_abs_ret_vol_corr_21d_pct_rank_252d},
    "mip_072_abs_ret_logvol_corr_63d": {"inputs": ["close", "volume"], "func": mip_072_abs_ret_logvol_corr_63d},
    "mip_073_ret_vol_corr_high_impact_flag": {"inputs": ["close", "volume"], "func": mip_073_ret_vol_corr_high_impact_flag},
    "mip_074_abs_ret_vol_corr_21d_spike_ratio": {"inputs": ["close", "volume"], "func": mip_074_abs_ret_vol_corr_21d_spike_ratio},
    "mip_075_abs_ret_vol_corr_above_mean_streak": {"inputs": ["close", "volume"], "func": mip_075_abs_ret_vol_corr_above_mean_streak},
}