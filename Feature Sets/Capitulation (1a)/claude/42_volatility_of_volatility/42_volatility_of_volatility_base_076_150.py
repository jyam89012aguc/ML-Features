"""
42_volatility_of_volatility — Base Features 076-150
Domain: instability/dispersion of the volatility series itself (vol-of-vol)
Measures: EWM-based vov, variance of vol, vol-of-vol z-scores, skew of rvol,
vol trend instability, intraday range variability, vol up-step vs down-step,
high-low vol spread measures, vol path entropy proxies, multi-scale vov composites.
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
_SQRT252 = 252 ** 0.5

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


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


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility over w-day rolling window."""
    lr = _log_ret(close)
    return lr.rolling(w, min_periods=max(2, w // 2)).std() * _SQRT252


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Average True Range over w-day window."""
    return _rolling_mean(_tr(close, high, low), w)


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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): EWM-based vol-of-vol and variance of vol ---

def vov_076_ewm_std_rvol21_span21(close: pd.Series) -> pd.Series:
    """EWM std (span=21) of 21d rvol series (EWM vol-of-vol)."""
    rv = _realized_vol(close, _TD_MON)
    return _ewm_std(rv, _TD_MON)


def vov_077_ewm_std_rvol21_span63(close: pd.Series) -> pd.Series:
    """EWM std (span=63) of 21d rvol series."""
    rv = _realized_vol(close, _TD_MON)
    return _ewm_std(rv, _TD_QTR)


def vov_078_ewm_std_rvol5_span21(close: pd.Series) -> pd.Series:
    """EWM std (span=21) of 5d rvol series."""
    rv = _realized_vol(close, _TD_WEEK)
    return _ewm_std(rv, _TD_MON)


def vov_079_ewm_std_rvol5_span63(close: pd.Series) -> pd.Series:
    """EWM std (span=63) of 5d rvol series."""
    rv = _realized_vol(close, _TD_WEEK)
    return _ewm_std(rv, _TD_QTR)


def vov_080_var_rvol21_63d(close: pd.Series) -> pd.Series:
    """Variance of 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).var()


def vov_081_var_rvol21_252d(close: pd.Series) -> pd.Series:
    """Variance of 21d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).var()


def vov_082_var_rvol5_63d(close: pd.Series) -> pd.Series:
    """Variance of 5d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_WEEK)
    return rv.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).var()


def vov_083_ewm_cv_rvol21_span63(close: pd.Series) -> pd.Series:
    """EWM CV of 21d rvol: ewm_std / ewm_mean (span=63)."""
    rv = _realized_vol(close, _TD_MON)
    return _safe_div(_ewm_std(rv, _TD_QTR), _ewm_mean(rv, _TD_QTR).clip(lower=_EPS))


def vov_084_ewm_cv_rvol5_span21(close: pd.Series) -> pd.Series:
    """EWM CV of 5d rvol: ewm_std / ewm_mean (span=21)."""
    rv = _realized_vol(close, _TD_WEEK)
    return _safe_div(_ewm_std(rv, _TD_MON), _ewm_mean(rv, _TD_MON).clip(lower=_EPS))


def vov_085_ewm_vov_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of ewm_std(span=21) to ewm_std(span=63) of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    return _safe_div(_ewm_std(rv, _TD_MON), _ewm_std(rv, _TD_QTR).clip(lower=_EPS))


def vov_086_ewm_vov_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of ewm_std(span=63) of 21d rvol within 252 days."""
    rv = _realized_vol(close, _TD_MON)
    vv = _ewm_std(rv, _TD_QTR)
    return vv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_087_ewm_std_atr21_span63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM std (span=63) of 21d ATR (EWM instability of ATR)."""
    a = _atr(close, high, low, _TD_MON)
    return _ewm_std(a, _TD_QTR)


def vov_088_ewm_std_atr21_span21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM std (span=21) of 21d ATR."""
    a = _atr(close, high, low, _TD_MON)
    return _ewm_std(a, _TD_MON)


def vov_089_ewm_cv_atr21_span63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM CV of 21d ATR (ewm_std/ewm_mean, span=63)."""
    a = _atr(close, high, low, _TD_MON)
    return _safe_div(_ewm_std(a, _TD_QTR), _ewm_mean(a, _TD_QTR).clip(lower=_EPS))


def vov_090_var_rvol21_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d variance of 21d rvol within 252 days."""
    rv = _realized_vol(close, _TD_MON)
    v = rv.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).var()
    return v.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group G (091-105): Vol-of-vol z-scores and higher-moment instability ---

def vov_091_vov_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 63d vov (std of 21d rvol) within its 252d distribution."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    m = _rolling_mean(vv, _TD_YEAR)
    s = _rolling_std(vv, _TD_YEAR)
    return _safe_div(vv - m, s.clip(lower=_EPS))


def vov_092_cv_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 63d CV of 21d rvol within its 252d distribution."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))
    m = _rolling_mean(cv, _TD_YEAR)
    s = _rolling_std(cv, _TD_YEAR)
    return _safe_div(cv - m, s.clip(lower=_EPS))


def vov_093_mac_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d MAC of 21d rvol within its 252d distribution."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    m = _rolling_mean(mac, _TD_YEAR)
    s = _rolling_std(mac, _TD_YEAR)
    return _safe_div(mac - m, s.clip(lower=_EPS))


def vov_094_skew_rvol21_63d(close: pd.Series) -> pd.Series:
    """Rolling skewness of 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def vov_095_skew_rvol21_252d(close: pd.Series) -> pd.Series:
    """Rolling skewness of 21d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).skew()


def vov_096_skew_rvol5_63d(close: pd.Series) -> pd.Series:
    """Rolling skewness of 5d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_WEEK)
    return rv.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def vov_097_kurt_rvol21_63d(close: pd.Series) -> pd.Series:
    """Rolling kurtosis of 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def vov_098_kurt_rvol21_252d(close: pd.Series) -> pd.Series:
    """Rolling kurtosis of 21d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 2)).kurt()


def vov_099_vov_above_longrun_flag(close: pd.Series) -> pd.Series:
    """Flag: 63d vov exceeds 252d average vov (elevated instability regime)."""
    rv = _realized_vol(close, _TD_MON)
    vv63 = _rolling_std(rv, _TD_QTR)
    avg252 = _rolling_mean(vv63, _TD_YEAR)
    return (vv63 > avg252).astype(float)


def vov_100_vov_vs_avg_ratio(close: pd.Series) -> pd.Series:
    """Ratio of current 63d vov to its 252d average."""
    rv = _realized_vol(close, _TD_MON)
    vv63 = _rolling_std(rv, _TD_QTR)
    avg = _rolling_mean(vv63, _TD_YEAR)
    return _safe_div(vv63, avg.clip(lower=_EPS))


def vov_101_max_vov_252d(close: pd.Series) -> pd.Series:
    """Maximum 63d vov seen in trailing 252 days (peak instability)."""
    rv = _realized_vol(close, _TD_MON)
    vv63 = _rolling_std(rv, _TD_QTR)
    return _rolling_max(vv63, _TD_YEAR)


def vov_102_current_vov_vs_max_252d(close: pd.Series) -> pd.Series:
    """Current 63d vov as fraction of its 252d maximum."""
    rv = _realized_vol(close, _TD_MON)
    vv63 = _rolling_std(rv, _TD_QTR)
    mx = _rolling_max(vv63, _TD_YEAR)
    return _safe_div(vv63, mx.clip(lower=_EPS))


def vov_103_vov_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of 63d vov (all-history standardized)."""
    rv = _realized_vol(close, _TD_MON)
    vv63 = _rolling_std(rv, _TD_QTR)
    m = vv63.expanding(min_periods=_TD_QTR).mean()
    s = vv63.expanding(min_periods=_TD_QTR).std()
    return _safe_div(vv63 - m, s.clip(lower=_EPS))


def vov_104_range_vov_252d(close: pd.Series) -> pd.Series:
    """Range of 63d vov over trailing 252 days (meta-instability of vov)."""
    rv = _realized_vol(close, _TD_MON)
    vv63 = _rolling_std(rv, _TD_QTR)
    return _rolling_max(vv63, _TD_YEAR) - _rolling_min(vv63, _TD_YEAR)


def vov_105_mac_vov_252d(close: pd.Series) -> pd.Series:
    """Mean absolute daily change of 63d vov over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    vv63 = _rolling_std(rv, _TD_QTR)
    return vv63.diff(1).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


# --- Group H (106-120): Intraday range variability and vol-of-intraday-range ---

def vov_106_std_tr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of daily true range over trailing 21 days."""
    tr = _tr(close, high, low)
    return _rolling_std(tr, _TD_MON)


def vov_107_std_tr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of daily true range over trailing 63 days."""
    tr = _tr(close, high, low)
    return _rolling_std(tr, _TD_QTR)


def vov_108_std_tr_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of daily true range over trailing 252 days."""
    tr = _tr(close, high, low)
    return _rolling_std(tr, _TD_YEAR)


def vov_109_cv_tr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CV of daily true range over trailing 21 days."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_std(tr, _TD_MON), _rolling_mean(tr, _TD_MON).clip(lower=_EPS))


def vov_110_cv_tr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CV of daily true range over trailing 63 days."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_std(tr, _TD_QTR), _rolling_mean(tr, _TD_QTR).clip(lower=_EPS))


def vov_111_cv_tr_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CV of daily true range over trailing 252 days."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_std(tr, _TD_YEAR), _rolling_mean(tr, _TD_YEAR).clip(lower=_EPS))


def vov_112_std_hl_range_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of high-low range (not true range) over trailing 21 days."""
    hl = high - low
    return _rolling_std(hl, _TD_MON)


def vov_113_std_hl_range_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of high-low range over trailing 63 days."""
    hl = high - low
    return _rolling_std(hl, _TD_QTR)


def vov_114_cv_hl_range_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CV of high-low range over trailing 63 days."""
    hl = high - low
    return _safe_div(_rolling_std(hl, _TD_QTR), _rolling_mean(hl, _TD_QTR).clip(lower=_EPS))


def vov_115_mac_tr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean absolute daily change of true range over trailing 63 days."""
    tr = _tr(close, high, low)
    return tr.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vov_116_mac_tr_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean absolute daily change of true range over trailing 252 days."""
    tr = _tr(close, high, low)
    return tr.diff(1).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vov_117_range_tr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range (max-min) of true range over trailing 63 days."""
    tr = _tr(close, high, low)
    return _rolling_max(tr, _TD_QTR) - _rolling_min(tr, _TD_QTR)


def vov_118_range_tr_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range (max-min) of true range over trailing 252 days."""
    tr = _tr(close, high, low)
    return _rolling_max(tr, _TD_YEAR) - _rolling_min(tr, _TD_YEAR)


def vov_119_std_tr_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63d std of TR within trailing 252 days."""
    tr = _tr(close, high, low)
    s63 = _rolling_std(tr, _TD_QTR)
    return s63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_120_cv_tr_63d_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63d CV of TR within trailing 252 days."""
    tr = _tr(close, high, low)
    cv = _safe_div(_rolling_std(tr, _TD_QTR), _rolling_mean(tr, _TD_QTR).clip(lower=_EPS))
    return cv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group I (121-135): Vol up-step vs down-step asymmetry ---

def vov_121_vol_up_steps_mean_63d(close: pd.Series) -> pd.Series:
    """Mean of daily upward changes in 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    up = rv.diff(1).clip(lower=0)
    return _rolling_mean(up, _TD_QTR)


def vov_122_vol_down_steps_mean_63d(close: pd.Series) -> pd.Series:
    """Mean of daily downward changes (abs) in 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    down = rv.diff(1).clip(upper=0).abs()
    return _rolling_mean(down, _TD_QTR)


def vov_123_vol_step_asymmetry_63d(close: pd.Series) -> pd.Series:
    """Ratio of mean vol up-step to mean vol down-step over 63 days."""
    rv = _realized_vol(close, _TD_MON)
    d = rv.diff(1)
    up = d.clip(lower=0).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    dn = d.clip(upper=0).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return _safe_div(up, dn.clip(lower=_EPS))


def vov_124_vol_up_freq_63d(close: pd.Series) -> pd.Series:
    """Fraction of days where 21d rvol rose over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    up = (rv.diff(1) > 0).astype(float)
    return _rolling_mean(up, _TD_QTR)


def vov_125_vol_up_freq_252d(close: pd.Series) -> pd.Series:
    """Fraction of days where 21d rvol rose over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    up = (rv.diff(1) > 0).astype(float)
    return _rolling_mean(up, _TD_YEAR)


def vov_126_vol_large_up_step_freq_63d(close: pd.Series) -> pd.Series:
    """Frequency of large vol up-steps (>1 std of daily vol change) over 63d."""
    rv = _realized_vol(close, _TD_MON)
    d = rv.diff(1)
    threshold = _rolling_std(d, _TD_YEAR)
    large_up = (d > threshold).astype(float)
    return _rolling_sum(large_up, _TD_QTR)


def vov_127_vol_large_down_step_freq_63d(close: pd.Series) -> pd.Series:
    """Frequency of large vol down-steps (< -1 std) over 63d."""
    rv = _realized_vol(close, _TD_MON)
    d = rv.diff(1)
    threshold = _rolling_std(d, _TD_YEAR)
    large_dn = (d < -threshold).astype(float)
    return _rolling_sum(large_dn, _TD_QTR)


def vov_128_vol_step_std_21d(close: pd.Series) -> pd.Series:
    """Std of daily changes in 21d rvol over trailing 21 days."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_std(rv.diff(1), _TD_MON)


def vov_129_vol_step_std_63d(close: pd.Series) -> pd.Series:
    """Std of daily changes in 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_std(rv.diff(1), _TD_QTR)


def vov_130_vol_step_std_252d(close: pd.Series) -> pd.Series:
    """Std of daily changes in 21d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    return _rolling_std(rv.diff(1), _TD_YEAR)


def vov_131_vol_step_std_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d std of daily vol-changes within 252 days."""
    rv = _realized_vol(close, _TD_MON)
    s = _rolling_std(rv.diff(1), _TD_QTR)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_132_vol_consec_up_streak(close: pd.Series) -> pd.Series:
    """Current consecutive days where 21d rvol is rising."""
    rv = _realized_vol(close, _TD_MON)
    cond = rv.diff(1) > 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def vov_133_vol_consec_down_streak(close: pd.Series) -> pd.Series:
    """Current consecutive days where 21d rvol is falling."""
    rv = _realized_vol(close, _TD_MON)
    cond = rv.diff(1) < 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def vov_134_vol_step_skew_63d(close: pd.Series) -> pd.Series:
    """Skewness of daily changes in 21d rvol over trailing 63 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.diff(1).rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def vov_135_vol_step_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of daily changes in 21d rvol over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    return rv.diff(1).rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).skew()


# --- Group J (136-150): Multi-scale vov composites and trend instability ---

def vov_136_vov_composite_3scale(close: pd.Series) -> pd.Series:
    """Mean of normalized vov at 3 scales (21d,63d,126d windows of 21d rvol)."""
    rv = _realized_vol(close, _TD_MON)
    v21 = _rolling_std(rv, _TD_MON)
    v63 = _rolling_std(rv, _TD_QTR)
    v126 = _rolling_std(rv, _TD_HALF)
    avg21 = _rolling_mean(v21, _TD_YEAR).clip(lower=_EPS)
    avg63 = _rolling_mean(v63, _TD_YEAR).clip(lower=_EPS)
    avg126 = _rolling_mean(v126, _TD_YEAR).clip(lower=_EPS)
    return (v21 / avg21 + v63 / avg63 + v126 / avg126) / 3.0


def vov_137_vov_trend_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21d vov series over trailing 63 days (trend in vov)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_MON)
    return _linslope(vv, _TD_QTR)


def vov_138_vov_trend_slope_252d(close: pd.Series) -> pd.Series:
    """OLS slope of 21d vov series over trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_MON)
    return _linslope(vv, _TD_YEAR)


def vov_139_cv_composite_rvol5_21(close: pd.Series) -> pd.Series:
    """Sum of CV of 5d rvol and CV of 21d rvol over 63d (multi-tenor instability)."""
    cv5 = _safe_div(_rolling_std(_realized_vol(close, _TD_WEEK), _TD_QTR),
                    _rolling_mean(_realized_vol(close, _TD_WEEK), _TD_QTR).clip(lower=_EPS))
    cv21 = _safe_div(_rolling_std(_realized_vol(close, _TD_MON), _TD_QTR),
                     _rolling_mean(_realized_vol(close, _TD_MON), _TD_QTR).clip(lower=_EPS))
    return (cv5 + cv21) / 2.0


def vov_140_vov_above_2std_flag(close: pd.Series) -> pd.Series:
    """Flag: current 63d vov > (252d mean + 2 * 252d std of vov)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    m = _rolling_mean(vv, _TD_YEAR)
    s = _rolling_std(vv, _TD_YEAR)
    return (vv > m + 2.0 * s).astype(float)


def vov_141_vov_above_1std_flag(close: pd.Series) -> pd.Series:
    """Flag: current 63d vov > (252d mean + 1 * 252d std of vov)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    m = _rolling_mean(vv, _TD_YEAR)
    s = _rolling_std(vv, _TD_YEAR)
    return (vv > m + s).astype(float)


def vov_142_rvol_median_dev_63d(close: pd.Series) -> pd.Series:
    """Mean absolute deviation of 21d rvol from its 63d median."""
    rv = _realized_vol(close, _TD_MON)
    med = _rolling_median(rv, _TD_QTR)
    return (rv - med).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vov_143_rvol_median_dev_252d(close: pd.Series) -> pd.Series:
    """Mean absolute deviation of 21d rvol from its 252d median."""
    rv = _realized_vol(close, _TD_MON)
    med = _rolling_median(rv, _TD_YEAR)
    return (rv - med).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vov_144_rvol_high_low_spread_63d(close: pd.Series) -> pd.Series:
    """Ratio of 63d max rvol to 63d min rvol (vol high/low spread)."""
    rv = _realized_vol(close, _TD_MON)
    return _safe_div(_rolling_max(rv, _TD_QTR), _rolling_min(rv, _TD_QTR).clip(lower=_EPS))


def vov_145_rvol_high_low_spread_252d(close: pd.Series) -> pd.Series:
    """Ratio of 252d max rvol to 252d min rvol."""
    rv = _realized_vol(close, _TD_MON)
    return _safe_div(_rolling_max(rv, _TD_YEAR), _rolling_min(rv, _TD_YEAR).clip(lower=_EPS))


def vov_146_vov_accel_21d(close: pd.Series) -> pd.Series:
    """Second-order diff (5d) of 63d vov (acceleration of vov trend)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    return vv.diff(_TD_WEEK).diff(_TD_WEEK)


def vov_147_rvol21_vs_rvol63_spread(close: pd.Series) -> pd.Series:
    """Spread between 21d and 63d realized vols (short minus long vol)."""
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    return rv21 - rv63


def vov_148_rvol21_vs_rvol63_spread_std_63d(close: pd.Series) -> pd.Series:
    """Std of (21d rvol - 63d rvol) spread over trailing 63 days."""
    spread = _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_QTR)
    return _rolling_std(spread, _TD_QTR)


def vov_149_rvol21_vs_rvol63_spread_std_252d(close: pd.Series) -> pd.Series:
    """Std of (21d rvol - 63d rvol) spread over trailing 252 days."""
    spread = _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_QTR)
    return _rolling_std(spread, _TD_YEAR)


def vov_150_vov_cv_composite_252d(close: pd.Series) -> pd.Series:
    """252d average of absolute normalized daily vov changes (meta-instability)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    dv = vv.diff(1).abs()
    avg_vv = _rolling_mean(vv, _TD_YEAR).clip(lower=_EPS)
    return _rolling_mean(_safe_div(dv, avg_vv), _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_OF_VOLATILITY_REGISTRY_076_150 = {
    "vov_076_ewm_std_rvol21_span21": {"inputs": ["close"], "func": vov_076_ewm_std_rvol21_span21},
    "vov_077_ewm_std_rvol21_span63": {"inputs": ["close"], "func": vov_077_ewm_std_rvol21_span63},
    "vov_078_ewm_std_rvol5_span21": {"inputs": ["close"], "func": vov_078_ewm_std_rvol5_span21},
    "vov_079_ewm_std_rvol5_span63": {"inputs": ["close"], "func": vov_079_ewm_std_rvol5_span63},
    "vov_080_var_rvol21_63d": {"inputs": ["close"], "func": vov_080_var_rvol21_63d},
    "vov_081_var_rvol21_252d": {"inputs": ["close"], "func": vov_081_var_rvol21_252d},
    "vov_082_var_rvol5_63d": {"inputs": ["close"], "func": vov_082_var_rvol5_63d},
    "vov_083_ewm_cv_rvol21_span63": {"inputs": ["close"], "func": vov_083_ewm_cv_rvol21_span63},
    "vov_084_ewm_cv_rvol5_span21": {"inputs": ["close"], "func": vov_084_ewm_cv_rvol5_span21},
    "vov_085_ewm_vov_ratio_21d_vs_63d": {"inputs": ["close"], "func": vov_085_ewm_vov_ratio_21d_vs_63d},
    "vov_086_ewm_vov_pct_rank_252d": {"inputs": ["close"], "func": vov_086_ewm_vov_pct_rank_252d},
    "vov_087_ewm_std_atr21_span63": {"inputs": ["close", "high", "low"], "func": vov_087_ewm_std_atr21_span63},
    "vov_088_ewm_std_atr21_span21": {"inputs": ["close", "high", "low"], "func": vov_088_ewm_std_atr21_span21},
    "vov_089_ewm_cv_atr21_span63": {"inputs": ["close", "high", "low"], "func": vov_089_ewm_cv_atr21_span63},
    "vov_090_var_rvol21_63d_pct_rank_252d": {"inputs": ["close"], "func": vov_090_var_rvol21_63d_pct_rank_252d},
    "vov_091_vov_zscore_252d": {"inputs": ["close"], "func": vov_091_vov_zscore_252d},
    "vov_092_cv_zscore_252d": {"inputs": ["close"], "func": vov_092_cv_zscore_252d},
    "vov_093_mac_zscore_252d": {"inputs": ["close"], "func": vov_093_mac_zscore_252d},
    "vov_094_skew_rvol21_63d": {"inputs": ["close"], "func": vov_094_skew_rvol21_63d},
    "vov_095_skew_rvol21_252d": {"inputs": ["close"], "func": vov_095_skew_rvol21_252d},
    "vov_096_skew_rvol5_63d": {"inputs": ["close"], "func": vov_096_skew_rvol5_63d},
    "vov_097_kurt_rvol21_63d": {"inputs": ["close"], "func": vov_097_kurt_rvol21_63d},
    "vov_098_kurt_rvol21_252d": {"inputs": ["close"], "func": vov_098_kurt_rvol21_252d},
    "vov_099_vov_above_longrun_flag": {"inputs": ["close"], "func": vov_099_vov_above_longrun_flag},
    "vov_100_vov_vs_avg_ratio": {"inputs": ["close"], "func": vov_100_vov_vs_avg_ratio},
    "vov_101_max_vov_252d": {"inputs": ["close"], "func": vov_101_max_vov_252d},
    "vov_102_current_vov_vs_max_252d": {"inputs": ["close"], "func": vov_102_current_vov_vs_max_252d},
    "vov_103_vov_expanding_zscore": {"inputs": ["close"], "func": vov_103_vov_expanding_zscore},
    "vov_104_range_vov_252d": {"inputs": ["close"], "func": vov_104_range_vov_252d},
    "vov_105_mac_vov_252d": {"inputs": ["close"], "func": vov_105_mac_vov_252d},
    "vov_106_std_tr_21d": {"inputs": ["close", "high", "low"], "func": vov_106_std_tr_21d},
    "vov_107_std_tr_63d": {"inputs": ["close", "high", "low"], "func": vov_107_std_tr_63d},
    "vov_108_std_tr_252d": {"inputs": ["close", "high", "low"], "func": vov_108_std_tr_252d},
    "vov_109_cv_tr_21d": {"inputs": ["close", "high", "low"], "func": vov_109_cv_tr_21d},
    "vov_110_cv_tr_63d": {"inputs": ["close", "high", "low"], "func": vov_110_cv_tr_63d},
    "vov_111_cv_tr_252d": {"inputs": ["close", "high", "low"], "func": vov_111_cv_tr_252d},
    "vov_112_std_hl_range_21d": {"inputs": ["close", "high", "low"], "func": vov_112_std_hl_range_21d},
    "vov_113_std_hl_range_63d": {"inputs": ["close", "high", "low"], "func": vov_113_std_hl_range_63d},
    "vov_114_cv_hl_range_63d": {"inputs": ["close", "high", "low"], "func": vov_114_cv_hl_range_63d},
    "vov_115_mac_tr_63d": {"inputs": ["close", "high", "low"], "func": vov_115_mac_tr_63d},
    "vov_116_mac_tr_252d": {"inputs": ["close", "high", "low"], "func": vov_116_mac_tr_252d},
    "vov_117_range_tr_63d": {"inputs": ["close", "high", "low"], "func": vov_117_range_tr_63d},
    "vov_118_range_tr_252d": {"inputs": ["close", "high", "low"], "func": vov_118_range_tr_252d},
    "vov_119_std_tr_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": vov_119_std_tr_pct_rank_252d},
    "vov_120_cv_tr_63d_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": vov_120_cv_tr_63d_pct_rank_252d},
    "vov_121_vol_up_steps_mean_63d": {"inputs": ["close"], "func": vov_121_vol_up_steps_mean_63d},
    "vov_122_vol_down_steps_mean_63d": {"inputs": ["close"], "func": vov_122_vol_down_steps_mean_63d},
    "vov_123_vol_step_asymmetry_63d": {"inputs": ["close"], "func": vov_123_vol_step_asymmetry_63d},
    "vov_124_vol_up_freq_63d": {"inputs": ["close"], "func": vov_124_vol_up_freq_63d},
    "vov_125_vol_up_freq_252d": {"inputs": ["close"], "func": vov_125_vol_up_freq_252d},
    "vov_126_vol_large_up_step_freq_63d": {"inputs": ["close"], "func": vov_126_vol_large_up_step_freq_63d},
    "vov_127_vol_large_down_step_freq_63d": {"inputs": ["close"], "func": vov_127_vol_large_down_step_freq_63d},
    "vov_128_vol_step_std_21d": {"inputs": ["close"], "func": vov_128_vol_step_std_21d},
    "vov_129_vol_step_std_63d": {"inputs": ["close"], "func": vov_129_vol_step_std_63d},
    "vov_130_vol_step_std_252d": {"inputs": ["close"], "func": vov_130_vol_step_std_252d},
    "vov_131_vol_step_std_pct_rank_252d": {"inputs": ["close"], "func": vov_131_vol_step_std_pct_rank_252d},
    "vov_132_vol_consec_up_streak": {"inputs": ["close"], "func": vov_132_vol_consec_up_streak},
    "vov_133_vol_consec_down_streak": {"inputs": ["close"], "func": vov_133_vol_consec_down_streak},
    "vov_134_vol_step_skew_63d": {"inputs": ["close"], "func": vov_134_vol_step_skew_63d},
    "vov_135_vol_step_skew_252d": {"inputs": ["close"], "func": vov_135_vol_step_skew_252d},
    "vov_136_vov_composite_3scale": {"inputs": ["close"], "func": vov_136_vov_composite_3scale},
    "vov_137_vov_trend_slope_63d": {"inputs": ["close"], "func": vov_137_vov_trend_slope_63d},
    "vov_138_vov_trend_slope_252d": {"inputs": ["close"], "func": vov_138_vov_trend_slope_252d},
    "vov_139_cv_composite_rvol5_21": {"inputs": ["close"], "func": vov_139_cv_composite_rvol5_21},
    "vov_140_vov_above_2std_flag": {"inputs": ["close"], "func": vov_140_vov_above_2std_flag},
    "vov_141_vov_above_1std_flag": {"inputs": ["close"], "func": vov_141_vov_above_1std_flag},
    "vov_142_rvol_median_dev_63d": {"inputs": ["close"], "func": vov_142_rvol_median_dev_63d},
    "vov_143_rvol_median_dev_252d": {"inputs": ["close"], "func": vov_143_rvol_median_dev_252d},
    "vov_144_rvol_high_low_spread_63d": {"inputs": ["close"], "func": vov_144_rvol_high_low_spread_63d},
    "vov_145_rvol_high_low_spread_252d": {"inputs": ["close"], "func": vov_145_rvol_high_low_spread_252d},
    "vov_146_vov_accel_21d": {"inputs": ["close"], "func": vov_146_vov_accel_21d},
    "vov_147_rvol21_vs_rvol63_spread": {"inputs": ["close"], "func": vov_147_rvol21_vs_rvol63_spread},
    "vov_148_rvol21_vs_rvol63_spread_std_63d": {"inputs": ["close"], "func": vov_148_rvol21_vs_rvol63_spread_std_63d},
    "vov_149_rvol21_vs_rvol63_spread_std_252d": {"inputs": ["close"], "func": vov_149_rvol21_vs_rvol63_spread_std_252d},
    "vov_150_vov_cv_composite_252d": {"inputs": ["close"], "func": vov_150_vov_cv_composite_252d},
}
