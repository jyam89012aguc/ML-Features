"""
08_decline_streaks — Base Features 076-150
Domain: consecutive down-day / down-week / down-month run lengths and streak severity
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
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
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_avg_streak(cond: pd.Series, w: int) -> pd.Series:
    """Average streak length of True runs within trailing w periods."""
    def _avg_run(arr):
        total = 0
        num_runs = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
            else:
                if cur > 0:
                    total += cur
                    num_runs += 1
                cur = 0
        if cur > 0:
            total += cur
            num_runs += 1
        if num_runs == 0:
            return 0.0
        return float(total) / float(num_runs)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_avg_run, raw=True)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Average streak length in windows ---

def dstk_076_avg_down_streak_len_21d(close: pd.Series) -> pd.Series:
    """Average length of down-day streaks within trailing 21 days."""
    cond = close < close.shift(1)
    return _rolling_avg_streak(cond, _TD_MON)


def dstk_077_avg_down_streak_len_63d(close: pd.Series) -> pd.Series:
    """Average length of down-day streaks within trailing 63 days."""
    cond = close < close.shift(1)
    return _rolling_avg_streak(cond, _TD_QTR)


def dstk_078_avg_down_streak_len_252d(close: pd.Series) -> pd.Series:
    """Average length of down-day streaks within trailing 252 days."""
    cond = close < close.shift(1)
    return _rolling_avg_streak(cond, _TD_YEAR)


def dstk_079_avg_up_streak_len_63d(close: pd.Series) -> pd.Series:
    """Average length of up-day streaks within trailing 63 days (up = short means bearish)."""
    cond = close > close.shift(1)
    return _rolling_avg_streak(cond, _TD_QTR)


def dstk_080_avg_up_streak_len_252d(close: pd.Series) -> pd.Series:
    """Average length of up-day streaks within trailing 252 days."""
    cond = close > close.shift(1)
    return _rolling_avg_streak(cond, _TD_YEAR)


def dstk_081_down_vs_up_avg_streak_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of avg down-streak to avg up-streak over 63 days."""
    d = dstk_077_avg_down_streak_len_63d(close)
    u = dstk_079_avg_up_streak_len_63d(close)
    return _safe_div(d, u)


def dstk_082_down_vs_up_avg_streak_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of avg down-streak to avg up-streak over 252 days."""
    d = dstk_078_avg_down_streak_len_252d(close)
    u = dstk_080_avg_up_streak_len_252d(close)
    return _safe_div(d, u)


def dstk_083_max_up_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive up-day run within trailing 63 days (short = bearish)."""
    cond = close > close.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_084_max_up_streak_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive up-day run within trailing 252 days."""
    cond = close > close.shift(1)
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_085_down_streak_count_63d(close: pd.Series) -> pd.Series:
    """Number of distinct down-day streaks (streak starts) in trailing 63 days."""
    ret = close.pct_change(1)
    is_start = ((ret < 0) & (ret.shift(1) >= 0)).astype(float)
    return _rolling_sum(is_start, _TD_QTR)


# --- Group I (086-095): Streak-based volume signatures ---

def dstk_086_avg_volume_current_down_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume during the current consecutive down-day streak."""
    cond = close < close.shift(1)
    group = (~cond).cumsum()
    vol_sum = volume.groupby(group).cumsum()
    streak_len = _consec_streak(cond).replace(0, np.nan)
    result = _safe_div(vol_sum.where(cond, np.nan), streak_len)
    return result


def dstk_087_vol_ratio_down_vs_up_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on down-days vs avg volume on up-days, trailing 21d."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(down_vol, up_vol)


def dstk_088_vol_ratio_down_vs_up_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on down-days vs avg volume on up-days, trailing 63d."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(down_vol, up_vol)


def dstk_089_vol_ratio_down_vs_up_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on down-days vs avg volume on up-days, trailing 252d."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    return _safe_div(down_vol, up_vol)


def dstk_090_consec_high_vol_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current streak of down-price days with volume > 21d avg volume."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = (close < close.shift(1)) & (volume > avg_vol)
    return _consec_streak(cond)


def dstk_091_max_high_vol_down_streak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max streak of high-volume down days in trailing 63 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = (close < close.shift(1)) & (volume > avg_vol)
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_092_vol_weighted_down_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted down-day count over 21 days (high-vol down days count more)."""
    ret = close.pct_change(1)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    weighted = vol_norm.where(ret < 0, 0.0)
    return _rolling_sum(weighted, _TD_MON)


def dstk_093_vol_weighted_down_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted down-day count over 63 days."""
    ret = close.pct_change(1)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    weighted = vol_norm.where(ret < 0, 0.0)
    return _rolling_sum(weighted, _TD_QTR)


def dstk_094_down_vol_streak_norm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current declining-volume streak normalized by 21-day avg."""
    streak = _consec_streak(volume < volume.shift(1))
    avg = _rolling_mean(streak, _TD_MON)
    return _safe_div(streak, avg)


def dstk_095_cum_volume_current_down_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative volume traded during the current consecutive down-day streak."""
    cond = close < close.shift(1)
    group = (~cond).cumsum()
    cum_vol = volume.groupby(group).cumsum()
    return cum_vol.where(cond, 0.0)


# --- Group J (096-105): Open-to-close / gap streaks ---

def dstk_096_consec_close_lt_open(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive bear-candle (close < open) streak."""
    cond = close < open
    return _consec_streak(cond)


def dstk_097_max_bear_candle_streak_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Max bear-candle streak within trailing 21 days."""
    cond = close < open
    return _rolling_max_streak(cond, _TD_MON)


def dstk_098_max_bear_candle_streak_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Max bear-candle streak within trailing 252 days."""
    cond = close < open
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_099_consec_gap_down_and_close_down(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current streak of days with both a gap-down open AND a down close."""
    gap_down = open < close.shift(1)
    close_down = close < close.shift(1)
    cond = gap_down & close_down
    return _consec_streak(cond)


def dstk_100_max_gap_down_and_close_down_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Max streak of gap-down + close-down days within trailing 63 days."""
    gap_down = open < close.shift(1)
    close_down = close < close.shift(1)
    cond = gap_down & close_down
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_101_gap_down_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 21 days with a gap-down open."""
    cond = open < close.shift(1)
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def dstk_102_gap_down_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days with a gap-down open."""
    cond = open < close.shift(1)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def dstk_103_avg_gap_down_magnitude_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average magnitude of gap-down opens (open/prior_close - 1) over 21 days."""
    gap = _safe_div(open - close.shift(1), close.shift(1))
    gap_dn = gap.where(gap < 0, np.nan)
    return gap_dn.rolling(_TD_MON, min_periods=1).mean()


def dstk_104_avg_gap_down_magnitude_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average magnitude of gap-down opens over 63 days."""
    gap = _safe_div(open - close.shift(1), close.shift(1))
    gap_dn = gap.where(gap < 0, np.nan)
    return gap_dn.rolling(_TD_QTR, min_periods=1).mean()


def dstk_105_sum_gap_down_magnitude_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of gap-down open returns over 21 days."""
    gap = _safe_div(open - close.shift(1), close.shift(1))
    gap_dn = gap.where(gap < 0, 0.0)
    return _rolling_sum(gap_dn, _TD_MON)


# --- Group K (106-115): ATR and range-based streak severity ---

def dstk_106_atr_14_streak_sum(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of ATR-normalized down moves during current down-day streak."""
    tr = _tr(close, high, low)
    atr14 = _rolling_mean(tr, 14)
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    cond = close < close.shift(1)
    norm_move = _safe_div(daily_log, atr14)
    group = (~cond).cumsum()
    cum_norm = norm_move.groupby(group).cumsum()
    return cum_norm.where(cond, 0.0)


def dstk_107_high_low_range_on_down_days_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average intraday high-low range on down days over 21 days (panic range)."""
    ret = close.pct_change(1)
    rng = (high - low) / close.shift(1)
    rng_dn = rng.where(ret < 0, np.nan)
    return rng_dn.rolling(_TD_MON, min_periods=1).mean()


def dstk_108_high_low_range_on_down_days_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average intraday range on down days over 63 days."""
    ret = close.pct_change(1)
    rng = (high - low) / close.shift(1)
    rng_dn = rng.where(ret < 0, np.nan)
    return rng_dn.rolling(_TD_QTR, min_periods=1).mean()


def dstk_109_max_single_day_loss_current_streak(close: pd.Series) -> pd.Series:
    """Maximum single-day loss within the current consecutive down streak."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    cond = close < close.shift(1)
    group = (~cond).cumsum()
    min_in_group = daily_log.groupby(group).cummin()
    return min_in_group.where(cond, 0.0)


def dstk_110_max_single_day_loss_63d(close: pd.Series) -> pd.Series:
    """Maximum single-day loss (most negative log-return) over trailing 63 days."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    return daily_log.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()


def dstk_111_max_single_day_loss_252d(close: pd.Series) -> pd.Series:
    """Maximum single-day loss over trailing 252 days."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    return daily_log.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()


def dstk_112_atr_ratio_down_vs_up_days_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of avg daily range on down vs up days over 63 days."""
    ret = close.pct_change(1)
    rng = high - low
    dn_range = rng.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_range = rng.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(dn_range, up_range)


def dstk_113_consecutive_wicks_down(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current streak of days where lower wick > upper wick (selling pressure)."""
    upper_wick = high - close
    lower_wick = close - low
    cond = lower_wick > upper_wick
    return _consec_streak(cond)


def dstk_114_max_lower_wick_streak_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max lower-wick-dominant streak in trailing 63 days."""
    upper_wick = high - close
    lower_wick = close - low
    cond = lower_wick > upper_wick
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_115_consec_close_near_daily_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current streak of days where close is in bottom 25% of daily range."""
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    cond = pos <= 0.25
    return _consec_streak(cond)


# --- Group L (116-125): Streak interaction with MA breakdown ---

def dstk_116_consec_all_mas_declining(close: pd.Series) -> pd.Series:
    """Streak of days where SMA21 < SMA63 < SMA200 (all short MAs below long)."""
    sma21 = _rolling_mean(close, _TD_MON)
    sma63 = _rolling_mean(close, _TD_QTR)
    sma200 = _rolling_mean(close, 200)
    cond = (sma21 < sma63) & (sma63 < sma200)
    return _consec_streak(cond)


def dstk_117_consec_close_below_all3_mas(close: pd.Series) -> pd.Series:
    """Streak of days where close is below SMA21, SMA63, and SMA200."""
    sma21 = _rolling_mean(close, _TD_MON)
    sma63 = _rolling_mean(close, _TD_QTR)
    sma200 = _rolling_mean(close, 200)
    cond = (close < sma21) & (close < sma63) & (close < sma200)
    return _consec_streak(cond)


def dstk_118_max_below_all3_mas_252d(close: pd.Series) -> pd.Series:
    """Max streak of close below all 3 MAs within trailing 252 days."""
    sma21 = _rolling_mean(close, _TD_MON)
    sma63 = _rolling_mean(close, _TD_QTR)
    sma200 = _rolling_mean(close, 200)
    cond = (close < sma21) & (close < sma63) & (close < sma200)
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_119_consec_sma21_below_sma63(close: pd.Series) -> pd.Series:
    """Current streak of days where SMA21 < SMA63."""
    sma21 = _rolling_mean(close, _TD_MON)
    sma63 = _rolling_mean(close, _TD_QTR)
    cond = sma21 < sma63
    return _consec_streak(cond)


def dstk_120_consec_sma50_below_sma200(close: pd.Series) -> pd.Series:
    """Current streak of days in death-cross (SMA50 < SMA200)."""
    sma50 = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    cond = sma50 < sma200
    return _consec_streak(cond)


def dstk_121_consec_ema12_below_ema26(close: pd.Series) -> pd.Series:
    """Current streak of days where EMA12 < EMA26 (MACD negative streak)."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    cond = ema12 < ema26
    return _consec_streak(cond)


def dstk_122_below_sma200_streak_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of below-SMA200 streak within trailing 252 days."""
    sma200 = _rolling_mean(close, 200)
    streak = _consec_streak(close < sma200)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dstk_123_consec_declining_sma21(close: pd.Series) -> pd.Series:
    """Current streak of days where SMA21 is lower than prior day's SMA21."""
    sma21 = _rolling_mean(close, _TD_MON)
    cond = sma21 < sma21.shift(1)
    return _consec_streak(cond)


def dstk_124_consec_declining_sma200(close: pd.Series) -> pd.Series:
    """Current streak of days where SMA200 is lower than prior day's SMA200."""
    sma200 = _rolling_mean(close, 200)
    cond = sma200 < sma200.shift(1)
    return _consec_streak(cond)


def dstk_125_max_death_cross_streak_504d(close: pd.Series) -> pd.Series:
    """Maximum death-cross (SMA50 < SMA200) streak within trailing 504 days."""
    sma50 = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    cond = sma50 < sma200
    return _rolling_max_streak(cond, 504)


# --- Group M (126-135): Multi-period streak composites and z-scores ---

def dstk_126_streak_composite_score(close: pd.Series) -> pd.Series:
    """Composite streak score: avg of normalized down-day, down-week, down-month streaks."""
    dd = _consec_streak(close < close.shift(1))
    dw = _consec_streak(close.pct_change(_TD_WEEK) < 0)
    dm = _consec_streak(close.pct_change(_TD_MON) < 0)
    dd_n = _safe_div(dd, _rolling_mean(dd, _TD_YEAR).clip(lower=_EPS))
    dw_n = _safe_div(dw, _rolling_mean(dw, _TD_YEAR).clip(lower=_EPS))
    dm_n = _safe_div(dm, _rolling_mean(dm, _TD_YEAR).clip(lower=_EPS))
    return (dd_n + dw_n + dm_n) / 3.0


def dstk_127_streak_zscore_21d(close: pd.Series) -> pd.Series:
    """Z-score of current down-day streak relative to 252-day distribution."""
    streak = _consec_streak(close < close.shift(1))
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    return _safe_div(streak - m, s)


def dstk_128_streak_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day max down streak relative to 252-day distribution."""
    cond = close < close.shift(1)
    mx63 = _rolling_max_streak(cond, _TD_QTR)
    m = _rolling_mean(mx63, _TD_YEAR)
    s = _rolling_std(mx63, _TD_YEAR)
    return _safe_div(mx63 - m, s)


def dstk_129_max_streak_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day max streak within 252-day distribution."""
    cond = close < close.shift(1)
    mx21 = _rolling_max_streak(cond, _TD_MON)
    m = _rolling_mean(mx21, _TD_YEAR)
    s = _rolling_std(mx21, _TD_YEAR)
    return _safe_div(mx21 - m, s)


def dstk_130_streak_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of current down-day streak (all-history extremity)."""
    streak = _consec_streak(close < close.shift(1))
    m = streak.expanding(min_periods=5).mean()
    s = streak.expanding(min_periods=5).std()
    return _safe_div(streak - m, s)


def dstk_131_down_day_count_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of trailing 21-day down-day count vs 252-day distribution."""
    ret = close.pct_change(1)
    count21 = _rolling_count_true(ret < 0, _TD_MON)
    m = _rolling_mean(count21, _TD_YEAR)
    s = _rolling_std(count21, _TD_YEAR)
    return _safe_div(count21 - m, s)


def dstk_132_streak_severity_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of trailing 21-day severity sum vs 252-day distribution."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    sev21 = daily_log.where(daily_log < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    m = _rolling_mean(sev21, _TD_YEAR)
    s = _rolling_std(sev21, _TD_YEAR)
    return _safe_div(sev21 - m, s)


def dstk_133_streak_length_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of current down streak in trailing 504-day distribution."""
    streak = _consec_streak(close < close.shift(1))
    return streak.rolling(504, min_periods=_TD_YEAR // 2).rank(pct=True)


def dstk_134_down_streak_freq_vs_avg_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day streak-start frequency to 252-day average frequency."""
    ret = close.pct_change(1)
    is_start = ((ret < 0) & (ret.shift(1) >= 0)).astype(float)
    freq21 = _rolling_sum(is_start, _TD_MON)
    freq252 = _rolling_mean(freq21, _TD_YEAR)
    return _safe_div(freq21, freq252)


def dstk_135_streak_severity_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current streak cumulative loss within 252-day distribution."""
    cond = close < close.shift(1)
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    group = (~cond).cumsum()
    cum = daily_log.groupby(group).cumsum().where(cond, 0.0)
    return cum.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group N (136-145): New-low streaks expanded, close vs prior-N-day range ---

def dstk_136_consec_new_504d_low_close(close: pd.Series) -> pd.Series:
    """Current consecutive days where close makes a new 504-day low."""
    roll_min = close.shift(1).rolling(504, min_periods=252).min()
    cond = close < roll_min
    return _consec_streak(cond)


def dstk_137_consec_close_below_52wk_low(close: pd.Series) -> pd.Series:
    """Current consecutive days below the 52-week (252-day) closing low."""
    low52 = _rolling_min(close, _TD_YEAR)
    cond = close < low52.shift(1)
    return _consec_streak(cond)


def dstk_138_consec_low_below_prior_low_5d(low: pd.Series) -> pd.Series:
    """Current streak of days where today's low < 5-day prior low."""
    cond = low < low.shift(_TD_WEEK)
    return _consec_streak(cond)


def dstk_139_consec_low_below_prior_low_21d(low: pd.Series) -> pd.Series:
    """Current streak of days where today's low < 21-day prior low."""
    cond = low < low.shift(_TD_MON)
    return _consec_streak(cond)


def dstk_140_consec_close_below_prior_close_5d(close: pd.Series) -> pd.Series:
    """Current streak of closes below the close from 5 days ago."""
    cond = close < close.shift(_TD_WEEK)
    return _consec_streak(cond)


def dstk_141_consec_close_below_prior_close_21d(close: pd.Series) -> pd.Series:
    """Current streak of closes below the close from 21 days ago."""
    cond = close < close.shift(_TD_MON)
    return _consec_streak(cond)


def dstk_142_new_52wk_low_count_63d(close: pd.Series) -> pd.Series:
    """Count of new 52-week low closes in trailing 63 days."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = (close < roll_min).astype(float)
    return _rolling_sum(new_low, _TD_QTR)


def dstk_143_new_52wk_low_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days that set a new 252-day low."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = (close < roll_min).astype(float)
    return _rolling_mean(new_low, _TD_YEAR)


def dstk_144_consec_lower_close_and_lower_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Streak of days with both a lower close AND a lower intraday low."""
    cond = (close < close.shift(1)) & (low < low.shift(1))
    return _consec_streak(cond)


def dstk_145_max_new_52wk_low_streak_252d(close: pd.Series) -> pd.Series:
    """Max consecutive new-52wk-low streak within trailing 252 days."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    cond = close < roll_min
    return _rolling_max_streak(cond, _TD_YEAR)


# --- Group O (146-150): Composite and cross-asset streak indicators ---

def dstk_146_streak_vol_interaction_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current streak length times normalized volume (streak intensity)."""
    streak = _consec_streak(close < close.shift(1))
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return streak * vol_norm


def dstk_147_down_streak_acceleration_5d(close: pd.Series) -> pd.Series:
    """5-day change in current down-streak length (positive = streak growing)."""
    streak = _consec_streak(close < close.shift(1))
    return streak.diff(_TD_WEEK)


def dstk_148_avg_streak_severity_per_day_252d(close: pd.Series) -> pd.Series:
    """Ratio of 252-day severity sum to 252-day down-day count (avg pain per bad day)."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    ret = close.pct_change(1)
    sev = daily_log.where(daily_log < 0, 0.0)
    sev_sum = _rolling_sum(sev, _TD_YEAR)
    dn_count = _rolling_count_true(ret < 0, _TD_YEAR).replace(0, np.nan)
    return _safe_div(sev_sum, dn_count)


def dstk_149_no_recovery_day_in_streak_flag(close: pd.Series) -> pd.Series:
    """Flag: no up day in last 10 days AND current streak >= 5."""
    ret = close.pct_change(1)
    up_count = _rolling_count_true(ret > 0, 10)
    streak = _consec_streak(close < close.shift(1))
    return ((up_count == 0) & (streak >= 5)).astype(float)


def dstk_150_combined_streak_distress_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined distress: (current_streak * vol_norm) / 252d_avg scaled by down_frac."""
    streak = _consec_streak(close < close.shift(1))
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    intensity = streak * vol_norm
    avg_intensity = _rolling_mean(intensity, _TD_YEAR)
    ret = close.pct_change(1)
    down_frac = _rolling_count_true(ret < 0, _TD_MON) / _TD_MON
    return _safe_div(intensity, avg_intensity.clip(lower=_EPS)) * down_frac


# ── Registry ──────────────────────────────────────────────────────────────────

DECLINE_STREAKS_REGISTRY_076_150 = {
    "dstk_076_avg_down_streak_len_21d": {"inputs": ["close"], "func": dstk_076_avg_down_streak_len_21d},
    "dstk_077_avg_down_streak_len_63d": {"inputs": ["close"], "func": dstk_077_avg_down_streak_len_63d},
    "dstk_078_avg_down_streak_len_252d": {"inputs": ["close"], "func": dstk_078_avg_down_streak_len_252d},
    "dstk_079_avg_up_streak_len_63d": {"inputs": ["close"], "func": dstk_079_avg_up_streak_len_63d},
    "dstk_080_avg_up_streak_len_252d": {"inputs": ["close"], "func": dstk_080_avg_up_streak_len_252d},
    "dstk_081_down_vs_up_avg_streak_ratio_63d": {"inputs": ["close"], "func": dstk_081_down_vs_up_avg_streak_ratio_63d},
    "dstk_082_down_vs_up_avg_streak_ratio_252d": {"inputs": ["close"], "func": dstk_082_down_vs_up_avg_streak_ratio_252d},
    "dstk_083_max_up_streak_63d": {"inputs": ["close"], "func": dstk_083_max_up_streak_63d},
    "dstk_084_max_up_streak_252d": {"inputs": ["close"], "func": dstk_084_max_up_streak_252d},
    "dstk_085_down_streak_count_63d": {"inputs": ["close"], "func": dstk_085_down_streak_count_63d},
    "dstk_086_avg_volume_current_down_streak": {"inputs": ["close", "volume"], "func": dstk_086_avg_volume_current_down_streak},
    "dstk_087_vol_ratio_down_vs_up_21d": {"inputs": ["close", "volume"], "func": dstk_087_vol_ratio_down_vs_up_21d},
    "dstk_088_vol_ratio_down_vs_up_63d": {"inputs": ["close", "volume"], "func": dstk_088_vol_ratio_down_vs_up_63d},
    "dstk_089_vol_ratio_down_vs_up_252d": {"inputs": ["close", "volume"], "func": dstk_089_vol_ratio_down_vs_up_252d},
    "dstk_090_consec_high_vol_down_days": {"inputs": ["close", "volume"], "func": dstk_090_consec_high_vol_down_days},
    "dstk_091_max_high_vol_down_streak_63d": {"inputs": ["close", "volume"], "func": dstk_091_max_high_vol_down_streak_63d},
    "dstk_092_vol_weighted_down_day_count_21d": {"inputs": ["close", "volume"], "func": dstk_092_vol_weighted_down_day_count_21d},
    "dstk_093_vol_weighted_down_day_count_63d": {"inputs": ["close", "volume"], "func": dstk_093_vol_weighted_down_day_count_63d},
    "dstk_094_down_vol_streak_norm_21d": {"inputs": ["close", "volume"], "func": dstk_094_down_vol_streak_norm_21d},
    "dstk_095_cum_volume_current_down_streak": {"inputs": ["close", "volume"], "func": dstk_095_cum_volume_current_down_streak},
    "dstk_096_consec_close_lt_open": {"inputs": ["close", "open"], "func": dstk_096_consec_close_lt_open},
    "dstk_097_max_bear_candle_streak_21d": {"inputs": ["close", "open"], "func": dstk_097_max_bear_candle_streak_21d},
    "dstk_098_max_bear_candle_streak_252d": {"inputs": ["close", "open"], "func": dstk_098_max_bear_candle_streak_252d},
    "dstk_099_consec_gap_down_and_close_down": {"inputs": ["close", "open"], "func": dstk_099_consec_gap_down_and_close_down},
    "dstk_100_max_gap_down_and_close_down_63d": {"inputs": ["close", "open"], "func": dstk_100_max_gap_down_and_close_down_63d},
    "dstk_101_gap_down_fraction_21d": {"inputs": ["close", "open"], "func": dstk_101_gap_down_fraction_21d},
    "dstk_102_gap_down_fraction_63d": {"inputs": ["close", "open"], "func": dstk_102_gap_down_fraction_63d},
    "dstk_103_avg_gap_down_magnitude_21d": {"inputs": ["close", "open"], "func": dstk_103_avg_gap_down_magnitude_21d},
    "dstk_104_avg_gap_down_magnitude_63d": {"inputs": ["close", "open"], "func": dstk_104_avg_gap_down_magnitude_63d},
    "dstk_105_sum_gap_down_magnitude_21d": {"inputs": ["close", "open"], "func": dstk_105_sum_gap_down_magnitude_21d},
    "dstk_106_atr_14_streak_sum": {"inputs": ["close", "high", "low"], "func": dstk_106_atr_14_streak_sum},
    "dstk_107_high_low_range_on_down_days_21d": {"inputs": ["close", "high", "low"], "func": dstk_107_high_low_range_on_down_days_21d},
    "dstk_108_high_low_range_on_down_days_63d": {"inputs": ["close", "high", "low"], "func": dstk_108_high_low_range_on_down_days_63d},
    "dstk_109_max_single_day_loss_current_streak": {"inputs": ["close"], "func": dstk_109_max_single_day_loss_current_streak},
    "dstk_110_max_single_day_loss_63d": {"inputs": ["close"], "func": dstk_110_max_single_day_loss_63d},
    "dstk_111_max_single_day_loss_252d": {"inputs": ["close"], "func": dstk_111_max_single_day_loss_252d},
    "dstk_112_atr_ratio_down_vs_up_days_63d": {"inputs": ["close", "high", "low"], "func": dstk_112_atr_ratio_down_vs_up_days_63d},
    "dstk_113_consecutive_wicks_down": {"inputs": ["close", "high", "low"], "func": dstk_113_consecutive_wicks_down},
    "dstk_114_max_lower_wick_streak_63d": {"inputs": ["close", "high", "low"], "func": dstk_114_max_lower_wick_streak_63d},
    "dstk_115_consec_close_near_daily_low": {"inputs": ["close", "high", "low"], "func": dstk_115_consec_close_near_daily_low},
    "dstk_116_consec_all_mas_declining": {"inputs": ["close"], "func": dstk_116_consec_all_mas_declining},
    "dstk_117_consec_close_below_all3_mas": {"inputs": ["close"], "func": dstk_117_consec_close_below_all3_mas},
    "dstk_118_max_below_all3_mas_252d": {"inputs": ["close"], "func": dstk_118_max_below_all3_mas_252d},
    "dstk_119_consec_sma21_below_sma63": {"inputs": ["close"], "func": dstk_119_consec_sma21_below_sma63},
    "dstk_120_consec_sma50_below_sma200": {"inputs": ["close"], "func": dstk_120_consec_sma50_below_sma200},
    "dstk_121_consec_ema12_below_ema26": {"inputs": ["close"], "func": dstk_121_consec_ema12_below_ema26},
    "dstk_122_below_sma200_streak_pct_rank_252d": {"inputs": ["close"], "func": dstk_122_below_sma200_streak_pct_rank_252d},
    "dstk_123_consec_declining_sma21": {"inputs": ["close"], "func": dstk_123_consec_declining_sma21},
    "dstk_124_consec_declining_sma200": {"inputs": ["close"], "func": dstk_124_consec_declining_sma200},
    "dstk_125_max_death_cross_streak_504d": {"inputs": ["close"], "func": dstk_125_max_death_cross_streak_504d},
    "dstk_126_streak_composite_score": {"inputs": ["close"], "func": dstk_126_streak_composite_score},
    "dstk_127_streak_zscore_21d": {"inputs": ["close"], "func": dstk_127_streak_zscore_21d},
    "dstk_128_streak_zscore_63d": {"inputs": ["close"], "func": dstk_128_streak_zscore_63d},
    "dstk_129_max_streak_21d_zscore_252d": {"inputs": ["close"], "func": dstk_129_max_streak_21d_zscore_252d},
    "dstk_130_streak_expanding_zscore": {"inputs": ["close"], "func": dstk_130_streak_expanding_zscore},
    "dstk_131_down_day_count_zscore_252d": {"inputs": ["close"], "func": dstk_131_down_day_count_zscore_252d},
    "dstk_132_streak_severity_zscore_252d": {"inputs": ["close"], "func": dstk_132_streak_severity_zscore_252d},
    "dstk_133_streak_length_pct_rank_504d": {"inputs": ["close"], "func": dstk_133_streak_length_pct_rank_504d},
    "dstk_134_down_streak_freq_vs_avg_63d": {"inputs": ["close"], "func": dstk_134_down_streak_freq_vs_avg_63d},
    "dstk_135_streak_severity_pct_rank_252d": {"inputs": ["close"], "func": dstk_135_streak_severity_pct_rank_252d},
    "dstk_136_consec_new_504d_low_close": {"inputs": ["close"], "func": dstk_136_consec_new_504d_low_close},
    "dstk_137_consec_close_below_52wk_low": {"inputs": ["close"], "func": dstk_137_consec_close_below_52wk_low},
    "dstk_138_consec_low_below_prior_low_5d": {"inputs": ["low"], "func": dstk_138_consec_low_below_prior_low_5d},
    "dstk_139_consec_low_below_prior_low_21d": {"inputs": ["low"], "func": dstk_139_consec_low_below_prior_low_21d},
    "dstk_140_consec_close_below_prior_close_5d": {"inputs": ["close"], "func": dstk_140_consec_close_below_prior_close_5d},
    "dstk_141_consec_close_below_prior_close_21d": {"inputs": ["close"], "func": dstk_141_consec_close_below_prior_close_21d},
    "dstk_142_new_52wk_low_count_63d": {"inputs": ["close"], "func": dstk_142_new_52wk_low_count_63d},
    "dstk_143_new_52wk_low_fraction_252d": {"inputs": ["close"], "func": dstk_143_new_52wk_low_fraction_252d},
    "dstk_144_consec_lower_close_and_lower_low": {"inputs": ["close", "low"], "func": dstk_144_consec_lower_close_and_lower_low},
    "dstk_145_max_new_52wk_low_streak_252d": {"inputs": ["close"], "func": dstk_145_max_new_52wk_low_streak_252d},
    "dstk_146_streak_vol_interaction_score": {"inputs": ["close", "volume"], "func": dstk_146_streak_vol_interaction_score},
    "dstk_147_down_streak_acceleration_5d": {"inputs": ["close"], "func": dstk_147_down_streak_acceleration_5d},
    "dstk_148_avg_streak_severity_per_day_252d": {"inputs": ["close"], "func": dstk_148_avg_streak_severity_per_day_252d},
    "dstk_149_no_recovery_day_in_streak_flag": {"inputs": ["close"], "func": dstk_149_no_recovery_day_in_streak_flag},
    "dstk_150_combined_streak_distress_index": {"inputs": ["close", "volume"], "func": dstk_150_combined_streak_distress_index},
}
