"""
114_overnight_intraday_split — Base Features 076-150
Domain: overnight vs intraday return decomposition — deeper variants including
        volume-weighted session returns, EWM cumulative returns, session-relative
        range analysis, cross-window consistency, normalized gap features
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _overnight_ret(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight return: prior close -> today open."""
    return open_ / close.shift(1) - 1.0


def _intraday_ret(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday return: today open -> today close."""
    return close / open_ - 1.0


def _total_ret(close: pd.Series) -> pd.Series:
    """Total daily return: prior close -> today close."""
    return close.pct_change(1)


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

# --- Group H (076-090): Volume-weighted session returns ---

def ois_076_vol_weighted_overnight_ret_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean overnight return over 21 days."""
    on = _overnight_ret(close, open)
    vol_sum = _rolling_sum(volume, _TD_MON)
    wt_sum = _rolling_sum(on * volume, _TD_MON)
    return _safe_div(wt_sum, vol_sum.replace(0, np.nan))


def ois_077_vol_weighted_intraday_ret_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean intraday return over 21 days."""
    intra = _intraday_ret(open, close)
    vol_sum = _rolling_sum(volume, _TD_MON)
    wt_sum = _rolling_sum(intra * volume, _TD_MON)
    return _safe_div(wt_sum, vol_sum.replace(0, np.nan))


def ois_078_vol_weighted_overnight_ret_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean overnight return over 63 days."""
    on = _overnight_ret(close, open)
    vol_sum = _rolling_sum(volume, _TD_QTR)
    wt_sum = _rolling_sum(on * volume, _TD_QTR)
    return _safe_div(wt_sum, vol_sum.replace(0, np.nan))


def ois_079_vol_weighted_intraday_ret_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean intraday return over 63 days."""
    intra = _intraday_ret(open, close)
    vol_sum = _rolling_sum(volume, _TD_QTR)
    wt_sum = _rolling_sum(intra * volume, _TD_QTR)
    return _safe_div(wt_sum, vol_sum.replace(0, np.nan))


def ois_080_high_volume_overnight_down_frac_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of high-volume days (top quartile) with negative overnight return (21d)."""
    on = _overnight_ret(close, open)
    vol_q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    high_vol = (volume >= vol_q75).astype(float)
    neg_on = (on < 0).astype(float)
    hv_cnt = _rolling_sum(high_vol, _TD_MON)
    hv_neg = _rolling_sum(high_vol * neg_on, _TD_MON)
    return _safe_div(hv_neg, hv_cnt.replace(0, np.nan))


def ois_081_high_volume_intraday_down_frac_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of high-volume days (top quartile) with negative intraday return (21d)."""
    intra = _intraday_ret(open, close)
    vol_q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    high_vol = (volume >= vol_q75).astype(float)
    neg_intra = (intra < 0).astype(float)
    hv_cnt = _rolling_sum(high_vol, _TD_MON)
    hv_neg = _rolling_sum(high_vol * neg_intra, _TD_MON)
    return _safe_div(hv_neg, hv_cnt.replace(0, np.nan))


def ois_082_overnight_down_volume_share_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of total volume occurring on overnight-down days (21d)."""
    on = _overnight_ret(close, open)
    neg_on_vol = _rolling_sum((on < 0).astype(float) * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(neg_on_vol, total_vol.replace(0, np.nan))


def ois_083_intraday_down_volume_share_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of total volume occurring on intraday-down days (21d)."""
    intra = _intraday_ret(open, close)
    neg_intra_vol = _rolling_sum((intra < 0).astype(float) * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(neg_intra_vol, total_vol.replace(0, np.nan))


def ois_084_overnight_ret_volume_corr_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between overnight return and volume."""
    on = _overnight_ret(close, open)
    return on.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).corr(volume)


def ois_085_intraday_ret_volume_corr_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between intraday return and volume."""
    intra = _intraday_ret(open, close)
    return intra.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).corr(volume)


def ois_086_overnight_ret_volume_corr_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between overnight return and volume."""
    on = _overnight_ret(close, open)
    return on.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).corr(volume)


def ois_087_intraday_ret_volume_corr_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between intraday return and volume."""
    intra = _intraday_ret(open, close)
    return intra.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).corr(volume)


def ois_088_overnight_negative_volume_intensity_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume * abs(overnight_ret) on negative overnight days (21d)."""
    on = _overnight_ret(close, open)
    return _rolling_sum((on < 0).astype(float) * volume * on.abs(), _TD_MON)


def ois_089_intraday_negative_volume_intensity_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume * abs(intraday_ret) on negative intraday days (21d)."""
    intra = _intraday_ret(open, close)
    return _rolling_sum((intra < 0).astype(float) * volume * intra.abs(), _TD_MON)


def ois_090_overnight_vs_intraday_volume_intensity_ratio_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of overnight negative volume intensity to intraday negative volume intensity (21d)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    on_int = _rolling_sum((on < 0).astype(float) * volume * on.abs(), _TD_MON)
    intra_int = _rolling_sum((intra < 0).astype(float) * volume * intra.abs(), _TD_MON)
    return _safe_div(on_int, intra_int.replace(0, np.nan))


# --- Group I (091-102): EWM and slope-based session features ---

def ois_091_ewm_overnight_ret_span21(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=21) of overnight return."""
    return _ewm_mean(_overnight_ret(close, open), _TD_MON)


def ois_092_ewm_intraday_ret_span21(open: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=21) of intraday return."""
    return _ewm_mean(_intraday_ret(open, close), _TD_MON)


def ois_093_ewm_overnight_ret_span63(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=63) of overnight return."""
    return _ewm_mean(_overnight_ret(close, open), _TD_QTR)


def ois_094_ewm_intraday_ret_span63(open: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=63) of intraday return."""
    return _ewm_mean(_intraday_ret(open, close), _TD_QTR)


def ois_095_overnight_ret_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of overnight return over 21 days (trend in overnight gaps)."""
    return _linslope(_overnight_ret(close, open), _TD_MON)


def ois_096_intraday_ret_slope_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of intraday return over 21 days (trend in intraday performance)."""
    return _linslope(_intraday_ret(open, close), _TD_MON)


def ois_097_overnight_ret_slope_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of overnight return over 63 days."""
    return _linslope(_overnight_ret(close, open), _TD_QTR)


def ois_098_intraday_ret_slope_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of intraday return over 63 days."""
    return _linslope(_intraday_ret(open, close), _TD_QTR)


def ois_099_overnight_ret_ewm_vs_mean_ratio_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of EWM(21) overnight return to simple mean (21d) — recency emphasis."""
    on = _overnight_ret(close, open)
    ewm = _ewm_mean(on, _TD_MON)
    mean = _rolling_mean(on, _TD_MON)
    return _safe_div(ewm, mean.replace(0, np.nan))


def ois_100_intraday_ret_ewm_vs_mean_ratio_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of EWM(21) intraday return to simple mean (21d)."""
    intra = _intraday_ret(open, close)
    ewm = _ewm_mean(intra, _TD_MON)
    mean = _rolling_mean(intra, _TD_MON)
    return _safe_div(ewm, mean.replace(0, np.nan))


def ois_101_overnight_negative_streak_max_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive negative overnight return streak within 63 days."""
    on = _overnight_ret(close, open)
    neg = (on < 0)

    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)

    return neg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def ois_102_intraday_negative_streak_max_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Maximum consecutive negative intraday return streak within 63 days."""
    intra = _intraday_ret(open, close)
    neg = (intra < 0)

    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)

    return neg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


# --- Group J (103-115): Gap size extremes and normalized gap metrics ---

def ois_103_overnight_gap_min_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day minimum overnight return (worst single gap)."""
    return _rolling_min(_overnight_ret(close, open), _TD_MON)


def ois_104_overnight_gap_min_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day minimum overnight return."""
    return _rolling_min(_overnight_ret(close, open), _TD_QTR)


def ois_105_intraday_ret_min_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum intraday return."""
    return _rolling_min(_intraday_ret(open, close), _TD_MON)


def ois_106_intraday_ret_min_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day minimum intraday return."""
    return _rolling_min(_intraday_ret(open, close), _TD_QTR)


def ois_107_overnight_gap_normalized_by_atr(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Overnight gap normalized by 14-day ATR."""
    on = _overnight_ret(close, open) * close.shift(1)
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    atr14 = _rolling_mean(tr, 14)
    return _safe_div(on, atr14.replace(0, np.nan))


def ois_108_intraday_range_normalized_by_atr(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday return normalized by 14-day ATR."""
    intra = _intraday_ret(open, close) * open
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    atr14 = _rolling_mean(tr, 14)
    return _safe_div(intra, atr14.replace(0, np.nan))


def ois_109_overnight_gap_down_size_mean_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean overnight return on gap-down days only (21d)."""
    on = _overnight_ret(close, open)
    neg_on = on.where(on < 0, np.nan)
    return _rolling_mean(neg_on, _TD_MON)


def ois_110_intraday_down_size_mean_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean intraday return on intraday-down days only (21d)."""
    intra = _intraday_ret(open, close)
    neg_intra = intra.where(intra < 0, np.nan)
    return _rolling_mean(neg_intra, _TD_MON)


def ois_111_overnight_gap_down_entry_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of new overnight gap-down below prior 5d low gap (entry events, 63d)."""
    on = _overnight_ret(close, open)
    prev_min = on.shift(1).rolling(_TD_WEEK, min_periods=1).min()
    entry = ((on < 0) & (on < prev_min)).astype(float)
    return _rolling_sum(entry, _TD_QTR)


def ois_112_intraday_down_entry_count_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of intraday moves below prior 5d minimum intraday return (entry events, 63d)."""
    intra = _intraday_ret(open, close)
    prev_min = intra.shift(1).rolling(_TD_WEEK, min_periods=1).min()
    entry = ((intra < 0) & (intra < prev_min)).astype(float)
    return _rolling_sum(entry, _TD_QTR)


def ois_113_overnight_expanding_zscore(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding all-history z-score of overnight return."""
    on = _overnight_ret(close, open)
    m = on.expanding(min_periods=5).mean()
    s = on.expanding(min_periods=5).std()
    return _safe_div(on - m, s)


def ois_114_intraday_expanding_zscore(open: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of intraday return."""
    intra = _intraday_ret(open, close)
    m = intra.expanding(min_periods=5).mean()
    s = intra.expanding(min_periods=5).std()
    return _safe_div(intra - m, s)


def ois_115_overnight_gap_expanding_pct_rank(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of overnight return."""
    on = _overnight_ret(close, open)
    return on.expanding(min_periods=5).rank(pct=True)


# --- Group K (116-125): Overnight/intraday cross-session interaction ---

def ois_116_intraday_ret_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of intraday return."""
    intra = _intraday_ret(open, close)
    return intra.expanding(min_periods=5).rank(pct=True)


def ois_117_overnight_ret_corr_intraday_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day rolling correlation between overnight and intraday returns."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    return on.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).corr(intra)


def ois_118_overnight_ret_corr_intraday_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling correlation between overnight and intraday returns."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    return on.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).corr(intra)


def ois_119_overnight_leads_intraday_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: today overnight return predicts intraday direction (both same sign today)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    return ((on < 0) & (intra < 0)).astype(float)


def ois_120_gap_down_followed_by_more_down_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gap-down days followed the NEXT day by another gap-down (21d)."""
    on = _overnight_ret(close, open)
    gap_down_today = (on < 0).astype(float)
    gap_down_next = gap_down_today.shift(-1).fillna(0)
    both = (gap_down_today * gap_down_next)
    cnt_today = _rolling_sum(gap_down_today, _TD_MON)
    cnt_both = _rolling_sum(both, _TD_MON)
    return _safe_div(cnt_both, cnt_today.replace(0, np.nan))


def ois_121_overnight_down_after_intraday_down_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of intraday-down days followed by an overnight-down next session (21d)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    intra_down = (intra < 0).astype(float)
    on_next_down = (on < 0).astype(float)
    on_down_lag = on_next_down
    intra_and_on = intra_down * on_down_lag
    cnt_intra = _rolling_sum(intra_down, _TD_MON)
    cnt_both = _rolling_sum(intra_and_on, _TD_MON)
    return _safe_div(cnt_both, cnt_intra.replace(0, np.nan))


def ois_122_overnight_skew_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of overnight returns."""
    on = _overnight_ret(close, open)
    return on.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()


def ois_123_intraday_skew_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of intraday returns."""
    intra = _intraday_ret(open, close)
    return intra.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()


def ois_124_overnight_skew_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day skewness of overnight returns."""
    on = _overnight_ret(close, open)
    return on.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def ois_125_intraday_skew_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day skewness of intraday returns."""
    intra = _intraday_ret(open, close)
    return intra.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


# --- Group L (126-135): Session return decomposition vs benchmark ---

def ois_126_overnight_ret_vs_intraday_ret_21d_beta(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day OLS slope of intraday on overnight (how much intraday follows overnight)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    cov = on.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).cov(intra)
    var_on = on.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).var()
    return _safe_div(cov, var_on.replace(0, np.nan))


def ois_127_overnight_ret_normalized_by_prior_vol(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight return normalized by prior 21-day total return std."""
    on = _overnight_ret(close, open)
    tot_std = _rolling_std(_total_ret(close), _TD_MON).shift(1)
    return _safe_div(on, tot_std.replace(0, np.nan))


def ois_128_intraday_ret_normalized_by_prior_vol(open: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday return normalized by prior 21-day total return std."""
    intra = _intraday_ret(open, close)
    tot_std = _rolling_std(close.pct_change(1), _TD_MON).shift(1)
    return _safe_div(intra, tot_std.replace(0, np.nan))


def ois_129_overnight_var_fraction_expanding(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding all-time overnight variance fraction of total daily variance."""
    on = _overnight_ret(close, open)
    tot = _total_ret(close)
    on_var = on.expanding(min_periods=10).var()
    tot_var = tot.expanding(min_periods=10).var()
    return _safe_div(on_var, tot_var.replace(0, np.nan))


def ois_130_intraday_var_fraction_expanding(open: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-time intraday variance fraction of total daily variance."""
    intra = _intraday_ret(open, close)
    tot = close.pct_change(1)
    intra_var = intra.expanding(min_periods=10).var()
    tot_var = tot.expanding(min_periods=10).var()
    return _safe_div(intra_var, tot_var.replace(0, np.nan))


def ois_131_overnight_distress_score_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative negative overnight return over 252 days (annual overnight distress)."""
    on = _overnight_ret(close, open)
    return _rolling_sum(on.clip(upper=0.0), _TD_YEAR)


def ois_132_intraday_distress_score_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative negative intraday return over 252 days (annual intraday distress)."""
    intra = _intraday_ret(open, close)
    return _rolling_sum(intra.clip(upper=0.0), _TD_YEAR)


def ois_133_overnight_gap_acceleration_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day change in overnight return (acceleration of gap movement)."""
    return _overnight_ret(close, open).diff(_TD_WEEK)


def ois_134_intraday_ret_acceleration_5d(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day change in intraday return (acceleration of intraday movement)."""
    return _intraday_ret(open, close).diff(_TD_WEEK)


def ois_135_overnight_ret_mean_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day mean of overnight return."""
    return _rolling_mean(_overnight_ret(close, open), _TD_MON)


# --- Group M (136-142): Dual-session distress composites ---

def ois_136_dual_session_distress_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: both overnight and intraday cumulative 5d returns are negative."""
    on_cum = _rolling_sum(_overnight_ret(close, open), _TD_WEEK)
    intra_cum = _rolling_sum(_intraday_ret(open, close), _TD_WEEK)
    return ((on_cum < 0) & (intra_cum < 0)).astype(float)


def ois_137_session_distress_composite_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Combined distress: sum of overnight and intraday cumulative negative returns (21d)."""
    on = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    intra = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    return on + intra


def ois_138_overnight_share_of_total_downside_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight share of total 252-day downside (abs(overnight_neg) / abs(total_neg))."""
    on = _overnight_ret(close, open)
    tot = _total_ret(close)
    on_loss = _rolling_sum(on.clip(upper=0.0).abs(), _TD_YEAR)
    tot_loss = _rolling_sum(tot.clip(upper=0.0).abs(), _TD_YEAR)
    return _safe_div(on_loss, tot_loss.replace(0, np.nan))


def ois_139_intraday_share_of_total_downside_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday share of total 252-day downside."""
    intra = _intraday_ret(open, close)
    tot = close.pct_change(1)
    intra_loss = _rolling_sum(intra.clip(upper=0.0).abs(), _TD_YEAR)
    tot_loss = _rolling_sum(tot.clip(upper=0.0).abs(), _TD_YEAR)
    return _safe_div(intra_loss, tot_loss.replace(0, np.nan))


def ois_140_overnight_ret_mean_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day mean of overnight return."""
    return _rolling_mean(_overnight_ret(close, open), _TD_QTR)


def ois_141_intraday_ret_mean_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day mean of intraday return."""
    return _rolling_mean(_intraday_ret(open, close), _TD_QTR)


def ois_142_overnight_ret_max_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day maximum overnight return (best single overnight gain)."""
    return _rolling_max(_overnight_ret(close, open), _TD_MON)


# --- Group N (143-150): Distress composites, pct ranks, normalized ---

def ois_143_overnight_distress_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21d overnight distress score within 252-day distribution."""
    score = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_144_intraday_distress_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 21d intraday distress score within 252-day distribution."""
    score = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_145_overnight_reversal_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-down -> intraday-up reversal events in 63 days."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    reversal = ((on < 0) & (intra > 0)).astype(float)
    return _rolling_sum(reversal, _TD_QTR)


def ois_146_intraday_reversal_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-up -> intraday-down reversal events in 63 days."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    reversal = ((on > 0) & (intra < 0)).astype(float)
    return _rolling_sum(reversal, _TD_QTR)


def ois_147_overnight_vs_intraday_cumret_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of cumulative overnight to cumulative intraday return (63d)."""
    on_cum = _rolling_sum(_overnight_ret(close, open), _TD_QTR)
    intra_cum = _rolling_sum(_intraday_ret(open, close), _TD_QTR)
    return _safe_div(on_cum, intra_cum.replace(0, np.nan))


def ois_148_overnight_intraday_cumret_composite_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of cumulative overnight and intraday returns over 63 days (total session sum)."""
    on_cum = _rolling_sum(_overnight_ret(close, open), _TD_QTR)
    intra_cum = _rolling_sum(_intraday_ret(open, close), _TD_QTR)
    return on_cum + intra_cum


def ois_149_overnight_negative_frac_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of days with negative overnight return over trailing 252 days."""
    on = _overnight_ret(close, open)
    return _rolling_sum((on < 0).astype(float), _TD_YEAR) / _TD_YEAR


def ois_150_intraday_negative_frac_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of days with negative intraday return over trailing 252 days."""
    intra = _intraday_ret(open, close)
    return _rolling_sum((intra < 0).astype(float), _TD_YEAR) / _TD_YEAR


# ── Registry ──────────────────────────────────────────────────────────────────

OVERNIGHT_INTRADAY_SPLIT_REGISTRY_076_150 = {
    "ois_076_vol_weighted_overnight_ret_21d": {"inputs": ["close", "open", "volume"], "func": ois_076_vol_weighted_overnight_ret_21d},
    "ois_077_vol_weighted_intraday_ret_21d": {"inputs": ["open", "close", "volume"], "func": ois_077_vol_weighted_intraday_ret_21d},
    "ois_078_vol_weighted_overnight_ret_63d": {"inputs": ["close", "open", "volume"], "func": ois_078_vol_weighted_overnight_ret_63d},
    "ois_079_vol_weighted_intraday_ret_63d": {"inputs": ["open", "close", "volume"], "func": ois_079_vol_weighted_intraday_ret_63d},
    "ois_080_high_volume_overnight_down_frac_21d": {"inputs": ["close", "open", "volume"], "func": ois_080_high_volume_overnight_down_frac_21d},
    "ois_081_high_volume_intraday_down_frac_21d": {"inputs": ["open", "close", "volume"], "func": ois_081_high_volume_intraday_down_frac_21d},
    "ois_082_overnight_down_volume_share_21d": {"inputs": ["close", "open", "volume"], "func": ois_082_overnight_down_volume_share_21d},
    "ois_083_intraday_down_volume_share_21d": {"inputs": ["open", "close", "volume"], "func": ois_083_intraday_down_volume_share_21d},
    "ois_084_overnight_ret_volume_corr_21d": {"inputs": ["close", "open", "volume"], "func": ois_084_overnight_ret_volume_corr_21d},
    "ois_085_intraday_ret_volume_corr_21d": {"inputs": ["open", "close", "volume"], "func": ois_085_intraday_ret_volume_corr_21d},
    "ois_086_overnight_ret_volume_corr_63d": {"inputs": ["close", "open", "volume"], "func": ois_086_overnight_ret_volume_corr_63d},
    "ois_087_intraday_ret_volume_corr_63d": {"inputs": ["open", "close", "volume"], "func": ois_087_intraday_ret_volume_corr_63d},
    "ois_088_overnight_negative_volume_intensity_21d": {"inputs": ["close", "open", "volume"], "func": ois_088_overnight_negative_volume_intensity_21d},
    "ois_089_intraday_negative_volume_intensity_21d": {"inputs": ["open", "close", "volume"], "func": ois_089_intraday_negative_volume_intensity_21d},
    "ois_090_overnight_vs_intraday_volume_intensity_ratio_21d": {"inputs": ["close", "open", "volume"], "func": ois_090_overnight_vs_intraday_volume_intensity_ratio_21d},
    "ois_091_ewm_overnight_ret_span21": {"inputs": ["close", "open"], "func": ois_091_ewm_overnight_ret_span21},
    "ois_092_ewm_intraday_ret_span21": {"inputs": ["open", "close"], "func": ois_092_ewm_intraday_ret_span21},
    "ois_093_ewm_overnight_ret_span63": {"inputs": ["close", "open"], "func": ois_093_ewm_overnight_ret_span63},
    "ois_094_ewm_intraday_ret_span63": {"inputs": ["open", "close"], "func": ois_094_ewm_intraday_ret_span63},
    "ois_095_overnight_ret_slope_21d": {"inputs": ["close", "open"], "func": ois_095_overnight_ret_slope_21d},
    "ois_096_intraday_ret_slope_21d": {"inputs": ["open", "close"], "func": ois_096_intraday_ret_slope_21d},
    "ois_097_overnight_ret_slope_63d": {"inputs": ["close", "open"], "func": ois_097_overnight_ret_slope_63d},
    "ois_098_intraday_ret_slope_63d": {"inputs": ["open", "close"], "func": ois_098_intraday_ret_slope_63d},
    "ois_099_overnight_ret_ewm_vs_mean_ratio_21d": {"inputs": ["close", "open"], "func": ois_099_overnight_ret_ewm_vs_mean_ratio_21d},
    "ois_100_intraday_ret_ewm_vs_mean_ratio_21d": {"inputs": ["open", "close"], "func": ois_100_intraday_ret_ewm_vs_mean_ratio_21d},
    "ois_101_overnight_negative_streak_max_63d": {"inputs": ["close", "open"], "func": ois_101_overnight_negative_streak_max_63d},
    "ois_102_intraday_negative_streak_max_63d": {"inputs": ["open", "close"], "func": ois_102_intraday_negative_streak_max_63d},
    "ois_103_overnight_gap_min_21d": {"inputs": ["close", "open"], "func": ois_103_overnight_gap_min_21d},
    "ois_104_overnight_gap_min_63d": {"inputs": ["close", "open"], "func": ois_104_overnight_gap_min_63d},
    "ois_105_intraday_ret_min_21d": {"inputs": ["open", "close"], "func": ois_105_intraday_ret_min_21d},
    "ois_106_intraday_ret_min_63d": {"inputs": ["open", "close"], "func": ois_106_intraday_ret_min_63d},
    "ois_107_overnight_gap_normalized_by_atr": {"inputs": ["close", "open", "high", "low"], "func": ois_107_overnight_gap_normalized_by_atr},
    "ois_108_intraday_range_normalized_by_atr": {"inputs": ["open", "close", "high", "low"], "func": ois_108_intraday_range_normalized_by_atr},
    "ois_109_overnight_gap_down_size_mean_21d": {"inputs": ["close", "open"], "func": ois_109_overnight_gap_down_size_mean_21d},
    "ois_110_intraday_down_size_mean_21d": {"inputs": ["open", "close"], "func": ois_110_intraday_down_size_mean_21d},
    "ois_111_overnight_gap_down_entry_count_63d": {"inputs": ["close", "open"], "func": ois_111_overnight_gap_down_entry_count_63d},
    "ois_112_intraday_down_entry_count_63d": {"inputs": ["open", "close"], "func": ois_112_intraday_down_entry_count_63d},
    "ois_113_overnight_expanding_zscore": {"inputs": ["close", "open"], "func": ois_113_overnight_expanding_zscore},
    "ois_114_intraday_expanding_zscore": {"inputs": ["open", "close"], "func": ois_114_intraday_expanding_zscore},
    "ois_115_overnight_gap_expanding_pct_rank": {"inputs": ["close", "open"], "func": ois_115_overnight_gap_expanding_pct_rank},
    "ois_116_intraday_ret_pct_rank_252d": {"inputs": ["open", "close"], "func": ois_116_intraday_ret_pct_rank_252d},
    "ois_117_overnight_ret_corr_intraday_21d": {"inputs": ["close", "open"], "func": ois_117_overnight_ret_corr_intraday_21d},
    "ois_118_overnight_ret_corr_intraday_63d": {"inputs": ["close", "open"], "func": ois_118_overnight_ret_corr_intraday_63d},
    "ois_119_overnight_leads_intraday_flag": {"inputs": ["close", "open"], "func": ois_119_overnight_leads_intraday_flag},
    "ois_120_gap_down_followed_by_more_down_frac_21d": {"inputs": ["close", "open"], "func": ois_120_gap_down_followed_by_more_down_frac_21d},
    "ois_121_overnight_down_after_intraday_down_frac_21d": {"inputs": ["close", "open"], "func": ois_121_overnight_down_after_intraday_down_frac_21d},
    "ois_122_overnight_skew_21d": {"inputs": ["close", "open"], "func": ois_122_overnight_skew_21d},
    "ois_123_intraday_skew_21d": {"inputs": ["open", "close"], "func": ois_123_intraday_skew_21d},
    "ois_124_overnight_skew_63d": {"inputs": ["close", "open"], "func": ois_124_overnight_skew_63d},
    "ois_125_intraday_skew_63d": {"inputs": ["open", "close"], "func": ois_125_intraday_skew_63d},
    "ois_126_overnight_ret_vs_intraday_ret_21d_beta": {"inputs": ["close", "open"], "func": ois_126_overnight_ret_vs_intraday_ret_21d_beta},
    "ois_127_overnight_ret_normalized_by_prior_vol": {"inputs": ["close", "open"], "func": ois_127_overnight_ret_normalized_by_prior_vol},
    "ois_128_intraday_ret_normalized_by_prior_vol": {"inputs": ["open", "close"], "func": ois_128_intraday_ret_normalized_by_prior_vol},
    "ois_129_overnight_var_fraction_expanding": {"inputs": ["close", "open"], "func": ois_129_overnight_var_fraction_expanding},
    "ois_130_intraday_var_fraction_expanding": {"inputs": ["open", "close"], "func": ois_130_intraday_var_fraction_expanding},
    "ois_131_overnight_distress_score_252d": {"inputs": ["close", "open"], "func": ois_131_overnight_distress_score_252d},
    "ois_132_intraday_distress_score_252d": {"inputs": ["open", "close"], "func": ois_132_intraday_distress_score_252d},
    "ois_133_overnight_gap_acceleration_5d": {"inputs": ["close", "open"], "func": ois_133_overnight_gap_acceleration_5d},
    "ois_134_intraday_ret_acceleration_5d": {"inputs": ["open", "close"], "func": ois_134_intraday_ret_acceleration_5d},
    "ois_135_overnight_ret_mean_21d": {"inputs": ["close", "open"], "func": ois_135_overnight_ret_mean_21d},
    "ois_136_dual_session_distress_flag": {"inputs": ["close", "open"], "func": ois_136_dual_session_distress_flag},
    "ois_137_session_distress_composite_21d": {"inputs": ["close", "open"], "func": ois_137_session_distress_composite_21d},
    "ois_138_overnight_share_of_total_downside_252d": {"inputs": ["close", "open"], "func": ois_138_overnight_share_of_total_downside_252d},
    "ois_139_intraday_share_of_total_downside_252d": {"inputs": ["open", "close"], "func": ois_139_intraday_share_of_total_downside_252d},
    "ois_140_overnight_ret_mean_63d": {"inputs": ["close", "open"], "func": ois_140_overnight_ret_mean_63d},
    "ois_141_intraday_ret_mean_63d": {"inputs": ["open", "close"], "func": ois_141_intraday_ret_mean_63d},
    "ois_142_overnight_ret_max_21d": {"inputs": ["close", "open"], "func": ois_142_overnight_ret_max_21d},
    "ois_143_overnight_distress_pct_rank_252d": {"inputs": ["close", "open"], "func": ois_143_overnight_distress_pct_rank_252d},
    "ois_144_intraday_distress_pct_rank_252d": {"inputs": ["open", "close"], "func": ois_144_intraday_distress_pct_rank_252d},
    "ois_145_overnight_reversal_count_63d": {"inputs": ["close", "open"], "func": ois_145_overnight_reversal_count_63d},
    "ois_146_intraday_reversal_count_63d": {"inputs": ["close", "open"], "func": ois_146_intraday_reversal_count_63d},
    "ois_147_overnight_vs_intraday_cumret_ratio_63d": {"inputs": ["close", "open"], "func": ois_147_overnight_vs_intraday_cumret_ratio_63d},
    "ois_148_overnight_intraday_cumret_composite_63d": {"inputs": ["close", "open"], "func": ois_148_overnight_intraday_cumret_composite_63d},
    "ois_149_overnight_negative_frac_252d": {"inputs": ["close", "open"], "func": ois_149_overnight_negative_frac_252d},
    "ois_150_intraday_negative_frac_252d": {"inputs": ["open", "close"], "func": ois_150_intraday_negative_frac_252d},
}
