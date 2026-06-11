"""
70_dilution_acceleration — Base Features 001-075
Domain: share-count dilution, secondary issuance, share-count growth acceleration
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
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
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

# --- Group A (001-015): QoQ and YoY share-count growth levels ---

def dla_001_sharesbas_qoq_change(sharesbas: pd.Series) -> pd.Series:
    """Basic shares outstanding QoQ absolute change (63-day lag)."""
    return sharesbas - sharesbas.shift(_TD_QTR)


def dla_002_sharesbas_yoy_change(sharesbas: pd.Series) -> pd.Series:
    """Basic shares outstanding YoY absolute change (252-day lag)."""
    return sharesbas - sharesbas.shift(_TD_YEAR)


def dla_003_sharesbas_qoq_pct(sharesbas: pd.Series) -> pd.Series:
    """Basic shares QoQ percent change; denominator is prior-period shares."""
    prior = sharesbas.shift(_TD_QTR)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def dla_004_sharesbas_yoy_pct(sharesbas: pd.Series) -> pd.Series:
    """Basic shares YoY percent change."""
    prior = sharesbas.shift(_TD_YEAR)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def dla_005_shareswa_qoq_change(shareswa: pd.Series) -> pd.Series:
    """Weighted-average basic shares QoQ absolute change."""
    return shareswa - shareswa.shift(_TD_QTR)


def dla_006_shareswa_yoy_change(shareswa: pd.Series) -> pd.Series:
    """Weighted-average basic shares YoY absolute change."""
    return shareswa - shareswa.shift(_TD_YEAR)


def dla_007_shareswa_qoq_pct(shareswa: pd.Series) -> pd.Series:
    """Weighted-average basic shares QoQ percent change."""
    prior = shareswa.shift(_TD_QTR)
    return _safe_div(shareswa - prior, prior.replace(0, np.nan))


def dla_008_shareswa_yoy_pct(shareswa: pd.Series) -> pd.Series:
    """Weighted-average basic shares YoY percent change."""
    prior = shareswa.shift(_TD_YEAR)
    return _safe_div(shareswa - prior, prior.replace(0, np.nan))


def dla_009_shareswadil_qoq_change(shareswadil: pd.Series) -> pd.Series:
    """Diluted weighted-average shares QoQ absolute change."""
    return shareswadil - shareswadil.shift(_TD_QTR)


def dla_010_shareswadil_yoy_change(shareswadil: pd.Series) -> pd.Series:
    """Diluted weighted-average shares YoY absolute change."""
    return shareswadil - shareswadil.shift(_TD_YEAR)


def dla_011_shareswadil_qoq_pct(shareswadil: pd.Series) -> pd.Series:
    """Diluted weighted-average shares QoQ percent change."""
    prior = shareswadil.shift(_TD_QTR)
    return _safe_div(shareswadil - prior, prior.replace(0, np.nan))


def dla_012_shareswadil_yoy_pct(shareswadil: pd.Series) -> pd.Series:
    """Diluted weighted-average shares YoY percent change."""
    prior = shareswadil.shift(_TD_YEAR)
    return _safe_div(shareswadil - prior, prior.replace(0, np.nan))


def dla_013_sharesbas_2y_change(sharesbas: pd.Series) -> pd.Series:
    """Basic shares outstanding absolute change over 2 years (504-day lag)."""
    return sharesbas - sharesbas.shift(_TD_2Y)


def dla_014_sharesbas_3y_change(sharesbas: pd.Series) -> pd.Series:
    """Basic shares outstanding absolute change over 3 years (756-day lag)."""
    return sharesbas - sharesbas.shift(_TD_3Y)


def dla_015_sharesbas_at_5y_high_flag(sharesbas: pd.Series) -> pd.Series:
    """Binary: 1 if basic shares are at or above their rolling 5-year maximum (all-time dilution peak)."""
    mx = _rolling_max(sharesbas, _TD_5Y)
    return (sharesbas >= mx).astype(float)


# --- Group B (016-030): Diluted-vs-basic gap and widening ---

def dla_016_diluted_basic_gap(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Diluted minus basic weighted-average shares (absolute gap = option/warrant overhang)."""
    return shareswadil - shareswa


def dla_017_diluted_basic_gap_pct(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Diluted-vs-basic gap as percent of basic shares."""
    gap = shareswadil - shareswa
    return _safe_div(gap, shareswa.replace(0, np.nan))


def dla_018_diluted_basic_gap_qoq_change(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """QoQ change in the diluted-vs-basic share gap (widening = worsening overhang)."""
    gap = shareswadil - shareswa
    return gap - gap.shift(_TD_QTR)


def dla_019_diluted_basic_gap_pct_rank_4q(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Rolling 4-quarter percentile rank of the diluted-vs-basic share gap (high rank = large option/warrant overhang)."""
    gap = shareswadil - shareswa
    return _rolling_rank_pct(gap, _TD_YEAR)


def dla_020_diluted_basic_gap_drawdown_from_2y_peak(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Diluted-vs-basic gap minus its rolling 2-year maximum (distance from worst overhang seen)."""
    gap = shareswadil - shareswa
    return gap - _rolling_max(gap, _TD_2Y)


def dla_021_diluted_vs_basic_ratio(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Diluted shares divided by basic shares (dilution multiplier)."""
    return _safe_div(shareswadil, shareswa.replace(0, np.nan))


def dla_022_diluted_vs_basic_ratio_zscore_4q(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Rolling 4-quarter z-score of the diluted-to-basic share ratio (high z-score = extreme overhang)."""
    ratio = _safe_div(shareswadil, shareswa.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_YEAR)


def dla_023_shareswadil_pct_rank_4q(shareswadil: pd.Series) -> pd.Series:
    """Rolling 4-quarter percentile rank of diluted weighted-average shares (high rank = extreme dilution level)."""
    return _rolling_rank_pct(shareswadil, _TD_YEAR)


def dla_024_shareswadil_vs_sharesbas_gap(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Diluted WA shares minus basic shares outstanding (full dilution overhang)."""
    return shareswadil - sharesbas


def dla_025_shareswadil_vs_sharesbas_pct(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Diluted WA minus basic as percent of basic (full dilution overhang rate)."""
    gap = shareswadil - sharesbas
    return _safe_div(gap, sharesbas.replace(0, np.nan))


# --- Group C (026-040): Secondary-issuance signatures (step-jump detection) ---

def dla_026_sharesbas_qoq_large_jump_flag(sharesbas: pd.Series) -> pd.Series:
    """
    Binary: 1 if basic shares grew >5% QoQ — secondary issuance signature.
    """
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_QTR), sharesbas.shift(_TD_QTR).replace(0, np.nan))
    return (pct > 0.05).astype(float)


def dla_027_sharesbas_qoq_very_large_jump_flag(sharesbas: pd.Series) -> pd.Series:
    """Binary: 1 if basic shares grew >15% QoQ — large dilutive event."""
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_QTR), sharesbas.shift(_TD_QTR).replace(0, np.nan))
    return (pct > 0.15).astype(float)


def dla_028_sharesbas_yoy_large_jump_flag(sharesbas: pd.Series) -> pd.Series:
    """Binary: 1 if basic shares grew >10% YoY — sustained issuance signature."""
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_YEAR), sharesbas.shift(_TD_YEAR).replace(0, np.nan))
    return (pct > 0.10).astype(float)


def dla_029_ncfcommon_positive_flag(ncfcommon: pd.Series) -> pd.Series:
    """
    Binary: 1 if net cash from common equity issuance (ncfcommon) > 0
    — company actively raising equity from the market.
    """
    return (ncfcommon > 0).astype(float)


def dla_030_ncfcommon_level(ncfcommon: pd.Series) -> pd.Series:
    """Net cash raised from common stock issuance (positive = dilutive equity raise)."""
    return ncfcommon.clip(lower=0)


def dla_031_ncfcommon_yoy_change(ncfcommon: pd.Series) -> pd.Series:
    """YoY change in net common equity issuance cash flow."""
    return ncfcommon - ncfcommon.shift(_TD_YEAR)


def dla_032_ncfcommon_trailing_4q_sum(ncfcommon: pd.Series) -> pd.Series:
    """Trailing 4-quarter (TTM) sum of equity issuance proceeds."""
    return _rolling_sum(ncfcommon, _TD_YEAR)


def dla_033_ncfcommon_trailing_8q_sum(ncfcommon: pd.Series) -> pd.Series:
    """Trailing 8-quarter (2-year) cumulative equity issuance proceeds."""
    return _rolling_sum(ncfcommon, _TD_2Y)


def dla_034_ncfcommon_trailing_12q_sum(ncfcommon: pd.Series) -> pd.Series:
    """Trailing 12-quarter (3-year) cumulative equity issuance proceeds."""
    return _rolling_sum(ncfcommon, _TD_3Y)


def dla_035_issuance_quarters_1y(ncfcommon: pd.Series) -> pd.Series:
    """Count of quarters in last year where positive equity was raised (ncfcommon > 0)."""
    flag = (ncfcommon > 0).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


# --- Group D (036-050): Dilution relative to equity and assets ---

def dla_036_ncfcommon_to_equity_ratio(ncfcommon: pd.Series, equity: pd.Series) -> pd.Series:
    """TTM equity issuance as fraction of book equity (dilution intensity vs equity base)."""
    ttm_issue = _rolling_sum(ncfcommon, _TD_YEAR)
    return _safe_div(ttm_issue, equity.abs().replace(0, np.nan))


def dla_037_ncfcommon_to_assets_ratio(ncfcommon: pd.Series, assets: pd.Series) -> pd.Series:
    """TTM equity issuance as fraction of total assets."""
    ttm_issue = _rolling_sum(ncfcommon, _TD_YEAR)
    return _safe_div(ttm_issue, assets.replace(0, np.nan))


def dla_038_sbcomp_to_equity_ratio(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """Stock-based compensation as fraction of book equity."""
    return _safe_div(sbcomp, equity.abs().replace(0, np.nan))


def dla_039_sbcomp_to_shareswa_ratio(sbcomp: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Stock-based compensation per basic weighted-average share (SBC intensity)."""
    return _safe_div(sbcomp, shareswa.replace(0, np.nan))


def dla_040_sbcomp_yoy_change(sbcomp: pd.Series) -> pd.Series:
    """YoY absolute change in stock-based compensation."""
    return sbcomp - sbcomp.shift(_TD_YEAR)


def dla_041_sbcomp_yoy_pct(sbcomp: pd.Series) -> pd.Series:
    """YoY percent change in stock-based compensation."""
    prior = sbcomp.shift(_TD_YEAR)
    return _safe_div(sbcomp - prior, prior.abs().replace(0, np.nan))


def dla_042_sbcomp_trailing_4q_sum(sbcomp: pd.Series) -> pd.Series:
    """Trailing TTM sum of stock-based compensation."""
    return _rolling_sum(sbcomp, _TD_YEAR)


def dla_043_sbcomp_trailing_8q_sum(sbcomp: pd.Series) -> pd.Series:
    """Trailing 2-year cumulative stock-based compensation."""
    return _rolling_sum(sbcomp, _TD_2Y)


def dla_044_sbcomp_plus_ncfcommon_to_equity(sbcomp: pd.Series, ncfcommon: pd.Series, equity: pd.Series) -> pd.Series:
    """Combined SBC and equity-raise divided by book equity (total dilution pressure)."""
    ttm_sbc = _rolling_sum(sbcomp, _TD_YEAR)
    ttm_iss = _rolling_sum(ncfcommon.clip(lower=0), _TD_YEAR)
    return _safe_div(ttm_sbc + ttm_iss, equity.abs().replace(0, np.nan))


def dla_045_sharesbas_2y_pct_change(sharesbas: pd.Series) -> pd.Series:
    """Basic shares 2-year cumulative percent change."""
    prior = sharesbas.shift(_TD_2Y)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


# --- Group E (046-060): Consecutive share growth and streak signals ---

def dla_046_sharesbas_qoq_positive_flag(sharesbas: pd.Series) -> pd.Series:
    """Binary: 1 if basic shares grew any amount QoQ."""
    return (sharesbas > sharesbas.shift(_TD_QTR)).astype(float)


def dla_047_sharesbas_consecutive_growth_streak(sharesbas: pd.Series) -> pd.Series:
    """
    Length of current consecutive-quarter share-growth streak (in daily obs).
    Resets to 0 when shares do not grow QoQ.
    """
    grew = (sharesbas > sharesbas.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(grew), dtype=float)
    arr = grew.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=sharesbas.index)


def dla_048_sharesbas_growth_quarters_1y(sharesbas: pd.Series) -> pd.Series:
    """Count of quarters with positive share growth in trailing 1 year."""
    grew = (sharesbas > sharesbas.shift(_TD_QTR)).astype(float)
    return _rolling_sum(grew, _TD_YEAR)


def dla_049_sharesbas_growth_quarters_2y(sharesbas: pd.Series) -> pd.Series:
    """Count of quarters with positive share growth in trailing 2 years."""
    grew = (sharesbas > sharesbas.shift(_TD_QTR)).astype(float)
    return _rolling_sum(grew, _TD_2Y)


def dla_050_sharesbas_growth_quarters_3y(sharesbas: pd.Series) -> pd.Series:
    """Count of quarters with positive share growth in trailing 3 years."""
    grew = (sharesbas > sharesbas.shift(_TD_QTR)).astype(float)
    return _rolling_sum(grew, _TD_3Y)


def dla_051_shareswadil_growth_quarters_1y(shareswadil: pd.Series) -> pd.Series:
    """Count of quarters with positive diluted-share growth in trailing 1 year."""
    grew = (shareswadil > shareswadil.shift(_TD_QTR)).astype(float)
    return _rolling_sum(grew, _TD_YEAR)


def dla_052_sharesbas_fraction_growing_3y(sharesbas: pd.Series) -> pd.Series:
    """Fraction of 3-year window where basic shares grew QoQ."""
    grew = (sharesbas > sharesbas.shift(_TD_QTR)).astype(float)
    return _rolling_mean(grew, _TD_3Y)


def dla_053_sharesbas_max_qoq_pct_1y(sharesbas: pd.Series) -> pd.Series:
    """Peak single-quarter share-count growth rate in trailing 1 year (issuance intensity)."""
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_QTR), sharesbas.shift(_TD_QTR).replace(0, np.nan))
    return _rolling_max(pct, _TD_YEAR)


def dla_054_sharesbas_max_qoq_pct_3y(sharesbas: pd.Series) -> pd.Series:
    """Peak single-quarter share-count growth rate in trailing 3 years."""
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_QTR), sharesbas.shift(_TD_QTR).replace(0, np.nan))
    return _rolling_max(pct, _TD_3Y)


def dla_055_recent_issuance_recency_flag(ncfcommon: pd.Series) -> pd.Series:
    """1 if equity was raised (ncfcommon > 0) in the most recent quarter."""
    return (ncfcommon > 0).astype(float)


# --- Group F (056-065): Cumulative dilution over multi-year windows ---

def dla_056_sharesbas_cumulative_dilution_2y(sharesbas: pd.Series) -> pd.Series:
    """Cumulative share-count increase over 2 years as fraction of starting count."""
    prior = sharesbas.shift(_TD_2Y)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def dla_057_sharesbas_cumulative_dilution_3y(sharesbas: pd.Series) -> pd.Series:
    """Cumulative share-count increase over 3 years as fraction of starting count."""
    prior = sharesbas.shift(_TD_3Y)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def dla_058_sharesbas_at_expanding_max_flag(sharesbas: pd.Series) -> pd.Series:
    """Binary: 1 if basic shares equal their all-history expanding maximum (new all-time dilution high)."""
    expanding_max = sharesbas.expanding(min_periods=1).max()
    return (sharesbas >= expanding_max).astype(float)


def dla_059_sharesbas_expanding_peak(sharesbas: pd.Series) -> pd.Series:
    """All-history expanding maximum share count (tracks share-count ceiling)."""
    return sharesbas.expanding(min_periods=1).max()


def dla_060_sharesbas_vs_expanding_min(sharesbas: pd.Series) -> pd.Series:
    """Current shares vs all-history expanding minimum (how far above trough)."""
    mn = sharesbas.expanding(min_periods=1).min()
    return sharesbas - mn


def dla_061_sharesbas_at_3y_high_flag(sharesbas: pd.Series) -> pd.Series:
    """1 if current basic shares are at or above 3-year rolling maximum."""
    mx = _rolling_max(sharesbas, _TD_3Y)
    return (sharesbas >= mx).astype(float)


def dla_062_ncfcommon_cumulative_3y(ncfcommon: pd.Series) -> pd.Series:
    """Cumulative net equity raised over 3 years (3Y rolling sum of ncfcommon)."""
    return _rolling_sum(ncfcommon, _TD_3Y)


def dla_063_ncfcommon_cumulative_5y(ncfcommon: pd.Series) -> pd.Series:
    """Cumulative net equity raised over 5 years."""
    return _rolling_sum(ncfcommon, _TD_5Y)


def dla_064_sbcomp_cumulative_3y(sbcomp: pd.Series) -> pd.Series:
    """Cumulative stock-based compensation over 3 years."""
    return _rolling_sum(sbcomp, _TD_3Y)


def dla_065_sbcomp_to_ncfcommon_ratio(sbcomp: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    """
    SBC as fraction of total equity raised (SBC + positive ncfcommon).
    Measures how much dilution is SBC-driven vs pure secondary issuance.
    """
    ttm_sbc = _rolling_sum(sbcomp, _TD_YEAR)
    ttm_iss = _rolling_sum(ncfcommon.clip(lower=0), _TD_YEAR)
    total   = ttm_sbc + ttm_iss
    return _safe_div(ttm_sbc, total.replace(0, np.nan))


# --- Group G (066-075): Distress dilution and z-score / rank signals ---

def dla_066_distress_dilution_flag(sharesbas: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Binary: 1 if shares grew QoQ while equity is negative or zero
    (diluting into negative book equity — maximum distress signature).
    """
    shares_grew  = (sharesbas > sharesbas.shift(_TD_QTR)).astype(float)
    equity_neg   = (equity <= 0).astype(float)
    return shares_grew * equity_neg


def dla_067_sharesbas_zscore_4q(sharesbas: pd.Series) -> pd.Series:
    """Z-score of basic shares within trailing 4-quarter (252-day) window."""
    return _zscore_rolling(sharesbas, _TD_YEAR)


def dla_068_sharesbas_zscore_8q(sharesbas: pd.Series) -> pd.Series:
    """Z-score of basic shares within trailing 8-quarter (504-day) window."""
    return _zscore_rolling(sharesbas, _TD_2Y)


def dla_069_sharesbas_pct_rank_4q(sharesbas: pd.Series) -> pd.Series:
    """Percentile rank of basic shares within trailing 4-quarter window."""
    return _rolling_rank_pct(sharesbas, _TD_YEAR)


def dla_070_sharesbas_pct_rank_3y(sharesbas: pd.Series) -> pd.Series:
    """Percentile rank of basic shares within trailing 3-year window."""
    return _rolling_rank_pct(sharesbas, _TD_3Y)


def dla_071_sharesbas_expanding_pct_rank(sharesbas: pd.Series) -> pd.Series:
    """Expanding percentile rank of basic shares (all-history share-count rank)."""
    return sharesbas.expanding(min_periods=2).rank(pct=True)


def dla_072_shareswadil_zscore_4q(shareswadil: pd.Series) -> pd.Series:
    """Z-score of diluted WA shares within trailing 4-quarter window."""
    return _zscore_rolling(shareswadil, _TD_YEAR)


def dla_073_sbcomp_zscore_4q(sbcomp: pd.Series) -> pd.Series:
    """Z-score of stock-based compensation within trailing 4-quarter window."""
    return _zscore_rolling(sbcomp, _TD_YEAR)


def dla_074_dilution_composite_qoq(sharesbas: pd.Series, shareswadil: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    """
    Composite dilution-pressure score (equal-weight z-scores):
    - QoQ sharesbas growth z-score
    - QoQ shareswadil growth z-score
    - Positive ncfcommon flag z-score
    All computed within a 4-quarter trailing window.
    """
    bas_chg  = sharesbas - sharesbas.shift(_TD_QTR)
    dil_chg  = shareswadil - shareswadil.shift(_TD_QTR)
    iss_flag = (ncfcommon > 0).astype(float)
    z1 = _zscore_rolling(bas_chg, _TD_YEAR)
    z2 = _zscore_rolling(dil_chg, _TD_YEAR)
    z3 = _zscore_rolling(iss_flag, _TD_YEAR)
    return (z1 + z2 + z3) / 3.0


def dla_075_sharesbas_ewm_deviation(sharesbas: pd.Series) -> pd.Series:
    """
    Current basic shares minus their 4-quarter EWM (span=252).
    Captures how much recent issuance deviates from the smoothed trend.
    """
    ewm = _ewm_mean(sharesbas, _TD_YEAR)
    return sharesbas - ewm


# ── Registry 001-075 ──────────────────────────────────────────────────────────

DILUTION_ACCELERATION_REGISTRY_001_075 = {
    "dla_001_sharesbas_qoq_change":                 {"inputs": ["sharesbas"],                              "func": dla_001_sharesbas_qoq_change},
    "dla_002_sharesbas_yoy_change":                 {"inputs": ["sharesbas"],                              "func": dla_002_sharesbas_yoy_change},
    "dla_003_sharesbas_qoq_pct":                    {"inputs": ["sharesbas"],                              "func": dla_003_sharesbas_qoq_pct},
    "dla_004_sharesbas_yoy_pct":                    {"inputs": ["sharesbas"],                              "func": dla_004_sharesbas_yoy_pct},
    "dla_005_shareswa_qoq_change":                  {"inputs": ["shareswa"],                               "func": dla_005_shareswa_qoq_change},
    "dla_006_shareswa_yoy_change":                  {"inputs": ["shareswa"],                               "func": dla_006_shareswa_yoy_change},
    "dla_007_shareswa_qoq_pct":                     {"inputs": ["shareswa"],                               "func": dla_007_shareswa_qoq_pct},
    "dla_008_shareswa_yoy_pct":                     {"inputs": ["shareswa"],                               "func": dla_008_shareswa_yoy_pct},
    "dla_009_shareswadil_qoq_change":               {"inputs": ["shareswadil"],                            "func": dla_009_shareswadil_qoq_change},
    "dla_010_shareswadil_yoy_change":               {"inputs": ["shareswadil"],                            "func": dla_010_shareswadil_yoy_change},
    "dla_011_shareswadil_qoq_pct":                  {"inputs": ["shareswadil"],                            "func": dla_011_shareswadil_qoq_pct},
    "dla_012_shareswadil_yoy_pct":                  {"inputs": ["shareswadil"],                            "func": dla_012_shareswadil_yoy_pct},
    "dla_013_sharesbas_2y_change":                  {"inputs": ["sharesbas"],                              "func": dla_013_sharesbas_2y_change},
    "dla_014_sharesbas_3y_change":                  {"inputs": ["sharesbas"],                              "func": dla_014_sharesbas_3y_change},
    "dla_015_sharesbas_at_5y_high_flag":             {"inputs": ["sharesbas"],                              "func": dla_015_sharesbas_at_5y_high_flag},
    "dla_016_diluted_basic_gap":                    {"inputs": ["shareswadil", "shareswa"],                "func": dla_016_diluted_basic_gap},
    "dla_017_diluted_basic_gap_pct":                {"inputs": ["shareswadil", "shareswa"],                "func": dla_017_diluted_basic_gap_pct},
    "dla_018_diluted_basic_gap_qoq_change":         {"inputs": ["shareswadil", "shareswa"],                "func": dla_018_diluted_basic_gap_qoq_change},
    "dla_019_diluted_basic_gap_pct_rank_4q":        {"inputs": ["shareswadil", "shareswa"],                "func": dla_019_diluted_basic_gap_pct_rank_4q},
    "dla_020_diluted_basic_gap_drawdown_from_2y_peak": {"inputs": ["shareswadil", "shareswa"],             "func": dla_020_diluted_basic_gap_drawdown_from_2y_peak},
    "dla_021_diluted_vs_basic_ratio":               {"inputs": ["shareswadil", "shareswa"],                "func": dla_021_diluted_vs_basic_ratio},
    "dla_022_diluted_vs_basic_ratio_zscore_4q":     {"inputs": ["shareswadil", "shareswa"],                "func": dla_022_diluted_vs_basic_ratio_zscore_4q},
    "dla_023_shareswadil_pct_rank_4q":              {"inputs": ["shareswadil"],                            "func": dla_023_shareswadil_pct_rank_4q},
    "dla_024_shareswadil_vs_sharesbas_gap":         {"inputs": ["shareswadil", "sharesbas"],               "func": dla_024_shareswadil_vs_sharesbas_gap},
    "dla_025_shareswadil_vs_sharesbas_pct":         {"inputs": ["shareswadil", "sharesbas"],               "func": dla_025_shareswadil_vs_sharesbas_pct},
    "dla_026_sharesbas_qoq_large_jump_flag":        {"inputs": ["sharesbas"],                              "func": dla_026_sharesbas_qoq_large_jump_flag},
    "dla_027_sharesbas_qoq_very_large_jump_flag":   {"inputs": ["sharesbas"],                              "func": dla_027_sharesbas_qoq_very_large_jump_flag},
    "dla_028_sharesbas_yoy_large_jump_flag":        {"inputs": ["sharesbas"],                              "func": dla_028_sharesbas_yoy_large_jump_flag},
    "dla_029_ncfcommon_positive_flag":              {"inputs": ["ncfcommon"],                              "func": dla_029_ncfcommon_positive_flag},
    "dla_030_ncfcommon_level":                      {"inputs": ["ncfcommon"],                              "func": dla_030_ncfcommon_level},
    "dla_031_ncfcommon_yoy_change":                 {"inputs": ["ncfcommon"],                              "func": dla_031_ncfcommon_yoy_change},
    "dla_032_ncfcommon_trailing_4q_sum":            {"inputs": ["ncfcommon"],                              "func": dla_032_ncfcommon_trailing_4q_sum},
    "dla_033_ncfcommon_trailing_8q_sum":            {"inputs": ["ncfcommon"],                              "func": dla_033_ncfcommon_trailing_8q_sum},
    "dla_034_ncfcommon_trailing_12q_sum":           {"inputs": ["ncfcommon"],                              "func": dla_034_ncfcommon_trailing_12q_sum},
    "dla_035_issuance_quarters_1y":                 {"inputs": ["ncfcommon"],                              "func": dla_035_issuance_quarters_1y},
    "dla_036_ncfcommon_to_equity_ratio":            {"inputs": ["ncfcommon", "equity"],                   "func": dla_036_ncfcommon_to_equity_ratio},
    "dla_037_ncfcommon_to_assets_ratio":            {"inputs": ["ncfcommon", "assets"],                   "func": dla_037_ncfcommon_to_assets_ratio},
    "dla_038_sbcomp_to_equity_ratio":               {"inputs": ["sbcomp", "equity"],                      "func": dla_038_sbcomp_to_equity_ratio},
    "dla_039_sbcomp_to_shareswa_ratio":             {"inputs": ["sbcomp", "shareswa"],                    "func": dla_039_sbcomp_to_shareswa_ratio},
    "dla_040_sbcomp_yoy_change":                    {"inputs": ["sbcomp"],                                "func": dla_040_sbcomp_yoy_change},
    "dla_041_sbcomp_yoy_pct":                       {"inputs": ["sbcomp"],                                "func": dla_041_sbcomp_yoy_pct},
    "dla_042_sbcomp_trailing_4q_sum":               {"inputs": ["sbcomp"],                                "func": dla_042_sbcomp_trailing_4q_sum},
    "dla_043_sbcomp_trailing_8q_sum":               {"inputs": ["sbcomp"],                                "func": dla_043_sbcomp_trailing_8q_sum},
    "dla_044_sbcomp_plus_ncfcommon_to_equity":      {"inputs": ["sbcomp", "ncfcommon", "equity"],         "func": dla_044_sbcomp_plus_ncfcommon_to_equity},
    "dla_045_sharesbas_2y_pct_change":              {"inputs": ["sharesbas"],                              "func": dla_045_sharesbas_2y_pct_change},
    "dla_046_sharesbas_qoq_positive_flag":          {"inputs": ["sharesbas"],                              "func": dla_046_sharesbas_qoq_positive_flag},
    "dla_047_sharesbas_consecutive_growth_streak":  {"inputs": ["sharesbas"],                              "func": dla_047_sharesbas_consecutive_growth_streak},
    "dla_048_sharesbas_growth_quarters_1y":         {"inputs": ["sharesbas"],                              "func": dla_048_sharesbas_growth_quarters_1y},
    "dla_049_sharesbas_growth_quarters_2y":         {"inputs": ["sharesbas"],                              "func": dla_049_sharesbas_growth_quarters_2y},
    "dla_050_sharesbas_growth_quarters_3y":         {"inputs": ["sharesbas"],                              "func": dla_050_sharesbas_growth_quarters_3y},
    "dla_051_shareswadil_growth_quarters_1y":       {"inputs": ["shareswadil"],                            "func": dla_051_shareswadil_growth_quarters_1y},
    "dla_052_sharesbas_fraction_growing_3y":        {"inputs": ["sharesbas"],                              "func": dla_052_sharesbas_fraction_growing_3y},
    "dla_053_sharesbas_max_qoq_pct_1y":             {"inputs": ["sharesbas"],                              "func": dla_053_sharesbas_max_qoq_pct_1y},
    "dla_054_sharesbas_max_qoq_pct_3y":             {"inputs": ["sharesbas"],                              "func": dla_054_sharesbas_max_qoq_pct_3y},
    "dla_055_recent_issuance_recency_flag":         {"inputs": ["ncfcommon"],                              "func": dla_055_recent_issuance_recency_flag},
    "dla_056_sharesbas_cumulative_dilution_2y":     {"inputs": ["sharesbas"],                              "func": dla_056_sharesbas_cumulative_dilution_2y},
    "dla_057_sharesbas_cumulative_dilution_3y":     {"inputs": ["sharesbas"],                              "func": dla_057_sharesbas_cumulative_dilution_3y},
    "dla_058_sharesbas_at_expanding_max_flag":      {"inputs": ["sharesbas"],                              "func": dla_058_sharesbas_at_expanding_max_flag},
    "dla_059_sharesbas_expanding_peak":             {"inputs": ["sharesbas"],                              "func": dla_059_sharesbas_expanding_peak},
    "dla_060_sharesbas_vs_expanding_min":           {"inputs": ["sharesbas"],                              "func": dla_060_sharesbas_vs_expanding_min},
    "dla_061_sharesbas_at_3y_high_flag":            {"inputs": ["sharesbas"],                              "func": dla_061_sharesbas_at_3y_high_flag},
    "dla_062_ncfcommon_cumulative_3y":              {"inputs": ["ncfcommon"],                              "func": dla_062_ncfcommon_cumulative_3y},
    "dla_063_ncfcommon_cumulative_5y":              {"inputs": ["ncfcommon"],                              "func": dla_063_ncfcommon_cumulative_5y},
    "dla_064_sbcomp_cumulative_3y":                 {"inputs": ["sbcomp"],                                "func": dla_064_sbcomp_cumulative_3y},
    "dla_065_sbcomp_to_ncfcommon_ratio":            {"inputs": ["sbcomp", "ncfcommon"],                   "func": dla_065_sbcomp_to_ncfcommon_ratio},
    "dla_066_distress_dilution_flag":               {"inputs": ["sharesbas", "equity"],                   "func": dla_066_distress_dilution_flag},
    "dla_067_sharesbas_zscore_4q":                  {"inputs": ["sharesbas"],                              "func": dla_067_sharesbas_zscore_4q},
    "dla_068_sharesbas_zscore_8q":                  {"inputs": ["sharesbas"],                              "func": dla_068_sharesbas_zscore_8q},
    "dla_069_sharesbas_pct_rank_4q":                {"inputs": ["sharesbas"],                              "func": dla_069_sharesbas_pct_rank_4q},
    "dla_070_sharesbas_pct_rank_3y":                {"inputs": ["sharesbas"],                              "func": dla_070_sharesbas_pct_rank_3y},
    "dla_071_sharesbas_expanding_pct_rank":         {"inputs": ["sharesbas"],                              "func": dla_071_sharesbas_expanding_pct_rank},
    "dla_072_shareswadil_zscore_4q":                {"inputs": ["shareswadil"],                            "func": dla_072_shareswadil_zscore_4q},
    "dla_073_sbcomp_zscore_4q":                     {"inputs": ["sbcomp"],                                "func": dla_073_sbcomp_zscore_4q},
    "dla_074_dilution_composite_qoq":               {"inputs": ["sharesbas", "shareswadil", "ncfcommon"], "func": dla_074_dilution_composite_qoq},
    "dla_075_sharesbas_ewm_deviation":              {"inputs": ["sharesbas"],                              "func": dla_075_sharesbas_ewm_deviation},
}
