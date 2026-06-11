"""
96_dividend_distress — 2nd-Derivative Features 001-025
Domain: rate of change of base dividend-distress features (acceleration)
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to a shared trading-day index.
Quarterly Sharadar SF1 fields are forward-filled to the daily index so that
flat stretches between report dates are correct and expected.
The 2nd-derivative series are sparse/stepwise on a daily index because the
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


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# These inline the relevant base computations so this file needs no cross-import.

def _dps_qoq(dps: pd.Series) -> pd.Series:
    return dps - dps.shift(_TD_QTR)


def _dps_yoy(dps: pd.Series) -> pd.Series:
    return dps - dps.shift(_TD_YEAR)


def _dps_qoq_pct(dps: pd.Series) -> pd.Series:
    prior = dps.shift(_TD_QTR)
    return _safe_div_abs(dps - prior, prior)


def _dps_yoy_pct(dps: pd.Series) -> pd.Series:
    prior = dps.shift(_TD_YEAR)
    return _safe_div_abs(dps - prior, prior)


def _dps_drawdown_from_1y_peak(dps: pd.Series) -> pd.Series:
    return dps - _rolling_max(dps, _TD_YEAR)


def _dps_zscore_1y(dps: pd.Series) -> pd.Series:
    m  = _rolling_mean(dps, _TD_YEAR)
    sd = _rolling_std(dps, _TD_YEAR)
    return _safe_div(dps - m, sd)


def _dps_zscore_3y(dps: pd.Series) -> pd.Series:
    m  = _rolling_mean(dps, _TD_3Y)
    sd = _rolling_std(dps, _TD_3Y)
    return _safe_div(dps - m, sd)


def _dps_cut_fraction_1y(dps: pd.Series) -> pd.Series:
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return cut.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()


def _div_yield_proxy(dps: pd.Series, close: pd.Series) -> pd.Series:
    return dps * 4.0 / close.replace(0, np.nan)


def _dividends_qoq(dividends: pd.Series) -> pd.Series:
    return dividends - dividends.shift(_TD_QTR)


def _dividends_yoy(dividends: pd.Series) -> pd.Series:
    return dividends - dividends.shift(_TD_YEAR)


def _dividends_drawdown_1y(dividends: pd.Series) -> pd.Series:
    return dividends - _rolling_max(dividends, _TD_YEAR)


def _dps_ttm(dps: pd.Series) -> pd.Series:
    return dps.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def dvd_drv2_001_dps_qoq_change_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the QoQ DPS change (acceleration of QoQ dividend trend)."""
    base = _dps_qoq(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_002_dps_yoy_change_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the YoY DPS change (how fast the YoY trend is shifting)."""
    base = _dps_yoy(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_003_dps_qoq_pct_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the QoQ percent change of DPS."""
    base = _dps_qoq_pct(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_004_dps_yoy_pct_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the YoY percent change of DPS."""
    base = _dps_yoy_pct(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_005_dps_yoy_pct_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the YoY percent change of DPS (2nd-order YoY)."""
    base = _dps_yoy_pct(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_006_dps_drawdown_1y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 1-year-peak drawdown of DPS."""
    base = _dps_drawdown_from_1y_peak(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_007_dps_drawdown_1y_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 1-year-peak drawdown of DPS."""
    base = _dps_drawdown_from_1y_peak(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_008_dps_zscore_1y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 1-year z-score of DPS."""
    base = _dps_zscore_1y(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_009_dps_zscore_1y_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 1-year z-score of DPS."""
    base = _dps_zscore_1y(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_010_dps_zscore_3y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 3-year z-score of DPS."""
    base = _dps_zscore_3y(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_011_dps_cut_fraction_1y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 1-year cut-fraction of DPS."""
    base = _dps_cut_fraction_1y(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_012_dps_ttm_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the trailing-12-month DPS sum."""
    base = _dps_ttm(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_013_dps_ttm_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the trailing-12-month DPS sum."""
    base = _dps_ttm(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_014_dividends_qoq_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the QoQ total-dividends change (payout acceleration)."""
    base = _dividends_qoq(dividends)
    return base - base.shift(_TD_QTR)


def dvd_drv2_015_dividends_yoy_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the YoY total-dividends change."""
    base = _dividends_yoy(dividends)
    return base - base.shift(_TD_QTR)


def dvd_drv2_016_dividends_drawdown_1y_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the 1-year-peak drawdown of total dividends."""
    base = _dividends_drawdown_1y(dividends)
    return base - base.shift(_TD_QTR)


def dvd_drv2_017_yield_proxy_qoq_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in the DPS/close yield proxy (yield drift acceleration)."""
    base = _div_yield_proxy(dps, close)
    return base - base.shift(_TD_QTR)


def dvd_drv2_018_yield_proxy_yoy_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """YoY change in the DPS/close yield proxy."""
    base = _div_yield_proxy(dps, close)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_019_dps_qoq_slope_of_qoq(dps: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the QoQ DPS change series.
    Captures the trend in QoQ dividend momentum.
    """
    base = _dps_qoq(dps)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def dvd_drv2_020_dps_drawdown_pct_1y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in (DPS percent drawdown from 1-year peak)."""
    peak = _rolling_max(dps, _TD_YEAR)
    base = _safe_div_abs(dps - peak, peak)
    return base - base.shift(_TD_QTR)


def dvd_drv2_021_dps_qoq_ewm_diff(dps: pd.Series) -> pd.Series:
    """
    Current QoQ DPS change minus its own 4-quarter EWM (span=252).
    Measures whether the current QoQ cut is worse than recent trend.
    """
    base = _dps_qoq(dps)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def dvd_drv2_022_dividends_qoq_ewm_diff(dividends: pd.Series) -> pd.Series:
    """Current QoQ total-dividends change minus its own 4-quarter EWM."""
    base = _dividends_qoq(dividends)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def dvd_drv2_023_dps_ttm_drawdown_accel(dps: pd.Series) -> pd.Series:
    """
    QoQ change in TTM-DPS drawdown from its expanding peak (2nd order):
    d/dq [(TTM_dps - expanding_max(TTM_dps))].
    """
    ttm  = _dps_ttm(dps)
    peak = ttm.expanding(min_periods=1).max()
    base = ttm - peak
    return base - base.shift(_TD_QTR)


def dvd_drv2_024_dps_cut_fraction_3y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 3-year cut-fraction of DPS."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    base = cut.rolling(_TD_3Y, min_periods=max(1, _TD_3Y // 4)).mean()
    return base - base.shift(_TD_QTR)


def dvd_drv2_025_yield_proxy_zscore_1y_qoq_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in the 1-year z-score of the DPS/close yield proxy."""
    y    = _div_yield_proxy(dps, close)
    m    = _rolling_mean(y, _TD_YEAR)
    sd   = _rolling_std(y, _TD_YEAR)
    base = _safe_div(y - m, sd)
    return base - base.shift(_TD_QTR)


# ── Additional base helpers for 026-075 ──────────────────────────────────────

def _dps_2q(dps: pd.Series) -> pd.Series:
    return dps - dps.shift(_TD_2Q)


def _dps_drawdown_3y_peak(dps: pd.Series) -> pd.Series:
    return dps - _rolling_max(dps, _TD_3Y)


def _dps_pct_drawdown_1y(dps: pd.Series) -> pd.Series:
    peak = _rolling_max(dps, _TD_YEAR)
    return _safe_div_abs(dps - peak, peak)


def _dps_pct_drawdown_3y(dps: pd.Series) -> pd.Series:
    peak = _rolling_max(dps, _TD_3Y)
    return _safe_div_abs(dps - peak, peak)


def _dps_cut_fraction_3y(dps: pd.Series) -> pd.Series:
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return cut.rolling(_TD_3Y, min_periods=max(1, _TD_3Y // 4)).mean()


def _dps_omission_frac_1y(dps: pd.Series) -> pd.Series:
    zero = (dps <= 0).astype(float)
    return zero.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()


def _dps_ewm_short(dps: pd.Series) -> pd.Series:
    return dps - dps.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()


def _dps_ewm_long(dps: pd.Series) -> pd.Series:
    return dps - dps.ewm(span=_TD_2Y, min_periods=max(1, _TD_2Y // 4)).mean()


def _dividends_drawdown_3y(dividends: pd.Series) -> pd.Series:
    return dividends - _rolling_max(dividends, _TD_3Y)


def _dividends_qoq_pct(dividends: pd.Series) -> pd.Series:
    prior = dividends.shift(_TD_QTR)
    return _safe_div_abs(dividends - prior, prior)


def _dividends_yoy_pct(dividends: pd.Series) -> pd.Series:
    prior = dividends.shift(_TD_YEAR)
    return _safe_div_abs(dividends - prior, prior)


def _div_yield_zscore_1y(dps: pd.Series, close: pd.Series) -> pd.Series:
    y = _div_yield_proxy(dps, close)
    m = _rolling_mean(y, _TD_YEAR)
    sd = _rolling_std(y, _TD_YEAR)
    return _safe_div(y - m, sd)


def _div_yield_zscore_3y(dps: pd.Series, close: pd.Series) -> pd.Series:
    y = _div_yield_proxy(dps, close)
    m = _rolling_mean(y, _TD_3Y)
    sd = _rolling_std(y, _TD_3Y)
    return _safe_div(y - m, sd)


def _dps_vs_1y_avg(dps: pd.Series) -> pd.Series:
    return dps - _rolling_mean(dps, _TD_YEAR)


def _dps_vs_3y_avg(dps: pd.Series) -> pd.Series:
    return dps - _rolling_mean(dps, _TD_3Y)


# ── 2nd-derivative feature functions 026-075 ─────────────────────────────────

def dvd_drv2_026_dps_2q_change_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 2-quarter DPS change (acceleration of 2Q trend)."""
    base = _dps_2q(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_027_dps_drawdown_3y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 3-year-peak DPS drawdown."""
    base = _dps_drawdown_3y_peak(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_028_dps_pct_drawdown_1y_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 1-year percent DPS drawdown."""
    base = _dps_pct_drawdown_1y(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_029_dps_pct_drawdown_3y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 3-year percent DPS drawdown."""
    base = _dps_pct_drawdown_3y(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_030_dps_zscore_3y_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 3-year z-score of DPS."""
    base = _dps_zscore_3y(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_031_dps_cut_fraction_3y_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 3-year cut-fraction of DPS."""
    base = _dps_cut_fraction_3y(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_032_dps_omission_frac_1y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in the 1-year DPS omission fraction."""
    base = _dps_omission_frac_1y(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_033_dps_omission_frac_1y_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 1-year DPS omission fraction."""
    base = _dps_omission_frac_1y(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_034_dps_ewm_short_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in DPS short-EWM deviation (1-quarter span)."""
    base = _dps_ewm_short(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_035_dps_ewm_long_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in DPS long-EWM deviation (2-year span)."""
    base = _dps_ewm_long(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_036_dps_vs_1y_avg_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in DPS vs its trailing 1-year mean."""
    base = _dps_vs_1y_avg(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_037_dps_vs_1y_avg_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in DPS vs its trailing 1-year mean."""
    base = _dps_vs_1y_avg(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_038_dps_vs_3y_avg_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in DPS vs its trailing 3-year mean."""
    base = _dps_vs_3y_avg(dps)
    return base - base.shift(_TD_QTR)


def dvd_drv2_039_dps_qoq_zscore_1y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in rolling 1-year z-score of the QoQ DPS change series."""
    qoq = _dps_qoq(dps)
    m   = _rolling_mean(qoq, _TD_YEAR)
    sd  = _rolling_std(qoq, _TD_YEAR)
    base = _safe_div(qoq - m, sd)
    return base - base.shift(_TD_QTR)


def dvd_drv2_040_dps_yoy_zscore_1y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in rolling 1-year z-score of the YoY DPS change series."""
    yoy = _dps_yoy(dps)
    m   = _rolling_mean(yoy, _TD_YEAR)
    sd  = _rolling_std(yoy, _TD_YEAR)
    base = _safe_div(yoy - m, sd)
    return base - base.shift(_TD_QTR)


def dvd_drv2_041_dividends_drawdown_3y_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the 3-year-peak drawdown of total dividends."""
    base = _dividends_drawdown_3y(dividends)
    return base - base.shift(_TD_QTR)


def dvd_drv2_042_dividends_qoq_pct_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the QoQ percent change of total dividends."""
    base = _dividends_qoq_pct(dividends)
    return base - base.shift(_TD_QTR)


def dvd_drv2_043_dividends_yoy_pct_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the YoY percent change of total dividends."""
    base = _dividends_yoy_pct(dividends)
    return base - base.shift(_TD_QTR)


def dvd_drv2_044_dividends_yoy_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the YoY total-dividends change (2nd-order annual)."""
    base = _dividends_yoy(dividends)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_045_dividends_drawdown_1y_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the 1-year-peak drawdown of total dividends."""
    base = _dividends_drawdown_1y(dividends)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_046_yield_proxy_zscore_3y_qoq_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in the 3-year z-score of the DPS/close yield proxy."""
    base = _div_yield_zscore_3y(dps, close)
    return base - base.shift(_TD_QTR)


def dvd_drv2_047_yield_proxy_zscore_1y_yoy_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """YoY change in the 1-year z-score of the DPS/close yield proxy."""
    base = _div_yield_zscore_1y(dps, close)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_048_yield_proxy_zscore_3y_yoy_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """YoY change in the 3-year z-score of the DPS/close yield proxy."""
    base = _div_yield_zscore_3y(dps, close)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_049_dps_ttm_pct_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in TTM-DPS percent change QoQ (rate of TTM momentum)."""
    ttm  = _dps_ttm(dps)
    pct  = _safe_div_abs(ttm - ttm.shift(_TD_QTR), ttm.shift(_TD_QTR))
    return pct - pct.shift(_TD_QTR)


def dvd_drv2_050_dps_ttm_zscore_1y_qoq_diff(dps: pd.Series) -> pd.Series:
    """QoQ change in rolling 1-year z-score of TTM DPS."""
    ttm  = _dps_ttm(dps)
    m    = _rolling_mean(ttm, _TD_YEAR)
    sd   = _rolling_std(ttm, _TD_YEAR)
    base = _safe_div(ttm - m, sd)
    return base - base.shift(_TD_QTR)


def dvd_drv2_051_dps_drawdown_3y_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 3-year-peak DPS drawdown."""
    base = _dps_drawdown_3y_peak(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_052_dps_2q_change_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 2-quarter DPS change."""
    base = _dps_2q(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_053_dps_qoq_slope_1q(dps: pd.Series) -> pd.Series:
    """Rolling 1-quarter OLS slope of the QoQ DPS change series (short trend)."""
    base = _dps_qoq(dps)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def dvd_drv2_054_dividends_ttm_qoq_diff(dividends: pd.Series) -> pd.Series:
    """QoQ change in the trailing-12-month total-dividends sum."""
    ttm = dividends.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    return ttm - ttm.shift(_TD_QTR)


def dvd_drv2_055_dividends_ttm_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the trailing-12-month total-dividends sum."""
    ttm = dividends.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    return ttm - ttm.shift(_TD_YEAR)


def dvd_drv2_056_yield_proxy_qoq_ewm_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ yield-proxy change minus its own 4-quarter EWM (yield momentum deviation)."""
    y   = _div_yield_proxy(dps, close)
    qoq = y - y.shift(_TD_QTR)
    ewm = qoq.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return qoq - ewm


def dvd_drv2_057_dps_zscore_1y_ewm_diff(dps: pd.Series) -> pd.Series:
    """1-year DPS z-score minus its own 4-quarter EWM (z-score momentum)."""
    base = _dps_zscore_1y(dps)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def dvd_drv2_058_dps_cut_fraction_1y_ewm_diff(dps: pd.Series) -> pd.Series:
    """1-year DPS cut-fraction minus its own 4-quarter EWM."""
    base = _dps_cut_fraction_1y(dps)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def dvd_drv2_059_dps_omission_frac_1y_ewm_diff(dps: pd.Series) -> pd.Series:
    """1-year DPS omission fraction minus its own 4-quarter EWM."""
    base = _dps_omission_frac_1y(dps)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def dvd_drv2_060_dividends_qoq_pct_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the QoQ percent change of total dividends."""
    base = _dividends_qoq_pct(dividends)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_061_dps_drawdown_1y_2q_diff(dps: pd.Series) -> pd.Series:
    """2-quarter change in the 1-year-peak DPS drawdown (semi-annual acceleration)."""
    base = _dps_drawdown_from_1y_peak(dps)
    return base - base.shift(_TD_2Q)


def dvd_drv2_062_dps_zscore_1y_2q_diff(dps: pd.Series) -> pd.Series:
    """2-quarter change in the 1-year z-score of DPS."""
    base = _dps_zscore_1y(dps)
    return base - base.shift(_TD_2Q)


def dvd_drv2_063_yield_proxy_2q_diff(dps: pd.Series, close: pd.Series) -> pd.Series:
    """2-quarter change in the DPS/close yield proxy."""
    base = _div_yield_proxy(dps, close)
    return base - base.shift(_TD_2Q)


def dvd_drv2_064_dividends_qoq_2q_diff(dividends: pd.Series) -> pd.Series:
    """2-quarter change in the QoQ total-dividends change."""
    base = _dividends_qoq(dividends)
    return base - base.shift(_TD_2Q)


def dvd_drv2_065_dps_qoq_pct_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the QoQ percent change of DPS."""
    base = _dps_qoq_pct(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_066_dps_ttm_drawdown_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in TTM-DPS drawdown from its expanding peak."""
    ttm  = _dps_ttm(dps)
    peak = ttm.expanding(min_periods=1).max()
    base = ttm - peak
    return base - base.shift(_TD_YEAR)


def dvd_drv2_067_dividends_yoy_ewm_diff(dividends: pd.Series) -> pd.Series:
    """YoY total-dividends change minus its own 4-quarter EWM."""
    base = _dividends_yoy(dividends)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def dvd_drv2_068_dps_vs_3y_avg_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in DPS vs its trailing 3-year mean."""
    base = _dps_vs_3y_avg(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_069_dps_zscore_3y_ewm_diff(dps: pd.Series) -> pd.Series:
    """3-year DPS z-score minus its own 4-quarter EWM."""
    base = _dps_zscore_3y(dps)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def dvd_drv2_070_dividends_ttm_drawdown_accel(dividends: pd.Series) -> pd.Series:
    """QoQ change in TTM-dividends drawdown from expanding peak (2nd order)."""
    ttm  = dividends.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    peak = ttm.expanding(min_periods=1).max()
    base = ttm - peak
    return base - base.shift(_TD_QTR)


def dvd_drv2_071_dps_pct_drawdown_3y_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in the 3-year percent DPS drawdown."""
    base = _dps_pct_drawdown_3y(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_072_dps_ewm_short_yoy_diff(dps: pd.Series) -> pd.Series:
    """YoY change in DPS short-EWM deviation (1-quarter span)."""
    base = _dps_ewm_short(dps)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_073_dps_cut_fraction_3y_ewm_diff(dps: pd.Series) -> pd.Series:
    """3-year DPS cut-fraction minus its own 4-quarter EWM."""
    base = _dps_cut_fraction_3y(dps)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def dvd_drv2_074_dividends_drawdown_3y_yoy_diff(dividends: pd.Series) -> pd.Series:
    """YoY change in the 3-year-peak drawdown of total dividends."""
    base = _dividends_drawdown_3y(dividends)
    return base - base.shift(_TD_YEAR)


def dvd_drv2_075_dps_qoq_pct_ewm_diff(dps: pd.Series) -> pd.Series:
    """QoQ DPS pct-change minus its own 4-quarter EWM (pct-momentum deviation)."""
    base = _dps_qoq_pct(dps)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

DIVIDEND_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    "dvd_drv2_001_dps_qoq_change_qoq_diff":          {"inputs": ["dps"],              "func": dvd_drv2_001_dps_qoq_change_qoq_diff},
    "dvd_drv2_002_dps_yoy_change_qoq_diff":          {"inputs": ["dps"],              "func": dvd_drv2_002_dps_yoy_change_qoq_diff},
    "dvd_drv2_003_dps_qoq_pct_qoq_diff":             {"inputs": ["dps"],              "func": dvd_drv2_003_dps_qoq_pct_qoq_diff},
    "dvd_drv2_004_dps_yoy_pct_qoq_diff":             {"inputs": ["dps"],              "func": dvd_drv2_004_dps_yoy_pct_qoq_diff},
    "dvd_drv2_005_dps_yoy_pct_yoy_diff":             {"inputs": ["dps"],              "func": dvd_drv2_005_dps_yoy_pct_yoy_diff},
    "dvd_drv2_006_dps_drawdown_1y_qoq_diff":         {"inputs": ["dps"],              "func": dvd_drv2_006_dps_drawdown_1y_qoq_diff},
    "dvd_drv2_007_dps_drawdown_1y_yoy_diff":         {"inputs": ["dps"],              "func": dvd_drv2_007_dps_drawdown_1y_yoy_diff},
    "dvd_drv2_008_dps_zscore_1y_qoq_diff":           {"inputs": ["dps"],              "func": dvd_drv2_008_dps_zscore_1y_qoq_diff},
    "dvd_drv2_009_dps_zscore_1y_yoy_diff":           {"inputs": ["dps"],              "func": dvd_drv2_009_dps_zscore_1y_yoy_diff},
    "dvd_drv2_010_dps_zscore_3y_qoq_diff":           {"inputs": ["dps"],              "func": dvd_drv2_010_dps_zscore_3y_qoq_diff},
    "dvd_drv2_011_dps_cut_fraction_1y_qoq_diff":     {"inputs": ["dps"],              "func": dvd_drv2_011_dps_cut_fraction_1y_qoq_diff},
    "dvd_drv2_012_dps_ttm_qoq_diff":                 {"inputs": ["dps"],              "func": dvd_drv2_012_dps_ttm_qoq_diff},
    "dvd_drv2_013_dps_ttm_yoy_diff":                 {"inputs": ["dps"],              "func": dvd_drv2_013_dps_ttm_yoy_diff},
    "dvd_drv2_014_dividends_qoq_qoq_diff":           {"inputs": ["dividends"],        "func": dvd_drv2_014_dividends_qoq_qoq_diff},
    "dvd_drv2_015_dividends_yoy_qoq_diff":           {"inputs": ["dividends"],        "func": dvd_drv2_015_dividends_yoy_qoq_diff},
    "dvd_drv2_016_dividends_drawdown_1y_qoq_diff":   {"inputs": ["dividends"],        "func": dvd_drv2_016_dividends_drawdown_1y_qoq_diff},
    "dvd_drv2_017_yield_proxy_qoq_diff":             {"inputs": ["dps", "close"],     "func": dvd_drv2_017_yield_proxy_qoq_diff},
    "dvd_drv2_018_yield_proxy_yoy_diff":             {"inputs": ["dps", "close"],     "func": dvd_drv2_018_yield_proxy_yoy_diff},
    "dvd_drv2_019_dps_qoq_slope_of_qoq":             {"inputs": ["dps"],              "func": dvd_drv2_019_dps_qoq_slope_of_qoq},
    "dvd_drv2_020_dps_drawdown_pct_1y_qoq_diff":     {"inputs": ["dps"],              "func": dvd_drv2_020_dps_drawdown_pct_1y_qoq_diff},
    "dvd_drv2_021_dps_qoq_ewm_diff":                 {"inputs": ["dps"],              "func": dvd_drv2_021_dps_qoq_ewm_diff},
    "dvd_drv2_022_dividends_qoq_ewm_diff":           {"inputs": ["dividends"],        "func": dvd_drv2_022_dividends_qoq_ewm_diff},
    "dvd_drv2_023_dps_ttm_drawdown_accel":           {"inputs": ["dps"],              "func": dvd_drv2_023_dps_ttm_drawdown_accel},
    "dvd_drv2_024_dps_cut_fraction_3y_qoq_diff":     {"inputs": ["dps"],              "func": dvd_drv2_024_dps_cut_fraction_3y_qoq_diff},
    "dvd_drv2_025_yield_proxy_zscore_1y_qoq_diff":   {"inputs": ["dps", "close"],     "func": dvd_drv2_025_yield_proxy_zscore_1y_qoq_diff},
    "dvd_drv2_026_dps_2q_change_qoq_diff":           {"inputs": ["dps"],              "func": dvd_drv2_026_dps_2q_change_qoq_diff},
    "dvd_drv2_027_dps_drawdown_3y_qoq_diff":         {"inputs": ["dps"],              "func": dvd_drv2_027_dps_drawdown_3y_qoq_diff},
    "dvd_drv2_028_dps_pct_drawdown_1y_yoy_diff":     {"inputs": ["dps"],              "func": dvd_drv2_028_dps_pct_drawdown_1y_yoy_diff},
    "dvd_drv2_029_dps_pct_drawdown_3y_qoq_diff":     {"inputs": ["dps"],              "func": dvd_drv2_029_dps_pct_drawdown_3y_qoq_diff},
    "dvd_drv2_030_dps_zscore_3y_yoy_diff":           {"inputs": ["dps"],              "func": dvd_drv2_030_dps_zscore_3y_yoy_diff},
    "dvd_drv2_031_dps_cut_fraction_3y_yoy_diff":     {"inputs": ["dps"],              "func": dvd_drv2_031_dps_cut_fraction_3y_yoy_diff},
    "dvd_drv2_032_dps_omission_frac_1y_qoq_diff":    {"inputs": ["dps"],              "func": dvd_drv2_032_dps_omission_frac_1y_qoq_diff},
    "dvd_drv2_033_dps_omission_frac_1y_yoy_diff":    {"inputs": ["dps"],              "func": dvd_drv2_033_dps_omission_frac_1y_yoy_diff},
    "dvd_drv2_034_dps_ewm_short_qoq_diff":           {"inputs": ["dps"],              "func": dvd_drv2_034_dps_ewm_short_qoq_diff},
    "dvd_drv2_035_dps_ewm_long_qoq_diff":            {"inputs": ["dps"],              "func": dvd_drv2_035_dps_ewm_long_qoq_diff},
    "dvd_drv2_036_dps_vs_1y_avg_qoq_diff":           {"inputs": ["dps"],              "func": dvd_drv2_036_dps_vs_1y_avg_qoq_diff},
    "dvd_drv2_037_dps_vs_1y_avg_yoy_diff":           {"inputs": ["dps"],              "func": dvd_drv2_037_dps_vs_1y_avg_yoy_diff},
    "dvd_drv2_038_dps_vs_3y_avg_qoq_diff":           {"inputs": ["dps"],              "func": dvd_drv2_038_dps_vs_3y_avg_qoq_diff},
    "dvd_drv2_039_dps_qoq_zscore_1y_qoq_diff":       {"inputs": ["dps"],              "func": dvd_drv2_039_dps_qoq_zscore_1y_qoq_diff},
    "dvd_drv2_040_dps_yoy_zscore_1y_qoq_diff":       {"inputs": ["dps"],              "func": dvd_drv2_040_dps_yoy_zscore_1y_qoq_diff},
    "dvd_drv2_041_dividends_drawdown_3y_qoq_diff":   {"inputs": ["dividends"],        "func": dvd_drv2_041_dividends_drawdown_3y_qoq_diff},
    "dvd_drv2_042_dividends_qoq_pct_qoq_diff":       {"inputs": ["dividends"],        "func": dvd_drv2_042_dividends_qoq_pct_qoq_diff},
    "dvd_drv2_043_dividends_yoy_pct_qoq_diff":       {"inputs": ["dividends"],        "func": dvd_drv2_043_dividends_yoy_pct_qoq_diff},
    "dvd_drv2_044_dividends_yoy_yoy_diff":           {"inputs": ["dividends"],        "func": dvd_drv2_044_dividends_yoy_yoy_diff},
    "dvd_drv2_045_dividends_drawdown_1y_yoy_diff":   {"inputs": ["dividends"],        "func": dvd_drv2_045_dividends_drawdown_1y_yoy_diff},
    "dvd_drv2_046_yield_proxy_zscore_3y_qoq_diff":   {"inputs": ["dps", "close"],     "func": dvd_drv2_046_yield_proxy_zscore_3y_qoq_diff},
    "dvd_drv2_047_yield_proxy_zscore_1y_yoy_diff":   {"inputs": ["dps", "close"],     "func": dvd_drv2_047_yield_proxy_zscore_1y_yoy_diff},
    "dvd_drv2_048_yield_proxy_zscore_3y_yoy_diff":   {"inputs": ["dps", "close"],     "func": dvd_drv2_048_yield_proxy_zscore_3y_yoy_diff},
    "dvd_drv2_049_dps_ttm_pct_qoq_diff":             {"inputs": ["dps"],              "func": dvd_drv2_049_dps_ttm_pct_qoq_diff},
    "dvd_drv2_050_dps_ttm_zscore_1y_qoq_diff":       {"inputs": ["dps"],              "func": dvd_drv2_050_dps_ttm_zscore_1y_qoq_diff},
    "dvd_drv2_051_dps_drawdown_3y_yoy_diff":         {"inputs": ["dps"],              "func": dvd_drv2_051_dps_drawdown_3y_yoy_diff},
    "dvd_drv2_052_dps_2q_change_yoy_diff":           {"inputs": ["dps"],              "func": dvd_drv2_052_dps_2q_change_yoy_diff},
    "dvd_drv2_053_dps_qoq_slope_1q":                 {"inputs": ["dps"],              "func": dvd_drv2_053_dps_qoq_slope_1q},
    "dvd_drv2_054_dividends_ttm_qoq_diff":           {"inputs": ["dividends"],        "func": dvd_drv2_054_dividends_ttm_qoq_diff},
    "dvd_drv2_055_dividends_ttm_yoy_diff":           {"inputs": ["dividends"],        "func": dvd_drv2_055_dividends_ttm_yoy_diff},
    "dvd_drv2_056_yield_proxy_qoq_ewm_diff":         {"inputs": ["dps", "close"],     "func": dvd_drv2_056_yield_proxy_qoq_ewm_diff},
    "dvd_drv2_057_dps_zscore_1y_ewm_diff":           {"inputs": ["dps"],              "func": dvd_drv2_057_dps_zscore_1y_ewm_diff},
    "dvd_drv2_058_dps_cut_fraction_1y_ewm_diff":     {"inputs": ["dps"],              "func": dvd_drv2_058_dps_cut_fraction_1y_ewm_diff},
    "dvd_drv2_059_dps_omission_frac_1y_ewm_diff":    {"inputs": ["dps"],              "func": dvd_drv2_059_dps_omission_frac_1y_ewm_diff},
    "dvd_drv2_060_dividends_qoq_pct_yoy_diff":       {"inputs": ["dividends"],        "func": dvd_drv2_060_dividends_qoq_pct_yoy_diff},
    "dvd_drv2_061_dps_drawdown_1y_2q_diff":          {"inputs": ["dps"],              "func": dvd_drv2_061_dps_drawdown_1y_2q_diff},
    "dvd_drv2_062_dps_zscore_1y_2q_diff":            {"inputs": ["dps"],              "func": dvd_drv2_062_dps_zscore_1y_2q_diff},
    "dvd_drv2_063_yield_proxy_2q_diff":              {"inputs": ["dps", "close"],     "func": dvd_drv2_063_yield_proxy_2q_diff},
    "dvd_drv2_064_dividends_qoq_2q_diff":            {"inputs": ["dividends"],        "func": dvd_drv2_064_dividends_qoq_2q_diff},
    "dvd_drv2_065_dps_qoq_pct_yoy_diff":             {"inputs": ["dps"],              "func": dvd_drv2_065_dps_qoq_pct_yoy_diff},
    "dvd_drv2_066_dps_ttm_drawdown_yoy_diff":        {"inputs": ["dps"],              "func": dvd_drv2_066_dps_ttm_drawdown_yoy_diff},
    "dvd_drv2_067_dividends_yoy_ewm_diff":           {"inputs": ["dividends"],        "func": dvd_drv2_067_dividends_yoy_ewm_diff},
    "dvd_drv2_068_dps_vs_3y_avg_yoy_diff":           {"inputs": ["dps"],              "func": dvd_drv2_068_dps_vs_3y_avg_yoy_diff},
    "dvd_drv2_069_dps_zscore_3y_ewm_diff":           {"inputs": ["dps"],              "func": dvd_drv2_069_dps_zscore_3y_ewm_diff},
    "dvd_drv2_070_dividends_ttm_drawdown_accel":     {"inputs": ["dividends"],        "func": dvd_drv2_070_dividends_ttm_drawdown_accel},
    "dvd_drv2_071_dps_pct_drawdown_3y_yoy_diff":     {"inputs": ["dps"],              "func": dvd_drv2_071_dps_pct_drawdown_3y_yoy_diff},
    "dvd_drv2_072_dps_ewm_short_yoy_diff":           {"inputs": ["dps"],              "func": dvd_drv2_072_dps_ewm_short_yoy_diff},
    "dvd_drv2_073_dps_cut_fraction_3y_ewm_diff":     {"inputs": ["dps"],              "func": dvd_drv2_073_dps_cut_fraction_3y_ewm_diff},
    "dvd_drv2_074_dividends_drawdown_3y_yoy_diff":   {"inputs": ["dividends"],        "func": dvd_drv2_074_dividends_drawdown_3y_yoy_diff},
    "dvd_drv2_075_dps_qoq_pct_ewm_diff":             {"inputs": ["dps"],              "func": dvd_drv2_075_dps_qoq_pct_ewm_diff},
}
