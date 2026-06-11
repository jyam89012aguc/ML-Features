"""
56_zero_volume_days — Base Features 076-150
Domain: zero-volume / near-zero-volume days and stale-price (unchanged close) sessions
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — dead/illiquid sessions, no-trade and stale-price frequency
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
_NEAR_ZERO_K = 0.05   # volume < 5% of trailing median => "near-zero"
_STALE_TOL = 1e-8     # |close - prior_close| < this => stale price

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
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
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _zero_vol_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: volume == 0."""
    return (volume == 0).astype(float)


def _near_zero_vol_flag(volume: pd.Series, w: int = _TD_MON) -> pd.Series:
    """Binary flag: volume < _NEAR_ZERO_K * trailing-median volume."""
    med = _rolling_median(volume.shift(1), w)
    return (volume < _NEAR_ZERO_K * med.clip(lower=_EPS)).astype(float)


def _stale_price_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is unchanged from prior close."""
    return (close.diff(1).abs() < _STALE_TOL).astype(float)


def _days_since_last_true(cond: pd.Series) -> pd.Series:
    """Days elapsed since the last True event (backward-looking)."""
    idx = np.arange(len(cond))
    last_true = np.full(len(cond), np.nan)
    prev = np.nan
    for i, v in enumerate(cond):
        if v:
            prev = idx[i]
        last_true[i] = prev
    result = idx - np.where(np.isnan(last_true), np.nan, last_true)
    return pd.Series(result, index=cond.index, dtype=float)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Near-zero volume streaks and max streak variants ---

def zvd_076_max_near_zero_streak_21d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive near-zero-volume run in trailing 21-day window."""
    return _rolling_max_streak(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON)


def zvd_077_max_near_zero_streak_63d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive near-zero-volume run in trailing 63-day window."""
    return _rolling_max_streak(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_QTR)


def zvd_078_max_near_zero_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive near-zero-volume run in trailing 252-day window."""
    return _rolling_max_streak(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_YEAR)


def zvd_079_consec_near_zero_streak_log(volume: pd.Series) -> pd.Series:
    """Log1p of current near-zero-volume streak (compresses long tails)."""
    return np.log1p(_consec_streak(_near_zero_vol_flag(volume, _TD_MON) == 1))


def zvd_080_consec_stale_streak_log(close: pd.Series) -> pd.Series:
    """Log1p of current stale-price streak."""
    return np.log1p(_consec_streak(_stale_price_flag(close) == 1))


def zvd_081_near_zero_streak_norm_252d(volume: pd.Series) -> pd.Series:
    """Current near-zero streak normalized by 252-day average near-zero streak."""
    streak = _consec_streak(_near_zero_vol_flag(volume, _TD_MON) == 1)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def zvd_082_stale_streak_norm_252d(close: pd.Series) -> pd.Series:
    """Current stale-price streak normalized by 252-day average stale streak."""
    streak = _consec_streak(_stale_price_flag(close) == 1)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def zvd_083_zero_vol_streak_expanding_max(volume: pd.Series) -> pd.Series:
    """Expanding all-time maximum consecutive zero-volume streak."""
    streak = _consec_streak(volume == 0)
    return streak.expanding(min_periods=1).max()


def zvd_084_stale_streak_expanding_max(close: pd.Series) -> pd.Series:
    """Expanding all-time maximum consecutive stale-price streak."""
    streak = _consec_streak(_stale_price_flag(close) == 1)
    return streak.expanding(min_periods=1).max()


def zvd_085_max_dead_session_streak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum consecutive dead-session run (zero-vol OR stale) in trailing 63 days."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0)
    return _rolling_max_streak(dead, _TD_QTR)


# --- Group I (086-095): Volume ratio relative comparisons and near-zero variants ---

def zvd_086_vol_below_1pct_median_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume below 1% of 21-day trailing median (extremely near-zero)."""
    med = _rolling_median(volume.shift(1), _TD_MON)
    return (volume < 0.01 * med.clip(lower=_EPS)).astype(float)


def zvd_087_vol_below_2pct_median_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume below 2% of 21-day trailing median."""
    med = _rolling_median(volume.shift(1), _TD_MON)
    return (volume < 0.02 * med.clip(lower=_EPS)).astype(float)


def zvd_088_vol_below_10pct_median_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume below 10% of 21-day trailing median."""
    med = _rolling_median(volume.shift(1), _TD_MON)
    return (volume < 0.10 * med.clip(lower=_EPS)).astype(float)


def zvd_089_vol_below_20pct_median_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume below 20% of 21-day trailing median."""
    med = _rolling_median(volume.shift(1), _TD_MON)
    return (volume < 0.20 * med.clip(lower=_EPS)).astype(float)


def zvd_090_vol_below_1pct_count_21d(volume: pd.Series) -> pd.Series:
    """Count of days with volume below 1% of trailing-median in 21-day window."""
    flag = (volume < 0.01 * _rolling_median(volume.shift(1), _TD_MON).clip(lower=_EPS)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def zvd_091_vol_below_10pct_count_21d(volume: pd.Series) -> pd.Series:
    """Count of days with volume below 10% of trailing-median in 21-day window."""
    flag = (volume < 0.10 * _rolling_median(volume.shift(1), _TD_MON).clip(lower=_EPS)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def zvd_092_vol_below_10pct_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days with volume below 10% of trailing-median in 63-day window."""
    flag = (volume < 0.10 * _rolling_median(volume.shift(1), _TD_MON).clip(lower=_EPS)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def zvd_093_vol_below_20pct_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days with volume below 20% of trailing-median in 63-day window."""
    flag = (volume < 0.20 * _rolling_median(volume.shift(1), _TD_MON).clip(lower=_EPS)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def zvd_094_vol_below_10pct_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days with volume below 10% of trailing median."""
    flag = (volume < 0.10 * _rolling_median(volume.shift(1), _TD_MON).clip(lower=_EPS)).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def zvd_095_vol_below_20pct_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days with volume below 20% of trailing median."""
    flag = (volume < 0.20 * _rolling_median(volume.shift(1), _TD_MON).clip(lower=_EPS)).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


# --- Group J (096-105): Stale high/low and open-unchanged variants ---

def zvd_096_stale_high_flag(high: pd.Series) -> pd.Series:
    """Flag: today's high is identical to prior day's high (stale high)."""
    return (high.diff(1).abs() < _STALE_TOL).astype(float)


def zvd_097_stale_low_flag(low: pd.Series) -> pd.Series:
    """Flag: today's low is identical to prior day's low (stale low)."""
    return (low.diff(1).abs() < _STALE_TOL).astype(float)


def zvd_098_stale_open_flag(open: pd.Series) -> pd.Series:
    """Flag: today's open is identical to prior day's open (stale open)."""
    return (open.diff(1).abs() < _STALE_TOL).astype(float)


def zvd_099_stale_ohlc_all_flag(close: pd.Series, open: pd.Series,
                                  high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: all four OHLC values are unchanged from prior day (total freeze)."""
    c_stale = close.diff(1).abs() < _STALE_TOL
    o_stale = open.diff(1).abs() < _STALE_TOL
    h_stale = high.diff(1).abs() < _STALE_TOL
    l_stale = low.diff(1).abs() < _STALE_TOL
    return (c_stale & o_stale & h_stale & l_stale).astype(float)


def zvd_100_stale_high_count_21d(high: pd.Series) -> pd.Series:
    """Count of stale-high days in trailing 21-day window."""
    return _rolling_sum((high.diff(1).abs() < _STALE_TOL).astype(float), _TD_MON)


def zvd_101_stale_low_count_21d(low: pd.Series) -> pd.Series:
    """Count of stale-low days in trailing 21-day window."""
    return _rolling_sum((low.diff(1).abs() < _STALE_TOL).astype(float), _TD_MON)


def zvd_102_stale_high_count_63d(high: pd.Series) -> pd.Series:
    """Count of stale-high days in trailing 63-day window."""
    return _rolling_sum((high.diff(1).abs() < _STALE_TOL).astype(float), _TD_QTR)


def zvd_103_stale_low_count_63d(low: pd.Series) -> pd.Series:
    """Count of stale-low days in trailing 63-day window."""
    return _rolling_sum((low.diff(1).abs() < _STALE_TOL).astype(float), _TD_QTR)


def zvd_104_stale_ohlc_all_count_21d(close: pd.Series, open: pd.Series,
                                       high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of all-OHLC-stale days in trailing 21-day window."""
    flag = zvd_099_stale_ohlc_all_flag(close, open, high, low)
    return _rolling_sum(flag, _TD_MON)


def zvd_105_stale_ohlc_all_frac_252d(close: pd.Series, open: pd.Series,
                                       high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days where all OHLC are stale."""
    flag = zvd_099_stale_ohlc_all_flag(close, open, high, low)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


# --- Group K (106-115): Zero-volume multi-month window proportions ---

def zvd_106_zero_vol_frac_5d(volume: pd.Series) -> pd.Series:
    """Fraction of last 5 days with zero volume."""
    return _rolling_count_true(volume == 0, _TD_WEEK) / _TD_WEEK


def zvd_107_near_zero_vol_frac_5d(volume: pd.Series) -> pd.Series:
    """Fraction of last 5 days with near-zero volume."""
    return _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_WEEK) / _TD_WEEK


def zvd_108_dead_session_frac_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 5 days that are dead (zero-vol OR stale-price)."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    return _rolling_sum(dead, _TD_WEEK) / _TD_WEEK


def zvd_109_zero_vol_count_504d(volume: pd.Series) -> pd.Series:
    """Count of zero-volume days in trailing 504-day (2-year) window."""
    return _rolling_count_true(volume == 0, 504)


def zvd_110_zero_vol_frac_504d(volume: pd.Series) -> pd.Series:
    """Fraction of last 504 days with zero volume."""
    return zvd_109_zero_vol_count_504d(volume) / 504


def zvd_111_near_zero_vol_count_126d(volume: pd.Series) -> pd.Series:
    """Count of near-zero-volume days in trailing 126-day window."""
    return _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_HALF)


def zvd_112_near_zero_vol_frac_126d(volume: pd.Series) -> pd.Series:
    """Fraction of last 126 days with near-zero volume."""
    return zvd_111_near_zero_vol_count_126d(volume) / _TD_HALF


def zvd_113_dead_session_count_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of dead sessions (zero-vol OR stale) in trailing 126-day window."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    return _rolling_sum(dead, _TD_HALF)


def zvd_114_dead_session_frac_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 504 days classified as dead sessions."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    return _rolling_sum(dead, 504) / 504


def zvd_115_zero_vol_pct_rank_63d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 63-day volume series."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


# --- Group L (116-125): EWM-based dead-session metrics ---

def zvd_116_zero_vol_ewm_flag_mean_21(volume: pd.Series) -> pd.Series:
    """EWM (span=21) of zero-volume flag (exponentially weighted dead-session rate)."""
    return _ewm_mean(_zero_vol_flag(volume), _TD_MON)


def zvd_117_near_zero_vol_ewm_mean_21(volume: pd.Series) -> pd.Series:
    """EWM (span=21) of near-zero-volume flag."""
    return _ewm_mean(_near_zero_vol_flag(volume, _TD_MON), _TD_MON)


def zvd_118_stale_price_ewm_mean_21(close: pd.Series) -> pd.Series:
    """EWM (span=21) of stale-price flag."""
    return _ewm_mean(_stale_price_flag(close), _TD_MON)


def zvd_119_dead_session_ewm_mean_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM (span=21) of dead-session flag (zero-vol OR stale)."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    return _ewm_mean(dead, _TD_MON)


def zvd_120_dead_session_ewm_mean_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM (span=63) of dead-session flag."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    return _ewm_mean(dead, _TD_QTR)


def zvd_121_zero_vol_ewm_vs_rolling_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of EWM-21 zero-vol rate to 63-day rolling zero-vol rate."""
    ewm = _ewm_mean(_zero_vol_flag(volume), _TD_MON)
    roll = _rolling_mean(_zero_vol_flag(volume), _TD_QTR)
    return _safe_div(ewm, roll)


def zvd_122_stale_ewm_vs_rolling_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM-21 stale-price rate to 63-day rolling stale-price rate."""
    ewm = _ewm_mean(_stale_price_flag(close), _TD_MON)
    roll = _rolling_mean(_stale_price_flag(close), _TD_QTR)
    return _safe_div(ewm, roll)


def zvd_123_near_zero_vol_ewm_mean_63(volume: pd.Series) -> pd.Series:
    """EWM (span=63) of near-zero-volume flag."""
    return _ewm_mean(_near_zero_vol_flag(volume, _TD_MON), _TD_QTR)


def zvd_124_dead_session_ewm_63_vs_252_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of EWM-63 dead-session rate to 252-day rolling dead-session rate."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    ewm = _ewm_mean(dead, _TD_QTR)
    roll = _rolling_mean(dead, _TD_YEAR)
    return _safe_div(ewm, roll)


def zvd_125_near_zero_vol_ewm_21_vs_252_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of EWM-21 near-zero rate to 252-day rolling near-zero rate."""
    nz = _near_zero_vol_flag(volume, _TD_MON)
    ewm = _ewm_mean(nz, _TD_MON)
    roll = _rolling_mean(nz, _TD_YEAR)
    return _safe_div(ewm, roll)


# --- Group M (126-135): Conditional stale/zero-vol on price direction ---

def zvd_126_stale_on_down_day_flag(close: pd.Series) -> pd.Series:
    """Flag: stale-price day occurring after a prior down-day close."""
    prior_down = (close.shift(1) < close.shift(2)).astype(float)
    return _stale_price_flag(close) * prior_down


def zvd_127_stale_on_up_day_flag(close: pd.Series) -> pd.Series:
    """Flag: stale-price day occurring after a prior up-day close."""
    prior_up = (close.shift(1) > close.shift(2)).astype(float)
    return _stale_price_flag(close) * prior_up


def zvd_128_zero_vol_on_down_day_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: zero-volume day after a prior down-close day."""
    prior_down = (close.shift(1) < close.shift(2)).astype(float)
    return _zero_vol_flag(volume) * prior_down


def zvd_129_near_zero_vol_on_down_day_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: near-zero volume day after a prior down-close day."""
    prior_down = (close.shift(1) < close.shift(2)).astype(float)
    return _near_zero_vol_flag(volume, _TD_MON) * prior_down


def zvd_130_stale_price_count_21d_on_down_days(close: pd.Series) -> pd.Series:
    """Count of stale-price days (post-down-day) in trailing 21-day window."""
    prior_down = (close.shift(1) < close.shift(2)).astype(float)
    stale_down = (_stale_price_flag(close) * prior_down)
    return _rolling_sum(stale_down, _TD_MON)


def zvd_131_zero_vol_count_21d_on_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of zero-vol days (post-down) in trailing 21-day window."""
    prior_down = (close.shift(1) < close.shift(2)).astype(float)
    zero_down = (_zero_vol_flag(volume) * prior_down)
    return _rolling_sum(zero_down, _TD_MON)


def zvd_132_stale_on_low_vol_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: stale-price AND volume is in lowest quartile of 63-day range."""
    pct = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    low_vol = (pct < 0.25).astype(float)
    return _stale_price_flag(close) * low_vol


def zvd_133_stale_run_after_active_flag(close: pd.Series) -> pd.Series:
    """Flag: first stale-price day following 3+ consecutive non-stale active days."""
    not_stale = (_stale_price_flag(close) == 0).astype(float)
    active_run = _consec_streak(not_stale == 1)
    return (_stale_price_flag(close) * (active_run.shift(1) >= 3).astype(float)).fillna(0.0)


def zvd_134_near_zero_vol_frac_21d_norm_by_252d(volume: pd.Series) -> pd.Series:
    """21-day near-zero-vol fraction normalized by 252-day average fraction."""
    frac21 = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON) / _TD_MON
    avg = _rolling_mean(frac21, _TD_YEAR)
    return _safe_div(frac21, avg)


def zvd_135_stale_price_frac_21d_norm_by_252d(close: pd.Series) -> pd.Series:
    """21-day stale-price fraction normalized by 252-day average fraction."""
    frac21 = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON) / _TD_MON
    avg = _rolling_mean(frac21, _TD_YEAR)
    return _safe_div(frac21, avg)


# --- Group N (136-145): Interaction and composite dead-session scores ---

def zvd_136_dead_session_score_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite score: 21d zero-vol frac + 21d stale frac + near-zero 21d frac."""
    zvf = _rolling_count_true(volume == 0, _TD_MON) / _TD_MON
    spf = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON) / _TD_MON
    nzf = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON) / _TD_MON
    return zvf + spf + nzf


def zvd_137_dead_session_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite dead-session score over 63-day window."""
    zvf = _rolling_count_true(volume == 0, _TD_QTR) / _TD_QTR
    spf = _rolling_count_true(_stale_price_flag(close) == 1, _TD_QTR) / _TD_QTR
    nzf = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_QTR) / _TD_QTR
    return zvf + spf + nzf


def zvd_138_dead_score_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day composite dead score within trailing 252 days."""
    score = zvd_136_dead_session_score_composite(close, volume)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def zvd_139_dead_score_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day dead score within trailing 252 days."""
    score = zvd_137_dead_session_score_63d(close, volume)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def zvd_140_zero_vol_flag_x_stale_count21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current zero-vol flag multiplied by 21-day stale count (interaction term)."""
    zflag = _zero_vol_flag(volume)
    sc21 = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON)
    return zflag * sc21


def zvd_141_near_zero_frac21_x_stale_frac21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of 21-day near-zero fraction and 21-day stale fraction."""
    nzf = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON) / _TD_MON
    spf = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON) / _TD_MON
    return nzf * spf


def zvd_142_vol_zscore_63d_when_stale(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score (63d) masked to stale-price days; zero on non-stale days."""
    mu = _rolling_mean(volume.shift(1), _TD_QTR)
    sigma = _rolling_std(volume.shift(1), _TD_QTR)
    z = _safe_div(volume - mu, sigma)
    return z * _stale_price_flag(close)


def zvd_143_stale_streak_gt3_flag(close: pd.Series) -> pd.Series:
    """Flag: current stale-price streak >= 3 days."""
    return (_consec_streak(_stale_price_flag(close) == 1) >= 3).astype(float)


def zvd_144_near_zero_streak_gt3_flag(volume: pd.Series) -> pd.Series:
    """Flag: current near-zero-volume streak >= 3 days."""
    return (_consec_streak(_near_zero_vol_flag(volume, _TD_MON) == 1) >= 3).astype(float)


def zvd_145_dead_session_gt5_consec_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current dead-session streak >= 5 days (full week of dead trading)."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0)
    return (_consec_streak(dead) >= 5).astype(float)


# --- Group O (146-150): Frequency / recurrence of dead-session clusters ---

def zvd_146_zero_vol_start_freq_252d(volume: pd.Series) -> pd.Series:
    """Count of new zero-volume streak starts in trailing 252 days."""
    zflag = _zero_vol_flag(volume)
    is_start = ((zflag == 1) & (zflag.shift(1) == 0)).astype(float)
    return _rolling_sum(is_start, _TD_YEAR)


def zvd_147_stale_start_freq_252d(close: pd.Series) -> pd.Series:
    """Count of new stale-price streak starts in trailing 252 days."""
    sp = _stale_price_flag(close)
    is_start = ((sp == 1) & (sp.shift(1) == 0)).astype(float)
    return _rolling_sum(is_start, _TD_YEAR)


def zvd_148_near_zero_start_freq_252d(volume: pd.Series) -> pd.Series:
    """Count of new near-zero-volume streak starts in trailing 252 days."""
    nz = _near_zero_vol_flag(volume, _TD_MON)
    is_start = ((nz == 1) & (nz.shift(1) == 0)).astype(float)
    return _rolling_sum(is_start, _TD_YEAR)


def zvd_149_avg_stale_streak_len_252d(close: pd.Series) -> pd.Series:
    """Average length of completed stale-price streaks over trailing 252 days."""
    sp = _stale_price_flag(close)
    is_in = sp
    is_start = ((sp == 1) & (sp.shift(1) == 0)).astype(float)
    total = _rolling_sum(is_in, _TD_YEAR)
    starts = _rolling_sum(is_start, _TD_YEAR)
    return _safe_div(total, starts.clip(lower=1))


def zvd_150_avg_near_zero_streak_len_252d(volume: pd.Series) -> pd.Series:
    """Average length of completed near-zero-vol streaks over trailing 252 days."""
    nz = _near_zero_vol_flag(volume, _TD_MON)
    is_start = ((nz == 1) & (nz.shift(1) == 0)).astype(float)
    total = _rolling_sum(nz, _TD_YEAR)
    starts = _rolling_sum(is_start, _TD_YEAR)
    return _safe_div(total, starts.clip(lower=1))


# ── Registry ──────────────────────────────────────────────────────────────────

ZERO_VOLUME_DAYS_REGISTRY_076_150 = {
    "zvd_076_max_near_zero_streak_21d": {"inputs": ["volume"], "func": zvd_076_max_near_zero_streak_21d},
    "zvd_077_max_near_zero_streak_63d": {"inputs": ["volume"], "func": zvd_077_max_near_zero_streak_63d},
    "zvd_078_max_near_zero_streak_252d": {"inputs": ["volume"], "func": zvd_078_max_near_zero_streak_252d},
    "zvd_079_consec_near_zero_streak_log": {"inputs": ["volume"], "func": zvd_079_consec_near_zero_streak_log},
    "zvd_080_consec_stale_streak_log": {"inputs": ["close"], "func": zvd_080_consec_stale_streak_log},
    "zvd_081_near_zero_streak_norm_252d": {"inputs": ["volume"], "func": zvd_081_near_zero_streak_norm_252d},
    "zvd_082_stale_streak_norm_252d": {"inputs": ["close"], "func": zvd_082_stale_streak_norm_252d},
    "zvd_083_zero_vol_streak_expanding_max": {"inputs": ["volume"], "func": zvd_083_zero_vol_streak_expanding_max},
    "zvd_084_stale_streak_expanding_max": {"inputs": ["close"], "func": zvd_084_stale_streak_expanding_max},
    "zvd_085_max_dead_session_streak_63d": {"inputs": ["close", "volume"], "func": zvd_085_max_dead_session_streak_63d},
    "zvd_086_vol_below_1pct_median_flag": {"inputs": ["volume"], "func": zvd_086_vol_below_1pct_median_flag},
    "zvd_087_vol_below_2pct_median_flag": {"inputs": ["volume"], "func": zvd_087_vol_below_2pct_median_flag},
    "zvd_088_vol_below_10pct_median_flag": {"inputs": ["volume"], "func": zvd_088_vol_below_10pct_median_flag},
    "zvd_089_vol_below_20pct_median_flag": {"inputs": ["volume"], "func": zvd_089_vol_below_20pct_median_flag},
    "zvd_090_vol_below_1pct_count_21d": {"inputs": ["volume"], "func": zvd_090_vol_below_1pct_count_21d},
    "zvd_091_vol_below_10pct_count_21d": {"inputs": ["volume"], "func": zvd_091_vol_below_10pct_count_21d},
    "zvd_092_vol_below_10pct_count_63d": {"inputs": ["volume"], "func": zvd_092_vol_below_10pct_count_63d},
    "zvd_093_vol_below_20pct_count_63d": {"inputs": ["volume"], "func": zvd_093_vol_below_20pct_count_63d},
    "zvd_094_vol_below_10pct_frac_252d": {"inputs": ["volume"], "func": zvd_094_vol_below_10pct_frac_252d},
    "zvd_095_vol_below_20pct_frac_252d": {"inputs": ["volume"], "func": zvd_095_vol_below_20pct_frac_252d},
    "zvd_096_stale_high_flag": {"inputs": ["high"], "func": zvd_096_stale_high_flag},
    "zvd_097_stale_low_flag": {"inputs": ["low"], "func": zvd_097_stale_low_flag},
    "zvd_098_stale_open_flag": {"inputs": ["open"], "func": zvd_098_stale_open_flag},
    "zvd_099_stale_ohlc_all_flag": {"inputs": ["close", "open", "high", "low"], "func": zvd_099_stale_ohlc_all_flag},
    "zvd_100_stale_high_count_21d": {"inputs": ["high"], "func": zvd_100_stale_high_count_21d},
    "zvd_101_stale_low_count_21d": {"inputs": ["low"], "func": zvd_101_stale_low_count_21d},
    "zvd_102_stale_high_count_63d": {"inputs": ["high"], "func": zvd_102_stale_high_count_63d},
    "zvd_103_stale_low_count_63d": {"inputs": ["low"], "func": zvd_103_stale_low_count_63d},
    "zvd_104_stale_ohlc_all_count_21d": {"inputs": ["close", "open", "high", "low"], "func": zvd_104_stale_ohlc_all_count_21d},
    "zvd_105_stale_ohlc_all_frac_252d": {"inputs": ["close", "open", "high", "low"], "func": zvd_105_stale_ohlc_all_frac_252d},
    "zvd_106_zero_vol_frac_5d": {"inputs": ["volume"], "func": zvd_106_zero_vol_frac_5d},
    "zvd_107_near_zero_vol_frac_5d": {"inputs": ["volume"], "func": zvd_107_near_zero_vol_frac_5d},
    "zvd_108_dead_session_frac_5d": {"inputs": ["close", "volume"], "func": zvd_108_dead_session_frac_5d},
    "zvd_109_zero_vol_count_504d": {"inputs": ["volume"], "func": zvd_109_zero_vol_count_504d},
    "zvd_110_zero_vol_frac_504d": {"inputs": ["volume"], "func": zvd_110_zero_vol_frac_504d},
    "zvd_111_near_zero_vol_count_126d": {"inputs": ["volume"], "func": zvd_111_near_zero_vol_count_126d},
    "zvd_112_near_zero_vol_frac_126d": {"inputs": ["volume"], "func": zvd_112_near_zero_vol_frac_126d},
    "zvd_113_dead_session_count_126d": {"inputs": ["close", "volume"], "func": zvd_113_dead_session_count_126d},
    "zvd_114_dead_session_frac_504d": {"inputs": ["close", "volume"], "func": zvd_114_dead_session_frac_504d},
    "zvd_115_zero_vol_pct_rank_63d": {"inputs": ["volume"], "func": zvd_115_zero_vol_pct_rank_63d},
    "zvd_116_zero_vol_ewm_flag_mean_21": {"inputs": ["volume"], "func": zvd_116_zero_vol_ewm_flag_mean_21},
    "zvd_117_near_zero_vol_ewm_mean_21": {"inputs": ["volume"], "func": zvd_117_near_zero_vol_ewm_mean_21},
    "zvd_118_stale_price_ewm_mean_21": {"inputs": ["close"], "func": zvd_118_stale_price_ewm_mean_21},
    "zvd_119_dead_session_ewm_mean_21": {"inputs": ["close", "volume"], "func": zvd_119_dead_session_ewm_mean_21},
    "zvd_120_dead_session_ewm_mean_63": {"inputs": ["close", "volume"], "func": zvd_120_dead_session_ewm_mean_63},
    "zvd_121_zero_vol_ewm_vs_rolling_ratio": {"inputs": ["volume"], "func": zvd_121_zero_vol_ewm_vs_rolling_ratio},
    "zvd_122_stale_ewm_vs_rolling_ratio": {"inputs": ["close"], "func": zvd_122_stale_ewm_vs_rolling_ratio},
    "zvd_123_near_zero_vol_ewm_mean_63": {"inputs": ["volume"], "func": zvd_123_near_zero_vol_ewm_mean_63},
    "zvd_124_dead_session_ewm_63_vs_252_ratio": {"inputs": ["close", "volume"], "func": zvd_124_dead_session_ewm_63_vs_252_ratio},
    "zvd_125_near_zero_vol_ewm_21_vs_252_ratio": {"inputs": ["volume"], "func": zvd_125_near_zero_vol_ewm_21_vs_252_ratio},
    "zvd_126_stale_on_down_day_flag": {"inputs": ["close"], "func": zvd_126_stale_on_down_day_flag},
    "zvd_127_stale_on_up_day_flag": {"inputs": ["close"], "func": zvd_127_stale_on_up_day_flag},
    "zvd_128_zero_vol_on_down_day_flag": {"inputs": ["close", "volume"], "func": zvd_128_zero_vol_on_down_day_flag},
    "zvd_129_near_zero_vol_on_down_day_flag": {"inputs": ["close", "volume"], "func": zvd_129_near_zero_vol_on_down_day_flag},
    "zvd_130_stale_price_count_21d_on_down_days": {"inputs": ["close"], "func": zvd_130_stale_price_count_21d_on_down_days},
    "zvd_131_zero_vol_count_21d_on_down_days": {"inputs": ["close", "volume"], "func": zvd_131_zero_vol_count_21d_on_down_days},
    "zvd_132_stale_on_low_vol_flag": {"inputs": ["close", "volume"], "func": zvd_132_stale_on_low_vol_flag},
    "zvd_133_stale_run_after_active_flag": {"inputs": ["close"], "func": zvd_133_stale_run_after_active_flag},
    "zvd_134_near_zero_vol_frac_21d_norm_by_252d": {"inputs": ["volume"], "func": zvd_134_near_zero_vol_frac_21d_norm_by_252d},
    "zvd_135_stale_price_frac_21d_norm_by_252d": {"inputs": ["close"], "func": zvd_135_stale_price_frac_21d_norm_by_252d},
    "zvd_136_dead_session_score_composite": {"inputs": ["close", "volume"], "func": zvd_136_dead_session_score_composite},
    "zvd_137_dead_session_score_63d": {"inputs": ["close", "volume"], "func": zvd_137_dead_session_score_63d},
    "zvd_138_dead_score_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": zvd_138_dead_score_21d_pct_rank_252d},
    "zvd_139_dead_score_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": zvd_139_dead_score_63d_pct_rank_252d},
    "zvd_140_zero_vol_flag_x_stale_count21": {"inputs": ["close", "volume"], "func": zvd_140_zero_vol_flag_x_stale_count21},
    "zvd_141_near_zero_frac21_x_stale_frac21": {"inputs": ["close", "volume"], "func": zvd_141_near_zero_frac21_x_stale_frac21},
    "zvd_142_vol_zscore_63d_when_stale": {"inputs": ["close", "volume"], "func": zvd_142_vol_zscore_63d_when_stale},
    "zvd_143_stale_streak_gt3_flag": {"inputs": ["close"], "func": zvd_143_stale_streak_gt3_flag},
    "zvd_144_near_zero_streak_gt3_flag": {"inputs": ["volume"], "func": zvd_144_near_zero_streak_gt3_flag},
    "zvd_145_dead_session_gt5_consec_flag": {"inputs": ["close", "volume"], "func": zvd_145_dead_session_gt5_consec_flag},
    "zvd_146_zero_vol_start_freq_252d": {"inputs": ["volume"], "func": zvd_146_zero_vol_start_freq_252d},
    "zvd_147_stale_start_freq_252d": {"inputs": ["close"], "func": zvd_147_stale_start_freq_252d},
    "zvd_148_near_zero_start_freq_252d": {"inputs": ["volume"], "func": zvd_148_near_zero_start_freq_252d},
    "zvd_149_avg_stale_streak_len_252d": {"inputs": ["close"], "func": zvd_149_avg_stale_streak_len_252d},
    "zvd_150_avg_near_zero_streak_len_252d": {"inputs": ["volume"], "func": zvd_150_avg_near_zero_streak_len_252d},
}
