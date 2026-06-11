"""
74_fundamental_momentum — Base Features 076-150
Domain: QoQ/YoY trend, slope, momentum acceleration, consistency, and cross-metric
        trend persistence for core fundamental metrics
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
_TD_3Q    = 189
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _ols_slope(arr):
    """Scalar OLS slope for use with rolling().apply(raw=True)."""
    n = len(arr)
    if n < 2:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = ((x - xm) ** 2).sum()
    if denom == 0.0:
        return np.nan
    return ((x - xm) * (arr - ym)).sum() / denom


def _rolling_slope(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_ols_slope, raw=True)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): YoY momentum levels and pct changes ---

def fmo_076_revenue_yoy_change(revenue: pd.Series) -> pd.Series:
    """Revenue YoY absolute change (252-day lag)."""
    return revenue - revenue.shift(_TD_YEAR)


def fmo_077_revenue_yoy_pct(revenue: pd.Series) -> pd.Series:
    """Revenue YoY percent change; denominator is abs(prior)."""
    prior = revenue.shift(_TD_YEAR)
    return _safe_div_abs(revenue - prior, prior)


def fmo_078_netinc_yoy_pct(netinc: pd.Series) -> pd.Series:
    """Net income YoY percent change; denominator is abs(prior)."""
    prior = netinc.shift(_TD_YEAR)
    return _safe_div_abs(netinc - prior, prior)


def fmo_079_eps_yoy_pct(eps: pd.Series) -> pd.Series:
    """EPS YoY percent change; denominator is abs(prior)."""
    prior = eps.shift(_TD_YEAR)
    return _safe_div_abs(eps - prior, prior)


def fmo_080_gp_yoy_pct(gp: pd.Series) -> pd.Series:
    """Gross profit YoY percent change; denominator is abs(prior)."""
    prior = gp.shift(_TD_YEAR)
    return _safe_div_abs(gp - prior, prior)


def fmo_081_opinc_yoy_pct(opinc: pd.Series) -> pd.Series:
    """Operating income YoY percent change; denominator is abs(prior)."""
    prior = opinc.shift(_TD_YEAR)
    return _safe_div_abs(opinc - prior, prior)


def fmo_082_ebitda_yoy_pct(ebitda: pd.Series) -> pd.Series:
    """EBITDA YoY percent change; denominator is abs(prior)."""
    prior = ebitda.shift(_TD_YEAR)
    return _safe_div_abs(ebitda - prior, prior)


def fmo_083_fcf_yoy_pct(fcf: pd.Series) -> pd.Series:
    """Free cash flow YoY percent change; denominator is abs(prior)."""
    prior = fcf.shift(_TD_YEAR)
    return _safe_div_abs(fcf - prior, prior)


def fmo_084_ncfo_yoy_pct(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow YoY percent change; denominator is abs(prior)."""
    prior = ncfo.shift(_TD_YEAR)
    return _safe_div_abs(ncfo - prior, prior)


def fmo_085_equity_yoy_pct(equity: pd.Series) -> pd.Series:
    """Equity YoY percent change; denominator is abs(prior)."""
    prior = equity.shift(_TD_YEAR)
    return _safe_div_abs(equity - prior, prior)


def fmo_086_assets_yoy_pct(assets: pd.Series) -> pd.Series:
    """Total assets YoY percent change; denominator is abs(prior)."""
    prior = assets.shift(_TD_YEAR)
    return _safe_div_abs(assets - prior, prior)


def fmo_087_revenue_2y_pct(revenue: pd.Series) -> pd.Series:
    """Revenue 2-year percent change (504-day lag); denominator is abs(prior)."""
    prior = revenue.shift(_TD_2Y)
    return _safe_div_abs(revenue - prior, prior)


def fmo_088_netinc_2y_pct(netinc: pd.Series) -> pd.Series:
    """Net income 2-year percent change; denominator is abs(prior)."""
    prior = netinc.shift(_TD_2Y)
    return _safe_div_abs(netinc - prior, prior)


def fmo_089_eps_2y_pct(eps: pd.Series) -> pd.Series:
    """EPS 2-year percent change; denominator is abs(prior)."""
    prior = eps.shift(_TD_2Y)
    return _safe_div_abs(eps - prior, prior)


def fmo_090_ebitda_2y_pct(ebitda: pd.Series) -> pd.Series:
    """EBITDA 2-year percent change; denominator is abs(prior)."""
    prior = ebitda.shift(_TD_2Y)
    return _safe_div_abs(ebitda - prior, prior)


# --- Group G (091-105): Momentum acceleration (QoQ of QoQ change) ---

def fmo_091_revenue_qoq_acceleration(revenue: pd.Series) -> pd.Series:
    """Second difference of revenue over 63-day steps: QoQ change of QoQ change."""
    d1 = revenue - revenue.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_092_netinc_qoq_acceleration(netinc: pd.Series) -> pd.Series:
    """Second difference of net income: QoQ change of QoQ change."""
    d1 = netinc - netinc.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_093_eps_qoq_acceleration(eps: pd.Series) -> pd.Series:
    """Second difference of EPS: QoQ change of QoQ change."""
    d1 = eps - eps.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_094_gp_qoq_acceleration(gp: pd.Series) -> pd.Series:
    """Second difference of gross profit: QoQ change of QoQ change."""
    d1 = gp - gp.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_095_opinc_qoq_acceleration(opinc: pd.Series) -> pd.Series:
    """Second difference of operating income: QoQ change of QoQ change."""
    d1 = opinc - opinc.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_096_ebitda_qoq_acceleration(ebitda: pd.Series) -> pd.Series:
    """Second difference of EBITDA: QoQ change of QoQ change."""
    d1 = ebitda - ebitda.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_097_fcf_qoq_acceleration(fcf: pd.Series) -> pd.Series:
    """Second difference of FCF: QoQ change of QoQ change."""
    d1 = fcf - fcf.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_098_ncfo_qoq_acceleration(ncfo: pd.Series) -> pd.Series:
    """Second difference of operating cash flow: QoQ change of QoQ change."""
    d1 = ncfo - ncfo.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_099_equity_qoq_acceleration(equity: pd.Series) -> pd.Series:
    """Second difference of equity: QoQ change of QoQ change."""
    d1 = equity - equity.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_100_revenue_yoy_acceleration(revenue: pd.Series) -> pd.Series:
    """YoY acceleration of revenue: QoQ change in the YoY revenue change."""
    d1 = revenue - revenue.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def fmo_101_netinc_yoy_acceleration(netinc: pd.Series) -> pd.Series:
    """YoY acceleration of net income: QoQ change in the YoY net income change."""
    d1 = netinc - netinc.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def fmo_102_eps_yoy_acceleration(eps: pd.Series) -> pd.Series:
    """YoY acceleration of EPS: QoQ change in the YoY EPS change."""
    d1 = eps - eps.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def fmo_103_gp_yoy_acceleration(gp: pd.Series) -> pd.Series:
    """YoY acceleration of gross profit: QoQ change in the YoY GP change."""
    d1 = gp - gp.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def fmo_104_ebitda_yoy_acceleration(ebitda: pd.Series) -> pd.Series:
    """YoY acceleration of EBITDA: QoQ change in the YoY EBITDA change."""
    d1 = ebitda - ebitda.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def fmo_105_fcf_yoy_acceleration(fcf: pd.Series) -> pd.Series:
    """YoY acceleration of FCF: QoQ change in the YoY FCF change."""
    d1 = fcf - fcf.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


# --- Group H (106-120): Trend persistence (fraction of window improving) ---

def fmo_106_revenue_trend_persistence_4q(revenue: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters (252 days) where revenue is above its own
    63-day-prior value — measures directional persistence."""
    improving = (revenue > revenue.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_107_revenue_trend_persistence_8q(revenue: pd.Series) -> pd.Series:
    """Fraction of trailing 8 quarters where revenue shows positive QoQ momentum."""
    improving = (revenue > revenue.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_2Y)


def fmo_108_netinc_trend_persistence_4q(netinc: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where net income shows positive QoQ momentum."""
    improving = (netinc > netinc.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_109_netinc_trend_persistence_8q(netinc: pd.Series) -> pd.Series:
    """Fraction of trailing 8 quarters where net income shows positive QoQ momentum."""
    improving = (netinc > netinc.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_2Y)


def fmo_110_eps_trend_persistence_4q(eps: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where EPS shows positive QoQ momentum."""
    improving = (eps > eps.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_111_gp_trend_persistence_4q(gp: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where gross profit shows positive QoQ momentum."""
    improving = (gp > gp.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_112_opinc_trend_persistence_4q(opinc: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where operating income shows positive QoQ momentum."""
    improving = (opinc > opinc.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_113_ebitda_trend_persistence_4q(ebitda: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where EBITDA shows positive QoQ momentum."""
    improving = (ebitda > ebitda.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_114_fcf_trend_persistence_4q(fcf: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where FCF shows positive QoQ momentum."""
    improving = (fcf > fcf.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_115_ncfo_trend_persistence_4q(ncfo: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where NCFO shows positive QoQ momentum."""
    improving = (ncfo > ncfo.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_116_equity_trend_persistence_4q(equity: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where equity shows positive QoQ momentum."""
    improving = (equity > equity.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_117_assets_trend_persistence_4q(assets: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where total assets show positive QoQ momentum."""
    improving = (assets > assets.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_118_composite_trend_persistence_4q(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Composite trend-persistence score: mean persistence fraction across all 10
    core metrics over trailing 4 quarters.
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    persis = [_rolling_mean((m > m.shift(_TD_QTR)).astype(float), _TD_YEAR) for m in metrics]
    total = persis[0].copy()
    for p in persis[1:]:
        total = total + p
    return total / 10.0


def fmo_119_revenue_momentum_consistency_sign_change(revenue: pd.Series) -> pd.Series:
    """
    Fraction of 4-quarter window where revenue QoQ sign flipped vs prior quarter.
    Low values = consistent momentum; high = erratic.
    """
    d1 = revenue - revenue.shift(_TD_QTR)
    flip = (d1 * d1.shift(_TD_QTR) < 0).astype(float)
    return _rolling_mean(flip, _TD_YEAR)


def fmo_120_netinc_momentum_consistency_sign_change(netinc: pd.Series) -> pd.Series:
    """
    Fraction of 4-quarter window where net income QoQ sign flipped vs prior quarter.
    """
    d1 = netinc - netinc.shift(_TD_QTR)
    flip = (d1 * d1.shift(_TD_QTR) < 0).astype(float)
    return _rolling_mean(flip, _TD_YEAR)


# --- Group I (121-135): Cross-metric ratio momentum ---

def fmo_121_gp_margin_qoq_change(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in gross margin (gp/revenue); measures margin momentum."""
    margin = _safe_div(gp, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def fmo_122_opinc_margin_qoq_change(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in operating margin (opinc/revenue)."""
    margin = _safe_div(opinc, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def fmo_123_netinc_margin_qoq_change(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in net income margin (netinc/revenue)."""
    margin = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def fmo_124_ebitda_margin_qoq_change(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in EBITDA margin (ebitda/revenue)."""
    margin = _safe_div(ebitda, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def fmo_125_fcf_margin_qoq_change(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in FCF margin (fcf/revenue)."""
    margin = _safe_div(fcf, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def fmo_126_gp_margin_yoy_change(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in gross margin."""
    margin = _safe_div(gp, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_YEAR)


def fmo_127_opinc_margin_yoy_change(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in operating margin."""
    margin = _safe_div(opinc, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_YEAR)


def fmo_128_netinc_margin_yoy_change(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in net income margin."""
    margin = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_YEAR)


def fmo_129_ebitda_margin_4q_slope(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """4-quarter OLS slope of EBITDA margin (ebitda/revenue)."""
    margin = _safe_div(ebitda, revenue.abs().replace(0, np.nan))
    return _rolling_slope(margin, _TD_YEAR)


def fmo_130_netinc_to_equity_qoq_change(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in return on equity proxy (netinc/equity)."""
    roe = _safe_div(netinc, equity.abs().replace(0, np.nan))
    return roe - roe.shift(_TD_QTR)


def fmo_131_netinc_to_assets_qoq_change(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in return on assets proxy (netinc/assets)."""
    roa = _safe_div(netinc, assets.abs().replace(0, np.nan))
    return roa - roa.shift(_TD_QTR)


def fmo_132_fcf_to_assets_qoq_change(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in FCF-to-assets ratio."""
    ratio = _safe_div(fcf, assets.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def fmo_133_ncfo_to_revenue_qoq_change(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in operating cash flow margin (ncfo/revenue)."""
    margin = _safe_div(ncfo, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def fmo_134_opinc_to_gp_ratio_qoq_change(opinc: pd.Series, gp: pd.Series) -> pd.Series:
    """QoQ change in operating leverage ratio (opinc/gp); measures cost-structure trend."""
    ratio = _safe_div(opinc, gp.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def fmo_135_ebitda_to_equity_qoq_change(ebitda: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in EBITDA-to-equity ratio."""
    ratio = _safe_div(ebitda, equity.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


# --- Group J (136-150): Z-scores, expanding z-scores, and composite summaries ---

def fmo_136_revenue_zscore_4q(revenue: pd.Series) -> pd.Series:
    """Z-score of revenue within trailing 4-quarter (252-day) window."""
    return _zscore_rolling(revenue, _TD_YEAR)


def fmo_137_revenue_zscore_8q(revenue: pd.Series) -> pd.Series:
    """Z-score of revenue within trailing 8-quarter (504-day) window."""
    return _zscore_rolling(revenue, _TD_2Y)


def fmo_138_netinc_zscore_4q(netinc: pd.Series) -> pd.Series:
    """Z-score of net income within trailing 4-quarter window."""
    return _zscore_rolling(netinc, _TD_YEAR)


def fmo_139_eps_zscore_4q(eps: pd.Series) -> pd.Series:
    """Z-score of EPS within trailing 4-quarter window."""
    return _zscore_rolling(eps, _TD_YEAR)


def fmo_140_ebitda_zscore_4q(ebitda: pd.Series) -> pd.Series:
    """Z-score of EBITDA within trailing 4-quarter window."""
    return _zscore_rolling(ebitda, _TD_YEAR)


def fmo_141_fcf_zscore_4q(fcf: pd.Series) -> pd.Series:
    """Z-score of FCF within trailing 4-quarter window."""
    return _zscore_rolling(fcf, _TD_YEAR)


def fmo_142_ncfo_zscore_4q(ncfo: pd.Series) -> pd.Series:
    """Z-score of operating cash flow within trailing 4-quarter window."""
    return _zscore_rolling(ncfo, _TD_YEAR)


def fmo_143_equity_zscore_4q(equity: pd.Series) -> pd.Series:
    """Z-score of equity within trailing 4-quarter window."""
    return _zscore_rolling(equity, _TD_YEAR)


def fmo_144_revenue_expanding_zscore(revenue: pd.Series) -> pd.Series:
    """Expanding z-score of revenue (how extreme vs entire history)."""
    m  = revenue.expanding(min_periods=2).mean()
    sd = revenue.expanding(min_periods=2).std()
    return _safe_div(revenue - m, sd)


def fmo_145_netinc_expanding_zscore(netinc: pd.Series) -> pd.Series:
    """Expanding z-score of net income."""
    m  = netinc.expanding(min_periods=2).mean()
    sd = netinc.expanding(min_periods=2).std()
    return _safe_div(netinc - m, sd)


def fmo_146_eps_expanding_zscore(eps: pd.Series) -> pd.Series:
    """Expanding z-score of EPS."""
    m  = eps.expanding(min_periods=2).mean()
    sd = eps.expanding(min_periods=2).std()
    return _safe_div(eps - m, sd)


def fmo_147_composite_zscore_income_metrics(
    netinc: pd.Series, eps: pd.Series, gp: pd.Series,
    opinc: pd.Series, ebitda: pd.Series
) -> pd.Series:
    """
    Equally weighted mean of 4-quarter z-scores for the 5 income-statement
    metrics: net income, EPS, gross profit, operating income, EBITDA.
    """
    metrics = [netinc, eps, gp, opinc, ebitda]
    zs = [_zscore_rolling(m, _TD_YEAR) for m in metrics]
    total = zs[0].copy()
    for z in zs[1:]:
        total = total + z
    return total / 5.0


def fmo_148_composite_zscore_cashflow_metrics(
    fcf: pd.Series, ncfo: pd.Series
) -> pd.Series:
    """
    Equally weighted mean of 4-quarter z-scores for cash flow metrics: FCF, NCFO.
    """
    z_fcf  = _zscore_rolling(fcf, _TD_YEAR)
    z_ncfo = _zscore_rolling(ncfo, _TD_YEAR)
    return (z_fcf + z_ncfo) / 2.0


def fmo_149_composite_momentum_score_full(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Full composite momentum score combining:
    1) Mean 4-quarter z-score across 10 metrics (normalized)
    2) Net-improving QoQ count normalized to [-1, +1]
    Equal-weighted average of (1) and (2).
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    z_mean = sum(_zscore_rolling(m, _TD_YEAR) for m in metrics) / 10.0
    net_improving = sum(np.sign(m - m.shift(_TD_QTR)) for m in metrics) / 10.0
    return (z_mean + net_improving.astype(float)) / 2.0


def fmo_150_breadth_net_improving_4q_rolling_mean(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Rolling 4-quarter mean of the net-improving count (YoY basis).
    Measures sustained positive breadth over the trailing year.
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    net = sum(np.sign(m - m.shift(_TD_YEAR)) for m in metrics).astype(float)
    return _rolling_mean(net, _TD_YEAR)


# ── Registry 076-150 ──────────────────────────────────────────────────────────

FUNDAMENTAL_MOMENTUM_REGISTRY_076_150 = {
    "fmo_076_revenue_yoy_change":                    {"inputs": ["revenue"],                                                                                            "func": fmo_076_revenue_yoy_change},
    "fmo_077_revenue_yoy_pct":                       {"inputs": ["revenue"],                                                                                            "func": fmo_077_revenue_yoy_pct},
    "fmo_078_netinc_yoy_pct":                        {"inputs": ["netinc"],                                                                                             "func": fmo_078_netinc_yoy_pct},
    "fmo_079_eps_yoy_pct":                           {"inputs": ["eps"],                                                                                                "func": fmo_079_eps_yoy_pct},
    "fmo_080_gp_yoy_pct":                            {"inputs": ["gp"],                                                                                                 "func": fmo_080_gp_yoy_pct},
    "fmo_081_opinc_yoy_pct":                         {"inputs": ["opinc"],                                                                                              "func": fmo_081_opinc_yoy_pct},
    "fmo_082_ebitda_yoy_pct":                        {"inputs": ["ebitda"],                                                                                             "func": fmo_082_ebitda_yoy_pct},
    "fmo_083_fcf_yoy_pct":                           {"inputs": ["fcf"],                                                                                                "func": fmo_083_fcf_yoy_pct},
    "fmo_084_ncfo_yoy_pct":                          {"inputs": ["ncfo"],                                                                                               "func": fmo_084_ncfo_yoy_pct},
    "fmo_085_equity_yoy_pct":                        {"inputs": ["equity"],                                                                                             "func": fmo_085_equity_yoy_pct},
    "fmo_086_assets_yoy_pct":                        {"inputs": ["assets"],                                                                                             "func": fmo_086_assets_yoy_pct},
    "fmo_087_revenue_2y_pct":                        {"inputs": ["revenue"],                                                                                            "func": fmo_087_revenue_2y_pct},
    "fmo_088_netinc_2y_pct":                         {"inputs": ["netinc"],                                                                                             "func": fmo_088_netinc_2y_pct},
    "fmo_089_eps_2y_pct":                            {"inputs": ["eps"],                                                                                                "func": fmo_089_eps_2y_pct},
    "fmo_090_ebitda_2y_pct":                         {"inputs": ["ebitda"],                                                                                             "func": fmo_090_ebitda_2y_pct},
    "fmo_091_revenue_qoq_acceleration":              {"inputs": ["revenue"],                                                                                            "func": fmo_091_revenue_qoq_acceleration},
    "fmo_092_netinc_qoq_acceleration":               {"inputs": ["netinc"],                                                                                             "func": fmo_092_netinc_qoq_acceleration},
    "fmo_093_eps_qoq_acceleration":                  {"inputs": ["eps"],                                                                                                "func": fmo_093_eps_qoq_acceleration},
    "fmo_094_gp_qoq_acceleration":                   {"inputs": ["gp"],                                                                                                 "func": fmo_094_gp_qoq_acceleration},
    "fmo_095_opinc_qoq_acceleration":                {"inputs": ["opinc"],                                                                                              "func": fmo_095_opinc_qoq_acceleration},
    "fmo_096_ebitda_qoq_acceleration":               {"inputs": ["ebitda"],                                                                                             "func": fmo_096_ebitda_qoq_acceleration},
    "fmo_097_fcf_qoq_acceleration":                  {"inputs": ["fcf"],                                                                                                "func": fmo_097_fcf_qoq_acceleration},
    "fmo_098_ncfo_qoq_acceleration":                 {"inputs": ["ncfo"],                                                                                               "func": fmo_098_ncfo_qoq_acceleration},
    "fmo_099_equity_qoq_acceleration":               {"inputs": ["equity"],                                                                                             "func": fmo_099_equity_qoq_acceleration},
    "fmo_100_revenue_yoy_acceleration":              {"inputs": ["revenue"],                                                                                            "func": fmo_100_revenue_yoy_acceleration},
    "fmo_101_netinc_yoy_acceleration":               {"inputs": ["netinc"],                                                                                             "func": fmo_101_netinc_yoy_acceleration},
    "fmo_102_eps_yoy_acceleration":                  {"inputs": ["eps"],                                                                                                "func": fmo_102_eps_yoy_acceleration},
    "fmo_103_gp_yoy_acceleration":                   {"inputs": ["gp"],                                                                                                 "func": fmo_103_gp_yoy_acceleration},
    "fmo_104_ebitda_yoy_acceleration":               {"inputs": ["ebitda"],                                                                                             "func": fmo_104_ebitda_yoy_acceleration},
    "fmo_105_fcf_yoy_acceleration":                  {"inputs": ["fcf"],                                                                                                "func": fmo_105_fcf_yoy_acceleration},
    "fmo_106_revenue_trend_persistence_4q":          {"inputs": ["revenue"],                                                                                            "func": fmo_106_revenue_trend_persistence_4q},
    "fmo_107_revenue_trend_persistence_8q":          {"inputs": ["revenue"],                                                                                            "func": fmo_107_revenue_trend_persistence_8q},
    "fmo_108_netinc_trend_persistence_4q":           {"inputs": ["netinc"],                                                                                             "func": fmo_108_netinc_trend_persistence_4q},
    "fmo_109_netinc_trend_persistence_8q":           {"inputs": ["netinc"],                                                                                             "func": fmo_109_netinc_trend_persistence_8q},
    "fmo_110_eps_trend_persistence_4q":              {"inputs": ["eps"],                                                                                                "func": fmo_110_eps_trend_persistence_4q},
    "fmo_111_gp_trend_persistence_4q":               {"inputs": ["gp"],                                                                                                 "func": fmo_111_gp_trend_persistence_4q},
    "fmo_112_opinc_trend_persistence_4q":            {"inputs": ["opinc"],                                                                                              "func": fmo_112_opinc_trend_persistence_4q},
    "fmo_113_ebitda_trend_persistence_4q":           {"inputs": ["ebitda"],                                                                                             "func": fmo_113_ebitda_trend_persistence_4q},
    "fmo_114_fcf_trend_persistence_4q":              {"inputs": ["fcf"],                                                                                                "func": fmo_114_fcf_trend_persistence_4q},
    "fmo_115_ncfo_trend_persistence_4q":             {"inputs": ["ncfo"],                                                                                               "func": fmo_115_ncfo_trend_persistence_4q},
    "fmo_116_equity_trend_persistence_4q":           {"inputs": ["equity"],                                                                                             "func": fmo_116_equity_trend_persistence_4q},
    "fmo_117_assets_trend_persistence_4q":           {"inputs": ["assets"],                                                                                             "func": fmo_117_assets_trend_persistence_4q},
    "fmo_118_composite_trend_persistence_4q":        {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],              "func": fmo_118_composite_trend_persistence_4q},
    "fmo_119_revenue_momentum_consistency_sign_change": {"inputs": ["revenue"],                                                                                         "func": fmo_119_revenue_momentum_consistency_sign_change},
    "fmo_120_netinc_momentum_consistency_sign_change":  {"inputs": ["netinc"],                                                                                          "func": fmo_120_netinc_momentum_consistency_sign_change},
    "fmo_121_gp_margin_qoq_change":                  {"inputs": ["gp", "revenue"],                                                                                      "func": fmo_121_gp_margin_qoq_change},
    "fmo_122_opinc_margin_qoq_change":               {"inputs": ["opinc", "revenue"],                                                                                    "func": fmo_122_opinc_margin_qoq_change},
    "fmo_123_netinc_margin_qoq_change":              {"inputs": ["netinc", "revenue"],                                                                                   "func": fmo_123_netinc_margin_qoq_change},
    "fmo_124_ebitda_margin_qoq_change":              {"inputs": ["ebitda", "revenue"],                                                                                   "func": fmo_124_ebitda_margin_qoq_change},
    "fmo_125_fcf_margin_qoq_change":                 {"inputs": ["fcf", "revenue"],                                                                                      "func": fmo_125_fcf_margin_qoq_change},
    "fmo_126_gp_margin_yoy_change":                  {"inputs": ["gp", "revenue"],                                                                                      "func": fmo_126_gp_margin_yoy_change},
    "fmo_127_opinc_margin_yoy_change":               {"inputs": ["opinc", "revenue"],                                                                                    "func": fmo_127_opinc_margin_yoy_change},
    "fmo_128_netinc_margin_yoy_change":              {"inputs": ["netinc", "revenue"],                                                                                   "func": fmo_128_netinc_margin_yoy_change},
    "fmo_129_ebitda_margin_4q_slope":                {"inputs": ["ebitda", "revenue"],                                                                                   "func": fmo_129_ebitda_margin_4q_slope},
    "fmo_130_netinc_to_equity_qoq_change":           {"inputs": ["netinc", "equity"],                                                                                    "func": fmo_130_netinc_to_equity_qoq_change},
    "fmo_131_netinc_to_assets_qoq_change":           {"inputs": ["netinc", "assets"],                                                                                    "func": fmo_131_netinc_to_assets_qoq_change},
    "fmo_132_fcf_to_assets_qoq_change":              {"inputs": ["fcf", "assets"],                                                                                       "func": fmo_132_fcf_to_assets_qoq_change},
    "fmo_133_ncfo_to_revenue_qoq_change":            {"inputs": ["ncfo", "revenue"],                                                                                     "func": fmo_133_ncfo_to_revenue_qoq_change},
    "fmo_134_opinc_to_gp_ratio_qoq_change":          {"inputs": ["opinc", "gp"],                                                                                         "func": fmo_134_opinc_to_gp_ratio_qoq_change},
    "fmo_135_ebitda_to_equity_qoq_change":           {"inputs": ["ebitda", "equity"],                                                                                    "func": fmo_135_ebitda_to_equity_qoq_change},
    "fmo_136_revenue_zscore_4q":                     {"inputs": ["revenue"],                                                                                             "func": fmo_136_revenue_zscore_4q},
    "fmo_137_revenue_zscore_8q":                     {"inputs": ["revenue"],                                                                                             "func": fmo_137_revenue_zscore_8q},
    "fmo_138_netinc_zscore_4q":                      {"inputs": ["netinc"],                                                                                              "func": fmo_138_netinc_zscore_4q},
    "fmo_139_eps_zscore_4q":                         {"inputs": ["eps"],                                                                                                 "func": fmo_139_eps_zscore_4q},
    "fmo_140_ebitda_zscore_4q":                      {"inputs": ["ebitda"],                                                                                              "func": fmo_140_ebitda_zscore_4q},
    "fmo_141_fcf_zscore_4q":                         {"inputs": ["fcf"],                                                                                                 "func": fmo_141_fcf_zscore_4q},
    "fmo_142_ncfo_zscore_4q":                        {"inputs": ["ncfo"],                                                                                                "func": fmo_142_ncfo_zscore_4q},
    "fmo_143_equity_zscore_4q":                      {"inputs": ["equity"],                                                                                              "func": fmo_143_equity_zscore_4q},
    "fmo_144_revenue_expanding_zscore":              {"inputs": ["revenue"],                                                                                             "func": fmo_144_revenue_expanding_zscore},
    "fmo_145_netinc_expanding_zscore":               {"inputs": ["netinc"],                                                                                              "func": fmo_145_netinc_expanding_zscore},
    "fmo_146_eps_expanding_zscore":                  {"inputs": ["eps"],                                                                                                 "func": fmo_146_eps_expanding_zscore},
    "fmo_147_composite_zscore_income_metrics":       {"inputs": ["netinc", "eps", "gp", "opinc", "ebitda"],                                                              "func": fmo_147_composite_zscore_income_metrics},
    "fmo_148_composite_zscore_cashflow_metrics":     {"inputs": ["fcf", "ncfo"],                                                                                         "func": fmo_148_composite_zscore_cashflow_metrics},
    "fmo_149_composite_momentum_score_full":         {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],              "func": fmo_149_composite_momentum_score_full},
    "fmo_150_breadth_net_improving_4q_rolling_mean": {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],              "func": fmo_150_breadth_net_improving_4q_rolling_mean},
}
