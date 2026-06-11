"""
38_volatility_regime — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base vol-regime features — velocity / acceleration of
        clustering, persistence, and regime-shift signals.
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


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


def _rolling_corr(a: pd.Series, b: pd.Series, w: int) -> pd.Series:
    return a.rolling(w, min_periods=max(2, w // 2)).corr(b)


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vrg_drv2_001_fast_slow_vol_ratio_5_63_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of fast/slow vol ratio (5d/63d) — velocity of regime shift signal."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    ratio = _safe_div(v5, v63)
    return ratio.diff(_TD_WEEK)


def vrg_drv2_002_fast_slow_vol_ratio_21_252_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d/252d vol ratio — velocity of monthly-vs-annual regime divergence."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v252 = _rolling_std(_log_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    ratio = _safe_div(v21, v252)
    return ratio.diff(_TD_WEEK)


def vrg_drv2_003_realized_vol_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d realized vol (velocity of monthly vol level)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return v21.diff(_TD_WEEK)


def vrg_drv2_004_realized_vol_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21d diff of 21d realized vol (monthly velocity of monthly vol)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return v21.diff(_TD_MON)


def vrg_drv2_005_arch_effect_sq_lag1_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 63d autocorrelation of squared returns at lag-1 (ARCH velocity)."""
    sq = _sq_ret(close)
    ac1 = _rolling_corr(sq, sq.shift(1), _TD_QTR)
    return ac1.diff(_TD_WEEK)


def vrg_drv2_006_arch_effect_sq_lag1_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21d diff of 63d autocorrelation of squared returns at lag-1."""
    sq = _sq_ret(close)
    ac1 = _rolling_corr(sq, sq.shift(1), _TD_QTR)
    return ac1.diff(_TD_MON)


def vrg_drv2_007_garch_persistence_ewm5_21_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of EWM(5)/EWM(21) variance ratio (GARCH alpha persistence velocity)."""
    sq = _sq_ret(close)
    e5 = _ewm_mean(sq, _TD_WEEK)
    e21 = _ewm_mean(sq, _TD_MON)
    ratio = _safe_div(e5, e21)
    return ratio.diff(_TD_WEEK)


def vrg_drv2_008_vol_zscore_21d_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d vol z-score within 252d (velocity of extremity score)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    z = _safe_div(v21 - _rolling_mean(v21, _TD_YEAR), _rolling_std(v21, _TD_YEAR))
    return z.diff(_TD_WEEK)


def vrg_drv2_009_days_in_high_vol_regime_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of consecutive-high-vol-regime days (velocity of regime duration growth)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    cond = v21 > _rolling_mean(v21, _TD_YEAR)
    dur = _consec_streak(cond)
    return dur.diff(_TD_WEEK)


def vrg_drv2_010_vol_above_1std_band_streak_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of days-above-1std-band streak (velocity of extreme-regime duration)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    cond = v21 > (v_mean + v_std)
    dur = _consec_streak(cond)
    return dur.diff(_TD_WEEK)


def vrg_drv2_011_vol_spread_21d_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of (21d vol - 252d vol) spread — velocity of term-structure shift."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v252 = _rolling_std(_log_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    spread = v21 - v252
    return spread.diff(_TD_WEEK)


def vrg_drv2_012_vol_spread_21d_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21d diff of (21d vol - 252d vol) spread."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v252 = _rolling_std(_log_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    spread = v21 - v252
    return spread.diff(_TD_MON)


def vrg_drv2_013_arch_abs_lag1_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 63d autocorrelation of absolute returns at lag-1 (clustering velocity)."""
    ab = _abs_ret(close)
    ac1 = _rolling_corr(ab, ab.shift(1), _TD_QTR)
    return ac1.diff(_TD_WEEK)


def vrg_drv2_014_vol_regime_transition_count_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 63d regime transition count (acceleration of regime instability)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    above = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    trans63 = _rolling_sum(above.diff(1).abs(), _TD_QTR)
    return trans63.diff(_TD_WEEK)


def vrg_drv2_015_downside_vol_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d downside realized vol (velocity of fear-vol)."""
    r = _log_ret(close)
    down_r = r.where(r < 0, 0.0)
    dv = _rolling_std(down_r, _TD_MON) * np.sqrt(_TD_YEAR)
    return dv.diff(_TD_WEEK)


def vrg_drv2_016_vol_skew_down_up_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d downside/upside vol ratio (velocity of asymmetry shift)."""
    r = _log_ret(close)
    dv = _rolling_std(r.where(r < 0, 0.0), _TD_MON) * np.sqrt(_TD_YEAR)
    uv = _rolling_std(r.where(r > 0, 0.0), _TD_MON) * np.sqrt(_TD_YEAR)
    ratio = _safe_div(dv, uv)
    return ratio.diff(_TD_WEEK)


def vrg_drv2_017_vol_cluster_score_sq_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d vol clustering score (fraction of days sq-ret > avg sq-ret)."""
    sq = _sq_ret(close)
    avg_sq = _rolling_mean(sq, _TD_MON)
    score = (sq > avg_sq).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return score.diff(_TD_WEEK)


def vrg_drv2_018_vol_half_life_ewm_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of vol persistence half-life from EWM autocorrelation."""
    sq = _sq_ret(close)
    ev = _ewm_mean(sq, _TD_WEEK)
    ac1 = _rolling_corr(ev, ev.shift(1), _TD_QTR)
    ac1_c = ac1.clip(lower=_EPS, upper=1 - _EPS)
    hl = -np.log(2.0) / np.log(ac1_c)
    return hl.diff(_TD_WEEK)


def vrg_drv2_019_vol_21d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of OLS slope of 21d vol over 63d (velocity of vol trend change)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    slp = _linslope(v21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vrg_drv2_020_high_vol_fraction_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21d diff of 63d high-vol-day fraction (monthly change in regime prevalence)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    above = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    frac63 = _rolling_mean(above, _TD_QTR)
    return frac63.diff(_TD_MON)


def vrg_drv2_021_vol_regime_consensus_score_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 3-timeframe vol regime consensus score (velocity of agreement)."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    score = ((v5 > _rolling_mean(v5, _TD_YEAR)).astype(float) +
             (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float) +
             (v63 > _rolling_mean(v63, _TD_YEAR)).astype(float))
    return score.diff(_TD_WEEK)


def vrg_drv2_022_vol_max_to_mean_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d max-to-mean abs-return ratio (velocity of spike intensity)."""
    ab = _abs_ret(close)
    ratio = _safe_div(ab.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max(),
                      _rolling_mean(ab, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vrg_drv2_023_vol_breakout_magnitude_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of vol-above-1std-band magnitude (velocity of extreme regime depth)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    excess = (v21 - (v_mean + v_std)).clip(lower=0)
    mag = _safe_div(excess, v_std)
    return mag.diff(_TD_WEEK)


def vrg_drv2_024_vol_regime_persistence_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 63d/252d high-vol fraction ratio (velocity of recency vs history)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    above = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    frac63 = _rolling_mean(above, _TD_QTR)
    frac252 = _rolling_mean(above, _TD_YEAR)
    ratio = _safe_div(frac63, frac252)
    return ratio.diff(_TD_WEEK)


def vrg_drv2_025_return_skewness_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d return skewness (velocity of tail-regime shift)."""
    r = _log_ret(close)
    skew = r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).skew()
    return skew.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_REGIME_REGISTRY_2ND_DERIVATIVES = {
    "vrg_drv2_001_fast_slow_vol_ratio_5_63_5d_diff": {"inputs": ["close"], "func": vrg_drv2_001_fast_slow_vol_ratio_5_63_5d_diff},
    "vrg_drv2_002_fast_slow_vol_ratio_21_252_5d_diff": {"inputs": ["close"], "func": vrg_drv2_002_fast_slow_vol_ratio_21_252_5d_diff},
    "vrg_drv2_003_realized_vol_21d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_003_realized_vol_21d_5d_diff},
    "vrg_drv2_004_realized_vol_21d_21d_diff": {"inputs": ["close"], "func": vrg_drv2_004_realized_vol_21d_21d_diff},
    "vrg_drv2_005_arch_effect_sq_lag1_63d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_005_arch_effect_sq_lag1_63d_5d_diff},
    "vrg_drv2_006_arch_effect_sq_lag1_63d_21d_diff": {"inputs": ["close"], "func": vrg_drv2_006_arch_effect_sq_lag1_63d_21d_diff},
    "vrg_drv2_007_garch_persistence_ewm5_21_5d_diff": {"inputs": ["close"], "func": vrg_drv2_007_garch_persistence_ewm5_21_5d_diff},
    "vrg_drv2_008_vol_zscore_21d_252d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_008_vol_zscore_21d_252d_5d_diff},
    "vrg_drv2_009_days_in_high_vol_regime_5d_diff": {"inputs": ["close"], "func": vrg_drv2_009_days_in_high_vol_regime_5d_diff},
    "vrg_drv2_010_vol_above_1std_band_streak_5d_diff": {"inputs": ["close"], "func": vrg_drv2_010_vol_above_1std_band_streak_5d_diff},
    "vrg_drv2_011_vol_spread_21d_252d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_011_vol_spread_21d_252d_5d_diff},
    "vrg_drv2_012_vol_spread_21d_252d_21d_diff": {"inputs": ["close"], "func": vrg_drv2_012_vol_spread_21d_252d_21d_diff},
    "vrg_drv2_013_arch_abs_lag1_63d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_013_arch_abs_lag1_63d_5d_diff},
    "vrg_drv2_014_vol_regime_transition_count_63d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_014_vol_regime_transition_count_63d_5d_diff},
    "vrg_drv2_015_downside_vol_21d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_015_downside_vol_21d_5d_diff},
    "vrg_drv2_016_vol_skew_down_up_ratio_21d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_016_vol_skew_down_up_ratio_21d_5d_diff},
    "vrg_drv2_017_vol_cluster_score_sq_21d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_017_vol_cluster_score_sq_21d_5d_diff},
    "vrg_drv2_018_vol_half_life_ewm_5d_diff": {"inputs": ["close"], "func": vrg_drv2_018_vol_half_life_ewm_5d_diff},
    "vrg_drv2_019_vol_21d_slope_63d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_019_vol_21d_slope_63d_5d_diff},
    "vrg_drv2_020_high_vol_fraction_63d_21d_diff": {"inputs": ["close"], "func": vrg_drv2_020_high_vol_fraction_63d_21d_diff},
    "vrg_drv2_021_vol_regime_consensus_score_5d_diff": {"inputs": ["close"], "func": vrg_drv2_021_vol_regime_consensus_score_5d_diff},
    "vrg_drv2_022_vol_max_to_mean_ratio_21d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_022_vol_max_to_mean_ratio_21d_5d_diff},
    "vrg_drv2_023_vol_breakout_magnitude_5d_diff": {"inputs": ["close"], "func": vrg_drv2_023_vol_breakout_magnitude_5d_diff},
    "vrg_drv2_024_vol_regime_persistence_ratio_5d_diff": {"inputs": ["close"], "func": vrg_drv2_024_vol_regime_persistence_ratio_5d_diff},
    "vrg_drv2_025_return_skewness_21d_5d_diff": {"inputs": ["close"], "func": vrg_drv2_025_return_skewness_21d_5d_diff},
}
