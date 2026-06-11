"""
38_volatility_regime — Base Features 001-075
Domain: volatility clustering and regime-shift detection — ARCH effects,
        GARCH-style persistence, regime classification (high/low vol state),
        days-in-current-vol-regime, vol regime shift detection, vol persistence.
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_var(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).var()


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


def _ewm_var(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).var()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS) / s.shift(1).clip(lower=_EPS))


def _abs_ret(s: pd.Series) -> pd.Series:
    return _log_ret(s).abs()


def _sq_ret(s: pd.Series) -> pd.Series:
    return _log_ret(s) ** 2


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


def _rolling_corr(a: pd.Series, b: pd.Series, w: int) -> pd.Series:
    return a.rolling(w, min_periods=max(2, w // 2)).corr(b)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Realized volatility levels (short/medium/long) ---

def vrg_001_realized_vol_5d(close: pd.Series) -> pd.Series:
    """5-day realized volatility (std of log-returns, annualized)."""
    r = _log_ret(close)
    return _rolling_std(r, _TD_WEEK) * np.sqrt(_TD_YEAR)


def vrg_002_realized_vol_21d(close: pd.Series) -> pd.Series:
    """21-day realized volatility (annualized)."""
    r = _log_ret(close)
    return _rolling_std(r, _TD_MON) * np.sqrt(_TD_YEAR)


def vrg_003_realized_vol_63d(close: pd.Series) -> pd.Series:
    """63-day realized volatility (annualized)."""
    r = _log_ret(close)
    return _rolling_std(r, _TD_QTR) * np.sqrt(_TD_YEAR)


def vrg_004_realized_vol_126d(close: pd.Series) -> pd.Series:
    """126-day realized volatility (annualized)."""
    r = _log_ret(close)
    return _rolling_std(r, _TD_HALF) * np.sqrt(_TD_YEAR)


def vrg_005_realized_vol_252d(close: pd.Series) -> pd.Series:
    """252-day realized volatility (annualized)."""
    r = _log_ret(close)
    return _rolling_std(r, _TD_YEAR) * np.sqrt(_TD_YEAR)


def vrg_006_fast_slow_vol_ratio_5_63(close: pd.Series) -> pd.Series:
    """Ratio of 5-day to 63-day realized vol — fast/slow regime indicator."""
    return _safe_div(vrg_001_realized_vol_5d(close), vrg_003_realized_vol_63d(close))


def vrg_007_fast_slow_vol_ratio_21_126(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 126-day realized vol — medium/long regime indicator."""
    return _safe_div(vrg_002_realized_vol_21d(close), vrg_004_realized_vol_126d(close))


def vrg_008_fast_slow_vol_ratio_5_252(close: pd.Series) -> pd.Series:
    """Ratio of 5-day to 252-day realized vol — short vs full-year regime."""
    return _safe_div(vrg_001_realized_vol_5d(close), vrg_005_realized_vol_252d(close))


def vrg_009_fast_slow_vol_ratio_21_252(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day realized vol — monthly vs annual regime."""
    return _safe_div(vrg_002_realized_vol_21d(close), vrg_005_realized_vol_252d(close))


def vrg_010_fast_slow_vol_ratio_63_252(close: pd.Series) -> pd.Series:
    """Ratio of 63-day to 252-day realized vol — quarterly vs annual regime."""
    return _safe_div(vrg_003_realized_vol_63d(close), vrg_005_realized_vol_252d(close))


# --- Group B (011-020): High-vol regime flags and days-in-regime ---

def vrg_011_high_vol_regime_flag_21_63(close: pd.Series) -> pd.Series:
    """Flag: 21-day vol exceeds its own 63-day mean (in high-vol regime)."""
    v21 = vrg_002_realized_vol_21d(close)
    v21_avg = _rolling_mean(v21, _TD_QTR)
    return (v21 > v21_avg).astype(float)


def vrg_012_high_vol_regime_flag_21_252(close: pd.Series) -> pd.Series:
    """Flag: 21-day vol exceeds its own 252-day mean (long-run threshold)."""
    v21 = vrg_002_realized_vol_21d(close)
    v21_avg = _rolling_mean(v21, _TD_YEAR)
    return (v21 > v21_avg).astype(float)


def vrg_013_high_vol_regime_flag_5_63(close: pd.Series) -> pd.Series:
    """Flag: 5-day vol exceeds 63-day vol — short burst above medium baseline."""
    return (vrg_001_realized_vol_5d(close) > vrg_003_realized_vol_63d(close)).astype(float)


def vrg_014_days_in_high_vol_regime_21_63(close: pd.Series) -> pd.Series:
    """Days continuously in high-vol regime (21d vol > 63d mean of 21d vol)."""
    cond = vrg_011_high_vol_regime_flag_21_63(close).astype(bool)
    return _consec_streak(cond)


def vrg_015_days_in_high_vol_regime_21_252(close: pd.Series) -> pd.Series:
    """Days continuously in high-vol regime (21d vol > 252d mean of 21d vol)."""
    cond = vrg_012_high_vol_regime_flag_21_252(close).astype(bool)
    return _consec_streak(cond)


def vrg_016_days_in_low_vol_regime_21_252(close: pd.Series) -> pd.Series:
    """Days continuously in low-vol regime (21d vol < 252d mean of 21d vol)."""
    v21 = vrg_002_realized_vol_21d(close)
    v21_avg = _rolling_mean(v21, _TD_YEAR)
    cond = v21 < v21_avg
    return _consec_streak(cond)


def vrg_017_high_vol_days_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days in high-vol regime (21d vs 252d)."""
    flags = vrg_012_high_vol_regime_flag_21_252(close)
    return _rolling_mean(flags, _TD_QTR)


def vrg_018_high_vol_days_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days in high-vol regime (21d vs 252d mean)."""
    flags = vrg_012_high_vol_regime_flag_21_252(close)
    return _rolling_mean(flags, _TD_YEAR)


def vrg_019_vol_percentile_rank_21d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 21d vol within trailing 252d distribution."""
    v21 = vrg_002_realized_vol_21d(close)
    return v21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vrg_020_vol_percentile_rank_5d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5d vol within trailing 252d distribution."""
    v5 = vrg_001_realized_vol_5d(close)
    return v5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (021-030): ARCH effects — autocorrelation of squared/absolute returns ---

def vrg_021_arch_effect_sq_ret_lag1_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d autocorrelation of squared returns at lag-1 (ARCH(1) proxy)."""
    sq = _sq_ret(close)
    return _rolling_corr(sq, sq.shift(1), _TD_MON)


def vrg_022_arch_effect_sq_ret_lag1_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d autocorrelation of squared returns at lag-1."""
    sq = _sq_ret(close)
    return _rolling_corr(sq, sq.shift(1), _TD_QTR)


def vrg_023_arch_effect_sq_ret_lag5_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d autocorrelation of squared returns at lag-5 (weekly ARCH)."""
    sq = _sq_ret(close)
    return _rolling_corr(sq, sq.shift(5), _TD_QTR)


def vrg_024_arch_effect_abs_ret_lag1_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d autocorrelation of absolute returns at lag-1 (volatility clustering)."""
    ab = _abs_ret(close)
    return _rolling_corr(ab, ab.shift(1), _TD_MON)


def vrg_025_arch_effect_abs_ret_lag1_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d autocorrelation of absolute returns at lag-1."""
    ab = _abs_ret(close)
    return _rolling_corr(ab, ab.shift(1), _TD_QTR)


def vrg_026_arch_effect_abs_ret_lag5_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d autocorrelation of absolute returns at lag-5."""
    ab = _abs_ret(close)
    return _rolling_corr(ab, ab.shift(5), _TD_QTR)


def vrg_027_arch_effect_sq_ret_lag1_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d autocorrelation of squared returns at lag-1 (long-horizon clustering)."""
    sq = _sq_ret(close)
    return _rolling_corr(sq, sq.shift(1), _TD_YEAR)


def vrg_028_arch_effect_sq_ret_lag2_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d autocorrelation of squared returns at lag-2."""
    sq = _sq_ret(close)
    return _rolling_corr(sq, sq.shift(2), _TD_QTR)


def vrg_029_arch_effect_sq_ret_lag3_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d autocorrelation of squared returns at lag-3."""
    sq = _sq_ret(close)
    return _rolling_corr(sq, sq.shift(3), _TD_QTR)


def vrg_030_arch_effect_composite_63d(close: pd.Series) -> pd.Series:
    """Mean of lag-1/2/3 autocorrelations of squared returns (composite ARCH signal, 63d)."""
    sq = _sq_ret(close)
    ac1 = _rolling_corr(sq, sq.shift(1), _TD_QTR)
    ac2 = _rolling_corr(sq, sq.shift(2), _TD_QTR)
    ac3 = _rolling_corr(sq, sq.shift(3), _TD_QTR)
    return (ac1 + ac2 + ac3) / 3.0


# --- Group D (031-040): GARCH-style persistence proxies ---

def vrg_031_garch_persistence_ewm5_21(close: pd.Series) -> pd.Series:
    """EWM-vol persistence: ratio of EWM(5) vol to EWM(21) vol — GARCH alpha proxy."""
    sq = _sq_ret(close)
    e5 = _ewm_mean(sq, _TD_WEEK)
    e21 = _ewm_mean(sq, _TD_MON)
    return _safe_div(e5, e21)


def vrg_032_garch_persistence_ewm21_63(close: pd.Series) -> pd.Series:
    """Ratio of EWM(21) variance to EWM(63) variance — medium GARCH persistence."""
    sq = _sq_ret(close)
    e21 = _ewm_mean(sq, _TD_MON)
    e63 = _ewm_mean(sq, _TD_QTR)
    return _safe_div(e21, e63)


def vrg_033_garch_persistence_ewm63_252(close: pd.Series) -> pd.Series:
    """Ratio of EWM(63) variance to EWM(252) variance — long-run GARCH persistence."""
    sq = _sq_ret(close)
    e63 = _ewm_mean(sq, _TD_QTR)
    e252 = _ewm_mean(sq, _TD_YEAR)
    return _safe_div(e63, e252)


def vrg_034_garch_beta_proxy_21d(close: pd.Series) -> pd.Series:
    """Rolling GARCH beta proxy: corr of today's vol with yesterday's vol (21d window)."""
    v5 = vrg_001_realized_vol_5d(close)
    return _rolling_corr(v5, v5.shift(1), _TD_MON)


def vrg_035_garch_beta_proxy_63d(close: pd.Series) -> pd.Series:
    """Rolling GARCH beta proxy: corr of today's vol with yesterday's vol (63d window)."""
    v5 = vrg_001_realized_vol_5d(close)
    return _rolling_corr(v5, v5.shift(1), _TD_QTR)


def vrg_036_ewm_vol_mean_reversion_21d(close: pd.Series) -> pd.Series:
    """EWM vol deviation from 252d mean, normalized — measures distance from long-run level."""
    v_ewm = _ewm_std(close.pct_change(1), _TD_MON) * np.sqrt(_TD_YEAR)
    v_avg = _rolling_mean(v_ewm, _TD_YEAR)
    v_std = _rolling_std(v_ewm, _TD_YEAR)
    return _safe_div(v_ewm - v_avg, v_std)


def vrg_037_ewm_vol_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """63d autocorrelation of EWM(5)-vol series at lag 1 — persistence of the smooth vol."""
    sq = _sq_ret(close)
    ev = _ewm_mean(sq, _TD_WEEK)
    return _rolling_corr(ev, ev.shift(1), _TD_QTR)


def vrg_038_vol_half_life_ewm(close: pd.Series) -> pd.Series:
    """Half-life of vol shock: -ln(2) / ln(corr of EWM vol lag-1, 63d window)."""
    sq = _sq_ret(close)
    ev = _ewm_mean(sq, _TD_WEEK)
    ac1 = _rolling_corr(ev, ev.shift(1), _TD_QTR)
    ac1_clipped = ac1.clip(lower=_EPS, upper=1 - _EPS)
    return -np.log(2.0) / np.log(ac1_clipped)


def vrg_039_vol_persistence_score_composite(close: pd.Series) -> pd.Series:
    """Composite persistence score: mean of lag-1 autocorrs at 21d/63d windows for sq rets."""
    sq = _sq_ret(close)
    ac21 = _rolling_corr(sq, sq.shift(1), _TD_MON)
    ac63 = _rolling_corr(sq, sq.shift(1), _TD_QTR)
    return (ac21 + ac63) / 2.0


def vrg_040_vol_clustering_score_abs_21d(close: pd.Series) -> pd.Series:
    """Clustering score: fraction of days where |ret| exceeds 21d mean |ret|."""
    ab = _abs_ret(close)
    avg_ab = _rolling_mean(ab, _TD_MON)
    above = (ab > avg_ab).astype(float)
    return _rolling_mean(above, _TD_MON)


# --- Group E (041-050): Regime-shift detection (vol breaking its band) ---

def vrg_041_vol_regime_shift_up_flag_21_63(close: pd.Series) -> pd.Series:
    """Flag: 21d vol just crossed above 63d rolling upper band (regime shift up)."""
    v21 = vrg_002_realized_vol_21d(close)
    v_mean = _rolling_mean(v21, _TD_QTR)
    v_std = _rolling_std(v21, _TD_QTR)
    upper = v_mean + v_std
    was_below = v21.shift(1) <= upper.shift(1)
    now_above = v21 > upper
    return (was_below & now_above).astype(float)


def vrg_042_vol_regime_shift_down_flag_21_63(close: pd.Series) -> pd.Series:
    """Flag: 21d vol just crossed below 63d rolling lower band (regime shift down)."""
    v21 = vrg_002_realized_vol_21d(close)
    v_mean = _rolling_mean(v21, _TD_QTR)
    v_std = _rolling_std(v21, _TD_QTR)
    lower = v_mean - v_std
    was_above = v21.shift(1) >= lower.shift(1)
    now_below = v21 < lower
    return (was_above & now_below).astype(float)


def vrg_043_vol_above_1std_band_21_252(close: pd.Series) -> pd.Series:
    """Flag: 21d vol is above its 252d mean + 1 std (extreme high-vol regime)."""
    v21 = vrg_002_realized_vol_21d(close)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    return (v21 > v_mean + v_std).astype(float)


def vrg_044_vol_above_2std_band_21_252(close: pd.Series) -> pd.Series:
    """Flag: 21d vol is above its 252d mean + 2 std (very extreme high-vol regime)."""
    v21 = vrg_002_realized_vol_21d(close)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    return (v21 > v_mean + 2 * v_std).astype(float)


def vrg_045_vol_below_1std_band_21_252(close: pd.Series) -> pd.Series:
    """Flag: 21d vol is below its 252d mean - 1 std (compressed/low-vol regime)."""
    v21 = vrg_002_realized_vol_21d(close)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    return (v21 < v_mean - v_std).astype(float)


def vrg_046_days_above_1std_vol_band_streak(close: pd.Series) -> pd.Series:
    """Consecutive days 21d vol remains above its 252d mean + 1 std band."""
    cond = vrg_043_vol_above_1std_band_21_252(close).astype(bool)
    return _consec_streak(cond)


def vrg_047_days_above_2std_vol_band_streak(close: pd.Series) -> pd.Series:
    """Consecutive days 21d vol remains above its 252d mean + 2 std band."""
    cond = vrg_044_vol_above_2std_band_21_252(close).astype(bool)
    return _consec_streak(cond)


def vrg_048_vol_regime_shift_count_63d(close: pd.Series) -> pd.Series:
    """Count of high-vol regime shifts (upward crossings of 1-std band) in last 63 days."""
    flags = vrg_041_vol_regime_shift_up_flag_21_63(close)
    return _rolling_sum(flags, _TD_QTR)


def vrg_049_vol_regime_shift_count_252d(close: pd.Series) -> pd.Series:
    """Count of high-vol regime shifts (upward crossings of 1-std band) in last 252 days."""
    flags = vrg_041_vol_regime_shift_up_flag_21_63(close)
    return _rolling_sum(flags, _TD_YEAR)


def vrg_050_vol_zscore_21d_in_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 21d vol relative to trailing 252d distribution of 21d vol."""
    v21 = vrg_002_realized_vol_21d(close)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    return _safe_div(v21 - v_mean, v_std)


# --- Group F (051-060): Vol clustering scores and intraday regime ---

def vrg_051_vol_cluster_score_sq_above_avg_21d(close: pd.Series) -> pd.Series:
    """Fraction of days squared return > 21d mean squared return (clustering density)."""
    sq = _sq_ret(close)
    avg_sq = _rolling_mean(sq, _TD_MON)
    above = (sq > avg_sq).astype(float)
    return _rolling_mean(above, _TD_MON)


def vrg_052_vol_cluster_score_sq_above_avg_63d(close: pd.Series) -> pd.Series:
    """Fraction of days squared return > 63d mean squared return."""
    sq = _sq_ret(close)
    avg_sq = _rolling_mean(sq, _TD_QTR)
    above = (sq > avg_sq).astype(float)
    return _rolling_mean(above, _TD_QTR)


def vrg_053_high_vol_run_max_21d(close: pd.Series) -> pd.Series:
    """Max consecutive days of above-average absolute return within 21-day window."""
    ab = _abs_ret(close)
    avg_ab = _rolling_mean(ab, _TD_MON)
    cond = ab > avg_ab
    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)


def vrg_054_high_vol_run_max_63d(close: pd.Series) -> pd.Series:
    """Max consecutive days of above-average absolute return within 63-day window."""
    ab = _abs_ret(close)
    avg_ab = _rolling_mean(ab, _TD_QTR)
    cond = ab > avg_ab
    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def vrg_055_intraday_range_vol_regime_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21d vol of intraday range (H-L)/close — range-based clustering measure."""
    hl_range = (high - low) / close.replace(0, np.nan)
    return _rolling_std(hl_range, _TD_MON)


def vrg_056_intraday_range_vol_ratio_5_63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5d to 63d intraday range volatility — fast vs slow range regime."""
    hl_range = (high - low) / close.replace(0, np.nan)
    r5 = _rolling_std(hl_range, _TD_WEEK)
    r63 = _rolling_std(hl_range, _TD_QTR)
    return _safe_div(r5, r63)


def vrg_057_vol_cluster_ewm_ratio_5_21(close: pd.Series) -> pd.Series:
    """Ratio of EWM(5) abs-return mean to EWM(21) abs-return mean (fast clustering ratio)."""
    ab = _abs_ret(close)
    e5 = _ewm_mean(ab, _TD_WEEK)
    e21 = _ewm_mean(ab, _TD_MON)
    return _safe_div(e5, e21)


def vrg_058_vol_cluster_ewm_ratio_21_63(close: pd.Series) -> pd.Series:
    """Ratio of EWM(21) abs-return mean to EWM(63) abs-return mean."""
    ab = _abs_ret(close)
    e21 = _ewm_mean(ab, _TD_MON)
    e63 = _ewm_mean(ab, _TD_QTR)
    return _safe_div(e21, e63)


def vrg_059_parkinson_vol_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day Parkinson volatility estimator using high-low range."""
    log_hl = (np.log(high.clip(lower=_EPS)) - np.log(low.clip(lower=_EPS))) ** 2
    pk_var = _rolling_mean(log_hl, _TD_WEEK) / (4.0 * np.log(2.0))
    return np.sqrt(pk_var * _TD_YEAR)


def vrg_060_parkinson_vol_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day Parkinson volatility estimator using high-low range."""
    log_hl = (np.log(high.clip(lower=_EPS)) - np.log(low.clip(lower=_EPS))) ** 2
    pk_var = _rolling_mean(log_hl, _TD_MON) / (4.0 * np.log(2.0))
    return np.sqrt(pk_var * _TD_YEAR)


# --- Group G (061-075): Hurst-style persistence, regime duration, vol spread ---

def vrg_061_hurst_proxy_rs_21d(close: pd.Series) -> pd.Series:
    """Hurst-proxy via R/S statistic of log-returns over 21-day rolling window."""
    r = _log_ret(close)
    def _rs(arr):
        if len(arr) < 4:
            return np.nan
        cumdev = np.cumsum(arr - arr.mean())
        rng = cumdev.max() - cumdev.min()
        std = arr.std()
        if std < _EPS:
            return np.nan
        return rng / std
    rs = r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(_rs, raw=True)
    expected_rs = np.sqrt(_TD_MON / 2.0)
    return _safe_div(rs, pd.Series(expected_rs, index=close.index))


def vrg_062_hurst_proxy_rs_63d(close: pd.Series) -> pd.Series:
    """Hurst-proxy via R/S statistic of log-returns over 63-day rolling window."""
    r = _log_ret(close)
    def _rs(arr):
        if len(arr) < 4:
            return np.nan
        cumdev = np.cumsum(arr - arr.mean())
        rng = cumdev.max() - cumdev.min()
        std = arr.std()
        if std < _EPS:
            return np.nan
        return rng / std
    rs = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(_rs, raw=True)
    expected_rs = np.sqrt(_TD_QTR / 2.0)
    return _safe_div(rs, pd.Series(expected_rs, index=close.index))


def vrg_063_vol_hurst_proxy_sq_ret_21d(close: pd.Series) -> pd.Series:
    """Hurst-proxy applied to squared returns (persistence of vol itself) over 21 days."""
    sq = _sq_ret(close)
    def _rs(arr):
        if len(arr) < 4:
            return np.nan
        cumdev = np.cumsum(arr - arr.mean())
        rng = cumdev.max() - cumdev.min()
        std = arr.std()
        if std < _EPS:
            return np.nan
        return rng / std
    return sq.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(_rs, raw=True)


def vrg_064_vol_regime_duration_high_median(close: pd.Series) -> pd.Series:
    """Current high-vol regime duration relative to 252d median high-vol regime duration."""
    dur = vrg_015_days_in_high_vol_regime_21_252(close)
    med = _rolling_median(dur, _TD_YEAR)
    return _safe_div(dur, med)


def vrg_065_vol_regime_duration_low_streak(close: pd.Series) -> pd.Series:
    """Consecutive days in low-vol regime (21d vol < 63d mean of 21d vol)."""
    v21 = vrg_002_realized_vol_21d(close)
    v_avg = _rolling_mean(v21, _TD_QTR)
    cond = v21 < v_avg
    return _consec_streak(cond)


def vrg_066_vol_spread_5d_minus_252d(close: pd.Series) -> pd.Series:
    """Absolute spread: 5d realized vol minus 252d realized vol (regime deviation)."""
    return vrg_001_realized_vol_5d(close) - vrg_005_realized_vol_252d(close)


def vrg_067_vol_spread_21d_minus_252d(close: pd.Series) -> pd.Series:
    """Absolute spread: 21d realized vol minus 252d realized vol."""
    return vrg_002_realized_vol_21d(close) - vrg_005_realized_vol_252d(close)


def vrg_068_vol_spread_63d_minus_252d(close: pd.Series) -> pd.Series:
    """Absolute spread: 63d realized vol minus 252d realized vol."""
    return vrg_003_realized_vol_63d(close) - vrg_005_realized_vol_252d(close)


def vrg_069_vol_spread_pct_5d_minus_252d(close: pd.Series) -> pd.Series:
    """Percentage spread: (5d vol - 252d vol) / 252d vol."""
    v252 = vrg_005_realized_vol_252d(close)
    return _safe_div(vrg_001_realized_vol_5d(close) - v252, v252)


def vrg_070_vol_spread_pct_21d_minus_252d(close: pd.Series) -> pd.Series:
    """Percentage spread: (21d vol - 252d vol) / 252d vol."""
    v252 = vrg_005_realized_vol_252d(close)
    return _safe_div(vrg_002_realized_vol_21d(close) - v252, v252)


def vrg_071_vol_regime_transition_score_63d(close: pd.Series) -> pd.Series:
    """Count of high/low vol regime transitions (sign changes of v21 - v252_mean) in 63d."""
    v21 = vrg_002_realized_vol_21d(close)
    v_avg = _rolling_mean(v21, _TD_YEAR)
    above = (v21 > v_avg).astype(float)
    transitions = above.diff(1).abs()
    return _rolling_sum(transitions, _TD_QTR)


def vrg_072_vol_regime_transition_score_252d(close: pd.Series) -> pd.Series:
    """Count of high/low vol regime transitions in 252d."""
    v21 = vrg_002_realized_vol_21d(close)
    v_avg = _rolling_mean(v21, _TD_YEAR)
    above = (v21 > v_avg).astype(float)
    transitions = above.diff(1).abs()
    return _rolling_sum(transitions, _TD_YEAR)


def vrg_073_vol_persistence_half_life_abs(close: pd.Series) -> pd.Series:
    """Half-life of abs-return autocorrelation shock (63d window lag-1)."""
    ab = _abs_ret(close)
    ac1 = _rolling_corr(ab, ab.shift(1), _TD_QTR)
    ac1_clipped = ac1.clip(lower=_EPS, upper=1 - _EPS)
    return -np.log(2.0) / np.log(ac1_clipped)


def vrg_074_vol_mean_reversion_speed_252d(close: pd.Series) -> pd.Series:
    """Mean-reversion speed: negative OLS slope of vol change on vol level (252d)."""
    v21 = vrg_002_realized_vol_21d(close)
    dv = v21.diff(1)
    return _linslope(dv, _TD_YEAR)


def vrg_075_high_vol_expanding_percentile(close: pd.Series) -> pd.Series:
    """Expanding-history percentile rank of current 21d vol (all-time extremity)."""
    v21 = vrg_002_realized_vol_21d(close)
    return v21.expanding(min_periods=_TD_MON).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_REGIME_REGISTRY_001_075 = {
    "vrg_001_realized_vol_5d": {"inputs": ["close"], "func": vrg_001_realized_vol_5d},
    "vrg_002_realized_vol_21d": {"inputs": ["close"], "func": vrg_002_realized_vol_21d},
    "vrg_003_realized_vol_63d": {"inputs": ["close"], "func": vrg_003_realized_vol_63d},
    "vrg_004_realized_vol_126d": {"inputs": ["close"], "func": vrg_004_realized_vol_126d},
    "vrg_005_realized_vol_252d": {"inputs": ["close"], "func": vrg_005_realized_vol_252d},
    "vrg_006_fast_slow_vol_ratio_5_63": {"inputs": ["close"], "func": vrg_006_fast_slow_vol_ratio_5_63},
    "vrg_007_fast_slow_vol_ratio_21_126": {"inputs": ["close"], "func": vrg_007_fast_slow_vol_ratio_21_126},
    "vrg_008_fast_slow_vol_ratio_5_252": {"inputs": ["close"], "func": vrg_008_fast_slow_vol_ratio_5_252},
    "vrg_009_fast_slow_vol_ratio_21_252": {"inputs": ["close"], "func": vrg_009_fast_slow_vol_ratio_21_252},
    "vrg_010_fast_slow_vol_ratio_63_252": {"inputs": ["close"], "func": vrg_010_fast_slow_vol_ratio_63_252},
    "vrg_011_high_vol_regime_flag_21_63": {"inputs": ["close"], "func": vrg_011_high_vol_regime_flag_21_63},
    "vrg_012_high_vol_regime_flag_21_252": {"inputs": ["close"], "func": vrg_012_high_vol_regime_flag_21_252},
    "vrg_013_high_vol_regime_flag_5_63": {"inputs": ["close"], "func": vrg_013_high_vol_regime_flag_5_63},
    "vrg_014_days_in_high_vol_regime_21_63": {"inputs": ["close"], "func": vrg_014_days_in_high_vol_regime_21_63},
    "vrg_015_days_in_high_vol_regime_21_252": {"inputs": ["close"], "func": vrg_015_days_in_high_vol_regime_21_252},
    "vrg_016_days_in_low_vol_regime_21_252": {"inputs": ["close"], "func": vrg_016_days_in_low_vol_regime_21_252},
    "vrg_017_high_vol_days_fraction_63d": {"inputs": ["close"], "func": vrg_017_high_vol_days_fraction_63d},
    "vrg_018_high_vol_days_fraction_252d": {"inputs": ["close"], "func": vrg_018_high_vol_days_fraction_252d},
    "vrg_019_vol_percentile_rank_21d_in_252d": {"inputs": ["close"], "func": vrg_019_vol_percentile_rank_21d_in_252d},
    "vrg_020_vol_percentile_rank_5d_in_252d": {"inputs": ["close"], "func": vrg_020_vol_percentile_rank_5d_in_252d},
    "vrg_021_arch_effect_sq_ret_lag1_21d": {"inputs": ["close"], "func": vrg_021_arch_effect_sq_ret_lag1_21d},
    "vrg_022_arch_effect_sq_ret_lag1_63d": {"inputs": ["close"], "func": vrg_022_arch_effect_sq_ret_lag1_63d},
    "vrg_023_arch_effect_sq_ret_lag5_63d": {"inputs": ["close"], "func": vrg_023_arch_effect_sq_ret_lag5_63d},
    "vrg_024_arch_effect_abs_ret_lag1_21d": {"inputs": ["close"], "func": vrg_024_arch_effect_abs_ret_lag1_21d},
    "vrg_025_arch_effect_abs_ret_lag1_63d": {"inputs": ["close"], "func": vrg_025_arch_effect_abs_ret_lag1_63d},
    "vrg_026_arch_effect_abs_ret_lag5_63d": {"inputs": ["close"], "func": vrg_026_arch_effect_abs_ret_lag5_63d},
    "vrg_027_arch_effect_sq_ret_lag1_252d": {"inputs": ["close"], "func": vrg_027_arch_effect_sq_ret_lag1_252d},
    "vrg_028_arch_effect_sq_ret_lag2_63d": {"inputs": ["close"], "func": vrg_028_arch_effect_sq_ret_lag2_63d},
    "vrg_029_arch_effect_sq_ret_lag3_63d": {"inputs": ["close"], "func": vrg_029_arch_effect_sq_ret_lag3_63d},
    "vrg_030_arch_effect_composite_63d": {"inputs": ["close"], "func": vrg_030_arch_effect_composite_63d},
    "vrg_031_garch_persistence_ewm5_21": {"inputs": ["close"], "func": vrg_031_garch_persistence_ewm5_21},
    "vrg_032_garch_persistence_ewm21_63": {"inputs": ["close"], "func": vrg_032_garch_persistence_ewm21_63},
    "vrg_033_garch_persistence_ewm63_252": {"inputs": ["close"], "func": vrg_033_garch_persistence_ewm63_252},
    "vrg_034_garch_beta_proxy_21d": {"inputs": ["close"], "func": vrg_034_garch_beta_proxy_21d},
    "vrg_035_garch_beta_proxy_63d": {"inputs": ["close"], "func": vrg_035_garch_beta_proxy_63d},
    "vrg_036_ewm_vol_mean_reversion_21d": {"inputs": ["close"], "func": vrg_036_ewm_vol_mean_reversion_21d},
    "vrg_037_ewm_vol_autocorr_lag1_63d": {"inputs": ["close"], "func": vrg_037_ewm_vol_autocorr_lag1_63d},
    "vrg_038_vol_half_life_ewm": {"inputs": ["close"], "func": vrg_038_vol_half_life_ewm},
    "vrg_039_vol_persistence_score_composite": {"inputs": ["close"], "func": vrg_039_vol_persistence_score_composite},
    "vrg_040_vol_clustering_score_abs_21d": {"inputs": ["close"], "func": vrg_040_vol_clustering_score_abs_21d},
    "vrg_041_vol_regime_shift_up_flag_21_63": {"inputs": ["close"], "func": vrg_041_vol_regime_shift_up_flag_21_63},
    "vrg_042_vol_regime_shift_down_flag_21_63": {"inputs": ["close"], "func": vrg_042_vol_regime_shift_down_flag_21_63},
    "vrg_043_vol_above_1std_band_21_252": {"inputs": ["close"], "func": vrg_043_vol_above_1std_band_21_252},
    "vrg_044_vol_above_2std_band_21_252": {"inputs": ["close"], "func": vrg_044_vol_above_2std_band_21_252},
    "vrg_045_vol_below_1std_band_21_252": {"inputs": ["close"], "func": vrg_045_vol_below_1std_band_21_252},
    "vrg_046_days_above_1std_vol_band_streak": {"inputs": ["close"], "func": vrg_046_days_above_1std_vol_band_streak},
    "vrg_047_days_above_2std_vol_band_streak": {"inputs": ["close"], "func": vrg_047_days_above_2std_vol_band_streak},
    "vrg_048_vol_regime_shift_count_63d": {"inputs": ["close"], "func": vrg_048_vol_regime_shift_count_63d},
    "vrg_049_vol_regime_shift_count_252d": {"inputs": ["close"], "func": vrg_049_vol_regime_shift_count_252d},
    "vrg_050_vol_zscore_21d_in_252d": {"inputs": ["close"], "func": vrg_050_vol_zscore_21d_in_252d},
    "vrg_051_vol_cluster_score_sq_above_avg_21d": {"inputs": ["close"], "func": vrg_051_vol_cluster_score_sq_above_avg_21d},
    "vrg_052_vol_cluster_score_sq_above_avg_63d": {"inputs": ["close"], "func": vrg_052_vol_cluster_score_sq_above_avg_63d},
    "vrg_053_high_vol_run_max_21d": {"inputs": ["close"], "func": vrg_053_high_vol_run_max_21d},
    "vrg_054_high_vol_run_max_63d": {"inputs": ["close"], "func": vrg_054_high_vol_run_max_63d},
    "vrg_055_intraday_range_vol_regime_21d": {"inputs": ["close", "high", "low"], "func": vrg_055_intraday_range_vol_regime_21d},
    "vrg_056_intraday_range_vol_ratio_5_63": {"inputs": ["close", "high", "low"], "func": vrg_056_intraday_range_vol_ratio_5_63},
    "vrg_057_vol_cluster_ewm_ratio_5_21": {"inputs": ["close"], "func": vrg_057_vol_cluster_ewm_ratio_5_21},
    "vrg_058_vol_cluster_ewm_ratio_21_63": {"inputs": ["close"], "func": vrg_058_vol_cluster_ewm_ratio_21_63},
    "vrg_059_parkinson_vol_5d": {"inputs": ["close", "high", "low"], "func": vrg_059_parkinson_vol_5d},
    "vrg_060_parkinson_vol_21d": {"inputs": ["close", "high", "low"], "func": vrg_060_parkinson_vol_21d},
    "vrg_061_hurst_proxy_rs_21d": {"inputs": ["close"], "func": vrg_061_hurst_proxy_rs_21d},
    "vrg_062_hurst_proxy_rs_63d": {"inputs": ["close"], "func": vrg_062_hurst_proxy_rs_63d},
    "vrg_063_vol_hurst_proxy_sq_ret_21d": {"inputs": ["close"], "func": vrg_063_vol_hurst_proxy_sq_ret_21d},
    "vrg_064_vol_regime_duration_high_median": {"inputs": ["close"], "func": vrg_064_vol_regime_duration_high_median},
    "vrg_065_vol_regime_duration_low_streak": {"inputs": ["close"], "func": vrg_065_vol_regime_duration_low_streak},
    "vrg_066_vol_spread_5d_minus_252d": {"inputs": ["close"], "func": vrg_066_vol_spread_5d_minus_252d},
    "vrg_067_vol_spread_21d_minus_252d": {"inputs": ["close"], "func": vrg_067_vol_spread_21d_minus_252d},
    "vrg_068_vol_spread_63d_minus_252d": {"inputs": ["close"], "func": vrg_068_vol_spread_63d_minus_252d},
    "vrg_069_vol_spread_pct_5d_minus_252d": {"inputs": ["close"], "func": vrg_069_vol_spread_pct_5d_minus_252d},
    "vrg_070_vol_spread_pct_21d_minus_252d": {"inputs": ["close"], "func": vrg_070_vol_spread_pct_21d_minus_252d},
    "vrg_071_vol_regime_transition_score_63d": {"inputs": ["close"], "func": vrg_071_vol_regime_transition_score_63d},
    "vrg_072_vol_regime_transition_score_252d": {"inputs": ["close"], "func": vrg_072_vol_regime_transition_score_252d},
    "vrg_073_vol_persistence_half_life_abs": {"inputs": ["close"], "func": vrg_073_vol_persistence_half_life_abs},
    "vrg_074_vol_mean_reversion_speed_252d": {"inputs": ["close"], "func": vrg_074_vol_mean_reversion_speed_252d},
    "vrg_075_high_vol_expanding_percentile": {"inputs": ["close"], "func": vrg_075_high_vol_expanding_percentile},
}
