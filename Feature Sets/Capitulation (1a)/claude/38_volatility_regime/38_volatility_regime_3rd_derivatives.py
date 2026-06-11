"""
38_volatility_regime — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative vol-regime features — acceleration of velocity
        in clustering, persistence, and regime-shift signals.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def vrg_drv3_001_fast_slow_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of fast/slow vol ratio (5d/63d) — acceleration of regime signal."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    ratio = _safe_div(v5, v63)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_002_realized_vol_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 21d realized vol (acceleration of monthly vol velocity)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vel = v21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_003_arch_sq_lag1_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 63d ARCH(1) autocorrelation (jerk in clustering persistence)."""
    sq = _sq_ret(close)
    ac1 = _rolling_corr(sq, sq.shift(1), _TD_QTR)
    vel = ac1.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_004_garch_ewm_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of GARCH persistence EWM ratio (jerk in alpha persistence)."""
    sq = _sq_ret(close)
    e5 = _ewm_mean(sq, _TD_WEEK)
    e21 = _ewm_mean(sq, _TD_MON)
    ratio = _safe_div(e5, e21)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_005_vol_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 21d vol z-score (acceleration of extremity score)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    z = _safe_div(v21 - _rolling_mean(v21, _TD_YEAR), _rolling_std(v21, _TD_YEAR))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_006_vol_spread_21_252_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of (21d - 252d) vol spread (jerk in term structure shift)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v252 = _rolling_std(_log_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    spread = v21 - v252
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_007_days_in_regime_5d_diff_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of high-vol regime duration."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    cond = v21 > _rolling_mean(v21, _TD_YEAR)
    dur = _consec_streak(cond)
    vel = dur.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vrg_drv3_008_vol_above_1std_streak_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of days-above-1std-band streak (acceleration of extreme regime)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    cond = v21 > (v_mean + v_std)
    dur = _consec_streak(cond)
    vel = dur.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_009_arch_abs_lag1_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 63d abs-return autocorrelation at lag-1 (jerk in clustering)."""
    ab = _abs_ret(close)
    ac1 = _rolling_corr(ab, ab.shift(1), _TD_QTR)
    vel = ac1.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_010_downside_vol_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 21d downside vol (acceleration of fear-vol velocity)."""
    r = _log_ret(close)
    dv = _rolling_std(r.where(r < 0, 0.0), _TD_MON) * np.sqrt(_TD_YEAR)
    vel = dv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_011_vol_skew_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 21d downside/upside vol ratio (jerk in fear asymmetry)."""
    r = _log_ret(close)
    dv = _rolling_std(r.where(r < 0, 0.0), _TD_MON) * np.sqrt(_TD_YEAR)
    uv = _rolling_std(r.where(r > 0, 0.0), _TD_MON) * np.sqrt(_TD_YEAR)
    ratio = _safe_div(dv, uv)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_012_vol_cluster_sq_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of vol clustering score (jerk in clustering density change)."""
    sq = _sq_ret(close)
    avg_sq = _rolling_mean(sq, _TD_MON)
    score = (sq > avg_sq).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_013_vol_regime_transition_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 63d regime transition count (jerk in instability)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    above = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    trans63 = _rolling_sum(above.diff(1).abs(), _TD_QTR)
    vel = trans63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_014_vol_21d_slope_63d_5d_diff_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of vol trend (trend-of-trend acceleration)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    slp = _linslope(v21, _TD_QTR)
    vel = slp.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vrg_drv3_015_vol_breakout_magnitude_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of vol-above-1std magnitude (jerk in extreme regime depth)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    excess = (v21 - (v_mean + v_std)).clip(lower=0)
    mag = _safe_div(excess, v_std)
    vel = mag.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_016_high_vol_fraction_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of the 21d-change in 63d high-vol fraction (jerk in prevalence shift)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    above = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    frac63 = _rolling_mean(above, _TD_QTR)
    vel21 = frac63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vrg_drv3_017_vol_consensus_score_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 3-timeframe vol regime consensus (jerk in regime agreement)."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    score = ((v5 > _rolling_mean(v5, _TD_YEAR)).astype(float) +
             (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float) +
             (v63 > _rolling_mean(v63, _TD_YEAR)).astype(float))
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_018_vol_half_life_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of EWM vol persistence half-life (jerk in clustering decay rate)."""
    sq = _sq_ret(close)
    ev = _ewm_mean(sq, _TD_WEEK)
    ac1 = _rolling_corr(ev, ev.shift(1), _TD_QTR)
    ac1_c = ac1.clip(lower=_EPS, upper=1 - _EPS)
    hl = -np.log(2.0) / np.log(ac1_c)
    vel = hl.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_019_vol_max_to_mean_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 21d max-to-mean abs-return ratio (jerk in spike intensity)."""
    ab = _abs_ret(close)
    ratio = _safe_div(ab.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max(),
                      _rolling_mean(ab, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_020_vol_spread_21d_252d_5d_diff_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of vol term spread."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v252 = _rolling_std(_log_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    vel = (v21 - v252).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vrg_drv3_021_return_skewness_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 21d return skewness (acceleration of tail-regime shift)."""
    r = _log_ret(close)
    skew = r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).skew()
    vel = skew.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_022_vol_persistence_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 63d/252d high-vol fraction ratio (jerk in recency bias)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    above = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    frac63 = _rolling_mean(above, _TD_QTR)
    frac252 = _rolling_mean(above, _TD_YEAR)
    ratio = _safe_div(frac63, frac252)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_023_garch_ewm21_63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of EWM(21)/EWM(63) variance ratio (jerk in medium persistence)."""
    sq = _sq_ret(close)
    e21 = _ewm_mean(sq, _TD_MON)
    e63 = _ewm_mean(sq, _TD_QTR)
    ratio = _safe_div(e21, e63)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_024_vol_cluster_ewm_ratio_5_21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of EWM(5)/EWM(21) abs-return ratio (jerk in fast cluster signal)."""
    ab = _abs_ret(close)
    e5 = _ewm_mean(ab, _TD_WEEK)
    e21 = _ewm_mean(ab, _TD_MON)
    ratio = _safe_div(e5, e21)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_drv3_025_vol_regime_stability_5d_diff_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of 5d-velocity of regime stability score (trend in stability)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    above = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    trans63 = _rolling_sum(above.diff(1).abs(), _TD_QTR)
    stability = _safe_div(pd.Series(1.0, index=close.index), trans63 + 1)
    vel = stability.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_REGIME_REGISTRY_3RD_DERIVATIVES = {
    "vrg_drv3_001_fast_slow_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_001_fast_slow_ratio_5d_diff_5d_diff},
    "vrg_drv3_002_realized_vol_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_002_realized_vol_21d_5d_diff_5d_diff},
    "vrg_drv3_003_arch_sq_lag1_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_003_arch_sq_lag1_63d_5d_diff_5d_diff},
    "vrg_drv3_004_garch_ewm_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_004_garch_ewm_ratio_5d_diff_5d_diff},
    "vrg_drv3_005_vol_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_005_vol_zscore_5d_diff_5d_diff},
    "vrg_drv3_006_vol_spread_21_252_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_006_vol_spread_21_252_5d_diff_5d_diff},
    "vrg_drv3_007_days_in_regime_5d_diff_slope": {"inputs": ["close"], "func": vrg_drv3_007_days_in_regime_5d_diff_slope},
    "vrg_drv3_008_vol_above_1std_streak_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_008_vol_above_1std_streak_5d_diff_5d_diff},
    "vrg_drv3_009_arch_abs_lag1_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_009_arch_abs_lag1_5d_diff_5d_diff},
    "vrg_drv3_010_downside_vol_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_010_downside_vol_5d_diff_5d_diff},
    "vrg_drv3_011_vol_skew_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_011_vol_skew_ratio_5d_diff_5d_diff},
    "vrg_drv3_012_vol_cluster_sq_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_012_vol_cluster_sq_5d_diff_5d_diff},
    "vrg_drv3_013_vol_regime_transition_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_013_vol_regime_transition_5d_diff_5d_diff},
    "vrg_drv3_014_vol_21d_slope_63d_5d_diff_slope": {"inputs": ["close"], "func": vrg_drv3_014_vol_21d_slope_63d_5d_diff_slope},
    "vrg_drv3_015_vol_breakout_magnitude_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_015_vol_breakout_magnitude_5d_diff_5d_diff},
    "vrg_drv3_016_high_vol_fraction_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_016_high_vol_fraction_63d_21d_diff_5d_diff},
    "vrg_drv3_017_vol_consensus_score_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_017_vol_consensus_score_5d_diff_5d_diff},
    "vrg_drv3_018_vol_half_life_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_018_vol_half_life_5d_diff_5d_diff},
    "vrg_drv3_019_vol_max_to_mean_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_019_vol_max_to_mean_ratio_5d_diff_5d_diff},
    "vrg_drv3_020_vol_spread_21d_252d_5d_diff_slope": {"inputs": ["close"], "func": vrg_drv3_020_vol_spread_21d_252d_5d_diff_slope},
    "vrg_drv3_021_return_skewness_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_021_return_skewness_5d_diff_5d_diff},
    "vrg_drv3_022_vol_persistence_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_022_vol_persistence_ratio_5d_diff_5d_diff},
    "vrg_drv3_023_garch_ewm21_63_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_023_garch_ewm21_63_5d_diff_5d_diff},
    "vrg_drv3_024_vol_cluster_ewm_ratio_5_21_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_drv3_024_vol_cluster_ewm_ratio_5_21_5d_diff_5d_diff},
    "vrg_drv3_025_vol_regime_stability_5d_diff_slope": {"inputs": ["close"], "func": vrg_drv3_025_vol_regime_stability_5d_diff_slope},
}
