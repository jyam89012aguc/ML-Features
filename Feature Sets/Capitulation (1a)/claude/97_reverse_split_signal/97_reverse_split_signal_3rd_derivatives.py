"""
97_reverse_split_signal — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative features (inflection / exhaustion signals)
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to one shared daily
trading-day index.  The 3rd-derivative series are sparse/stepwise on a
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


# ── Base and 2nd-derivative helpers (self-contained recomputes) ───────────────

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


# ── 2nd-derivative recomputes (needed to compute 3rd derivatives) ─────────────

def _drv2_rs_count_252d_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_count_252d(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_rs_count_252d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_count_252d(split_factor)
    return base - base.shift(_TD_QTR)


def _drv2_rs_count_63d_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_count_63d(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_rs_recency_decay63_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_recency_decay_63(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_rs_recency_decay252_qtr_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_recency_decay_252(split_factor)
    return base - base.shift(_TD_QTR)


def _drv2_cumulative_rs_log_252d_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _cumulative_rs_log_252(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_closeunadj_log_mo_diff(closeunadj: pd.Series) -> pd.Series:
    base = _closeunadj_log(closeunadj)
    return base - base.shift(_TD_MO)


def _drv2_closeunadj_log_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    base = _closeunadj_log(closeunadj)
    return base - base.shift(_TD_QTR)


def _drv2_closeunadj_pct_dd_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    base = _closeunadj_pct_drawdown_252(closeunadj)
    return base - base.shift(_TD_MO)


def _drv2_closeunadj_pct_dd_252d_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    base = _closeunadj_pct_drawdown_252(closeunadj)
    return base - base.shift(_TD_QTR)


def _drv2_close_pct_dd_252d_mo_diff(close: pd.Series) -> pd.Series:
    base = _close_pct_drawdown_252(close)
    return base - base.shift(_TD_MO)


def _drv2_below1_frac_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    base = _below1_frac_252(closeunadj)
    return base - base.shift(_TD_MO)


def _drv2_below5_frac_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    base = _below5_frac_252(closeunadj)
    return base - base.shift(_TD_MO)


def _drv2_rs_severity_ewm63_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_severity_ewm63(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_closeunadj_zscore_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    base = _closeunadj_zscore_252(closeunadj)
    return base - base.shift(_TD_MO)


def _drv2_close_zscore_252d_mo_diff(close: pd.Series) -> pd.Series:
    base = _close_zscore_252(close)
    return base - base.shift(_TD_MO)


def _drv2_close_log_mo_diff(close: pd.Series) -> pd.Series:
    base = _close_log(close)
    return base - base.shift(_TD_MO)


def _drv2_close_log_qtr_diff(close: pd.Series) -> pd.Series:
    base = _close_log(close)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def rss_drv3_001_rs_count_252d_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the 21d-diff of 252d RS count (3rd-order monthly inflection)."""
    d2 = _drv2_rs_count_252d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_002_rs_count_252d_qtr_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the 63d-diff of 252d RS count."""
    d2 = _drv2_rs_count_252d_qtr_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_003_rs_count_63d_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of 63d RS count (3rd-order RS clustering)."""
    d2 = _drv2_rs_count_63d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_004_rs_recency_decay63_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of EWM-63 RS recency decay."""
    d2 = _drv2_rs_recency_decay63_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_005_rs_recency_decay252_qtr_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the quarterly-diff of EWM-252 RS recency decay."""
    d2 = _drv2_rs_recency_decay252_qtr_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_006_cumulative_rs_log_252d_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of log cumulative RS factor (252d)."""
    d2 = _drv2_cumulative_rs_log_252d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_007_closeunadj_log_mo_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 21d log-return of unadjusted close (acceleration of return)."""
    d2 = _drv2_closeunadj_log_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_008_closeunadj_log_qtr_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 63d log-return of unadjusted close."""
    d2 = _drv2_closeunadj_log_qtr_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_009_closeunadj_pct_dd_252d_mo_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of 252d unadjusted drawdown (drawdown exhaustion)."""
    d2 = _drv2_closeunadj_pct_dd_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_010_closeunadj_pct_dd_252d_qtr_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the quarterly-diff of 252d unadjusted drawdown."""
    d2 = _drv2_closeunadj_pct_dd_252d_qtr_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_011_close_pct_dd_252d_mo_diff_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of 252d adjusted close drawdown."""
    d2 = _drv2_close_pct_dd_252d_mo_diff(close)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_012_below1_frac_252d_mo_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of below-$1 fraction (exhaustion of distress worsening)."""
    d2 = _drv2_below1_frac_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_013_below5_frac_252d_mo_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of below-$5 fraction."""
    d2 = _drv2_below5_frac_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_014_rs_severity_ewm63_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of EWM-63 RS severity signal."""
    d2 = _drv2_rs_severity_ewm63_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_015_closeunadj_zscore_252d_mo_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of 252d z-score of unadjusted close."""
    d2 = _drv2_closeunadj_zscore_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_016_close_zscore_252d_mo_diff_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of 252d z-score of adjusted close."""
    d2 = _drv2_close_zscore_252d_mo_diff(close)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_017_closeunadj_log_mo_diff_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of log unadjusted close (cross-horizon 3rd deriv)."""
    d2 = _drv2_closeunadj_log_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_018_close_log_mo_diff_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of log adjusted close."""
    d2 = _drv2_close_log_mo_diff(close)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_019_close_log_qtr_diff_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the quarterly-diff of log adjusted close."""
    d2 = _drv2_close_log_qtr_diff(close)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_020_rs_count_252d_mo_diff_ewm_diff(split_factor: pd.Series) -> pd.Series:
    """
    Monthly-diff of 252d RS count minus its EWM (span=63):
    detects inflection where RS acceleration diverges from its recent trend.
    """
    d2  = _drv2_rs_count_252d_mo_diff(split_factor)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return d2 - ewm


def rss_drv3_021_closeunadj_pct_dd_mo_diff_ewm_diff(closeunadj: pd.Series) -> pd.Series:
    """
    Monthly-diff of 252d unadjusted drawdown minus its EWM (span=63):
    inflection where drawdown acceleration exceeds its own trend.
    """
    d2  = _drv2_closeunadj_pct_dd_252d_mo_diff(closeunadj)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return d2 - ewm


def rss_drv3_022_below1_frac_mo_diff_ewm_diff(closeunadj: pd.Series) -> pd.Series:
    """
    Monthly-diff of below-$1 fraction minus its EWM (span=252):
    measures inflection where the rate of sub-$1 accumulation departs from trend.
    """
    d2  = _drv2_below1_frac_252d_mo_diff(closeunadj)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def rss_drv3_023_rs_recency_decay63_mo_diff_ewm_diff(split_factor: pd.Series) -> pd.Series:
    """
    Monthly-diff of EWM-63 RS recency decay minus its own EWM (span=63):
    detects acceleration inflection in how quickly RS memory is building.
    """
    d2  = _drv2_rs_recency_decay63_mo_diff(split_factor)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return d2 - ewm


def rss_drv3_024_close_log_mo_diff_ewm_diff(close: pd.Series) -> pd.Series:
    """
    Monthly log-return of adjusted close minus its EWM (span=63):
    inflection in price momentum relative to recent trend.
    """
    d2  = _drv2_close_log_mo_diff(close)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return d2 - ewm


def rss_drv3_025_composite_distress_3rd_deriv(split_factor: pd.Series, closeunadj: pd.Series, close: pd.Series) -> pd.Series:
    """
    3rd-derivative of composite distress:
    21d change in the monthly-diff of the composite distress score
    (RS-within-252d + sub-$5 + below-$1 frac + clipped RS count/5 + 252d dd) / 5.
    """
    def _composite(sf, cu):
        rs252  = (_rolling_sum(_is_reverse_split(sf), _TD_YEAR) > 0).astype(float)
        sub5   = (cu < 5.0).astype(float)
        frac1  = _rolling_mean((cu < 1.0).astype(float), _TD_YEAR)
        cnt_rs = (_is_reverse_split(sf).expanding(min_periods=1).sum().clip(upper=5) / 5.0)
        peak   = _rolling_max(cu, _TD_YEAR)
        dd     = _safe_div_abs(cu - peak, peak).abs().clip(upper=1.0)
        return (rs252 + sub5 + frac1 + cnt_rs + dd) / 5.0

    comp = _composite(split_factor, closeunadj)
    d2   = comp - comp.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


# ── Additional 2nd-derivative helpers for drv3 026-075 ───────────────────────

def _rs_count_504d(split_factor: pd.Series) -> pd.Series:
    return _rolling_sum(_is_reverse_split(split_factor), _TD_2Y)


def _rs_count_126d(split_factor: pd.Series) -> pd.Series:
    return _rolling_sum(_is_reverse_split(split_factor), _TD_2Q)


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


def _rs_cluster_density_63(split_factor: pd.Series) -> pd.Series:
    return _rolling_mean(_is_reverse_split(split_factor), _TD_QTR)


def _drv2_rs_count_504d_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_count_504d(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_rs_count_126d_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_count_126d(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_rs_severity_ewm252_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_severity_ewm252(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_cumulative_rs_log_504d_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _cumulative_rs_log_504(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_closeunadj_pct_dd_504d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    base = _closeunadj_pct_drawdown_504(closeunadj)
    return base - base.shift(_TD_MO)


def _drv2_close_pct_dd_504d_mo_diff(close: pd.Series) -> pd.Series:
    base = _close_pct_drawdown_504(close)
    return base - base.shift(_TD_MO)


def _drv2_below2_frac_252d_mo_diff(closeunadj: pd.Series) -> pd.Series:
    base = _below2_frac_252(closeunadj)
    return base - base.shift(_TD_MO)


def _drv2_rs_cluster_density_63d_mo_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_cluster_density_63(split_factor)
    return base - base.shift(_TD_MO)


def _drv2_close_log_qtr_diff(close: pd.Series) -> pd.Series:
    base = _close_log(close)
    return base - base.shift(_TD_QTR)


def _drv2_closeunadj_log_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    base = _closeunadj_log(closeunadj)
    return base - base.shift(_TD_QTR)


def _drv2_rs_count_252d_qtr_diff(split_factor: pd.Series) -> pd.Series:
    base = _rs_count_252d(split_factor)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions 026-075 ─────────────────────────────────

def rss_drv3_026_rs_count_504d_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the 21d-diff of 504d RS count (3rd-order longer-horizon inflection)."""
    d2 = _drv2_rs_count_504d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_027_rs_count_126d_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of 126d RS count."""
    d2 = _drv2_rs_count_126d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_028_rs_severity_ewm252_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of EWM-252 RS severity signal."""
    d2 = _drv2_rs_severity_ewm252_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_029_cumulative_rs_log_504d_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of log cumulative RS factor (504d)."""
    d2 = _drv2_cumulative_rs_log_504d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_030_closeunadj_pct_dd_504d_mo_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of 504d unadjusted pct drawdown."""
    d2 = _drv2_closeunadj_pct_dd_504d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_031_close_pct_dd_504d_mo_diff_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of 504d adjusted pct drawdown."""
    d2 = _drv2_close_pct_dd_504d_mo_diff(close)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_032_below2_frac_252d_mo_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of below-$2 fraction (252d)."""
    d2 = _drv2_below2_frac_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_033_rs_cluster_density_63d_mo_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of RS cluster density (63d window)."""
    d2 = _drv2_rs_cluster_density_63d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_034_closeunadj_log_mo_diff_qtr_diff2(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of log unadjusted close (cross-horizon 3rd deriv, v2)."""
    d2 = _drv2_closeunadj_log_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_035_close_log_mo_diff_qtr_diff(close: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of log adjusted close."""
    d2 = _drv2_close_log_mo_diff(close)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_036_rs_count_252d_qtr_diff_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the quarterly-diff of 252d RS count."""
    d2 = _drv2_rs_count_252d_qtr_diff(split_factor)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_037_closeunadj_pct_dd_252d_qtr_diff_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the quarterly-diff of 252d unadjusted drawdown."""
    d2 = _drv2_closeunadj_pct_dd_252d_qtr_diff(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_038_close_pct_dd_252d_mo_diff_qtr_diff(close: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of 252d adjusted close drawdown."""
    d2 = _drv2_close_pct_dd_252d_mo_diff(close)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_039_rs_recency_decay63_mo_diff_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of EWM-63 RS recency decay."""
    d2 = _drv2_rs_recency_decay63_mo_diff(split_factor)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_040_below1_frac_252d_mo_diff_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of below-$1 fraction."""
    d2 = _drv2_below1_frac_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_041_rs_count_252d_mo_diff_ewm_diff2(split_factor: pd.Series) -> pd.Series:
    """Monthly-diff of 252d RS count minus its EWM (span=252); slower-decay inflection."""
    d2  = _drv2_rs_count_252d_mo_diff(split_factor)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def rss_drv3_042_closeunadj_pct_dd_mo_diff_ewm_diff2(closeunadj: pd.Series) -> pd.Series:
    """Monthly-diff of 252d unadjusted drawdown minus its EWM (span=252)."""
    d2  = _drv2_closeunadj_pct_dd_252d_mo_diff(closeunadj)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def rss_drv3_043_below5_frac_mo_diff_ewm_diff(closeunadj: pd.Series) -> pd.Series:
    """Monthly-diff of below-$5 fraction minus its EWM (span=63)."""
    d2  = _drv2_below5_frac_252d_mo_diff(closeunadj)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return d2 - ewm


def rss_drv3_044_close_log_qtr_diff_qtr_diff(close: pd.Series) -> pd.Series:
    """63-day change in the quarterly-diff of log adjusted close."""
    d2 = _drv2_close_log_qtr_diff(close)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_045_closeunadj_log_qtr_diff_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the quarterly-diff of log unadjusted close."""
    d2 = _drv2_closeunadj_log_qtr_diff(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_046_rs_severity_ewm63_mo_diff_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of EWM-63 RS severity."""
    d2 = _drv2_rs_severity_ewm63_mo_diff(split_factor)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_047_closeunadj_zscore_252d_mo_diff_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of 252d z-score of unadjusted close."""
    d2 = _drv2_closeunadj_zscore_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_048_close_zscore_252d_mo_diff_qtr_diff(close: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of 252d z-score of adjusted close."""
    d2 = _drv2_close_zscore_252d_mo_diff(close)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_049_rs_recency_decay252_qtr_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the quarterly-diff of EWM-252 RS recency decay."""
    d2 = _drv2_rs_recency_decay252_qtr_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_050_rs_recency_decay252_qtr_diff_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the quarterly-diff of EWM-252 RS recency decay."""
    d2 = _drv2_rs_recency_decay252_qtr_diff(split_factor)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_051_rs_count_252d_mo_diff_yoy_diff(split_factor: pd.Series) -> pd.Series:
    """252-day change in the monthly-diff of 252d RS count (YoY change in RS acceleration)."""
    d2 = _drv2_rs_count_252d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_YEAR)


def rss_drv3_052_closeunadj_log_mo_diff_yoy_diff(closeunadj: pd.Series) -> pd.Series:
    """252-day change in the monthly log-return of unadjusted close."""
    d2 = _drv2_closeunadj_log_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_YEAR)


def rss_drv3_053_close_log_mo_diff_yoy_diff(close: pd.Series) -> pd.Series:
    """252-day change in the monthly log-return of adjusted close."""
    d2 = _drv2_close_log_mo_diff(close)
    return d2 - d2.shift(_TD_YEAR)


def rss_drv3_054_below1_frac_252d_mo_diff_yoy_diff(closeunadj: pd.Series) -> pd.Series:
    """252-day change in the monthly-diff of below-$1 fraction."""
    d2 = _drv2_below1_frac_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_YEAR)


def rss_drv3_055_closeunadj_pct_dd_252d_mo_diff_yoy_diff(closeunadj: pd.Series) -> pd.Series:
    """252-day change in the monthly-diff of 252d unadjusted drawdown."""
    d2 = _drv2_closeunadj_pct_dd_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_YEAR)


def rss_drv3_056_rs_count_252d_mo_diff_ewm_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in (monthly-diff of 252d RS count minus its EWM span=63)."""
    d2  = _drv2_rs_count_252d_mo_diff(split_factor)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    base = d2 - ewm
    return base - base.shift(_TD_MO)


def rss_drv3_057_closeunadj_pct_dd_mo_diff_ewm_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in (monthly-diff of 252d unadjusted drawdown minus EWM span=63)."""
    d2  = _drv2_closeunadj_pct_dd_252d_mo_diff(closeunadj)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    base = d2 - ewm
    return base - base.shift(_TD_MO)


def rss_drv3_058_below1_frac_mo_diff_ewm_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in (monthly-diff of below-$1 fraction minus EWM span=252)."""
    d2  = _drv2_below1_frac_252d_mo_diff(closeunadj)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    base = d2 - ewm
    return base - base.shift(_TD_MO)


def rss_drv3_059_rs_recency_decay63_mo_diff_ewm_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in (monthly-diff of EWM-63 RS decay minus EWM span=63)."""
    d2  = _drv2_rs_recency_decay63_mo_diff(split_factor)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    base = d2 - ewm
    return base - base.shift(_TD_MO)


def rss_drv3_060_close_log_mo_diff_ewm_diff_mo_diff(close: pd.Series) -> pd.Series:
    """21-day change in (monthly log-return of adjusted close minus EWM span=63)."""
    d2  = _drv2_close_log_mo_diff(close)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    base = d2 - ewm
    return base - base.shift(_TD_MO)


def rss_drv3_061_rs_count_504d_mo_diff_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of 504d RS count."""
    d2 = _drv2_rs_count_504d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_062_below2_frac_252d_mo_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of below-$2 fraction."""
    d2 = _drv2_below2_frac_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_063_rs_count_126d_mo_diff_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of 126d RS count."""
    d2 = _drv2_rs_count_126d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_064_closeunadj_pct_dd_504d_mo_diff_qtr_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of 504d unadjusted drawdown."""
    d2 = _drv2_closeunadj_pct_dd_504d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_065_close_pct_dd_504d_mo_diff_qtr_diff(close: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of 504d adjusted drawdown."""
    d2 = _drv2_close_pct_dd_504d_mo_diff(close)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_066_rs_severity_ewm252_mo_diff_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of EWM-252 RS severity."""
    d2 = _drv2_rs_severity_ewm252_mo_diff(split_factor)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_067_cumulative_rs_log_252d_mo_diff_qtr_diff(split_factor: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of log cumulative RS factor (252d)."""
    d2 = _drv2_cumulative_rs_log_252d_mo_diff(split_factor)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_068_closeunadj_zscore_252d_mo_diff_qtr_diff2(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of 252d z-score of unadjusted close (v2)."""
    d2 = _drv2_closeunadj_zscore_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_069_below5_frac_252d_mo_diff_mo_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the monthly-diff of below-$5 fraction (252d)."""
    d2 = _drv2_below5_frac_252d_mo_diff(closeunadj)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_070_rs_count_252d_qtr_diff_mo_diff(split_factor: pd.Series) -> pd.Series:
    """21-day change in the quarterly-diff of 252d RS count."""
    d2 = _drv2_rs_count_252d_qtr_diff(split_factor)
    return d2 - d2.shift(_TD_MO)


def rss_drv3_071_closeunadj_pct_dd_252d_qtr_diff_qtr_diff2(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the quarterly-diff of 252d unadjusted drawdown (v2)."""
    d2 = _drv2_closeunadj_pct_dd_252d_qtr_diff(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_072_rs_recency_decay63_mo_diff_mo_diff2(split_factor: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of EWM-63 RS recency decay (v2)."""
    d2 = _drv2_rs_recency_decay63_mo_diff(split_factor)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_073_close_log_qtr_diff_mo_diff2(close: pd.Series) -> pd.Series:
    """63-day change in the monthly-diff of log adjusted close (cross-lag)."""
    d2 = _drv2_close_log_mo_diff(close)
    return d2 - d2.shift(_TD_QTR)


def rss_drv3_074_closeunadj_log_mo_diff_ewm_diff(closeunadj: pd.Series) -> pd.Series:
    """Monthly log-return of unadjusted close minus its EWM (span=63): momentum inflection."""
    d2  = _drv2_closeunadj_log_mo_diff(closeunadj)
    ewm = d2.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return d2 - ewm


def rss_drv3_075_composite_distress_3rd_deriv_qtr(split_factor: pd.Series, closeunadj: pd.Series, close: pd.Series) -> pd.Series:
    """
    3rd-derivative of composite distress using quarterly diff:
    63d change in the monthly-diff of the composite distress score.
    """
    def _composite(sf, cu):
        rs252  = (_rolling_sum(_is_reverse_split(sf), _TD_YEAR) > 0).astype(float)
        sub5   = (cu < 5.0).astype(float)
        frac1  = _rolling_mean((cu < 1.0).astype(float), _TD_YEAR)
        cnt_rs = (_is_reverse_split(sf).expanding(min_periods=1).sum().clip(upper=5) / 5.0)
        peak   = _rolling_max(cu, _TD_YEAR)
        dd     = _safe_div_abs(cu - peak, peak).abs().clip(upper=1.0)
        return (rs252 + sub5 + frac1 + cnt_rs + dd) / 5.0

    comp = _composite(split_factor, closeunadj)
    d2   = comp - comp.shift(_TD_MO)
    return d2 - d2.shift(_TD_QTR)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

REVERSE_SPLIT_SIGNAL_REGISTRY_3RD_DERIVATIVES = {
    "rss_drv3_001_rs_count_252d_mo_diff_mo_diff":            {"inputs": ["split_factor"],                      "func": rss_drv3_001_rs_count_252d_mo_diff_mo_diff},
    "rss_drv3_002_rs_count_252d_qtr_diff_mo_diff":           {"inputs": ["split_factor"],                      "func": rss_drv3_002_rs_count_252d_qtr_diff_mo_diff},
    "rss_drv3_003_rs_count_63d_mo_diff_mo_diff":             {"inputs": ["split_factor"],                      "func": rss_drv3_003_rs_count_63d_mo_diff_mo_diff},
    "rss_drv3_004_rs_recency_decay63_mo_diff_mo_diff":       {"inputs": ["split_factor"],                      "func": rss_drv3_004_rs_recency_decay63_mo_diff_mo_diff},
    "rss_drv3_005_rs_recency_decay252_qtr_diff_mo_diff":     {"inputs": ["split_factor"],                      "func": rss_drv3_005_rs_recency_decay252_qtr_diff_mo_diff},
    "rss_drv3_006_cumulative_rs_log_252d_mo_diff_mo_diff":   {"inputs": ["split_factor"],                      "func": rss_drv3_006_cumulative_rs_log_252d_mo_diff_mo_diff},
    "rss_drv3_007_closeunadj_log_mo_diff_mo_diff":           {"inputs": ["closeunadj"],                        "func": rss_drv3_007_closeunadj_log_mo_diff_mo_diff},
    "rss_drv3_008_closeunadj_log_qtr_diff_mo_diff":          {"inputs": ["closeunadj"],                        "func": rss_drv3_008_closeunadj_log_qtr_diff_mo_diff},
    "rss_drv3_009_closeunadj_pct_dd_252d_mo_diff_mo_diff":   {"inputs": ["closeunadj"],                        "func": rss_drv3_009_closeunadj_pct_dd_252d_mo_diff_mo_diff},
    "rss_drv3_010_closeunadj_pct_dd_252d_qtr_diff_mo_diff":  {"inputs": ["closeunadj"],                        "func": rss_drv3_010_closeunadj_pct_dd_252d_qtr_diff_mo_diff},
    "rss_drv3_011_close_pct_dd_252d_mo_diff_mo_diff":        {"inputs": ["close"],                             "func": rss_drv3_011_close_pct_dd_252d_mo_diff_mo_diff},
    "rss_drv3_012_below1_frac_252d_mo_diff_mo_diff":         {"inputs": ["closeunadj"],                        "func": rss_drv3_012_below1_frac_252d_mo_diff_mo_diff},
    "rss_drv3_013_below5_frac_252d_mo_diff_mo_diff":         {"inputs": ["closeunadj"],                        "func": rss_drv3_013_below5_frac_252d_mo_diff_mo_diff},
    "rss_drv3_014_rs_severity_ewm63_mo_diff_mo_diff":        {"inputs": ["split_factor"],                      "func": rss_drv3_014_rs_severity_ewm63_mo_diff_mo_diff},
    "rss_drv3_015_closeunadj_zscore_252d_mo_diff_mo_diff":   {"inputs": ["closeunadj"],                        "func": rss_drv3_015_closeunadj_zscore_252d_mo_diff_mo_diff},
    "rss_drv3_016_close_zscore_252d_mo_diff_mo_diff":        {"inputs": ["close"],                             "func": rss_drv3_016_close_zscore_252d_mo_diff_mo_diff},
    "rss_drv3_017_closeunadj_log_mo_diff_qtr_diff":          {"inputs": ["closeunadj"],                        "func": rss_drv3_017_closeunadj_log_mo_diff_qtr_diff},
    "rss_drv3_018_close_log_mo_diff_mo_diff":                {"inputs": ["close"],                             "func": rss_drv3_018_close_log_mo_diff_mo_diff},
    "rss_drv3_019_close_log_qtr_diff_mo_diff":               {"inputs": ["close"],                             "func": rss_drv3_019_close_log_qtr_diff_mo_diff},
    "rss_drv3_020_rs_count_252d_mo_diff_ewm_diff":           {"inputs": ["split_factor"],                      "func": rss_drv3_020_rs_count_252d_mo_diff_ewm_diff},
    "rss_drv3_021_closeunadj_pct_dd_mo_diff_ewm_diff":       {"inputs": ["closeunadj"],                        "func": rss_drv3_021_closeunadj_pct_dd_mo_diff_ewm_diff},
    "rss_drv3_022_below1_frac_mo_diff_ewm_diff":             {"inputs": ["closeunadj"],                        "func": rss_drv3_022_below1_frac_mo_diff_ewm_diff},
    "rss_drv3_023_rs_recency_decay63_mo_diff_ewm_diff":      {"inputs": ["split_factor"],                      "func": rss_drv3_023_rs_recency_decay63_mo_diff_ewm_diff},
    "rss_drv3_024_close_log_mo_diff_ewm_diff":               {"inputs": ["close"],                             "func": rss_drv3_024_close_log_mo_diff_ewm_diff},
    "rss_drv3_025_composite_distress_3rd_deriv":             {"inputs": ["split_factor", "closeunadj", "close"], "func": rss_drv3_025_composite_distress_3rd_deriv},
    "rss_drv3_026_rs_count_504d_mo_diff_mo_diff":            {"inputs": ["split_factor"],                      "func": rss_drv3_026_rs_count_504d_mo_diff_mo_diff},
    "rss_drv3_027_rs_count_126d_mo_diff_mo_diff":            {"inputs": ["split_factor"],                      "func": rss_drv3_027_rs_count_126d_mo_diff_mo_diff},
    "rss_drv3_028_rs_severity_ewm252_mo_diff_mo_diff":       {"inputs": ["split_factor"],                      "func": rss_drv3_028_rs_severity_ewm252_mo_diff_mo_diff},
    "rss_drv3_029_cumulative_rs_log_504d_mo_diff_mo_diff":   {"inputs": ["split_factor"],                      "func": rss_drv3_029_cumulative_rs_log_504d_mo_diff_mo_diff},
    "rss_drv3_030_closeunadj_pct_dd_504d_mo_diff_mo_diff":   {"inputs": ["closeunadj"],                        "func": rss_drv3_030_closeunadj_pct_dd_504d_mo_diff_mo_diff},
    "rss_drv3_031_close_pct_dd_504d_mo_diff_mo_diff":        {"inputs": ["close"],                             "func": rss_drv3_031_close_pct_dd_504d_mo_diff_mo_diff},
    "rss_drv3_032_below2_frac_252d_mo_diff_mo_diff":         {"inputs": ["closeunadj"],                        "func": rss_drv3_032_below2_frac_252d_mo_diff_mo_diff},
    "rss_drv3_033_rs_cluster_density_63d_mo_diff_mo_diff":   {"inputs": ["split_factor"],                      "func": rss_drv3_033_rs_cluster_density_63d_mo_diff_mo_diff},
    "rss_drv3_034_closeunadj_log_mo_diff_qtr_diff2":         {"inputs": ["closeunadj"],                        "func": rss_drv3_034_closeunadj_log_mo_diff_qtr_diff2},
    "rss_drv3_035_close_log_mo_diff_qtr_diff":               {"inputs": ["close"],                             "func": rss_drv3_035_close_log_mo_diff_qtr_diff},
    "rss_drv3_036_rs_count_252d_qtr_diff_qtr_diff":          {"inputs": ["split_factor"],                      "func": rss_drv3_036_rs_count_252d_qtr_diff_qtr_diff},
    "rss_drv3_037_closeunadj_pct_dd_252d_qtr_diff_qtr_diff": {"inputs": ["closeunadj"],                        "func": rss_drv3_037_closeunadj_pct_dd_252d_qtr_diff_qtr_diff},
    "rss_drv3_038_close_pct_dd_252d_mo_diff_qtr_diff":       {"inputs": ["close"],                             "func": rss_drv3_038_close_pct_dd_252d_mo_diff_qtr_diff},
    "rss_drv3_039_rs_recency_decay63_mo_diff_qtr_diff":      {"inputs": ["split_factor"],                      "func": rss_drv3_039_rs_recency_decay63_mo_diff_qtr_diff},
    "rss_drv3_040_below1_frac_252d_mo_diff_qtr_diff":        {"inputs": ["closeunadj"],                        "func": rss_drv3_040_below1_frac_252d_mo_diff_qtr_diff},
    "rss_drv3_041_rs_count_252d_mo_diff_ewm_diff2":          {"inputs": ["split_factor"],                      "func": rss_drv3_041_rs_count_252d_mo_diff_ewm_diff2},
    "rss_drv3_042_closeunadj_pct_dd_mo_diff_ewm_diff2":      {"inputs": ["closeunadj"],                        "func": rss_drv3_042_closeunadj_pct_dd_mo_diff_ewm_diff2},
    "rss_drv3_043_below5_frac_mo_diff_ewm_diff":             {"inputs": ["closeunadj"],                        "func": rss_drv3_043_below5_frac_mo_diff_ewm_diff},
    "rss_drv3_044_close_log_qtr_diff_qtr_diff":              {"inputs": ["close"],                             "func": rss_drv3_044_close_log_qtr_diff_qtr_diff},
    "rss_drv3_045_closeunadj_log_qtr_diff_qtr_diff":         {"inputs": ["closeunadj"],                        "func": rss_drv3_045_closeunadj_log_qtr_diff_qtr_diff},
    "rss_drv3_046_rs_severity_ewm63_mo_diff_qtr_diff":       {"inputs": ["split_factor"],                      "func": rss_drv3_046_rs_severity_ewm63_mo_diff_qtr_diff},
    "rss_drv3_047_closeunadj_zscore_252d_mo_diff_qtr_diff":  {"inputs": ["closeunadj"],                        "func": rss_drv3_047_closeunadj_zscore_252d_mo_diff_qtr_diff},
    "rss_drv3_048_close_zscore_252d_mo_diff_qtr_diff":       {"inputs": ["close"],                             "func": rss_drv3_048_close_zscore_252d_mo_diff_qtr_diff},
    "rss_drv3_049_rs_recency_decay252_qtr_diff_mo_diff":     {"inputs": ["split_factor"],                      "func": rss_drv3_049_rs_recency_decay252_qtr_diff_mo_diff},
    "rss_drv3_050_rs_recency_decay252_qtr_diff_qtr_diff":    {"inputs": ["split_factor"],                      "func": rss_drv3_050_rs_recency_decay252_qtr_diff_qtr_diff},
    "rss_drv3_051_rs_count_252d_mo_diff_yoy_diff":           {"inputs": ["split_factor"],                      "func": rss_drv3_051_rs_count_252d_mo_diff_yoy_diff},
    "rss_drv3_052_closeunadj_log_mo_diff_yoy_diff":          {"inputs": ["closeunadj"],                        "func": rss_drv3_052_closeunadj_log_mo_diff_yoy_diff},
    "rss_drv3_053_close_log_mo_diff_yoy_diff":               {"inputs": ["close"],                             "func": rss_drv3_053_close_log_mo_diff_yoy_diff},
    "rss_drv3_054_below1_frac_252d_mo_diff_yoy_diff":        {"inputs": ["closeunadj"],                        "func": rss_drv3_054_below1_frac_252d_mo_diff_yoy_diff},
    "rss_drv3_055_closeunadj_pct_dd_252d_mo_diff_yoy_diff":  {"inputs": ["closeunadj"],                        "func": rss_drv3_055_closeunadj_pct_dd_252d_mo_diff_yoy_diff},
    "rss_drv3_056_rs_count_252d_mo_diff_ewm_diff_mo_diff":   {"inputs": ["split_factor"],                      "func": rss_drv3_056_rs_count_252d_mo_diff_ewm_diff_mo_diff},
    "rss_drv3_057_closeunadj_pct_dd_mo_diff_ewm_diff_mo_diff": {"inputs": ["closeunadj"],                      "func": rss_drv3_057_closeunadj_pct_dd_mo_diff_ewm_diff_mo_diff},
    "rss_drv3_058_below1_frac_mo_diff_ewm_diff_mo_diff":     {"inputs": ["closeunadj"],                        "func": rss_drv3_058_below1_frac_mo_diff_ewm_diff_mo_diff},
    "rss_drv3_059_rs_recency_decay63_mo_diff_ewm_diff_mo_diff": {"inputs": ["split_factor"],                   "func": rss_drv3_059_rs_recency_decay63_mo_diff_ewm_diff_mo_diff},
    "rss_drv3_060_close_log_mo_diff_ewm_diff_mo_diff":       {"inputs": ["close"],                             "func": rss_drv3_060_close_log_mo_diff_ewm_diff_mo_diff},
    "rss_drv3_061_rs_count_504d_mo_diff_qtr_diff":           {"inputs": ["split_factor"],                      "func": rss_drv3_061_rs_count_504d_mo_diff_qtr_diff},
    "rss_drv3_062_below2_frac_252d_mo_diff_mo_diff":         {"inputs": ["closeunadj"],                        "func": rss_drv3_062_below2_frac_252d_mo_diff_mo_diff},
    "rss_drv3_063_rs_count_126d_mo_diff_qtr_diff":           {"inputs": ["split_factor"],                      "func": rss_drv3_063_rs_count_126d_mo_diff_qtr_diff},
    "rss_drv3_064_closeunadj_pct_dd_504d_mo_diff_qtr_diff":  {"inputs": ["closeunadj"],                        "func": rss_drv3_064_closeunadj_pct_dd_504d_mo_diff_qtr_diff},
    "rss_drv3_065_close_pct_dd_504d_mo_diff_qtr_diff":       {"inputs": ["close"],                             "func": rss_drv3_065_close_pct_dd_504d_mo_diff_qtr_diff},
    "rss_drv3_066_rs_severity_ewm252_mo_diff_qtr_diff":      {"inputs": ["split_factor"],                      "func": rss_drv3_066_rs_severity_ewm252_mo_diff_qtr_diff},
    "rss_drv3_067_cumulative_rs_log_252d_mo_diff_qtr_diff":  {"inputs": ["split_factor"],                      "func": rss_drv3_067_cumulative_rs_log_252d_mo_diff_qtr_diff},
    "rss_drv3_068_closeunadj_zscore_252d_mo_diff_qtr_diff2": {"inputs": ["closeunadj"],                        "func": rss_drv3_068_closeunadj_zscore_252d_mo_diff_qtr_diff2},
    "rss_drv3_069_below5_frac_252d_mo_diff_mo_diff":         {"inputs": ["closeunadj"],                        "func": rss_drv3_069_below5_frac_252d_mo_diff_mo_diff},
    "rss_drv3_070_rs_count_252d_qtr_diff_mo_diff":           {"inputs": ["split_factor"],                      "func": rss_drv3_070_rs_count_252d_qtr_diff_mo_diff},
    "rss_drv3_071_closeunadj_pct_dd_252d_qtr_diff_qtr_diff2": {"inputs": ["closeunadj"],                       "func": rss_drv3_071_closeunadj_pct_dd_252d_qtr_diff_qtr_diff2},
    "rss_drv3_072_rs_recency_decay63_mo_diff_mo_diff2":      {"inputs": ["split_factor"],                      "func": rss_drv3_072_rs_recency_decay63_mo_diff_mo_diff2},
    "rss_drv3_073_close_log_qtr_diff_mo_diff2":              {"inputs": ["close"],                             "func": rss_drv3_073_close_log_qtr_diff_mo_diff2},
    "rss_drv3_074_closeunadj_log_mo_diff_ewm_diff":          {"inputs": ["closeunadj"],                        "func": rss_drv3_074_closeunadj_log_mo_diff_ewm_diff},
    "rss_drv3_075_composite_distress_3rd_deriv_qtr":         {"inputs": ["split_factor", "closeunadj", "close"], "func": rss_drv3_075_composite_distress_3rd_deriv_qtr},
}
