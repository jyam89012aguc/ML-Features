"""
19_volume_trend — Base Features 076-200
Domain: directional drift/slope/trend of volume over multi-week and multi-month windows
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
    """Rolling mean with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling std with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling min with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Rolling max with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponential weighted mean."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Log of series clipped at EPS."""
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope of s over w periods."""
    def _slope(x):
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
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


def _linslope_rsq(s: pd.Series, w: int) -> pd.Series:
    """Rolling R-squared of OLS line fit of s over w periods."""
    def _rsq(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        ss_tot = ((x - x_m) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        slope = num / den
        intercept = x_m - slope * xi_m
        resid = x - (slope * xi + intercept)
        ss_res = (resid ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_rsq, raw=False)


# ── Feature functions 076-150 ──────────────────────────────────────────────────

# --- Group G (076-087): Volume trend z-scores and percentile ranks ---

def vtr_076_vol_slope_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day raw-volume slope relative to trailing 252-day distribution."""
    slope = _linslope(volume, _TD_MON)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    return _safe_div(slope - m, s)


def vtr_077_vol_slope_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day raw-volume slope relative to trailing 252-day distribution."""
    slope = _linslope(volume, _TD_QTR)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    return _safe_div(slope - m, s)


def vtr_078_logvol_slope_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day log-volume slope relative to trailing 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_QTR)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    return _safe_div(slope - m, s)


def vtr_079_logvol_slope_126d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 126-day log-volume slope relative to trailing 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_HALF)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    return _safe_div(slope - m, s)


def vtr_080_vol_sma21_vs_sma63_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of SMA21/SMA63 volume ratio in trailing 252-day distribution."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_081_vol_ema21_vs_ema63_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of EMA21/EMA63 volume ratio in trailing 252-day distribution."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_082_vol_slope_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day raw-volume slope in trailing 252-day distribution."""
    slope = _linslope(volume, _TD_MON)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_083_vol_slope_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day raw-volume slope in trailing 252-day distribution."""
    slope = _linslope(volume, _TD_QTR)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_084_vol_rising_days_frac_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day rising-volume-days fraction vs 252-day distribution."""
    frac = (volume > volume.shift(1)).astype(float)
    frac21 = _rolling_mean(frac, _TD_MON)
    m = _rolling_mean(frac21, _TD_YEAR)
    s = _rolling_std(frac21, _TD_YEAR)
    return _safe_div(frac21 - m, s)


def vtr_085_vol_ema_crossover_score_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of EMA crossover score vs trailing 252-day distribution."""
    s1 = (_ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)).astype(float)
    s2 = (_ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_QTR)).astype(float)
    s3 = (_ewm_mean(volume, _TD_QTR) > _ewm_mean(volume, _TD_YEAR)).astype(float)
    score = s1 + s2 + s3
    m = _rolling_mean(score, _TD_YEAR)
    s = _rolling_std(score, _TD_YEAR)
    return _safe_div(score - m, s)


def vtr_086_vol_slope_252d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding-history percentile rank of 252-day volume slope."""
    slope = _linslope(volume, _TD_YEAR)
    return slope.expanding(min_periods=5).rank(pct=True)


def vtr_087_vol_rsq_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day volume R-squared in trailing 252-day distribution."""
    rsq = _linslope_rsq(volume, _TD_QTR)
    return rsq.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group H (088-099): Cross-window slope comparisons and regime indicators ---

def vtr_088_vol_slope_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day normalized volume slope (near vs long trend)."""
    s21 = _safe_div(_linslope(volume, _TD_MON), _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    s252 = _safe_div(_linslope(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))
    return _safe_div(s21, s252.replace(0, np.nan))


def vtr_089_vol_slope_63d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day to 252-day normalized volume slope."""
    s63 = _safe_div(_linslope(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    s252 = _safe_div(_linslope(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))
    return _safe_div(s63, s252.replace(0, np.nan))


def vtr_090_vol_slope_sign_agreement_flag(volume: pd.Series) -> pd.Series:
    """Flag: 21d, 63d, and 252d volume slopes all share the same sign."""
    s21 = np.sign(_linslope(volume, _TD_MON))
    s63 = np.sign(_linslope(volume, _TD_QTR))
    s252 = np.sign(_linslope(volume, _TD_YEAR))
    return ((s21 == s63) & (s63 == s252)).astype(float)


def vtr_091_vol_slope_all_negative_flag(volume: pd.Series) -> pd.Series:
    """Flag: all three volume slopes (21d, 63d, 252d) are simultaneously negative."""
    s21 = _linslope(volume, _TD_MON)
    s63 = _linslope(volume, _TD_QTR)
    s252 = _linslope(volume, _TD_YEAR)
    return ((s21 < 0) & (s63 < 0) & (s252 < 0)).astype(float)


def vtr_092_vol_slope_all_positive_flag(volume: pd.Series) -> pd.Series:
    """Flag: all three volume slopes (21d, 63d, 252d) are simultaneously positive."""
    s21 = _linslope(volume, _TD_MON)
    s63 = _linslope(volume, _TD_QTR)
    s252 = _linslope(volume, _TD_YEAR)
    return ((s21 > 0) & (s63 > 0) & (s252 > 0)).astype(float)


def vtr_093_vol_negative_slope_count(volume: pd.Series) -> pd.Series:
    """Count of negative slopes among 21d, 63d, 126d, 252d (0-4 scale)."""
    s21 = (_linslope(volume, _TD_MON) < 0).astype(float)
    s63 = (_linslope(volume, _TD_QTR) < 0).astype(float)
    s126 = (_linslope(volume, _TD_HALF) < 0).astype(float)
    s252 = (_linslope(volume, _TD_YEAR) < 0).astype(float)
    return s21 + s63 + s126 + s252


def vtr_094_logvol_slope_21d_vs_63d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day log-volume slope (acceleration of trend)."""
    s21 = _linslope(_log_safe(volume), _TD_MON)
    s63 = _linslope(_log_safe(volume), _TD_QTR)
    return _safe_div(s21, s63.replace(0, np.nan))


def vtr_095_vol_ema_bearish_alignment_flag(volume: pd.Series) -> pd.Series:
    """Flag: EMA5 < EMA21 < EMA63 < EMA252 (full bearish EMA stack on volume)."""
    e5 = _ewm_mean(volume, _TD_WEEK)
    e21 = _ewm_mean(volume, _TD_MON)
    e63 = _ewm_mean(volume, _TD_QTR)
    e252 = _ewm_mean(volume, _TD_YEAR)
    return ((e5 < e21) & (e21 < e63) & (e63 < e252)).astype(float)


def vtr_096_vol_ema_bullish_alignment_flag(volume: pd.Series) -> pd.Series:
    """Flag: EMA5 > EMA21 > EMA63 > EMA252 (full bullish EMA stack on volume)."""
    e5 = _ewm_mean(volume, _TD_WEEK)
    e21 = _ewm_mean(volume, _TD_MON)
    e63 = _ewm_mean(volume, _TD_QTR)
    e252 = _ewm_mean(volume, _TD_YEAR)
    return ((e5 > e21) & (e21 > e63) & (e63 > e252)).astype(float)


def vtr_097_vol_slope_21d_slope_63d_diff_norm(volume: pd.Series) -> pd.Series:
    """Difference of normalized 21d and 63d volume slopes (short-minus-long trend)."""
    s21 = _safe_div(_linslope(volume, _TD_MON), _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    s63 = _safe_div(_linslope(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    return s21 - s63


def vtr_098_vol_sma_dispersion_21_63_252(volume: pd.Series) -> pd.Series:
    """Dispersion of SMA21, SMA63, SMA252 volumes: std / mean of the three values."""
    s21 = _rolling_mean(volume, _TD_MON)
    s63 = _rolling_mean(volume, _TD_QTR)
    s252 = _rolling_mean(volume, _TD_YEAR)
    avg = (s21 + s63 + s252) / 3.0
    spread = ((s21 - avg) ** 2 + (s63 - avg) ** 2 + (s252 - avg) ** 2) / 3.0
    return _safe_div(spread ** 0.5, avg.clip(lower=_EPS))


def vtr_099_vol_trend_direction_composite(volume: pd.Series) -> pd.Series:
    """Composite trend direction: avg of three signed R-squares (21d, 63d, 252d)."""
    def _signed_rsq(w):
        rsq = _linslope_rsq(volume, w)
        sgn = np.sign(_linslope(volume, w))
        return rsq * sgn
    return (_signed_rsq(_TD_MON) + _signed_rsq(_TD_QTR) + _signed_rsq(_TD_YEAR)) / 3.0


# --- Group I (100-111): Volume trend vs price direction interactions ---

def vtr_100_vol_slope_21d_on_down_price_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day OLS slope of volume measured only on days when price declines."""
    ret = close.pct_change(1)
    vol_down = volume.where(ret < 0, np.nan)
    return _linslope(vol_down.ffill(), _TD_MON)


def vtr_101_vol_slope_21d_on_up_price_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day OLS slope of volume measured only on days when price rises."""
    ret = close.pct_change(1)
    vol_up = volume.where(ret > 0, np.nan)
    return _linslope(vol_up.ffill(), _TD_MON)


def vtr_102_vol_trend_down_vs_up_days_slope_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day volume slope on down-days to slope on up-days."""
    ret = close.pct_change(1)
    vd = _linslope(volume.where(ret < 0, np.nan).ffill(), _TD_MON)
    vu = _linslope(volume.where(ret > 0, np.nan).ffill(), _TD_MON)
    return _safe_div(vd, vu.replace(0, np.nan))


def vtr_103_vol_rising_on_down_price_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of down-price days where volume also rose vs prior day, trailing 21d."""
    ret = close.pct_change(1)
    vol_rose = (volume > volume.shift(1)).astype(float)
    down_days = (ret < 0).astype(float)
    both = vol_rose * down_days
    dn_cnt = _rolling_sum(down_days, _TD_MON).clip(lower=1)
    return _safe_div(_rolling_sum(both, _TD_MON), dn_cnt)


def vtr_104_vol_rising_on_down_price_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of down-price days where volume also rose vs prior day, trailing 63d."""
    ret = close.pct_change(1)
    vol_rose = (volume > volume.shift(1)).astype(float)
    down_days = (ret < 0).astype(float)
    both = vol_rose * down_days
    dn_cnt = _rolling_sum(down_days, _TD_QTR).clip(lower=1)
    return _safe_div(_rolling_sum(both, _TD_QTR), dn_cnt)


def vtr_105_vol_trend_price_divergence_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Divergence: sign of 21d volume slope minus sign of 21d price slope."""
    vs = np.sign(_linslope(volume, _TD_MON))
    ps = np.sign(_linslope(close, _TD_MON))
    return vs - ps


def vtr_106_vol_trend_price_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Divergence: sign of 63d volume slope minus sign of 63d price slope."""
    vs = np.sign(_linslope(volume, _TD_QTR))
    ps = np.sign(_linslope(close, _TD_QTR))
    return vs - ps


def vtr_107_vol_up_trend_price_down_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: volume trending up (positive 21d slope) while price trending down."""
    vs = _linslope(volume, _TD_MON)
    ps = _linslope(close, _TD_MON)
    return ((vs > 0) & (ps < 0)).astype(float)


def vtr_108_vol_down_trend_price_down_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: both volume and price trending down over 21 days (quiet decline)."""
    vs = _linslope(volume, _TD_MON)
    ps = _linslope(close, _TD_MON)
    return ((vs < 0) & (ps < 0)).astype(float)


def vtr_109_vol_up_trend_price_down_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: volume trending up (positive 63d slope) while price trending down."""
    vs = _linslope(volume, _TD_QTR)
    ps = _linslope(close, _TD_QTR)
    return ((vs > 0) & (ps < 0)).astype(float)


def vtr_110_logvol_slope_21d_times_price_slope_sign(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of log-vol 21d slope sign and price 21d slope sign (+1=aligned, -1=diverged)."""
    vs = np.sign(_linslope(_log_safe(volume), _TD_MON))
    ps = np.sign(_linslope(close, _TD_MON))
    return vs * ps


def vtr_111_vol_cumulative_trend_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative volume change on down-price days only, 21-day window."""
    ret = close.pct_change(1)
    vol_chg = volume.diff(1)
    vol_down = vol_chg.where(ret < 0, 0.0)
    return _rolling_sum(vol_down, _TD_MON)


# --- Group J (112-123): Log-volume net change and momentum ---

def vtr_112_logvol_21d_change(volume: pd.Series) -> pd.Series:
    """21-day log-volume change (log(V_t) - log(V_{t-21}))."""
    lv = _log_safe(volume)
    return lv - lv.shift(_TD_MON)


def vtr_113_logvol_63d_change(volume: pd.Series) -> pd.Series:
    """63-day log-volume change."""
    lv = _log_safe(volume)
    return lv - lv.shift(_TD_QTR)


def vtr_114_logvol_126d_change(volume: pd.Series) -> pd.Series:
    """126-day log-volume change."""
    lv = _log_safe(volume)
    return lv - lv.shift(_TD_HALF)


def vtr_115_logvol_252d_change(volume: pd.Series) -> pd.Series:
    """252-day log-volume change (annual drift in log-volume)."""
    lv = _log_safe(volume)
    return lv - lv.shift(_TD_YEAR)


def vtr_116_logvol_21d_change_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day log-volume change within trailing 252-day distribution."""
    chg = _log_safe(volume) - _log_safe(volume).shift(_TD_MON)
    return chg.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_117_logvol_63d_change_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day log-volume change vs trailing 252-day distribution."""
    chg = _log_safe(volume) - _log_safe(volume).shift(_TD_QTR)
    m = _rolling_mean(chg, _TD_YEAR)
    s = _rolling_std(chg, _TD_YEAR)
    return _safe_div(chg - m, s)


def vtr_118_vol_21d_return(volume: pd.Series) -> pd.Series:
    """Simple 21-day percent change in volume."""
    return volume.pct_change(_TD_MON)


def vtr_119_vol_63d_return(volume: pd.Series) -> pd.Series:
    """Simple 63-day percent change in volume."""
    return volume.pct_change(_TD_QTR)


def vtr_120_vol_126d_return(volume: pd.Series) -> pd.Series:
    """Simple 126-day percent change in volume."""
    return volume.pct_change(_TD_HALF)


def vtr_121_vol_252d_return(volume: pd.Series) -> pd.Series:
    """Simple 252-day percent change in volume."""
    return volume.pct_change(_TD_YEAR)


def vtr_122_vol_21d_return_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day volume return in trailing 252-day distribution."""
    ret = volume.pct_change(_TD_MON)
    return ret.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_123_vol_63d_return_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day volume return vs trailing 252-day distribution."""
    ret = volume.pct_change(_TD_QTR)
    m = _rolling_mean(ret, _TD_YEAR)
    s = _rolling_std(ret, _TD_YEAR)
    return _safe_div(ret - m, s)


# --- Group K (124-135): Volume EMA slope and acceleration ---

def vtr_124_vol_ema21_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day EMA of volume over trailing 21 days."""
    return _linslope(_ewm_mean(volume, _TD_MON), _TD_MON)


def vtr_125_vol_ema63_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day EMA of volume over trailing 21 days."""
    return _linslope(_ewm_mean(volume, _TD_QTR), _TD_MON)


def vtr_126_vol_ema21_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day EMA of volume over trailing 63 days."""
    return _linslope(_ewm_mean(volume, _TD_MON), _TD_QTR)


def vtr_127_vol_ema63_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day EMA of volume over trailing 63 days."""
    return _linslope(_ewm_mean(volume, _TD_QTR), _TD_QTR)


def vtr_128_vol_ema21_slope_sign_21d(volume: pd.Series) -> pd.Series:
    """Sign of 21-day slope of the 21-day EMA volume."""
    return np.sign(_linslope(_ewm_mean(volume, _TD_MON), _TD_MON))


def vtr_129_vol_ema63_slope_sign_21d(volume: pd.Series) -> pd.Series:
    """Sign of 21-day slope of the 63-day EMA volume."""
    return np.sign(_linslope(_ewm_mean(volume, _TD_QTR), _TD_MON))


def vtr_130_vol_ema21_5d_change(volume: pd.Series) -> pd.Series:
    """5-day change in the 21-day EMA of volume."""
    ema21 = _ewm_mean(volume, _TD_MON)
    return ema21 - ema21.shift(_TD_WEEK)


def vtr_131_vol_ema63_21d_change(volume: pd.Series) -> pd.Series:
    """21-day change in the 63-day EMA of volume."""
    ema63 = _ewm_mean(volume, _TD_QTR)
    return ema63 - ema63.shift(_TD_MON)


def vtr_132_vol_ema21_5d_change_norm(volume: pd.Series) -> pd.Series:
    """Normalized 5-day change in EMA21 volume: (EMA21 - EMA21_5ago) / EMA21_5ago."""
    ema21 = _ewm_mean(volume, _TD_MON)
    return _safe_div(ema21 - ema21.shift(_TD_WEEK), ema21.shift(_TD_WEEK).clip(lower=_EPS))


def vtr_133_vol_ema63_21d_change_norm(volume: pd.Series) -> pd.Series:
    """Normalized 21-day change in EMA63 volume."""
    ema63 = _ewm_mean(volume, _TD_QTR)
    return _safe_div(ema63 - ema63.shift(_TD_MON), ema63.shift(_TD_MON).clip(lower=_EPS))


def vtr_134_vol_ema21_declining_flag(volume: pd.Series) -> pd.Series:
    """Flag: EMA21 volume is lower today than 5 days ago (short-term EMA declining)."""
    ema21 = _ewm_mean(volume, _TD_MON)
    return (ema21 < ema21.shift(_TD_WEEK)).astype(float)


def vtr_135_vol_ema63_declining_flag(volume: pd.Series) -> pd.Series:
    """Flag: EMA63 volume is lower today than 21 days ago (medium EMA declining)."""
    ema63 = _ewm_mean(volume, _TD_QTR)
    return (ema63 < ema63.shift(_TD_MON)).astype(float)


# --- Group L (136-150): Advanced trend composites and long-horizon drift ---

def vtr_136_vol_trend_score_composite_4window(volume: pd.Series) -> pd.Series:
    """Sum of normalized slopes over 21d, 63d, 126d, 252d windows (direction composite)."""
    def _norm_slope(w):
        sl = _linslope(volume, w)
        avg = _rolling_mean(volume, w).clip(lower=_EPS)
        return _safe_div(sl, avg)
    return _norm_slope(_TD_MON) + _norm_slope(_TD_QTR) + _norm_slope(_TD_HALF) + _norm_slope(_TD_YEAR)


def vtr_137_logvol_slope_composite_4window(volume: pd.Series) -> pd.Series:
    """Sum of log-volume slopes over 21d, 63d, 126d, 252d windows."""
    lv = _log_safe(volume)
    return (_linslope(lv, _TD_MON) + _linslope(lv, _TD_QTR)
            + _linslope(lv, _TD_HALF) + _linslope(lv, _TD_YEAR))


def vtr_138_vol_trend_regime_score(volume: pd.Series) -> pd.Series:
    """Regime score: count of windows (21, 63, 126, 252) with positive volume slope."""
    s = [(_linslope(volume, w) > 0).astype(float)
         for w in [_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR]]
    return s[0] + s[1] + s[2] + s[3]


def vtr_139_vol_rising_days_frac_126d(volume: pd.Series) -> pd.Series:
    """Fraction of days with rising volume in trailing 126 days."""
    rising = (volume > volume.shift(1)).astype(float)
    return _rolling_mean(rising, _TD_HALF)


def vtr_140_vol_net_drift_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day volume net drift vs trailing 252-day distribution."""
    drift = _safe_div(volume - volume.shift(_TD_MON), volume.shift(_TD_MON).clip(lower=_EPS))
    m = _rolling_mean(drift, _TD_YEAR)
    s = _rolling_std(drift, _TD_YEAR)
    return _safe_div(drift - m, s)


def vtr_141_vol_net_drift_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day volume net drift vs trailing 252-day distribution."""
    drift = _safe_div(volume - volume.shift(_TD_QTR), volume.shift(_TD_QTR).clip(lower=_EPS))
    m = _rolling_mean(drift, _TD_YEAR)
    s = _rolling_std(drift, _TD_YEAR)
    return _safe_div(drift - m, s)


def vtr_142_vol_rising_weeks_count_63d(volume: pd.Series) -> pd.Series:
    """Count of 5-day periods with rising volume within trailing 63 days."""
    weekly_ret = volume.pct_change(_TD_WEEK)
    rising = (weekly_ret > 0).astype(float)
    return _rolling_sum(rising, _TD_QTR)


def vtr_143_vol_rising_weeks_count_252d(volume: pd.Series) -> pd.Series:
    """Count of 5-day periods with rising volume within trailing 252 days."""
    weekly_ret = volume.pct_change(_TD_WEEK)
    rising = (weekly_ret > 0).astype(float)
    return _rolling_sum(rising, _TD_YEAR)


def vtr_144_vol_logslope_21d_expanding_zscore(volume: pd.Series) -> pd.Series:
    """Expanding-history z-score of 21-day log-volume slope."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    m = slope.expanding(min_periods=5).mean()
    s = slope.expanding(min_periods=5).std()
    return _safe_div(slope - m, s)


def vtr_145_vol_logslope_63d_expanding_zscore(volume: pd.Series) -> pd.Series:
    """Expanding-history z-score of 63-day log-volume slope."""
    slope = _linslope(_log_safe(volume), _TD_QTR)
    m = slope.expanding(min_periods=5).mean()
    s = slope.expanding(min_periods=5).std()
    return _safe_div(slope - m, s)


def vtr_146_vol_ema21_vs_ema252_ratio_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of EMA21/EMA252 volume ratio vs trailing 252-day distribution."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_YEAR))
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def vtr_147_vol_slope_21d_negative_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days with negative 21-day volume slope over trailing 63 days."""
    slope = _linslope(volume, _TD_MON)
    neg = (slope < 0).astype(float)
    return _rolling_sum(neg, _TD_QTR)


def vtr_148_vol_slope_21d_negative_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days with negative 21-day volume slope over trailing 252 days."""
    slope = _linslope(volume, _TD_MON)
    neg = (slope < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR)


def vtr_149_vol_ema21_slope_21d_norm(volume: pd.Series) -> pd.Series:
    """Normalized 21-day slope of EMA21 volume: slope / EMA21_mean."""
    ema21 = _ewm_mean(volume, _TD_MON)
    slope = _linslope(ema21, _TD_MON)
    avg = _rolling_mean(ema21, _TD_MON).clip(lower=_EPS)
    return _safe_div(slope, avg)


def vtr_150_vol_trend_strength_index(volume: pd.Series) -> pd.Series:
    """Trend-strength index: signed R-squared (63d log-vol) times consistency (63d)."""
    rsq = _linslope_rsq(_log_safe(volume), _TD_QTR)
    sgn = np.sign(_linslope(_log_safe(volume), _TD_QTR))
    sign_chg = np.sign(volume - volume.shift(1))
    total_sign = sign_chg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    consistency = total_sign.abs() / _TD_QTR
    return rsq * sgn * consistency


# --- Group M (176-200): Dollar-volume, OHLC-weighted, and cross-signal features ---

def vtr_176_vol_dollar_volume_slope_21d_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of dollar-volume (close*volume) over 21d, normalized by 21d mean dollar-vol."""
    dv = close * volume
    slope = _linslope(dv, _TD_MON)
    avg = _rolling_mean(dv, _TD_MON)
    return _safe_div(slope, avg)


def vtr_177_vol_dollar_volume_slope_63d_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of dollar-volume (close*volume) over 63d, normalized by 63d mean."""
    dv = close * volume
    slope = _linslope(dv, _TD_QTR)
    avg = _rolling_mean(dv, _TD_QTR)
    return _safe_div(slope, avg)


def vtr_178_vol_intraday_range_vol_slope_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of (high-low)*volume over 21d, normalized by its 21d mean."""
    rv = (high - low) * volume
    slope = _linslope(rv, _TD_MON)
    avg = _rolling_mean(rv, _TD_MON)
    return _safe_div(slope, avg)


def vtr_179_vol_high_low_weighted_vol_sma21_vs_sma63(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """SMA21/SMA63 ratio of range-weighted volume (high-low)*volume."""
    rv = (high - low) * volume
    return _safe_div(_rolling_mean(rv, _TD_MON), _rolling_mean(rv, _TD_QTR))


def vtr_180_vol_slope_126d_norm(volume: pd.Series) -> pd.Series:
    """OLS slope of raw volume over 126d, normalized by 126d mean."""
    slope = _linslope(volume, _TD_HALF)
    avg = _rolling_mean(volume, _TD_HALF)
    return _safe_div(slope, avg)


def vtr_181_logvol_slope_252d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 252-day log-vol slope within trailing 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_YEAR)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_182_vol_ema63_vs_ema126_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day EMA volume to 126-day EMA volume."""
    return _safe_div(_ewm_mean(volume, _TD_QTR), _ewm_mean(volume, _TD_HALF))


def vtr_183_vol_sma63_vs_sma126_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day SMA volume to 126-day SMA volume."""
    return _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_HALF))


def vtr_184_vol_slope_all_negative_flag_4window(volume: pd.Series) -> pd.Series:
    """Flag: all four volume slopes (10d, 21d, 63d, 126d) are simultaneously negative."""
    s10 = _linslope(volume, 10)
    s21 = _linslope(volume, _TD_MON)
    s63 = _linslope(volume, _TD_QTR)
    s126 = _linslope(volume, _TD_HALF)
    return ((s10 < 0) & (s21 < 0) & (s63 < 0) & (s126 < 0)).astype(float)


def vtr_185_vol_sma_crossover_score_4level(volume: pd.Series) -> pd.Series:
    """Count of aligned SMA order signals: SMA5>SMA21, SMA21>SMA63, SMA63>SMA126, SMA126>SMA252."""
    s5 = _rolling_mean(volume, _TD_WEEK)
    s21 = _rolling_mean(volume, _TD_MON)
    s63 = _rolling_mean(volume, _TD_QTR)
    s126 = _rolling_mean(volume, _TD_HALF)
    s252 = _rolling_mean(volume, _TD_YEAR)
    return ((s5 > s21).astype(float) + (s21 > s63).astype(float)
            + (s63 > s126).astype(float) + (s126 > s252).astype(float))


def vtr_186_vol_rising_days_frac_126d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 126-day rising-volume-day fraction vs trailing 252-day distribution."""
    rising = (volume > volume.shift(1)).astype(float)
    frac126 = _rolling_mean(rising, _TD_HALF)
    m = _rolling_mean(frac126, _TD_YEAR)
    s = _rolling_std(frac126, _TD_YEAR)
    return _safe_div(frac126 - m, s)


def vtr_187_vol_net_drift_252d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 252-day volume net drift vs trailing 252-day expanding distribution."""
    drift = _safe_div(volume - volume.shift(_TD_YEAR), volume.shift(_TD_YEAR).clip(lower=_EPS))
    m = drift.expanding(min_periods=5).mean()
    s = drift.expanding(min_periods=5).std()
    return _safe_div(drift - m, s)


def vtr_188_vol_ema63_slope_126d(volume: pd.Series) -> pd.Series:
    """OLS slope of the 63-day EMA of volume over trailing 126 days."""
    return _linslope(_ewm_mean(volume, _TD_QTR), _TD_HALF)


def vtr_189_vol_ema126_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of the 126-day EMA of volume over trailing 63 days."""
    return _linslope(_ewm_mean(volume, _TD_HALF), _TD_QTR)


def vtr_190_vol_logslope_10d_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of 10-day log-volume slope relative to trailing 63-day distribution."""
    slope = _linslope(_log_safe(volume), 10)
    m = _rolling_mean(slope, _TD_QTR)
    s = _rolling_std(slope, _TD_QTR)
    return _safe_div(slope - m, s)


def vtr_191_vol_price_down_vol_down_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of days where both price and volume declined, trailing 63 days."""
    ret = close.pct_change(1)
    vol_fell = (volume < volume.shift(1)).astype(float)
    price_fell = (ret < 0).astype(float)
    both = vol_fell * price_fell
    return _rolling_mean(both, _TD_QTR)


def vtr_192_vol_price_down_vol_up_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of days where price fell but volume rose, trailing 63 days."""
    ret = close.pct_change(1)
    vol_rose = (volume > volume.shift(1)).astype(float)
    price_fell = (ret < 0).astype(float)
    both = vol_rose * price_fell
    return _rolling_mean(both, _TD_QTR)


def vtr_193_vol_cumulative_down_day_vol_norm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on price-down days normalized by total volume over 63 days."""
    ret = close.pct_change(1)
    vol_down = volume.where(ret < 0, 0.0)
    return _safe_div(_rolling_sum(vol_down, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def vtr_194_vol_slope_252d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 252-day raw-volume slope in trailing 252-day distribution."""
    slope = _linslope(volume, _TD_YEAR)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_195_logvol_21d_change_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day log-volume change relative to trailing 63-day distribution."""
    chg = _log_safe(volume) - _log_safe(volume).shift(_TD_MON)
    m = _rolling_mean(chg, _TD_QTR)
    s = _rolling_std(chg, _TD_QTR)
    return _safe_div(chg - m, s)


def vtr_196_vol_ema21_above_ema126_flag(volume: pd.Series) -> pd.Series:
    """Flag: EMA21 volume > EMA126 volume (month trend above half-year baseline)."""
    return (_ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_HALF)).astype(float)


def vtr_197_vol_sma126_above_sma252_flag(volume: pd.Series) -> pd.Series:
    """Flag: SMA126 volume > SMA252 volume (half-year average above annual average)."""
    return (_rolling_mean(volume, _TD_HALF) > _rolling_mean(volume, _TD_YEAR)).astype(float)


def vtr_198_vol_ema_dispersion_4level(volume: pd.Series) -> pd.Series:
    """Dispersion of EMA5, EMA21, EMA63, EMA252 volumes: std / mean of the four values."""
    e5 = _ewm_mean(volume, _TD_WEEK)
    e21 = _ewm_mean(volume, _TD_MON)
    e63 = _ewm_mean(volume, _TD_QTR)
    e252 = _ewm_mean(volume, _TD_YEAR)
    avg = (e5 + e21 + e63 + e252) / 4.0
    spread = ((e5 - avg)**2 + (e21 - avg)**2 + (e63 - avg)**2 + (e252 - avg)**2) / 4.0
    return _safe_div(spread**0.5, avg.clip(lower=_EPS))


def vtr_199_vol_open_close_range_vol_slope_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of |close-open|*volume over 21d, normalized by its 21d mean."""
    oc_vol = (close - open).abs() * volume
    slope = _linslope(oc_vol, _TD_MON)
    avg = _rolling_mean(oc_vol, _TD_MON)
    return _safe_div(slope, avg)


def vtr_200_vol_trend_strength_index_4window(volume: pd.Series) -> pd.Series:
    """Average signed R-squared across 21d, 63d, 126d, 252d log-volume trends."""
    lv = _log_safe(volume)
    def _srq(w):
        rsq = _linslope_rsq(lv, w)
        sgn = np.sign(_linslope(lv, w))
        return rsq * sgn
    return (_srq(_TD_MON) + _srq(_TD_QTR) + _srq(_TD_HALF) + _srq(_TD_YEAR)) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_TREND_REGISTRY_076_150 = {
    "vtr_076_vol_slope_21d_zscore_252d": {"inputs": ["volume"], "func": vtr_076_vol_slope_21d_zscore_252d},
    "vtr_077_vol_slope_63d_zscore_252d": {"inputs": ["volume"], "func": vtr_077_vol_slope_63d_zscore_252d},
    "vtr_078_logvol_slope_63d_zscore_252d": {"inputs": ["volume"], "func": vtr_078_logvol_slope_63d_zscore_252d},
    "vtr_079_logvol_slope_126d_zscore_252d": {"inputs": ["volume"], "func": vtr_079_logvol_slope_126d_zscore_252d},
    "vtr_080_vol_sma21_vs_sma63_pct_rank_252d": {"inputs": ["volume"], "func": vtr_080_vol_sma21_vs_sma63_pct_rank_252d},
    "vtr_081_vol_ema21_vs_ema63_pct_rank_252d": {"inputs": ["volume"], "func": vtr_081_vol_ema21_vs_ema63_pct_rank_252d},
    "vtr_082_vol_slope_21d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_082_vol_slope_21d_pct_rank_252d},
    "vtr_083_vol_slope_63d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_083_vol_slope_63d_pct_rank_252d},
    "vtr_084_vol_rising_days_frac_21d_zscore_252d": {"inputs": ["volume"], "func": vtr_084_vol_rising_days_frac_21d_zscore_252d},
    "vtr_085_vol_ema_crossover_score_zscore_252d": {"inputs": ["volume"], "func": vtr_085_vol_ema_crossover_score_zscore_252d},
    "vtr_086_vol_slope_252d_expanding_rank": {"inputs": ["volume"], "func": vtr_086_vol_slope_252d_expanding_rank},
    "vtr_087_vol_rsq_63d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_087_vol_rsq_63d_pct_rank_252d},
    "vtr_088_vol_slope_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vtr_088_vol_slope_21d_vs_252d_ratio},
    "vtr_089_vol_slope_63d_vs_252d_ratio": {"inputs": ["volume"], "func": vtr_089_vol_slope_63d_vs_252d_ratio},
    "vtr_090_vol_slope_sign_agreement_flag": {"inputs": ["volume"], "func": vtr_090_vol_slope_sign_agreement_flag},
    "vtr_091_vol_slope_all_negative_flag": {"inputs": ["volume"], "func": vtr_091_vol_slope_all_negative_flag},
    "vtr_092_vol_slope_all_positive_flag": {"inputs": ["volume"], "func": vtr_092_vol_slope_all_positive_flag},
    "vtr_093_vol_negative_slope_count": {"inputs": ["volume"], "func": vtr_093_vol_negative_slope_count},
    "vtr_094_logvol_slope_21d_vs_63d_ratio": {"inputs": ["volume"], "func": vtr_094_logvol_slope_21d_vs_63d_ratio},
    "vtr_095_vol_ema_bearish_alignment_flag": {"inputs": ["volume"], "func": vtr_095_vol_ema_bearish_alignment_flag},
    "vtr_096_vol_ema_bullish_alignment_flag": {"inputs": ["volume"], "func": vtr_096_vol_ema_bullish_alignment_flag},
    "vtr_097_vol_slope_21d_slope_63d_diff_norm": {"inputs": ["volume"], "func": vtr_097_vol_slope_21d_slope_63d_diff_norm},
    "vtr_098_vol_sma_dispersion_21_63_252": {"inputs": ["volume"], "func": vtr_098_vol_sma_dispersion_21_63_252},
    "vtr_099_vol_trend_direction_composite": {"inputs": ["volume"], "func": vtr_099_vol_trend_direction_composite},
    "vtr_100_vol_slope_21d_on_down_price_days": {"inputs": ["close", "volume"], "func": vtr_100_vol_slope_21d_on_down_price_days},
    "vtr_101_vol_slope_21d_on_up_price_days": {"inputs": ["close", "volume"], "func": vtr_101_vol_slope_21d_on_up_price_days},
    "vtr_102_vol_trend_down_vs_up_days_slope_ratio": {"inputs": ["close", "volume"], "func": vtr_102_vol_trend_down_vs_up_days_slope_ratio},
    "vtr_103_vol_rising_on_down_price_frac_21d": {"inputs": ["close", "volume"], "func": vtr_103_vol_rising_on_down_price_frac_21d},
    "vtr_104_vol_rising_on_down_price_frac_63d": {"inputs": ["close", "volume"], "func": vtr_104_vol_rising_on_down_price_frac_63d},
    "vtr_105_vol_trend_price_divergence_21d": {"inputs": ["close", "volume"], "func": vtr_105_vol_trend_price_divergence_21d},
    "vtr_106_vol_trend_price_divergence_63d": {"inputs": ["close", "volume"], "func": vtr_106_vol_trend_price_divergence_63d},
    "vtr_107_vol_up_trend_price_down_flag_21d": {"inputs": ["close", "volume"], "func": vtr_107_vol_up_trend_price_down_flag_21d},
    "vtr_108_vol_down_trend_price_down_flag_21d": {"inputs": ["close", "volume"], "func": vtr_108_vol_down_trend_price_down_flag_21d},
    "vtr_109_vol_up_trend_price_down_flag_63d": {"inputs": ["close", "volume"], "func": vtr_109_vol_up_trend_price_down_flag_63d},
    "vtr_110_logvol_slope_21d_times_price_slope_sign": {"inputs": ["close", "volume"], "func": vtr_110_logvol_slope_21d_times_price_slope_sign},
    "vtr_111_vol_cumulative_trend_down_days_21d": {"inputs": ["close", "volume"], "func": vtr_111_vol_cumulative_trend_down_days_21d},
    "vtr_112_logvol_21d_change": {"inputs": ["volume"], "func": vtr_112_logvol_21d_change},
    "vtr_113_logvol_63d_change": {"inputs": ["volume"], "func": vtr_113_logvol_63d_change},
    "vtr_114_logvol_126d_change": {"inputs": ["volume"], "func": vtr_114_logvol_126d_change},
    "vtr_115_logvol_252d_change": {"inputs": ["volume"], "func": vtr_115_logvol_252d_change},
    "vtr_116_logvol_21d_change_pct_rank_252d": {"inputs": ["volume"], "func": vtr_116_logvol_21d_change_pct_rank_252d},
    "vtr_117_logvol_63d_change_zscore_252d": {"inputs": ["volume"], "func": vtr_117_logvol_63d_change_zscore_252d},
    "vtr_118_vol_21d_return": {"inputs": ["volume"], "func": vtr_118_vol_21d_return},
    "vtr_119_vol_63d_return": {"inputs": ["volume"], "func": vtr_119_vol_63d_return},
    "vtr_120_vol_126d_return": {"inputs": ["volume"], "func": vtr_120_vol_126d_return},
    "vtr_121_vol_252d_return": {"inputs": ["volume"], "func": vtr_121_vol_252d_return},
    "vtr_122_vol_21d_return_pct_rank_252d": {"inputs": ["volume"], "func": vtr_122_vol_21d_return_pct_rank_252d},
    "vtr_123_vol_63d_return_zscore_252d": {"inputs": ["volume"], "func": vtr_123_vol_63d_return_zscore_252d},
    "vtr_124_vol_ema21_slope_21d": {"inputs": ["volume"], "func": vtr_124_vol_ema21_slope_21d},
    "vtr_125_vol_ema63_slope_21d": {"inputs": ["volume"], "func": vtr_125_vol_ema63_slope_21d},
    "vtr_126_vol_ema21_slope_63d": {"inputs": ["volume"], "func": vtr_126_vol_ema21_slope_63d},
    "vtr_127_vol_ema63_slope_63d": {"inputs": ["volume"], "func": vtr_127_vol_ema63_slope_63d},
    "vtr_128_vol_ema21_slope_sign_21d": {"inputs": ["volume"], "func": vtr_128_vol_ema21_slope_sign_21d},
    "vtr_129_vol_ema63_slope_sign_21d": {"inputs": ["volume"], "func": vtr_129_vol_ema63_slope_sign_21d},
    "vtr_130_vol_ema21_5d_change": {"inputs": ["volume"], "func": vtr_130_vol_ema21_5d_change},
    "vtr_131_vol_ema63_21d_change": {"inputs": ["volume"], "func": vtr_131_vol_ema63_21d_change},
    "vtr_132_vol_ema21_5d_change_norm": {"inputs": ["volume"], "func": vtr_132_vol_ema21_5d_change_norm},
    "vtr_133_vol_ema63_21d_change_norm": {"inputs": ["volume"], "func": vtr_133_vol_ema63_21d_change_norm},
    "vtr_134_vol_ema21_declining_flag": {"inputs": ["volume"], "func": vtr_134_vol_ema21_declining_flag},
    "vtr_135_vol_ema63_declining_flag": {"inputs": ["volume"], "func": vtr_135_vol_ema63_declining_flag},
    "vtr_136_vol_trend_score_composite_4window": {"inputs": ["volume"], "func": vtr_136_vol_trend_score_composite_4window},
    "vtr_137_logvol_slope_composite_4window": {"inputs": ["volume"], "func": vtr_137_logvol_slope_composite_4window},
    "vtr_138_vol_trend_regime_score": {"inputs": ["volume"], "func": vtr_138_vol_trend_regime_score},
    "vtr_139_vol_rising_days_frac_126d": {"inputs": ["volume"], "func": vtr_139_vol_rising_days_frac_126d},
    "vtr_140_vol_net_drift_21d_zscore_252d": {"inputs": ["volume"], "func": vtr_140_vol_net_drift_21d_zscore_252d},
    "vtr_141_vol_net_drift_63d_zscore_252d": {"inputs": ["volume"], "func": vtr_141_vol_net_drift_63d_zscore_252d},
    "vtr_142_vol_rising_weeks_count_63d": {"inputs": ["volume"], "func": vtr_142_vol_rising_weeks_count_63d},
    "vtr_143_vol_rising_weeks_count_252d": {"inputs": ["volume"], "func": vtr_143_vol_rising_weeks_count_252d},
    "vtr_144_vol_logslope_21d_expanding_zscore": {"inputs": ["volume"], "func": vtr_144_vol_logslope_21d_expanding_zscore},
    "vtr_145_vol_logslope_63d_expanding_zscore": {"inputs": ["volume"], "func": vtr_145_vol_logslope_63d_expanding_zscore},
    "vtr_146_vol_ema21_vs_ema252_ratio_zscore_252d": {"inputs": ["volume"], "func": vtr_146_vol_ema21_vs_ema252_ratio_zscore_252d},
    "vtr_147_vol_slope_21d_negative_count_63d": {"inputs": ["volume"], "func": vtr_147_vol_slope_21d_negative_count_63d},
    "vtr_148_vol_slope_21d_negative_count_252d": {"inputs": ["volume"], "func": vtr_148_vol_slope_21d_negative_count_252d},
    "vtr_149_vol_ema21_slope_21d_norm": {"inputs": ["volume"], "func": vtr_149_vol_ema21_slope_21d_norm},
    "vtr_150_vol_trend_strength_index": {"inputs": ["volume"], "func": vtr_150_vol_trend_strength_index},
    "vtr_176_vol_dollar_volume_slope_21d_norm": {"inputs": ["close", "volume"], "func": vtr_176_vol_dollar_volume_slope_21d_norm},
    "vtr_177_vol_dollar_volume_slope_63d_norm": {"inputs": ["close", "volume"], "func": vtr_177_vol_dollar_volume_slope_63d_norm},
    "vtr_178_vol_intraday_range_vol_slope_21d": {"inputs": ["high", "low", "volume"], "func": vtr_178_vol_intraday_range_vol_slope_21d},
    "vtr_179_vol_high_low_weighted_vol_sma21_vs_sma63": {"inputs": ["high", "low", "volume"], "func": vtr_179_vol_high_low_weighted_vol_sma21_vs_sma63},
    "vtr_180_vol_slope_126d_norm": {"inputs": ["volume"], "func": vtr_180_vol_slope_126d_norm},
    "vtr_181_logvol_slope_252d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_181_logvol_slope_252d_pct_rank_252d},
    "vtr_182_vol_ema63_vs_ema126_ratio": {"inputs": ["volume"], "func": vtr_182_vol_ema63_vs_ema126_ratio},
    "vtr_183_vol_sma63_vs_sma126_ratio": {"inputs": ["volume"], "func": vtr_183_vol_sma63_vs_sma126_ratio},
    "vtr_184_vol_slope_all_negative_flag_4window": {"inputs": ["volume"], "func": vtr_184_vol_slope_all_negative_flag_4window},
    "vtr_185_vol_sma_crossover_score_4level": {"inputs": ["volume"], "func": vtr_185_vol_sma_crossover_score_4level},
    "vtr_186_vol_rising_days_frac_126d_zscore_252d": {"inputs": ["volume"], "func": vtr_186_vol_rising_days_frac_126d_zscore_252d},
    "vtr_187_vol_net_drift_252d_zscore_252d": {"inputs": ["volume"], "func": vtr_187_vol_net_drift_252d_zscore_252d},
    "vtr_188_vol_ema63_slope_126d": {"inputs": ["volume"], "func": vtr_188_vol_ema63_slope_126d},
    "vtr_189_vol_ema126_slope_63d": {"inputs": ["volume"], "func": vtr_189_vol_ema126_slope_63d},
    "vtr_190_vol_logslope_10d_zscore_63d": {"inputs": ["volume"], "func": vtr_190_vol_logslope_10d_zscore_63d},
    "vtr_191_vol_price_down_vol_down_frac_63d": {"inputs": ["close", "volume"], "func": vtr_191_vol_price_down_vol_down_frac_63d},
    "vtr_192_vol_price_down_vol_up_frac_63d": {"inputs": ["close", "volume"], "func": vtr_192_vol_price_down_vol_up_frac_63d},
    "vtr_193_vol_cumulative_down_day_vol_norm_63d": {"inputs": ["close", "volume"], "func": vtr_193_vol_cumulative_down_day_vol_norm_63d},
    "vtr_194_vol_slope_252d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_194_vol_slope_252d_pct_rank_252d},
    "vtr_195_logvol_21d_change_zscore_63d": {"inputs": ["volume"], "func": vtr_195_logvol_21d_change_zscore_63d},
    "vtr_196_vol_ema21_above_ema126_flag": {"inputs": ["volume"], "func": vtr_196_vol_ema21_above_ema126_flag},
    "vtr_197_vol_sma126_above_sma252_flag": {"inputs": ["volume"], "func": vtr_197_vol_sma126_above_sma252_flag},
    "vtr_198_vol_ema_dispersion_4level": {"inputs": ["volume"], "func": vtr_198_vol_ema_dispersion_4level},
    "vtr_199_vol_open_close_range_vol_slope_21d": {"inputs": ["open", "close", "volume"], "func": vtr_199_vol_open_close_range_vol_slope_21d},
    "vtr_200_vol_trend_strength_index_4window": {"inputs": ["volume"], "func": vtr_200_vol_trend_strength_index_4window},
}
