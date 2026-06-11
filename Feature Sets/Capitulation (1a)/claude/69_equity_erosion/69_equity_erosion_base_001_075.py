"""
69_equity_erosion — Base Features 001-075
Domain: shareholders'-equity erosion (equity-VALUE side) — total equity declining,
retained earnings falling and going negative, book value per share decline,
equity drawdown from trailing peak, OCI deterioration, tangible book value decline,
equity-to-assets shrinking, negative-equity onset and depth.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Quarterly cadence on the daily index: 1 quarter = 63 trading
days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63    # 1 quarter in trading days
_TD_2Q    = 126
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions in this file already receive Series prepared this way;
    this helper is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN.
    Negative denominators are intentionally preserved — negative equity is a meaningful
    distress signal and should not be suppressed."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features
    while still producing a defined result when the denominator is negative."""
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Total-equity low flags, ranks, and multi-period changes ---

def eqe_001_equity_at_1y_low(equity: pd.Series) -> pd.Series:
    """Binary: 1 if total equity equals its rolling 1-year minimum (new 1-year book low)."""
    low1 = _rolling_min(equity, _TD_YEAR)
    return (equity <= low1).astype(float)


def eqe_002_equity_pct_rank_3y(equity: pd.Series) -> pd.Series:
    """Rolling 3-year (756-day) percentile rank of total equity (low rank = severe erosion)."""
    return _rolling_rank_pct(equity, _TD_3Y)


def eqe_003_equity_qoq_pct(equity: pd.Series) -> pd.Series:
    """Total equity QoQ percent change; denominator is abs(prior equity)."""
    prior = equity.shift(_TD_QTR)
    return _safe_div_abs(equity - prior, prior)


def eqe_004_equity_yoy_pct(equity: pd.Series) -> pd.Series:
    """Total equity YoY percent change; denominator is abs(prior equity)."""
    prior = equity.shift(_TD_YEAR)
    return _safe_div_abs(equity - prior, prior)


def eqe_005_equity_2y_change(equity: pd.Series) -> pd.Series:
    """Total equity change over 2 years (504-day lag)."""
    return equity - equity.shift(_TD_2Y)


def eqe_006_equity_3y_change(equity: pd.Series) -> pd.Series:
    """Total equity change over 3 years (756-day lag)."""
    return equity - equity.shift(_TD_3Y)


def eqe_007_equity_2y_pct(equity: pd.Series) -> pd.Series:
    """Total equity 2-year percent change; denominator is abs(prior)."""
    prior = equity.shift(_TD_2Y)
    return _safe_div_abs(equity - prior, prior)


def eqe_008_equity_3y_pct(equity: pd.Series) -> pd.Series:
    """Total equity 3-year percent change; denominator is abs(prior)."""
    prior = equity.shift(_TD_3Y)
    return _safe_div_abs(equity - prior, prior)


def eqe_009_retearn_to_assets_ratio(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Retained earnings as a fraction of total assets (Altman Z-score component; negative = deficit)."""
    return _safe_div(retearn, assets)


def eqe_010_retearn_yoy_change(retearn: pd.Series) -> pd.Series:
    """Retained earnings YoY absolute change."""
    return retearn - retearn.shift(_TD_YEAR)


def eqe_011_retearn_2y_change(retearn: pd.Series) -> pd.Series:
    """Retained earnings 2-year absolute change."""
    return retearn - retearn.shift(_TD_2Y)


def eqe_012_retearn_3y_change(retearn: pd.Series) -> pd.Series:
    """Retained earnings 3-year absolute change."""
    return retearn - retearn.shift(_TD_3Y)


def eqe_013_retearn_qoq_pct(retearn: pd.Series) -> pd.Series:
    """Retained earnings QoQ percent change; denominator is abs(prior)."""
    prior = retearn.shift(_TD_QTR)
    return _safe_div_abs(retearn - prior, prior)


def eqe_014_retearn_yoy_pct(retearn: pd.Series) -> pd.Series:
    """Retained earnings YoY percent change; denominator is abs(prior)."""
    prior = retearn.shift(_TD_YEAR)
    return _safe_div_abs(retearn - prior, prior)


def eqe_015_equity_5y_pct(equity: pd.Series) -> pd.Series:
    """Total equity 5-year percent change; denominator is abs(prior)."""
    prior = equity.shift(_TD_5Y)
    return _safe_div_abs(equity - prior, prior)


# --- Group B (016-030): Negative-equity onset and depth ---

def eqe_016_equity_is_negative(equity: pd.Series) -> pd.Series:
    """Binary: 1 if total equity < 0 (technically insolvent book), else 0."""
    return (equity < 0).astype(float)


def eqe_017_retearn_is_negative(retearn: pd.Series) -> pd.Series:
    """Binary: 1 if retained earnings < 0 (accumulated deficit), else 0."""
    return (retearn < 0).astype(float)


def eqe_018_equity_turned_negative(equity: pd.Series) -> pd.Series:
    """1 on first quarter where equity flips from non-negative to negative."""
    curr_neg  = (equity < 0).astype(float)
    prior_pos = (equity.shift(_TD_QTR) >= 0).astype(float)
    return curr_neg * prior_pos


def eqe_019_retearn_turned_negative(retearn: pd.Series) -> pd.Series:
    """1 on first quarter where retained earnings flip from non-negative to negative."""
    curr_neg  = (retearn < 0).astype(float)
    prior_pos = (retearn.shift(_TD_QTR) >= 0).astype(float)
    return curr_neg * prior_pos


def eqe_020_equity_negative_depth(equity: pd.Series) -> pd.Series:
    """Depth of negative equity: min(equity, 0). Zero when equity is positive."""
    return equity.clip(upper=0)


def eqe_021_retearn_negative_depth(retearn: pd.Series) -> pd.Series:
    """Depth of accumulated deficit: min(retearn, 0). Zero when positive."""
    return retearn.clip(upper=0)


def eqe_022_equity_negative_quarters_1y(equity: pd.Series) -> pd.Series:
    """Count of daily observations with equity < 0 over trailing 252 days."""
    neg = (equity < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR)


def eqe_023_equity_negative_quarters_2y(equity: pd.Series) -> pd.Series:
    """Count of daily observations with equity < 0 over trailing 504 days."""
    neg = (equity < 0).astype(float)
    return _rolling_sum(neg, _TD_2Y)


def eqe_024_retearn_negative_quarters_1y(retearn: pd.Series) -> pd.Series:
    """Count of daily observations with retearn < 0 over trailing 252 days."""
    neg = (retearn < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR)


def eqe_025_retearn_negative_quarters_2y(retearn: pd.Series) -> pd.Series:
    """Count of daily observations with retearn < 0 over trailing 504 days."""
    neg = (retearn < 0).astype(float)
    return _rolling_sum(neg, _TD_2Y)


# --- Group C (026-040): Equity drawdown from trailing peak ---

def eqe_026_equity_drawdown_from_1y_peak(equity: pd.Series) -> pd.Series:
    """Total equity minus its rolling 1-year maximum (drawdown, negative or zero)."""
    return equity - _rolling_max(equity, _TD_YEAR)


def eqe_027_equity_drawdown_from_2y_peak(equity: pd.Series) -> pd.Series:
    """Total equity minus its rolling 2-year maximum."""
    return equity - _rolling_max(equity, _TD_2Y)


def eqe_028_equity_drawdown_from_3y_peak(equity: pd.Series) -> pd.Series:
    """Total equity minus its rolling 3-year maximum."""
    return equity - _rolling_max(equity, _TD_3Y)


def eqe_029_equity_drawdown_pct_1y_peak(equity: pd.Series) -> pd.Series:
    """Equity drawdown from 1-year peak as percent of abs(peak)."""
    peak = _rolling_max(equity, _TD_YEAR)
    return _safe_div_abs(equity - peak, peak)


def eqe_030_equity_drawdown_pct_2y_peak(equity: pd.Series) -> pd.Series:
    """Equity drawdown from 2-year peak as percent of abs(peak)."""
    peak = _rolling_max(equity, _TD_2Y)
    return _safe_div_abs(equity - peak, peak)


def eqe_031_equity_drawdown_from_expanding_peak(equity: pd.Series) -> pd.Series:
    """Total equity minus its all-time (expanding) maximum — maximum erosion depth."""
    peak = equity.expanding(min_periods=1).max()
    return equity - peak


def eqe_032_equity_drawdown_pct_expanding_peak(equity: pd.Series) -> pd.Series:
    """Equity drawdown from expanding peak as percent of abs(peak)."""
    peak = equity.expanding(min_periods=1).max()
    return _safe_div_abs(equity - peak, peak)


def eqe_033_retearn_drawdown_from_1y_peak(retearn: pd.Series) -> pd.Series:
    """Retained earnings minus its rolling 1-year maximum."""
    return retearn - _rolling_max(retearn, _TD_YEAR)


def eqe_034_retearn_drawdown_from_expanding_peak(retearn: pd.Series) -> pd.Series:
    """Retained earnings minus its all-time (expanding) maximum."""
    peak = retearn.expanding(min_periods=1).max()
    return retearn - peak


def eqe_035_equity_at_5y_low(equity: pd.Series) -> pd.Series:
    """Binary: 1 if equity equals its rolling 5-year minimum (new 5-year book low)."""
    low5 = _rolling_min(equity, _TD_5Y)
    return (equity <= low5).astype(float)


# --- Group D (036-050): Book value per share decline ---

def eqe_036_bvps(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Book value per share: equity / sharesbas."""
    return _safe_div(equity, sharesbas)


def eqe_037_bvps_qoq_change(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """QoQ absolute change in book value per share."""
    bvps = _safe_div(equity, sharesbas)
    return bvps - bvps.shift(_TD_QTR)


def eqe_038_bvps_yoy_change(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """YoY absolute change in book value per share."""
    bvps = _safe_div(equity, sharesbas)
    return bvps - bvps.shift(_TD_YEAR)


def eqe_039_bvps_yoy_pct(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """YoY percent change in book value per share."""
    bvps = _safe_div(equity, sharesbas)
    prior = bvps.shift(_TD_YEAR)
    return _safe_div_abs(bvps - prior, prior)


def eqe_040_bvps_drawdown_from_2y_peak(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """BVPS minus its rolling 2-year maximum."""
    bvps = _safe_div(equity, sharesbas)
    return bvps - _rolling_max(bvps, _TD_2Y)


def eqe_041_bvps_drawdown_from_expanding_peak(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """BVPS minus its all-time (expanding) maximum."""
    bvps = _safe_div(equity, sharesbas)
    peak = bvps.expanding(min_periods=1).max()
    return bvps - peak


def eqe_042_bvps_is_negative(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Binary: 1 if BVPS < 0."""
    bvps = _safe_div(equity, sharesbas)
    return (bvps < 0).astype(float)


def eqe_043_bvps_2y_pct(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """2-year percent change in book value per share."""
    bvps = _safe_div(equity, sharesbas)
    prior = bvps.shift(_TD_2Y)
    return _safe_div_abs(bvps - prior, prior)


def eqe_044_bvps_3y_pct(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """3-year percent change in book value per share."""
    bvps = _safe_div(equity, sharesbas)
    prior = bvps.shift(_TD_3Y)
    return _safe_div_abs(bvps - prior, prior)


def eqe_045_bvps_rolling_min_4q(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Rolling 4-quarter minimum of BVPS (worst book value in the past year)."""
    bvps = _safe_div(equity, sharesbas)
    return _rolling_min(bvps, _TD_YEAR)


# --- Group E (046-060): Tangible book value and equity-to-assets ---

def eqe_046_tangible_equity(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Tangible book value = equity - intangibles."""
    return equity - intangibles


def eqe_047_tangible_equity_qoq_change(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """QoQ change in tangible book value."""
    tbe = equity - intangibles
    return tbe - tbe.shift(_TD_QTR)


def eqe_048_tangible_equity_yoy_change(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """YoY change in tangible book value."""
    tbe = equity - intangibles
    return tbe - tbe.shift(_TD_YEAR)


def eqe_049_tangible_equity_yoy_pct(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """YoY percent change in tangible book value."""
    tbe = equity - intangibles
    prior = tbe.shift(_TD_YEAR)
    return _safe_div_abs(tbe - prior, prior)


def eqe_050_tangible_equity_is_negative(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Binary: 1 if tangible equity < 0."""
    return ((equity - intangibles) < 0).astype(float)


def eqe_051_equity_to_assets(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Equity-to-assets ratio (book leverage inverse)."""
    return _safe_div(equity, assets)


def eqe_052_equity_to_assets_qoq_change(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in equity-to-assets ratio."""
    ratio = _safe_div(equity, assets)
    return ratio - ratio.shift(_TD_QTR)


def eqe_053_equity_to_assets_yoy_change(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in equity-to-assets ratio."""
    ratio = _safe_div(equity, assets)
    return ratio - ratio.shift(_TD_YEAR)


def eqe_054_equity_to_assets_2y_change(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """2-year change in equity-to-assets ratio."""
    ratio = _safe_div(equity, assets)
    return ratio - ratio.shift(_TD_2Y)


def eqe_055_equity_to_assets_at_1y_low(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Binary: 1 if equity/assets equals its rolling 1-year minimum."""
    ratio = _safe_div(equity, assets)
    low1y = _rolling_min(ratio, _TD_YEAR)
    return (ratio <= low1y).astype(float)


# --- Group F (056-065): Accumulated OCI deterioration ---

def eqe_056_accoci_qoq_change(accoci: pd.Series) -> pd.Series:
    """Accumulated OCI QoQ absolute change (negative = additional losses)."""
    return accoci - accoci.shift(_TD_QTR)


def eqe_057_accoci_yoy_change(accoci: pd.Series) -> pd.Series:
    """Accumulated OCI YoY absolute change."""
    return accoci - accoci.shift(_TD_YEAR)


def eqe_058_accoci_is_negative(accoci: pd.Series) -> pd.Series:
    """Binary: 1 if accumulated OCI < 0 (unrealized losses dominate)."""
    return (accoci < 0).astype(float)


def eqe_059_accoci_drawdown_from_expanding_peak(accoci: pd.Series) -> pd.Series:
    """Accumulated OCI minus its all-time (expanding) maximum."""
    peak = accoci.expanding(min_periods=1).max()
    return accoci - peak


def eqe_060_accoci_rolling_min_1y(accoci: pd.Series) -> pd.Series:
    """Rolling 1-year minimum of accumulated OCI (worst OCI balance in the past year)."""
    return _rolling_min(accoci, _TD_YEAR)


# --- Group G (061-068): Consecutive equity-decline streak and rolling count ---

def eqe_061_equity_qoq_decline_flag(equity: pd.Series) -> pd.Series:
    """Binary: 1 if equity declined QoQ (equity < equity 63 days ago)."""
    return (equity < equity.shift(_TD_QTR)).astype(float)


def eqe_062_equity_consecutive_decline_streak(equity: pd.Series) -> pd.Series:
    """
    Current consecutive-quarter decline streak length (in daily observations).
    Resets to 0 whenever equity does NOT decline QoQ.
    """
    decline = (equity < equity.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(decline), dtype=float)
    arr = decline.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=equity.index)


def eqe_063_equity_decline_quarters_1y(equity: pd.Series) -> pd.Series:
    """Count of daily observations where equity declined QoQ over trailing 252 days."""
    decline = (equity < equity.shift(_TD_QTR)).astype(float)
    return _rolling_sum(decline, _TD_YEAR)


def eqe_064_equity_decline_quarters_2y(equity: pd.Series) -> pd.Series:
    """Count of equity-QoQ-decline observations over trailing 504 days."""
    decline = (equity < equity.shift(_TD_QTR)).astype(float)
    return _rolling_sum(decline, _TD_2Y)


def eqe_065_retearn_decline_quarters_1y(retearn: pd.Series) -> pd.Series:
    """Count of QoQ retained-earnings declines over trailing 252 days."""
    decline = (retearn < retearn.shift(_TD_QTR)).astype(float)
    return _rolling_sum(decline, _TD_YEAR)


def eqe_066_retearn_consecutive_decline_streak(retearn: pd.Series) -> pd.Series:
    """
    Current consecutive-quarter decline streak in retained earnings.
    Resets to 0 whenever retearn does NOT decline QoQ.
    """
    decline = (retearn < retearn.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(decline), dtype=float)
    arr = decline.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=retearn.index)


def eqe_067_equity_rolling_min_1y(equity: pd.Series) -> pd.Series:
    """Rolling 1-year minimum of total equity."""
    return _rolling_min(equity, _TD_YEAR)


def eqe_068_equity_rolling_min_3y(equity: pd.Series) -> pd.Series:
    """Rolling 3-year minimum of total equity."""
    return _rolling_min(equity, _TD_3Y)


# --- Group H (069-075): Z-scores, ranks, and composite severity ---

def eqe_069_equity_zscore_4q(equity: pd.Series) -> pd.Series:
    """Rolling 4-quarter (252-day) z-score of total equity."""
    return _zscore_rolling(equity, _TD_YEAR)


def eqe_070_equity_zscore_8q(equity: pd.Series) -> pd.Series:
    """Rolling 8-quarter (504-day) z-score of total equity."""
    return _zscore_rolling(equity, _TD_2Y)


def eqe_071_retearn_zscore_4q(retearn: pd.Series) -> pd.Series:
    """Rolling 4-quarter z-score of retained earnings."""
    return _zscore_rolling(retearn, _TD_YEAR)


def eqe_072_equity_pct_rank_4q(equity: pd.Series) -> pd.Series:
    """Rolling 4-quarter percentile rank of total equity (low rank = severe erosion)."""
    return _rolling_rank_pct(equity, _TD_YEAR)


def eqe_073_equity_pct_rank_8q(equity: pd.Series) -> pd.Series:
    """Rolling 8-quarter percentile rank of total equity."""
    return _rolling_rank_pct(equity, _TD_2Y)


def eqe_074_retearn_pct_rank_4q(retearn: pd.Series) -> pd.Series:
    """Rolling 4-quarter percentile rank of retained earnings."""
    return _rolling_rank_pct(retearn, _TD_YEAR)


def eqe_075_equity_erosion_composite(equity: pd.Series, retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """
    Composite equity-erosion severity score:
    average of (1) equity z-score, (2) retearn z-score, (3) equity/assets z-score.
    More negative = deeper distress.
    """
    z_eq = _zscore_rolling(equity, _TD_YEAR)
    z_re = _zscore_rolling(retearn, _TD_YEAR)
    ea   = _safe_div(equity, assets)
    z_ea = _zscore_rolling(ea, _TD_YEAR)
    return (z_eq + z_re + z_ea) / 3.0


# ── Registry 001-075 ──────────────────────────────────────────────────────────

EQUITY_EROSION_REGISTRY_001_075 = {
    "eqe_001_equity_at_1y_low":                     {"inputs": ["equity"],                              "func": eqe_001_equity_at_1y_low},
    "eqe_002_equity_pct_rank_3y":                  {"inputs": ["equity"],                              "func": eqe_002_equity_pct_rank_3y},
    "eqe_003_equity_qoq_pct":                      {"inputs": ["equity"],                              "func": eqe_003_equity_qoq_pct},
    "eqe_004_equity_yoy_pct":                      {"inputs": ["equity"],                              "func": eqe_004_equity_yoy_pct},
    "eqe_005_equity_2y_change":                    {"inputs": ["equity"],                              "func": eqe_005_equity_2y_change},
    "eqe_006_equity_3y_change":                    {"inputs": ["equity"],                              "func": eqe_006_equity_3y_change},
    "eqe_007_equity_2y_pct":                       {"inputs": ["equity"],                              "func": eqe_007_equity_2y_pct},
    "eqe_008_equity_3y_pct":                       {"inputs": ["equity"],                              "func": eqe_008_equity_3y_pct},
    "eqe_009_retearn_to_assets_ratio":              {"inputs": ["retearn", "assets"],                   "func": eqe_009_retearn_to_assets_ratio},
    "eqe_010_retearn_yoy_change":                  {"inputs": ["retearn"],                             "func": eqe_010_retearn_yoy_change},
    "eqe_011_retearn_2y_change":                   {"inputs": ["retearn"],                             "func": eqe_011_retearn_2y_change},
    "eqe_012_retearn_3y_change":                   {"inputs": ["retearn"],                             "func": eqe_012_retearn_3y_change},
    "eqe_013_retearn_qoq_pct":                     {"inputs": ["retearn"],                             "func": eqe_013_retearn_qoq_pct},
    "eqe_014_retearn_yoy_pct":                     {"inputs": ["retearn"],                             "func": eqe_014_retearn_yoy_pct},
    "eqe_015_equity_5y_pct":                       {"inputs": ["equity"],                              "func": eqe_015_equity_5y_pct},
    "eqe_016_equity_is_negative":                  {"inputs": ["equity"],                              "func": eqe_016_equity_is_negative},
    "eqe_017_retearn_is_negative":                 {"inputs": ["retearn"],                             "func": eqe_017_retearn_is_negative},
    "eqe_018_equity_turned_negative":              {"inputs": ["equity"],                              "func": eqe_018_equity_turned_negative},
    "eqe_019_retearn_turned_negative":             {"inputs": ["retearn"],                             "func": eqe_019_retearn_turned_negative},
    "eqe_020_equity_negative_depth":               {"inputs": ["equity"],                              "func": eqe_020_equity_negative_depth},
    "eqe_021_retearn_negative_depth":              {"inputs": ["retearn"],                             "func": eqe_021_retearn_negative_depth},
    "eqe_022_equity_negative_quarters_1y":         {"inputs": ["equity"],                              "func": eqe_022_equity_negative_quarters_1y},
    "eqe_023_equity_negative_quarters_2y":         {"inputs": ["equity"],                              "func": eqe_023_equity_negative_quarters_2y},
    "eqe_024_retearn_negative_quarters_1y":        {"inputs": ["retearn"],                             "func": eqe_024_retearn_negative_quarters_1y},
    "eqe_025_retearn_negative_quarters_2y":        {"inputs": ["retearn"],                             "func": eqe_025_retearn_negative_quarters_2y},
    "eqe_026_equity_drawdown_from_1y_peak":        {"inputs": ["equity"],                              "func": eqe_026_equity_drawdown_from_1y_peak},
    "eqe_027_equity_drawdown_from_2y_peak":        {"inputs": ["equity"],                              "func": eqe_027_equity_drawdown_from_2y_peak},
    "eqe_028_equity_drawdown_from_3y_peak":        {"inputs": ["equity"],                              "func": eqe_028_equity_drawdown_from_3y_peak},
    "eqe_029_equity_drawdown_pct_1y_peak":         {"inputs": ["equity"],                              "func": eqe_029_equity_drawdown_pct_1y_peak},
    "eqe_030_equity_drawdown_pct_2y_peak":         {"inputs": ["equity"],                              "func": eqe_030_equity_drawdown_pct_2y_peak},
    "eqe_031_equity_drawdown_from_expanding_peak": {"inputs": ["equity"],                              "func": eqe_031_equity_drawdown_from_expanding_peak},
    "eqe_032_equity_drawdown_pct_expanding_peak":  {"inputs": ["equity"],                              "func": eqe_032_equity_drawdown_pct_expanding_peak},
    "eqe_033_retearn_drawdown_from_1y_peak":       {"inputs": ["retearn"],                             "func": eqe_033_retearn_drawdown_from_1y_peak},
    "eqe_034_retearn_drawdown_from_expanding_peak":{"inputs": ["retearn"],                             "func": eqe_034_retearn_drawdown_from_expanding_peak},
    "eqe_035_equity_at_5y_low":                    {"inputs": ["equity"],                              "func": eqe_035_equity_at_5y_low},
    "eqe_036_bvps":                                {"inputs": ["equity", "sharesbas"],                 "func": eqe_036_bvps},
    "eqe_037_bvps_qoq_change":                     {"inputs": ["equity", "sharesbas"],                 "func": eqe_037_bvps_qoq_change},
    "eqe_038_bvps_yoy_change":                     {"inputs": ["equity", "sharesbas"],                 "func": eqe_038_bvps_yoy_change},
    "eqe_039_bvps_yoy_pct":                        {"inputs": ["equity", "sharesbas"],                 "func": eqe_039_bvps_yoy_pct},
    "eqe_040_bvps_drawdown_from_2y_peak":          {"inputs": ["equity", "sharesbas"],                 "func": eqe_040_bvps_drawdown_from_2y_peak},
    "eqe_041_bvps_drawdown_from_expanding_peak":   {"inputs": ["equity", "sharesbas"],                 "func": eqe_041_bvps_drawdown_from_expanding_peak},
    "eqe_042_bvps_is_negative":                    {"inputs": ["equity", "sharesbas"],                 "func": eqe_042_bvps_is_negative},
    "eqe_043_bvps_2y_pct":                         {"inputs": ["equity", "sharesbas"],                 "func": eqe_043_bvps_2y_pct},
    "eqe_044_bvps_3y_pct":                         {"inputs": ["equity", "sharesbas"],                 "func": eqe_044_bvps_3y_pct},
    "eqe_045_bvps_rolling_min_4q":                 {"inputs": ["equity", "sharesbas"],                 "func": eqe_045_bvps_rolling_min_4q},
    "eqe_046_tangible_equity":                     {"inputs": ["equity", "intangibles"],               "func": eqe_046_tangible_equity},
    "eqe_047_tangible_equity_qoq_change":          {"inputs": ["equity", "intangibles"],               "func": eqe_047_tangible_equity_qoq_change},
    "eqe_048_tangible_equity_yoy_change":          {"inputs": ["equity", "intangibles"],               "func": eqe_048_tangible_equity_yoy_change},
    "eqe_049_tangible_equity_yoy_pct":             {"inputs": ["equity", "intangibles"],               "func": eqe_049_tangible_equity_yoy_pct},
    "eqe_050_tangible_equity_is_negative":         {"inputs": ["equity", "intangibles"],               "func": eqe_050_tangible_equity_is_negative},
    "eqe_051_equity_to_assets":                    {"inputs": ["equity", "assets"],                    "func": eqe_051_equity_to_assets},
    "eqe_052_equity_to_assets_qoq_change":         {"inputs": ["equity", "assets"],                    "func": eqe_052_equity_to_assets_qoq_change},
    "eqe_053_equity_to_assets_yoy_change":         {"inputs": ["equity", "assets"],                    "func": eqe_053_equity_to_assets_yoy_change},
    "eqe_054_equity_to_assets_2y_change":          {"inputs": ["equity", "assets"],                    "func": eqe_054_equity_to_assets_2y_change},
    "eqe_055_equity_to_assets_at_1y_low":          {"inputs": ["equity", "assets"],                    "func": eqe_055_equity_to_assets_at_1y_low},
    "eqe_056_accoci_qoq_change":                   {"inputs": ["accoci"],                              "func": eqe_056_accoci_qoq_change},
    "eqe_057_accoci_yoy_change":                   {"inputs": ["accoci"],                              "func": eqe_057_accoci_yoy_change},
    "eqe_058_accoci_is_negative":                  {"inputs": ["accoci"],                              "func": eqe_058_accoci_is_negative},
    "eqe_059_accoci_drawdown_from_expanding_peak": {"inputs": ["accoci"],                              "func": eqe_059_accoci_drawdown_from_expanding_peak},
    "eqe_060_accoci_rolling_min_1y":               {"inputs": ["accoci"],                              "func": eqe_060_accoci_rolling_min_1y},
    "eqe_061_equity_qoq_decline_flag":             {"inputs": ["equity"],                              "func": eqe_061_equity_qoq_decline_flag},
    "eqe_062_equity_consecutive_decline_streak":   {"inputs": ["equity"],                              "func": eqe_062_equity_consecutive_decline_streak},
    "eqe_063_equity_decline_quarters_1y":          {"inputs": ["equity"],                              "func": eqe_063_equity_decline_quarters_1y},
    "eqe_064_equity_decline_quarters_2y":          {"inputs": ["equity"],                              "func": eqe_064_equity_decline_quarters_2y},
    "eqe_065_retearn_decline_quarters_1y":         {"inputs": ["retearn"],                             "func": eqe_065_retearn_decline_quarters_1y},
    "eqe_066_retearn_consecutive_decline_streak":  {"inputs": ["retearn"],                             "func": eqe_066_retearn_consecutive_decline_streak},
    "eqe_067_equity_rolling_min_1y":               {"inputs": ["equity"],                              "func": eqe_067_equity_rolling_min_1y},
    "eqe_068_equity_rolling_min_3y":               {"inputs": ["equity"],                              "func": eqe_068_equity_rolling_min_3y},
    "eqe_069_equity_zscore_4q":                    {"inputs": ["equity"],                              "func": eqe_069_equity_zscore_4q},
    "eqe_070_equity_zscore_8q":                    {"inputs": ["equity"],                              "func": eqe_070_equity_zscore_8q},
    "eqe_071_retearn_zscore_4q":                   {"inputs": ["retearn"],                             "func": eqe_071_retearn_zscore_4q},
    "eqe_072_equity_pct_rank_4q":                  {"inputs": ["equity"],                              "func": eqe_072_equity_pct_rank_4q},
    "eqe_073_equity_pct_rank_8q":                  {"inputs": ["equity"],                              "func": eqe_073_equity_pct_rank_8q},
    "eqe_074_retearn_pct_rank_4q":                 {"inputs": ["retearn"],                             "func": eqe_074_retearn_pct_rank_4q},
    "eqe_075_equity_erosion_composite":            {"inputs": ["equity", "retearn", "assets"],         "func": eqe_075_equity_erosion_composite},
}
