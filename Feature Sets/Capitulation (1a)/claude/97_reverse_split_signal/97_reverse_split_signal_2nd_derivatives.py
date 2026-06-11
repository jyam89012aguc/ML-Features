"""
97_reverse_split_signal — 2nd-Derivative Features 001-075
Domain: rate of change (acceleration) of base reverse-split-signal features
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to one shared daily
trading-day index.  The 2nd-derivative series are sparse/stepwise on a
daily index because the underlying split_factor data is event-driven —
this is correct and expected.  Functions look strictly backward using
.shift(positive), .rolling(), or .expanding().

  split_factor  : per-day split factor; 1.0 on normal days.
                  < 1.0 on reverse-split effective dates.
                  > 1.0 on forward-split effective dates.
  closeunadj    : raw unadjusted daily close price (USD).
  close         : split/dividend-adjusted daily close price (USD).
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_TD_2Q    = 126
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of denominator."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# These inline the relevant base computations so this file needs no cross-import.

def _is_reverse_split(split_factor: pd.Series) -> pd.Series:
    return (split_factor < 1.0).astype(float)


def _is_forward_split(split_factor: pd.Series) -> pd.Series:
    return (split_factor > 1.0).astype(float)


def _reverse_split_magnitude(split_factor: pd.Series) -> pd.Series:
    rs = split_factor.copy().astype(float)
    rs[rs >= 1.0] = np.nan
    return 1.0 / rs.replace(0, np.nan)


def _rs_count_252d(split_factor: pd.Series) -> pd.Series:
    return _rolling_sum(_is_reverse_split(split_factor), _TD_YEAR)


def _rs_count_63d(split_factor: pd.Series) -> pd.Series:
    return _rolling_sum(_is_reverse_split(split_factor), _TD_QTR)


def _rs_recency_decay_63(split_factor: pd.Series) -> pd.Series:
    return _ewm_mean(_is_reverse_split(split_factor), _TD_QTR)


def _rs_recency_decay_252(split_factor: pd.Series) -> pd.Series:
    return _ewm_mean(_is_reverse_split(split_factor), _TD_YEAR)


def _cumulative_rs_log_252(split_factor: pd.Series) -> pd.Series:
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return _rolling_sum(log_sf, _TD_YEAR)


def _closeunadj_log(closeunadj: pd.Series) -> pd.Series:
    return np.log(closeunadj.clip(lower=_EPS))


def _close_log(close: pd.Series) -> pd.Series:
    return np.log(close.clip(lower=_EPS))


def _closeunadj_pct_drawdown_252(closeunadj: pd.Series) -> pd.Series:
    peak = _rolling_max(closeunadj, _TD_YEAR)
    return _safe_div_abs(closeunadj - peak, peak)


def _close_pct_drawdown_252(close: pd.Series) -> pd.Series:
    peak = _rolling_max(close, _TD_YEAR)
    return _safe_div_abs(close - peak, peak)


def _below1_frac_252(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_YEAR)


def _below5_frac_252(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 5.0).astype(float), _TD_YEAR)


def _rs_severity_ewm63(split_factor: pd.Series) -> pd.Series:
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _ewm_mean(mag, _TD_QTR)


def _rs_cluster_density_252(split_factor: pd.Series) -> pd.Series:
    return _rolling_mean(_is_reverse_split(split_factor), _TD_YEAR)


def _closeunadj_zscore_252(closeunadj: pd.Series) -> pd.Series:
    m  = _rolling_mean(closeunadj, _TD_YEAR)
    sd = _rolling_std(closeunadj, _TD_YEAR)
    return _safe_div(closeunadj - m, sd)


def _close_zscore_252(close: pd.Series) -> pd.Series:
    m  = _rolling_mean(close, _TD_YEAR)
    sd = _rolling_std(close, _TD_YEAR)
    return _safe_div(close - m, sd)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def rss_drv2_001_rs_count_252d_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the RS count over trailing 252 days (monthly acceleration)."""
    base = _rs_count_252d(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_002_rs_count_252d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the RS count over trailing 252 days (quarterly acceleration)."""
    base = _rs_count_252d(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_003_rs_count_63d_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the 63-day RS count (short-horizon acceleration)."""
    base = _rs_count_63d(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_004_rs_recency_decay63_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the EWM-63 recency decay of RS flag."""
    base = _rs_recency_decay_63(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_005_rs_recency_decay252_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the EWM-252 recency decay of RS flag."""
    base = _rs_recency_decay_252(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_006_cumulative_rs_log_252d_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in log-cumulative RS factor over 252 days."""
    base = _cumulative_rs_log_252(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_007_closeunadj_log_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in log unadjusted close (log-return over 21 days)."""
    base = _closeunadj_log(closeunadj)
    return base - base.shift(_TD_MO)


def rss_drv2_008_closeunadj_log_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in log unadjusted close."""
    base = _closeunadj_log(closeunadj)
    return base - base.shift(_TD_QTR)


def rss_drv2_009_closeunadj_pct_drawdown_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 252-day percent drawdown of unadjusted close."""
    base = _closeunadj_pct_drawdown_252(closeunadj)
    return base - base.shift(_TD_MO)


def rss_drv2_010_closeunadj_pct_drawdown_252d_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 252-day percent drawdown of unadjusted close."""
    base = _closeunadj_pct_drawdown_252(closeunadj)
    return base - base.shift(_TD_QTR)


def rss_drv2_011_close_pct_drawdown_252d_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the 252-day percent drawdown of adjusted close."""
    base = _close_pct_drawdown_252(close)
    return base - base.shift(_TD_MO)


def rss_drv2_012_below1_frac_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the fraction of days below $1 in trailing 252 days."""
    base = _below1_frac_252(closeunadj)
    return base - base.shift(_TD_MO)


def rss_drv2_013_below5_frac_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the fraction of days below $5 in trailing 252 days."""
    base = _below5_frac_252(closeunadj)
    return base - base.shift(_TD_MO)


def rss_drv2_014_rs_severity_ewm63_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in EWM-63 reverse-split magnitude signal."""
    base = _rs_severity_ewm63(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_015_rs_cluster_density_252d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in RS cluster density over 252-day window."""
    base = _rs_cluster_density_252(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_016_closeunadj_zscore_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 252-day z-score of unadjusted close."""
    base = _closeunadj_zscore_252(closeunadj)
    return base - base.shift(_TD_MO)


def rss_drv2_017_close_zscore_252d_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the 252-day z-score of adjusted close."""
    base = _close_zscore_252(close)
    return base - base.shift(_TD_MO)


def rss_drv2_018_rs_count_252d_yoy_diff(split_factor: pd.Series) -> pd.Series:
    """252-day (YoY) change in the trailing 252-day RS count."""
    base = _rs_count_252d(split_factor)
    return base - base.shift(_TD_YEAR)


def rss_drv2_019_closeunadj_log_yoy_diff(closeunadj: pd.Series) -> pd.Series:
    """252-day change in log unadjusted close (YoY log-return)."""
    base = _closeunadj_log(closeunadj)
    return base - base.shift(_TD_YEAR)


def rss_drv2_020_close_log_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in log adjusted close."""
    base = _close_log(close)
    return base - base.shift(_TD_MO)


def rss_drv2_021_close_log_qtr_diff(close: pd.Series) -> pd.Series:
    """63-day change in log adjusted close."""
    base = _close_log(close)
    return base - base.shift(_TD_QTR)


def rss_drv2_022_rs_recency_decay63_slope_252d(split_factor: pd.Series) -> pd.Series:
    """
    Rolling 252-day OLS slope of EWM-63 RS recency-decay series.
    Captures the trend in how quickly RS recency is growing/fading.
    """
    base = _rs_recency_decay_63(split_factor)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def rss_drv2_023_below1_frac_252d_ewm_diff(closeunadj: pd.Series) -> pd.Series:
    """
    Current below-$1 fraction (252d) minus its EWM (span=252):
    measures whether the fraction is rising above its own trend.
    """
    base = _below1_frac_252(closeunadj)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def rss_drv2_024_closeunadj_pct_drawdown_252d_ewm_diff(closeunadj: pd.Series) -> pd.Series:
    """
    Current 252d pct drawdown of unadjusted close minus its EWM (span=63):
    measures if drawdown is accelerating beyond recent trend.
    """
    base = _closeunadj_pct_drawdown_252(closeunadj)
    ewm  = base.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return base - ewm


def rss_drv2_025_rs_composite_distress_mo_diff(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """
    21-day change in the composite distress score:
    (RS-within-252d flag + sub-$5 flag + below-$1 fraction 252d +
     expanding RS count clipped/5 + 252d pct drawdown of closeunadj) / 5.
    """
    def _composite(sf, cu):
        rs252  = (_rolling_sum(_is_reverse_split(sf), _TD_YEAR) > 0).astype(float)
        sub5   = (cu < 5.0).astype(float)
        frac1  = _rolling_mean((cu < 1.0).astype(float), _TD_YEAR)
        cnt_rs = (_is_reverse_split(sf).expanding(min_periods=1).sum().clip(upper=5) / 5.0)
        peak   = _rolling_max(cu, _TD_YEAR)
        dd     = _safe_div_abs(cu - peak, peak).abs().clip(upper=1.0)
        return (rs252 + sub5 + frac1 + cnt_rs + dd) / 5.0

    base = _composite(split_factor, closeunadj)
    return base - base.shift(_TD_MO)


# ── Additional base helpers for drv2 026-075 ─────────────────────────────────

def _rs_count_126d(split_factor: pd.Series) -> pd.Series:
    return _rolling_sum(_is_reverse_split(split_factor), _TD_2Q)


def _rs_count_504d(split_factor: pd.Series) -> pd.Series:
    return _rolling_sum(_is_reverse_split(split_factor), _TD_2Y)


def _rs_severity_ewm252(split_factor: pd.Series) -> pd.Series:
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _ewm_mean(mag, _TD_YEAR)


def _cumulative_rs_log_504(split_factor: pd.Series) -> pd.Series:
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return _rolling_sum(log_sf, _TD_2Y)


def _closeunadj_pct_drawdown_504(closeunadj: pd.Series) -> pd.Series:
    peak = _rolling_max(closeunadj, _TD_2Y)
    return _safe_div_abs(closeunadj - peak, peak)


def _close_pct_drawdown_504(close: pd.Series) -> pd.Series:
    peak = _rolling_max(close, _TD_2Y)
    return _safe_div_abs(close - peak, peak)


def _below2_frac_252(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 2.0).astype(float), _TD_YEAR)


def _close_pct_rank_252(close: pd.Series) -> pd.Series:
    return close.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def _closeunadj_pct_rank_252(closeunadj: pd.Series) -> pd.Series:
    return closeunadj.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def _close_zscore_504(close: pd.Series) -> pd.Series:
    m  = _rolling_mean(close, _TD_2Y)
    sd = _rolling_std(close, _TD_2Y)
    return _safe_div(close - m, sd)


def _closeunadj_zscore_504(closeunadj: pd.Series) -> pd.Series:
    m  = _rolling_mean(closeunadj, _TD_2Y)
    sd = _rolling_std(closeunadj, _TD_2Y)
    return _safe_div(closeunadj - m, sd)


def _rs_cluster_density_63(split_factor: pd.Series) -> pd.Series:
    return _rolling_mean(_is_reverse_split(split_factor), _TD_QTR)


def _rs_magnitude_sum_252(split_factor: pd.Series) -> pd.Series:
    mag = _reverse_split_magnitude(split_factor).fillna(0.0)
    return _rolling_sum(mag, _TD_YEAR)


# ── 2nd-derivative feature functions 026-075 ─────────────────────────────────

def rss_drv2_026_rs_count_504d_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the RS count over trailing 504 days."""
    base = _rs_count_504d(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_027_rs_count_504d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the RS count over trailing 504 days."""
    base = _rs_count_504d(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_028_rs_count_126d_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the 126-day RS count."""
    base = _rs_count_126d(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_029_rs_count_126d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the 126-day RS count."""
    base = _rs_count_126d(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_030_rs_severity_ewm252_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in EWM-252 reverse-split magnitude signal."""
    base = _rs_severity_ewm252(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_031_cumulative_rs_log_504d_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in log-cumulative RS factor over 504 days."""
    base = _cumulative_rs_log_504(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_032_cumulative_rs_log_504d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in log-cumulative RS factor over 504 days."""
    base = _cumulative_rs_log_504(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_033_closeunadj_pct_drawdown_504d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 504-day pct drawdown of unadjusted close."""
    base = _closeunadj_pct_drawdown_504(closeunadj)
    return base - base.shift(_TD_MO)


def rss_drv2_034_closeunadj_pct_drawdown_504d_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 504-day pct drawdown of unadjusted close."""
    base = _closeunadj_pct_drawdown_504(closeunadj)
    return base - base.shift(_TD_QTR)


def rss_drv2_035_close_pct_drawdown_504d_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the 504-day pct drawdown of adjusted close."""
    base = _close_pct_drawdown_504(close)
    return base - base.shift(_TD_MO)


def rss_drv2_036_close_pct_drawdown_504d_qtr_diff(close: pd.Series) -> pd.Series:
    """63-day change in the 504-day pct drawdown of adjusted close."""
    base = _close_pct_drawdown_504(close)
    return base - base.shift(_TD_QTR)


def rss_drv2_037_below2_frac_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the fraction of days below $2 in trailing 252 days."""
    base = _below2_frac_252(closeunadj)
    return base - base.shift(_TD_MO)


def rss_drv2_038_below2_frac_252d_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the fraction of days below $2 in trailing 252 days."""
    base = _below2_frac_252(closeunadj)
    return base - base.shift(_TD_QTR)


def rss_drv2_039_below1_frac_252d_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the fraction of days below $1 in trailing 252 days."""
    base = _below1_frac_252(closeunadj)
    return base - base.shift(_TD_QTR)


def rss_drv2_040_below5_frac_252d_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the fraction of days below $5 in trailing 252 days."""
    base = _below5_frac_252(closeunadj)
    return base - base.shift(_TD_QTR)


def rss_drv2_041_close_pct_rank_252d_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the percentile rank of adjusted close (252d window)."""
    base = _close_pct_rank_252(close)
    return base - base.shift(_TD_MO)


def rss_drv2_042_closeunadj_pct_rank_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the percentile rank of unadjusted close (252d window)."""
    base = _closeunadj_pct_rank_252(closeunadj)
    return base - base.shift(_TD_MO)


def rss_drv2_043_close_pct_rank_252d_qtr_diff(close: pd.Series) -> pd.Series:
    """63-day change in the percentile rank of adjusted close (252d window)."""
    base = _close_pct_rank_252(close)
    return base - base.shift(_TD_QTR)


def rss_drv2_044_closeunadj_pct_rank_252d_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the percentile rank of unadjusted close (252d window)."""
    base = _closeunadj_pct_rank_252(closeunadj)
    return base - base.shift(_TD_QTR)


def rss_drv2_045_close_zscore_504d_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the 504-day z-score of adjusted close."""
    base = _close_zscore_504(close)
    return base - base.shift(_TD_MO)


def rss_drv2_046_closeunadj_zscore_504d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 504-day z-score of unadjusted close."""
    base = _closeunadj_zscore_504(closeunadj)
    return base - base.shift(_TD_MO)


def rss_drv2_047_rs_cluster_density_63d_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in RS cluster density over 63-day window."""
    base = _rs_cluster_density_63(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_048_rs_cluster_density_63d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in RS cluster density over 63-day window."""
    base = _rs_cluster_density_63(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_049_rs_cluster_density_252d_yoy_diff(split_factor: pd.Series) -> pd.Series:
    """252-day change in RS cluster density over 252-day window."""
    base = _rs_cluster_density_252(split_factor)
    return base - base.shift(_TD_YEAR)


def rss_drv2_050_rs_magnitude_sum_252d_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in sum of RS magnitudes over trailing 252 days."""
    base = _rs_magnitude_sum_252(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_051_rs_magnitude_sum_252d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in sum of RS magnitudes over trailing 252 days."""
    base = _rs_magnitude_sum_252(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_052_closeunadj_log_wk_diff(closeunadj: pd.Series) -> pd.Series:
    """5-day change in log unadjusted close (weekly log-return)."""
    base = _closeunadj_log(closeunadj)
    return base - base.shift(_TD_WK)


def rss_drv2_053_close_log_wk_diff(close: pd.Series) -> pd.Series:
    """5-day change in log adjusted close (weekly log-return)."""
    base = _close_log(close)
    return base - base.shift(_TD_WK)


def rss_drv2_054_closeunadj_pct_drawdown_252d_wk_diff(closeunadj: pd.Series) -> pd.Series:
    """5-day change in the 252-day pct drawdown of unadjusted close."""
    base = _closeunadj_pct_drawdown_252(closeunadj)
    return base - base.shift(_TD_WK)


def rss_drv2_055_close_pct_drawdown_252d_wk_diff(close: pd.Series) -> pd.Series:
    """5-day change in the 252-day pct drawdown of adjusted close."""
    base = _close_pct_drawdown_252(close)
    return base - base.shift(_TD_WK)


def rss_drv2_056_closeunadj_zscore_252d_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 252-day z-score of unadjusted close."""
    base = _closeunadj_zscore_252(closeunadj)
    return base - base.shift(_TD_QTR)


def rss_drv2_057_close_zscore_252d_qtr_diff(close: pd.Series) -> pd.Series:
    """63-day change in the 252-day z-score of adjusted close."""
    base = _close_zscore_252(close)
    return base - base.shift(_TD_QTR)


def rss_drv2_058_rs_recency_decay63_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the EWM-63 RS recency decay signal."""
    base = _rs_recency_decay_63(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_059_rs_recency_decay252_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the EWM-252 RS recency decay signal."""
    base = _rs_recency_decay_252(split_factor)
    return base - base.shift(_TD_MO)


def rss_drv2_060_cumulative_rs_log_252d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in log-cumulative RS factor over 252 days."""
    base = _cumulative_rs_log_252(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_061_rs_count_252d_mo_diff_slope_63d(split_factor: pd.Series) -> pd.Series:
    """Rolling 63-day OLS slope of the 21d-diff of 252d RS count (short-horizon trend)."""
    base = _rs_count_252d(split_factor)
    d2   = base - base.shift(_TD_MO)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0 else ((x - xm) * (arr - ym)).sum() / denom

    return d2.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def rss_drv2_062_closeunadj_pct_drawdown_252d_slope_63d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 63-day OLS slope of the 252d unadjusted pct drawdown series."""
    base = _closeunadj_pct_drawdown_252(closeunadj)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def rss_drv2_063_below1_frac_252d_slope_63d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 63-day OLS slope of the below-$1 fraction (252d) series."""
    base = _below1_frac_252(closeunadj)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def rss_drv2_064_close_zscore_252d_slope_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day OLS slope of the 252d z-score of adjusted close."""
    base = _close_zscore_252(close)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def rss_drv2_065_closeunadj_log_yoy_ewm_diff(closeunadj: pd.Series) -> pd.Series:
    """YoY log-return of unadjusted close minus its EWM (span=252); trend-adjusted YoY momentum."""
    base = _closeunadj_log(closeunadj)
    yoy  = base - base.shift(_TD_YEAR)
    ewm  = yoy.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return yoy - ewm


def rss_drv2_066_rs_count_252d_ewm_diff(split_factor: pd.Series) -> pd.Series:
    """252d RS count minus its EWM (span=252); measures whether RS count is above trend."""
    base = _rs_count_252d(split_factor)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def rss_drv2_067_rs_severity_ewm63_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in EWM-63 RS severity signal."""
    base = _rs_severity_ewm63(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_068_rs_severity_ewm252_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in EWM-252 RS severity signal."""
    base = _rs_severity_ewm252(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_069_closeunadj_zscore_252d_ewm_diff(closeunadj: pd.Series) -> pd.Series:
    """252d z-score of unadjusted close minus its EWM (span=63); momentum of z-score."""
    base = _closeunadj_zscore_252(closeunadj)
    ewm  = base.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return base - ewm


def rss_drv2_070_close_log_yoy_diff(close: pd.Series) -> pd.Series:
    """252-day change in log adjusted close (YoY log-return of adjusted close)."""
    base = _close_log(close)
    return base - base.shift(_TD_YEAR)


def rss_drv2_071_rs_count_63d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the 63-day RS count."""
    base = _rs_count_63d(split_factor)
    return base - base.shift(_TD_QTR)


def rss_drv2_072_rs_count_252d_yoy_ewm_diff(split_factor: pd.Series) -> pd.Series:
    """YoY RS count diff minus its EWM (span=63); trend-adjusted RS acceleration."""
    base = _rs_count_252d(split_factor)
    yoy  = base - base.shift(_TD_YEAR)
    ewm  = yoy.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return yoy - ewm


def rss_drv2_073_below1_frac_252d_yoy_diff(closeunadj: pd.Series) -> pd.Series:
    """252-day change in the below-$1 fraction (252d) — YoY acceleration of sub-$1 persistence."""
    base = _below1_frac_252(closeunadj)
    return base - base.shift(_TD_YEAR)


def rss_drv2_074_closeunadj_pct_drawdown_252d_yoy_diff(closeunadj: pd.Series) -> pd.Series:
    """252-day change in the 252d pct drawdown of unadjusted close."""
    base = _closeunadj_pct_drawdown_252(closeunadj)
    return base - base.shift(_TD_YEAR)


def rss_drv2_075_rs_composite_distress_qtr_diff(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """63-day change in composite distress score (RS-within-252d + sub-$5 + below-$1 frac + clipped RS/5 + 252d dd) / 5."""
    def _composite(sf, cu):
        rs252  = (_rolling_sum(_is_reverse_split(sf), _TD_YEAR) > 0).astype(float)
        sub5   = (cu < 5.0).astype(float)
        frac1  = _rolling_mean((cu < 1.0).astype(float), _TD_YEAR)
        cnt_rs = (_is_reverse_split(sf).expanding(min_periods=1).sum().clip(upper=5) / 5.0)
        peak   = _rolling_max(cu, _TD_YEAR)
        dd     = _safe_div_abs(cu - peak, peak).abs().clip(upper=1.0)
        return (rs252 + sub5 + frac1 + cnt_rs + dd) / 5.0

    base = _composite(split_factor, closeunadj)
    return base - base.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

REVERSE_SPLIT_SIGNAL_REGISTRY_2ND_DERIVATIVES = {
    "rss_drv2_001_rs_count_252d_mo_diff":                 {"inputs": ["split_factor"],              "func": rss_drv2_001_rs_count_252d_mo_diff},
    "rss_drv2_002_rs_count_252d_qtr_diff":                {"inputs": ["split_factor"],              "func": rss_drv2_002_rs_count_252d_qtr_diff},
    "rss_drv2_003_rs_count_63d_mo_diff":                  {"inputs": ["split_factor"],              "func": rss_drv2_003_rs_count_63d_mo_diff},
    "rss_drv2_004_rs_recency_decay63_mo_diff":            {"inputs": ["split_factor"],              "func": rss_drv2_004_rs_recency_decay63_mo_diff},
    "rss_drv2_005_rs_recency_decay252_qtr_diff":          {"inputs": ["split_factor"],              "func": rss_drv2_005_rs_recency_decay252_qtr_diff},
    "rss_drv2_006_cumulative_rs_log_252d_mo_diff":        {"inputs": ["split_factor"],              "func": rss_drv2_006_cumulative_rs_log_252d_mo_diff},
    "rss_drv2_007_closeunadj_log_mo_diff":                {"inputs": ["closeunadj"],                "func": rss_drv2_007_closeunadj_log_mo_diff},
    "rss_drv2_008_closeunadj_log_qtr_diff":               {"inputs": ["closeunadj"],                "func": rss_drv2_008_closeunadj_log_qtr_diff},
    "rss_drv2_009_closeunadj_pct_drawdown_252d_mo_diff":  {"inputs": ["closeunadj"],                "func": rss_drv2_009_closeunadj_pct_drawdown_252d_mo_diff},
    "rss_drv2_010_closeunadj_pct_drawdown_252d_qtr_diff": {"inputs": ["closeunadj"],                "func": rss_drv2_010_closeunadj_pct_drawdown_252d_qtr_diff},
    "rss_drv2_011_close_pct_drawdown_252d_mo_diff":       {"inputs": ["close"],                     "func": rss_drv2_011_close_pct_drawdown_252d_mo_diff},
    "rss_drv2_012_below1_frac_252d_mo_diff":              {"inputs": ["closeunadj"],                "func": rss_drv2_012_below1_frac_252d_mo_diff},
    "rss_drv2_013_below5_frac_252d_mo_diff":              {"inputs": ["closeunadj"],                "func": rss_drv2_013_below5_frac_252d_mo_diff},
    "rss_drv2_014_rs_severity_ewm63_mo_diff":             {"inputs": ["split_factor"],              "func": rss_drv2_014_rs_severity_ewm63_mo_diff},
    "rss_drv2_015_rs_cluster_density_252d_qtr_diff":      {"inputs": ["split_factor"],              "func": rss_drv2_015_rs_cluster_density_252d_qtr_diff},
    "rss_drv2_016_closeunadj_zscore_252d_mo_diff":        {"inputs": ["closeunadj"],                "func": rss_drv2_016_closeunadj_zscore_252d_mo_diff},
    "rss_drv2_017_close_zscore_252d_mo_diff":             {"inputs": ["close"],                     "func": rss_drv2_017_close_zscore_252d_mo_diff},
    "rss_drv2_018_rs_count_252d_yoy_diff":                {"inputs": ["split_factor"],              "func": rss_drv2_018_rs_count_252d_yoy_diff},
    "rss_drv2_019_closeunadj_log_yoy_diff":               {"inputs": ["closeunadj"],                "func": rss_drv2_019_closeunadj_log_yoy_diff},
    "rss_drv2_020_close_log_mo_diff":                     {"inputs": ["close"],                     "func": rss_drv2_020_close_log_mo_diff},
    "rss_drv2_021_close_log_qtr_diff":                    {"inputs": ["close"],                     "func": rss_drv2_021_close_log_qtr_diff},
    "rss_drv2_022_rs_recency_decay63_slope_252d":         {"inputs": ["split_factor"],              "func": rss_drv2_022_rs_recency_decay63_slope_252d},
    "rss_drv2_023_below1_frac_252d_ewm_diff":             {"inputs": ["closeunadj"],                "func": rss_drv2_023_below1_frac_252d_ewm_diff},
    "rss_drv2_024_closeunadj_pct_drawdown_252d_ewm_diff": {"inputs": ["closeunadj"],                "func": rss_drv2_024_closeunadj_pct_drawdown_252d_ewm_diff},
    "rss_drv2_025_rs_composite_distress_mo_diff":         {"inputs": ["split_factor", "closeunadj"], "func": rss_drv2_025_rs_composite_distress_mo_diff},
    "rss_drv2_026_rs_count_504d_mo_diff":                 {"inputs": ["split_factor"],              "func": rss_drv2_026_rs_count_504d_mo_diff},
    "rss_drv2_027_rs_count_504d_qtr_diff":                {"inputs": ["split_factor"],              "func": rss_drv2_027_rs_count_504d_qtr_diff},
    "rss_drv2_028_rs_count_126d_mo_diff":                 {"inputs": ["split_factor"],              "func": rss_drv2_028_rs_count_126d_mo_diff},
    "rss_drv2_029_rs_count_126d_qtr_diff":                {"inputs": ["split_factor"],              "func": rss_drv2_029_rs_count_126d_qtr_diff},
    "rss_drv2_030_rs_severity_ewm252_mo_diff":            {"inputs": ["split_factor"],              "func": rss_drv2_030_rs_severity_ewm252_mo_diff},
    "rss_drv2_031_cumulative_rs_log_504d_mo_diff":        {"inputs": ["split_factor"],              "func": rss_drv2_031_cumulative_rs_log_504d_mo_diff},
    "rss_drv2_032_cumulative_rs_log_504d_qtr_diff":       {"inputs": ["split_factor"],              "func": rss_drv2_032_cumulative_rs_log_504d_qtr_diff},
    "rss_drv2_033_closeunadj_pct_drawdown_504d_mo_diff":  {"inputs": ["closeunadj"],                "func": rss_drv2_033_closeunadj_pct_drawdown_504d_mo_diff},
    "rss_drv2_034_closeunadj_pct_drawdown_504d_qtr_diff": {"inputs": ["closeunadj"],                "func": rss_drv2_034_closeunadj_pct_drawdown_504d_qtr_diff},
    "rss_drv2_035_close_pct_drawdown_504d_mo_diff":       {"inputs": ["close"],                     "func": rss_drv2_035_close_pct_drawdown_504d_mo_diff},
    "rss_drv2_036_close_pct_drawdown_504d_qtr_diff":      {"inputs": ["close"],                     "func": rss_drv2_036_close_pct_drawdown_504d_qtr_diff},
    "rss_drv2_037_below2_frac_252d_mo_diff":              {"inputs": ["closeunadj"],                "func": rss_drv2_037_below2_frac_252d_mo_diff},
    "rss_drv2_038_below2_frac_252d_qtr_diff":             {"inputs": ["closeunadj"],                "func": rss_drv2_038_below2_frac_252d_qtr_diff},
    "rss_drv2_039_below1_frac_252d_qtr_diff":             {"inputs": ["closeunadj"],                "func": rss_drv2_039_below1_frac_252d_qtr_diff},
    "rss_drv2_040_below5_frac_252d_qtr_diff":             {"inputs": ["closeunadj"],                "func": rss_drv2_040_below5_frac_252d_qtr_diff},
    "rss_drv2_041_close_pct_rank_252d_mo_diff":           {"inputs": ["close"],                     "func": rss_drv2_041_close_pct_rank_252d_mo_diff},
    "rss_drv2_042_closeunadj_pct_rank_252d_mo_diff":      {"inputs": ["closeunadj"],                "func": rss_drv2_042_closeunadj_pct_rank_252d_mo_diff},
    "rss_drv2_043_close_pct_rank_252d_qtr_diff":          {"inputs": ["close"],                     "func": rss_drv2_043_close_pct_rank_252d_qtr_diff},
    "rss_drv2_044_closeunadj_pct_rank_252d_qtr_diff":     {"inputs": ["closeunadj"],                "func": rss_drv2_044_closeunadj_pct_rank_252d_qtr_diff},
    "rss_drv2_045_close_zscore_504d_mo_diff":             {"inputs": ["close"],                     "func": rss_drv2_045_close_zscore_504d_mo_diff},
    "rss_drv2_046_closeunadj_zscore_504d_mo_diff":        {"inputs": ["closeunadj"],                "func": rss_drv2_046_closeunadj_zscore_504d_mo_diff},
    "rss_drv2_047_rs_cluster_density_63d_mo_diff":        {"inputs": ["split_factor"],              "func": rss_drv2_047_rs_cluster_density_63d_mo_diff},
    "rss_drv2_048_rs_cluster_density_63d_qtr_diff":       {"inputs": ["split_factor"],              "func": rss_drv2_048_rs_cluster_density_63d_qtr_diff},
    "rss_drv2_049_rs_cluster_density_252d_yoy_diff":      {"inputs": ["split_factor"],              "func": rss_drv2_049_rs_cluster_density_252d_yoy_diff},
    "rss_drv2_050_rs_magnitude_sum_252d_mo_diff":         {"inputs": ["split_factor"],              "func": rss_drv2_050_rs_magnitude_sum_252d_mo_diff},
    "rss_drv2_051_rs_magnitude_sum_252d_qtr_diff":        {"inputs": ["split_factor"],              "func": rss_drv2_051_rs_magnitude_sum_252d_qtr_diff},
    "rss_drv2_052_closeunadj_log_wk_diff":                {"inputs": ["closeunadj"],                "func": rss_drv2_052_closeunadj_log_wk_diff},
    "rss_drv2_053_close_log_wk_diff":                     {"inputs": ["close"],                     "func": rss_drv2_053_close_log_wk_diff},
    "rss_drv2_054_closeunadj_pct_drawdown_252d_wk_diff":  {"inputs": ["closeunadj"],                "func": rss_drv2_054_closeunadj_pct_drawdown_252d_wk_diff},
    "rss_drv2_055_close_pct_drawdown_252d_wk_diff":       {"inputs": ["close"],                     "func": rss_drv2_055_close_pct_drawdown_252d_wk_diff},
    "rss_drv2_056_closeunadj_zscore_252d_qtr_diff":       {"inputs": ["closeunadj"],                "func": rss_drv2_056_closeunadj_zscore_252d_qtr_diff},
    "rss_drv2_057_close_zscore_252d_qtr_diff":            {"inputs": ["close"],                     "func": rss_drv2_057_close_zscore_252d_qtr_diff},
    "rss_drv2_058_rs_recency_decay63_qtr_diff":           {"inputs": ["split_factor"],              "func": rss_drv2_058_rs_recency_decay63_qtr_diff},
    "rss_drv2_059_rs_recency_decay252_mo_diff":           {"inputs": ["split_factor"],              "func": rss_drv2_059_rs_recency_decay252_mo_diff},
    "rss_drv2_060_cumulative_rs_log_252d_qtr_diff":       {"inputs": ["split_factor"],              "func": rss_drv2_060_cumulative_rs_log_252d_qtr_diff},
    "rss_drv2_061_rs_count_252d_mo_diff_slope_63d":       {"inputs": ["split_factor"],              "func": rss_drv2_061_rs_count_252d_mo_diff_slope_63d},
    "rss_drv2_062_closeunadj_pct_drawdown_252d_slope_63d":{"inputs": ["closeunadj"],                "func": rss_drv2_062_closeunadj_pct_drawdown_252d_slope_63d},
    "rss_drv2_063_below1_frac_252d_slope_63d":            {"inputs": ["closeunadj"],                "func": rss_drv2_063_below1_frac_252d_slope_63d},
    "rss_drv2_064_close_zscore_252d_slope_252d":          {"inputs": ["close"],                     "func": rss_drv2_064_close_zscore_252d_slope_252d},
    "rss_drv2_065_closeunadj_log_yoy_ewm_diff":           {"inputs": ["closeunadj"],                "func": rss_drv2_065_closeunadj_log_yoy_ewm_diff},
    "rss_drv2_066_rs_count_252d_ewm_diff":                {"inputs": ["split_factor"],              "func": rss_drv2_066_rs_count_252d_ewm_diff},
    "rss_drv2_067_rs_severity_ewm63_qtr_diff":            {"inputs": ["split_factor"],              "func": rss_drv2_067_rs_severity_ewm63_qtr_diff},
    "rss_drv2_068_rs_severity_ewm252_qtr_diff":           {"inputs": ["split_factor"],              "func": rss_drv2_068_rs_severity_ewm252_qtr_diff},
    "rss_drv2_069_closeunadj_zscore_252d_ewm_diff":       {"inputs": ["closeunadj"],                "func": rss_drv2_069_closeunadj_zscore_252d_ewm_diff},
    "rss_drv2_070_close_log_yoy_diff":                    {"inputs": ["close"],                     "func": rss_drv2_070_close_log_yoy_diff},
    "rss_drv2_071_rs_count_63d_qtr_diff":                 {"inputs": ["split_factor"],              "func": rss_drv2_071_rs_count_63d_qtr_diff},
    "rss_drv2_072_rs_count_252d_yoy_ewm_diff":            {"inputs": ["split_factor"],              "func": rss_drv2_072_rs_count_252d_yoy_ewm_diff},
    "rss_drv2_073_below1_frac_252d_yoy_diff":             {"inputs": ["closeunadj"],                "func": rss_drv2_073_below1_frac_252d_yoy_diff},
    "rss_drv2_074_closeunadj_pct_drawdown_252d_yoy_diff": {"inputs": ["closeunadj"],                "func": rss_drv2_074_closeunadj_pct_drawdown_252d_yoy_diff},
    "rss_drv2_075_rs_composite_distress_qtr_diff":        {"inputs": ["split_factor", "closeunadj"], "func": rss_drv2_075_rs_composite_distress_qtr_diff},
}
