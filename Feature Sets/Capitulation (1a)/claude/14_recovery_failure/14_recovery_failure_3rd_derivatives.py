"""
14_recovery_failure — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative recovery-failure features — acceleration of
bounce-fade velocity, lower-high structure worsening, and retracement decay inflection.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _local_peak(s: pd.Series, lookback: int) -> pd.Series:
    return s.shift(1).rolling(lookback, min_periods=max(1, lookback // 2)).max()


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
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept.

def rfl_drv3_001_bounce_ret_5d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day bounce return (acceleration of bounce-velocity change)."""
    r = close.pct_change(_TD_WEEK)
    vel = r.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_002_bounce_ret_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day return velocity (jerk in monthly bounce change)."""
    r = close.pct_change(_TD_MON)
    vel = r.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_003_retracement_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d retracement fraction (acceleration of bounce failure)."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_004_retracement_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63d retracement fraction."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_005_lower_high_frac_21d_5d_diff_5d_diff(high: pd.Series) -> pd.Series:
    """Second 5-day diff of lower-high fraction (21d) — jerk in structural deterioration."""
    frac = _rolling_count_true(high < high.shift(1), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_006_bounce_fade_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d-peak bounce fade (acceleration of fade deepening)."""
    pk21 = _local_peak(close, _TD_MON)
    fade = _safe_div(close - pk21, pk21)
    vel = fade.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_007_vol_up_down_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d up/down volume ratio."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(up_vol, dn_vol)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_008_up_day_count_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of up-day count in 21d (acceleration of up-day frequency change)."""
    cnt = _rolling_count_true(close > close.shift(1), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_009_ema_spread_5_21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA5-EMA21 spread (jerk in short vs medium trend gap)."""
    ema5 = _ewm_mean(close, _TD_WEEK)
    ema21 = _ewm_mean(close, _TD_MON)
    spread = _safe_div(ema5 - ema21, ema21)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_010_bounce_ret_5d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 5-day returns over 21 days."""
    r = close.pct_change(_TD_WEEK)
    slp = _linslope(r, _TD_MON)
    return slp.diff(_TD_WEEK)


def rfl_drv3_011_failed_rally_rate_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in failed-rally rate."""
    up = (close > close.shift(1)).astype(float)
    fail = (up.shift(1) * (close < close.shift(1)).astype(float))
    up_sum = _rolling_sum(up.shift(1), _TD_QTR)
    fail_sum = _rolling_sum(fail, _TD_QTR)
    rate = _safe_div(fail_sum, up_sum.replace(0, np.nan))
    vel21 = rate.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_012_up_leg_dn_leg_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of up-leg/down-leg ratio (21d)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_sum = lr.where(lr > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    dn_sum = (-lr).where(lr < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    ratio = _safe_div(up_sum, dn_sum.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_013_retracement_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 126d retracement fraction."""
    pk = _rolling_max(close, _TD_HALF)
    tr = _rolling_min(close, _TD_HALF)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_014_lower_high_frac_63d_21d_diff_5d_diff(high: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d lower-high fraction."""
    frac = _rolling_count_true(high < high.shift(1), _TD_QTR) / _TD_QTR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_015_ema21_slope_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA21 slope (acceleration of trend slope change)."""
    ema21 = _ewm_mean(close, _TD_MON)
    slp = ema21.diff(_TD_WEEK)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_016_lower_high_streak_5d_diff_5d_diff(high: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive lower-highs streak."""
    streak = _consec_streak(high < high.shift(1))
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_017_vol_decline_bounce_ratio_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d down/up volume ratio."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(dn_vol, up_vol.replace(0, np.nan))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_018_close_vs_sma21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-relative-to-SMA21 (jerk in MA divergence)."""
    sma21 = _rolling_mean(close, _TD_MON)
    rel = _safe_div(close - sma21, sma21)
    vel = rel.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_019_retracement_pct_21d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d retracement fraction over 63d window."""
    pk = _rolling_max(close, _TD_MON)
    tr = _rolling_min(close, _TD_MON)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    slp = _linslope(frac, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rfl_drv3_020_up_vs_dn_magnitude_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of avg-up/avg-down day magnitude ratio (21d)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_avg = lr.where(lr > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dn_avg = (-lr).where(lr < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(up_avg, dn_avg)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_021_bounce_attempt_count_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d bounce attempt count."""
    ret = close.pct_change(1)
    is_start = ((ret > 0) & (ret.shift(1) <= 0)).astype(float)
    cnt = _rolling_sum(is_start, _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_022_peak_drawdown_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown from 63d peak (acceleration of retreat from peak)."""
    pk = _rolling_max(close, _TD_QTR)
    dd = _safe_div(close - pk, pk)
    vel = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_023_bounce_ret_5d_slope_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the OLS slope of 5-day returns (inflection in bounce trend)."""
    r = close.pct_change(_TD_WEEK)
    slp = _linslope(r, _TD_MON)
    return _linslope(slp, _TD_MON)


def rfl_drv3_024_ema_spread_21_63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA21-EMA63 spread (jerk in intermediate vs long trend gap)."""
    ema21 = _ewm_mean(close, _TD_MON)
    ema63 = _ewm_mean(close, _TD_QTR)
    spread = _safe_div(ema21 - ema63, ema63)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_025_high_to_close_ratio_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series) -> pd.Series:
    """Second 5-day diff of avg high/close ratio (21d) — acceleration of intraday fade change."""
    ratio = _safe_div(close, high)
    avg = _rolling_mean(ratio, _TD_MON)
    vel = avg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_026_bounce_ret_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day bounce return (acceleration of quarter-bounce velocity)."""
    r = close.pct_change(_TD_QTR)
    vel = r.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_027_bounce_ret_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d bounce return (jerk in quarter-bounce)."""
    r = close.pct_change(_TD_QTR)
    vel21 = r.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_028_bounce_ret_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 126d bounce return (acceleration of half-year bounce change)."""
    r = close.pct_change(_TD_HALF)
    vel = r.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_029_retracement_126d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 126d retracement fraction."""
    pk = _rolling_max(close, _TD_HALF)
    tr = _rolling_min(close, _TD_HALF)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_030_lower_high_frac_126d_21d_diff_5d_diff(high: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 126d lower-high fraction."""
    frac = _rolling_count_true(high < high.shift(1), _TD_HALF) / _TD_HALF
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_031_up_day_count_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d up-day count (acceleration of frequency change)."""
    cnt = _rolling_count_true(close > close.shift(1), _TD_QTR)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_032_down_day_ret_avg_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of avg down-day return in 21d (acceleration of decline worsening)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    dn = lr.where(lr < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    vel = dn.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_033_up_day_fraction_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of up-day fraction in 21d."""
    frac = _rolling_count_true(close > close.shift(1), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_034_bounce_fade_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of bounce-fade from 63d peak (acceleration of quarterly fade)."""
    pk63 = _local_peak(close, _TD_QTR)
    fade = _safe_div(close - pk63, pk63)
    vel = fade.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_035_close_vs_sma50_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close relative to 50d SMA (jerk in MA divergence)."""
    sma50 = _rolling_mean(close, 50)
    rel = _safe_div(close - sma50, sma50)
    vel = rel.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_036_ema_spread_21_63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA21-EMA63 spread (acceleration of intermediate/long gap change)."""
    ema21 = _ewm_mean(close, _TD_MON)
    ema63 = _ewm_mean(close, _TD_QTR)
    spread = _safe_div(ema21 - ema63, ema63)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_037_vol_on_up_days_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of avg up-day volume in 21d (acceleration of demand change)."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    vel = up_vol.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_038_vol_up_vs_down_ratio_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d up/down volume ratio (jerk in vol imbalance)."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(up_vol, dn_vol)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_039_close_vs_21d_high_5d_diff_5d_diff(close: pd.Series, high: pd.Series) -> pd.Series:
    """Second 5-day diff of close relative to 21d high (acceleration of distance from local high)."""
    hh21 = _rolling_max(high, _TD_MON)
    rel = _safe_div(close - hh21, hh21)
    vel = rel.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_040_net_log_return_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of net 21d log return (acceleration of medium-term momentum change)."""
    lr = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    vel = lr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_041_net_log_return_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d log return (jerk in quarterly momentum)."""
    lr = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    vel21 = lr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_042_up_leg_dn_leg_ratio_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d up/down ratio (jerk in quarterly asymmetry)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_sum = lr.where(lr > 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    dn_sum = (-lr).where(lr < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    ratio = _safe_div(up_sum, dn_sum.replace(0, np.nan))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_043_lower_high_count_21d_5d_diff_5d_diff(high: pd.Series) -> pd.Series:
    """Second 5-day diff of lower-high count in 21d."""
    cnt = _rolling_count_true(high < high.shift(1), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_044_close_pct_from_52wk_high_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close as fraction of 252d rolling high (acceleration of drift from annual high)."""
    hh252 = _rolling_max(close, _TD_YEAR)
    rel = _safe_div(close, hh252)
    vel = rel.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_045_peak_drawdown_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown from 126d peak."""
    pk = _rolling_max(close, _TD_HALF)
    dd = _safe_div(close - pk, pk)
    vel = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_046_intraday_high_reversal_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series) -> pd.Series:
    """Second 5-day diff of avg (high-close)/close over 21 days."""
    rev = _safe_div(high - close, close)
    avg = _rolling_mean(rev, _TD_MON)
    vel = avg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_047_open_to_close_fade_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of avg open-to-close fade in 21d."""
    fade = _safe_div(open - close, open)
    avg = _rolling_mean(fade, _TD_MON)
    vel = avg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_048_close_to_range_pos_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of close position in 21d range."""
    hh = _rolling_max(high, _TD_MON)
    ll = _rolling_min(low, _TD_MON)
    pos = _safe_div(close - ll, (hh - ll).replace(0, np.nan))
    vel = pos.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_049_high_vol_decline_count_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of high-volume down-day count in 21d."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    cnt = _rolling_count_true((ret < 0) & (volume > avg_vol), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_050_consec_up_days_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive up-days streak (acceleration of streak change)."""
    streak = _consec_streak(close > close.shift(1))
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_051_rally_fails_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of failed-rally count in 21d."""
    up = (close > close.shift(1)).astype(float)
    dn_next = (close.shift(1) > close).astype(float)
    fail = up.shift(1) * dn_next
    cnt = _rolling_sum(fail, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_052_vol_decline_sum_vs_bounce_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of down-vol/up-vol ratio (21d)."""
    ret = close.pct_change(1)
    up_s = volume.where(ret > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    dn_s = volume.where(ret < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    ratio = _safe_div(dn_s, up_s.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_053_retracement_decay_score_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of retracement decay score (21d retr - 63d retr)."""
    pk21 = _rolling_max(close, _TD_MON); tr21 = _rolling_min(close, _TD_MON)
    r21 = _safe_div(close - tr21, (pk21 - tr21).replace(0, np.nan))
    pk63 = _rolling_max(close, _TD_QTR); tr63 = _rolling_min(close, _TD_QTR)
    r63 = _safe_div(close - tr63, (pk63 - tr63).replace(0, np.nan))
    decay = r21 - r63
    vel = decay.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_054_bounce_decay_score_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of bounce-decay score (mx21/mx63 log-return ratio)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    mx21 = lr.rolling(_TD_MON, min_periods=1).max()
    mx63 = lr.rolling(_TD_QTR, min_periods=1).max()
    score = _safe_div(mx21, mx63.replace(0, np.nan))
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_055_bounce_ret_5d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 5-day returns over 63-day window."""
    r = close.pct_change(_TD_WEEK)
    slp = _linslope(r, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rfl_drv3_056_retracement_pct_63d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63d retracement fraction over 21d window."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    slp = _linslope(frac, _TD_MON)
    return slp.diff(_TD_WEEK)


def rfl_drv3_057_lower_high_count_63d_5d_diff_5d_diff(high: pd.Series) -> pd.Series:
    """Second 5-day diff of lower-high count in 63d."""
    cnt = _rolling_count_true(high < high.shift(1), _TD_QTR)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_058_ema_spread_5_63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA5-EMA63 spread (acceleration of short vs long trend gap)."""
    ema5 = _ewm_mean(close, _TD_WEEK)
    ema63 = _ewm_mean(close, _TD_QTR)
    spread = _safe_div(ema5 - ema63, ema63)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_059_vol_weighted_bounce_ret_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of volume-weighted up-day return in 21d."""
    ret = close.pct_change(1)
    up_ret = ret.where(ret > 0, 0.0)
    vol_up = volume.where(ret > 0, 0.0)
    vw = _safe_div(
        (up_ret * vol_up).rolling(_TD_MON, min_periods=1).sum(),
        vol_up.rolling(_TD_MON, min_periods=1).sum().replace(0, np.nan)
    )
    vel = vw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_060_bounce_attempt_count_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of bounce attempt count in 63d (acceleration of attempt frequency)."""
    ret = close.pct_change(1)
    is_start = ((ret > 0) & (ret.shift(1) <= 0)).astype(float)
    cnt = _rolling_sum(is_start, _TD_QTR)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_061_gap_up_fade_count_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of gap-up fade count in 21d."""
    cond = (open > close.shift(1)) & (close < close.shift(1))
    cnt = _rolling_count_true(cond, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_062_up_day_fraction_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d up-day fraction."""
    frac = _rolling_count_true(close > close.shift(1), _TD_QTR) / _TD_QTR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_063_close_vs_sma21_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of (close/SMA21) relative measure over 21 days."""
    sma21 = _rolling_mean(close, _TD_MON)
    rel = _safe_div(close - sma21, sma21)
    slp = _linslope(rel, _TD_MON)
    return slp.diff(_TD_WEEK)


def rfl_drv3_064_close_vs_sma63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close relative to 63d SMA (jerk in long MA divergence)."""
    sma63 = _rolling_mean(close, _TD_QTR)
    rel = _safe_div(close - sma63, sma63)
    vel = rel.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_065_intraday_bounce_frac_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of avg intraday bounce fraction over 21 days."""
    num = (close - low).clip(lower=0)
    den = (open - low).abs().replace(0, np.nan)
    frac = _safe_div(num, den).rolling(_TD_MON, min_periods=1).mean()
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_066_bounce_retracement_ratio_5d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d bounce/prior-decline ratio (jerk in retracement velocity)."""
    bounce = close.pct_change(_TD_WEEK)
    prior = _safe_div(close.shift(_TD_WEEK) - close.shift(10), close.shift(10))
    ratio = _safe_div(bounce, (-prior).clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_067_consec_lower_highs_daily_5d_diff_5d_diff(high: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive daily lower-highs streak."""
    streak = _consec_streak(high < high.shift(1))
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_068_close_to_range_pos_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in close position within 63d range."""
    hh = _rolling_max(high, _TD_QTR)
    ll = _rolling_min(low, _TD_QTR)
    pos = _safe_div(close - ll, (hh - ll).replace(0, np.nan))
    vel21 = pos.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rfl_drv3_069_failed_rally_rate_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 63d failed-rally rate (inflection in failure trend)."""
    up = (close > close.shift(1)).astype(float)
    fail = up.shift(1) * (close < close.shift(1)).astype(float)
    up_sum = _rolling_sum(up.shift(1), _TD_QTR)
    fail_sum = _rolling_sum(fail, _TD_QTR)
    rate = _safe_div(fail_sum, up_sum.replace(0, np.nan))
    return _linslope(rate, _TD_MON)


def rfl_drv3_070_vol_on_down_days_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of avg down-day volume in 21d."""
    ret = close.pct_change(1)
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    vel = dn_vol.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_071_close_vs_sma200_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close relative to 200d SMA (jerk in long-term MA divergence)."""
    sma200 = _rolling_mean(close, 200)
    rel = _safe_div(close - sma200, sma200)
    vel = rel.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rfl_drv3_072_up_leg_dn_leg_ratio_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 21d up-leg/down-leg return ratio."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_sum = lr.where(lr > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    dn_sum = (-lr).where(lr < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    ratio = _safe_div(up_sum, dn_sum.replace(0, np.nan))
    return _linslope(ratio, _TD_MON)


def rfl_drv3_073_retracement_126d_5d_diff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the 5-day velocity of 126d retracement fraction."""
    pk = _rolling_max(close, _TD_HALF)
    tr = _rolling_min(close, _TD_HALF)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    vel5 = frac.diff(_TD_WEEK)
    return vel5.diff(_TD_MON)


def rfl_drv3_074_bounce_ret_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day bounce return over trailing 63-day window."""
    r = close.pct_change(_TD_MON)
    return _linslope(r, _TD_QTR)


def rfl_drv3_075_lower_high_frac_21d_slope_63d(high: pd.Series) -> pd.Series:
    """OLS slope of 21d lower-high fraction over trailing 63-day window."""
    frac = _rolling_count_true(high < high.shift(1), _TD_MON) / _TD_MON
    return _linslope(frac, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

RECOVERY_FAILURE_REGISTRY_3RD_DERIVATIVES = {
    "rfl_drv3_001_bounce_ret_5d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_001_bounce_ret_5d_5d_diff_5d_diff},
    "rfl_drv3_002_bounce_ret_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_002_bounce_ret_21d_5d_diff_5d_diff},
    "rfl_drv3_003_retracement_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_003_retracement_63d_5d_diff_5d_diff},
    "rfl_drv3_004_retracement_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_004_retracement_63d_21d_diff_5d_diff},
    "rfl_drv3_005_lower_high_frac_21d_5d_diff_5d_diff": {"inputs": ["high"], "func": rfl_drv3_005_lower_high_frac_21d_5d_diff_5d_diff},
    "rfl_drv3_006_bounce_fade_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_006_bounce_fade_21d_5d_diff_5d_diff},
    "rfl_drv3_007_vol_up_down_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv3_007_vol_up_down_ratio_21d_5d_diff_5d_diff},
    "rfl_drv3_008_up_day_count_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_008_up_day_count_21d_5d_diff_5d_diff},
    "rfl_drv3_009_ema_spread_5_21_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_009_ema_spread_5_21_5d_diff_5d_diff},
    "rfl_drv3_010_bounce_ret_5d_slope_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv3_010_bounce_ret_5d_slope_21d_5d_diff},
    "rfl_drv3_011_failed_rally_rate_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_011_failed_rally_rate_63d_21d_diff_5d_diff},
    "rfl_drv3_012_up_leg_dn_leg_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_012_up_leg_dn_leg_ratio_21d_5d_diff_5d_diff},
    "rfl_drv3_013_retracement_126d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_013_retracement_126d_5d_diff_5d_diff},
    "rfl_drv3_014_lower_high_frac_63d_21d_diff_5d_diff": {"inputs": ["high"], "func": rfl_drv3_014_lower_high_frac_63d_21d_diff_5d_diff},
    "rfl_drv3_015_ema21_slope_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_015_ema21_slope_5d_diff_5d_diff},
    "rfl_drv3_016_lower_high_streak_5d_diff_5d_diff": {"inputs": ["high"], "func": rfl_drv3_016_lower_high_streak_5d_diff_5d_diff},
    "rfl_drv3_017_vol_decline_bounce_ratio_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv3_017_vol_decline_bounce_ratio_63d_21d_diff_5d_diff},
    "rfl_drv3_018_close_vs_sma21_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_018_close_vs_sma21_5d_diff_5d_diff},
    "rfl_drv3_019_retracement_pct_21d_slope_5d_diff": {"inputs": ["close"], "func": rfl_drv3_019_retracement_pct_21d_slope_5d_diff},
    "rfl_drv3_020_up_vs_dn_magnitude_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_020_up_vs_dn_magnitude_ratio_21d_5d_diff_5d_diff},
    "rfl_drv3_021_bounce_attempt_count_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_021_bounce_attempt_count_63d_21d_diff_5d_diff},
    "rfl_drv3_022_peak_drawdown_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_022_peak_drawdown_63d_5d_diff_5d_diff},
    "rfl_drv3_023_bounce_ret_5d_slope_slope_21d": {"inputs": ["close"], "func": rfl_drv3_023_bounce_ret_5d_slope_slope_21d},
    "rfl_drv3_024_ema_spread_21_63_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_024_ema_spread_21_63_5d_diff_5d_diff},
    "rfl_drv3_025_high_to_close_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "high"], "func": rfl_drv3_025_high_to_close_ratio_21d_5d_diff_5d_diff},
    "rfl_drv3_026_bounce_ret_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_026_bounce_ret_63d_5d_diff_5d_diff},
    "rfl_drv3_027_bounce_ret_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_027_bounce_ret_63d_21d_diff_5d_diff},
    "rfl_drv3_028_bounce_ret_126d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_028_bounce_ret_126d_5d_diff_5d_diff},
    "rfl_drv3_029_retracement_126d_21d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_029_retracement_126d_21d_diff_5d_diff},
    "rfl_drv3_030_lower_high_frac_126d_21d_diff_5d_diff": {"inputs": ["high"], "func": rfl_drv3_030_lower_high_frac_126d_21d_diff_5d_diff},
    "rfl_drv3_031_up_day_count_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_031_up_day_count_63d_5d_diff_5d_diff},
    "rfl_drv3_032_down_day_ret_avg_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_032_down_day_ret_avg_21d_5d_diff_5d_diff},
    "rfl_drv3_033_up_day_fraction_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_033_up_day_fraction_21d_5d_diff_5d_diff},
    "rfl_drv3_034_bounce_fade_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_034_bounce_fade_63d_5d_diff_5d_diff},
    "rfl_drv3_035_close_vs_sma50_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_035_close_vs_sma50_5d_diff_5d_diff},
    "rfl_drv3_036_ema_spread_21_63_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_036_ema_spread_21_63_5d_diff_5d_diff},
    "rfl_drv3_037_vol_on_up_days_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv3_037_vol_on_up_days_21d_5d_diff_5d_diff},
    "rfl_drv3_038_vol_up_vs_down_ratio_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv3_038_vol_up_vs_down_ratio_63d_5d_diff_5d_diff},
    "rfl_drv3_039_close_vs_21d_high_5d_diff_5d_diff": {"inputs": ["close", "high"], "func": rfl_drv3_039_close_vs_21d_high_5d_diff_5d_diff},
    "rfl_drv3_040_net_log_return_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_040_net_log_return_21d_5d_diff_5d_diff},
    "rfl_drv3_041_net_log_return_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_041_net_log_return_63d_21d_diff_5d_diff},
    "rfl_drv3_042_up_leg_dn_leg_ratio_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_042_up_leg_dn_leg_ratio_63d_21d_diff_5d_diff},
    "rfl_drv3_043_lower_high_count_21d_5d_diff_5d_diff": {"inputs": ["high"], "func": rfl_drv3_043_lower_high_count_21d_5d_diff_5d_diff},
    "rfl_drv3_044_close_pct_from_52wk_high_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_044_close_pct_from_52wk_high_5d_diff_5d_diff},
    "rfl_drv3_045_peak_drawdown_126d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_045_peak_drawdown_126d_5d_diff_5d_diff},
    "rfl_drv3_046_intraday_high_reversal_21d_5d_diff_5d_diff": {"inputs": ["close", "high"], "func": rfl_drv3_046_intraday_high_reversal_21d_5d_diff_5d_diff},
    "rfl_drv3_047_open_to_close_fade_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": rfl_drv3_047_open_to_close_fade_21d_5d_diff_5d_diff},
    "rfl_drv3_048_close_to_range_pos_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rfl_drv3_048_close_to_range_pos_21d_5d_diff_5d_diff},
    "rfl_drv3_049_high_vol_decline_count_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv3_049_high_vol_decline_count_21d_5d_diff_5d_diff},
    "rfl_drv3_050_consec_up_days_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_050_consec_up_days_5d_diff_5d_diff},
    "rfl_drv3_051_rally_fails_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_051_rally_fails_21d_5d_diff_5d_diff},
    "rfl_drv3_052_vol_decline_sum_vs_bounce_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv3_052_vol_decline_sum_vs_bounce_21d_5d_diff_5d_diff},
    "rfl_drv3_053_retracement_decay_score_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_053_retracement_decay_score_5d_diff_5d_diff},
    "rfl_drv3_054_bounce_decay_score_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_054_bounce_decay_score_63d_5d_diff_5d_diff},
    "rfl_drv3_055_bounce_ret_5d_slope_63d_5d_diff": {"inputs": ["close"], "func": rfl_drv3_055_bounce_ret_5d_slope_63d_5d_diff},
    "rfl_drv3_056_retracement_pct_63d_slope_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv3_056_retracement_pct_63d_slope_21d_5d_diff},
    "rfl_drv3_057_lower_high_count_63d_5d_diff_5d_diff": {"inputs": ["high"], "func": rfl_drv3_057_lower_high_count_63d_5d_diff_5d_diff},
    "rfl_drv3_058_ema_spread_5_63_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_058_ema_spread_5_63_5d_diff_5d_diff},
    "rfl_drv3_059_vol_weighted_bounce_ret_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv3_059_vol_weighted_bounce_ret_21d_5d_diff_5d_diff},
    "rfl_drv3_060_bounce_attempt_count_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_060_bounce_attempt_count_63d_5d_diff_5d_diff},
    "rfl_drv3_061_gap_up_fade_count_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": rfl_drv3_061_gap_up_fade_count_21d_5d_diff_5d_diff},
    "rfl_drv3_062_up_day_fraction_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_062_up_day_fraction_63d_21d_diff_5d_diff},
    "rfl_drv3_063_close_vs_sma21_slope_5d_diff": {"inputs": ["close"], "func": rfl_drv3_063_close_vs_sma21_slope_5d_diff},
    "rfl_drv3_064_close_vs_sma63_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_064_close_vs_sma63_5d_diff_5d_diff},
    "rfl_drv3_065_intraday_bounce_frac_21d_5d_diff_5d_diff": {"inputs": ["close", "open", "low"], "func": rfl_drv3_065_intraday_bounce_frac_21d_5d_diff_5d_diff},
    "rfl_drv3_066_bounce_retracement_ratio_5d_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_066_bounce_retracement_ratio_5d_5d_diff_5d_diff},
    "rfl_drv3_067_consec_lower_highs_daily_5d_diff_5d_diff": {"inputs": ["high"], "func": rfl_drv3_067_consec_lower_highs_daily_5d_diff_5d_diff},
    "rfl_drv3_068_close_to_range_pos_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rfl_drv3_068_close_to_range_pos_63d_21d_diff_5d_diff},
    "rfl_drv3_069_failed_rally_rate_63d_slope_21d": {"inputs": ["close"], "func": rfl_drv3_069_failed_rally_rate_63d_slope_21d},
    "rfl_drv3_070_vol_on_down_days_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv3_070_vol_on_down_days_21d_5d_diff_5d_diff},
    "rfl_drv3_071_close_vs_sma200_5d_diff_5d_diff": {"inputs": ["close"], "func": rfl_drv3_071_close_vs_sma200_5d_diff_5d_diff},
    "rfl_drv3_072_up_leg_dn_leg_ratio_21d_slope_21d": {"inputs": ["close"], "func": rfl_drv3_072_up_leg_dn_leg_ratio_21d_slope_21d},
    "rfl_drv3_073_retracement_126d_5d_diff_21d_diff": {"inputs": ["close"], "func": rfl_drv3_073_retracement_126d_5d_diff_21d_diff},
    "rfl_drv3_074_bounce_ret_21d_slope_63d": {"inputs": ["close"], "func": rfl_drv3_074_bounce_ret_21d_slope_63d},
    "rfl_drv3_075_lower_high_frac_21d_slope_63d": {"inputs": ["high"], "func": rfl_drv3_075_lower_high_frac_21d_slope_63d},
}
