"""
57_spread_proxy — Base Features 001-075
Domain: HIGH-LOW SPREAD illiquidity estimators — effective bid-ask spread proxies
        from OHLC (Corwin-Schultz, Abdi-Ranaldi, Roll-style, high-low%, gap-based).
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
    """Element-wise division; replaces zero/nan denominator with NaN."""
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


def _hl_spread_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Simple (high-low)/close spread proxy, the base spread estimator."""
    return _safe_div(high - low, close)


def _beta_cs(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz beta: sum of squared log(H/L) over two consecutive days."""
    log_hl = (_log_safe(high) - _log_safe(low)) ** 2
    return log_hl + log_hl.shift(1)


def _gamma_cs(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz gamma: squared log of two-day H/L range."""
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    return (_log_safe(h2) - _log_safe(l2)) ** 2


def _corwin_schultz_alpha(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz alpha = (sqrt(2*beta)-sqrt(beta)) / (3-2*sqrt(2)) - sqrt(gamma/(3-2*sqrt(2)))."""
    k1 = 3.0 - 2.0 * np.sqrt(2.0)
    beta = _beta_cs(high, low)
    gamma = _gamma_cs(high, low)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k1 - np.sqrt(gamma / k1)
    return alpha


def _cs_spread(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz spread estimate: 2*(exp(alpha)-1)/(1+exp(alpha)), floored at 0."""
    alpha = _corwin_schultz_alpha(high, low)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0.0)


def _ar_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Abdi-Ranaldi spread: 4*(log(close)-log(midpoint)), midpoint=0.5*(high+low)."""
    mid = 0.5 * (high + low)
    return 4.0 * (_log_safe(close) - _log_safe(mid))


def _roll_cov(close: pd.Series, w: int) -> pd.Series:
    """Roll-model covariance: rolling cov(delta_c_t, delta_c_{t-1}) over w periods."""
    dc = close.diff(1)
    dc1 = dc.shift(1)
    return dc.rolling(w, min_periods=max(2, w // 2)).cov(dc1)


def _roll_spread(close: pd.Series, w: int) -> pd.Series:
    """Roll effective spread estimate: 2*sqrt(max(-cov,0))."""
    cov = _roll_cov(close, w)
    return 2.0 * np.sqrt((-cov).clip(lower=0.0))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Raw spread estimators (Corwin-Schultz) ---

def spr_001_cs_spread_daily(high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily Corwin-Schultz effective spread estimate (two-day high-low method)."""
    return _cs_spread(high, low)


def spr_002_cs_spread_roll_mean_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day rolling mean of Corwin-Schultz spread."""
    return _rolling_mean(_cs_spread(high, low), _TD_WEEK)


def spr_003_cs_spread_roll_mean_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling mean of Corwin-Schultz spread."""
    return _rolling_mean(_cs_spread(high, low), _TD_MON)


def spr_004_cs_spread_roll_mean_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling mean of Corwin-Schultz spread."""
    return _rolling_mean(_cs_spread(high, low), _TD_QTR)


def spr_005_cs_spread_roll_mean_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day rolling mean of Corwin-Schultz spread."""
    return _rolling_mean(_cs_spread(high, low), _TD_YEAR)


def spr_006_cs_spread_zscore_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day z-score of Corwin-Schultz spread."""
    cs = _cs_spread(high, low)
    return _safe_div(cs - _rolling_mean(cs, _TD_MON), _rolling_std(cs, _TD_MON))


def spr_007_cs_spread_zscore_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day z-score of Corwin-Schultz spread."""
    cs = _cs_spread(high, low)
    return _safe_div(cs - _rolling_mean(cs, _TD_QTR), _rolling_std(cs, _TD_QTR))


def spr_008_cs_spread_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day z-score of Corwin-Schultz spread."""
    cs = _cs_spread(high, low)
    return _safe_div(cs - _rolling_mean(cs, _TD_YEAR), _rolling_std(cs, _TD_YEAR))


def spr_009_cs_spread_pct_rank_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day percentile rank of Corwin-Schultz spread."""
    return _cs_spread(high, low).rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def spr_010_cs_spread_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day percentile rank of Corwin-Schultz spread."""
    return _cs_spread(high, low).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def spr_011_cs_spread_expanding_max(high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-time maximum Corwin-Schultz spread."""
    return _cs_spread(high, low).expanding(min_periods=2).max()


def spr_012_cs_spread_vs_expanding_max(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current CS spread as fraction of expanding all-time maximum."""
    cs = _cs_spread(high, low)
    return _safe_div(cs, cs.expanding(min_periods=2).max())


# --- Group B (013-024): Abdi-Ranaldi spread estimator ---

def spr_013_ar_spread_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily Abdi-Ranaldi spread: 4*(log(close) - log(midpoint))."""
    return _ar_spread(high, low, close)


def spr_014_ar_spread_abs_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of daily Abdi-Ranaldi spread."""
    return _ar_spread(high, low, close).abs()


def spr_015_ar_spread_roll_mean_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day rolling mean of absolute Abdi-Ranaldi spread."""
    return _rolling_mean(_ar_spread(high, low, close).abs(), _TD_WEEK)


def spr_016_ar_spread_roll_mean_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of absolute Abdi-Ranaldi spread."""
    return _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON)


def spr_017_ar_spread_roll_mean_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of absolute Abdi-Ranaldi spread."""
    return _rolling_mean(_ar_spread(high, low, close).abs(), _TD_QTR)


def spr_018_ar_spread_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day z-score of absolute Abdi-Ranaldi spread."""
    ar = _ar_spread(high, low, close).abs()
    return _safe_div(ar - _rolling_mean(ar, _TD_MON), _rolling_std(ar, _TD_MON))


def spr_019_ar_spread_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day z-score of absolute Abdi-Ranaldi spread."""
    ar = _ar_spread(high, low, close).abs()
    return _safe_div(ar - _rolling_mean(ar, _TD_QTR), _rolling_std(ar, _TD_QTR))


def spr_020_ar_spread_pct_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day percentile rank of absolute Abdi-Ranaldi spread."""
    ar = _ar_spread(high, low, close).abs()
    return ar.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def spr_021_ar_spread_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day percentile rank of absolute Abdi-Ranaldi spread."""
    ar = _ar_spread(high, low, close).abs()
    return ar.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def spr_022_ar_spread_ewm_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EWM mean of absolute Abdi-Ranaldi spread."""
    return _ewm_mean(_ar_spread(high, low, close).abs(), _TD_MON)


def spr_023_ar_spread_vs_cs_spread_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of AR spread to CS spread (cross-estimator comparison)."""
    ar = _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON)
    cs = _rolling_mean(_cs_spread(high, low), _TD_MON)
    return _safe_div(ar, cs)


def spr_024_ar_spread_expanding_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-time maximum of absolute Abdi-Ranaldi spread."""
    return _ar_spread(high, low, close).abs().expanding(min_periods=2).max()


# --- Group C (025-036): Simple high-low/close spread proxy ---

def spr_025_hl_spread_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily (high-low)/close spread proxy."""
    return _hl_spread_raw(high, low, close)


def spr_026_hl_spread_roll_mean_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day rolling mean of (high-low)/close spread proxy."""
    return _rolling_mean(_hl_spread_raw(high, low, close), _TD_WEEK)


def spr_027_hl_spread_roll_mean_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of (high-low)/close spread proxy."""
    return _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)


def spr_028_hl_spread_roll_mean_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of (high-low)/close spread proxy."""
    return _rolling_mean(_hl_spread_raw(high, low, close), _TD_QTR)


def spr_029_hl_spread_roll_mean_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling mean of (high-low)/close spread proxy."""
    return _rolling_mean(_hl_spread_raw(high, low, close), _TD_YEAR)


def spr_030_hl_spread_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day z-score of (high-low)/close spread proxy."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(hl - _rolling_mean(hl, _TD_MON), _rolling_std(hl, _TD_MON))


def spr_031_hl_spread_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day z-score of (high-low)/close spread proxy."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(hl - _rolling_mean(hl, _TD_QTR), _rolling_std(hl, _TD_QTR))


def spr_032_hl_spread_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day z-score of (high-low)/close spread proxy."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(hl - _rolling_mean(hl, _TD_YEAR), _rolling_std(hl, _TD_YEAR))


def spr_033_hl_spread_pct_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day percentile rank of (high-low)/close spread proxy."""
    return _hl_spread_raw(high, low, close).rolling(_TD_MON, min_periods=5).rank(pct=True)


def spr_034_hl_spread_pct_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day percentile rank of (high-low)/close spread proxy."""
    return _hl_spread_raw(high, low, close).rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def spr_035_hl_spread_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day percentile rank of (high-low)/close spread proxy."""
    return _hl_spread_raw(high, low, close).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def spr_036_hl_spread_expanding_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-time maximum of (high-low)/close spread proxy."""
    return _hl_spread_raw(high, low, close).expanding(min_periods=1).max()


# --- Group D (037-048): Roll-style close-to-close covariance spread ---

def spr_037_roll_spread_21d(close: pd.Series) -> pd.Series:
    """Roll effective spread: 2*sqrt(max(-cov(delta_c_t, delta_c_{t-1}), 0)) over 21d."""
    return _roll_spread(close, _TD_MON)


def spr_038_roll_spread_63d(close: pd.Series) -> pd.Series:
    """Roll effective spread estimate over 63-day window."""
    return _roll_spread(close, _TD_QTR)


def spr_039_roll_spread_126d(close: pd.Series) -> pd.Series:
    """Roll effective spread estimate over 126-day window."""
    return _roll_spread(close, _TD_HALF)


def spr_040_roll_spread_252d(close: pd.Series) -> pd.Series:
    """Roll effective spread estimate over 252-day window."""
    return _roll_spread(close, _TD_YEAR)


def spr_041_roll_spread_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """252-day z-score of the 21-day Roll spread."""
    rs = _roll_spread(close, _TD_MON)
    return _safe_div(rs - _rolling_mean(rs, _TD_YEAR), _rolling_std(rs, _TD_YEAR))


def spr_042_roll_spread_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """252-day percentile rank of the 21-day Roll spread."""
    return _roll_spread(close, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def spr_043_roll_cov_21d(close: pd.Series) -> pd.Series:
    """Raw 21-day Roll covariance cov(delta_c_t, delta_c_{t-1})."""
    return _roll_cov(close, _TD_MON)


def spr_044_roll_cov_63d(close: pd.Series) -> pd.Series:
    """Raw 63-day Roll covariance cov(delta_c_t, delta_c_{t-1})."""
    return _roll_cov(close, _TD_QTR)


def spr_045_roll_spread_21d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day Roll spread to 63-day Roll spread (short vs medium liquidity)."""
    return _safe_div(_roll_spread(close, _TD_MON), _roll_spread(close, _TD_QTR))


def spr_046_roll_spread_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day Roll spread to 252-day Roll spread."""
    return _safe_div(_roll_spread(close, _TD_QTR), _roll_spread(close, _TD_YEAR))


def spr_047_roll_spread_21d_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM smoothed (span=21) version of the 21-day Roll spread."""
    return _ewm_mean(_roll_spread(close, _TD_MON), _TD_MON)


def spr_048_roll_spread_21d_expanding_max(close: pd.Series) -> pd.Series:
    """Expanding all-time maximum of 21-day Roll spread."""
    return _roll_spread(close, _TD_MON).expanding(min_periods=2).max()


# --- Group E (049-060): Gap-based spread proxies ---

def spr_049_gap_spread_daily(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight gap spread proxy: abs(open - prior_close) / prior_close."""
    return _safe_div((open - close.shift(1)).abs(), close.shift(1))


def spr_050_gap_spread_roll_mean_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day rolling mean of overnight gap spread proxy."""
    return _rolling_mean(_safe_div((open - close.shift(1)).abs(), close.shift(1)), _TD_WEEK)


def spr_051_gap_spread_roll_mean_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day rolling mean of overnight gap spread proxy."""
    return _rolling_mean(_safe_div((open - close.shift(1)).abs(), close.shift(1)), _TD_MON)


def spr_052_gap_spread_roll_mean_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling mean of overnight gap spread proxy."""
    return _rolling_mean(_safe_div((open - close.shift(1)).abs(), close.shift(1)), _TD_QTR)


def spr_053_gap_spread_zscore_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day z-score of overnight gap spread proxy."""
    gap = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    return _safe_div(gap - _rolling_mean(gap, _TD_MON), _rolling_std(gap, _TD_MON))


def spr_054_gap_spread_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day z-score of overnight gap spread proxy."""
    gap = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    return _safe_div(gap - _rolling_mean(gap, _TD_QTR), _rolling_std(gap, _TD_QTR))


def spr_055_gap_spread_pct_rank_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day percentile rank of overnight gap spread proxy."""
    gap = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    return gap.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def spr_056_gap_spread_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day percentile rank of overnight gap spread proxy."""
    gap = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    return gap.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def spr_057_gap_vs_hl_spread_ratio_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series
) -> pd.Series:
    """Ratio of 21d avg gap spread to 21d avg HL spread (overnight vs intraday)."""
    gap21 = _rolling_mean(_safe_div((open - close.shift(1)).abs(), close.shift(1)), _TD_MON)
    hl21  = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    return _safe_div(gap21, hl21)


def spr_058_intraday_vs_overnight_spread_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series
) -> pd.Series:
    """21d avg intraday (open-to-close range) vs overnight spread ratio."""
    intra = _safe_div((close - open).abs(), open.replace(0, np.nan))
    over  = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    return _safe_div(_rolling_mean(intra, _TD_MON), _rolling_mean(over, _TD_MON))


def spr_059_gap_down_spread_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21d mean of negative gaps only: (prior_close - open)/prior_close when open < prior_close."""
    prior = close.shift(1)
    gap = _safe_div(prior - open, prior)
    gap_down = gap.where(open < prior, 0.0)
    return _rolling_mean(gap_down, _TD_MON)


def spr_060_gap_up_spread_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21d mean of positive gaps only: (open - prior_close)/prior_close when open > prior_close."""
    prior = close.shift(1)
    gap = _safe_div(open - prior, prior)
    gap_up = gap.where(open > prior, 0.0)
    return _rolling_mean(gap_up, _TD_MON)


# --- Group F (061-075): HL% spread vs baselines, spread widening streaks ---

def spr_061_hl_spread_vs_21d_baseline(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current HL spread divided by its own 21-day mean (spread widening ratio)."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(hl, _rolling_mean(hl, _TD_MON))


def spr_062_hl_spread_vs_63d_baseline(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current HL spread divided by its 63-day mean baseline."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(hl, _rolling_mean(hl, _TD_QTR))


def spr_063_hl_spread_vs_252d_baseline(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current HL spread divided by its 252-day mean baseline."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(hl, _rolling_mean(hl, _TD_YEAR))


def spr_064_cs_spread_vs_21d_baseline(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current CS spread divided by its own 21-day mean (widening ratio)."""
    cs = _cs_spread(high, low)
    return _safe_div(cs, _rolling_mean(cs, _TD_MON))


def spr_065_cs_spread_vs_63d_baseline(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current CS spread divided by its 63-day mean baseline."""
    cs = _cs_spread(high, low)
    return _safe_div(cs, _rolling_mean(cs, _TD_QTR))


def spr_066_cs_spread_vs_252d_baseline(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current CS spread divided by its 252-day mean baseline."""
    cs = _cs_spread(high, low)
    return _safe_div(cs, _rolling_mean(cs, _TD_YEAR))


def spr_067_spread_widening_streak_hl(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days HL spread > prior day HL spread (spread-widening streak)."""
    hl = _hl_spread_raw(high, low, close)
    cond = hl > hl.shift(1)
    return _consec_streak(cond)


def spr_068_spread_widening_streak_cs(high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days CS spread > prior day CS spread."""
    cs = _cs_spread(high, low)
    cond = cs > cs.shift(1)
    return _consec_streak(cond)


def spr_069_spread_above_21d_mean_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days HL spread exceeds its trailing 21-day mean."""
    hl = _hl_spread_raw(high, low, close)
    cond = hl > _rolling_mean(hl, _TD_MON)
    return _consec_streak(cond)


def spr_070_spread_above_63d_mean_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days HL spread exceeds its trailing 63-day mean."""
    hl = _hl_spread_raw(high, low, close)
    cond = hl > _rolling_mean(hl, _TD_QTR)
    return _consec_streak(cond)


def spr_071_hl_spread_max_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling maximum of HL spread proxy."""
    return _rolling_max(_hl_spread_raw(high, low, close), _TD_MON)


def spr_072_hl_spread_max_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling maximum of HL spread proxy."""
    return _rolling_max(_hl_spread_raw(high, low, close), _TD_QTR)


def spr_073_hl_spread_median_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling median of HL spread proxy."""
    return _rolling_median(_hl_spread_raw(high, low, close), _TD_MON)


def spr_074_hl_spread_median_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling median of HL spread proxy."""
    return _rolling_median(_hl_spread_raw(high, low, close), _TD_QTR)


def spr_075_hl_spread_std_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling standard deviation of HL spread proxy (spread volatility)."""
    return _rolling_std(_hl_spread_raw(high, low, close), _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

SPREAD_PROXY_REGISTRY_001_075 = {
    "spr_001_cs_spread_daily": {"inputs": ["high", "low"], "func": spr_001_cs_spread_daily},
    "spr_002_cs_spread_roll_mean_5d": {"inputs": ["high", "low"], "func": spr_002_cs_spread_roll_mean_5d},
    "spr_003_cs_spread_roll_mean_21d": {"inputs": ["high", "low"], "func": spr_003_cs_spread_roll_mean_21d},
    "spr_004_cs_spread_roll_mean_63d": {"inputs": ["high", "low"], "func": spr_004_cs_spread_roll_mean_63d},
    "spr_005_cs_spread_roll_mean_252d": {"inputs": ["high", "low"], "func": spr_005_cs_spread_roll_mean_252d},
    "spr_006_cs_spread_zscore_21d": {"inputs": ["high", "low"], "func": spr_006_cs_spread_zscore_21d},
    "spr_007_cs_spread_zscore_63d": {"inputs": ["high", "low"], "func": spr_007_cs_spread_zscore_63d},
    "spr_008_cs_spread_zscore_252d": {"inputs": ["high", "low"], "func": spr_008_cs_spread_zscore_252d},
    "spr_009_cs_spread_pct_rank_63d": {"inputs": ["high", "low"], "func": spr_009_cs_spread_pct_rank_63d},
    "spr_010_cs_spread_pct_rank_252d": {"inputs": ["high", "low"], "func": spr_010_cs_spread_pct_rank_252d},
    "spr_011_cs_spread_expanding_max": {"inputs": ["high", "low"], "func": spr_011_cs_spread_expanding_max},
    "spr_012_cs_spread_vs_expanding_max": {"inputs": ["high", "low"], "func": spr_012_cs_spread_vs_expanding_max},
    "spr_013_ar_spread_daily": {"inputs": ["high", "low", "close"], "func": spr_013_ar_spread_daily},
    "spr_014_ar_spread_abs_daily": {"inputs": ["high", "low", "close"], "func": spr_014_ar_spread_abs_daily},
    "spr_015_ar_spread_roll_mean_5d": {"inputs": ["high", "low", "close"], "func": spr_015_ar_spread_roll_mean_5d},
    "spr_016_ar_spread_roll_mean_21d": {"inputs": ["high", "low", "close"], "func": spr_016_ar_spread_roll_mean_21d},
    "spr_017_ar_spread_roll_mean_63d": {"inputs": ["high", "low", "close"], "func": spr_017_ar_spread_roll_mean_63d},
    "spr_018_ar_spread_zscore_21d": {"inputs": ["high", "low", "close"], "func": spr_018_ar_spread_zscore_21d},
    "spr_019_ar_spread_zscore_63d": {"inputs": ["high", "low", "close"], "func": spr_019_ar_spread_zscore_63d},
    "spr_020_ar_spread_pct_rank_63d": {"inputs": ["high", "low", "close"], "func": spr_020_ar_spread_pct_rank_63d},
    "spr_021_ar_spread_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": spr_021_ar_spread_pct_rank_252d},
    "spr_022_ar_spread_ewm_21d": {"inputs": ["high", "low", "close"], "func": spr_022_ar_spread_ewm_21d},
    "spr_023_ar_spread_vs_cs_spread_ratio": {"inputs": ["high", "low", "close"], "func": spr_023_ar_spread_vs_cs_spread_ratio},
    "spr_024_ar_spread_expanding_max": {"inputs": ["high", "low", "close"], "func": spr_024_ar_spread_expanding_max},
    "spr_025_hl_spread_daily": {"inputs": ["high", "low", "close"], "func": spr_025_hl_spread_daily},
    "spr_026_hl_spread_roll_mean_5d": {"inputs": ["high", "low", "close"], "func": spr_026_hl_spread_roll_mean_5d},
    "spr_027_hl_spread_roll_mean_21d": {"inputs": ["high", "low", "close"], "func": spr_027_hl_spread_roll_mean_21d},
    "spr_028_hl_spread_roll_mean_63d": {"inputs": ["high", "low", "close"], "func": spr_028_hl_spread_roll_mean_63d},
    "spr_029_hl_spread_roll_mean_252d": {"inputs": ["high", "low", "close"], "func": spr_029_hl_spread_roll_mean_252d},
    "spr_030_hl_spread_zscore_21d": {"inputs": ["high", "low", "close"], "func": spr_030_hl_spread_zscore_21d},
    "spr_031_hl_spread_zscore_63d": {"inputs": ["high", "low", "close"], "func": spr_031_hl_spread_zscore_63d},
    "spr_032_hl_spread_zscore_252d": {"inputs": ["high", "low", "close"], "func": spr_032_hl_spread_zscore_252d},
    "spr_033_hl_spread_pct_rank_21d": {"inputs": ["high", "low", "close"], "func": spr_033_hl_spread_pct_rank_21d},
    "spr_034_hl_spread_pct_rank_63d": {"inputs": ["high", "low", "close"], "func": spr_034_hl_spread_pct_rank_63d},
    "spr_035_hl_spread_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": spr_035_hl_spread_pct_rank_252d},
    "spr_036_hl_spread_expanding_max": {"inputs": ["high", "low", "close"], "func": spr_036_hl_spread_expanding_max},
    "spr_037_roll_spread_21d": {"inputs": ["close"], "func": spr_037_roll_spread_21d},
    "spr_038_roll_spread_63d": {"inputs": ["close"], "func": spr_038_roll_spread_63d},
    "spr_039_roll_spread_126d": {"inputs": ["close"], "func": spr_039_roll_spread_126d},
    "spr_040_roll_spread_252d": {"inputs": ["close"], "func": spr_040_roll_spread_252d},
    "spr_041_roll_spread_21d_zscore_252d": {"inputs": ["close"], "func": spr_041_roll_spread_21d_zscore_252d},
    "spr_042_roll_spread_21d_pct_rank_252d": {"inputs": ["close"], "func": spr_042_roll_spread_21d_pct_rank_252d},
    "spr_043_roll_cov_21d": {"inputs": ["close"], "func": spr_043_roll_cov_21d},
    "spr_044_roll_cov_63d": {"inputs": ["close"], "func": spr_044_roll_cov_63d},
    "spr_045_roll_spread_21d_vs_63d_ratio": {"inputs": ["close"], "func": spr_045_roll_spread_21d_vs_63d_ratio},
    "spr_046_roll_spread_63d_vs_252d_ratio": {"inputs": ["close"], "func": spr_046_roll_spread_63d_vs_252d_ratio},
    "spr_047_roll_spread_21d_ewm_21d": {"inputs": ["close"], "func": spr_047_roll_spread_21d_ewm_21d},
    "spr_048_roll_spread_21d_expanding_max": {"inputs": ["close"], "func": spr_048_roll_spread_21d_expanding_max},
    "spr_049_gap_spread_daily": {"inputs": ["close", "open"], "func": spr_049_gap_spread_daily},
    "spr_050_gap_spread_roll_mean_5d": {"inputs": ["close", "open"], "func": spr_050_gap_spread_roll_mean_5d},
    "spr_051_gap_spread_roll_mean_21d": {"inputs": ["close", "open"], "func": spr_051_gap_spread_roll_mean_21d},
    "spr_052_gap_spread_roll_mean_63d": {"inputs": ["close", "open"], "func": spr_052_gap_spread_roll_mean_63d},
    "spr_053_gap_spread_zscore_21d": {"inputs": ["close", "open"], "func": spr_053_gap_spread_zscore_21d},
    "spr_054_gap_spread_zscore_63d": {"inputs": ["close", "open"], "func": spr_054_gap_spread_zscore_63d},
    "spr_055_gap_spread_pct_rank_63d": {"inputs": ["close", "open"], "func": spr_055_gap_spread_pct_rank_63d},
    "spr_056_gap_spread_pct_rank_252d": {"inputs": ["close", "open"], "func": spr_056_gap_spread_pct_rank_252d},
    "spr_057_gap_vs_hl_spread_ratio_21d": {"inputs": ["high", "low", "close", "open"], "func": spr_057_gap_vs_hl_spread_ratio_21d},
    "spr_058_intraday_vs_overnight_spread_21d": {"inputs": ["high", "low", "close", "open"], "func": spr_058_intraday_vs_overnight_spread_21d},
    "spr_059_gap_down_spread_21d": {"inputs": ["close", "open"], "func": spr_059_gap_down_spread_21d},
    "spr_060_gap_up_spread_21d": {"inputs": ["close", "open"], "func": spr_060_gap_up_spread_21d},
    "spr_061_hl_spread_vs_21d_baseline": {"inputs": ["high", "low", "close"], "func": spr_061_hl_spread_vs_21d_baseline},
    "spr_062_hl_spread_vs_63d_baseline": {"inputs": ["high", "low", "close"], "func": spr_062_hl_spread_vs_63d_baseline},
    "spr_063_hl_spread_vs_252d_baseline": {"inputs": ["high", "low", "close"], "func": spr_063_hl_spread_vs_252d_baseline},
    "spr_064_cs_spread_vs_21d_baseline": {"inputs": ["high", "low"], "func": spr_064_cs_spread_vs_21d_baseline},
    "spr_065_cs_spread_vs_63d_baseline": {"inputs": ["high", "low"], "func": spr_065_cs_spread_vs_63d_baseline},
    "spr_066_cs_spread_vs_252d_baseline": {"inputs": ["high", "low"], "func": spr_066_cs_spread_vs_252d_baseline},
    "spr_067_spread_widening_streak_hl": {"inputs": ["high", "low", "close"], "func": spr_067_spread_widening_streak_hl},
    "spr_068_spread_widening_streak_cs": {"inputs": ["high", "low"], "func": spr_068_spread_widening_streak_cs},
    "spr_069_spread_above_21d_mean_streak": {"inputs": ["high", "low", "close"], "func": spr_069_spread_above_21d_mean_streak},
    "spr_070_spread_above_63d_mean_streak": {"inputs": ["high", "low", "close"], "func": spr_070_spread_above_63d_mean_streak},
    "spr_071_hl_spread_max_21d": {"inputs": ["high", "low", "close"], "func": spr_071_hl_spread_max_21d},
    "spr_072_hl_spread_max_63d": {"inputs": ["high", "low", "close"], "func": spr_072_hl_spread_max_63d},
    "spr_073_hl_spread_median_21d": {"inputs": ["high", "low", "close"], "func": spr_073_hl_spread_median_21d},
    "spr_074_hl_spread_median_63d": {"inputs": ["high", "low", "close"], "func": spr_074_hl_spread_median_63d},
    "spr_075_hl_spread_std_21d": {"inputs": ["high", "low", "close"], "func": spr_075_hl_spread_std_21d},
}
