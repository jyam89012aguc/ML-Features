"""
14_recovery_failure — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base recovery-failure features — velocity of bounce fade,
lower-high structure, and retracement decay.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def rfl_drv2_001_bounce_ret_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day bounce return (velocity of bounce change)."""
    r = close.pct_change(_TD_WEEK)
    return r.diff(_TD_WEEK)


def rfl_drv2_002_bounce_ret_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day bounce return."""
    r = close.pct_change(_TD_MON)
    return r.diff(_TD_WEEK)


def rfl_drv2_003_retracement_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63d retracement fraction (is bounce recovery improving or failing)."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    return frac.diff(_TD_WEEK)


def rfl_drv2_004_retracement_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the 63d retracement fraction."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    return frac.diff(_TD_MON)


def rfl_drv2_005_lower_high_frac_21d_5d_diff(high: pd.Series) -> pd.Series:
    """5-day diff of lower-high fraction in 21d (is lower-high structure worsening)."""
    frac = _rolling_count_true(high < high.shift(1), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def rfl_drv2_006_lower_high_frac_63d_21d_diff(high: pd.Series) -> pd.Series:
    """21-day diff of lower-high fraction in 63d."""
    frac = _rolling_count_true(high < high.shift(1), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def rfl_drv2_007_bounce_fade_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of bounce-fade-from-21d-peak (velocity of fade deepening)."""
    pk21 = _local_peak(close, _TD_MON)
    fade = _safe_div(close - pk21, pk21)
    return fade.diff(_TD_WEEK)


def rfl_drv2_008_vol_up_down_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21d up/down volume ratio."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(up_vol, dn_vol)
    return ratio.diff(_TD_WEEK)


def rfl_drv2_009_up_day_count_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of up-day count in 21d (is up-day frequency increasing or decreasing)."""
    cnt = _rolling_count_true(close > close.shift(1), _TD_MON)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_010_ema_spread_5_21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA5-EMA21 spread (velocity of short-term trend vs medium-term)."""
    ema5 = _ewm_mean(close, _TD_WEEK)
    ema21 = _ewm_mean(close, _TD_MON)
    spread = _safe_div(ema5 - ema21, ema21)
    return spread.diff(_TD_WEEK)


def rfl_drv2_011_bounce_ret_5d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day return over trailing 21 days (trend in bounce size)."""
    r = close.pct_change(_TD_WEEK)
    return _linslope(r, _TD_MON)


def rfl_drv2_012_retracement_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 126d retracement fraction."""
    pk = _rolling_max(close, _TD_HALF)
    tr = _rolling_min(close, _TD_HALF)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    return frac.diff(_TD_WEEK)


def rfl_drv2_013_failed_rally_rate_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the failed-rally rate in 63d."""
    up = (close > close.shift(1)).astype(float)
    fail = (up.shift(1) * (close < close.shift(1)).astype(float))
    up_sum = _rolling_sum(up.shift(1), _TD_QTR)
    fail_sum = _rolling_sum(fail, _TD_QTR)
    rate = _safe_div(fail_sum, up_sum.replace(0, np.nan))
    return rate.diff(_TD_MON)


def rfl_drv2_014_up_leg_dn_leg_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d up-leg/down-leg return ratio."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_sum = lr.where(lr > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    dn_sum = (-lr).where(lr < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    ratio = _safe_div(up_sum, dn_sum.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def rfl_drv2_015_close_vs_63d_high_5d_diff(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of close relative to 63d rolling high."""
    hh63 = _rolling_max(high, _TD_QTR)
    rel = _safe_div(close - hh63, hh63)
    return rel.diff(_TD_WEEK)


def rfl_drv2_016_retracement_pct_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21d retracement fraction over 63-day window."""
    pk = _rolling_max(close, _TD_MON)
    tr = _rolling_min(close, _TD_MON)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    return _linslope(frac, _TD_QTR)


def rfl_drv2_017_ema21_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day EMA21 slope (acceleration of intermediate trend)."""
    ema21 = _ewm_mean(close, _TD_MON)
    slp = ema21.diff(_TD_WEEK)
    return slp.diff(_TD_WEEK)


def rfl_drv2_018_lower_high_streak_5d_diff(high: pd.Series) -> pd.Series:
    """5-day diff of consecutive lower-highs streak."""
    streak = _consec_streak(high < high.shift(1))
    return streak.diff(_TD_WEEK)


def rfl_drv2_019_vol_decline_bounce_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63d down-volume to up-volume ratio."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(dn_vol, up_vol.replace(0, np.nan))
    return ratio.diff(_TD_MON)


def rfl_drv2_020_close_vs_sma21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close relative to 21d SMA."""
    sma21 = _rolling_mean(close, _TD_MON)
    rel = _safe_div(close - sma21, sma21)
    return rel.diff(_TD_WEEK)


def rfl_drv2_021_max_up_streak_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d max up-streak length (bounces getting shorter)."""
    from numpy import float64
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    cond = close > close.shift(1)
    mx = cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)
    return mx.diff(_TD_WEEK)


def rfl_drv2_022_up_vs_dn_magnitude_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of avg-up/avg-down day magnitude ratio (21d)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_avg = lr.where(lr > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dn_avg = (-lr).where(lr < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(up_avg, dn_avg)
    return ratio.diff(_TD_WEEK)


def rfl_drv2_023_bounce_attempt_count_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of bounce attempt count in 63d (are bounces happening less often)."""
    ret = close.pct_change(1)
    is_start = ((ret > 0) & (ret.shift(1) <= 0)).astype(float)
    cnt = _rolling_sum(is_start, _TD_QTR)
    return cnt.diff(_TD_MON)


def rfl_drv2_024_high_to_close_ratio_21d_5d_diff(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of avg high/close ratio (21d), velocity of intraday fade."""
    ratio = _safe_div(close, high)
    avg = _rolling_mean(ratio, _TD_MON)
    return avg.diff(_TD_WEEK)


def rfl_drv2_025_peak_drawdown_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of drawdown from 63d rolling peak (velocity of retreat from local peak)."""
    pk = _rolling_max(close, _TD_QTR)
    dd = _safe_div(close - pk, pk)
    return dd.diff(_TD_WEEK)


def rfl_drv2_026_bounce_ret_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day bounce return (velocity of quarter-bounce change)."""
    r = close.pct_change(_TD_QTR)
    return r.diff(_TD_WEEK)


def rfl_drv2_027_bounce_ret_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the 63-day bounce return."""
    r = close.pct_change(_TD_QTR)
    return r.diff(_TD_MON)


def rfl_drv2_028_bounce_ret_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 126-day bounce return (velocity of half-year bounce change)."""
    r = close.pct_change(_TD_HALF)
    return r.diff(_TD_WEEK)


def rfl_drv2_029_retracement_126d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 126d retracement fraction."""
    pk = _rolling_max(close, _TD_HALF)
    tr = _rolling_min(close, _TD_HALF)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    return frac.diff(_TD_MON)


def rfl_drv2_030_lower_high_frac_126d_21d_diff(high: pd.Series) -> pd.Series:
    """21-day diff of lower-high fraction in 126d."""
    frac = _rolling_count_true(high < high.shift(1), _TD_HALF) / _TD_HALF
    return frac.diff(_TD_MON)


def rfl_drv2_031_up_day_count_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of up-day count in 63d (weekly change in up-day frequency)."""
    cnt = _rolling_count_true(close > close.shift(1), _TD_QTR)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_032_up_day_count_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of up-day count in 63d (monthly change in up-day frequency)."""
    cnt = _rolling_count_true(close > close.shift(1), _TD_QTR)
    return cnt.diff(_TD_MON)


def rfl_drv2_033_down_day_ret_avg_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of avg down-day return in 21d (are down days getting worse)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    dn = lr.where(lr < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return dn.diff(_TD_WEEK)


def rfl_drv2_034_up_day_fraction_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of up-day fraction in 21d."""
    frac = _rolling_count_true(close > close.shift(1), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def rfl_drv2_035_up_day_fraction_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of up-day fraction in 63d."""
    frac = _rolling_count_true(close > close.shift(1), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def rfl_drv2_036_bounce_fade_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of bounce-fade from 63d rolling peak."""
    pk63 = _local_peak(close, _TD_QTR)
    fade = _safe_div(close - pk63, pk63)
    return fade.diff(_TD_WEEK)


def rfl_drv2_037_bounce_fade_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of bounce-fade from 63d rolling peak."""
    pk63 = _local_peak(close, _TD_QTR)
    fade = _safe_div(close - pk63, pk63)
    return fade.diff(_TD_MON)


def rfl_drv2_038_close_vs_sma50_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close relative to 50d SMA (velocity of MA divergence)."""
    sma50 = _rolling_mean(close, 50)
    rel = _safe_div(close - sma50, sma50)
    return rel.diff(_TD_WEEK)


def rfl_drv2_039_close_vs_sma200_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close relative to 200d SMA."""
    sma200 = _rolling_mean(close, 200)
    rel = _safe_div(close - sma200, sma200)
    return rel.diff(_TD_WEEK)


def rfl_drv2_040_ema_spread_21_63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA21-EMA63 spread (velocity of intermediate vs long trend gap)."""
    ema21 = _ewm_mean(close, _TD_MON)
    ema63 = _ewm_mean(close, _TD_QTR)
    spread = _safe_div(ema21 - ema63, ema63)
    return spread.diff(_TD_WEEK)


def rfl_drv2_041_sma63_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day SMA63 slope (acceleration of long trend direction)."""
    sma63 = _rolling_mean(close, _TD_QTR)
    slp = sma63.diff(_TD_WEEK)
    return slp.diff(_TD_WEEK)


def rfl_drv2_042_vol_on_up_days_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of avg up-day volume in 21d (is demand on bounces changing)."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return up_vol.diff(_TD_WEEK)


def rfl_drv2_043_vol_on_down_days_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of avg down-day volume in 21d (is supply on declines rising)."""
    ret = close.pct_change(1)
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return dn_vol.diff(_TD_WEEK)


def rfl_drv2_044_vol_up_vs_down_ratio_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63d up/down volume ratio."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(up_vol, dn_vol)
    return ratio.diff(_TD_WEEK)


def rfl_drv2_045_high_to_close_ratio_63d_5d_diff(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of avg high/close ratio (63d), velocity of intraday fade over quarter."""
    ratio = _safe_div(close, high)
    avg = _rolling_mean(ratio, _TD_QTR)
    return avg.diff(_TD_WEEK)


def rfl_drv2_046_close_vs_21d_high_5d_diff(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of close relative to 21d rolling high."""
    hh21 = _rolling_max(high, _TD_MON)
    rel = _safe_div(close - hh21, hh21)
    return rel.diff(_TD_WEEK)


def rfl_drv2_047_intraday_reversal_count_21d_5d_diff(close: pd.Series, open: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of count of intraday reversal days in 21d."""
    cond = (high > high.shift(1)) & (close < open)
    cnt = _rolling_count_true(cond, _TD_MON)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_048_failed_rally_rate_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of failed-rally count in 21d."""
    up = (close > close.shift(1)).astype(float)
    fail = up.shift(1) * (close < close.shift(1)).astype(float)
    cnt = _rolling_sum(fail, _TD_MON)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_049_gap_up_fade_count_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of count of gap-up fade days in 21d."""
    cond = (open > close.shift(1)) & (close < close.shift(1))
    cnt = _rolling_count_true(cond, _TD_MON)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_050_net_log_return_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of net 21-day log return (velocity of medium-term return)."""
    lr = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return lr.diff(_TD_WEEK)


def rfl_drv2_051_net_log_return_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of net 63-day log return (monthly change in quarterly momentum)."""
    lr = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    return lr.diff(_TD_MON)


def rfl_drv2_052_consec_lower_highs_daily_5d_diff(high: pd.Series) -> pd.Series:
    """5-day diff of consecutive daily lower-highs streak."""
    streak = _consec_streak(high < high.shift(1))
    return streak.diff(_TD_WEEK)


def rfl_drv2_053_up_leg_dn_leg_ratio_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d up-leg/down-leg return ratio."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_sum = lr.where(lr > 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    dn_sum = (-lr).where(lr < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    ratio = _safe_div(up_sum, dn_sum.replace(0, np.nan))
    return ratio.diff(_TD_MON)


def rfl_drv2_054_bounce_ret_5d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day return over trailing 63 days (longer-window bounce trend)."""
    r = close.pct_change(_TD_WEEK)
    return _linslope(r, _TD_QTR)


def rfl_drv2_055_retracement_pct_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 63d retracement fraction over 21-day window."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    frac = _safe_div(close - tr, (pk - tr).replace(0, np.nan))
    return _linslope(frac, _TD_MON)


def rfl_drv2_056_lower_high_count_21d_5d_diff(high: pd.Series) -> pd.Series:
    """5-day diff of lower-high count in 21d."""
    cnt = _rolling_count_true(high < high.shift(1), _TD_MON)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_057_lower_high_count_63d_5d_diff(high: pd.Series) -> pd.Series:
    """5-day diff of lower-high count in 63d."""
    cnt = _rolling_count_true(high < high.shift(1), _TD_QTR)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_058_close_pct_from_52wk_high_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close as fraction of 252d rolling high."""
    hh252 = _rolling_max(close, _TD_YEAR)
    rel = _safe_div(close, hh252)
    return rel.diff(_TD_WEEK)


def rfl_drv2_059_close_pct_from_52wk_high_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of close as fraction of 252d rolling high."""
    hh252 = _rolling_max(close, _TD_YEAR)
    rel = _safe_div(close, hh252)
    return rel.diff(_TD_MON)


def rfl_drv2_060_peak_drawdown_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of drawdown from 126d rolling peak."""
    pk = _rolling_max(close, _TD_HALF)
    dd = _safe_div(close - pk, pk)
    return dd.diff(_TD_WEEK)


def rfl_drv2_061_vol_weighted_bounce_ret_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of volume-weighted avg up-day return in 21d."""
    ret = close.pct_change(1)
    up_ret = ret.where(ret > 0, 0.0)
    vol_up = volume.where(ret > 0, 0.0)
    vw = _safe_div(
        (up_ret * vol_up).rolling(_TD_MON, min_periods=1).sum(),
        vol_up.rolling(_TD_MON, min_periods=1).sum().replace(0, np.nan)
    )
    return vw.diff(_TD_WEEK)


def rfl_drv2_062_intraday_high_reversal_21d_5d_diff(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of avg (high-close)/close over 21 days."""
    rev = _safe_div(high - close, close)
    avg = _rolling_mean(rev, _TD_MON)
    return avg.diff(_TD_WEEK)


def rfl_drv2_063_open_to_close_fade_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of avg open-to-close fade in 21d."""
    fade = _safe_div(open - close, open)
    avg = _rolling_mean(fade, _TD_MON)
    return avg.diff(_TD_WEEK)


def rfl_drv2_064_close_to_range_pos_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of close position within 21d range."""
    hh = _rolling_max(high, _TD_MON)
    ll = _rolling_min(low, _TD_MON)
    pos = _safe_div(close - ll, (hh - ll).replace(0, np.nan))
    return pos.diff(_TD_WEEK)


def rfl_drv2_065_close_to_range_pos_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of close position within 63d range."""
    hh = _rolling_max(high, _TD_QTR)
    ll = _rolling_min(low, _TD_QTR)
    pos = _safe_div(close - ll, (hh - ll).replace(0, np.nan))
    return pos.diff(_TD_MON)


def rfl_drv2_066_upper_shadow_ratio_21d_5d_diff(close: pd.Series, open: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of avg upper shadow ratio over 21 days."""
    body_top = pd.concat([open, close], axis=1).max(axis=1)
    upper = (high - body_top).clip(lower=0)
    rng = (high - pd.concat([open, close], axis=1).min(axis=1)).replace(0, np.nan)
    ratio = _safe_div(upper, rng)
    avg = ratio.rolling(_TD_MON, min_periods=1).mean()
    return avg.diff(_TD_WEEK)


def rfl_drv2_067_high_vol_decline_count_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of count of high-volume down days in 21d."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    cnt = _rolling_count_true((ret < 0) & (volume > avg_vol), _TD_MON)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_068_intraday_bounce_frac_21d_5d_diff(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of avg intraday bounce fraction (close-low)/(open-low) over 21 days."""
    num = (close - low).clip(lower=0)
    den = (open - low).abs().replace(0, np.nan)
    frac = _safe_div(num, den).rolling(_TD_MON, min_periods=1).mean()
    return frac.diff(_TD_WEEK)


def rfl_drv2_069_bounce_retracement_ratio_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d bounce/prior-5d-decline ratio (velocity of retracement change)."""
    bounce = close.pct_change(_TD_WEEK)
    prior = _safe_div(close.shift(_TD_WEEK) - close.shift(10), close.shift(10))
    ratio = _safe_div(bounce, (-prior).clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def rfl_drv2_070_consec_up_days_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of current consecutive up-days streak."""
    streak = _consec_streak(close > close.shift(1))
    return streak.diff(_TD_WEEK)


def rfl_drv2_071_rally_fails_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of failed-rally count in 21d (rfl_031 velocity)."""
    up = (close > close.shift(1)).astype(float)
    dn_next = (close.shift(1) > close).astype(float)
    fail = up.shift(1) * dn_next
    cnt = _rolling_sum(fail, _TD_MON)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_072_vol_decline_sum_vs_bounce_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of down-vol-sum / up-vol-sum ratio (21d)."""
    ret = close.pct_change(1)
    up_s = volume.where(ret > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    dn_s = volume.where(ret < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    ratio = _safe_div(dn_s, up_s.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def rfl_drv2_073_bounce_attempt_count_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of bounce attempt count in 63d."""
    ret = close.pct_change(1)
    is_start = ((ret > 0) & (ret.shift(1) <= 0)).astype(float)
    cnt = _rolling_sum(is_start, _TD_QTR)
    return cnt.diff(_TD_WEEK)


def rfl_drv2_074_retracement_decay_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-retracement minus 63d-retracement (decay of bounce recovery)."""
    pk21 = _rolling_max(close, _TD_MON); tr21 = _rolling_min(close, _TD_MON)
    r21 = _safe_div(close - tr21, (pk21 - tr21).replace(0, np.nan))
    pk63 = _rolling_max(close, _TD_QTR); tr63 = _rolling_min(close, _TD_QTR)
    r63 = _safe_div(close - tr63, (pk63 - tr63).replace(0, np.nan))
    decay = r21 - r63
    return decay.diff(_TD_WEEK)


def rfl_drv2_075_bounce_decay_score_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of bounce-decay score (21d max bounce / 63d max bounce ratio)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    mx21 = lr.rolling(_TD_MON, min_periods=1).max()
    mx63 = lr.rolling(_TD_QTR, min_periods=1).max()
    score = _safe_div(mx21, mx63.replace(0, np.nan))
    return score.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RECOVERY_FAILURE_REGISTRY_2ND_DERIVATIVES = {
    "rfl_drv2_001_bounce_ret_5d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_001_bounce_ret_5d_5d_diff},
    "rfl_drv2_002_bounce_ret_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_002_bounce_ret_21d_5d_diff},
    "rfl_drv2_003_retracement_63d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_003_retracement_63d_5d_diff},
    "rfl_drv2_004_retracement_63d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_004_retracement_63d_21d_diff},
    "rfl_drv2_005_lower_high_frac_21d_5d_diff": {"inputs": ["high"], "func": rfl_drv2_005_lower_high_frac_21d_5d_diff},
    "rfl_drv2_006_lower_high_frac_63d_21d_diff": {"inputs": ["high"], "func": rfl_drv2_006_lower_high_frac_63d_21d_diff},
    "rfl_drv2_007_bounce_fade_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_007_bounce_fade_21d_5d_diff},
    "rfl_drv2_008_vol_up_down_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv2_008_vol_up_down_ratio_21d_5d_diff},
    "rfl_drv2_009_up_day_count_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_009_up_day_count_21d_5d_diff},
    "rfl_drv2_010_ema_spread_5_21_5d_diff": {"inputs": ["close"], "func": rfl_drv2_010_ema_spread_5_21_5d_diff},
    "rfl_drv2_011_bounce_ret_5d_slope_21d": {"inputs": ["close"], "func": rfl_drv2_011_bounce_ret_5d_slope_21d},
    "rfl_drv2_012_retracement_126d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_012_retracement_126d_5d_diff},
    "rfl_drv2_013_failed_rally_rate_63d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_013_failed_rally_rate_63d_21d_diff},
    "rfl_drv2_014_up_leg_dn_leg_ratio_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_014_up_leg_dn_leg_ratio_21d_5d_diff},
    "rfl_drv2_015_close_vs_63d_high_5d_diff": {"inputs": ["close", "high"], "func": rfl_drv2_015_close_vs_63d_high_5d_diff},
    "rfl_drv2_016_retracement_pct_21d_slope_63d": {"inputs": ["close"], "func": rfl_drv2_016_retracement_pct_21d_slope_63d},
    "rfl_drv2_017_ema21_slope_5d_diff": {"inputs": ["close"], "func": rfl_drv2_017_ema21_slope_5d_diff},
    "rfl_drv2_018_lower_high_streak_5d_diff": {"inputs": ["high"], "func": rfl_drv2_018_lower_high_streak_5d_diff},
    "rfl_drv2_019_vol_decline_bounce_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": rfl_drv2_019_vol_decline_bounce_ratio_63d_21d_diff},
    "rfl_drv2_020_close_vs_sma21_5d_diff": {"inputs": ["close"], "func": rfl_drv2_020_close_vs_sma21_5d_diff},
    "rfl_drv2_021_max_up_streak_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_021_max_up_streak_21d_5d_diff},
    "rfl_drv2_022_up_vs_dn_magnitude_ratio_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_022_up_vs_dn_magnitude_ratio_21d_5d_diff},
    "rfl_drv2_023_bounce_attempt_count_63d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_023_bounce_attempt_count_63d_21d_diff},
    "rfl_drv2_024_high_to_close_ratio_21d_5d_diff": {"inputs": ["close", "high"], "func": rfl_drv2_024_high_to_close_ratio_21d_5d_diff},
    "rfl_drv2_025_peak_drawdown_63d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_025_peak_drawdown_63d_5d_diff},
    "rfl_drv2_026_bounce_ret_63d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_026_bounce_ret_63d_5d_diff},
    "rfl_drv2_027_bounce_ret_63d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_027_bounce_ret_63d_21d_diff},
    "rfl_drv2_028_bounce_ret_126d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_028_bounce_ret_126d_5d_diff},
    "rfl_drv2_029_retracement_126d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_029_retracement_126d_21d_diff},
    "rfl_drv2_030_lower_high_frac_126d_21d_diff": {"inputs": ["high"], "func": rfl_drv2_030_lower_high_frac_126d_21d_diff},
    "rfl_drv2_031_up_day_count_63d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_031_up_day_count_63d_5d_diff},
    "rfl_drv2_032_up_day_count_63d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_032_up_day_count_63d_21d_diff},
    "rfl_drv2_033_down_day_ret_avg_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_033_down_day_ret_avg_21d_5d_diff},
    "rfl_drv2_034_up_day_fraction_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_034_up_day_fraction_21d_5d_diff},
    "rfl_drv2_035_up_day_fraction_63d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_035_up_day_fraction_63d_21d_diff},
    "rfl_drv2_036_bounce_fade_63d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_036_bounce_fade_63d_5d_diff},
    "rfl_drv2_037_bounce_fade_63d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_037_bounce_fade_63d_21d_diff},
    "rfl_drv2_038_close_vs_sma50_5d_diff": {"inputs": ["close"], "func": rfl_drv2_038_close_vs_sma50_5d_diff},
    "rfl_drv2_039_close_vs_sma200_5d_diff": {"inputs": ["close"], "func": rfl_drv2_039_close_vs_sma200_5d_diff},
    "rfl_drv2_040_ema_spread_21_63_5d_diff": {"inputs": ["close"], "func": rfl_drv2_040_ema_spread_21_63_5d_diff},
    "rfl_drv2_041_sma63_slope_5d_diff": {"inputs": ["close"], "func": rfl_drv2_041_sma63_slope_5d_diff},
    "rfl_drv2_042_vol_on_up_days_21d_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv2_042_vol_on_up_days_21d_5d_diff},
    "rfl_drv2_043_vol_on_down_days_21d_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv2_043_vol_on_down_days_21d_5d_diff},
    "rfl_drv2_044_vol_up_vs_down_ratio_63d_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv2_044_vol_up_vs_down_ratio_63d_5d_diff},
    "rfl_drv2_045_high_to_close_ratio_63d_5d_diff": {"inputs": ["close", "high"], "func": rfl_drv2_045_high_to_close_ratio_63d_5d_diff},
    "rfl_drv2_046_close_vs_21d_high_5d_diff": {"inputs": ["close", "high"], "func": rfl_drv2_046_close_vs_21d_high_5d_diff},
    "rfl_drv2_047_intraday_reversal_count_21d_5d_diff": {"inputs": ["close", "open", "high"], "func": rfl_drv2_047_intraday_reversal_count_21d_5d_diff},
    "rfl_drv2_048_failed_rally_rate_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_048_failed_rally_rate_21d_5d_diff},
    "rfl_drv2_049_gap_up_fade_count_21d_5d_diff": {"inputs": ["close", "open"], "func": rfl_drv2_049_gap_up_fade_count_21d_5d_diff},
    "rfl_drv2_050_net_log_return_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_050_net_log_return_21d_5d_diff},
    "rfl_drv2_051_net_log_return_63d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_051_net_log_return_63d_21d_diff},
    "rfl_drv2_052_consec_lower_highs_daily_5d_diff": {"inputs": ["high"], "func": rfl_drv2_052_consec_lower_highs_daily_5d_diff},
    "rfl_drv2_053_up_leg_dn_leg_ratio_63d_21d_diff": {"inputs": ["close"], "func": rfl_drv2_053_up_leg_dn_leg_ratio_63d_21d_diff},
    "rfl_drv2_054_bounce_ret_5d_slope_63d": {"inputs": ["close"], "func": rfl_drv2_054_bounce_ret_5d_slope_63d},
    "rfl_drv2_055_retracement_pct_63d_slope_21d": {"inputs": ["close"], "func": rfl_drv2_055_retracement_pct_63d_slope_21d},
    "rfl_drv2_056_lower_high_count_21d_5d_diff": {"inputs": ["high"], "func": rfl_drv2_056_lower_high_count_21d_5d_diff},
    "rfl_drv2_057_lower_high_count_63d_5d_diff": {"inputs": ["high"], "func": rfl_drv2_057_lower_high_count_63d_5d_diff},
    "rfl_drv2_058_close_pct_from_52wk_high_5d_diff": {"inputs": ["close"], "func": rfl_drv2_058_close_pct_from_52wk_high_5d_diff},
    "rfl_drv2_059_close_pct_from_52wk_high_21d_diff": {"inputs": ["close"], "func": rfl_drv2_059_close_pct_from_52wk_high_21d_diff},
    "rfl_drv2_060_peak_drawdown_126d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_060_peak_drawdown_126d_5d_diff},
    "rfl_drv2_061_vol_weighted_bounce_ret_21d_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv2_061_vol_weighted_bounce_ret_21d_5d_diff},
    "rfl_drv2_062_intraday_high_reversal_21d_5d_diff": {"inputs": ["close", "high"], "func": rfl_drv2_062_intraday_high_reversal_21d_5d_diff},
    "rfl_drv2_063_open_to_close_fade_21d_5d_diff": {"inputs": ["close", "open"], "func": rfl_drv2_063_open_to_close_fade_21d_5d_diff},
    "rfl_drv2_064_close_to_range_pos_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rfl_drv2_064_close_to_range_pos_21d_5d_diff},
    "rfl_drv2_065_close_to_range_pos_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": rfl_drv2_065_close_to_range_pos_63d_21d_diff},
    "rfl_drv2_066_upper_shadow_ratio_21d_5d_diff": {"inputs": ["close", "open", "high"], "func": rfl_drv2_066_upper_shadow_ratio_21d_5d_diff},
    "rfl_drv2_067_high_vol_decline_count_21d_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv2_067_high_vol_decline_count_21d_5d_diff},
    "rfl_drv2_068_intraday_bounce_frac_21d_5d_diff": {"inputs": ["close", "open", "low"], "func": rfl_drv2_068_intraday_bounce_frac_21d_5d_diff},
    "rfl_drv2_069_bounce_retracement_ratio_5d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_069_bounce_retracement_ratio_5d_5d_diff},
    "rfl_drv2_070_consec_up_days_5d_diff": {"inputs": ["close"], "func": rfl_drv2_070_consec_up_days_5d_diff},
    "rfl_drv2_071_rally_fails_21d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_071_rally_fails_21d_5d_diff},
    "rfl_drv2_072_vol_decline_sum_vs_bounce_21d_5d_diff": {"inputs": ["close", "volume"], "func": rfl_drv2_072_vol_decline_sum_vs_bounce_21d_5d_diff},
    "rfl_drv2_073_bounce_attempt_count_63d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_073_bounce_attempt_count_63d_5d_diff},
    "rfl_drv2_074_retracement_decay_score_5d_diff": {"inputs": ["close"], "func": rfl_drv2_074_retracement_decay_score_5d_diff},
    "rfl_drv2_075_bounce_decay_score_63d_5d_diff": {"inputs": ["close"], "func": rfl_drv2_075_bounce_decay_score_63d_5d_diff},
}
