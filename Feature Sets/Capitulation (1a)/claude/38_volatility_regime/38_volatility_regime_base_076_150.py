"""
38_volatility_regime — Base Features 076-150
Domain: volatility clustering and regime-shift detection — vol regime classification,
        volume-vol regime interaction, Garman-Klass vol, regime asymmetry,
        cross-window vol rank comparisons, regime entropy, vol acceleration.
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Garman-Klass and Rogers-Satchell range-based vol ---

def vrg_076_garman_klass_vol_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day Garman-Klass volatility estimator (annualized)."""
    log_hl = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    gk = 0.5 * log_hl ** 2 - (2 * np.log(2) - 1) * log_co ** 2
    return np.sqrt(_rolling_mean(gk, _TD_WEEK) * _TD_YEAR)


def vrg_077_garman_klass_vol_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day Garman-Klass volatility estimator (annualized)."""
    log_hl = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    gk = 0.5 * log_hl ** 2 - (2 * np.log(2) - 1) * log_co ** 2
    return np.sqrt(_rolling_mean(gk, _TD_MON) * _TD_YEAR)


def vrg_078_garman_klass_vol_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """63-day Garman-Klass volatility estimator (annualized)."""
    log_hl = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    gk = 0.5 * log_hl ** 2 - (2 * np.log(2) - 1) * log_co ** 2
    return np.sqrt(_rolling_mean(gk, _TD_QTR) * _TD_YEAR)


def vrg_079_gk_fast_slow_ratio_5_21(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 5d to 21d Garman-Klass vol — fast/slow regime in range-based vol."""
    return _safe_div(vrg_076_garman_klass_vol_5d(close, high, low, open),
                     vrg_077_garman_klass_vol_21d(close, high, low, open))


def vrg_080_gk_fast_slow_ratio_5_63(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 5d to 63d Garman-Klass vol."""
    return _safe_div(vrg_076_garman_klass_vol_5d(close, high, low, open),
                     vrg_078_garman_klass_vol_63d(close, high, low, open))


def vrg_081_rogers_satchell_vol_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day Rogers-Satchell volatility estimator (drift-free, annualized)."""
    log_hc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_ho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_lc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_lo = np.log(low.clip(lower=_EPS) / open.clip(lower=_EPS))
    rs = log_hc * log_ho + log_lc * log_lo
    return np.sqrt(_rolling_mean(rs, _TD_WEEK) * _TD_YEAR)


def vrg_082_rogers_satchell_vol_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day Rogers-Satchell volatility estimator (annualized)."""
    log_hc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_ho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    log_lc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    log_lo = np.log(low.clip(lower=_EPS) / open.clip(lower=_EPS))
    rs = log_hc * log_ho + log_lc * log_lo
    return np.sqrt(_rolling_mean(rs, _TD_MON) * _TD_YEAR)


def vrg_083_gk_vs_close_vol_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21d GK vol to 21d close-to-close vol — regime efficiency measure."""
    gk21 = vrg_077_garman_klass_vol_21d(close, high, low, open)
    cc21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return _safe_div(gk21, cc21)


def vrg_084_gk_vol_zscore_21d_in_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 21d GK vol relative to trailing 252d distribution of 21d GK vol."""
    gk21 = vrg_077_garman_klass_vol_21d(close, high, low, open)
    return _safe_div(gk21 - _rolling_mean(gk21, _TD_YEAR), _rolling_std(gk21, _TD_YEAR))


def vrg_085_gk_high_vol_flag_21_252(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: 21d GK vol exceeds its 252d mean (high-vol regime via range estimator)."""
    gk21 = vrg_077_garman_klass_vol_21d(close, high, low, open)
    return (gk21 > _rolling_mean(gk21, _TD_YEAR)).astype(float)


# --- Group I (086-095): Volume-vol regime interaction ---

def vrg_086_vol_volume_corr_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d correlation between absolute returns and volume (vol-volume co-clustering)."""
    ab = _abs_ret(close)
    return _rolling_corr(ab, volume, _TD_MON)


def vrg_087_vol_volume_corr_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d correlation between absolute returns and volume."""
    ab = _abs_ret(close)
    return _rolling_corr(ab, volume, _TD_QTR)


def vrg_088_high_vol_high_volume_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: both abs-return and volume above their 21d means (joint high-regime)."""
    ab = _abs_ret(close)
    avg_ab = _rolling_mean(ab, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((ab > avg_ab) & (volume > avg_vol)).astype(float)


def vrg_089_high_vol_high_volume_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days of joint high-vol and high-volume regime."""
    cond = vrg_088_high_vol_high_volume_flag(close, volume).astype(bool)
    return _consec_streak(cond)


def vrg_090_high_vol_low_volume_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: high abs-return with low volume (vol without conviction, illiquidity regime)."""
    ab = _abs_ret(close)
    avg_ab = _rolling_mean(ab, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((ab > avg_ab) & (volume < avg_vol)).astype(float)


def vrg_091_vol_volume_regime_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of joint high-vol/high-volume days in trailing 63 days."""
    flags = vrg_088_high_vol_high_volume_flag(close, volume)
    return _rolling_sum(flags, _TD_QTR)


def vrg_092_volume_vol_ratio_regime_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of vol-weighted volume to total volume (regime-weighted activity)."""
    ab = _abs_ret(close)
    vol_wtd = (ab * volume)
    return _safe_div(_rolling_mean(vol_wtd, _TD_MON), _rolling_mean(volume, _TD_MON))


def vrg_093_vol_volume_zscore_interaction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of vol z-score and volume z-score over 21d (joint extremity score)."""
    ab = _abs_ret(close)
    ab_z = _safe_div(ab - _rolling_mean(ab, _TD_MON), _rolling_std(ab, _TD_MON))
    v_z = _safe_div(volume - _rolling_mean(volume, _TD_MON), _rolling_std(volume, _TD_MON))
    return ab_z * v_z


def vrg_094_vol_on_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean absolute return on down-price days in trailing 21d (panic vol)."""
    ab = _abs_ret(close)
    down = ab.where(_log_ret(close) < 0, np.nan)
    return down.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vrg_095_vol_asymmetry_down_vs_up_21d(close: pd.Series) -> pd.Series:
    """Ratio of mean abs-return on down days to mean abs-return on up days (21d)."""
    r = _log_ret(close)
    ab = r.abs()
    down_ab = ab.where(r < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    up_ab = ab.where(r > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(down_ab, up_ab)


# --- Group J (096-105): Regime asymmetry and skewness ---

def vrg_096_vol_asymmetry_down_vs_up_63d(close: pd.Series) -> pd.Series:
    """Ratio of mean abs-return on down days to mean abs-return on up days (63d)."""
    r = _log_ret(close)
    ab = r.abs()
    down_ab = ab.where(r < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_ab = ab.where(r > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(down_ab, up_ab)


def vrg_097_downside_vol_21d(close: pd.Series) -> pd.Series:
    """21d downside realized vol (std of negative log-returns only)."""
    r = _log_ret(close)
    down_r = r.where(r < 0, 0.0)
    return _rolling_std(down_r, _TD_MON) * np.sqrt(_TD_YEAR)


def vrg_098_downside_vol_63d(close: pd.Series) -> pd.Series:
    """63d downside realized vol (std of negative log-returns only)."""
    r = _log_ret(close)
    down_r = r.where(r < 0, 0.0)
    return _rolling_std(down_r, _TD_QTR) * np.sqrt(_TD_YEAR)


def vrg_099_upside_vol_21d(close: pd.Series) -> pd.Series:
    """21d upside realized vol (std of positive log-returns only)."""
    r = _log_ret(close)
    up_r = r.where(r > 0, 0.0)
    return _rolling_std(up_r, _TD_MON) * np.sqrt(_TD_YEAR)


def vrg_100_upside_vol_63d(close: pd.Series) -> pd.Series:
    """63d upside realized vol (std of positive log-returns only)."""
    r = _log_ret(close)
    up_r = r.where(r > 0, 0.0)
    return _rolling_std(up_r, _TD_QTR) * np.sqrt(_TD_YEAR)


def vrg_101_vol_skew_down_up_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of downside to upside vol at 21d (vol asymmetry / fear ratio)."""
    return _safe_div(vrg_097_downside_vol_21d(close), vrg_099_upside_vol_21d(close))


def vrg_102_vol_skew_down_up_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of downside to upside vol at 63d."""
    return _safe_div(vrg_098_downside_vol_63d(close), vrg_100_upside_vol_63d(close))


def vrg_103_return_skewness_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d skewness of log-returns (negative = left-tail regime)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).skew()


def vrg_104_return_skewness_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d skewness of log-returns."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).skew()


def vrg_105_return_kurtosis_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d excess kurtosis of log-returns (fat-tail regime indicator)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).kurt()


# --- Group K (106-115): Cross-window vol rank comparisons ---

def vrg_106_vol_rank_5d_in_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d realized vol within trailing 63d vol distribution."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    return v5.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vrg_107_vol_rank_21d_in_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d realized vol within trailing 63d vol distribution."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return v21.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vrg_108_vol_rank_5d_in_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d realized vol within trailing 126d vol distribution."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    return v5.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def vrg_109_vol_rank_21d_in_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d realized vol within trailing 504d vol distribution (2yr)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return v21.rolling(504, min_periods=_TD_HALF).rank(pct=True)


def vrg_110_vol_expanding_rank_21d(close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 21d realized vol."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return v21.expanding(min_periods=_TD_MON).rank(pct=True)


def vrg_111_vol_rank_gk_21d_in_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21d GK vol within trailing 252d GK vol distribution."""
    log_hl = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    gk = 0.5 * log_hl ** 2 - (2 * np.log(2) - 1) * log_co ** 2
    gk21 = np.sqrt(_rolling_mean(gk, _TD_MON) * _TD_YEAR)
    return gk21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vrg_112_vol_rank_parkinson_21d_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21d Parkinson vol within trailing 252d distribution."""
    log_hl = (np.log(high.clip(lower=_EPS)) - np.log(low.clip(lower=_EPS))) ** 2
    pk21 = np.sqrt(_rolling_mean(log_hl, _TD_MON) / (4.0 * np.log(2.0)) * _TD_YEAR)
    return pk21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vrg_113_vol_rank_5d_vs_rank_252d_spread(close: pd.Series) -> pd.Series:
    """Spread between 5d vol rank (in 252d) and 252d vol rank (in expanding)."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    v252 = _rolling_std(_log_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    rank5 = v5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    rank252 = v252.expanding(min_periods=_TD_YEAR).rank(pct=True)
    return rank5 - rank252


def vrg_114_vol_regime_consensus_flag(close: pd.Series) -> pd.Series:
    """Flag: 5d, 21d, and 63d vols all simultaneously above their respective 252d means."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    high5 = v5 > _rolling_mean(v5, _TD_YEAR)
    high21 = v21 > _rolling_mean(v21, _TD_YEAR)
    high63 = v63 > _rolling_mean(v63, _TD_YEAR)
    return (high5 & high21 & high63).astype(float)


def vrg_115_vol_regime_consensus_score(close: pd.Series) -> pd.Series:
    """Sum of three regime flags (0/1 each): 5d, 21d, 63d vs 252d mean (score 0-3)."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    f5 = (v5 > _rolling_mean(v5, _TD_YEAR)).astype(float)
    f21 = (v21 > _rolling_mean(v21, _TD_YEAR)).astype(float)
    f63 = (v63 > _rolling_mean(v63, _TD_YEAR)).astype(float)
    return f5 + f21 + f63


# --- Group L (116-125): Vol acceleration and trend ---

def vrg_116_vol_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 21d realized vol over trailing 21-day window (vol trend)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return _linslope(v21, _TD_MON)


def vrg_117_vol_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21d realized vol over trailing 63-day window."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return _linslope(v21, _TD_QTR)


def vrg_118_vol_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day difference of 5d realized vol (velocity of short-term vol)."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    return v5.diff(_TD_WEEK)


def vrg_119_vol_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day difference of 21d realized vol (velocity of monthly vol)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return v21.diff(_TD_WEEK)


def vrg_120_vol_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day difference of 21d realized vol."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return v21.diff(_TD_MON)


def vrg_121_vol_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day difference of 63d realized vol."""
    v63 = _rolling_std(_log_ret(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    return v63.diff(_TD_MON)


def vrg_122_vol_acceleration_5d(close: pd.Series) -> pd.Series:
    """Second 5d diff of 5d vol (acceleration of short-term volatility)."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    return v5.diff(_TD_WEEK).diff(_TD_WEEK)


def vrg_123_vol_acceleration_21d(close: pd.Series) -> pd.Series:
    """Second 5d diff of 21d vol (acceleration of monthly volatility)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    return v21.diff(_TD_WEEK).diff(_TD_WEEK)


def vrg_124_ewm_vol_5d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of EWM(5) vol over trailing 21 days (trend of smooth vol)."""
    r = _log_ret(close)
    ev5 = _ewm_std(r, _TD_WEEK) * np.sqrt(_TD_YEAR)
    return _linslope(ev5, _TD_MON)


def vrg_125_vol_trend_consistency_63d(close: pd.Series) -> pd.Series:
    """Fraction of 5d rolling windows (within 63d) where vol is rising vs prior window."""
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    rising = (v5.diff(_TD_WEEK) > 0).astype(float)
    return _rolling_mean(rising, _TD_QTR)


# --- Group M (126-135): Regime entropy and variability ---

def vrg_126_vol_regime_entropy_63d(close: pd.Series) -> pd.Series:
    """Entropy of high/low vol regime binary series over 63d (regime stability)."""
    flags = ((_rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)) >
             _rolling_mean(_rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR), _TD_YEAR)).astype(float)
    p1 = _rolling_mean(flags, _TD_QTR).clip(_EPS, 1 - _EPS)
    p0 = 1 - p1
    return -(p1 * np.log(p1) + p0 * np.log(p0))


def vrg_127_vol_variability_cv_21d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of daily abs-returns over 21d (regime spread)."""
    ab = _abs_ret(close)
    return _safe_div(_rolling_std(ab, _TD_MON), _rolling_mean(ab, _TD_MON))


def vrg_128_vol_variability_cv_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of daily abs-returns over 63d."""
    ab = _abs_ret(close)
    return _safe_div(_rolling_std(ab, _TD_QTR), _rolling_mean(ab, _TD_QTR))


def vrg_129_vol_iqr_21d(close: pd.Series) -> pd.Series:
    """IQR of daily abs-returns over 21d (robust spread in vol regime)."""
    ab = _abs_ret(close)
    q75 = ab.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = ab.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    return q75 - q25


def vrg_130_vol_iqr_63d(close: pd.Series) -> pd.Series:
    """IQR of daily abs-returns over 63d."""
    ab = _abs_ret(close)
    q75 = ab.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = ab.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def vrg_131_vol_upper_tail_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of days where abs-return > 2x 21d mean abs-return (tail regime)."""
    ab = _abs_ret(close)
    threshold = 2.0 * _rolling_mean(ab, _TD_MON)
    return (ab > threshold).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vrg_132_vol_upper_tail_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of days where abs-return > 2x 63d mean abs-return."""
    ab = _abs_ret(close)
    threshold = 2.0 * _rolling_mean(ab, _TD_QTR)
    return (ab > threshold).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vrg_133_vol_regime_stability_score_63d(close: pd.Series) -> pd.Series:
    """Inverse of regime transition count in 63d (fewer transitions = more stable)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_avg = _rolling_mean(v21, _TD_YEAR)
    above = (v21 > v_avg).astype(float)
    transitions = _rolling_sum(above.diff(1).abs(), _TD_QTR)
    return _safe_div(pd.Series(1.0, index=close.index), transitions + 1)


def vrg_134_vol_max_to_mean_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of max abs-return to mean abs-return in 21d (spike intensity in regime)."""
    ab = _abs_ret(close)
    return _safe_div(_rolling_max(ab, _TD_MON), _rolling_mean(ab, _TD_MON))


def vrg_135_vol_max_to_mean_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of max abs-return to mean abs-return in 63d."""
    ab = _abs_ret(close)
    return _safe_div(_rolling_max(ab, _TD_QTR), _rolling_mean(ab, _TD_QTR))


# --- Group N (136-145): Vol regime in context of price trend ---

def vrg_136_high_vol_below_sma200_flag(close: pd.Series) -> pd.Series:
    """Flag: high-vol regime AND close below 200-day SMA (distress confluence)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    high_vol = v21 > _rolling_mean(v21, _TD_YEAR)
    sma200 = _rolling_mean(close, 200)
    below_ma = close < sma200
    return (high_vol & below_ma).astype(float)


def vrg_137_high_vol_below_sma200_streak(close: pd.Series) -> pd.Series:
    """Consecutive days of joint high-vol regime and below-200d SMA."""
    cond = vrg_136_high_vol_below_sma200_flag(close).astype(bool)
    return _consec_streak(cond)


def vrg_138_vol_regime_in_downtrend_score(close: pd.Series) -> pd.Series:
    """Score: 21d vol rank * (1 if close below 252d SMA, else 0) — vol in downtrend."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    rank = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    below = (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    return rank * below


def vrg_139_vol_regime_new_high_vol_flag_126d(close: pd.Series) -> pd.Series:
    """Flag: current 21d vol is new 126-day high vol (regime breakout)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    prior_max = v21.shift(1).rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).max()
    return (v21 > prior_max).astype(float)


def vrg_140_vol_regime_new_high_vol_flag_252d(close: pd.Series) -> pd.Series:
    """Flag: current 21d vol is new 252-day high vol (annual regime breakout)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    prior_max = v21.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    return (v21 > prior_max).astype(float)


def vrg_141_vol_regime_vs_trend_divergence(close: pd.Series) -> pd.Series:
    """Divergence: vol rising while price falling (both standardized, 21d window)."""
    r = _log_ret(close)
    v21 = _rolling_std(r, _TD_MON)
    v_chg = v21.diff(_TD_WEEK)
    p_chg = close.pct_change(_TD_WEEK)
    v_z = _safe_div(v_chg - _rolling_mean(v_chg, _TD_QTR), _rolling_std(v_chg, _TD_QTR))
    p_z = _safe_div(p_chg - _rolling_mean(p_chg, _TD_QTR), _rolling_std(p_chg, _TD_QTR))
    return v_z - p_z


def vrg_142_vol_regime_price_reversal_score(close: pd.Series) -> pd.Series:
    """High-vol regime score weighted by recent drawdown depth (distress index)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    rank = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    roll_max = close.rolling(_TD_YEAR, min_periods=_TD_QTR).max()
    drawdown = _safe_div(close - roll_max, roll_max).abs()
    return rank * drawdown


def vrg_143_vol_regime_low_vol_complacency_streak(close: pd.Series) -> pd.Series:
    """Consecutive days of below-1std vol band (complacency / calm regime)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    cond = v21 < (v_mean - v_std)
    return _consec_streak(cond)


def vrg_144_vol_regime_breakout_magnitude(close: pd.Series) -> pd.Series:
    """Magnitude of vol above its upper band: max(0, v21 - (mean + 1std)) / std."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    upper = v_mean + v_std
    excess = (v21 - upper).clip(lower=0)
    return _safe_div(excess, v_std)


def vrg_145_vol_regime_breakout_magnitude_2std(close: pd.Series) -> pd.Series:
    """Magnitude of vol above 2-std band: max(0, v21 - (mean + 2std)) / std."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    upper2 = v_mean + 2 * v_std
    excess = (v21 - upper2).clip(lower=0)
    return _safe_div(excess, v_std)


# --- Group O (146-150): Additional regime synthesis features ---

def vrg_146_vol_regime_composite_score(close: pd.Series) -> pd.Series:
    """Composite high-vol score: mean of z-score, rank, and fast/slow ratio (normalized)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_mean = _rolling_mean(v21, _TD_YEAR)
    v_std = _rolling_std(v21, _TD_YEAR)
    z = _safe_div(v21 - v_mean, v_std)
    rank = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    v5 = _rolling_std(_log_ret(close), _TD_WEEK) * np.sqrt(_TD_YEAR)
    ratio = _safe_div(v5, v21)
    z_n = z / 3.0
    rank_n = rank - 0.5
    ratio_n = (ratio - 1.0) / 2.0
    return (z_n + rank_n + ratio_n) / 3.0


def vrg_147_vol_regime_persistence_ratio_63_252(close: pd.Series) -> pd.Series:
    """Ratio of 63d high-vol fraction to 252d high-vol fraction (recent vs historical)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_avg = _rolling_mean(v21, _TD_YEAR)
    above = (v21 > v_avg).astype(float)
    frac63 = _rolling_mean(above, _TD_QTR)
    frac252 = _rolling_mean(above, _TD_YEAR)
    return _safe_div(frac63, frac252)


def vrg_148_vol_regime_ewm_vs_rolling_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM(21) vol to rolling 21d vol (regime detection via estimator divergence)."""
    r = _log_ret(close)
    ewm_v = _ewm_std(r, _TD_MON) * np.sqrt(_TD_YEAR)
    roll_v = _rolling_std(r, _TD_MON) * np.sqrt(_TD_YEAR)
    return _safe_div(ewm_v, roll_v)


def vrg_149_vol_regime_high_vol_low_vol_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63d high-vol streak count to 63d low-vol streak days (instability)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    v_avg = _rolling_mean(v21, _TD_YEAR)
    high_days = _rolling_sum((v21 > v_avg).astype(float), _TD_QTR)
    low_days = _rolling_sum((v21 < v_avg).astype(float), _TD_QTR)
    return _safe_div(high_days, low_days)


def vrg_150_vol_regime_trend_strength_252d(close: pd.Series) -> pd.Series:
    """R-squared of OLS fit of 21d vol over 252 days (trend strength in vol regime)."""
    v21 = _rolling_std(_log_ret(close), _TD_MON) * np.sqrt(_TD_YEAR)
    def _r2(x):
        if len(x) < max(2, _TD_YEAR // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        ss_tot = ((x - x_m) ** 2).sum()
        if ss_tot < _EPS:
            return np.nan
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den < _EPS:
            return np.nan
        slope = num / den
        ss_res = ((x - (x_m + slope * (xi - xi_m))) ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return v21.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).apply(_r2, raw=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_REGIME_REGISTRY_076_150 = {
    "vrg_076_garman_klass_vol_5d": {"inputs": ["close", "high", "low", "open"], "func": vrg_076_garman_klass_vol_5d},
    "vrg_077_garman_klass_vol_21d": {"inputs": ["close", "high", "low", "open"], "func": vrg_077_garman_klass_vol_21d},
    "vrg_078_garman_klass_vol_63d": {"inputs": ["close", "high", "low", "open"], "func": vrg_078_garman_klass_vol_63d},
    "vrg_079_gk_fast_slow_ratio_5_21": {"inputs": ["close", "high", "low", "open"], "func": vrg_079_gk_fast_slow_ratio_5_21},
    "vrg_080_gk_fast_slow_ratio_5_63": {"inputs": ["close", "high", "low", "open"], "func": vrg_080_gk_fast_slow_ratio_5_63},
    "vrg_081_rogers_satchell_vol_5d": {"inputs": ["close", "high", "low", "open"], "func": vrg_081_rogers_satchell_vol_5d},
    "vrg_082_rogers_satchell_vol_21d": {"inputs": ["close", "high", "low", "open"], "func": vrg_082_rogers_satchell_vol_21d},
    "vrg_083_gk_vs_close_vol_ratio_21d": {"inputs": ["close", "high", "low", "open"], "func": vrg_083_gk_vs_close_vol_ratio_21d},
    "vrg_084_gk_vol_zscore_21d_in_252d": {"inputs": ["close", "high", "low", "open"], "func": vrg_084_gk_vol_zscore_21d_in_252d},
    "vrg_085_gk_high_vol_flag_21_252": {"inputs": ["close", "high", "low", "open"], "func": vrg_085_gk_high_vol_flag_21_252},
    "vrg_086_vol_volume_corr_21d": {"inputs": ["close", "volume"], "func": vrg_086_vol_volume_corr_21d},
    "vrg_087_vol_volume_corr_63d": {"inputs": ["close", "volume"], "func": vrg_087_vol_volume_corr_63d},
    "vrg_088_high_vol_high_volume_flag": {"inputs": ["close", "volume"], "func": vrg_088_high_vol_high_volume_flag},
    "vrg_089_high_vol_high_volume_streak": {"inputs": ["close", "volume"], "func": vrg_089_high_vol_high_volume_streak},
    "vrg_090_high_vol_low_volume_flag": {"inputs": ["close", "volume"], "func": vrg_090_high_vol_low_volume_flag},
    "vrg_091_vol_volume_regime_score_63d": {"inputs": ["close", "volume"], "func": vrg_091_vol_volume_regime_score_63d},
    "vrg_092_volume_vol_ratio_regime_21d": {"inputs": ["close", "volume"], "func": vrg_092_volume_vol_ratio_regime_21d},
    "vrg_093_vol_volume_zscore_interaction_21d": {"inputs": ["close", "volume"], "func": vrg_093_vol_volume_zscore_interaction_21d},
    "vrg_094_vol_on_down_days_21d": {"inputs": ["close", "volume"], "func": vrg_094_vol_on_down_days_21d},
    "vrg_095_vol_asymmetry_down_vs_up_21d": {"inputs": ["close"], "func": vrg_095_vol_asymmetry_down_vs_up_21d},
    "vrg_096_vol_asymmetry_down_vs_up_63d": {"inputs": ["close"], "func": vrg_096_vol_asymmetry_down_vs_up_63d},
    "vrg_097_downside_vol_21d": {"inputs": ["close"], "func": vrg_097_downside_vol_21d},
    "vrg_098_downside_vol_63d": {"inputs": ["close"], "func": vrg_098_downside_vol_63d},
    "vrg_099_upside_vol_21d": {"inputs": ["close"], "func": vrg_099_upside_vol_21d},
    "vrg_100_upside_vol_63d": {"inputs": ["close"], "func": vrg_100_upside_vol_63d},
    "vrg_101_vol_skew_down_up_ratio_21d": {"inputs": ["close"], "func": vrg_101_vol_skew_down_up_ratio_21d},
    "vrg_102_vol_skew_down_up_ratio_63d": {"inputs": ["close"], "func": vrg_102_vol_skew_down_up_ratio_63d},
    "vrg_103_return_skewness_21d": {"inputs": ["close"], "func": vrg_103_return_skewness_21d},
    "vrg_104_return_skewness_63d": {"inputs": ["close"], "func": vrg_104_return_skewness_63d},
    "vrg_105_return_kurtosis_21d": {"inputs": ["close"], "func": vrg_105_return_kurtosis_21d},
    "vrg_106_vol_rank_5d_in_63d": {"inputs": ["close"], "func": vrg_106_vol_rank_5d_in_63d},
    "vrg_107_vol_rank_21d_in_63d": {"inputs": ["close"], "func": vrg_107_vol_rank_21d_in_63d},
    "vrg_108_vol_rank_5d_in_126d": {"inputs": ["close"], "func": vrg_108_vol_rank_5d_in_126d},
    "vrg_109_vol_rank_21d_in_504d": {"inputs": ["close"], "func": vrg_109_vol_rank_21d_in_504d},
    "vrg_110_vol_expanding_rank_21d": {"inputs": ["close"], "func": vrg_110_vol_expanding_rank_21d},
    "vrg_111_vol_rank_gk_21d_in_252d": {"inputs": ["close", "high", "low", "open"], "func": vrg_111_vol_rank_gk_21d_in_252d},
    "vrg_112_vol_rank_parkinson_21d_in_252d": {"inputs": ["close", "high", "low"], "func": vrg_112_vol_rank_parkinson_21d_in_252d},
    "vrg_113_vol_rank_5d_vs_rank_252d_spread": {"inputs": ["close"], "func": vrg_113_vol_rank_5d_vs_rank_252d_spread},
    "vrg_114_vol_regime_consensus_flag": {"inputs": ["close"], "func": vrg_114_vol_regime_consensus_flag},
    "vrg_115_vol_regime_consensus_score": {"inputs": ["close"], "func": vrg_115_vol_regime_consensus_score},
    "vrg_116_vol_21d_slope_21d": {"inputs": ["close"], "func": vrg_116_vol_21d_slope_21d},
    "vrg_117_vol_21d_slope_63d": {"inputs": ["close"], "func": vrg_117_vol_21d_slope_63d},
    "vrg_118_vol_5d_5d_diff": {"inputs": ["close"], "func": vrg_118_vol_5d_5d_diff},
    "vrg_119_vol_21d_5d_diff": {"inputs": ["close"], "func": vrg_119_vol_21d_5d_diff},
    "vrg_120_vol_21d_21d_diff": {"inputs": ["close"], "func": vrg_120_vol_21d_21d_diff},
    "vrg_121_vol_63d_21d_diff": {"inputs": ["close"], "func": vrg_121_vol_63d_21d_diff},
    "vrg_122_vol_acceleration_5d": {"inputs": ["close"], "func": vrg_122_vol_acceleration_5d},
    "vrg_123_vol_acceleration_21d": {"inputs": ["close"], "func": vrg_123_vol_acceleration_21d},
    "vrg_124_ewm_vol_5d_slope_21d": {"inputs": ["close"], "func": vrg_124_ewm_vol_5d_slope_21d},
    "vrg_125_vol_trend_consistency_63d": {"inputs": ["close"], "func": vrg_125_vol_trend_consistency_63d},
    "vrg_126_vol_regime_entropy_63d": {"inputs": ["close"], "func": vrg_126_vol_regime_entropy_63d},
    "vrg_127_vol_variability_cv_21d": {"inputs": ["close"], "func": vrg_127_vol_variability_cv_21d},
    "vrg_128_vol_variability_cv_63d": {"inputs": ["close"], "func": vrg_128_vol_variability_cv_63d},
    "vrg_129_vol_iqr_21d": {"inputs": ["close"], "func": vrg_129_vol_iqr_21d},
    "vrg_130_vol_iqr_63d": {"inputs": ["close"], "func": vrg_130_vol_iqr_63d},
    "vrg_131_vol_upper_tail_fraction_21d": {"inputs": ["close"], "func": vrg_131_vol_upper_tail_fraction_21d},
    "vrg_132_vol_upper_tail_fraction_63d": {"inputs": ["close"], "func": vrg_132_vol_upper_tail_fraction_63d},
    "vrg_133_vol_regime_stability_score_63d": {"inputs": ["close"], "func": vrg_133_vol_regime_stability_score_63d},
    "vrg_134_vol_max_to_mean_ratio_21d": {"inputs": ["close"], "func": vrg_134_vol_max_to_mean_ratio_21d},
    "vrg_135_vol_max_to_mean_ratio_63d": {"inputs": ["close"], "func": vrg_135_vol_max_to_mean_ratio_63d},
    "vrg_136_high_vol_below_sma200_flag": {"inputs": ["close"], "func": vrg_136_high_vol_below_sma200_flag},
    "vrg_137_high_vol_below_sma200_streak": {"inputs": ["close"], "func": vrg_137_high_vol_below_sma200_streak},
    "vrg_138_vol_regime_in_downtrend_score": {"inputs": ["close"], "func": vrg_138_vol_regime_in_downtrend_score},
    "vrg_139_vol_regime_new_high_vol_flag_126d": {"inputs": ["close"], "func": vrg_139_vol_regime_new_high_vol_flag_126d},
    "vrg_140_vol_regime_new_high_vol_flag_252d": {"inputs": ["close"], "func": vrg_140_vol_regime_new_high_vol_flag_252d},
    "vrg_141_vol_regime_vs_trend_divergence": {"inputs": ["close"], "func": vrg_141_vol_regime_vs_trend_divergence},
    "vrg_142_vol_regime_price_reversal_score": {"inputs": ["close"], "func": vrg_142_vol_regime_price_reversal_score},
    "vrg_143_vol_regime_low_vol_complacency_streak": {"inputs": ["close"], "func": vrg_143_vol_regime_low_vol_complacency_streak},
    "vrg_144_vol_regime_breakout_magnitude": {"inputs": ["close"], "func": vrg_144_vol_regime_breakout_magnitude},
    "vrg_145_vol_regime_breakout_magnitude_2std": {"inputs": ["close"], "func": vrg_145_vol_regime_breakout_magnitude_2std},
    "vrg_146_vol_regime_composite_score": {"inputs": ["close"], "func": vrg_146_vol_regime_composite_score},
    "vrg_147_vol_regime_persistence_ratio_63_252": {"inputs": ["close"], "func": vrg_147_vol_regime_persistence_ratio_63_252},
    "vrg_148_vol_regime_ewm_vs_rolling_ratio": {"inputs": ["close"], "func": vrg_148_vol_regime_ewm_vs_rolling_ratio},
    "vrg_149_vol_regime_high_vol_low_vol_ratio": {"inputs": ["close"], "func": vrg_149_vol_regime_high_vol_low_vol_ratio},
    "vrg_150_vol_regime_trend_strength_252d": {"inputs": ["close"], "func": vrg_150_vol_regime_trend_strength_252d},
}
