"""
96_dividend_distress — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative dividend-distress features (exhaustion/inflection)
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to a shared trading-day index.
Quarterly Sharadar SF1 fields are forward-filled to the daily index so that
flat stretches between report dates are correct and expected.
The 3rd-derivative series are sparse/stepwise on a daily index because the
underlying data is quarterly — this is correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or .expanding().
Quarterly cadence on the daily index: 1 quarter = 63 trading days, 1 year = 252 trading days.

  dps       : dividends per share, USD (Sharadar SF1 quarterly, forward-filled; 0.0 when none).
  dividends : total cash dividends paid, USD, positive outflow (Sharadar SF1 quarterly,
              forward-filled; 0.0 when none).
  close     : split/dividend-adjusted daily close price, USD.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_TD_2Q    = 126
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
    """
    return q_series.reindex(daily_index).ffill()


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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


# ── 2nd-derivative helpers (self-contained recomputes) ───────────────────────
# Each _drv2_* helper recomputes the corresponding 2nd-derivative series
# so this file needs no cross-import from the 2nd-derivatives file.

def _drv2_dps_qoq_qoq(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ DPS change."""
    base = dps - dps.shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def _drv2_dps_yoy_qoq(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in YoY DPS change."""
    base = dps - dps.shift(_TD_YEAR)
    return base - base.shift(_TD_QTR)


def _drv2_dps_qoq_pct_qoq(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ DPS pct change."""
    prior = dps.shift(_TD_QTR)
    base = _safe_div_abs(dps - prior, prior)
    return base - base.shift(_TD_QTR)


def _drv2_dps_yoy_pct_qoq(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in YoY DPS pct change."""
    prior = dps.shift(_TD_YEAR)
    base = _safe_div_abs(dps - prior, prior)
    return base - base.shift(_TD_QTR)


def _drv2_dps_drawdown_1y_qoq(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in DPS 1-year-peak drawdown."""
    base = dps - _rolling_max(dps, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def _drv2_dps_zscore_1y_qoq(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in DPS 1-year z-score."""
    m  = _rolling_mean(dps, _TD_YEAR)
    sd = _rolling_std(dps, _TD_YEAR)
    base = _safe_div(dps - m, sd)
    return base - base.shift(_TD_QTR)


def _drv2_dps_zscore_3y_qoq(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in DPS 3-year z-score."""
    m  = _rolling_mean(dps, _TD_3Y)
    sd = _rolling_std(dps, _TD_3Y)
    base = _safe_div(dps - m, sd)
    return base - base.shift(_TD_QTR)


def _drv2_dps_cut_fraction_1y_qoq(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in DPS 1-year cut fraction."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    base = cut.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - base.shift(_TD_QTR)


def _drv2_dps_ttm_qoq(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in TTM DPS sum."""
    ttm  = dps.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    return ttm - ttm.shift(_TD_QTR)


def _drv2_dividends_qoq_qoq(dividends: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ total-dividends change."""
    base = dividends - dividends.shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def _drv2_dividends_yoy_qoq(dividends: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in YoY total-dividends change."""
    base = dividends - dividends.shift(_TD_YEAR)
    return base - base.shift(_TD_QTR)


def _drv2_yield_proxy_qoq(dps: pd.Series, close: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in DPS/close yield proxy."""
    y = dps * 4.0 / close.replace(0, np.nan)
    return y - y.shift(_TD_QTR)


def _drv2_dps_ttm_drawdown_accel(dps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in TTM-DPS drawdown from expanding peak."""
    ttm  = dps.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    peak = ttm.expanding(min_periods=1).max()
    base = ttm - peak
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def dvd_drv3_001_dps_qoq_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative QoQ/QoQ DPS series (inflection of acceleration)."""
    d2 = _drv2_dps_qoq_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_002_dps_yoy_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative YoY/QoQ DPS series."""
    d2 = _drv2_dps_yoy_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_003_dps_qoq_pct_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative QoQ-pct/QoQ DPS series."""
    d2 = _drv2_dps_qoq_pct_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_004_dps_yoy_pct_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative YoY-pct/QoQ DPS series."""
    d2 = _drv2_dps_yoy_pct_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_005_dps_drawdown_1y_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS drawdown acceleration."""
    d2 = _drv2_dps_drawdown_1y_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_006_dps_zscore_1y_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS 1-year z-score acceleration."""
    d2 = _drv2_dps_zscore_1y_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_007_dps_zscore_3y_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS 3-year z-score acceleration."""
    d2 = _drv2_dps_zscore_3y_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_008_dps_cut_fraction_1y_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS 1-year cut-fraction acceleration."""
    d2 = _drv2_dps_cut_fraction_1y_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_009_dps_ttm_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative TTM DPS acceleration."""
    d2 = _drv2_dps_ttm_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_010_dividends_qoq_qoq_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative total-dividends QoQ/QoQ series."""
    d2 = _drv2_dividends_qoq_qoq(dividends)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_011_dividends_yoy_qoq_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative total-dividends YoY/QoQ series."""
    d2 = _drv2_dividends_yoy_qoq(dividends)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_012_yield_proxy_qoq_qoq_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative yield-proxy QoQ acceleration."""
    d2 = _drv2_yield_proxy_qoq(dps, close)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_013_dps_ttm_drawdown_accel_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative TTM-DPS drawdown acceleration."""
    d2 = _drv2_dps_ttm_drawdown_accel(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_014_dps_qoq_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative QoQ/QoQ DPS series (annual inflection)."""
    d2 = _drv2_dps_qoq_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_015_dps_yoy_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative YoY/QoQ DPS series."""
    d2 = _drv2_dps_yoy_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_016_dps_zscore_1y_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS 1-year z-score acceleration."""
    d2 = _drv2_dps_zscore_1y_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_017_dps_drawdown_1y_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS drawdown acceleration."""
    d2 = _drv2_dps_drawdown_1y_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_018_dividends_qoq_qoq_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative total-dividends QoQ acceleration."""
    d2 = _drv2_dividends_qoq_qoq(dividends)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_019_dps_qoq_qoq_ewm(dps: pd.Series) -> pd.Series:
    """2nd-derivative QoQ/QoQ DPS minus its own 4-quarter EWM (exhaustion signal)."""
    d2  = _drv2_dps_qoq_qoq(dps)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_020_dividends_qoq_qoq_ewm(dividends: pd.Series) -> pd.Series:
    """2nd-derivative dividends QoQ/QoQ minus its own 4-quarter EWM."""
    d2  = _drv2_dividends_qoq_qoq(dividends)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_021_dps_zscore_1y_qoq_ewm(dps: pd.Series) -> pd.Series:
    """2nd-derivative DPS z-score acceleration minus its 4-quarter EWM."""
    d2  = _drv2_dps_zscore_1y_qoq(dps)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_022_yield_proxy_qoq_yoy_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative yield-proxy QoQ acceleration."""
    d2 = _drv2_yield_proxy_qoq(dps, close)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_023_dps_ttm_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative TTM DPS acceleration."""
    d2 = _drv2_dps_ttm_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_024_dps_cut_fraction_1y_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS cut-fraction acceleration."""
    d2 = _drv2_dps_cut_fraction_1y_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_025_dps_ttm_drawdown_accel_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative TTM-DPS drawdown acceleration (deepest exhaustion)."""
    d2 = _drv2_dps_ttm_drawdown_accel(dps)
    return d2 - d2.shift(_TD_YEAR)


# ── Additional 2nd-derivative helpers for 3rd-derivative features 026-075 ────

def _drv2_dps_pct_drawdown_1y_qoq(dps: pd.Series) -> pd.Series:
    peak = _rolling_max(dps, _TD_YEAR)
    base = _safe_div_abs(dps - peak, peak)
    return base - base.shift(_TD_QTR)


def _drv2_dps_pct_drawdown_3y_qoq(dps: pd.Series) -> pd.Series:
    peak = _rolling_max(dps, _TD_3Y)
    base = _safe_div_abs(dps - peak, peak)
    return base - base.shift(_TD_QTR)


def _drv2_dps_drawdown_3y_qoq(dps: pd.Series) -> pd.Series:
    base = dps - _rolling_max(dps, _TD_3Y)
    return base - base.shift(_TD_QTR)


def _drv2_dps_omission_frac_1y_qoq(dps: pd.Series) -> pd.Series:
    zero = (dps <= 0).astype(float)
    base = zero.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - base.shift(_TD_QTR)


def _drv2_dps_cut_frac_3y_qoq(dps: pd.Series) -> pd.Series:
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    base = cut.rolling(_TD_3Y, min_periods=max(1, _TD_3Y // 4)).mean()
    return base - base.shift(_TD_QTR)


def _drv2_dps_vs_1y_avg_qoq(dps: pd.Series) -> pd.Series:
    base = dps - _rolling_mean(dps, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def _drv2_dps_vs_3y_avg_qoq(dps: pd.Series) -> pd.Series:
    base = dps - _rolling_mean(dps, _TD_3Y)
    return base - base.shift(_TD_QTR)


def _drv2_dividends_qoq_pct_qoq(dividends: pd.Series) -> pd.Series:
    prior = dividends.shift(_TD_QTR)
    base  = _safe_div_abs(dividends - prior, prior)
    return base - base.shift(_TD_QTR)


def _drv2_dividends_drawdown_3y_qoq(dividends: pd.Series) -> pd.Series:
    base = dividends - _rolling_max(dividends, _TD_3Y)
    return base - base.shift(_TD_QTR)


def _drv2_yield_zscore_1y_qoq(dps: pd.Series, close: pd.Series) -> pd.Series:
    y  = dps * 4.0 / close.replace(0, np.nan)
    m  = _rolling_mean(y, _TD_YEAR)
    sd = _rolling_std(y, _TD_YEAR)
    base = _safe_div(y - m, sd)
    return base - base.shift(_TD_QTR)


def _drv2_yield_zscore_3y_qoq(dps: pd.Series, close: pd.Series) -> pd.Series:
    y  = dps * 4.0 / close.replace(0, np.nan)
    m  = _rolling_mean(y, _TD_3Y)
    sd = _rolling_std(y, _TD_3Y)
    base = _safe_div(y - m, sd)
    return base - base.shift(_TD_QTR)


def _drv2_dps_ttm_zscore_qoq(dps: pd.Series) -> pd.Series:
    ttm = dps.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    m   = _rolling_mean(ttm, _TD_YEAR)
    sd  = _rolling_std(ttm, _TD_YEAR)
    base = _safe_div(ttm - m, sd)
    return base - base.shift(_TD_QTR)


def _drv2_dividends_ttm_qoq(dividends: pd.Series) -> pd.Series:
    ttm = dividends.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    return ttm - ttm.shift(_TD_QTR)


def _drv2_dividends_ttm_drawdown_accel(dividends: pd.Series) -> pd.Series:
    ttm  = dividends.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    peak = ttm.expanding(min_periods=1).max()
    base = ttm - peak
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions 026-075 ─────────────────────────────────

def dvd_drv3_026_dps_pct_drawdown_1y_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS 1-year pct-drawdown acceleration."""
    d2 = _drv2_dps_pct_drawdown_1y_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_027_dps_pct_drawdown_3y_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS 3-year pct-drawdown acceleration."""
    d2 = _drv2_dps_pct_drawdown_3y_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_028_dps_drawdown_3y_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS 3-year drawdown acceleration."""
    d2 = _drv2_dps_drawdown_3y_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_029_dps_omission_frac_1y_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS omission-fraction acceleration."""
    d2 = _drv2_dps_omission_frac_1y_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_030_dps_cut_frac_3y_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS 3-year cut-fraction acceleration."""
    d2 = _drv2_dps_cut_frac_3y_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_031_dps_vs_1y_avg_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS-vs-1y-avg acceleration."""
    d2 = _drv2_dps_vs_1y_avg_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_032_dps_vs_3y_avg_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS-vs-3y-avg acceleration."""
    d2 = _drv2_dps_vs_3y_avg_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_033_dividends_qoq_pct_qoq_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative total-dividends QoQ-pct acceleration."""
    d2 = _drv2_dividends_qoq_pct_qoq(dividends)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_034_dividends_drawdown_3y_qoq_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative total-dividends 3y drawdown acceleration."""
    d2 = _drv2_dividends_drawdown_3y_qoq(dividends)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_035_yield_zscore_1y_qoq_qoq_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative yield 1y z-score acceleration."""
    d2 = _drv2_yield_zscore_1y_qoq(dps, close)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_036_yield_zscore_3y_qoq_qoq_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative yield 3y z-score acceleration."""
    d2 = _drv2_yield_zscore_3y_qoq(dps, close)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_037_dps_ttm_zscore_qoq_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative TTM DPS z-score acceleration."""
    d2 = _drv2_dps_ttm_zscore_qoq(dps)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_038_dividends_ttm_qoq_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative TTM total-dividends acceleration."""
    d2 = _drv2_dividends_ttm_qoq(dividends)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_039_dividends_ttm_drawdown_accel_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative TTM-dividends drawdown acceleration."""
    d2 = _drv2_dividends_ttm_drawdown_accel(dividends)
    return d2 - d2.shift(_TD_QTR)


def dvd_drv3_040_dps_pct_drawdown_1y_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS 1-year pct-drawdown acceleration."""
    d2 = _drv2_dps_pct_drawdown_1y_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_041_dps_drawdown_3y_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS 3-year drawdown acceleration."""
    d2 = _drv2_dps_drawdown_3y_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_042_dps_omission_frac_1y_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS omission-fraction acceleration."""
    d2 = _drv2_dps_omission_frac_1y_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_043_dps_cut_frac_3y_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS 3-year cut-fraction acceleration."""
    d2 = _drv2_dps_cut_frac_3y_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_044_dps_vs_1y_avg_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS-vs-1y-avg acceleration."""
    d2 = _drv2_dps_vs_1y_avg_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_045_dps_vs_3y_avg_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS-vs-3y-avg acceleration."""
    d2 = _drv2_dps_vs_3y_avg_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_046_dividends_qoq_pct_qoq_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative dividends QoQ-pct acceleration."""
    d2 = _drv2_dividends_qoq_pct_qoq(dividends)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_047_dividends_drawdown_3y_qoq_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative total-dividends 3y drawdown acceleration."""
    d2 = _drv2_dividends_drawdown_3y_qoq(dividends)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_048_yield_zscore_1y_qoq_yoy_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative yield 1y z-score acceleration."""
    d2 = _drv2_yield_zscore_1y_qoq(dps, close)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_049_dps_ttm_zscore_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative TTM DPS z-score acceleration."""
    d2 = _drv2_dps_ttm_zscore_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_050_dividends_ttm_drawdown_accel_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative TTM-dividends drawdown acceleration."""
    d2 = _drv2_dividends_ttm_drawdown_accel(dividends)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_051_dps_qoq_qoq_ewm_yoy(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative QoQ/QoQ DPS EWM-deviation series."""
    base = _drv2_dps_qoq_qoq(dps)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    d2   = base - ewm
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_052_dps_zscore_1y_qoq_ewm_qoq(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DPS z-score EWM-deviation series."""
    m  = _rolling_mean(dps, _TD_YEAR)
    sd = _rolling_std(dps, _TD_YEAR)
    base = _safe_div(dps - m, sd)
    d2 = base - base.shift(_TD_QTR)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    d3  = d2 - ewm
    return d3 - d3.shift(_TD_QTR)


def dvd_drv3_053_dividends_qoq_qoq_ewm_qoq(dividends: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative dividends QoQ/QoQ EWM-deviation series."""
    base = dividends - dividends.shift(_TD_QTR)
    d2   = base - base.shift(_TD_QTR)
    ewm  = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    d3   = d2 - ewm
    return d3 - d3.shift(_TD_QTR)


def dvd_drv3_054_dps_pct_drawdown_3y_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS 3-year pct-drawdown acceleration."""
    d2 = _drv2_dps_pct_drawdown_3y_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_055_yield_zscore_3y_qoq_yoy_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative yield 3y z-score acceleration."""
    d2 = _drv2_yield_zscore_3y_qoq(dps, close)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_056_dps_yoy_qoq_ewm_diff(dps: pd.Series) -> pd.Series:
    """2nd-derivative YoY/QoQ DPS series minus its own 4-quarter EWM."""
    d2  = _drv2_dps_yoy_qoq(dps)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_057_dividends_yoy_qoq_ewm_diff(dividends: pd.Series) -> pd.Series:
    """2nd-derivative dividends YoY/QoQ series minus its own 4-quarter EWM."""
    d2  = _drv2_dividends_yoy_qoq(dividends)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_058_dps_cut_fraction_1y_qoq_ewm_diff(dps: pd.Series) -> pd.Series:
    """2nd-derivative DPS cut-fraction acceleration minus its own 4-quarter EWM."""
    d2  = _drv2_dps_cut_fraction_1y_qoq(dps)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_059_dividends_ttm_qoq_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative TTM total-dividends acceleration."""
    d2 = _drv2_dividends_ttm_qoq(dividends)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_060_dps_ttm_qoq_ewm_diff(dps: pd.Series) -> pd.Series:
    """2nd-derivative TTM DPS acceleration minus its own 4-quarter EWM."""
    d2  = _drv2_dps_ttm_qoq(dps)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_061_dps_zscore_3y_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative DPS 3-year z-score acceleration."""
    d2 = _drv2_dps_zscore_3y_qoq(dps)
    return d2 - d2.shift(_TD_YEAR)


def dvd_drv3_062_dps_drawdown_1y_qoq_2q_diff(dps: pd.Series) -> pd.Series:
    """2-quarter change in the 2nd-derivative DPS drawdown acceleration."""
    d2 = _drv2_dps_drawdown_1y_qoq(dps)
    return d2 - d2.shift(_TD_2Q)


def dvd_drv3_063_dps_zscore_1y_qoq_2q_diff(dps: pd.Series) -> pd.Series:
    """2-quarter change in the 2nd-derivative DPS 1-year z-score acceleration."""
    d2 = _drv2_dps_zscore_1y_qoq(dps)
    return d2 - d2.shift(_TD_2Q)


def dvd_drv3_064_dividends_qoq_qoq_2q_diff(dividends: pd.Series) -> pd.Series:
    """2-quarter change in the 2nd-derivative total-dividends QoQ/QoQ series."""
    d2 = _drv2_dividends_qoq_qoq(dividends)
    return d2 - d2.shift(_TD_2Q)


def dvd_drv3_065_yield_proxy_qoq_2q_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """2-quarter change in the 2nd-derivative yield-proxy QoQ acceleration."""
    d2 = _drv2_yield_proxy_qoq(dps, close)
    return d2 - d2.shift(_TD_2Q)


def dvd_drv3_066_dps_vs_1y_avg_qoq_ewm_diff(dps: pd.Series) -> pd.Series:
    """2nd-derivative DPS-vs-1y-avg acceleration minus its own 4-quarter EWM."""
    d2  = _drv2_dps_vs_1y_avg_qoq(dps)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_067_dps_omission_frac_1y_qoq_ewm_diff(dps: pd.Series) -> pd.Series:
    """2nd-derivative DPS omission-fraction acceleration minus its own 4-quarter EWM."""
    d2  = _drv2_dps_omission_frac_1y_qoq(dps)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_068_dividends_drawdown_1y_qoq_ewm_diff(dividends: pd.Series) -> pd.Series:
    """2nd-derivative total-dividends drawdown acceleration minus its own 4-quarter EWM."""
    d2  = _drv2_dividends_qoq_qoq(dividends)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_069_dps_ttm_drawdown_accel_ewm_diff(dps: pd.Series) -> pd.Series:
    """2nd-derivative TTM-DPS drawdown acceleration minus its own 4-quarter EWM."""
    d2  = _drv2_dps_ttm_drawdown_accel(dps)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_070_dividends_ttm_drawdown_accel_ewm_diff(dividends: pd.Series) -> pd.Series:
    """2nd-derivative TTM-dividends drawdown acceleration minus its own 4-quarter EWM."""
    d2  = _drv2_dividends_ttm_drawdown_accel(dividends)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_071_dps_cut_frac_3y_qoq_ewm_diff(dps: pd.Series) -> pd.Series:
    """2nd-derivative DPS 3-year cut-fraction acceleration minus its own 4-quarter EWM."""
    d2  = _drv2_dps_cut_frac_3y_qoq(dps)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_072_yield_zscore_1y_qoq_ewm_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """2nd-derivative yield 1y z-score acceleration minus its own 4-quarter EWM."""
    d2  = _drv2_yield_zscore_1y_qoq(dps, close)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dvd_drv3_073_dps_drawdown_1y_qoq_qoq_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in 3rd-derivative DPS drawdown acceleration (4th-order check)."""
    d2 = _drv2_dps_drawdown_1y_qoq(dps)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3 - d3.shift(_TD_YEAR)


def dvd_drv3_074_dividends_qoq_qoq_qoq_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the 3rd-derivative total-dividends QoQ/QoQ/QoQ series."""
    d2 = _drv2_dividends_qoq_qoq(dividends)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3 - d3.shift(_TD_YEAR)


def dvd_drv3_075_yield_proxy_qoq_qoq_yoy_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """YoY change in the 3rd-derivative yield-proxy QoQ/QoQ acceleration."""
    d2 = _drv2_yield_proxy_qoq(dps, close)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3 - d3.shift(_TD_YEAR)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

DIVIDEND_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    "dvd_drv3_001_dps_qoq_qoq_qoq_diff":             {"inputs": ["dps"],              "func": dvd_drv3_001_dps_qoq_qoq_qoq_diff},
    "dvd_drv3_002_dps_yoy_qoq_qoq_diff":             {"inputs": ["dps"],              "func": dvd_drv3_002_dps_yoy_qoq_qoq_diff},
    "dvd_drv3_003_dps_qoq_pct_qoq_qoq_diff":         {"inputs": ["dps"],              "func": dvd_drv3_003_dps_qoq_pct_qoq_qoq_diff},
    "dvd_drv3_004_dps_yoy_pct_qoq_qoq_diff":         {"inputs": ["dps"],              "func": dvd_drv3_004_dps_yoy_pct_qoq_qoq_diff},
    "dvd_drv3_005_dps_drawdown_1y_qoq_qoq_diff":     {"inputs": ["dps"],              "func": dvd_drv3_005_dps_drawdown_1y_qoq_qoq_diff},
    "dvd_drv3_006_dps_zscore_1y_qoq_qoq_diff":       {"inputs": ["dps"],              "func": dvd_drv3_006_dps_zscore_1y_qoq_qoq_diff},
    "dvd_drv3_007_dps_zscore_3y_qoq_qoq_diff":       {"inputs": ["dps"],              "func": dvd_drv3_007_dps_zscore_3y_qoq_qoq_diff},
    "dvd_drv3_008_dps_cut_fraction_1y_qoq_qoq_diff": {"inputs": ["dps"],              "func": dvd_drv3_008_dps_cut_fraction_1y_qoq_qoq_diff},
    "dvd_drv3_009_dps_ttm_qoq_qoq_diff":             {"inputs": ["dps"],              "func": dvd_drv3_009_dps_ttm_qoq_qoq_diff},
    "dvd_drv3_010_dividends_qoq_qoq_qoq_diff":       {"inputs": ["dividends"],        "func": dvd_drv3_010_dividends_qoq_qoq_qoq_diff},
    "dvd_drv3_011_dividends_yoy_qoq_qoq_diff":       {"inputs": ["dividends"],        "func": dvd_drv3_011_dividends_yoy_qoq_qoq_diff},
    "dvd_drv3_012_yield_proxy_qoq_qoq_diff":         {"inputs": ["dps", "close"],     "func": dvd_drv3_012_yield_proxy_qoq_qoq_diff},
    "dvd_drv3_013_dps_ttm_drawdown_accel_qoq_diff":  {"inputs": ["dps"],              "func": dvd_drv3_013_dps_ttm_drawdown_accel_qoq_diff},
    "dvd_drv3_014_dps_qoq_qoq_yoy_diff":             {"inputs": ["dps"],              "func": dvd_drv3_014_dps_qoq_qoq_yoy_diff},
    "dvd_drv3_015_dps_yoy_qoq_yoy_diff":             {"inputs": ["dps"],              "func": dvd_drv3_015_dps_yoy_qoq_yoy_diff},
    "dvd_drv3_016_dps_zscore_1y_qoq_yoy_diff":       {"inputs": ["dps"],              "func": dvd_drv3_016_dps_zscore_1y_qoq_yoy_diff},
    "dvd_drv3_017_dps_drawdown_1y_qoq_yoy_diff":     {"inputs": ["dps"],              "func": dvd_drv3_017_dps_drawdown_1y_qoq_yoy_diff},
    "dvd_drv3_018_dividends_qoq_qoq_yoy_diff":       {"inputs": ["dividends"],        "func": dvd_drv3_018_dividends_qoq_qoq_yoy_diff},
    "dvd_drv3_019_dps_qoq_qoq_ewm":                  {"inputs": ["dps"],              "func": dvd_drv3_019_dps_qoq_qoq_ewm},
    "dvd_drv3_020_dividends_qoq_qoq_ewm":            {"inputs": ["dividends"],        "func": dvd_drv3_020_dividends_qoq_qoq_ewm},
    "dvd_drv3_021_dps_zscore_1y_qoq_ewm":            {"inputs": ["dps"],              "func": dvd_drv3_021_dps_zscore_1y_qoq_ewm},
    "dvd_drv3_022_yield_proxy_qoq_yoy_diff":         {"inputs": ["dps", "close"],     "func": dvd_drv3_022_yield_proxy_qoq_yoy_diff},
    "dvd_drv3_023_dps_ttm_qoq_yoy_diff":             {"inputs": ["dps"],              "func": dvd_drv3_023_dps_ttm_qoq_yoy_diff},
    "dvd_drv3_024_dps_cut_fraction_1y_qoq_yoy_diff": {"inputs": ["dps"],              "func": dvd_drv3_024_dps_cut_fraction_1y_qoq_yoy_diff},
    "dvd_drv3_025_dps_ttm_drawdown_accel_yoy_diff":  {"inputs": ["dps"],              "func": dvd_drv3_025_dps_ttm_drawdown_accel_yoy_diff},
    "dvd_drv3_026_dps_pct_drawdown_1y_qoq_qoq_diff": {"inputs": ["dps"],              "func": dvd_drv3_026_dps_pct_drawdown_1y_qoq_qoq_diff},
    "dvd_drv3_027_dps_pct_drawdown_3y_qoq_qoq_diff": {"inputs": ["dps"],              "func": dvd_drv3_027_dps_pct_drawdown_3y_qoq_qoq_diff},
    "dvd_drv3_028_dps_drawdown_3y_qoq_qoq_diff":     {"inputs": ["dps"],              "func": dvd_drv3_028_dps_drawdown_3y_qoq_qoq_diff},
    "dvd_drv3_029_dps_omission_frac_1y_qoq_qoq_diff":{"inputs": ["dps"],              "func": dvd_drv3_029_dps_omission_frac_1y_qoq_qoq_diff},
    "dvd_drv3_030_dps_cut_frac_3y_qoq_qoq_diff":     {"inputs": ["dps"],              "func": dvd_drv3_030_dps_cut_frac_3y_qoq_qoq_diff},
    "dvd_drv3_031_dps_vs_1y_avg_qoq_qoq_diff":       {"inputs": ["dps"],              "func": dvd_drv3_031_dps_vs_1y_avg_qoq_qoq_diff},
    "dvd_drv3_032_dps_vs_3y_avg_qoq_qoq_diff":       {"inputs": ["dps"],              "func": dvd_drv3_032_dps_vs_3y_avg_qoq_qoq_diff},
    "dvd_drv3_033_dividends_qoq_pct_qoq_qoq_diff":   {"inputs": ["dividends"],        "func": dvd_drv3_033_dividends_qoq_pct_qoq_qoq_diff},
    "dvd_drv3_034_dividends_drawdown_3y_qoq_qoq_diff":{"inputs": ["dividends"],       "func": dvd_drv3_034_dividends_drawdown_3y_qoq_qoq_diff},
    "dvd_drv3_035_yield_zscore_1y_qoq_qoq_diff":     {"inputs": ["dps", "close"],     "func": dvd_drv3_035_yield_zscore_1y_qoq_qoq_diff},
    "dvd_drv3_036_yield_zscore_3y_qoq_qoq_diff":     {"inputs": ["dps", "close"],     "func": dvd_drv3_036_yield_zscore_3y_qoq_qoq_diff},
    "dvd_drv3_037_dps_ttm_zscore_qoq_qoq_diff":      {"inputs": ["dps"],              "func": dvd_drv3_037_dps_ttm_zscore_qoq_qoq_diff},
    "dvd_drv3_038_dividends_ttm_qoq_qoq_diff":       {"inputs": ["dividends"],        "func": dvd_drv3_038_dividends_ttm_qoq_qoq_diff},
    "dvd_drv3_039_dividends_ttm_drawdown_accel_qoq_diff":{"inputs": ["dividends"],    "func": dvd_drv3_039_dividends_ttm_drawdown_accel_qoq_diff},
    "dvd_drv3_040_dps_pct_drawdown_1y_qoq_yoy_diff": {"inputs": ["dps"],              "func": dvd_drv3_040_dps_pct_drawdown_1y_qoq_yoy_diff},
    "dvd_drv3_041_dps_drawdown_3y_qoq_yoy_diff":     {"inputs": ["dps"],              "func": dvd_drv3_041_dps_drawdown_3y_qoq_yoy_diff},
    "dvd_drv3_042_dps_omission_frac_1y_qoq_yoy_diff":{"inputs": ["dps"],              "func": dvd_drv3_042_dps_omission_frac_1y_qoq_yoy_diff},
    "dvd_drv3_043_dps_cut_frac_3y_qoq_yoy_diff":     {"inputs": ["dps"],              "func": dvd_drv3_043_dps_cut_frac_3y_qoq_yoy_diff},
    "dvd_drv3_044_dps_vs_1y_avg_qoq_yoy_diff":       {"inputs": ["dps"],              "func": dvd_drv3_044_dps_vs_1y_avg_qoq_yoy_diff},
    "dvd_drv3_045_dps_vs_3y_avg_qoq_yoy_diff":       {"inputs": ["dps"],              "func": dvd_drv3_045_dps_vs_3y_avg_qoq_yoy_diff},
    "dvd_drv3_046_dividends_qoq_pct_qoq_yoy_diff":   {"inputs": ["dividends"],        "func": dvd_drv3_046_dividends_qoq_pct_qoq_yoy_diff},
    "dvd_drv3_047_dividends_drawdown_3y_qoq_yoy_diff":{"inputs": ["dividends"],       "func": dvd_drv3_047_dividends_drawdown_3y_qoq_yoy_diff},
    "dvd_drv3_048_yield_zscore_1y_qoq_yoy_diff":     {"inputs": ["dps", "close"],     "func": dvd_drv3_048_yield_zscore_1y_qoq_yoy_diff},
    "dvd_drv3_049_dps_ttm_zscore_qoq_yoy_diff":      {"inputs": ["dps"],              "func": dvd_drv3_049_dps_ttm_zscore_qoq_yoy_diff},
    "dvd_drv3_050_dividends_ttm_drawdown_accel_yoy_diff":{"inputs": ["dividends"],    "func": dvd_drv3_050_dividends_ttm_drawdown_accel_yoy_diff},
    "dvd_drv3_051_dps_qoq_qoq_ewm_yoy":              {"inputs": ["dps"],              "func": dvd_drv3_051_dps_qoq_qoq_ewm_yoy},
    "dvd_drv3_052_dps_zscore_1y_qoq_ewm_qoq":        {"inputs": ["dps"],              "func": dvd_drv3_052_dps_zscore_1y_qoq_ewm_qoq},
    "dvd_drv3_053_dividends_qoq_qoq_ewm_qoq":        {"inputs": ["dividends"],        "func": dvd_drv3_053_dividends_qoq_qoq_ewm_qoq},
    "dvd_drv3_054_dps_pct_drawdown_3y_qoq_yoy_diff": {"inputs": ["dps"],              "func": dvd_drv3_054_dps_pct_drawdown_3y_qoq_yoy_diff},
    "dvd_drv3_055_yield_zscore_3y_qoq_yoy_diff":     {"inputs": ["dps", "close"],     "func": dvd_drv3_055_yield_zscore_3y_qoq_yoy_diff},
    "dvd_drv3_056_dps_yoy_qoq_ewm_diff":             {"inputs": ["dps"],              "func": dvd_drv3_056_dps_yoy_qoq_ewm_diff},
    "dvd_drv3_057_dividends_yoy_qoq_ewm_diff":       {"inputs": ["dividends"],        "func": dvd_drv3_057_dividends_yoy_qoq_ewm_diff},
    "dvd_drv3_058_dps_cut_fraction_1y_qoq_ewm_diff": {"inputs": ["dps"],              "func": dvd_drv3_058_dps_cut_fraction_1y_qoq_ewm_diff},
    "dvd_drv3_059_dividends_ttm_qoq_yoy_diff":       {"inputs": ["dividends"],        "func": dvd_drv3_059_dividends_ttm_qoq_yoy_diff},
    "dvd_drv3_060_dps_ttm_qoq_ewm_diff":             {"inputs": ["dps"],              "func": dvd_drv3_060_dps_ttm_qoq_ewm_diff},
    "dvd_drv3_061_dps_zscore_3y_qoq_yoy_diff":       {"inputs": ["dps"],              "func": dvd_drv3_061_dps_zscore_3y_qoq_yoy_diff},
    "dvd_drv3_062_dps_drawdown_1y_qoq_2q_diff":      {"inputs": ["dps"],              "func": dvd_drv3_062_dps_drawdown_1y_qoq_2q_diff},
    "dvd_drv3_063_dps_zscore_1y_qoq_2q_diff":        {"inputs": ["dps"],              "func": dvd_drv3_063_dps_zscore_1y_qoq_2q_diff},
    "dvd_drv3_064_dividends_qoq_qoq_2q_diff":        {"inputs": ["dividends"],        "func": dvd_drv3_064_dividends_qoq_qoq_2q_diff},
    "dvd_drv3_065_yield_proxy_qoq_2q_diff":          {"inputs": ["dps", "close"],     "func": dvd_drv3_065_yield_proxy_qoq_2q_diff},
    "dvd_drv3_066_dps_vs_1y_avg_qoq_ewm_diff":       {"inputs": ["dps"],              "func": dvd_drv3_066_dps_vs_1y_avg_qoq_ewm_diff},
    "dvd_drv3_067_dps_omission_frac_1y_qoq_ewm_diff":{"inputs": ["dps"],              "func": dvd_drv3_067_dps_omission_frac_1y_qoq_ewm_diff},
    "dvd_drv3_068_dividends_drawdown_1y_qoq_ewm_diff":{"inputs": ["dividends"],       "func": dvd_drv3_068_dividends_drawdown_1y_qoq_ewm_diff},
    "dvd_drv3_069_dps_ttm_drawdown_accel_ewm_diff":  {"inputs": ["dps"],              "func": dvd_drv3_069_dps_ttm_drawdown_accel_ewm_diff},
    "dvd_drv3_070_dividends_ttm_drawdown_accel_ewm_diff":{"inputs": ["dividends"],    "func": dvd_drv3_070_dividends_ttm_drawdown_accel_ewm_diff},
    "dvd_drv3_071_dps_cut_frac_3y_qoq_ewm_diff":     {"inputs": ["dps"],              "func": dvd_drv3_071_dps_cut_frac_3y_qoq_ewm_diff},
    "dvd_drv3_072_yield_zscore_1y_qoq_ewm_diff":     {"inputs": ["dps", "close"],     "func": dvd_drv3_072_yield_zscore_1y_qoq_ewm_diff},
    "dvd_drv3_073_dps_drawdown_1y_qoq_qoq_yoy_diff": {"inputs": ["dps"],              "func": dvd_drv3_073_dps_drawdown_1y_qoq_qoq_yoy_diff},
    "dvd_drv3_074_dividends_qoq_qoq_qoq_yoy_diff":   {"inputs": ["dividends"],        "func": dvd_drv3_074_dividends_qoq_qoq_qoq_yoy_diff},
    "dvd_drv3_075_yield_proxy_qoq_qoq_yoy_diff":     {"inputs": ["dps", "close"],     "func": dvd_drv3_075_yield_proxy_qoq_qoq_yoy_diff},
}
