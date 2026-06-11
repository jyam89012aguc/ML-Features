"""
53_liquidity_collapse — Base Features 001-075
Domain: illiquidity spikes — Amihud illiquidity ratio, bid-ask spread estimators
  (Corwin-Schultz, Roll), illiquidity streaks, z-scores, percentile ranks
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — liquidity drying up / price-impact spikes
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
    """Element-wise division; zero denominator becomes NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


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
    mu  = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


def _pct_rank(s: pd.Series, w: int) -> pd.Series:
    """Rolling percentile rank of s within trailing w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _amihud(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud illiquidity: |ret| / dollar_volume (NaN on zero vol days)."""
    ret      = close.pct_change(1).abs()
    dolvol   = close * volume
    return _safe_div(ret, dolvol)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c      = cond.astype(int)
    group  = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
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


def _roll_spread(close: pd.Series) -> pd.Series:
    """Roll (1984) effective spread proxy: 2*sqrt(max(-cov(dP_t, dP_{t-1}), 0))."""
    dp   = close.diff(1)
    cov  = dp.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).cov(dp.shift(1))
    return 2.0 * np.sqrt((-cov).clip(lower=0.0))


def _cs_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corwin-Schultz (2012) high-low bid-ask spread estimator (daily version).

    beta  = (ln H/L)^2 + (ln H_{t-1}/L_{t-1})^2
    gamma = (ln max(H,H_{t-1}) / min(L,L_{t-1}))^2
    alpha = (sqrt(2*beta) - sqrt(beta)) / (3 - 2*sqrt(2)) - sqrt(gamma/(3-2*sqrt(2)))
    spread = 2*(exp(alpha)-1) / (1+exp(alpha)), floored at 0.
    """
    ln_hl   = _log_safe(high) - _log_safe(low)
    beta    = ln_hl ** 2 + (ln_hl.shift(1)) ** 2
    h2      = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2      = pd.concat([low,  low.shift(1)],  axis=1).min(axis=1)
    gamma   = (_log_safe(h2) - _log_safe(l2)) ** 2
    k       = 3.0 - 2.0 * np.sqrt(2.0)
    alpha   = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k - np.sqrt(gamma / k)
    spread  = (2.0 * (np.exp(alpha) - 1.0)) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0.0)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw Amihud illiquidity ratio ---

def lqc_001_amihud_daily(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud illiquidity ratio: |return| / dollar_volume."""
    return _amihud(close, volume)


def lqc_002_amihud_scaled_1e6(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud ratio scaled by 1e6 for readability."""
    return _amihud(close, volume) * 1e6


def lqc_003_amihud_log(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of (1 + Amihud*1e6) — compresses heavy right tail."""
    return np.log1p(_amihud(close, volume) * 1e6)


def lqc_004_amihud_roll_mean_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rolling mean of daily Amihud ratio (weekly illiquidity level)."""
    return _rolling_mean(_amihud(close, volume), _TD_WEEK)


def lqc_005_amihud_roll_mean_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling mean of daily Amihud ratio (monthly illiquidity level)."""
    return _rolling_mean(_amihud(close, volume), _TD_MON)


def lqc_006_amihud_roll_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling mean of daily Amihud ratio (quarterly illiquidity baseline)."""
    return _rolling_mean(_amihud(close, volume), _TD_QTR)


def lqc_007_amihud_roll_mean_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day rolling mean of daily Amihud ratio (half-year baseline)."""
    return _rolling_mean(_amihud(close, volume), _TD_HALF)


def lqc_008_amihud_roll_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day rolling mean of daily Amihud ratio (annual baseline)."""
    return _rolling_mean(_amihud(close, volume), _TD_YEAR)


def lqc_009_amihud_roll_max_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling maximum Amihud ratio (worst illiquidity spike in month)."""
    return _rolling_max(_amihud(close, volume), _TD_MON)


def lqc_010_amihud_roll_max_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling maximum Amihud ratio (worst illiquidity spike in quarter)."""
    return _rolling_max(_amihud(close, volume), _TD_QTR)


# --- Group B (011-020): Amihud z-scores and percentile ranks ---

def lqc_011_amihud_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily Amihud ratio within trailing 21-day window."""
    return _zscore(_amihud(close, volume), _TD_MON)


def lqc_012_amihud_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily Amihud ratio within trailing 63-day window."""
    return _zscore(_amihud(close, volume), _TD_QTR)


def lqc_013_amihud_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily Amihud ratio within trailing 126-day window."""
    return _zscore(_amihud(close, volume), _TD_HALF)


def lqc_014_amihud_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily Amihud ratio within trailing 252-day window."""
    return _zscore(_amihud(close, volume), _TD_YEAR)


def lqc_015_amihud_pct_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of daily Amihud within trailing 21 days."""
    return _pct_rank(_amihud(close, volume), _TD_MON)


def lqc_016_amihud_pct_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of daily Amihud within trailing 63 days."""
    return _pct_rank(_amihud(close, volume), _TD_QTR)


def lqc_017_amihud_pct_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of daily Amihud within trailing 126 days."""
    return _pct_rank(_amihud(close, volume), _TD_HALF)


def lqc_018_amihud_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of daily Amihud within trailing 252 days."""
    return _pct_rank(_amihud(close, volume), _TD_YEAR)


def lqc_019_amihud_expanding_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of daily Amihud ratio."""
    return _amihud(close, volume).expanding(min_periods=5).rank(pct=True)


def lqc_020_amihud_ewm_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM-based z-score of Amihud ratio (span=21)."""
    ami  = _amihud(close, volume)
    mu   = _ewm_mean(ami, _TD_MON)
    var  = ami.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).var()
    return _safe_div(ami - mu, np.sqrt(var.clip(lower=0.0)))


# --- Group C (021-030): Amihud spike detection ---

def lqc_021_amihud_spike_gt2std_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: daily Amihud > 2 std above 21-day mean (illiquidity spike)."""
    ami = _amihud(close, volume)
    mu  = _rolling_mean(ami, _TD_MON)
    sig = _rolling_std(ami, _TD_MON)
    return (ami > mu + 2.0 * sig).astype(float)


def lqc_022_amihud_spike_gt3std_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: daily Amihud > 3 std above 63-day mean (extreme illiquidity spike)."""
    ami = _amihud(close, volume)
    mu  = _rolling_mean(ami, _TD_QTR)
    sig = _rolling_std(ami, _TD_QTR)
    return (ami > mu + 3.0 * sig).astype(float)


def lqc_023_amihud_spike_gt2std_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: daily Amihud > 2 std above 252-day mean (annual-baseline spike)."""
    ami = _amihud(close, volume)
    mu  = _rolling_mean(ami, _TD_YEAR)
    sig = _rolling_std(ami, _TD_YEAR)
    return (ami > mu + 2.0 * sig).astype(float)


def lqc_024_amihud_spike_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud divided by its 21-day rolling mean (relative spike magnitude)."""
    ami = _amihud(close, volume)
    return _safe_div(ami, _rolling_mean(ami, _TD_MON))


def lqc_025_amihud_spike_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud divided by its 63-day rolling mean."""
    ami = _amihud(close, volume)
    return _safe_div(ami, _rolling_mean(ami, _TD_QTR))


def lqc_026_amihud_spike_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily Amihud divided by its 252-day rolling mean."""
    ami = _amihud(close, volume)
    return _safe_div(ami, _rolling_mean(ami, _TD_YEAR))


def lqc_027_amihud_spike_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in last 21 where Amihud exceeded its 63-day mean by 2 std."""
    ami   = _amihud(close, volume)
    mu    = _rolling_mean(ami, _TD_QTR)
    sig   = _rolling_std(ami, _TD_QTR)
    spike = (ami > mu + 2.0 * sig).astype(float)
    return _rolling_sum(spike, _TD_MON)


def lqc_028_amihud_spike_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in last 63 where Amihud exceeded its 252-day mean by 2 std."""
    ami   = _amihud(close, volume)
    mu    = _rolling_mean(ami, _TD_YEAR)
    sig   = _rolling_std(ami, _TD_YEAR)
    spike = (ami > mu + 2.0 * sig).astype(float)
    return _rolling_sum(spike, _TD_QTR)


def lqc_029_amihud_above_90pct_21d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: today's Amihud above 90th percentile of trailing 21-day distribution."""
    ami = _amihud(close, volume)
    p90 = ami.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.90)
    return (ami > p90).astype(float)


def lqc_030_amihud_above_95pct_252d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: today's Amihud above 95th percentile of trailing 252-day distribution."""
    ami = _amihud(close, volume)
    p95 = ami.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.95)
    return (ami > p95).astype(float)


# --- Group D (031-040): Amihud vs price — illiquidity rising while price falls ---

def lqc_031_amihud_rising_price_falling_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: Amihud above 21d mean AND close below prior close (illiq + price drop)."""
    ami   = _amihud(close, volume)
    mu    = _rolling_mean(ami, _TD_MON)
    return ((ami > mu) & (close < close.shift(1))).astype(float)


def lqc_032_amihud_5d_chg_vs_ret(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day change in Amihud minus 5-day log-return (illiquidity surge vs price drop)."""
    ami = _amihud(close, volume)
    ret = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    return ami.diff(_TD_WEEK) - ret


def lqc_033_amihud_21d_chg_vs_ret(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in Amihud minus 21-day log-return."""
    ami = _amihud(close, volume)
    ret = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return ami.diff(_TD_MON) - ret


def lqc_034_amihud_diverge_from_price_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (Amihud zscore + return zscore): illiq up + price down = extreme."""
    ami    = _amihud(close, volume)
    az     = _zscore(ami, _TD_QTR)
    ret    = close.pct_change(1)
    rz     = _zscore(ret, _TD_QTR)
    signal = az - rz
    return _zscore(signal, _TD_QTR)


def lqc_035_amihud_price_fall_consec(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days of simultaneous Amihud above 63d mean AND price decline."""
    ami  = _amihud(close, volume)
    mu   = _rolling_mean(ami, _TD_QTR)
    cond = (ami > mu) & (close < close.shift(1))
    return _consec_streak(cond)


def lqc_036_amihud_corr_neg_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21d correlation of Amihud with negative daily returns (liquidity-return link)."""
    ami = _amihud(close, volume)
    ret = close.pct_change(1)
    return ami.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).corr(ret)


def lqc_037_amihud_corr_neg_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d correlation of Amihud with daily returns."""
    ami = _amihud(close, volume)
    ret = close.pct_change(1)
    return ami.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).corr(ret)


def lqc_038_amihud_down_day_mean_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean Amihud on down-price days over trailing 21 days."""
    ami    = _amihud(close, volume)
    ret    = close.pct_change(1)
    masked = ami.where(ret < 0, np.nan)
    return masked.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def lqc_039_amihud_up_day_mean_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean Amihud on up-price days over trailing 21 days."""
    ami    = _amihud(close, volume)
    ret    = close.pct_change(1)
    masked = ami.where(ret > 0, np.nan)
    return masked.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def lqc_040_amihud_down_vs_up_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of mean Amihud on down days to mean Amihud on up days (21d window)."""
    return _safe_div(lqc_038_amihud_down_day_mean_21d(close, volume),
                     lqc_039_amihud_up_day_mean_21d(close, volume))


# --- Group E (041-050): Amihud illiquidity streaks ---

def lqc_041_amihud_above_mean_streak_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days where Amihud exceeds its 21-day rolling mean."""
    ami  = _amihud(close, volume)
    mu   = _rolling_mean(ami, _TD_MON)
    cond = ami > mu
    return _consec_streak(cond)


def lqc_042_amihud_above_mean_streak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days where Amihud exceeds its 63-day rolling mean."""
    ami  = _amihud(close, volume)
    mu   = _rolling_mean(ami, _TD_QTR)
    cond = ami > mu
    return _consec_streak(cond)


def lqc_043_amihud_above_mean_streak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days where Amihud exceeds its 252-day rolling mean."""
    ami  = _amihud(close, volume)
    mu   = _rolling_mean(ami, _TD_YEAR)
    cond = ami > mu
    return _consec_streak(cond)


def lqc_044_amihud_rising_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days of rising Amihud (today > yesterday, illiquidity worsening)."""
    ami  = _amihud(close, volume)
    cond = ami > ami.shift(1)
    return _consec_streak(cond)


def lqc_045_amihud_max_rising_streak_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum consecutive Amihud-rising days within trailing 21 days."""
    ami  = _amihud(close, volume)
    cond = ami > ami.shift(1)
    return _rolling_max_streak(cond, _TD_MON)


def lqc_046_amihud_max_rising_streak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum consecutive Amihud-rising days within trailing 63 days."""
    ami  = _amihud(close, volume)
    cond = ami > ami.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


def lqc_047_amihud_above_90pct_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days where Amihud exceeds its trailing 252d 90th percentile."""
    ami  = _amihud(close, volume)
    p90  = ami.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)
    cond = ami > p90
    return _consec_streak(cond)


def lqc_048_amihud_spike_streak_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of spike days (Amihud > 2std above 63d mean) in trailing 63-day window."""
    ami   = _amihud(close, volume)
    mu    = _rolling_mean(ami, _TD_QTR)
    sig   = _rolling_std(ami, _TD_QTR)
    spike = (ami > mu + 2.0 * sig).astype(float)
    return _rolling_sum(spike, _TD_QTR)


def lqc_049_amihud_streak_norm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Above-21d-mean Amihud streak normalized by its 252d average streak length."""
    streak = lqc_041_amihud_above_mean_streak_21d(close, volume)
    avg    = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def lqc_050_amihud_max_above_mean_streak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive days above 21d Amihud mean within trailing 252 days."""
    ami  = _amihud(close, volume)
    mu   = _rolling_mean(ami, _TD_MON)
    cond = ami > mu
    return _rolling_max_streak(cond, _TD_YEAR)


# --- Group F (051-062): Corwin-Schultz high-low bid-ask spread estimator ---

def lqc_051_cs_spread_daily(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz (2012) daily bid-ask spread estimate from high-low prices."""
    return _cs_spread(high, low, close)


def lqc_052_cs_spread_roll_mean_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day rolling mean of Corwin-Schultz spread estimate."""
    return _rolling_mean(_cs_spread(high, low, close), _TD_WEEK)


def lqc_053_cs_spread_roll_mean_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling mean of Corwin-Schultz spread estimate."""
    return _rolling_mean(_cs_spread(high, low, close), _TD_MON)


def lqc_054_cs_spread_roll_mean_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling mean of Corwin-Schultz spread estimate."""
    return _rolling_mean(_cs_spread(high, low, close), _TD_QTR)


def lqc_055_cs_spread_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Corwin-Schultz spread within trailing 21 days."""
    return _zscore(_cs_spread(high, low, close), _TD_MON)


def lqc_056_cs_spread_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Corwin-Schultz spread within trailing 63 days."""
    return _zscore(_cs_spread(high, low, close), _TD_QTR)


def lqc_057_cs_spread_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Corwin-Schultz spread within trailing 252 days."""
    return _zscore(_cs_spread(high, low, close), _TD_YEAR)


def lqc_058_cs_spread_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of Corwin-Schultz spread within trailing 252 days."""
    return _pct_rank(_cs_spread(high, low, close), _TD_YEAR)


def lqc_059_cs_spread_spike_gt2std_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Corwin-Schultz spread > 2 std above 63-day mean (wide-spread spike)."""
    cs  = _cs_spread(high, low, close)
    mu  = _rolling_mean(cs, _TD_QTR)
    sig = _rolling_std(cs, _TD_QTR)
    return (cs > mu + 2.0 * sig).astype(float)


def lqc_060_cs_spread_spike_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz spread divided by its 63-day mean (relative spike magnitude)."""
    cs = _cs_spread(high, low, close)
    return _safe_div(cs, _rolling_mean(cs, _TD_QTR))


def lqc_061_cs_spread_rising_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days of rising Corwin-Schultz spread (worsening bid-ask)."""
    cs   = _cs_spread(high, low, close)
    cond = cs > cs.shift(1)
    return _consec_streak(cond)


def lqc_062_cs_spread_above_mean_streak_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days where C-S spread exceeds its 63-day rolling mean."""
    cs   = _cs_spread(high, low, close)
    mu   = _rolling_mean(cs, _TD_QTR)
    cond = cs > mu
    return _consec_streak(cond)


# --- Group G (063-075): Roll spread estimator ---

def lqc_063_roll_spread_daily(close: pd.Series) -> pd.Series:
    """Roll (1984) effective spread: 2*sqrt(-cov(dP_t, dP_{t-1})), clipped at 0."""
    return _roll_spread(close)


def lqc_064_roll_spread_roll_mean_21d(close: pd.Series) -> pd.Series:
    """21-day rolling mean of Roll spread estimate."""
    return _rolling_mean(_roll_spread(close), _TD_MON)


def lqc_065_roll_spread_roll_mean_63d(close: pd.Series) -> pd.Series:
    """63-day rolling mean of Roll spread estimate."""
    return _rolling_mean(_roll_spread(close), _TD_QTR)


def lqc_066_roll_spread_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of Roll spread within trailing 63-day window."""
    return _zscore(_roll_spread(close), _TD_QTR)


def lqc_067_roll_spread_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Roll spread within trailing 252-day window."""
    return _zscore(_roll_spread(close), _TD_YEAR)


def lqc_068_roll_spread_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of Roll spread within trailing 252 days."""
    return _pct_rank(_roll_spread(close), _TD_YEAR)


def lqc_069_roll_spread_spike_gt2std_63d(close: pd.Series) -> pd.Series:
    """Flag: Roll spread > 2 std above 63-day mean."""
    rs  = _roll_spread(close)
    mu  = _rolling_mean(rs, _TD_QTR)
    sig = _rolling_std(rs, _TD_QTR)
    return (rs > mu + 2.0 * sig).astype(float)


def lqc_070_roll_spread_spike_ratio_252d(close: pd.Series) -> pd.Series:
    """Roll spread divided by its 252-day mean (long-run relative spike)."""
    rs = _roll_spread(close)
    return _safe_div(rs, _rolling_mean(rs, _TD_YEAR))


def lqc_071_roll_vs_cs_spread_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of Roll spread to Corwin-Schultz spread (cross-estimator comparison)."""
    return _safe_div(_roll_spread(close), _cs_spread(high, low, close))


def lqc_072_roll_spread_rising_streak(close: pd.Series) -> pd.Series:
    """Consecutive days of rising Roll spread estimate."""
    rs   = _roll_spread(close)
    cond = rs > rs.shift(1)
    return _consec_streak(cond)


def lqc_073_roll_spread_above_mean_streak_63d(close: pd.Series) -> pd.Series:
    """Consecutive days where Roll spread exceeds its 63-day mean."""
    rs   = _roll_spread(close)
    mu   = _rolling_mean(rs, _TD_QTR)
    cond = rs > mu
    return _consec_streak(cond)


def lqc_074_roll_spread_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of Roll spread."""
    return _roll_spread(close).expanding(min_periods=5).rank(pct=True)


def lqc_075_roll_spread_max_21d(close: pd.Series) -> pd.Series:
    """21-day rolling maximum of Roll spread estimate (worst bid-ask in recent month)."""
    return _rolling_max(_roll_spread(close), _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

LIQUIDITY_COLLAPSE_REGISTRY_001_075 = {
    "lqc_001_amihud_daily": {"inputs": ["close", "volume"], "func": lqc_001_amihud_daily},
    "lqc_002_amihud_scaled_1e6": {"inputs": ["close", "volume"], "func": lqc_002_amihud_scaled_1e6},
    "lqc_003_amihud_log": {"inputs": ["close", "volume"], "func": lqc_003_amihud_log},
    "lqc_004_amihud_roll_mean_5d": {"inputs": ["close", "volume"], "func": lqc_004_amihud_roll_mean_5d},
    "lqc_005_amihud_roll_mean_21d": {"inputs": ["close", "volume"], "func": lqc_005_amihud_roll_mean_21d},
    "lqc_006_amihud_roll_mean_63d": {"inputs": ["close", "volume"], "func": lqc_006_amihud_roll_mean_63d},
    "lqc_007_amihud_roll_mean_126d": {"inputs": ["close", "volume"], "func": lqc_007_amihud_roll_mean_126d},
    "lqc_008_amihud_roll_mean_252d": {"inputs": ["close", "volume"], "func": lqc_008_amihud_roll_mean_252d},
    "lqc_009_amihud_roll_max_21d": {"inputs": ["close", "volume"], "func": lqc_009_amihud_roll_max_21d},
    "lqc_010_amihud_roll_max_63d": {"inputs": ["close", "volume"], "func": lqc_010_amihud_roll_max_63d},
    "lqc_011_amihud_zscore_21d": {"inputs": ["close", "volume"], "func": lqc_011_amihud_zscore_21d},
    "lqc_012_amihud_zscore_63d": {"inputs": ["close", "volume"], "func": lqc_012_amihud_zscore_63d},
    "lqc_013_amihud_zscore_126d": {"inputs": ["close", "volume"], "func": lqc_013_amihud_zscore_126d},
    "lqc_014_amihud_zscore_252d": {"inputs": ["close", "volume"], "func": lqc_014_amihud_zscore_252d},
    "lqc_015_amihud_pct_rank_21d": {"inputs": ["close", "volume"], "func": lqc_015_amihud_pct_rank_21d},
    "lqc_016_amihud_pct_rank_63d": {"inputs": ["close", "volume"], "func": lqc_016_amihud_pct_rank_63d},
    "lqc_017_amihud_pct_rank_126d": {"inputs": ["close", "volume"], "func": lqc_017_amihud_pct_rank_126d},
    "lqc_018_amihud_pct_rank_252d": {"inputs": ["close", "volume"], "func": lqc_018_amihud_pct_rank_252d},
    "lqc_019_amihud_expanding_pct_rank": {"inputs": ["close", "volume"], "func": lqc_019_amihud_expanding_pct_rank},
    "lqc_020_amihud_ewm_zscore_21d": {"inputs": ["close", "volume"], "func": lqc_020_amihud_ewm_zscore_21d},
    "lqc_021_amihud_spike_gt2std_21d": {"inputs": ["close", "volume"], "func": lqc_021_amihud_spike_gt2std_21d},
    "lqc_022_amihud_spike_gt3std_63d": {"inputs": ["close", "volume"], "func": lqc_022_amihud_spike_gt3std_63d},
    "lqc_023_amihud_spike_gt2std_252d": {"inputs": ["close", "volume"], "func": lqc_023_amihud_spike_gt2std_252d},
    "lqc_024_amihud_spike_ratio_21d": {"inputs": ["close", "volume"], "func": lqc_024_amihud_spike_ratio_21d},
    "lqc_025_amihud_spike_ratio_63d": {"inputs": ["close", "volume"], "func": lqc_025_amihud_spike_ratio_63d},
    "lqc_026_amihud_spike_ratio_252d": {"inputs": ["close", "volume"], "func": lqc_026_amihud_spike_ratio_252d},
    "lqc_027_amihud_spike_count_21d": {"inputs": ["close", "volume"], "func": lqc_027_amihud_spike_count_21d},
    "lqc_028_amihud_spike_count_63d": {"inputs": ["close", "volume"], "func": lqc_028_amihud_spike_count_63d},
    "lqc_029_amihud_above_90pct_21d_flag": {"inputs": ["close", "volume"], "func": lqc_029_amihud_above_90pct_21d_flag},
    "lqc_030_amihud_above_95pct_252d_flag": {"inputs": ["close", "volume"], "func": lqc_030_amihud_above_95pct_252d_flag},
    "lqc_031_amihud_rising_price_falling_flag": {"inputs": ["close", "volume"], "func": lqc_031_amihud_rising_price_falling_flag},
    "lqc_032_amihud_5d_chg_vs_ret": {"inputs": ["close", "volume"], "func": lqc_032_amihud_5d_chg_vs_ret},
    "lqc_033_amihud_21d_chg_vs_ret": {"inputs": ["close", "volume"], "func": lqc_033_amihud_21d_chg_vs_ret},
    "lqc_034_amihud_diverge_from_price_zscore": {"inputs": ["close", "volume"], "func": lqc_034_amihud_diverge_from_price_zscore},
    "lqc_035_amihud_price_fall_consec": {"inputs": ["close", "volume"], "func": lqc_035_amihud_price_fall_consec},
    "lqc_036_amihud_corr_neg_ret_21d": {"inputs": ["close", "volume"], "func": lqc_036_amihud_corr_neg_ret_21d},
    "lqc_037_amihud_corr_neg_ret_63d": {"inputs": ["close", "volume"], "func": lqc_037_amihud_corr_neg_ret_63d},
    "lqc_038_amihud_down_day_mean_21d": {"inputs": ["close", "volume"], "func": lqc_038_amihud_down_day_mean_21d},
    "lqc_039_amihud_up_day_mean_21d": {"inputs": ["close", "volume"], "func": lqc_039_amihud_up_day_mean_21d},
    "lqc_040_amihud_down_vs_up_ratio_21d": {"inputs": ["close", "volume"], "func": lqc_040_amihud_down_vs_up_ratio_21d},
    "lqc_041_amihud_above_mean_streak_21d": {"inputs": ["close", "volume"], "func": lqc_041_amihud_above_mean_streak_21d},
    "lqc_042_amihud_above_mean_streak_63d": {"inputs": ["close", "volume"], "func": lqc_042_amihud_above_mean_streak_63d},
    "lqc_043_amihud_above_mean_streak_252d": {"inputs": ["close", "volume"], "func": lqc_043_amihud_above_mean_streak_252d},
    "lqc_044_amihud_rising_streak": {"inputs": ["close", "volume"], "func": lqc_044_amihud_rising_streak},
    "lqc_045_amihud_max_rising_streak_21d": {"inputs": ["close", "volume"], "func": lqc_045_amihud_max_rising_streak_21d},
    "lqc_046_amihud_max_rising_streak_63d": {"inputs": ["close", "volume"], "func": lqc_046_amihud_max_rising_streak_63d},
    "lqc_047_amihud_above_90pct_streak": {"inputs": ["close", "volume"], "func": lqc_047_amihud_above_90pct_streak},
    "lqc_048_amihud_spike_streak_count_63d": {"inputs": ["close", "volume"], "func": lqc_048_amihud_spike_streak_count_63d},
    "lqc_049_amihud_streak_norm_252d": {"inputs": ["close", "volume"], "func": lqc_049_amihud_streak_norm_252d},
    "lqc_050_amihud_max_above_mean_streak_252d": {"inputs": ["close", "volume"], "func": lqc_050_amihud_max_above_mean_streak_252d},
    "lqc_051_cs_spread_daily": {"inputs": ["close", "high", "low"], "func": lqc_051_cs_spread_daily},
    "lqc_052_cs_spread_roll_mean_5d": {"inputs": ["close", "high", "low"], "func": lqc_052_cs_spread_roll_mean_5d},
    "lqc_053_cs_spread_roll_mean_21d": {"inputs": ["close", "high", "low"], "func": lqc_053_cs_spread_roll_mean_21d},
    "lqc_054_cs_spread_roll_mean_63d": {"inputs": ["close", "high", "low"], "func": lqc_054_cs_spread_roll_mean_63d},
    "lqc_055_cs_spread_zscore_21d": {"inputs": ["close", "high", "low"], "func": lqc_055_cs_spread_zscore_21d},
    "lqc_056_cs_spread_zscore_63d": {"inputs": ["close", "high", "low"], "func": lqc_056_cs_spread_zscore_63d},
    "lqc_057_cs_spread_zscore_252d": {"inputs": ["close", "high", "low"], "func": lqc_057_cs_spread_zscore_252d},
    "lqc_058_cs_spread_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": lqc_058_cs_spread_pct_rank_252d},
    "lqc_059_cs_spread_spike_gt2std_63d": {"inputs": ["close", "high", "low"], "func": lqc_059_cs_spread_spike_gt2std_63d},
    "lqc_060_cs_spread_spike_ratio_63d": {"inputs": ["close", "high", "low"], "func": lqc_060_cs_spread_spike_ratio_63d},
    "lqc_061_cs_spread_rising_streak": {"inputs": ["close", "high", "low"], "func": lqc_061_cs_spread_rising_streak},
    "lqc_062_cs_spread_above_mean_streak_63d": {"inputs": ["close", "high", "low"], "func": lqc_062_cs_spread_above_mean_streak_63d},
    "lqc_063_roll_spread_daily": {"inputs": ["close"], "func": lqc_063_roll_spread_daily},
    "lqc_064_roll_spread_roll_mean_21d": {"inputs": ["close"], "func": lqc_064_roll_spread_roll_mean_21d},
    "lqc_065_roll_spread_roll_mean_63d": {"inputs": ["close"], "func": lqc_065_roll_spread_roll_mean_63d},
    "lqc_066_roll_spread_zscore_63d": {"inputs": ["close"], "func": lqc_066_roll_spread_zscore_63d},
    "lqc_067_roll_spread_zscore_252d": {"inputs": ["close"], "func": lqc_067_roll_spread_zscore_252d},
    "lqc_068_roll_spread_pct_rank_252d": {"inputs": ["close"], "func": lqc_068_roll_spread_pct_rank_252d},
    "lqc_069_roll_spread_spike_gt2std_63d": {"inputs": ["close"], "func": lqc_069_roll_spread_spike_gt2std_63d},
    "lqc_070_roll_spread_spike_ratio_252d": {"inputs": ["close"], "func": lqc_070_roll_spread_spike_ratio_252d},
    "lqc_071_roll_vs_cs_spread_ratio": {"inputs": ["close", "high", "low"], "func": lqc_071_roll_vs_cs_spread_ratio},
    "lqc_072_roll_spread_rising_streak": {"inputs": ["close"], "func": lqc_072_roll_spread_rising_streak},
    "lqc_073_roll_spread_above_mean_streak_63d": {"inputs": ["close"], "func": lqc_073_roll_spread_above_mean_streak_63d},
    "lqc_074_roll_spread_expanding_pct_rank": {"inputs": ["close"], "func": lqc_074_roll_spread_expanding_pct_rank},
    "lqc_075_roll_spread_max_21d": {"inputs": ["close"], "func": lqc_075_roll_spread_max_21d},
}
