"""
34_velocity_inflection — Base Features 076-150
Domain: sign change in price velocity — inflection points where smoothed price velocity
(1st derivative) changes sign, days since last velocity sign-flip, curvature/2nd-derivative
of price crossing zero, count of inflections in a window, magnitude of velocity at most
recent inflection, alternating up/down velocity regimes, zero-crossings of momentum,
smoothed-slope sign reversals.
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _velocity(close: pd.Series, span: int) -> pd.Series:
    """EMA-smoothed 1-day log-return (price velocity)."""
    lr = _log_safe(close).diff(1)
    return _ewm_mean(lr, span)


def _sign_flip(s: pd.Series) -> pd.Series:
    """Binary: 1 where sign of s differs from prior row."""
    sg = np.sign(s)
    return ((sg != sg.shift(1)) & sg.notna() & sg.shift(1).notna()).astype(float)


def _days_since_flip(flip: pd.Series) -> pd.Series:
    """Bars elapsed since last 1 in binary flip series (backward-looking)."""
    idx = np.arange(len(flip))
    last_flip_idx = pd.Series(np.where(flip.values == 1, idx, np.nan))
    last_flip_idx = last_flip_idx.ffill()
    result = pd.Series(idx, index=flip.index, dtype=float) - last_flip_idx.values
    result[last_flip_idx.isna().values] = np.nan
    return result


def _rolling_count(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


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


def _consec_true(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Momentum zero-crossing (RSI/ROC/momentum sign change) ---

def vif_076_roc5_zero_cross_neg(close: pd.Series) -> pd.Series:
    """Binary: 5-day rate-of-change crossed below zero (velocity gone negative)."""
    roc = close.pct_change(_TD_WEEK)
    return ((roc < 0) & (roc.shift(1) >= 0)).astype(float)


def vif_077_roc5_zero_cross_pos(close: pd.Series) -> pd.Series:
    """Binary: 5-day rate-of-change crossed above zero (velocity gone positive)."""
    roc = close.pct_change(_TD_WEEK)
    return ((roc > 0) & (roc.shift(1) <= 0)).astype(float)


def vif_078_roc21_zero_cross_neg(close: pd.Series) -> pd.Series:
    """Binary: 21-day ROC crossed below zero."""
    roc = close.pct_change(_TD_MON)
    return ((roc < 0) & (roc.shift(1) >= 0)).astype(float)


def vif_079_roc21_zero_cross_pos(close: pd.Series) -> pd.Series:
    """Binary: 21-day ROC crossed above zero."""
    roc = close.pct_change(_TD_MON)
    return ((roc > 0) & (roc.shift(1) <= 0)).astype(float)


def vif_080_roc63_zero_cross_neg(close: pd.Series) -> pd.Series:
    """Binary: 63-day ROC crossed below zero (quarterly velocity gone negative)."""
    roc = close.pct_change(_TD_QTR)
    return ((roc < 0) & (roc.shift(1) >= 0)).astype(float)


def vif_081_days_since_roc5_zero_cross(close: pd.Series) -> pd.Series:
    """Days since last 5-day ROC zero-crossing (either direction)."""
    roc = close.pct_change(_TD_WEEK)
    flip = _sign_flip(roc)
    return _days_since_flip(flip)


def vif_082_days_since_roc21_zero_cross(close: pd.Series) -> pd.Series:
    """Days since last 21-day ROC zero-crossing."""
    roc = close.pct_change(_TD_MON)
    flip = _sign_flip(roc)
    return _days_since_flip(flip)


def vif_083_roc5_sign(close: pd.Series) -> pd.Series:
    """Sign of current 5-day ROC (-1/0/+1)."""
    return np.sign(close.pct_change(_TD_WEEK)).astype(float)


def vif_084_roc21_sign(close: pd.Series) -> pd.Series:
    """Sign of current 21-day ROC."""
    return np.sign(close.pct_change(_TD_MON)).astype(float)


def vif_085_roc63_sign(close: pd.Series) -> pd.Series:
    """Sign of current 63-day ROC."""
    return np.sign(close.pct_change(_TD_QTR)).astype(float)


def vif_086_roc_sign_disagreement_5_63(close: pd.Series) -> pd.Series:
    """Binary: 5-day and 63-day ROC have opposite signs."""
    s5 = np.sign(close.pct_change(_TD_WEEK))
    s63 = np.sign(close.pct_change(_TD_QTR))
    return ((s5 != s63) & s5.notna() & s63.notna()).astype(float)


def vif_087_all_roc_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: 5-day, 21-day, and 63-day ROC all negative simultaneously."""
    r5 = close.pct_change(_TD_WEEK)
    r21 = close.pct_change(_TD_MON)
    r63 = close.pct_change(_TD_QTR)
    return ((r5 < 0) & (r21 < 0) & (r63 < 0)).astype(float)


def vif_088_roc5_zero_cross_count_63d(close: pd.Series) -> pd.Series:
    """Count of 5-day ROC zero-crossings (either direction) in trailing 63 days."""
    roc = close.pct_change(_TD_WEEK)
    return _rolling_count(_sign_flip(roc), _TD_QTR)


def vif_089_roc21_zero_cross_count_252d(close: pd.Series) -> pd.Series:
    """Count of 21-day ROC zero-crossings in trailing 252 days."""
    roc = close.pct_change(_TD_MON)
    return _rolling_count(_sign_flip(roc), _TD_YEAR)


def vif_090_roc5_neg_cross_count_63d(close: pd.Series) -> pd.Series:
    """Count of bearish 5-day ROC zero-crosses (positive-to-negative) in trailing 63 days."""
    roc = close.pct_change(_TD_WEEK)
    cross = ((roc < 0) & (roc.shift(1) >= 0)).astype(float)
    return _rolling_count(cross, _TD_QTR)


# --- Group G (091-105): Volume-weighted and high/low velocity inflections ---

def vif_091_vol_wtd_vel_ema5_sign(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign of volume-weighted EMA-5 velocity (volume amplifies regime direction)."""
    lr = _log_safe(close).diff(1)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    vw_lr = lr * vol_norm
    vw_vel = _ewm_mean(vw_lr, _TD_WEEK)
    return np.sign(vw_vel).astype(float)


def vif_092_vol_wtd_vel_ema5_flip(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: volume-weighted EMA-5 velocity sign-flipped today."""
    lr = _log_safe(close).diff(1)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    vw_vel = _ewm_mean(lr * vol_norm, _TD_WEEK)
    return _sign_flip(vw_vel)


def vif_093_vol_wtd_vel_to_neg_flip(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: volume-weighted EMA-5 velocity turned negative (bearish vol-weighted inflection)."""
    lr = _log_safe(close).diff(1)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    vw_vel = _ewm_mean(lr * vol_norm, _TD_WEEK)
    sg = np.sign(vw_vel)
    return ((sg < 0) & (sg.shift(1) > 0)).astype(float)


def vif_094_high_vel_ema5_sign(close: pd.Series, high: pd.Series) -> pd.Series:
    """Sign of EMA-5 smoothed 1-day log-return of daily highs (high-price velocity)."""
    lr_h = _log_safe(high).diff(1)
    vel_h = _ewm_mean(lr_h, _TD_WEEK)
    return np.sign(vel_h).astype(float)


def vif_095_low_vel_ema5_sign(close: pd.Series, low: pd.Series) -> pd.Series:
    """Sign of EMA-5 smoothed 1-day log-return of daily lows (low-price velocity)."""
    lr_l = _log_safe(low).diff(1)
    vel_l = _ewm_mean(lr_l, _TD_WEEK)
    return np.sign(vel_l).astype(float)


def vif_096_high_vel_flip_to_neg(close: pd.Series, high: pd.Series) -> pd.Series:
    """Binary: EMA-5 high-price velocity flipped negative (highs decelerating bearishly)."""
    lr_h = _log_safe(high).diff(1)
    vel_h = _ewm_mean(lr_h, _TD_WEEK)
    sg = np.sign(vel_h)
    return ((sg < 0) & (sg.shift(1) > 0)).astype(float)


def vif_097_low_vel_flip_to_neg(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: EMA-5 low-price velocity flipped negative (lows falling faster)."""
    lr_l = _log_safe(low).diff(1)
    vel_l = _ewm_mean(lr_l, _TD_WEEK)
    sg = np.sign(vel_l)
    return ((sg < 0) & (sg.shift(1) > 0)).astype(float)


def vif_098_range_vel_flip(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: sign flip in EMA-5 of daily range change (high-low expanding/contracting)."""
    rng = (high - low) / close.shift(1).clip(lower=_EPS)
    vel_rng = _ewm_mean(rng.diff(1), _TD_WEEK)
    return _sign_flip(vel_rng)


def vif_099_close_minus_open_vel_flip(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: sign flip in EMA-5 of (close-open)/open velocity (candle body direction flip)."""
    body = (close - open) / open.clip(lower=_EPS)
    vel_body = _ewm_mean(body, _TD_WEEK)
    return _sign_flip(vel_body)


def vif_100_days_since_vol_wtd_vel_flip(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since last volume-weighted EMA-5 velocity sign-flip."""
    return _days_since_flip(vif_092_vol_wtd_vel_ema5_flip(close, volume))


def vif_101_vol_wtd_vel_flip_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of volume-weighted EMA-5 velocity flips in trailing 63 days."""
    return _rolling_count(vif_092_vol_wtd_vel_ema5_flip(close, volume), _TD_QTR)


def vif_102_high_vel_flip_count_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of EMA-5 high-price velocity sign-flips in trailing 63 days."""
    lr_h = _log_safe(high).diff(1)
    return _rolling_count(_sign_flip(_ewm_mean(lr_h, _TD_WEEK)), _TD_QTR)


def vif_103_low_vel_flip_count_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of EMA-5 low-price velocity sign-flips in trailing 63 days."""
    lr_l = _log_safe(low).diff(1)
    return _rolling_count(_sign_flip(_ewm_mean(lr_l, _TD_WEEK)), _TD_QTR)


def vif_104_high_low_vel_regime_agree(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: high-price and low-price EMA-5 velocities have the same sign (aligned decline)."""
    vel_h = _ewm_mean(_log_safe(high).diff(1), _TD_WEEK)
    vel_l = _ewm_mean(_log_safe(low).diff(1), _TD_WEEK)
    return (np.sign(vel_h) == np.sign(vel_l)).astype(float)


def vif_105_open_vel_flip_to_neg(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: EMA-5 open-price velocity flipped negative (gap-open trend reversal)."""
    lr_o = _log_safe(open).diff(1)
    vel_o = _ewm_mean(lr_o, _TD_WEEK)
    sg = np.sign(vel_o)
    return ((sg < 0) & (sg.shift(1) > 0)).astype(float)


# --- Group H (106-120): Smoothed-slope sign reversals (OLS-based velocity) ---

def vif_106_ols_slope_5d_sign(close: pd.Series) -> pd.Series:
    """Sign of 5-day OLS price slope (direction of short-term price trend)."""
    return np.sign(_linslope(_log_safe(close), _TD_WEEK)).astype(float)


def vif_107_ols_slope_21d_sign(close: pd.Series) -> pd.Series:
    """Sign of 21-day OLS price slope."""
    return np.sign(_linslope(_log_safe(close), _TD_MON)).astype(float)


def vif_108_ols_slope_63d_sign(close: pd.Series) -> pd.Series:
    """Sign of 63-day OLS price slope."""
    return np.sign(_linslope(_log_safe(close), _TD_QTR)).astype(float)


def vif_109_ols_slope_5d_flip(close: pd.Series) -> pd.Series:
    """Binary: 5-day OLS slope changed sign today (short-term slope reversal)."""
    return _sign_flip(_linslope(_log_safe(close), _TD_WEEK))


def vif_110_ols_slope_21d_flip(close: pd.Series) -> pd.Series:
    """Binary: 21-day OLS slope changed sign today."""
    return _sign_flip(_linslope(_log_safe(close), _TD_MON))


def vif_111_ols_slope_63d_flip(close: pd.Series) -> pd.Series:
    """Binary: 63-day OLS slope changed sign today."""
    return _sign_flip(_linslope(_log_safe(close), _TD_QTR))


def vif_112_days_since_ols5_slope_flip(close: pd.Series) -> pd.Series:
    """Days since last 5-day OLS slope sign-flip."""
    return _days_since_flip(vif_109_ols_slope_5d_flip(close))


def vif_113_days_since_ols21_slope_flip(close: pd.Series) -> pd.Series:
    """Days since last 21-day OLS slope sign-flip."""
    return _days_since_flip(vif_110_ols_slope_21d_flip(close))


def vif_114_days_since_ols63_slope_flip(close: pd.Series) -> pd.Series:
    """Days since last 63-day OLS slope sign-flip."""
    return _days_since_flip(vif_111_ols_slope_63d_flip(close))


def vif_115_ols5_slope_flip_count_63d(close: pd.Series) -> pd.Series:
    """Count of 5-day OLS slope sign-flips in trailing 63 days."""
    return _rolling_count(vif_109_ols_slope_5d_flip(close), _TD_QTR)


def vif_116_ols21_slope_flip_count_252d(close: pd.Series) -> pd.Series:
    """Count of 21-day OLS slope sign-flips in trailing 252 days."""
    return _rolling_count(vif_110_ols_slope_21d_flip(close), _TD_YEAR)


def vif_117_ols5_slope_to_neg_flip(close: pd.Series) -> pd.Series:
    """Binary: 5-day OLS slope flipped from positive to negative."""
    slp = _linslope(_log_safe(close), _TD_WEEK)
    sg = np.sign(slp)
    return ((sg < 0) & (sg.shift(1) > 0)).astype(float)


def vif_118_ols21_slope_to_neg_flip(close: pd.Series) -> pd.Series:
    """Binary: 21-day OLS slope flipped from positive to negative."""
    slp = _linslope(_log_safe(close), _TD_MON)
    sg = np.sign(slp)
    return ((sg < 0) & (sg.shift(1) > 0)).astype(float)


def vif_119_ols5_ols21_slope_sign_agree(close: pd.Series) -> pd.Series:
    """Binary: 5-day and 21-day OLS slopes have the same sign (trend alignment)."""
    s5 = np.sign(_linslope(_log_safe(close), _TD_WEEK))
    s21 = np.sign(_linslope(_log_safe(close), _TD_MON))
    return (s5 == s21).astype(float)


def vif_120_all_ols_slopes_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: 5-, 21-, and 63-day OLS slopes all negative simultaneously."""
    s5 = _linslope(_log_safe(close), _TD_WEEK)
    s21 = _linslope(_log_safe(close), _TD_MON)
    s63 = _linslope(_log_safe(close), _TD_QTR)
    return ((s5 < 0) & (s21 < 0) & (s63 < 0)).astype(float)


# --- Group I (121-135): Regime duration, alternation, and composite signals ---

def vif_121_consec_neg_vel_regime_ema5(close: pd.Series) -> pd.Series:
    """Consecutive days in negative EMA-5 velocity regime."""
    cond = _velocity(close, 5) < 0
    return _consec_true(cond)


def vif_122_consec_pos_vel_regime_ema5(close: pd.Series) -> pd.Series:
    """Consecutive days in positive EMA-5 velocity regime."""
    cond = _velocity(close, 5) > 0
    return _consec_true(cond)


def vif_123_consec_neg_vel_regime_ema63(close: pd.Series) -> pd.Series:
    """Consecutive days in negative EMA-63 velocity regime."""
    cond = _velocity(close, _TD_QTR) < 0
    return _consec_true(cond)


def vif_124_neg_regime_ema21_norm_252d(close: pd.Series) -> pd.Series:
    """Current negative EMA-21 regime streak normalized by 252-day avg duration."""
    cond = _velocity(close, _TD_MON) < 0
    streak = _consec_true(cond)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def vif_125_max_neg_regime_ema21_252d(close: pd.Series) -> pd.Series:
    """Maximum negative EMA-21 regime duration within trailing 252 days."""
    cond = _velocity(close, _TD_MON) < 0
    streak = _consec_true(cond)
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v > 0:
                cur = int(v)
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return streak.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def vif_126_neg_regime_ema5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current negative EMA-5 regime streak in 252-day distribution."""
    cond = _velocity(close, 5) < 0
    streak = _consec_true(cond)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_127_vel_regime_composite_neg_score(close: pd.Series) -> pd.Series:
    """Composite: sum of negative-regime flags for EMA-5, EMA-21, EMA-63 (0-3)."""
    v5 = (_velocity(close, 5) < 0).astype(float)
    v21 = (_velocity(close, _TD_MON) < 0).astype(float)
    v63 = (_velocity(close, _TD_QTR) < 0).astype(float)
    return v5 + v21 + v63


def vif_128_inflection_after_long_neg_regime(close: pd.Series) -> pd.Series:
    """Binary: bullish EMA-21 flip occurring after >= 21 consecutive neg-regime days."""
    cond = _velocity(close, _TD_MON) < 0
    streak = _consec_true(cond)
    sg = np.sign(_velocity(close, _TD_MON))
    pos_flip = (sg > 0) & (sg.shift(1) < 0)
    long_streak = streak.shift(1) >= _TD_MON
    return (pos_flip & long_streak).astype(float)


def vif_129_vel_ema5_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current EMA-5 velocity vs trailing 252-day distribution."""
    v = _velocity(close, 5)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vif_130_vel_ema21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current EMA-21 velocity vs trailing 252-day distribution."""
    v = _velocity(close, _TD_MON)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vif_131_vel_ema5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current EMA-5 velocity within trailing 252 days."""
    v = _velocity(close, 5)
    return v.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_132_vel_ema21_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current EMA-21 velocity within trailing 252 days."""
    v = _velocity(close, _TD_MON)
    return v.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_133_days_since_ols5_neg_flip(close: pd.Series) -> pd.Series:
    """Days since 5-day OLS slope last turned negative."""
    slp = _linslope(_log_safe(close), _TD_WEEK)
    sg = np.sign(slp)
    flip = ((sg < 0) & (sg.shift(1) > 0)).astype(float)
    return _days_since_flip(flip)


def vif_134_days_since_ols21_neg_flip(close: pd.Series) -> pd.Series:
    """Days since 21-day OLS slope last turned negative."""
    slp = _linslope(_log_safe(close), _TD_MON)
    sg = np.sign(slp)
    flip = ((sg < 0) & (sg.shift(1) > 0)).astype(float)
    return _days_since_flip(flip)


def vif_135_ols_slope_all_neg_consec(close: pd.Series) -> pd.Series:
    """Consecutive days with all three OLS slopes (5/21/63) negative."""
    s5 = _linslope(_log_safe(close), _TD_WEEK)
    s21 = _linslope(_log_safe(close), _TD_MON)
    s63 = _linslope(_log_safe(close), _TD_QTR)
    cond = (s5 < 0) & (s21 < 0) & (s63 < 0)
    return _consec_true(cond)


# --- Group J (136-150): Cross-span and composite inflection geometry ---

def vif_136_vel_ema5_ema21_cross_neg(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity crossed below EMA-21 velocity (short-velocity death-cross)."""
    v5 = _velocity(close, 5)
    v21 = _velocity(close, _TD_MON)
    return ((v5 < v21) & (v5.shift(1) >= v21.shift(1))).astype(float)


def vif_137_vel_ema5_ema21_cross_pos(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity crossed above EMA-21 velocity (short-velocity golden-cross)."""
    v5 = _velocity(close, 5)
    v21 = _velocity(close, _TD_MON)
    return ((v5 > v21) & (v5.shift(1) <= v21.shift(1))).astype(float)


def vif_138_days_since_vel_ema5_below_ema21(close: pd.Series) -> pd.Series:
    """Days since EMA-5 velocity crossed below EMA-21 velocity."""
    return _days_since_flip(vif_136_vel_ema5_ema21_cross_neg(close))


def vif_139_vel_ema5_below_ema21_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity currently below EMA-21 velocity."""
    return (_velocity(close, 5) < _velocity(close, _TD_MON)).astype(float)


def vif_140_vel_ema21_below_ema63_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-21 velocity currently below EMA-63 velocity."""
    return (_velocity(close, _TD_MON) < _velocity(close, _TD_QTR)).astype(float)


def vif_141_vel_all_span_cascade_neg(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 vel < EMA-21 vel < EMA-63 vel (velocity cascade — all falling fast)."""
    v5 = _velocity(close, 5)
    v21 = _velocity(close, _TD_MON)
    v63 = _velocity(close, _TD_QTR)
    return ((v5 < v21) & (v21 < v63)).astype(float)


def vif_142_inflection_cluster_21d(close: pd.Series) -> pd.Series:
    """Binary: three or more EMA-5 velocity flips within the last 21 days (choppy regime)."""
    cnt = _rolling_count(((np.sign(_velocity(close, 5)) != np.sign(_velocity(close, 5)).shift(1)) &
                          _velocity(close, 5).notna()).astype(float), _TD_MON)
    return (cnt >= 3).astype(float)


def vif_143_inflection_drought_63d(close: pd.Series) -> pd.Series:
    """Binary: zero EMA-21 velocity flips in the last 63 days (entrenched regime)."""
    cnt = _rolling_count(
        _sign_flip(_velocity(close, _TD_MON)), _TD_QTR)
    return (cnt == 0).astype(float)


def vif_144_vel_ema5_cross_zero_count_21d(close: pd.Series) -> pd.Series:
    """Count of times EMA-5 velocity crossed zero in the last 21 days."""
    v = _velocity(close, 5)
    cross = _sign_flip(v)
    return _rolling_count(cross, _TD_MON)


def vif_145_inflection_after_extreme_vel(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity flip occurring when prior-day velocity was in bottom 10% (extreme low)."""
    v = _velocity(close, 5)
    pct10 = v.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    extreme_prior = (v.shift(1) <= pct10.shift(1)).fillna(False)
    flip = _sign_flip(v).astype(bool)
    return (flip & extreme_prior).astype(float)


def vif_146_neg_inflection_density_score(close: pd.Series) -> pd.Series:
    """Rolling 63-day density of bearish EMA-21 inflections (neg flips per 21 days)."""
    neg_flips = ((np.sign(_velocity(close, _TD_MON)) < 0) &
                 (np.sign(_velocity(close, _TD_MON)).shift(1) > 0)).astype(float)
    return _rolling_count(neg_flips, _TD_QTR) / 3.0


def vif_147_pos_inflection_density_score(close: pd.Series) -> pd.Series:
    """Rolling 63-day density of bullish EMA-21 inflections (pos flips per 21 days)."""
    pos_flips = ((np.sign(_velocity(close, _TD_MON)) > 0) &
                 (np.sign(_velocity(close, _TD_MON)).shift(1) < 0)).astype(float)
    return _rolling_count(pos_flips, _TD_QTR) / 3.0


def vif_148_vel_ema5_at_new_price_low(close: pd.Series) -> pd.Series:
    """EMA-5 velocity on days when close sets a new 63-day low (velocity at distress point)."""
    v = _velocity(close, 5)
    new_low = close < close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return v.where(new_low, np.nan).ffill()


def vif_149_vel_divergence_price_vs_high(close: pd.Series, high: pd.Series) -> pd.Series:
    """EMA-5 velocity of close minus EMA-5 velocity of high (close losing to high = bearish)."""
    vel_c = _velocity(close, 5)
    vel_h = _ewm_mean(_log_safe(high).diff(1), _TD_WEEK)
    return vel_c - vel_h


def vif_150_composite_inflection_distress(close: pd.Series) -> pd.Series:
    """Composite inflection distress: negative regime score + inflection density + days-since norm."""
    neg_score = vif_127_vel_regime_composite_neg_score(close) / 3.0
    density = vif_146_neg_inflection_density_score(close)
    days_since = _days_since_flip(((np.sign(_velocity(close, _TD_MON)) > 0) &
                                   (np.sign(_velocity(close, _TD_MON)).shift(1) < 0)).astype(float))
    days_norm = _safe_div(days_since, _rolling_mean(days_since.fillna(0), _TD_YEAR))
    return neg_score + density + days_norm.fillna(0)


# ── Registry ──────────────────────────────────────────────────────────────────

VELOCITY_INFLECTION_REGISTRY_076_150 = {
    "vif_076_roc5_zero_cross_neg": {"inputs": ["close"], "func": vif_076_roc5_zero_cross_neg},
    "vif_077_roc5_zero_cross_pos": {"inputs": ["close"], "func": vif_077_roc5_zero_cross_pos},
    "vif_078_roc21_zero_cross_neg": {"inputs": ["close"], "func": vif_078_roc21_zero_cross_neg},
    "vif_079_roc21_zero_cross_pos": {"inputs": ["close"], "func": vif_079_roc21_zero_cross_pos},
    "vif_080_roc63_zero_cross_neg": {"inputs": ["close"], "func": vif_080_roc63_zero_cross_neg},
    "vif_081_days_since_roc5_zero_cross": {"inputs": ["close"], "func": vif_081_days_since_roc5_zero_cross},
    "vif_082_days_since_roc21_zero_cross": {"inputs": ["close"], "func": vif_082_days_since_roc21_zero_cross},
    "vif_083_roc5_sign": {"inputs": ["close"], "func": vif_083_roc5_sign},
    "vif_084_roc21_sign": {"inputs": ["close"], "func": vif_084_roc21_sign},
    "vif_085_roc63_sign": {"inputs": ["close"], "func": vif_085_roc63_sign},
    "vif_086_roc_sign_disagreement_5_63": {"inputs": ["close"], "func": vif_086_roc_sign_disagreement_5_63},
    "vif_087_all_roc_neg_flag": {"inputs": ["close"], "func": vif_087_all_roc_neg_flag},
    "vif_088_roc5_zero_cross_count_63d": {"inputs": ["close"], "func": vif_088_roc5_zero_cross_count_63d},
    "vif_089_roc21_zero_cross_count_252d": {"inputs": ["close"], "func": vif_089_roc21_zero_cross_count_252d},
    "vif_090_roc5_neg_cross_count_63d": {"inputs": ["close"], "func": vif_090_roc5_neg_cross_count_63d},
    "vif_091_vol_wtd_vel_ema5_sign": {"inputs": ["close", "volume"], "func": vif_091_vol_wtd_vel_ema5_sign},
    "vif_092_vol_wtd_vel_ema5_flip": {"inputs": ["close", "volume"], "func": vif_092_vol_wtd_vel_ema5_flip},
    "vif_093_vol_wtd_vel_to_neg_flip": {"inputs": ["close", "volume"], "func": vif_093_vol_wtd_vel_to_neg_flip},
    "vif_094_high_vel_ema5_sign": {"inputs": ["close", "high"], "func": vif_094_high_vel_ema5_sign},
    "vif_095_low_vel_ema5_sign": {"inputs": ["close", "low"], "func": vif_095_low_vel_ema5_sign},
    "vif_096_high_vel_flip_to_neg": {"inputs": ["close", "high"], "func": vif_096_high_vel_flip_to_neg},
    "vif_097_low_vel_flip_to_neg": {"inputs": ["close", "low"], "func": vif_097_low_vel_flip_to_neg},
    "vif_098_range_vel_flip": {"inputs": ["close", "high", "low"], "func": vif_098_range_vel_flip},
    "vif_099_close_minus_open_vel_flip": {"inputs": ["close", "open"], "func": vif_099_close_minus_open_vel_flip},
    "vif_100_days_since_vol_wtd_vel_flip": {"inputs": ["close", "volume"], "func": vif_100_days_since_vol_wtd_vel_flip},
    "vif_101_vol_wtd_vel_flip_count_63d": {"inputs": ["close", "volume"], "func": vif_101_vol_wtd_vel_flip_count_63d},
    "vif_102_high_vel_flip_count_63d": {"inputs": ["close", "high"], "func": vif_102_high_vel_flip_count_63d},
    "vif_103_low_vel_flip_count_63d": {"inputs": ["close", "low"], "func": vif_103_low_vel_flip_count_63d},
    "vif_104_high_low_vel_regime_agree": {"inputs": ["close", "high", "low"], "func": vif_104_high_low_vel_regime_agree},
    "vif_105_open_vel_flip_to_neg": {"inputs": ["close", "open"], "func": vif_105_open_vel_flip_to_neg},
    "vif_106_ols_slope_5d_sign": {"inputs": ["close"], "func": vif_106_ols_slope_5d_sign},
    "vif_107_ols_slope_21d_sign": {"inputs": ["close"], "func": vif_107_ols_slope_21d_sign},
    "vif_108_ols_slope_63d_sign": {"inputs": ["close"], "func": vif_108_ols_slope_63d_sign},
    "vif_109_ols_slope_5d_flip": {"inputs": ["close"], "func": vif_109_ols_slope_5d_flip},
    "vif_110_ols_slope_21d_flip": {"inputs": ["close"], "func": vif_110_ols_slope_21d_flip},
    "vif_111_ols_slope_63d_flip": {"inputs": ["close"], "func": vif_111_ols_slope_63d_flip},
    "vif_112_days_since_ols5_slope_flip": {"inputs": ["close"], "func": vif_112_days_since_ols5_slope_flip},
    "vif_113_days_since_ols21_slope_flip": {"inputs": ["close"], "func": vif_113_days_since_ols21_slope_flip},
    "vif_114_days_since_ols63_slope_flip": {"inputs": ["close"], "func": vif_114_days_since_ols63_slope_flip},
    "vif_115_ols5_slope_flip_count_63d": {"inputs": ["close"], "func": vif_115_ols5_slope_flip_count_63d},
    "vif_116_ols21_slope_flip_count_252d": {"inputs": ["close"], "func": vif_116_ols21_slope_flip_count_252d},
    "vif_117_ols5_slope_to_neg_flip": {"inputs": ["close"], "func": vif_117_ols5_slope_to_neg_flip},
    "vif_118_ols21_slope_to_neg_flip": {"inputs": ["close"], "func": vif_118_ols21_slope_to_neg_flip},
    "vif_119_ols5_ols21_slope_sign_agree": {"inputs": ["close"], "func": vif_119_ols5_ols21_slope_sign_agree},
    "vif_120_all_ols_slopes_neg_flag": {"inputs": ["close"], "func": vif_120_all_ols_slopes_neg_flag},
    "vif_121_consec_neg_vel_regime_ema5": {"inputs": ["close"], "func": vif_121_consec_neg_vel_regime_ema5},
    "vif_122_consec_pos_vel_regime_ema5": {"inputs": ["close"], "func": vif_122_consec_pos_vel_regime_ema5},
    "vif_123_consec_neg_vel_regime_ema63": {"inputs": ["close"], "func": vif_123_consec_neg_vel_regime_ema63},
    "vif_124_neg_regime_ema21_norm_252d": {"inputs": ["close"], "func": vif_124_neg_regime_ema21_norm_252d},
    "vif_125_max_neg_regime_ema21_252d": {"inputs": ["close"], "func": vif_125_max_neg_regime_ema21_252d},
    "vif_126_neg_regime_ema5_pct_rank_252d": {"inputs": ["close"], "func": vif_126_neg_regime_ema5_pct_rank_252d},
    "vif_127_vel_regime_composite_neg_score": {"inputs": ["close"], "func": vif_127_vel_regime_composite_neg_score},
    "vif_128_inflection_after_long_neg_regime": {"inputs": ["close"], "func": vif_128_inflection_after_long_neg_regime},
    "vif_129_vel_ema5_zscore_252d": {"inputs": ["close"], "func": vif_129_vel_ema5_zscore_252d},
    "vif_130_vel_ema21_zscore_252d": {"inputs": ["close"], "func": vif_130_vel_ema21_zscore_252d},
    "vif_131_vel_ema5_pct_rank_252d": {"inputs": ["close"], "func": vif_131_vel_ema5_pct_rank_252d},
    "vif_132_vel_ema21_pct_rank_252d": {"inputs": ["close"], "func": vif_132_vel_ema21_pct_rank_252d},
    "vif_133_days_since_ols5_neg_flip": {"inputs": ["close"], "func": vif_133_days_since_ols5_neg_flip},
    "vif_134_days_since_ols21_neg_flip": {"inputs": ["close"], "func": vif_134_days_since_ols21_neg_flip},
    "vif_135_ols_slope_all_neg_consec": {"inputs": ["close"], "func": vif_135_ols_slope_all_neg_consec},
    "vif_136_vel_ema5_ema21_cross_neg": {"inputs": ["close"], "func": vif_136_vel_ema5_ema21_cross_neg},
    "vif_137_vel_ema5_ema21_cross_pos": {"inputs": ["close"], "func": vif_137_vel_ema5_ema21_cross_pos},
    "vif_138_days_since_vel_ema5_below_ema21": {"inputs": ["close"], "func": vif_138_days_since_vel_ema5_below_ema21},
    "vif_139_vel_ema5_below_ema21_flag": {"inputs": ["close"], "func": vif_139_vel_ema5_below_ema21_flag},
    "vif_140_vel_ema21_below_ema63_flag": {"inputs": ["close"], "func": vif_140_vel_ema21_below_ema63_flag},
    "vif_141_vel_all_span_cascade_neg": {"inputs": ["close"], "func": vif_141_vel_all_span_cascade_neg},
    "vif_142_inflection_cluster_21d": {"inputs": ["close"], "func": vif_142_inflection_cluster_21d},
    "vif_143_inflection_drought_63d": {"inputs": ["close"], "func": vif_143_inflection_drought_63d},
    "vif_144_vel_ema5_cross_zero_count_21d": {"inputs": ["close"], "func": vif_144_vel_ema5_cross_zero_count_21d},
    "vif_145_inflection_after_extreme_vel": {"inputs": ["close"], "func": vif_145_inflection_after_extreme_vel},
    "vif_146_neg_inflection_density_score": {"inputs": ["close"], "func": vif_146_neg_inflection_density_score},
    "vif_147_pos_inflection_density_score": {"inputs": ["close"], "func": vif_147_pos_inflection_density_score},
    "vif_148_vel_ema5_at_new_price_low": {"inputs": ["close"], "func": vif_148_vel_ema5_at_new_price_low},
    "vif_149_vel_divergence_price_vs_high": {"inputs": ["close", "high"], "func": vif_149_vel_divergence_price_vs_high},
    "vif_150_composite_inflection_distress": {"inputs": ["close"], "func": vif_150_composite_inflection_distress},
}
