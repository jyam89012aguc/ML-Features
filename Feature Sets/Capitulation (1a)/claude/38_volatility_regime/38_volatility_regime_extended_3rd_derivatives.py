"""
38_volatility_regime — Extended 3rd Derivatives (Features vrg_extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative vol-regime concepts — acceleration
        of velocity in vol-of-vol states, Yang-Zhang, GARCH proxies, volume-weighted vol,
        extreme return counts, and extended regime duration signals.
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


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative extended concept

def vrg_extdrv3_001_vol_of_vol_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of vol-of-vol (21d/63d) — jerk in vol turbulence velocity."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vov = _rolling_std(v21, _TD_QTR)
    vel = vov.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_002_vol_of_vol_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of vol-of-vol z-score (jerk in turbulence extremity)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vov = _rolling_std(v21, _TD_QTR)
    z = _safe_div(vov - _rolling_mean(vov, _TD_YEAR), _rolling_std(vov, _TD_YEAR))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_003_realized_vol_10d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 10-day realized vol (acceleration of bi-weekly vol)."""
    v10 = _rolling_std(_log_ret(close), 10) * np.sqrt(_TD_YEAR)
    vel = v10.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_004_vol_ratio_10d_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 10d/63d vol ratio (jerk in bi-weekly vs quarterly regime)."""
    v10 = _rolling_std(_log_ret(close), 10) * np.sqrt(_TD_YEAR)
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    ratio = _safe_div(v10, v63)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_005_garch_ewm2_10_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of EWM(2)/EWM(10) GARCH ratio (jerk in ultra-fast persistence)."""
    sq = _sq_ret(close)
    ratio = _safe_div(_ewm_mean(sq, 2), _ewm_mean(sq, 10))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_006_garch_ewm10_63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of EWM(10)/EWM(63) GARCH ratio (jerk in bi-weekly/quarterly persistence)."""
    sq = _sq_ret(close)
    ratio = _safe_div(_ewm_mean(sq, 10), _ewm_mean(sq, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_007_yang_zhang_vol_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5d diff of 21d Yang-Zhang vol (jerk in YZ estimator level)."""
    k = 0.34 / (1.34 + (_TD_MON + 1) / (_TD_MON - 1))
    log_oc = np.log(open.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_hc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_ho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_lc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_lo = np.log(low.clip(lower=_EPS) / open.clip(lower=_EPS))
    rs = log_hc * log_ho + log_lc * log_lo
    yz_var = (_rolling_var(log_oc, _TD_MON) + k * _rolling_var(log_co, _TD_MON)
              + (1 - k) * _rolling_mean(rs, _TD_MON))
    yz = np.sqrt(yz_var.clip(lower=0) * _TD_YEAR)
    vel = yz.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_008_parkinson_vol_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5d diff of 63d Parkinson vol (jerk in quarterly range-based vol)."""
    log_hl = (np.log(high.clip(lower=_EPS)) - np.log(low.clip(lower=_EPS))) ** 2
    pk63 = np.sqrt(_rolling_mean(log_hl, _TD_QTR) / (4.0 * np.log(2.0)) * _TD_YEAR)
    vel = pk63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_009_vol_of_vol_pct_rank_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of vol-of-vol percentile rank (jerk in turbulence rank)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vov = _rolling_std(v21, _TD_QTR)
    rank = vov.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_010_volume_weighted_vol_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5d diff of volume-weighted realized vol 21d (jerk in vw-vol velocity)."""
    r = _log_ret(close)
    vol_sum = _rolling_sum(volume, _TD_MON)
    r_vw = _safe_div(_rolling_sum(r * volume, _TD_MON), vol_sum)
    dev2 = (r - r_vw) ** 2
    vw_var = _safe_div(_rolling_sum(dev2 * volume, _TD_MON), vol_sum)
    vw_vol = np.sqrt(vw_var.clip(lower=0) * _TD_YEAR)
    vel = vw_vol.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_011_extreme_return_count_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 63d tail-event count (jerk in extreme return frequency)."""
    r = _log_ret(close)
    threshold = 3.0 * _rolling_std(r, _TD_MON)
    flags = (r.abs() > threshold).astype(float)
    count = _rolling_sum(flags, _TD_QTR)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_012_days_in_high_vol_5_21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of ultra-fast high-vol regime duration (jerk in fast streak)."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    cond = v5 > _rolling_mean(v5, _TD_MON)
    dur = _consec_streak(cond)
    vel = dur.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_013_vol_zscore_63d_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 63d vol z-score in 252d (jerk in quarterly vol extremity)."""
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    z = _safe_div(v63 - _rolling_mean(v63, _TD_YEAR), _rolling_std(v63, _TD_YEAR))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_014_vol_of_vol_21d_5d_diff_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of vol-of-vol (trend in turbulence change)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    vov = _rolling_std(v21, _TD_QTR)
    vel = vov.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vrg_extdrv3_015_garch_alpha_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of z-score of EWM5/EWM21 alpha (jerk in alpha extremity)."""
    sq = _sq_ret(close)
    ratio = _safe_div(_ewm_mean(sq, _TD_WEEK), _ewm_mean(sq, _TD_MON))
    z = _safe_div(ratio - _rolling_mean(ratio, _TD_YEAR), _rolling_std(ratio, _TD_YEAR))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_016_high_vol_fraction_126d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5d diff of monthly change in 126d high-vol fraction (jerk in half-year prevalence)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    flags = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    frac126 = _rolling_mean(flags, _TD_HALF)
    vel21 = frac126.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vrg_extdrv3_017_vol_composite_distress_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of vol composite distress (jerk in combined extremity signal)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    z = _safe_div(v21 - v_mean, v_std)
    rank = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    above2 = (v21 > v_mean + 2 * v_std).astype(float)
    composite = z / 3.0 + rank + above2
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_018_vol_mean_reversion_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of vol z-score vs 63d mean (jerk in short-run mean-reversion signal)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    z = _safe_div(v21 - _rolling_mean(v21, _TD_QTR), _rolling_std(v21, _TD_QTR))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_019_return_kurtosis_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 63d return kurtosis (jerk in fat-tail regime change)."""
    r = _log_ret(close)
    kurt = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()
    vel = kurt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_020_vol_ratio_42d_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 42d/252d vol ratio (jerk in 2-month vs annual regime divergence)."""
    v42 = _rolling_std(_log_ret(close), 42) * np.sqrt(_TD_YEAR)
    v252 = _rolling_std(_log_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    ratio = _safe_div(v42, v252)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_021_vol_persistence_3lags_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of 3-lag EWM vol autocorrelation bundle (jerk in persistence)."""
    sq = _sq_ret(close)
    ev = _ewm_mean(sq, _TD_WEEK)
    ac1 = _rolling_corr(ev, ev.shift(1), _TD_MON)
    ac2 = _rolling_corr(ev, ev.shift(2), _TD_MON)
    ac3 = _rolling_corr(ev, ev.shift(3), _TD_MON)
    bundle = (ac1 + ac2 + ac3) / 3.0
    vel = bundle.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_022_vol_of_vol_ewm_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5d diff of EWM5/EWM21 squared-vol-change ratio (jerk in vov persistence)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    dv2 = v21.diff(1) ** 2
    ratio = _safe_div(_ewm_mean(dv2, _TD_WEEK), _ewm_mean(dv2, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_023_vol_volume_corr_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5d diff of 63d abs-return/volume correlation (jerk in co-clustering signal)."""
    ab = _abs_ret(close)
    corr = _rolling_corr(ab, volume, _TD_QTR)
    vel = corr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vrg_extdrv3_024_yang_zhang_vs_close_5d_diff_slope(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of YZ/close vol ratio (trend in estimator split)."""
    k = 0.34 / (1.34 + (_TD_MON + 1) / (_TD_MON - 1))
    log_oc = np.log(open.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_hc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_ho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_lc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_lo = np.log(low.clip(lower=_EPS) / open.clip(lower=_EPS))
    rs = log_hc * log_ho + log_lc * log_lo
    yz_var = (_rolling_var(log_oc, _TD_MON) + k * _rolling_var(log_co, _TD_MON)
              + (1 - k) * _rolling_mean(rs, _TD_MON))
    yz = np.sqrt(yz_var.clip(lower=0) * _TD_YEAR)
    cc = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    ratio = _safe_div(yz, cc)
    vel = ratio.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vrg_extdrv3_025_days_in_high_vol_63_252_5d_diff_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of slow high-vol regime duration."""
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    cond = v63 > _rolling_mean(v63, _TD_YEAR)
    dur = _consec_streak(cond)
    vel = dur.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_REGIME_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "vrg_extdrv3_001_vol_of_vol_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_001_vol_of_vol_5d_diff_5d_diff},
    "vrg_extdrv3_002_vol_of_vol_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_002_vol_of_vol_zscore_5d_diff_5d_diff},
    "vrg_extdrv3_003_realized_vol_10d_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_003_realized_vol_10d_5d_diff_5d_diff},
    "vrg_extdrv3_004_vol_ratio_10d_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_004_vol_ratio_10d_63d_5d_diff_5d_diff},
    "vrg_extdrv3_005_garch_ewm2_10_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_005_garch_ewm2_10_5d_diff_5d_diff},
    "vrg_extdrv3_006_garch_ewm10_63_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_006_garch_ewm10_63_5d_diff_5d_diff},
    "vrg_extdrv3_007_yang_zhang_vol_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vrg_extdrv3_007_yang_zhang_vol_21d_5d_diff_5d_diff},
    "vrg_extdrv3_008_parkinson_vol_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": vrg_extdrv3_008_parkinson_vol_63d_5d_diff_5d_diff},
    "vrg_extdrv3_009_vol_of_vol_pct_rank_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_009_vol_of_vol_pct_rank_5d_diff_5d_diff},
    "vrg_extdrv3_010_volume_weighted_vol_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vrg_extdrv3_010_volume_weighted_vol_21d_5d_diff_5d_diff},
    "vrg_extdrv3_011_extreme_return_count_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_011_extreme_return_count_63d_5d_diff_5d_diff},
    "vrg_extdrv3_012_days_in_high_vol_5_21_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_012_days_in_high_vol_5_21_5d_diff_5d_diff},
    "vrg_extdrv3_013_vol_zscore_63d_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_013_vol_zscore_63d_252d_5d_diff_5d_diff},
    "vrg_extdrv3_014_vol_of_vol_21d_5d_diff_slope": {"inputs": ["close"], "func": vrg_extdrv3_014_vol_of_vol_21d_5d_diff_slope},
    "vrg_extdrv3_015_garch_alpha_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_015_garch_alpha_zscore_5d_diff_5d_diff},
    "vrg_extdrv3_016_high_vol_fraction_126d_21d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_016_high_vol_fraction_126d_21d_diff_5d_diff},
    "vrg_extdrv3_017_vol_composite_distress_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_017_vol_composite_distress_5d_diff_5d_diff},
    "vrg_extdrv3_018_vol_mean_reversion_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_018_vol_mean_reversion_zscore_5d_diff_5d_diff},
    "vrg_extdrv3_019_return_kurtosis_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_019_return_kurtosis_63d_5d_diff_5d_diff},
    "vrg_extdrv3_020_vol_ratio_42d_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_020_vol_ratio_42d_252d_5d_diff_5d_diff},
    "vrg_extdrv3_021_vol_persistence_3lags_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_021_vol_persistence_3lags_5d_diff_5d_diff},
    "vrg_extdrv3_022_vol_of_vol_ewm_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vrg_extdrv3_022_vol_of_vol_ewm_ratio_5d_diff_5d_diff},
    "vrg_extdrv3_023_vol_volume_corr_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vrg_extdrv3_023_vol_volume_corr_63d_5d_diff_5d_diff},
    "vrg_extdrv3_024_yang_zhang_vs_close_5d_diff_slope": {"inputs": ["close", "high", "low", "open"], "func": vrg_extdrv3_024_yang_zhang_vs_close_5d_diff_slope},
    "vrg_extdrv3_025_days_in_high_vol_63_252_5d_diff_slope": {"inputs": ["close"], "func": vrg_extdrv3_025_days_in_high_vol_63_252_5d_diff_slope},
}
