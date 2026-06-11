"""
69_equity_erosion — Base Features 076-150
Domain: shareholders'-equity erosion (equity-VALUE side) — retained-earnings erosion
pace, net-loss accumulation effect on equity, equity-versus-liabilities dynamics,
preferred equity overhang, EWM smoothed equity trends, net-income cumulative
damage on book value, tangible-book-per-share decay, OCI vs equity share,
equity sufficiency ratios, multi-year equity low flags.
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
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63
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
    """Element-wise division; replaces zero denominators with NaN.
    Negative denominators are preserved — negative equity is a meaningful distress signal."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of denominator; sign-agnostic ratio."""
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group I (076-090): Retained-earnings erosion pace and net-loss accumulation ---

def eqe_076_retearn_ttm_change(retearn: pd.Series) -> pd.Series:
    """Trailing-12-month change in retained earnings (retearn vs retearn 252 days ago)."""
    return retearn - retearn.shift(_TD_YEAR)


def eqe_077_retearn_cumulative_loss_4q(retearn: pd.Series, netinc: pd.Series) -> pd.Series:
    """Rolling 4-quarter sum of net income — cumulative earnings absorbed into retearn."""
    return _rolling_sum(netinc, _TD_YEAR)


def eqe_078_retearn_cumulative_loss_8q(retearn: pd.Series, netinc: pd.Series) -> pd.Series:
    """Rolling 8-quarter sum of net income — longer-term earnings absorbed into retearn."""
    return _rolling_sum(netinc, _TD_2Y)


def eqe_079_retearn_deficit_to_equity(retearn: pd.Series, equity: pd.Series) -> pd.Series:
    """Retained-earnings-to-equity ratio; negative means accumulated deficit vs. equity."""
    return _safe_div(retearn, equity.abs().replace(0, np.nan))


def eqe_080_retearn_as_pct_assets(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Retained earnings as a fraction of total assets."""
    return _safe_div(retearn, assets)


def eqe_081_retearn_ewm_trend_1y(retearn: pd.Series) -> pd.Series:
    """EWM (span=252) of retained earnings — smoothed level."""
    return _ewm_mean(retearn, _TD_YEAR)


def eqe_082_retearn_deviation_from_ewm(retearn: pd.Series) -> pd.Series:
    """Retained earnings minus its 1-year EWM (deviation from smoothed trend)."""
    return retearn - _ewm_mean(retearn, _TD_YEAR)


def eqe_083_retearn_pct_rank_3y(retearn: pd.Series) -> pd.Series:
    """Rolling 3-year (756-day) percentile rank of retained earnings (low rank = deep accumulated deficit)."""
    return _rolling_rank_pct(retearn, _TD_3Y)


def eqe_084_retearn_at_expanding_min(retearn: pd.Series) -> pd.Series:
    """Binary: 1 if retearn equals its all-time (expanding) minimum (new all-time deficit)."""
    expanding_min = retearn.expanding(min_periods=1).min()
    return (retearn <= expanding_min).astype(float)


def eqe_085_netinc_ttm_sum(netinc: pd.Series) -> pd.Series:
    """Trailing-12-month sum of net income — total annual earnings power."""
    return _rolling_sum(netinc, _TD_YEAR)


def eqe_086_netinc_ttm_sum_yoy_change(netinc: pd.Series) -> pd.Series:
    """YoY change in the TTM net income sum."""
    ttm = _rolling_sum(netinc, _TD_YEAR)
    return ttm - ttm.shift(_TD_YEAR)


def eqe_087_netinc_2y_sum(netinc: pd.Series) -> pd.Series:
    """2-year cumulative sum of net income."""
    return _rolling_sum(netinc, _TD_2Y)


def eqe_088_equity_minus_retearn_trend(equity: pd.Series, retearn: pd.Series) -> pd.Series:
    """Paid-in capital proxy: equity - retearn (captures contributed capital vs. retained earnings)."""
    return equity - retearn


def eqe_089_equity_minus_retearn_yoy_change(equity: pd.Series, retearn: pd.Series) -> pd.Series:
    """YoY change in (equity - retearn) — measures non-retained-earnings equity shifts."""
    base = equity - retearn
    return base - base.shift(_TD_YEAR)


def eqe_090_retearn_rolling_min_2y(retearn: pd.Series) -> pd.Series:
    """Rolling 2-year minimum of retained earnings."""
    return _rolling_min(retearn, _TD_2Y)


# --- Group J (091-105): Equity vs. liabilities and leverage dynamics ---

def eqe_091_debt_to_equity(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Total debt to equity ratio; negative equity produces negative ratio (distress signal)."""
    return _safe_div(debt, equity)


def eqe_092_debt_to_equity_qoq_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in debt/equity ratio."""
    ratio = _safe_div(debt, equity)
    return ratio - ratio.shift(_TD_QTR)


def eqe_093_debt_to_equity_yoy_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in debt/equity ratio."""
    ratio = _safe_div(debt, equity)
    return ratio - ratio.shift(_TD_YEAR)


def eqe_094_liabilities_to_equity(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """Total liabilities to equity ratio."""
    return _safe_div(liabilities, equity)


def eqe_095_liabilities_to_equity_yoy_change(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in liabilities/equity."""
    ratio = _safe_div(liabilities, equity)
    return ratio - ratio.shift(_TD_YEAR)


def eqe_096_equity_less_liabilities(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Net asset surplus: equity - liabilities (deeply negative = severely insolvent)."""
    return equity - liabilities


def eqe_097_equity_covers_liabilities(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Binary: 1 if equity >= liabilities (equity covers all liabilities), else 0."""
    return (equity >= liabilities).astype(float)


def eqe_098_equity_shrinkage_vs_liab_growth(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Equity YoY change minus liabilities YoY change — joint stress indicator."""
    eq_chg  = equity     - equity.shift(_TD_YEAR)
    lia_chg = liabilities - liabilities.shift(_TD_YEAR)
    return eq_chg - lia_chg


def eqe_099_equity_to_liabilities_ratio(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Equity / liabilities — solvency buffer ratio."""
    return _safe_div(equity, liabilities)


def eqe_100_equity_to_liabilities_qoq_change(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """QoQ change in equity/liabilities ratio."""
    ratio = _safe_div(equity, liabilities)
    return ratio - ratio.shift(_TD_QTR)


def eqe_101_debtnc_to_equity(debtnc: pd.Series, equity: pd.Series) -> pd.Series:
    """Non-current debt to equity ratio."""
    return _safe_div(debtnc, equity)


def eqe_102_equity_drawdown_normalized_by_assets(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Equity drawdown from 2-year peak normalized by total assets."""
    drawdown = equity - _rolling_max(equity, _TD_2Y)
    return _safe_div(drawdown, assets)


def eqe_103_equity_to_assets_3y_change(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """3-year change in equity/assets ratio."""
    ratio = _safe_div(equity, assets)
    return ratio - ratio.shift(_TD_3Y)


def eqe_104_equity_to_assets_zscore_4q(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 4-quarter z-score of equity/assets ratio."""
    ratio = _safe_div(equity, assets)
    return _zscore_rolling(ratio, _TD_YEAR)


def eqe_105_equity_to_assets_pct_rank_4q(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 4-quarter percentile rank of equity/assets (low rank = severe leverage)."""
    ratio = _safe_div(equity, assets)
    return _rolling_rank_pct(ratio, _TD_YEAR)


# --- Group K (106-120): Preferred equity overhang and common-equity residual ---

def eqe_106_prefdivis_to_equity(prefdivis: pd.Series, equity: pd.Series) -> pd.Series:
    """Preferred dividends as a fraction of total equity — overhang on common equity."""
    return _safe_div_abs(prefdivis, equity)


def eqe_107_prefdivis_yoy_change(prefdivis: pd.Series) -> pd.Series:
    """YoY change in preferred dividends paid."""
    return prefdivis - prefdivis.shift(_TD_YEAR)


def eqe_108_common_equity_proxy(equity: pd.Series, prefdivis: pd.Series) -> pd.Series:
    """Common equity proxy: equity minus trailing-12-month preferred dividends."""
    pref_ttm = _rolling_sum(prefdivis, _TD_YEAR)
    return equity - pref_ttm


def eqe_109_common_equity_proxy_yoy_change(equity: pd.Series, prefdivis: pd.Series) -> pd.Series:
    """YoY change in common equity proxy (equity - TTM preferred divs)."""
    pref_ttm = _rolling_sum(prefdivis, _TD_YEAR)
    base = equity - pref_ttm
    return base - base.shift(_TD_YEAR)


def eqe_110_common_equity_proxy_is_negative(equity: pd.Series, prefdivis: pd.Series) -> pd.Series:
    """Binary: 1 if common equity proxy < 0."""
    pref_ttm = _rolling_sum(prefdivis, _TD_YEAR)
    return ((equity - pref_ttm) < 0).astype(float)


def eqe_111_equity_qoq_decline_magnitude(equity: pd.Series) -> pd.Series:
    """Magnitude of QoQ equity decline; zero when equity increases."""
    delta = equity - equity.shift(_TD_QTR)
    return delta.clip(upper=0)


def eqe_112_equity_at_2y_low(equity: pd.Series) -> pd.Series:
    """Binary: 1 if total equity equals its rolling 2-year minimum (new 2-year book low)."""
    low2 = _rolling_min(equity, _TD_2Y)
    return (equity <= low2).astype(float)


def eqe_113_retearn_qoq_decline_magnitude(retearn: pd.Series) -> pd.Series:
    """Magnitude of QoQ retained-earnings decline; zero when retearn increases."""
    delta = retearn - retearn.shift(_TD_QTR)
    return delta.clip(upper=0)


def eqe_114_equity_rolling_mean_1y(equity: pd.Series) -> pd.Series:
    """Rolling 1-year mean of total equity."""
    return _rolling_mean(equity, _TD_YEAR)


def eqe_115_equity_vs_1y_mean(equity: pd.Series) -> pd.Series:
    """Total equity minus its rolling 1-year mean (deviation below trend)."""
    return equity - _rolling_mean(equity, _TD_YEAR)


def eqe_116_equity_rolling_mean_2y(equity: pd.Series) -> pd.Series:
    """Rolling 2-year mean of total equity."""
    return _rolling_mean(equity, _TD_2Y)


def eqe_117_equity_vs_2y_mean(equity: pd.Series) -> pd.Series:
    """Total equity minus its rolling 2-year mean."""
    return equity - _rolling_mean(equity, _TD_2Y)


def eqe_118_equity_ewm_1y(equity: pd.Series) -> pd.Series:
    """Exponentially weighted mean of equity (span=252)."""
    return _ewm_mean(equity, _TD_YEAR)


def eqe_119_equity_deviation_from_ewm(equity: pd.Series) -> pd.Series:
    """Equity minus its 1-year EWM — deviation from smoothed level."""
    return equity - _ewm_mean(equity, _TD_YEAR)


def eqe_120_equity_ewm_2y(equity: pd.Series) -> pd.Series:
    """Exponentially weighted mean of equity (span=504)."""
    return _ewm_mean(equity, _TD_2Y)


# --- Group L (121-135): Tangible book per share and intangibles burden ---

def eqe_121_tangible_bvps(equity: pd.Series, intangibles: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Tangible book value per share: (equity - intangibles) / sharesbas."""
    tbe = equity - intangibles
    return _safe_div(tbe, sharesbas)


def eqe_122_tangible_bvps_qoq_change(equity: pd.Series, intangibles: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """QoQ change in tangible book value per share."""
    tbvps = _safe_div(equity - intangibles, sharesbas)
    return tbvps - tbvps.shift(_TD_QTR)


def eqe_123_tangible_bvps_yoy_change(equity: pd.Series, intangibles: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """YoY change in tangible book value per share."""
    tbvps = _safe_div(equity - intangibles, sharesbas)
    return tbvps - tbvps.shift(_TD_YEAR)


def eqe_124_tangible_bvps_yoy_pct(equity: pd.Series, intangibles: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """YoY percent change in tangible book value per share."""
    tbvps = _safe_div(equity - intangibles, sharesbas)
    prior = tbvps.shift(_TD_YEAR)
    return _safe_div_abs(tbvps - prior, prior)


def eqe_125_tangible_bvps_drawdown_from_2y_peak(equity: pd.Series, intangibles: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Tangible BVPS minus its rolling 2-year maximum."""
    tbvps = _safe_div(equity - intangibles, sharesbas)
    return tbvps - _rolling_max(tbvps, _TD_2Y)


def eqe_126_intangibles_to_equity(intangibles: pd.Series, equity: pd.Series) -> pd.Series:
    """Intangibles as a fraction of equity (high ratio = thin tangible book)."""
    return _safe_div_abs(intangibles, equity)


def eqe_127_intangibles_to_equity_yoy_change(intangibles: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in intangibles/equity ratio."""
    ratio = _safe_div_abs(intangibles, equity)
    return ratio - ratio.shift(_TD_YEAR)


def eqe_128_equity_excl_oci(equity: pd.Series, accoci: pd.Series) -> pd.Series:
    """Equity excluding accumulated OCI: equity - accoci (core operating book value)."""
    return equity - accoci


def eqe_129_equity_excl_oci_yoy_change(equity: pd.Series, accoci: pd.Series) -> pd.Series:
    """YoY change in equity excluding OCI."""
    base = equity - accoci
    return base - base.shift(_TD_YEAR)


def eqe_130_accoci_to_equity(accoci: pd.Series, equity: pd.Series) -> pd.Series:
    """Accumulated OCI as a fraction of equity (negative = OCI is a drag on book)."""
    return _safe_div(accoci, equity.abs().replace(0, np.nan))


def eqe_131_accoci_to_equity_yoy_change(accoci: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in accoci/equity ratio."""
    ratio = _safe_div(accoci, equity.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def eqe_132_tangible_equity_to_assets(equity: pd.Series, intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Tangible equity / total assets ratio."""
    return _safe_div(equity - intangibles, assets)


def eqe_133_tangible_equity_to_assets_yoy_change(equity: pd.Series, intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in tangible equity/assets ratio."""
    ratio = _safe_div(equity - intangibles, assets)
    return ratio - ratio.shift(_TD_YEAR)


def eqe_134_tangible_equity_drawdown_from_expanding_peak(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Tangible equity minus its all-time (expanding) maximum."""
    tbe  = equity - intangibles
    peak = tbe.expanding(min_periods=1).max()
    return tbe - peak


def eqe_135_tangible_bvps_is_negative(equity: pd.Series, intangibles: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Binary: 1 if tangible BVPS < 0."""
    tbvps = _safe_div(equity - intangibles, sharesbas)
    return (tbvps < 0).astype(float)


# --- Group M (136-150): Multi-year low flags, OLS slope, and advanced ratios ---

def eqe_136_equity_at_3y_low(equity: pd.Series) -> pd.Series:
    """Binary: 1 if equity equals its rolling 3-year minimum (new 3-year book low)."""
    low3 = _rolling_min(equity, _TD_3Y)
    return (equity <= low3).astype(float)


def eqe_137_retearn_at_3y_low(retearn: pd.Series) -> pd.Series:
    """Binary: 1 if retearn equals its rolling 3-year minimum."""
    low3 = _rolling_min(retearn, _TD_3Y)
    return (retearn <= low3).astype(float)


def eqe_138_bvps_at_3y_low(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Binary: 1 if BVPS equals its rolling 3-year minimum."""
    bvps = _safe_div(equity, sharesbas)
    low3 = _rolling_min(bvps, _TD_3Y)
    return (bvps <= low3).astype(float)


def eqe_139_equity_ols_slope_1y(equity: pd.Series) -> pd.Series:
    """
    Rolling 1-year OLS slope of total equity (units: equity per trading day).
    Negative slope = equity on a declining trend.
    """
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return float(((x - xm) * (arr - ym)).sum() / denom)
    return equity.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def eqe_140_retearn_ols_slope_1y(retearn: pd.Series) -> pd.Series:
    """
    Rolling 1-year OLS slope of retained earnings.
    Negative slope = retained earnings on a declining trend.
    """
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return float(((x - xm) * (arr - ym)).sum() / denom)
    return retearn.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def eqe_141_equity_ols_slope_2y(equity: pd.Series) -> pd.Series:
    """Rolling 2-year OLS slope of total equity."""
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return float(((x - xm) * (arr - ym)).sum() / denom)
    return equity.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(_slope, raw=True)


def eqe_142_equity_zscore_12q(equity: pd.Series) -> pd.Series:
    """Rolling 12-quarter (3-year) z-score of total equity."""
    return _zscore_rolling(equity, _TD_3Y)


def eqe_143_retearn_zscore_8q(retearn: pd.Series) -> pd.Series:
    """Rolling 8-quarter (2-year) z-score of retained earnings."""
    return _zscore_rolling(retearn, _TD_2Y)


def eqe_144_equity_pct_rank_12q(equity: pd.Series) -> pd.Series:
    """Rolling 12-quarter percentile rank of total equity."""
    return _rolling_rank_pct(equity, _TD_3Y)


def eqe_145_retearn_pct_rank_8q(retearn: pd.Series) -> pd.Series:
    """Rolling 8-quarter percentile rank of retained earnings."""
    return _rolling_rank_pct(retearn, _TD_2Y)


def eqe_146_equity_expanding_pct_rank(equity: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of equity — absolute historical position."""
    return equity.expanding(min_periods=2).rank(pct=True)


def eqe_147_retearn_expanding_pct_rank(retearn: pd.Series) -> pd.Series:
    """Expanding percentile rank of retained earnings."""
    return retearn.expanding(min_periods=2).rank(pct=True)


def eqe_148_equity_median_4q(equity: pd.Series) -> pd.Series:
    """Rolling 4-quarter median of total equity."""
    return _rolling_median(equity, _TD_YEAR)


def eqe_149_equity_vs_median_4q(equity: pd.Series) -> pd.Series:
    """Total equity minus its rolling 4-quarter median (deviation below typical level)."""
    return equity - _rolling_median(equity, _TD_YEAR)


def eqe_150_equity_erosion_deep_composite(equity: pd.Series, retearn: pd.Series, assets: pd.Series, intangibles: pd.Series) -> pd.Series:
    """
    Extended composite equity-erosion severity:
    average of z-scores for equity, retearn, tangible equity, and equity/assets.
    More negative = deeper multi-dimensional distress.
    """
    z_eq  = _zscore_rolling(equity, _TD_YEAR)
    z_re  = _zscore_rolling(retearn, _TD_YEAR)
    tbe   = equity - intangibles
    z_tbe = _zscore_rolling(tbe, _TD_YEAR)
    ea    = _safe_div(equity, assets)
    z_ea  = _zscore_rolling(ea, _TD_YEAR)
    return (z_eq + z_re + z_tbe + z_ea) / 4.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

EQUITY_EROSION_REGISTRY_076_150 = {
    "eqe_076_retearn_ttm_change":                        {"inputs": ["retearn"],                                         "func": eqe_076_retearn_ttm_change},
    "eqe_077_retearn_cumulative_loss_4q":                {"inputs": ["retearn", "netinc"],                               "func": eqe_077_retearn_cumulative_loss_4q},
    "eqe_078_retearn_cumulative_loss_8q":                {"inputs": ["retearn", "netinc"],                               "func": eqe_078_retearn_cumulative_loss_8q},
    "eqe_079_retearn_deficit_to_equity":                 {"inputs": ["retearn", "equity"],                               "func": eqe_079_retearn_deficit_to_equity},
    "eqe_080_retearn_as_pct_assets":                     {"inputs": ["retearn", "assets"],                               "func": eqe_080_retearn_as_pct_assets},
    "eqe_081_retearn_ewm_trend_1y":                      {"inputs": ["retearn"],                                         "func": eqe_081_retearn_ewm_trend_1y},
    "eqe_082_retearn_deviation_from_ewm":                {"inputs": ["retearn"],                                         "func": eqe_082_retearn_deviation_from_ewm},
    "eqe_083_retearn_pct_rank_3y":                        {"inputs": ["retearn"],                                         "func": eqe_083_retearn_pct_rank_3y},
    "eqe_084_retearn_at_expanding_min":                  {"inputs": ["retearn"],                                         "func": eqe_084_retearn_at_expanding_min},
    "eqe_085_netinc_ttm_sum":                            {"inputs": ["netinc"],                                          "func": eqe_085_netinc_ttm_sum},
    "eqe_086_netinc_ttm_sum_yoy_change":                 {"inputs": ["netinc"],                                          "func": eqe_086_netinc_ttm_sum_yoy_change},
    "eqe_087_netinc_2y_sum":                             {"inputs": ["netinc"],                                          "func": eqe_087_netinc_2y_sum},
    "eqe_088_equity_minus_retearn_trend":                {"inputs": ["equity", "retearn"],                               "func": eqe_088_equity_minus_retearn_trend},
    "eqe_089_equity_minus_retearn_yoy_change":           {"inputs": ["equity", "retearn"],                               "func": eqe_089_equity_minus_retearn_yoy_change},
    "eqe_090_retearn_rolling_min_2y":                    {"inputs": ["retearn"],                                         "func": eqe_090_retearn_rolling_min_2y},
    "eqe_091_debt_to_equity":                            {"inputs": ["debt", "equity"],                                  "func": eqe_091_debt_to_equity},
    "eqe_092_debt_to_equity_qoq_change":                 {"inputs": ["debt", "equity"],                                  "func": eqe_092_debt_to_equity_qoq_change},
    "eqe_093_debt_to_equity_yoy_change":                 {"inputs": ["debt", "equity"],                                  "func": eqe_093_debt_to_equity_yoy_change},
    "eqe_094_liabilities_to_equity":                     {"inputs": ["liabilities", "equity"],                           "func": eqe_094_liabilities_to_equity},
    "eqe_095_liabilities_to_equity_yoy_change":          {"inputs": ["liabilities", "equity"],                           "func": eqe_095_liabilities_to_equity_yoy_change},
    "eqe_096_equity_less_liabilities":                   {"inputs": ["equity", "liabilities"],                           "func": eqe_096_equity_less_liabilities},
    "eqe_097_equity_covers_liabilities":                 {"inputs": ["equity", "liabilities"],                           "func": eqe_097_equity_covers_liabilities},
    "eqe_098_equity_shrinkage_vs_liab_growth":           {"inputs": ["equity", "liabilities"],                           "func": eqe_098_equity_shrinkage_vs_liab_growth},
    "eqe_099_equity_to_liabilities_ratio":               {"inputs": ["equity", "liabilities"],                           "func": eqe_099_equity_to_liabilities_ratio},
    "eqe_100_equity_to_liabilities_qoq_change":          {"inputs": ["equity", "liabilities"],                           "func": eqe_100_equity_to_liabilities_qoq_change},
    "eqe_101_debtnc_to_equity":                          {"inputs": ["debtnc", "equity"],                                "func": eqe_101_debtnc_to_equity},
    "eqe_102_equity_drawdown_normalized_by_assets":      {"inputs": ["equity", "assets"],                                "func": eqe_102_equity_drawdown_normalized_by_assets},
    "eqe_103_equity_to_assets_3y_change":                {"inputs": ["equity", "assets"],                                "func": eqe_103_equity_to_assets_3y_change},
    "eqe_104_equity_to_assets_zscore_4q":                {"inputs": ["equity", "assets"],                                "func": eqe_104_equity_to_assets_zscore_4q},
    "eqe_105_equity_to_assets_pct_rank_4q":              {"inputs": ["equity", "assets"],                                "func": eqe_105_equity_to_assets_pct_rank_4q},
    "eqe_106_prefdivis_to_equity":                       {"inputs": ["prefdivis", "equity"],                             "func": eqe_106_prefdivis_to_equity},
    "eqe_107_prefdivis_yoy_change":                      {"inputs": ["prefdivis"],                                       "func": eqe_107_prefdivis_yoy_change},
    "eqe_108_common_equity_proxy":                       {"inputs": ["equity", "prefdivis"],                             "func": eqe_108_common_equity_proxy},
    "eqe_109_common_equity_proxy_yoy_change":            {"inputs": ["equity", "prefdivis"],                             "func": eqe_109_common_equity_proxy_yoy_change},
    "eqe_110_common_equity_proxy_is_negative":           {"inputs": ["equity", "prefdivis"],                             "func": eqe_110_common_equity_proxy_is_negative},
    "eqe_111_equity_qoq_decline_magnitude":              {"inputs": ["equity"],                                          "func": eqe_111_equity_qoq_decline_magnitude},
    "eqe_112_equity_at_2y_low":                          {"inputs": ["equity"],                                          "func": eqe_112_equity_at_2y_low},
    "eqe_113_retearn_qoq_decline_magnitude":             {"inputs": ["retearn"],                                         "func": eqe_113_retearn_qoq_decline_magnitude},
    "eqe_114_equity_rolling_mean_1y":                    {"inputs": ["equity"],                                          "func": eqe_114_equity_rolling_mean_1y},
    "eqe_115_equity_vs_1y_mean":                         {"inputs": ["equity"],                                          "func": eqe_115_equity_vs_1y_mean},
    "eqe_116_equity_rolling_mean_2y":                    {"inputs": ["equity"],                                          "func": eqe_116_equity_rolling_mean_2y},
    "eqe_117_equity_vs_2y_mean":                         {"inputs": ["equity"],                                          "func": eqe_117_equity_vs_2y_mean},
    "eqe_118_equity_ewm_1y":                             {"inputs": ["equity"],                                          "func": eqe_118_equity_ewm_1y},
    "eqe_119_equity_deviation_from_ewm":                 {"inputs": ["equity"],                                          "func": eqe_119_equity_deviation_from_ewm},
    "eqe_120_equity_ewm_2y":                             {"inputs": ["equity"],                                          "func": eqe_120_equity_ewm_2y},
    "eqe_121_tangible_bvps":                             {"inputs": ["equity", "intangibles", "sharesbas"],              "func": eqe_121_tangible_bvps},
    "eqe_122_tangible_bvps_qoq_change":                  {"inputs": ["equity", "intangibles", "sharesbas"],              "func": eqe_122_tangible_bvps_qoq_change},
    "eqe_123_tangible_bvps_yoy_change":                  {"inputs": ["equity", "intangibles", "sharesbas"],              "func": eqe_123_tangible_bvps_yoy_change},
    "eqe_124_tangible_bvps_yoy_pct":                     {"inputs": ["equity", "intangibles", "sharesbas"],              "func": eqe_124_tangible_bvps_yoy_pct},
    "eqe_125_tangible_bvps_drawdown_from_2y_peak":       {"inputs": ["equity", "intangibles", "sharesbas"],              "func": eqe_125_tangible_bvps_drawdown_from_2y_peak},
    "eqe_126_intangibles_to_equity":                     {"inputs": ["intangibles", "equity"],                           "func": eqe_126_intangibles_to_equity},
    "eqe_127_intangibles_to_equity_yoy_change":          {"inputs": ["intangibles", "equity"],                           "func": eqe_127_intangibles_to_equity_yoy_change},
    "eqe_128_equity_excl_oci":                           {"inputs": ["equity", "accoci"],                                "func": eqe_128_equity_excl_oci},
    "eqe_129_equity_excl_oci_yoy_change":                {"inputs": ["equity", "accoci"],                                "func": eqe_129_equity_excl_oci_yoy_change},
    "eqe_130_accoci_to_equity":                          {"inputs": ["accoci", "equity"],                                "func": eqe_130_accoci_to_equity},
    "eqe_131_accoci_to_equity_yoy_change":               {"inputs": ["accoci", "equity"],                                "func": eqe_131_accoci_to_equity_yoy_change},
    "eqe_132_tangible_equity_to_assets":                 {"inputs": ["equity", "intangibles", "assets"],                 "func": eqe_132_tangible_equity_to_assets},
    "eqe_133_tangible_equity_to_assets_yoy_change":      {"inputs": ["equity", "intangibles", "assets"],                 "func": eqe_133_tangible_equity_to_assets_yoy_change},
    "eqe_134_tangible_equity_drawdown_from_expanding_peak": {"inputs": ["equity", "intangibles"],                        "func": eqe_134_tangible_equity_drawdown_from_expanding_peak},
    "eqe_135_tangible_bvps_is_negative":                 {"inputs": ["equity", "intangibles", "sharesbas"],              "func": eqe_135_tangible_bvps_is_negative},
    "eqe_136_equity_at_3y_low":                          {"inputs": ["equity"],                                          "func": eqe_136_equity_at_3y_low},
    "eqe_137_retearn_at_3y_low":                         {"inputs": ["retearn"],                                         "func": eqe_137_retearn_at_3y_low},
    "eqe_138_bvps_at_3y_low":                            {"inputs": ["equity", "sharesbas"],                             "func": eqe_138_bvps_at_3y_low},
    "eqe_139_equity_ols_slope_1y":                       {"inputs": ["equity"],                                          "func": eqe_139_equity_ols_slope_1y},
    "eqe_140_retearn_ols_slope_1y":                      {"inputs": ["retearn"],                                         "func": eqe_140_retearn_ols_slope_1y},
    "eqe_141_equity_ols_slope_2y":                       {"inputs": ["equity"],                                          "func": eqe_141_equity_ols_slope_2y},
    "eqe_142_equity_zscore_12q":                         {"inputs": ["equity"],                                          "func": eqe_142_equity_zscore_12q},
    "eqe_143_retearn_zscore_8q":                         {"inputs": ["retearn"],                                         "func": eqe_143_retearn_zscore_8q},
    "eqe_144_equity_pct_rank_12q":                       {"inputs": ["equity"],                                          "func": eqe_144_equity_pct_rank_12q},
    "eqe_145_retearn_pct_rank_8q":                       {"inputs": ["retearn"],                                         "func": eqe_145_retearn_pct_rank_8q},
    "eqe_146_equity_expanding_pct_rank":                 {"inputs": ["equity"],                                          "func": eqe_146_equity_expanding_pct_rank},
    "eqe_147_retearn_expanding_pct_rank":                {"inputs": ["retearn"],                                         "func": eqe_147_retearn_expanding_pct_rank},
    "eqe_148_equity_median_4q":                          {"inputs": ["equity"],                                          "func": eqe_148_equity_median_4q},
    "eqe_149_equity_vs_median_4q":                       {"inputs": ["equity"],                                          "func": eqe_149_equity_vs_median_4q},
    "eqe_150_equity_erosion_deep_composite":             {"inputs": ["equity", "retearn", "assets", "intangibles"],      "func": eqe_150_equity_erosion_deep_composite},
}
