"""
16_volume_persistence — Base Features 076-200
Domain: sustained elevated volume over multiple days — volume persistence.
Measures consecutive elevated-volume streaks, count of elevated days in trailing
windows, multi-day average elevation, fraction of recent days elevated, and
autocorrelation/stickiness of volume. Focus is on DURATION/SUSTAINMENT of high
volume, not one-off spikes, single-day climax, or volume collapse.
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


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
        return float(total) / float(num_runs) if num_runs > 0 else 0.0
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_avg_run, raw=True)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Elevated-vol runs interacting with price direction ---

def vp_076_elev_vol_on_down_days_consec(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive days with elevated volume (>21d avg) AND price decline."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    return _consec_streak(cond)


def vp_077_elev_vol_on_up_days_consec(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive days with elevated volume AND price advance."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close > close.shift(1))
    return _consec_streak(cond)


def vp_078_elev_vol_on_down_days_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol down-price days in trailing 21 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    return _rolling_count_true(cond, _TD_MON)


def vp_079_elev_vol_on_down_days_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol down-price days in trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    return _rolling_count_true(cond, _TD_QTR)


def vp_080_elev_vol_on_up_days_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol up-price days in trailing 21 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close > close.shift(1))
    return _rolling_count_true(cond, _TD_MON)


def vp_081_elev_vol_down_vs_up_count_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of elevated-vol-down days to elevated-vol-up days in 21 days."""
    base = _rolling_mean(volume, _TD_MON)
    dn = _rolling_count_true((volume > base) & (close < close.shift(1)), _TD_MON)
    up = _rolling_count_true((volume > base) & (close > close.shift(1)), _TD_MON)
    return _safe_div(dn, up)


def vp_082_elev_vol_down_vs_up_count_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of elevated-vol-down days to elevated-vol-up days in 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    dn = _rolling_count_true((volume > base) & (close < close.shift(1)), _TD_QTR)
    up = _rolling_count_true((volume > base) & (close > close.shift(1)), _TD_QTR)
    return _safe_div(dn, up)


def vp_083_max_elev_vol_down_streak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum consecutive elevated-vol down-price days in trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    return _rolling_max_streak(cond, _TD_QTR)


def vp_084_max_elev_vol_down_streak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum consecutive elevated-vol down-price days in trailing 252 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_085_elev_vol_down_fraction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with both elevated volume and price decline."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


# --- Group I (086-095): Volume persistence normalized by historical percentiles ---

def vp_086_elev_vol_streak_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of current elevated-vol streak length within 252-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    return _safe_div(streak - m, s)


def vp_087_elev_vol_count_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day elevated-day count within 252-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


def vp_088_avg_vol_ratio_21d_vs_252d_pct_rank(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d/252d volume ratio within 252-day trailing window."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    ratio = _safe_div(avg21, avg252)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_089_elev_vol_streak_expanding_zscore(volume: pd.Series) -> pd.Series:
    """Expanding z-score of elevated-vol streak (all-history extremity)."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    m = streak.expanding(min_periods=5).mean()
    s = streak.expanding(min_periods=5).std()
    return _safe_div(streak - m, s)


def vp_090_elev_vol_fraction_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day elevated-vol fraction within 252-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    return frac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_091_elev_vol_streak_norm_by_hist_max(volume: pd.Series) -> pd.Series:
    """Current elevated streak divided by trailing 252-day max streak."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    mx = _rolling_max_streak(volume > base, _TD_YEAR)
    return _safe_div(streak, mx)


def vp_092_max_elev_streak_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day max elevated streak within 252-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    mx63 = _rolling_max_streak(volume > base, _TD_QTR)
    m = _rolling_mean(mx63, _TD_YEAR)
    s = _rolling_std(mx63, _TD_YEAR)
    return _safe_div(mx63 - m, s)


def vp_093_elev_vol_fraction_252d_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 252-day elevated fraction in trailing 504-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_YEAR) / _TD_YEAR
    return frac.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def vp_094_elev_vol_count_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day elevated-day count within trailing 252-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_QTR)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_095_avg_elev_streak_len_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day avg elevated streak length within 252-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    avg_len = _rolling_avg_streak(volume > base, _TD_QTR)
    m = _rolling_mean(avg_len, _TD_YEAR)
    s = _rolling_std(avg_len, _TD_YEAR)
    return _safe_div(avg_len - m, s)


# --- Group J (096-105): Weekly and monthly period elevated-volume persistence ---

def vp_096_consec_elev_vol_weeks(volume: pd.Series) -> pd.Series:
    """Current run of consecutive 5-day periods where avg volume > 21d prior avg."""
    avg5 = _rolling_mean(volume, _TD_WEEK)
    base = avg5.shift(_TD_WEEK)
    cond = avg5 > base
    return _consec_streak(cond)


def vp_097_consec_elev_vol_months(volume: pd.Series) -> pd.Series:
    """Current run of consecutive 21-day periods where avg vol > prior 21-day avg."""
    avg21 = _rolling_mean(volume, _TD_MON)
    base = avg21.shift(_TD_MON)
    cond = avg21 > base
    return _consec_streak(cond)


def vp_098_elev_vol_week_count_63d(volume: pd.Series) -> pd.Series:
    """Count of weeks (5d) with above-prior-period average volume in trailing 63 days."""
    avg5 = _rolling_mean(volume, _TD_WEEK)
    base = avg5.shift(_TD_WEEK)
    cond = avg5 > base
    return _rolling_count_true(cond, _TD_QTR)


def vp_099_elev_vol_week_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of 252-day window where 5d avg vol > prior-5d avg."""
    avg5 = _rolling_mean(volume, _TD_WEEK)
    base = avg5.shift(_TD_WEEK)
    cond = avg5 > base
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def vp_100_max_elev_vol_week_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-prior-period-avg weeks within trailing 252 days."""
    avg5 = _rolling_mean(volume, _TD_WEEK)
    base = avg5.shift(_TD_WEEK)
    cond = avg5 > base
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_101_consec_above_prior_month_vol(volume: pd.Series) -> pd.Series:
    """Current streak of days where 21-day rolling avg vol > 21-day rolling avg vol 21d ago."""
    avg21 = _rolling_mean(volume, _TD_MON)
    cond = avg21 > avg21.shift(_TD_MON)
    return _consec_streak(cond)


def vp_102_elev_vol_month_count_252d(volume: pd.Series) -> pd.Series:
    """Count of 21-day periods in last 252 days with avg vol above prior-21d avg."""
    avg21 = _rolling_mean(volume, _TD_MON)
    cond = avg21 > avg21.shift(_TD_MON)
    return _rolling_count_true(cond, _TD_YEAR)


def vp_103_elev_vol_month_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of 252-day window where monthly avg vol beat prior monthly avg."""
    avg21 = _rolling_mean(volume, _TD_MON)
    cond = avg21 > avg21.shift(_TD_MON)
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def vp_104_elev_vol_qtr_fraction_504d(volume: pd.Series) -> pd.Series:
    """Fraction of 504-day window where 63-day avg vol > prior 63-day avg vol."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    cond = avg63 > avg63.shift(_TD_QTR)
    return _rolling_count_true(cond, 504) / 504


def vp_105_consec_vol_above_prior_63d_avg(volume: pd.Series) -> pd.Series:
    """Current streak of days where volume > 63-day average vol from 63d ago."""
    base_lagged = _rolling_mean(volume, _TD_QTR).shift(_TD_QTR)
    cond = volume > base_lagged
    return _consec_streak(cond)


# --- Group K (106-115): Volume-weighted and dollar-volume persistence ---

def vp_106_elev_dollar_vol_consec_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive days where dollar volume (close*vol) > 21d avg dollar vol."""
    dv = close * volume
    base = _rolling_mean(dv, _TD_MON)
    cond = dv > base
    return _consec_streak(cond)


def vp_107_elev_dollar_vol_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of above-avg dollar-volume days in trailing 21 days."""
    dv = close * volume
    base = _rolling_mean(dv, _TD_MON)
    cond = dv > base
    return _rolling_count_true(cond, _TD_MON)


def vp_108_elev_dollar_vol_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of above-avg dollar-volume days in trailing 63 days."""
    dv = close * volume
    base = _rolling_mean(dv, _TD_MON)
    cond = dv > base
    return _rolling_count_true(cond, _TD_QTR)


def vp_109_elev_dollar_vol_fraction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where dollar volume > 21-day average."""
    dv = close * volume
    base = _rolling_mean(dv, _TD_MON)
    cond = dv > base
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def vp_110_avg_dollar_vol_ratio_21d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day avg dollar volume divided by 252-day avg dollar volume."""
    dv = close * volume
    return _safe_div(_rolling_mean(dv, _TD_MON), _rolling_mean(dv, _TD_YEAR))


def vp_111_elev_dollar_vol_max_streak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-avg dollar-volume days within trailing 63 days."""
    dv = close * volume
    base = _rolling_mean(dv, _TD_MON)
    cond = dv > base
    return _rolling_max_streak(cond, _TD_QTR)


def vp_112_cumvol_over_elev_streak_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative volume in current elevated streak normalized by 21d avg daily vol."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    group = (~cond).cumsum()
    cum_vol = volume.groupby(group).cumsum()
    avg_daily = _rolling_mean(volume, _TD_MON)
    return _safe_div(cum_vol.where(cond, 0.0), avg_daily)


def vp_113_vol_log_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Log ratio of 21-day average volume to 252-day average volume."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    return _log_safe(avg21) - _log_safe(avg252)


def vp_114_vol_log_ratio_5d_vs_63d(volume: pd.Series) -> pd.Series:
    """Log ratio of 5-day average volume to 63-day average volume."""
    avg5 = _rolling_mean(volume, _TD_WEEK)
    avg63 = _rolling_mean(volume, _TD_QTR)
    return _log_safe(avg5) - _log_safe(avg63)


def vp_115_elev_vol_count_21d_vs_252d_avg(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day elevated-day count to 252-day average 21-day count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt21 = _rolling_count_true(volume > base, _TD_MON)
    avg_cnt = _rolling_mean(cnt21, _TD_YEAR)
    return _safe_div(cnt21, avg_cnt)


# --- Group L (116-125): Composite persistence and cross-timeframe features ---

def vp_116_persistence_composite_21d_63d_252d(volume: pd.Series) -> pd.Series:
    """Composite: average of normalized elevated-day fractions at 21/63/252d windows."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    f21 = _rolling_count_true(cond, _TD_MON) / _TD_MON
    f63 = _rolling_count_true(cond, _TD_QTR) / _TD_QTR
    f252 = _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR
    return (f21 + f63 + f252) / 3.0


def vp_117_streak_x_fraction_x_elevation_21d(volume: pd.Series) -> pd.Series:
    """Current streak * 21d fraction * 21d avg elevation ratio (3-way intensity)."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    streak = _consec_streak(cond)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    avg_ratio = _rolling_mean(_safe_div(volume, base), _TD_MON)
    return streak * frac * avg_ratio


def vp_118_elev_vol_consecutive_flag_gt5(volume: pd.Series) -> pd.Series:
    """Binary: current elevated-volume streak >= 5 consecutive days."""
    base = _rolling_mean(volume, _TD_MON)
    return (_consec_streak(volume > base) >= 5).astype(float)


def vp_119_elev_vol_consecutive_flag_gt10(volume: pd.Series) -> pd.Series:
    """Binary: current elevated-volume streak >= 10 consecutive days."""
    base = _rolling_mean(volume, _TD_MON)
    return (_consec_streak(volume > base) >= 10).astype(float)


def vp_120_elev_vol_consecutive_flag_gt21(volume: pd.Series) -> pd.Series:
    """Binary: current elevated-volume streak >= 21 consecutive days (full month)."""
    base = _rolling_mean(volume, _TD_MON)
    return (_consec_streak(volume > base) >= 21).astype(float)


def vp_121_elev_vol_2x_consec_flag_gt3(volume: pd.Series) -> pd.Series:
    """Binary: current 2x-elevated streak >= 3 consecutive days."""
    base = _rolling_mean(volume, _TD_MON)
    return (_consec_streak(volume > 2.0 * base.replace(0, np.nan)) >= 3).astype(float)


def vp_122_all_5d_elevated_vol_flag(volume: pd.Series) -> pd.Series:
    """Binary: every day in the last 5 had above-21d-avg volume."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_WEEK)
    return (cnt == _TD_WEEK).astype(float)


def vp_123_all_21d_elevated_vol_flag(volume: pd.Series) -> pd.Series:
    """Binary: every day in the last 21 had above-21d-avg volume."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_MON)
    return (cnt == _TD_MON).astype(float)


def vp_124_elev_vol_on_down_day_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with elevated volume on a down-price day."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vp_125_vol_above_prior_day_fraction_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where volume > prior day's volume."""
    cond = volume > volume.shift(1)
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


# --- Group M (126-135): EMA-based persistence and ratio momentum ---

def vp_126_vol_ewm_ratio_5d_vs_21d(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day EMA to 21-day EMA of volume."""
    return _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_MON))


def vp_127_vol_ewm_ratio_21d_vs_63d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day EMA to 63-day EMA of volume."""
    return _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))


def vp_128_vol_ewm_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day EMA to 252-day EMA of volume."""
    return _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_YEAR))


def vp_129_consec_ewm5_above_ewm21(volume: pd.Series) -> pd.Series:
    """Current consecutive days where 5-day EMA vol > 21-day EMA vol."""
    cond = _ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)
    return _consec_streak(cond)


def vp_130_consec_ewm21_above_ewm63(volume: pd.Series) -> pd.Series:
    """Current consecutive days where 21-day EMA vol > 63-day EMA vol."""
    cond = _ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_QTR)
    return _consec_streak(cond)


def vp_131_max_ewm5_above_ewm21_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive days EMA5 vol > EMA21 vol in trailing 252 days."""
    cond = _ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_132_vol_ewm_ratio_21d_vs_63d_pct_rank(volume: pd.Series) -> pd.Series:
    """Percentile rank of EMA21/EMA63 volume ratio within trailing 252-day distribution."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_133_vol_ewm_ratio_5d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day EMA to 252-day EMA of volume."""
    return _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_YEAR))


def vp_134_vol_ewm_crossover_count_21d(volume: pd.Series) -> pd.Series:
    """Count of days in last 21 where EMA5 > EMA21 for volume."""
    cond = _ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)
    return _rolling_count_true(cond, _TD_MON)


def vp_135_vol_ewm_crossover_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where EMA5 vol > EMA21 vol."""
    cond = _ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


# --- Group N (136-145): Percentile-rank threshold elevation persistence ---

def vp_136_vol_above_90th_pct_consec(volume: pd.Series) -> pd.Series:
    """Current streak where volume > 90th percentile of trailing 252-day volume."""
    pct90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    cond = volume > pct90
    return _consec_streak(cond)


def vp_137_vol_above_75th_pct_consec(volume: pd.Series) -> pd.Series:
    """Current streak where volume > 75th percentile of trailing 252-day volume."""
    pct75 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    cond = volume > pct75
    return _consec_streak(cond)


def vp_138_vol_above_90th_pct_count_21d(volume: pd.Series) -> pd.Series:
    """Count of days in last 21 where volume > 90th percentile (252-day)."""
    pct90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    cond = volume > pct90
    return _rolling_count_true(cond, _TD_MON)


def vp_139_vol_above_75th_pct_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in last 63 where volume > 75th percentile (252-day)."""
    pct75 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    cond = volume > pct75
    return _rolling_count_true(cond, _TD_QTR)


def vp_140_vol_above_90th_pct_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where volume > 90th percentile (252-day)."""
    pct90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    cond = volume > pct90
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vp_141_vol_pct_rank_21d_avg_in_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day average volume within trailing 252-day volume series."""
    avg21 = _rolling_mean(volume, _TD_MON)
    return avg21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_142_vol_pct_rank_5d_avg_in_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 5-day average volume within trailing 252-day volume series."""
    avg5 = _rolling_mean(volume, _TD_WEEK)
    return avg5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_143_vol_above_90th_pct_max_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-90th-pct volume days within trailing 252 days."""
    pct90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    cond = volume > pct90
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_144_vol_above_75th_pct_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where volume > 75th percentile (252-day)."""
    pct75 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    cond = volume > pct75
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def vp_145_vol_pct_rank_current_vs_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 252-day volume distribution."""
    return volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group O (146-150): Composite and multi-input persistence signals ---

def vp_146_elev_vol_persistence_index(volume: pd.Series) -> pd.Series:
    """Persistence index: streak * fraction * zscore product (capped sign-preserving)."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    streak = _consec_streak(cond)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s).fillna(0.0)
    return frac * z


def vp_147_elev_vol_streak_acc_5d(volume: pd.Series) -> pd.Series:
    """5-day change in current elevated-volume streak length."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    return streak.diff(_TD_WEEK)


def vp_148_elev_vol_on_down_x_streak_len(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Elevated-vol-down-day count (21d) times current elevated streak length."""
    base = _rolling_mean(volume, _TD_MON)
    dn_cnt = _rolling_count_true((volume > base) & (close < close.shift(1)), _TD_MON)
    streak = _consec_streak(volume > base)
    return dn_cnt * streak


def vp_149_vol_ratio_21d_vs_252d_x_elev_frac(volume: pd.Series) -> pd.Series:
    """21d/252d avg-vol ratio times 21-day elevated fraction (elevation scale)."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    ratio = _safe_div(avg21, avg252)
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    return ratio * frac


def vp_150_vol_persistence_distress_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distress composite: elev streak * elev-vol-down fraction * avg elevation ratio."""
    base = _rolling_mean(volume, _TD_MON)
    cond_elev = volume > base
    streak = _consec_streak(cond_elev)
    avg_ratio = _rolling_mean(_safe_div(volume, base), _TD_MON)
    cond_dn = (volume > base) & (close < close.shift(1))
    dn_frac = _rolling_count_true(cond_dn, _TD_MON) / _TD_MON
    return streak * avg_ratio * dn_frac


# --- Group R (176-185): Turnover-rate and open-based persistence ---

def vp_176_elev_vol_on_gap_down_consec(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with elevated vol AND gap-down open (open < prior close)."""
    base = _rolling_mean(volume, _TD_MON)
    gap_dn = open < close.shift(1)
    cond = (volume > base) & gap_dn
    return _consec_streak(cond)


def vp_177_elev_vol_on_gap_down_count_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol gap-down-open days in trailing 21 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (open < close.shift(1))
    return _rolling_count_true(cond, _TD_MON)


def vp_178_elev_vol_on_gap_down_count_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol gap-down-open days in trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (open < close.shift(1))
    return _rolling_count_true(cond, _TD_QTR)


def vp_179_elev_vol_on_close_below_open_consec(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with elevated vol AND bearish close (close < open)."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < open)
    return _consec_streak(cond)


def vp_180_elev_vol_close_below_open_count_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol bearish-close days (close < open) in trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < open)
    return _rolling_count_true(cond, _TD_QTR)


def vp_181_high_vol_low_close_consec(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with elevated vol AND close near daily low (close < 25th pct of range)."""
    base = _rolling_mean(volume, _TD_MON)
    rng = (high - close).replace(0, np.nan)
    full_rng = _rolling_mean(high - close, _TD_MON).replace(0, np.nan)
    near_low = (high - close) > 0.75 * full_rng
    cond = (volume > base) & near_low
    return _consec_streak(cond)


def vp_182_elev_vol_high_gt_prior_high_consec(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with elevated vol AND new session high > prior session high."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (high > high.shift(1))
    return _consec_streak(cond)


def vp_183_elev_vol_low_lt_prior_low_consec(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with elevated vol AND lower low than prior session."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (low < low.shift(1))
    return _consec_streak(cond)


def vp_184_elev_vol_low_lt_prior_low_count_21d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol lower-low days in trailing 21 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (low < low.shift(1))
    return _rolling_count_true(cond, _TD_MON)


def vp_185_elev_vol_low_lt_prior_low_count_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol lower-low days in trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (low < low.shift(1))
    return _rolling_count_true(cond, _TD_QTR)


# --- Group S (186-200): Volatility-adjusted persistence, turnover decay, composites ---

def vp_186_vol_sum_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of total volume over last 21 days to total over trailing 252 days."""
    s21 = _rolling_sum(volume, _TD_MON)
    s252 = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(s21, s252)


def vp_187_vol_sum_5d_vs_63d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of total volume over last 5 days to total over trailing 63 days."""
    s5 = _rolling_sum(volume, _TD_WEEK)
    s63 = _rolling_sum(volume, _TD_QTR)
    return _safe_div(s5, s63)


def vp_188_vol_std_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day vol std to 252-day vol std (recent vs long-run dispersion)."""
    return _safe_div(_rolling_std(volume, _TD_MON), _rolling_std(volume, _TD_YEAR))


def vp_189_vol_cv_21d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 21 days (std/mean, dispersion)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    return _safe_div(s, m)


def vp_190_vol_cv_63d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 63 days (std/mean)."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    return _safe_div(s, m)


def vp_191_elev_vol_on_down_day_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day elevated-vol-down-day count within 252-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    cnt = _rolling_count_true(cond, _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


def vp_192_avg_elev_streak_len_252d_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day average elevated-streak length."""
    avg252 = _rolling_avg_streak(volume > _rolling_mean(volume, _TD_MON), _TD_YEAR)
    return avg252.expanding(min_periods=5).rank(pct=True)


def vp_193_vol_ewm_crossover_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where EMA5 vol > EMA21 vol."""
    cond = _ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def vp_194_elev_vol_count_126d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 126-day elevated-day count within trailing 252-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_HALF)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_195_vol_above_prior_day_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in last 63 where volume > prior day's volume."""
    cond = volume > volume.shift(1)
    return _rolling_count_true(cond, _TD_QTR)


def vp_196_vol_above_prior_day_max_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive days of volume > prior day in trailing 252 days."""
    cond = volume > volume.shift(1)
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_197_consec_elev_vol_126d_baseline(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 126-day rolling average."""
    base = _rolling_mean(volume, _TD_HALF)
    cond = volume > base
    return _consec_streak(cond)


def vp_198_elev_vol_126d_baseline_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days in last 252 where volume > 126-day rolling average."""
    base = _rolling_mean(volume, _TD_HALF)
    cond = volume > base
    return _rolling_count_true(cond, _TD_YEAR)


def vp_199_vol_log_ratio_63d_vs_252d(volume: pd.Series) -> pd.Series:
    """Log ratio of 63-day average volume to 252-day average volume."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    return _log_safe(avg63) - _log_safe(avg252)


def vp_200_elev_vol_distress_extended_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Extended distress: elev-vol-down count (63d) * avg elev streak (63d) * elev fraction (21d)."""
    base = _rolling_mean(volume, _TD_MON)
    dn_cnt = _rolling_count_true((volume > base) & (close < close.shift(1)), _TD_QTR)
    avg_len = _rolling_avg_streak(volume > base, _TD_QTR)
    frac21 = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    return dn_cnt * avg_len * frac21


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PERSISTENCE_REGISTRY_076_150 = {
    "vp_076_elev_vol_on_down_days_consec": {"inputs": ["close", "volume"], "func": vp_076_elev_vol_on_down_days_consec},
    "vp_077_elev_vol_on_up_days_consec": {"inputs": ["close", "volume"], "func": vp_077_elev_vol_on_up_days_consec},
    "vp_078_elev_vol_on_down_days_count_21d": {"inputs": ["close", "volume"], "func": vp_078_elev_vol_on_down_days_count_21d},
    "vp_079_elev_vol_on_down_days_count_63d": {"inputs": ["close", "volume"], "func": vp_079_elev_vol_on_down_days_count_63d},
    "vp_080_elev_vol_on_up_days_count_21d": {"inputs": ["close", "volume"], "func": vp_080_elev_vol_on_up_days_count_21d},
    "vp_081_elev_vol_down_vs_up_count_ratio_21d": {"inputs": ["close", "volume"], "func": vp_081_elev_vol_down_vs_up_count_ratio_21d},
    "vp_082_elev_vol_down_vs_up_count_ratio_63d": {"inputs": ["close", "volume"], "func": vp_082_elev_vol_down_vs_up_count_ratio_63d},
    "vp_083_max_elev_vol_down_streak_63d": {"inputs": ["close", "volume"], "func": vp_083_max_elev_vol_down_streak_63d},
    "vp_084_max_elev_vol_down_streak_252d": {"inputs": ["close", "volume"], "func": vp_084_max_elev_vol_down_streak_252d},
    "vp_085_elev_vol_down_fraction_21d": {"inputs": ["close", "volume"], "func": vp_085_elev_vol_down_fraction_21d},
    "vp_086_elev_vol_streak_zscore_252d": {"inputs": ["volume"], "func": vp_086_elev_vol_streak_zscore_252d},
    "vp_087_elev_vol_count_21d_zscore_252d": {"inputs": ["volume"], "func": vp_087_elev_vol_count_21d_zscore_252d},
    "vp_088_avg_vol_ratio_21d_vs_252d_pct_rank": {"inputs": ["volume"], "func": vp_088_avg_vol_ratio_21d_vs_252d_pct_rank},
    "vp_089_elev_vol_streak_expanding_zscore": {"inputs": ["volume"], "func": vp_089_elev_vol_streak_expanding_zscore},
    "vp_090_elev_vol_fraction_21d_pct_rank_252d": {"inputs": ["volume"], "func": vp_090_elev_vol_fraction_21d_pct_rank_252d},
    "vp_091_elev_vol_streak_norm_by_hist_max": {"inputs": ["volume"], "func": vp_091_elev_vol_streak_norm_by_hist_max},
    "vp_092_max_elev_streak_63d_zscore_252d": {"inputs": ["volume"], "func": vp_092_max_elev_streak_63d_zscore_252d},
    "vp_093_elev_vol_fraction_252d_pct_rank_504d": {"inputs": ["volume"], "func": vp_093_elev_vol_fraction_252d_pct_rank_504d},
    "vp_094_elev_vol_count_63d_pct_rank_252d": {"inputs": ["volume"], "func": vp_094_elev_vol_count_63d_pct_rank_252d},
    "vp_095_avg_elev_streak_len_63d_zscore_252d": {"inputs": ["volume"], "func": vp_095_avg_elev_streak_len_63d_zscore_252d},
    "vp_096_consec_elev_vol_weeks": {"inputs": ["volume"], "func": vp_096_consec_elev_vol_weeks},
    "vp_097_consec_elev_vol_months": {"inputs": ["volume"], "func": vp_097_consec_elev_vol_months},
    "vp_098_elev_vol_week_count_63d": {"inputs": ["volume"], "func": vp_098_elev_vol_week_count_63d},
    "vp_099_elev_vol_week_fraction_252d": {"inputs": ["volume"], "func": vp_099_elev_vol_week_fraction_252d},
    "vp_100_max_elev_vol_week_streak_252d": {"inputs": ["volume"], "func": vp_100_max_elev_vol_week_streak_252d},
    "vp_101_consec_above_prior_month_vol": {"inputs": ["volume"], "func": vp_101_consec_above_prior_month_vol},
    "vp_102_elev_vol_month_count_252d": {"inputs": ["volume"], "func": vp_102_elev_vol_month_count_252d},
    "vp_103_elev_vol_month_fraction_252d": {"inputs": ["volume"], "func": vp_103_elev_vol_month_fraction_252d},
    "vp_104_elev_vol_qtr_fraction_504d": {"inputs": ["volume"], "func": vp_104_elev_vol_qtr_fraction_504d},
    "vp_105_consec_vol_above_prior_63d_avg": {"inputs": ["volume"], "func": vp_105_consec_vol_above_prior_63d_avg},
    "vp_106_elev_dollar_vol_consec_21d": {"inputs": ["close", "volume"], "func": vp_106_elev_dollar_vol_consec_21d},
    "vp_107_elev_dollar_vol_count_21d": {"inputs": ["close", "volume"], "func": vp_107_elev_dollar_vol_count_21d},
    "vp_108_elev_dollar_vol_count_63d": {"inputs": ["close", "volume"], "func": vp_108_elev_dollar_vol_count_63d},
    "vp_109_elev_dollar_vol_fraction_21d": {"inputs": ["close", "volume"], "func": vp_109_elev_dollar_vol_fraction_21d},
    "vp_110_avg_dollar_vol_ratio_21d_vs_252d": {"inputs": ["close", "volume"], "func": vp_110_avg_dollar_vol_ratio_21d_vs_252d},
    "vp_111_elev_dollar_vol_max_streak_63d": {"inputs": ["close", "volume"], "func": vp_111_elev_dollar_vol_max_streak_63d},
    "vp_112_cumvol_over_elev_streak_norm": {"inputs": ["close", "volume"], "func": vp_112_cumvol_over_elev_streak_norm},
    "vp_113_vol_log_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vp_113_vol_log_ratio_21d_vs_252d},
    "vp_114_vol_log_ratio_5d_vs_63d": {"inputs": ["volume"], "func": vp_114_vol_log_ratio_5d_vs_63d},
    "vp_115_elev_vol_count_21d_vs_252d_avg": {"inputs": ["volume"], "func": vp_115_elev_vol_count_21d_vs_252d_avg},
    "vp_116_persistence_composite_21d_63d_252d": {"inputs": ["volume"], "func": vp_116_persistence_composite_21d_63d_252d},
    "vp_117_streak_x_fraction_x_elevation_21d": {"inputs": ["volume"], "func": vp_117_streak_x_fraction_x_elevation_21d},
    "vp_118_elev_vol_consecutive_flag_gt5": {"inputs": ["volume"], "func": vp_118_elev_vol_consecutive_flag_gt5},
    "vp_119_elev_vol_consecutive_flag_gt10": {"inputs": ["volume"], "func": vp_119_elev_vol_consecutive_flag_gt10},
    "vp_120_elev_vol_consecutive_flag_gt21": {"inputs": ["volume"], "func": vp_120_elev_vol_consecutive_flag_gt21},
    "vp_121_elev_vol_2x_consec_flag_gt3": {"inputs": ["volume"], "func": vp_121_elev_vol_2x_consec_flag_gt3},
    "vp_122_all_5d_elevated_vol_flag": {"inputs": ["volume"], "func": vp_122_all_5d_elevated_vol_flag},
    "vp_123_all_21d_elevated_vol_flag": {"inputs": ["volume"], "func": vp_123_all_21d_elevated_vol_flag},
    "vp_124_elev_vol_on_down_day_fraction_63d": {"inputs": ["close", "volume"], "func": vp_124_elev_vol_on_down_day_fraction_63d},
    "vp_125_vol_above_prior_day_fraction_21d": {"inputs": ["volume"], "func": vp_125_vol_above_prior_day_fraction_21d},
    "vp_126_vol_ewm_ratio_5d_vs_21d": {"inputs": ["volume"], "func": vp_126_vol_ewm_ratio_5d_vs_21d},
    "vp_127_vol_ewm_ratio_21d_vs_63d": {"inputs": ["volume"], "func": vp_127_vol_ewm_ratio_21d_vs_63d},
    "vp_128_vol_ewm_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vp_128_vol_ewm_ratio_21d_vs_252d},
    "vp_129_consec_ewm5_above_ewm21": {"inputs": ["volume"], "func": vp_129_consec_ewm5_above_ewm21},
    "vp_130_consec_ewm21_above_ewm63": {"inputs": ["volume"], "func": vp_130_consec_ewm21_above_ewm63},
    "vp_131_max_ewm5_above_ewm21_streak_252d": {"inputs": ["volume"], "func": vp_131_max_ewm5_above_ewm21_streak_252d},
    "vp_132_vol_ewm_ratio_21d_vs_63d_pct_rank": {"inputs": ["volume"], "func": vp_132_vol_ewm_ratio_21d_vs_63d_pct_rank},
    "vp_133_vol_ewm_ratio_5d_vs_252d": {"inputs": ["volume"], "func": vp_133_vol_ewm_ratio_5d_vs_252d},
    "vp_134_vol_ewm_crossover_count_21d": {"inputs": ["volume"], "func": vp_134_vol_ewm_crossover_count_21d},
    "vp_135_vol_ewm_crossover_fraction_63d": {"inputs": ["volume"], "func": vp_135_vol_ewm_crossover_fraction_63d},
    "vp_136_vol_above_90th_pct_consec": {"inputs": ["volume"], "func": vp_136_vol_above_90th_pct_consec},
    "vp_137_vol_above_75th_pct_consec": {"inputs": ["volume"], "func": vp_137_vol_above_75th_pct_consec},
    "vp_138_vol_above_90th_pct_count_21d": {"inputs": ["volume"], "func": vp_138_vol_above_90th_pct_count_21d},
    "vp_139_vol_above_75th_pct_count_63d": {"inputs": ["volume"], "func": vp_139_vol_above_75th_pct_count_63d},
    "vp_140_vol_above_90th_pct_fraction_63d": {"inputs": ["volume"], "func": vp_140_vol_above_90th_pct_fraction_63d},
    "vp_141_vol_pct_rank_21d_avg_in_252d": {"inputs": ["volume"], "func": vp_141_vol_pct_rank_21d_avg_in_252d},
    "vp_142_vol_pct_rank_5d_avg_in_252d": {"inputs": ["volume"], "func": vp_142_vol_pct_rank_5d_avg_in_252d},
    "vp_143_vol_above_90th_pct_max_streak_252d": {"inputs": ["volume"], "func": vp_143_vol_above_90th_pct_max_streak_252d},
    "vp_144_vol_above_75th_pct_fraction_252d": {"inputs": ["volume"], "func": vp_144_vol_above_75th_pct_fraction_252d},
    "vp_145_vol_pct_rank_current_vs_252d": {"inputs": ["volume"], "func": vp_145_vol_pct_rank_current_vs_252d},
    "vp_146_elev_vol_persistence_index": {"inputs": ["volume"], "func": vp_146_elev_vol_persistence_index},
    "vp_147_elev_vol_streak_acc_5d": {"inputs": ["volume"], "func": vp_147_elev_vol_streak_acc_5d},
    "vp_148_elev_vol_on_down_x_streak_len": {"inputs": ["close", "volume"], "func": vp_148_elev_vol_on_down_x_streak_len},
    "vp_149_vol_ratio_21d_vs_252d_x_elev_frac": {"inputs": ["volume"], "func": vp_149_vol_ratio_21d_vs_252d_x_elev_frac},
    "vp_150_vol_persistence_distress_composite": {"inputs": ["close", "volume"], "func": vp_150_vol_persistence_distress_composite},
    "vp_176_elev_vol_on_gap_down_consec": {"inputs": ["open", "close", "volume"], "func": vp_176_elev_vol_on_gap_down_consec},
    "vp_177_elev_vol_on_gap_down_count_21d": {"inputs": ["open", "close", "volume"], "func": vp_177_elev_vol_on_gap_down_count_21d},
    "vp_178_elev_vol_on_gap_down_count_63d": {"inputs": ["open", "close", "volume"], "func": vp_178_elev_vol_on_gap_down_count_63d},
    "vp_179_elev_vol_on_close_below_open_consec": {"inputs": ["open", "close", "volume"], "func": vp_179_elev_vol_on_close_below_open_consec},
    "vp_180_elev_vol_close_below_open_count_63d": {"inputs": ["open", "close", "volume"], "func": vp_180_elev_vol_close_below_open_count_63d},
    "vp_181_high_vol_low_close_consec": {"inputs": ["close", "high", "volume"], "func": vp_181_high_vol_low_close_consec},
    "vp_182_elev_vol_high_gt_prior_high_consec": {"inputs": ["high", "volume"], "func": vp_182_elev_vol_high_gt_prior_high_consec},
    "vp_183_elev_vol_low_lt_prior_low_consec": {"inputs": ["low", "volume"], "func": vp_183_elev_vol_low_lt_prior_low_consec},
    "vp_184_elev_vol_low_lt_prior_low_count_21d": {"inputs": ["low", "volume"], "func": vp_184_elev_vol_low_lt_prior_low_count_21d},
    "vp_185_elev_vol_low_lt_prior_low_count_63d": {"inputs": ["low", "volume"], "func": vp_185_elev_vol_low_lt_prior_low_count_63d},
    "vp_186_vol_sum_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vp_186_vol_sum_21d_vs_252d_ratio},
    "vp_187_vol_sum_5d_vs_63d_ratio": {"inputs": ["volume"], "func": vp_187_vol_sum_5d_vs_63d_ratio},
    "vp_188_vol_std_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vp_188_vol_std_ratio_21d_vs_252d},
    "vp_189_vol_cv_21d": {"inputs": ["volume"], "func": vp_189_vol_cv_21d},
    "vp_190_vol_cv_63d": {"inputs": ["volume"], "func": vp_190_vol_cv_63d},
    "vp_191_elev_vol_on_down_day_zscore_252d": {"inputs": ["close", "volume"], "func": vp_191_elev_vol_on_down_day_zscore_252d},
    "vp_192_avg_elev_streak_len_252d_pct_rank": {"inputs": ["volume"], "func": vp_192_avg_elev_streak_len_252d_pct_rank},
    "vp_193_vol_ewm_crossover_fraction_252d": {"inputs": ["volume"], "func": vp_193_vol_ewm_crossover_fraction_252d},
    "vp_194_elev_vol_count_126d_pct_rank_252d": {"inputs": ["volume"], "func": vp_194_elev_vol_count_126d_pct_rank_252d},
    "vp_195_vol_above_prior_day_count_63d": {"inputs": ["volume"], "func": vp_195_vol_above_prior_day_count_63d},
    "vp_196_vol_above_prior_day_max_streak_252d": {"inputs": ["volume"], "func": vp_196_vol_above_prior_day_max_streak_252d},
    "vp_197_consec_elev_vol_126d_baseline": {"inputs": ["volume"], "func": vp_197_consec_elev_vol_126d_baseline},
    "vp_198_elev_vol_126d_baseline_count_252d": {"inputs": ["volume"], "func": vp_198_elev_vol_126d_baseline_count_252d},
    "vp_199_vol_log_ratio_63d_vs_252d": {"inputs": ["volume"], "func": vp_199_vol_log_ratio_63d_vs_252d},
    "vp_200_elev_vol_distress_extended_score": {"inputs": ["close", "volume"], "func": vp_200_elev_vol_distress_extended_score},
}
