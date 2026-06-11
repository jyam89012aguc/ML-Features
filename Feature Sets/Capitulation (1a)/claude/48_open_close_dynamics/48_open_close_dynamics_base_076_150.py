"""
48_open_close_dynamics — Base Features 076-150
Domain: open-to-close vs close-to-open session return decomposition — intraday vs overnight dynamics
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


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


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


def _intraday_ret(open: pd.Series, close: pd.Series) -> pd.Series:
    """Log return from open to close."""
    return _log_safe(close) - _log_safe(open)


def _overnight_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log return from prior close to today's open."""
    return _log_safe(open) - _log_safe(close.shift(1))


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Cumulative session return paths ---

def ocd_076_cum_intraday_ret_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative sum of intraday log returns over trailing 21 days."""
    return _rolling_sum(_intraday_ret(open, close), _TD_MON)


def ocd_077_cum_overnight_ret_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative sum of overnight log returns over trailing 21 days."""
    return _rolling_sum(_overnight_ret(close, open), _TD_MON)


def ocd_078_cum_intraday_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative sum of intraday log returns over trailing 63 days."""
    return _rolling_sum(_intraday_ret(open, close), _TD_QTR)


def ocd_079_cum_overnight_ret_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative sum of overnight log returns over trailing 63 days."""
    return _rolling_sum(_overnight_ret(close, open), _TD_QTR)


def ocd_080_cum_intraday_ret_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative sum of intraday log returns over trailing 252 days."""
    return _rolling_sum(_intraday_ret(open, close), _TD_YEAR)


def ocd_081_cum_overnight_ret_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative sum of overnight log returns over trailing 252 days."""
    return _rolling_sum(_overnight_ret(close, open), _TD_YEAR)


def ocd_082_intraday_minus_overnight_cum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day cumulative intraday minus cumulative overnight (session imbalance)."""
    return ocd_076_cum_intraday_ret_21d(open, close) - ocd_077_cum_overnight_ret_21d(close, open)


def ocd_083_intraday_minus_overnight_cum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day cumulative intraday minus cumulative overnight."""
    return ocd_078_cum_intraday_ret_63d(open, close) - ocd_079_cum_overnight_ret_63d(close, open)


def ocd_084_overnight_dominates_loss_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if 21-day cum overnight loss exceeds 21-day cum intraday loss."""
    cum_over = ocd_077_cum_overnight_ret_21d(close, open)
    cum_intra = ocd_076_cum_intraday_ret_21d(open, close)
    return (cum_over < cum_intra).astype(float)


def ocd_085_intraday_dominates_loss_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if 21-day cum intraday loss exceeds 21-day cum overnight loss."""
    cum_over = ocd_077_cum_overnight_ret_21d(close, open)
    cum_intra = ocd_076_cum_intraday_ret_21d(open, close)
    return (cum_intra < cum_over).astype(float)


# --- Group I (086-095): Session return normalization and z-scores ---

def ocd_086_intraday_ret_zscore_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of intraday return relative to 252-day distribution."""
    r = _intraday_ret(open, close)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def ocd_087_overnight_ret_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of overnight return relative to 252-day distribution."""
    r = _overnight_ret(close, open)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def ocd_088_intraday_ret_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of intraday return in trailing 252-day window."""
    r = _intraday_ret(open, close)
    return r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def ocd_089_overnight_ret_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of overnight return in trailing 252-day window."""
    r = _overnight_ret(close, open)
    return r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def ocd_090_intraday_mean_21d_zscore_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21-day mean intraday return within 252-day distribution."""
    r = _intraday_ret(open, close)
    mean21 = _rolling_mean(r, _TD_MON)
    m = _rolling_mean(mean21, _TD_YEAR)
    s = _rolling_std(mean21, _TD_YEAR)
    return _safe_div(mean21 - m, s)


def ocd_091_overnight_mean_21d_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 21-day mean overnight return within 252-day distribution."""
    r = _overnight_ret(close, open)
    mean21 = _rolling_mean(r, _TD_MON)
    m = _rolling_mean(mean21, _TD_YEAR)
    s = _rolling_std(mean21, _TD_YEAR)
    return _safe_div(mean21 - m, s)


def ocd_092_intraday_vol_zscore_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21-day intraday vol within 252-day vol distribution."""
    r = _intraday_ret(open, close)
    std21 = _rolling_std(r, _TD_MON)
    m = _rolling_mean(std21, _TD_YEAR)
    s = _rolling_std(std21, _TD_YEAR)
    return _safe_div(std21 - m, s)


def ocd_093_overnight_vol_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 21-day overnight vol within 252-day vol distribution."""
    r = _overnight_ret(close, open)
    std21 = _rolling_std(r, _TD_MON)
    m = _rolling_mean(std21, _TD_YEAR)
    s = _rolling_std(std21, _TD_YEAR)
    return _safe_div(std21 - m, s)


def ocd_094_session_ratio_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of overnight/intraday vol ratio within 252-day distribution."""
    over_std = _rolling_std(_overnight_ret(close, open), _TD_MON)
    intra_std = _rolling_std(_intraday_ret(open, close), _TD_MON)
    ratio = _safe_div(over_std, intra_std)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def ocd_095_intraday_expanding_pct_rank(open: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of today's intraday return."""
    r = _intraday_ret(open, close)
    return r.expanding(min_periods=5).rank(pct=True)


# --- Group J (096-105): Volume-weighted session returns ---

def ocd_096_vol_weighted_intraday_ret_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean intraday return over 21 days."""
    r = _intraday_ret(open, close)
    vw = r * volume
    return _safe_div(_rolling_sum(vw, _TD_MON), _rolling_sum(volume, _TD_MON))


def ocd_097_vol_weighted_overnight_ret_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean overnight return over 21 days."""
    r = _overnight_ret(close, open)
    vw = r * volume
    return _safe_div(_rolling_sum(vw, _TD_MON), _rolling_sum(volume, _TD_MON))


def ocd_098_vol_weighted_intraday_ret_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean intraday return over 63 days."""
    r = _intraday_ret(open, close)
    vw = r * volume
    return _safe_div(_rolling_sum(vw, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def ocd_099_vol_weighted_overnight_ret_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean overnight return over 63 days."""
    r = _overnight_ret(close, open)
    vw = r * volume
    return _safe_div(_rolling_sum(vw, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def ocd_100_high_vol_intraday_loss_mean_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean intraday return on high-volume intraday-loss days (above 21d avg vol), 21d window."""
    r = _intraday_ret(open, close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    masked = r.where((r < 0) & (volume > avg_vol), np.nan)
    return masked.rolling(_TD_MON, min_periods=1).mean()


def ocd_101_high_vol_overnight_loss_mean_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean overnight return on high-volume overnight-loss days, 21d window."""
    r = _overnight_ret(close, open)
    avg_vol = _rolling_mean(volume, _TD_MON)
    masked = r.where((r < 0) & (volume > avg_vol), np.nan)
    return masked.rolling(_TD_MON, min_periods=1).mean()


def ocd_102_intraday_loss_vol_ratio_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on intraday-loss days vs avg volume on intraday-gain days, 21d."""
    r = _intraday_ret(open, close)
    loss_vol = volume.where(r < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    gain_vol = volume.where(r > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(loss_vol, gain_vol)


def ocd_103_overnight_loss_vol_ratio_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on overnight-loss days vs avg volume on overnight-gain days, 21d."""
    r = _overnight_ret(close, open)
    loss_vol = volume.where(r < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    gain_vol = volume.where(r > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(loss_vol, gain_vol)


def ocd_104_vol_on_intraday_loss_days_sum_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume traded on intraday-loss days over trailing 21 days."""
    r = _intraday_ret(open, close)
    return _rolling_sum(volume.where(r < 0, 0.0), _TD_MON)


def ocd_105_vol_on_both_sessions_loss_days_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume on days where both sessions had negative returns, 21d window."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _rolling_sum(volume.where((intra < 0) & (over < 0), 0.0), _TD_MON)


# --- Group K (106-115): Intraday give-back patterns ---

def ocd_106_intraday_giveback_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days where overnight was positive but intraday was negative, 21d."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _rolling_count_true((over > 0) & (intra < 0), _TD_MON)


def ocd_107_intraday_giveback_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of intraday give-back days (overnight+ / intraday-) in 63d window."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _rolling_count_true((over > 0) & (intra < 0), _TD_QTR)


def ocd_108_intraday_giveback_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days with intraday give-back (overnight+, intraday-)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _rolling_count_true((over > 0) & (intra < 0), _TD_MON) / _TD_MON


def ocd_109_avg_giveback_magnitude_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean intraday loss magnitude on give-back days, trailing 21d."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    gb = intra.where((over > 0) & (intra < 0), np.nan)
    return gb.rolling(_TD_MON, min_periods=1).mean()


def ocd_110_full_giveback_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if intraday loss exceeds overnight gain (full give-back)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return ((over > 0) & (intra < 0) & (intra.abs() >= over)).astype(float)


def ocd_111_full_giveback_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of full give-back days (intraday erases all overnight gain) in 21d."""
    return _rolling_sum(ocd_110_full_giveback_flag(close, open), _TD_MON)


def ocd_112_full_giveback_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of full give-back days in trailing 63 days."""
    return _rolling_sum(ocd_110_full_giveback_flag(close, open), _TD_QTR)


def ocd_113_partial_giveback_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if overnight positive, intraday negative, but not full give-back."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return ((over > 0) & (intra < 0) & (intra.abs() < over)).astype(float)


def ocd_114_overnight_gain_captured_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """On gap-up days: fraction of overnight gain retained intraday on avg, 21d."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    retained = (over + intra).where(over > 0, np.nan)
    overnight_gain = over.where(over > 0, np.nan)
    ratio = _safe_div(retained, overnight_gain)
    return ratio.rolling(_TD_MON, min_periods=1).mean()


def ocd_115_consec_full_giveback_days(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current streak of consecutive full give-back days."""
    return _consec_streak(ocd_110_full_giveback_flag(close, open) == 1)


# --- Group L (116-125): Intraday recovery from overnight loss ---

def ocd_116_overnight_loss_recovered_intraday_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if overnight was negative but intraday was positive (recovery day)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return ((over < 0) & (intra > 0)).astype(float)


def ocd_117_overnight_loss_recovered_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of intraday-recovery days (overnight- / intraday+) in 21d window."""
    return _rolling_sum(ocd_116_overnight_loss_recovered_intraday_flag(close, open), _TD_MON)


def ocd_118_overnight_loss_recovered_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days where intraday recovered an overnight loss."""
    return ocd_117_overnight_loss_recovered_count_21d(close, open) / _TD_MON


def ocd_119_avg_intraday_recovery_magnitude_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean intraday gain on overnight-loss recovery days, trailing 21d."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    rec = intra.where((over < 0) & (intra > 0), np.nan)
    return rec.rolling(_TD_MON, min_periods=1).mean()


def ocd_120_full_recovery_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if intraday gain exceeds overnight loss magnitude (full recovery)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return ((over < 0) & (intra > 0) & (intra >= over.abs())).astype(float)


def ocd_121_full_recovery_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of full intraday-recovery days in trailing 21 days."""
    return _rolling_sum(ocd_120_full_recovery_flag(close, open), _TD_MON)


def ocd_122_full_recovery_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of full intraday-recovery days in trailing 63 days."""
    return _rolling_sum(ocd_120_full_recovery_flag(close, open), _TD_QTR)


def ocd_123_recovery_vs_giveback_ratio_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of recovery days to give-back days in trailing 21d (low = bearish)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    rec = _rolling_count_true((over < 0) & (intra > 0), _TD_MON)
    gb = _rolling_count_true((over > 0) & (intra < 0), _TD_MON)
    return _safe_div(rec, gb)


def ocd_124_consec_no_intraday_recovery(close: pd.Series, open: pd.Series) -> pd.Series:
    """Streak of days without any full intraday recovery from overnight loss."""
    return _consec_streak(ocd_120_full_recovery_flag(close, open) == 0)


def ocd_125_overnight_loss_intraday_amplify_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days where overnight loss was amplified intraday, 21d window."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _rolling_count_true((over < 0) & (intra < 0), _TD_MON)


# --- Group M (126-135): Session return extremes and quantiles ---

def ocd_126_intraday_ret_rolling_min_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum intraday return (worst intraday day this month)."""
    return _rolling_min(_intraday_ret(open, close), _TD_MON)


def ocd_127_intraday_ret_rolling_min_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day minimum intraday return."""
    return _rolling_min(_intraday_ret(open, close), _TD_QTR)


def ocd_128_overnight_ret_rolling_min_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day minimum overnight return."""
    return _rolling_min(_overnight_ret(close, open), _TD_MON)


def ocd_129_overnight_ret_rolling_min_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day minimum overnight return."""
    return _rolling_min(_overnight_ret(close, open), _TD_QTR)


def ocd_130_intraday_ret_rolling_max_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day maximum intraday return (best intraday day)."""
    return _rolling_max(_intraday_ret(open, close), _TD_MON)


def ocd_131_overnight_ret_rolling_max_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day maximum overnight return."""
    return _rolling_max(_overnight_ret(close, open), _TD_MON)


def ocd_132_intraday_worst_vs_mean_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of worst intraday day to mean intraday return, 21d window."""
    r = _intraday_ret(open, close)
    return _safe_div(_rolling_min(r, _TD_MON), _rolling_mean(r, _TD_MON).abs() + _EPS)


def ocd_133_overnight_worst_vs_mean_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of worst overnight to mean overnight return, 21d window."""
    r = _overnight_ret(close, open)
    return _safe_div(_rolling_min(r, _TD_MON), _rolling_mean(r, _TD_MON).abs() + _EPS)


def ocd_134_intraday_ret_expanding_min(open: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-time minimum intraday return."""
    return _intraday_ret(open, close).expanding(min_periods=1).min()


def ocd_135_overnight_ret_expanding_min(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding all-time minimum overnight return."""
    return _overnight_ret(close, open).expanding(min_periods=1).min()


# --- Group N (136-145): Session return interaction with price levels ---

def ocd_136_intraday_ret_when_below_sma50_mean_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean intraday return on days when close is below its 50-day SMA, 21d window."""
    r = _intraday_ret(open, close)
    sma50 = _rolling_mean(close, 50)
    masked = r.where(close < sma50, np.nan)
    return masked.rolling(_TD_MON, min_periods=1).mean()


def ocd_137_overnight_ret_when_below_sma50_mean_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean overnight return on days when close is below its 50-day SMA, 21d window."""
    r = _overnight_ret(close, open)
    sma50 = _rolling_mean(close, 50)
    masked = r.where(close < sma50, np.nan)
    return masked.rolling(_TD_MON, min_periods=1).mean()


def ocd_138_intraday_loss_at_52wk_low_flag(open: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 if intraday loss occurs on a day that is a new 252-day closing low."""
    r = _intraday_ret(open, close)
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = close < roll_min
    return ((r < 0) & new_low).astype(float)


def ocd_139_intraday_loss_at_52wk_low_count_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of intraday-loss days at new 52-week lows, trailing 63 days."""
    return _rolling_sum(ocd_138_intraday_loss_at_52wk_low_flag(open, close), _TD_QTR)


def ocd_140_overnight_loss_at_52wk_low_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of overnight-loss days at new 52-week lows, trailing 63 days."""
    r = _overnight_ret(close, open)
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = close < roll_min
    flag = ((r < 0) & new_low).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def ocd_141_intraday_ret_below_sma200_mean_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean intraday return on days below 200-day SMA, trailing 63 days."""
    r = _intraday_ret(open, close)
    sma200 = _rolling_mean(close, 200)
    masked = r.where(close < sma200, np.nan)
    return masked.rolling(_TD_QTR, min_periods=1).mean()


def ocd_142_overnight_ret_below_sma200_mean_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean overnight return on days below 200-day SMA, trailing 63 days."""
    r = _overnight_ret(close, open)
    sma200 = _rolling_mean(close, 200)
    masked = r.where(close < sma200, np.nan)
    return masked.rolling(_TD_QTR, min_periods=1).mean()


def ocd_143_session_loss_asymmetry_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Asymmetry: overnight loss fraction minus intraday loss fraction, 21d."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    over_loss_frac = _rolling_count_true(over < 0, _TD_MON) / _TD_MON
    intra_loss_frac = _rolling_count_true(intra < 0, _TD_MON) / _TD_MON
    return over_loss_frac - intra_loss_frac


def ocd_144_intraday_ret_pct_rank_expanding(open: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day mean intraday return."""
    r = _intraday_ret(open, close)
    mean21 = _rolling_mean(r, _TD_MON)
    return mean21.expanding(min_periods=5).rank(pct=True)


def ocd_145_overnight_ret_pct_rank_expanding(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day mean overnight return."""
    r = _overnight_ret(close, open)
    mean21 = _rolling_mean(r, _TD_MON)
    return mean21.expanding(min_periods=5).rank(pct=True)


# --- Group O (146-150): Composite session dynamics ---

def ocd_146_session_distress_composite_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Composite distress: avg of normalized intraday and overnight loss sums, 21d."""
    intra_loss = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    over_loss = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    intra_avg = _rolling_mean(intra_loss, _TD_YEAR).clip(upper=-_EPS)
    over_avg = _rolling_mean(over_loss, _TD_YEAR).clip(upper=-_EPS)
    return (_safe_div(intra_loss, intra_avg) + _safe_div(over_loss, over_avg)) / 2.0


def ocd_147_both_session_loss_vol_interaction_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of both-session-loss days weighted by volume ratio, 21d window."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    flagged = vol_norm.where((intra < 0) & (over < 0), 0.0)
    return _rolling_sum(flagged, _TD_MON)


def ocd_148_intraday_overnight_corr_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between intraday and overnight returns."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return intra.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).corr(over)


def ocd_149_intraday_overnight_corr_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between intraday and overnight returns."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return intra.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).corr(over)


def ocd_150_total_session_loss_score_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of absolute intraday + overnight losses normalized by 252d avg, 63d window."""
    intra_loss = _intraday_ret(open, close).clip(upper=0.0).abs()
    over_loss = _overnight_ret(close, open).clip(upper=0.0).abs()
    combined = intra_loss + over_loss
    score63 = _rolling_sum(combined, _TD_QTR)
    avg252 = _rolling_mean(score63, _TD_YEAR)
    return _safe_div(score63, avg252 + _EPS)


# ── Registry ──────────────────────────────────────────────────────────────────

OPEN_CLOSE_DYNAMICS_REGISTRY_076_150 = {
    "ocd_076_cum_intraday_ret_21d": {"inputs": ["open", "close"], "func": ocd_076_cum_intraday_ret_21d},
    "ocd_077_cum_overnight_ret_21d": {"inputs": ["close", "open"], "func": ocd_077_cum_overnight_ret_21d},
    "ocd_078_cum_intraday_ret_63d": {"inputs": ["open", "close"], "func": ocd_078_cum_intraday_ret_63d},
    "ocd_079_cum_overnight_ret_63d": {"inputs": ["close", "open"], "func": ocd_079_cum_overnight_ret_63d},
    "ocd_080_cum_intraday_ret_252d": {"inputs": ["open", "close"], "func": ocd_080_cum_intraday_ret_252d},
    "ocd_081_cum_overnight_ret_252d": {"inputs": ["close", "open"], "func": ocd_081_cum_overnight_ret_252d},
    "ocd_082_intraday_minus_overnight_cum_21d": {"inputs": ["close", "open"], "func": ocd_082_intraday_minus_overnight_cum_21d},
    "ocd_083_intraday_minus_overnight_cum_63d": {"inputs": ["close", "open"], "func": ocd_083_intraday_minus_overnight_cum_63d},
    "ocd_084_overnight_dominates_loss_21d": {"inputs": ["close", "open"], "func": ocd_084_overnight_dominates_loss_21d},
    "ocd_085_intraday_dominates_loss_21d": {"inputs": ["close", "open"], "func": ocd_085_intraday_dominates_loss_21d},
    "ocd_086_intraday_ret_zscore_252d": {"inputs": ["open", "close"], "func": ocd_086_intraday_ret_zscore_252d},
    "ocd_087_overnight_ret_zscore_252d": {"inputs": ["close", "open"], "func": ocd_087_overnight_ret_zscore_252d},
    "ocd_088_intraday_ret_pct_rank_252d": {"inputs": ["open", "close"], "func": ocd_088_intraday_ret_pct_rank_252d},
    "ocd_089_overnight_ret_pct_rank_252d": {"inputs": ["close", "open"], "func": ocd_089_overnight_ret_pct_rank_252d},
    "ocd_090_intraday_mean_21d_zscore_252d": {"inputs": ["open", "close"], "func": ocd_090_intraday_mean_21d_zscore_252d},
    "ocd_091_overnight_mean_21d_zscore_252d": {"inputs": ["close", "open"], "func": ocd_091_overnight_mean_21d_zscore_252d},
    "ocd_092_intraday_vol_zscore_252d": {"inputs": ["open", "close"], "func": ocd_092_intraday_vol_zscore_252d},
    "ocd_093_overnight_vol_zscore_252d": {"inputs": ["close", "open"], "func": ocd_093_overnight_vol_zscore_252d},
    "ocd_094_session_ratio_zscore_252d": {"inputs": ["close", "open"], "func": ocd_094_session_ratio_zscore_252d},
    "ocd_095_intraday_expanding_pct_rank": {"inputs": ["open", "close"], "func": ocd_095_intraday_expanding_pct_rank},
    "ocd_096_vol_weighted_intraday_ret_21d": {"inputs": ["open", "close", "volume"], "func": ocd_096_vol_weighted_intraday_ret_21d},
    "ocd_097_vol_weighted_overnight_ret_21d": {"inputs": ["close", "open", "volume"], "func": ocd_097_vol_weighted_overnight_ret_21d},
    "ocd_098_vol_weighted_intraday_ret_63d": {"inputs": ["open", "close", "volume"], "func": ocd_098_vol_weighted_intraday_ret_63d},
    "ocd_099_vol_weighted_overnight_ret_63d": {"inputs": ["close", "open", "volume"], "func": ocd_099_vol_weighted_overnight_ret_63d},
    "ocd_100_high_vol_intraday_loss_mean_21d": {"inputs": ["open", "close", "volume"], "func": ocd_100_high_vol_intraday_loss_mean_21d},
    "ocd_101_high_vol_overnight_loss_mean_21d": {"inputs": ["close", "open", "volume"], "func": ocd_101_high_vol_overnight_loss_mean_21d},
    "ocd_102_intraday_loss_vol_ratio_21d": {"inputs": ["open", "close", "volume"], "func": ocd_102_intraday_loss_vol_ratio_21d},
    "ocd_103_overnight_loss_vol_ratio_21d": {"inputs": ["close", "open", "volume"], "func": ocd_103_overnight_loss_vol_ratio_21d},
    "ocd_104_vol_on_intraday_loss_days_sum_21d": {"inputs": ["open", "close", "volume"], "func": ocd_104_vol_on_intraday_loss_days_sum_21d},
    "ocd_105_vol_on_both_sessions_loss_days_21d": {"inputs": ["close", "open", "volume"], "func": ocd_105_vol_on_both_sessions_loss_days_21d},
    "ocd_106_intraday_giveback_count_21d": {"inputs": ["close", "open"], "func": ocd_106_intraday_giveback_count_21d},
    "ocd_107_intraday_giveback_count_63d": {"inputs": ["close", "open"], "func": ocd_107_intraday_giveback_count_63d},
    "ocd_108_intraday_giveback_fraction_21d": {"inputs": ["close", "open"], "func": ocd_108_intraday_giveback_fraction_21d},
    "ocd_109_avg_giveback_magnitude_21d": {"inputs": ["close", "open"], "func": ocd_109_avg_giveback_magnitude_21d},
    "ocd_110_full_giveback_flag": {"inputs": ["close", "open"], "func": ocd_110_full_giveback_flag},
    "ocd_111_full_giveback_count_21d": {"inputs": ["close", "open"], "func": ocd_111_full_giveback_count_21d},
    "ocd_112_full_giveback_count_63d": {"inputs": ["close", "open"], "func": ocd_112_full_giveback_count_63d},
    "ocd_113_partial_giveback_flag": {"inputs": ["close", "open"], "func": ocd_113_partial_giveback_flag},
    "ocd_114_overnight_gain_captured_fraction_21d": {"inputs": ["close", "open"], "func": ocd_114_overnight_gain_captured_fraction_21d},
    "ocd_115_consec_full_giveback_days": {"inputs": ["close", "open"], "func": ocd_115_consec_full_giveback_days},
    "ocd_116_overnight_loss_recovered_intraday_flag": {"inputs": ["close", "open"], "func": ocd_116_overnight_loss_recovered_intraday_flag},
    "ocd_117_overnight_loss_recovered_count_21d": {"inputs": ["close", "open"], "func": ocd_117_overnight_loss_recovered_count_21d},
    "ocd_118_overnight_loss_recovered_fraction_21d": {"inputs": ["close", "open"], "func": ocd_118_overnight_loss_recovered_fraction_21d},
    "ocd_119_avg_intraday_recovery_magnitude_21d": {"inputs": ["close", "open"], "func": ocd_119_avg_intraday_recovery_magnitude_21d},
    "ocd_120_full_recovery_flag": {"inputs": ["close", "open"], "func": ocd_120_full_recovery_flag},
    "ocd_121_full_recovery_count_21d": {"inputs": ["close", "open"], "func": ocd_121_full_recovery_count_21d},
    "ocd_122_full_recovery_count_63d": {"inputs": ["close", "open"], "func": ocd_122_full_recovery_count_63d},
    "ocd_123_recovery_vs_giveback_ratio_21d": {"inputs": ["close", "open"], "func": ocd_123_recovery_vs_giveback_ratio_21d},
    "ocd_124_consec_no_intraday_recovery": {"inputs": ["close", "open"], "func": ocd_124_consec_no_intraday_recovery},
    "ocd_125_overnight_loss_intraday_amplify_count_21d": {"inputs": ["close", "open"], "func": ocd_125_overnight_loss_intraday_amplify_count_21d},
    "ocd_126_intraday_ret_rolling_min_21d": {"inputs": ["open", "close"], "func": ocd_126_intraday_ret_rolling_min_21d},
    "ocd_127_intraday_ret_rolling_min_63d": {"inputs": ["open", "close"], "func": ocd_127_intraday_ret_rolling_min_63d},
    "ocd_128_overnight_ret_rolling_min_21d": {"inputs": ["close", "open"], "func": ocd_128_overnight_ret_rolling_min_21d},
    "ocd_129_overnight_ret_rolling_min_63d": {"inputs": ["close", "open"], "func": ocd_129_overnight_ret_rolling_min_63d},
    "ocd_130_intraday_ret_rolling_max_21d": {"inputs": ["open", "close"], "func": ocd_130_intraday_ret_rolling_max_21d},
    "ocd_131_overnight_ret_rolling_max_21d": {"inputs": ["close", "open"], "func": ocd_131_overnight_ret_rolling_max_21d},
    "ocd_132_intraday_worst_vs_mean_21d": {"inputs": ["open", "close"], "func": ocd_132_intraday_worst_vs_mean_21d},
    "ocd_133_overnight_worst_vs_mean_21d": {"inputs": ["close", "open"], "func": ocd_133_overnight_worst_vs_mean_21d},
    "ocd_134_intraday_ret_expanding_min": {"inputs": ["open", "close"], "func": ocd_134_intraday_ret_expanding_min},
    "ocd_135_overnight_ret_expanding_min": {"inputs": ["close", "open"], "func": ocd_135_overnight_ret_expanding_min},
    "ocd_136_intraday_ret_when_below_sma50_mean_21d": {"inputs": ["open", "close"], "func": ocd_136_intraday_ret_when_below_sma50_mean_21d},
    "ocd_137_overnight_ret_when_below_sma50_mean_21d": {"inputs": ["close", "open"], "func": ocd_137_overnight_ret_when_below_sma50_mean_21d},
    "ocd_138_intraday_loss_at_52wk_low_flag": {"inputs": ["open", "close"], "func": ocd_138_intraday_loss_at_52wk_low_flag},
    "ocd_139_intraday_loss_at_52wk_low_count_63d": {"inputs": ["open", "close"], "func": ocd_139_intraday_loss_at_52wk_low_count_63d},
    "ocd_140_overnight_loss_at_52wk_low_count_63d": {"inputs": ["close", "open"], "func": ocd_140_overnight_loss_at_52wk_low_count_63d},
    "ocd_141_intraday_ret_below_sma200_mean_63d": {"inputs": ["open", "close"], "func": ocd_141_intraday_ret_below_sma200_mean_63d},
    "ocd_142_overnight_ret_below_sma200_mean_63d": {"inputs": ["close", "open"], "func": ocd_142_overnight_ret_below_sma200_mean_63d},
    "ocd_143_session_loss_asymmetry_21d": {"inputs": ["close", "open"], "func": ocd_143_session_loss_asymmetry_21d},
    "ocd_144_intraday_ret_pct_rank_expanding": {"inputs": ["open", "close"], "func": ocd_144_intraday_ret_pct_rank_expanding},
    "ocd_145_overnight_ret_pct_rank_expanding": {"inputs": ["close", "open"], "func": ocd_145_overnight_ret_pct_rank_expanding},
    "ocd_146_session_distress_composite_21d": {"inputs": ["close", "open"], "func": ocd_146_session_distress_composite_21d},
    "ocd_147_both_session_loss_vol_interaction_21d": {"inputs": ["close", "open", "volume"], "func": ocd_147_both_session_loss_vol_interaction_21d},
    "ocd_148_intraday_overnight_corr_21d": {"inputs": ["close", "open"], "func": ocd_148_intraday_overnight_corr_21d},
    "ocd_149_intraday_overnight_corr_63d": {"inputs": ["close", "open"], "func": ocd_149_intraday_overnight_corr_63d},
    "ocd_150_total_session_loss_score_63d": {"inputs": ["close", "open"], "func": ocd_150_total_session_loss_score_63d},
}
