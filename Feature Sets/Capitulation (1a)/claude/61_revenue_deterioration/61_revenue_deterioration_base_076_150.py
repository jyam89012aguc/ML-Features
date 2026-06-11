"""
61_revenue_deterioration — Base Features 076-150
Domain: revenue contraction, growth reversal, top-line deterioration (continued)
Asset class: US equities | Sharadar SF1 fundamentals ONLY (no price/volume)
Target context: capitulation — absolute multi-year low / maximum distress

All inputs are daily-frequency Series, forward-filled from the most recent
quarterly Sharadar SF1 report known as of each date (pipeline contract).
Functions look strictly backward — no future information.

Quarterly cadence on daily index:
    1 quarter  ~  63 trading days   (.diff(63)  = QoQ)
    1 year     ~ 252 trading days   (.diff(252) = YoY)
    2 years    ~ 504 trading days
    3 years    ~ 756 trading days
    5 years    ~ 1260 trading days
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2YEAR = 504
_TD_3YEAR = 756
_TD_5YEAR = 1260
_TD_QTR   = 63
_TD_HALF  = 126
_EPS      = 1e-9

# ── Alignment helper ──────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Re-index a quarterly SF1 Series onto a daily trading-day index and
    forward-fill gaps.  Contract: all feature-function inputs in this file
    have already been aligned this way by the upstream pipeline; this helper
    is provided for documentation and optional manual use only.
    """
    return q_series.reindex(daily_index).ffill()

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/NaN denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(x):
        n = len(x)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        denom = ((xi - xi_m) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((xi - xi_m) * (x - x_m)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=True)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-090): Revenue vs cost-structure divergence ---

def rvd_076_cor_yoy_pct(cor: pd.Series) -> pd.Series:
    """YoY % change in cost of revenue (COGS growth vs revenue decline)."""
    prior = cor.shift(_TD_YEAR)
    return _safe_div(cor - prior, prior.abs())


def rvd_077_cor_qoq_pct(cor: pd.Series) -> pd.Series:
    """QoQ % change in cost of revenue."""
    prior = cor.shift(_TD_QTR)
    return _safe_div(cor - prior, prior.abs())


def rvd_078_rev_cor_spread_qoq(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """QoQ diff: (revenue growth - COR growth); negative = cost outpacing revenue."""
    rev_g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    cor_g = _safe_div(cor - cor.shift(_TD_QTR), cor.shift(_TD_QTR).abs())
    return rev_g - cor_g


def rvd_079_rev_cor_spread_yoy(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """YoY diff: (revenue growth - COR growth); negative = cost squeeze."""
    rev_g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    cor_g = _safe_div(cor - cor.shift(_TD_YEAR), cor.shift(_TD_YEAR).abs())
    return rev_g - cor_g


def rvd_080_rev_declining_cor_flat_flag(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Flag: revenue falling QoQ while COGS is not declining (margin squeeze signal)."""
    rev_chg = revenue - revenue.shift(_TD_QTR)
    cor_chg = cor - cor.shift(_TD_QTR)
    return ((rev_chg < 0) & (cor_chg >= 0)).astype(float)


def rvd_081_gp_yoy_pct(gp: pd.Series) -> pd.Series:
    """YoY % change in gross profit."""
    prior = gp.shift(_TD_YEAR)
    return _safe_div(gp - prior, prior.abs())


def rvd_082_gp_qoq_pct(gp: pd.Series) -> pd.Series:
    """QoQ % change in gross profit."""
    prior = gp.shift(_TD_QTR)
    return _safe_div(gp - prior, prior.abs())


def rvd_083_gp_rev_growth_divergence_qoq(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """QoQ GP growth minus revenue growth: negative = margins compressing faster."""
    gp_g  = _safe_div(gp  - gp.shift(_TD_QTR),  gp.shift(_TD_QTR).abs())
    rev_g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return gp_g - rev_g


def rvd_084_gp_rev_growth_divergence_yoy(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """YoY GP growth minus revenue growth."""
    gp_g  = _safe_div(gp  - gp.shift(_TD_YEAR),  gp.shift(_TD_YEAR).abs())
    rev_g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return gp_g - rev_g


def rvd_085_gp_vs_4q_avg(gp: pd.Series) -> pd.Series:
    """Gross profit deviation from 4-quarter trailing average."""
    avg = _rolling_mean(gp, _TD_YEAR)
    return _safe_div(gp - avg, avg.abs())


def rvd_086_gp_dd_from_4q_peak(gp: pd.Series) -> pd.Series:
    """GP drawdown from 4-quarter (1-year) trailing peak."""
    peak = _rolling_max(gp, _TD_YEAR)
    return _safe_div(gp - peak, peak.abs())


def rvd_087_gp_dd_from_ath(gp: pd.Series) -> pd.Series:
    """Gross profit drawdown from all-time expanding peak."""
    peak = gp.expanding(min_periods=1).max()
    return _safe_div(gp - peak, peak.abs())


def rvd_088_gp_new_4q_low_flag(gp: pd.Series) -> pd.Series:
    """Flag: 1 if gross profit is at a 4-quarter (1-year) low."""
    mn = _rolling_min(gp, _TD_YEAR)
    return (gp <= mn).astype(float)


def rvd_089_gp_zscore_4q(gp: pd.Series) -> pd.Series:
    """Z-score of gross profit within trailing 4-quarter (1-year) window."""
    return _zscore_rolling(gp, _TD_YEAR)


def rvd_090_cor_to_rev_rising_trend(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """OLS slope of COGS/revenue ratio over trailing 4 quarters (rising = worsening)."""
    ratio = _safe_div(cor, revenue)
    return _linslope(ratio, _TD_YEAR)


# --- Group H (091-105): Receivables and inventory demand signals ---

def rvd_091_receivables_yoy_pct(receivables: pd.Series) -> pd.Series:
    """YoY % change in receivables (rising while revenue falls = collection risk)."""
    prior = receivables.shift(_TD_YEAR)
    return _safe_div(receivables - prior, prior.abs())


def rvd_092_receivables_qoq_pct(receivables: pd.Series) -> pd.Series:
    """QoQ % change in receivables."""
    prior = receivables.shift(_TD_QTR)
    return _safe_div(receivables - prior, prior.abs())


def rvd_093_inventory_yoy_pct(inventory: pd.Series) -> pd.Series:
    """YoY % change in inventory (rising while revenue falls = demand weakness)."""
    prior = inventory.shift(_TD_YEAR)
    return _safe_div(inventory - prior, prior.abs())


def rvd_094_inventory_qoq_pct(inventory: pd.Series) -> pd.Series:
    """QoQ % change in inventory."""
    prior = inventory.shift(_TD_QTR)
    return _safe_div(inventory - prior, prior.abs())


def rvd_095_receivables_growth_vs_rev_growth_qoq(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """QoQ receivables growth minus revenue growth: positive = demand-quality warning."""
    rec_g = _safe_div(receivables - receivables.shift(_TD_QTR), receivables.shift(_TD_QTR).abs())
    rev_g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return rec_g - rev_g


def rvd_096_receivables_growth_vs_rev_growth_yoy(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """YoY receivables growth minus revenue growth."""
    rec_g = _safe_div(receivables - receivables.shift(_TD_YEAR), receivables.shift(_TD_YEAR).abs())
    rev_g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return rec_g - rev_g


def rvd_097_inventory_growth_vs_rev_growth_qoq(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """QoQ inventory growth minus revenue growth: positive = demand weakness warning."""
    inv_g = _safe_div(inventory - inventory.shift(_TD_QTR), inventory.shift(_TD_QTR).abs())
    rev_g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return inv_g - rev_g


def rvd_098_inventory_growth_vs_rev_growth_yoy(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """YoY inventory growth minus revenue growth."""
    inv_g = _safe_div(inventory - inventory.shift(_TD_YEAR), inventory.shift(_TD_YEAR).abs())
    rev_g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return inv_g - rev_g


def rvd_099_receivables_plus_inventory_to_rev(revenue: pd.Series, receivables: pd.Series, inventory: pd.Series) -> pd.Series:
    """(Receivables + Inventory) / Revenue: combined demand-weakness ratio."""
    return _safe_div(receivables + inventory, revenue)


def rvd_100_rec_inv_to_rev_qoq_chg(revenue: pd.Series, receivables: pd.Series, inventory: pd.Series) -> pd.Series:
    """QoQ change in (receivables + inventory) / revenue."""
    ratio = _safe_div(receivables + inventory, revenue)
    return ratio - ratio.shift(_TD_QTR)


def rvd_101_rec_inv_to_rev_yoy_chg(revenue: pd.Series, receivables: pd.Series, inventory: pd.Series) -> pd.Series:
    """YoY change in (receivables + inventory) / revenue."""
    ratio = _safe_div(receivables + inventory, revenue)
    return ratio - ratio.shift(_TD_YEAR)


def rvd_102_receivables_to_rev_4q_avg(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """4-quarter trailing average of receivables/revenue ratio."""
    ratio = _safe_div(receivables, revenue)
    return _rolling_mean(ratio, _TD_YEAR)


def rvd_103_inventory_to_rev_4q_avg(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """4-quarter trailing average of inventory/revenue ratio."""
    ratio = _safe_div(inventory, revenue)
    return _rolling_mean(ratio, _TD_YEAR)


def rvd_104_receivables_to_rev_zscore_4q(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """Z-score of receivables/revenue within trailing 4-quarter window."""
    ratio = _safe_div(receivables, revenue)
    return _zscore_rolling(ratio, _TD_YEAR)


def rvd_105_inventory_to_rev_zscore_4q(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Z-score of inventory/revenue within trailing 4-quarter window."""
    ratio = _safe_div(inventory, revenue)
    return _zscore_rolling(ratio, _TD_YEAR)


# --- Group I (106-118): Deferred revenue, assets, and per-share signals ---

def rvd_106_deferredrev_yoy_pct(deferredrev: pd.Series) -> pd.Series:
    """YoY % change in deferred revenue (backlog growth/decay)."""
    prior = deferredrev.shift(_TD_YEAR)
    return _safe_div(deferredrev - prior, prior.abs())


def rvd_107_deferredrev_qoq_pct(deferredrev: pd.Series) -> pd.Series:
    """QoQ % change in deferred revenue."""
    prior = deferredrev.shift(_TD_QTR)
    return _safe_div(deferredrev - prior, prior.abs())


def rvd_108_deferredrev_to_rev_zscore_4q(revenue: pd.Series, deferredrev: pd.Series) -> pd.Series:
    """Z-score of deferred-revenue/revenue ratio within trailing 4-quarter window."""
    ratio = _safe_div(deferredrev, revenue)
    return _zscore_rolling(ratio, _TD_YEAR)


def rvd_109_deferredrev_growth_vs_rev_growth_qoq(revenue: pd.Series, deferredrev: pd.Series) -> pd.Series:
    """QoQ deferred-rev growth minus revenue growth: negative = backlog not supporting revenue."""
    dr_g  = _safe_div(deferredrev - deferredrev.shift(_TD_QTR), deferredrev.shift(_TD_QTR).abs())
    rev_g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return dr_g - rev_g


def rvd_110_rev_to_assets_ratio(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Revenue/assets (asset turnover): declining ratio signals deteriorating efficiency."""
    return _safe_div(revenue, assets)


def rvd_111_rev_to_assets_pct_rank_8q(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of revenue/assets (asset turnover) within trailing 8-quarter window.
    Low rank signals unusually weak asset utilization — revenue shrinking relative to asset base."""
    ratio = _safe_div(revenue, assets)
    return ratio.rolling(_TD_2YEAR, min_periods=max(2, _TD_2YEAR // 4)).rank(pct=True)


def rvd_112_rev_to_assets_yoy_chg(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in asset turnover (revenue/assets)."""
    ratio = _safe_div(revenue, assets)
    return ratio - ratio.shift(_TD_YEAR)


def rvd_113_rev_to_assets_zscore_4q(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of revenue/assets within trailing 4-quarter window."""
    ratio = _safe_div(revenue, assets)
    return _zscore_rolling(ratio, _TD_YEAR)


def rvd_114_rev_per_share_level(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Revenue per diluted share (absolute level)."""
    return _safe_div(revenue, shareswa)


def rvd_115_rev_per_share_dd_from_4q_peak(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Revenue per share drawdown from 4-quarter (1-year) trailing peak."""
    rps  = _safe_div(revenue, shareswa)
    peak = _rolling_max(rps, _TD_YEAR)
    return _safe_div(rps - peak, peak.abs())


def rvd_116_rev_per_share_dd_from_ath(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Revenue per share drawdown from all-time expanding peak."""
    rps  = _safe_div(revenue, shareswa)
    peak = rps.expanding(min_periods=1).max()
    return _safe_div(rps - peak, peak.abs())


def rvd_117_rev_per_share_zscore_4q(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Z-score of revenue per share within trailing 4-quarter window."""
    rps = _safe_div(revenue, shareswa)
    return _zscore_rolling(rps, _TD_YEAR)


def rvd_118_shareswa_yoy_pct(shareswa: pd.Series) -> pd.Series:
    """YoY % change in diluted shares (dilution context for per-share revenue)."""
    prior = shareswa.shift(_TD_YEAR)
    return _safe_div(shareswa - prior, prior.abs())


# --- Group J (119-135): Multi-period revenue trend and regime signals ---

def rvd_119_rev_4q_cagr(revenue: pd.Series) -> pd.Series:
    """4-quarter (1-year) compounded annual growth rate of revenue."""
    prior = revenue.shift(_TD_YEAR)
    ratio = _safe_div(revenue, prior.abs())
    return ratio - 1.0


def rvd_120_rev_8q_cagr(revenue: pd.Series) -> pd.Series:
    """8-quarter (2-year) CAGR of revenue: (rev/rev_2y)^0.5 - 1."""
    prior = revenue.shift(_TD_2YEAR)
    ratio = _safe_div(revenue, prior.abs()).clip(lower=_EPS)
    return np.power(ratio, 0.5) - 1.0


def rvd_121_rev_20q_cagr(revenue: pd.Series) -> pd.Series:
    """20-quarter (5-year) CAGR of revenue: (rev/rev_5y)^0.2 - 1."""
    prior = revenue.shift(_TD_5YEAR)
    ratio = _safe_div(revenue, prior.abs()).clip(lower=_EPS)
    return np.power(ratio, 0.2) - 1.0


def rvd_122_rev_growth_regime_flag(revenue: pd.Series) -> pd.Series:
    """Growth regime: +1 if YoY > 0, -1 if YoY < 0, 0 otherwise."""
    yoy = revenue - revenue.shift(_TD_YEAR)
    return np.sign(yoy).astype(float)


def rvd_123_rev_growth_decel_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if current YoY growth rate < prior-year YoY growth rate (deceleration)."""
    g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    g_prior = g.shift(_TD_YEAR)
    return (g < g_prior).astype(float)


def rvd_124_rev_below_2q_and_4q_avg_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if revenue is below both 2-quarter and 4-quarter trailing averages."""
    avg2 = _rolling_mean(revenue, _TD_HALF)
    avg4 = _rolling_mean(revenue, _TD_YEAR)
    return ((revenue < avg2) & (revenue < avg4)).astype(float)


def rvd_125_rev_3q_consecutive_yoy_decline_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if YoY revenue is negative for current and 2 prior quarters (3 in a row)."""
    yoy = (revenue - revenue.shift(_TD_YEAR)).fillna(0.0)
    flag = (yoy < 0).astype(float)
    return ((flag + flag.shift(_TD_QTR) + flag.shift(2 * _TD_QTR)) >= 3.0).astype(float)


def rvd_126_rev_4q_consecutive_yoy_decline_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if YoY revenue negative for 4 consecutive quarters (full-year decline)."""
    yoy = (revenue - revenue.shift(_TD_YEAR)).fillna(0.0)
    flag = (yoy < 0).astype(float)
    s = (flag + flag.shift(_TD_QTR) + flag.shift(2 * _TD_QTR) + flag.shift(3 * _TD_QTR))
    return (s >= 4.0).astype(float)


def rvd_127_rev_reversal_from_growth_to_decline(revenue: pd.Series) -> pd.Series:
    """
    Reversal signal: 1 if current YoY < 0 but prior-year YoY >= 0 (first decline
    after growth); captures the exact moment of top-line inflection.
    """
    yoy       = revenue - revenue.shift(_TD_YEAR)
    yoy_prior = yoy.shift(_TD_YEAR)
    return ((yoy < 0) & (yoy_prior >= 0)).astype(float)


def rvd_128_rev_qoq_pct_4q_rolling_min(revenue: pd.Series) -> pd.Series:
    """Trailing 4-quarter minimum of QoQ revenue % change (worst recent quarter)."""
    g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return _rolling_min(g, _TD_YEAR)


def rvd_129_rev_qoq_pct_4q_range(revenue: pd.Series) -> pd.Series:
    """Range (max - min) of QoQ % change over trailing 4 quarters (growth volatility)."""
    g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return _rolling_max(g, _TD_YEAR) - _rolling_min(g, _TD_YEAR)


def rvd_130_rev_level_new_8q_low_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if revenue is at an 8-quarter (2-year) trailing minimum."""
    mn = _rolling_min(revenue, _TD_2YEAR)
    return (revenue <= mn).astype(float)


def rvd_131_rev_expanding_pct_rank(revenue: pd.Series) -> pd.Series:
    """Expanding percentile rank of revenue (position vs all history)."""
    return revenue.expanding(min_periods=2).rank(pct=True)


def rvd_132_rev_4q_pct_above_trend(revenue: pd.Series) -> pd.Series:
    """Revenue deviation (%) from its 4-quarter OLS linear trend."""
    trend = _ewm_mean(revenue, _TD_YEAR)
    return _safe_div(revenue - trend, trend.abs())


def rvd_133_rev_yoy_pct_4q_avg(revenue: pd.Series) -> pd.Series:
    """4-quarter rolling average of YoY revenue growth rate."""
    g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return _rolling_mean(g, _TD_YEAR)


def rvd_134_rev_qoq_pct_4q_avg(revenue: pd.Series) -> pd.Series:
    """4-quarter rolling average of QoQ revenue growth rate."""
    g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return _rolling_mean(g, _TD_YEAR)


def rvd_135_rev_qoq_pct_8q_avg(revenue: pd.Series) -> pd.Series:
    """8-quarter rolling average of QoQ revenue growth rate."""
    g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return _rolling_mean(g, _TD_2YEAR)


# --- Group K (136-150): Composite and normalized deterioration signals ---

def rvd_136_rev_yoy_vs_2y_avg_growth(revenue: pd.Series) -> pd.Series:
    """Current YoY growth vs its own 2-year average (growth deceleration vs baseline)."""
    g    = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    base = _rolling_mean(g, _TD_2YEAR)
    return g - base


def rvd_137_rev_growth_vs_5y_avg_growth(revenue: pd.Series) -> pd.Series:
    """Current YoY growth vs its own 5-year average (long-run regime change)."""
    g    = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    base = _rolling_mean(g, _TD_5YEAR)
    return g - base


def rvd_138_rev_yoy_zscore_4q(revenue: pd.Series) -> pd.Series:
    """Z-score of YoY revenue growth within trailing 4-quarter window."""
    g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return _zscore_rolling(g, _TD_YEAR)


def rvd_139_rev_yoy_zscore_8q(revenue: pd.Series) -> pd.Series:
    """Z-score of YoY revenue growth within trailing 8-quarter window."""
    g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return _zscore_rolling(g, _TD_2YEAR)


def rvd_140_rev_qoq_zscore_4q(revenue: pd.Series) -> pd.Series:
    """Z-score of QoQ revenue growth within trailing 4-quarter window."""
    g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return _zscore_rolling(g, _TD_YEAR)


def rvd_141_rev_dd_4q_pct_rank(revenue: pd.Series) -> pd.Series:
    """Percentile rank of 4-quarter revenue drawdown within its trailing 4-year window."""
    dd = _safe_div(revenue - _rolling_max(revenue, _TD_YEAR), _rolling_max(revenue, _TD_YEAR).abs())
    return dd.rolling(_TD_2YEAR * 2, min_periods=max(1, _TD_YEAR)).rank(pct=True)


def rvd_142_rev_3factor_deterioration_score(revenue: pd.Series) -> pd.Series:
    """
    Composite: mean of (a) YoY growth sign, (b) QoQ growth sign,
    (c) revenue-below-4q-avg flag, rescaled to [-1, +1].
    More negative = more severe deterioration.
    """
    yoy_s  = np.sign((revenue - revenue.shift(_TD_YEAR)).fillna(0.0))
    qoq_s  = np.sign((revenue - revenue.shift(_TD_QTR)).fillna(0.0))
    avg4   = _rolling_mean(revenue, _TD_YEAR)
    below  = np.where(revenue < avg4, -1.0, 1.0)
    below  = pd.Series(below, index=revenue.index)
    return (yoy_s + qoq_s + below) / 3.0


def rvd_143_rev_payables_ratio(revenue: pd.Series, payables: pd.Series) -> pd.Series:
    """Payables-to-revenue: rising ratio can signal revenue decline with sticky costs."""
    return _safe_div(payables, revenue)


def rvd_144_rev_payables_ratio_qoq_chg(revenue: pd.Series, payables: pd.Series) -> pd.Series:
    """QoQ change in payables-to-revenue."""
    ratio = _safe_div(payables, revenue)
    return ratio - ratio.shift(_TD_QTR)


def rvd_145_rev_payables_ratio_yoy_chg(revenue: pd.Series, payables: pd.Series) -> pd.Series:
    """YoY change in payables-to-revenue."""
    ratio = _safe_div(payables, revenue)
    return ratio - ratio.shift(_TD_YEAR)


def rvd_146_rev_payables_ratio_zscore_4q(revenue: pd.Series, payables: pd.Series) -> pd.Series:
    """Z-score of payables/revenue ratio within trailing 4-quarter window."""
    ratio = _safe_div(payables, revenue)
    return _zscore_rolling(ratio, _TD_YEAR)


def rvd_147_rev_growth_to_assets_ratio(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY revenue growth rate normalized by (revenue/assets) — efficiency-adjusted growth."""
    g      = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    turnov = _safe_div(revenue, assets)
    return _safe_div(g, turnov.abs())


def rvd_148_rev_yoy_below_zero_fraction_8q(revenue: pd.Series) -> pd.Series:
    """Fraction of trailing 8-quarter window with negative YoY revenue growth."""
    g    = revenue - revenue.shift(_TD_YEAR)
    flag = (g < 0).astype(float)
    return _rolling_mean(flag, _TD_2YEAR)


def rvd_149_rev_qoq_sum_4q(revenue: pd.Series) -> pd.Series:
    """Sum of QoQ revenue changes over trailing 4 quarters (trailing revenue momentum)."""
    qoq = revenue - revenue.shift(_TD_QTR)
    return _rolling_sum(qoq, _TD_YEAR)


def rvd_150_rev_composite_deterioration_index(revenue: pd.Series) -> pd.Series:
    """
    Composite deterioration index: equal-weight average of YoY growth z-score,
    4q drawdown z-score, and QoQ growth z-score (all normalized to comparable scale).
    More negative = more severe top-line deterioration.
    """
    g_yoy  = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    g_qoq  = _safe_div(revenue - revenue.shift(_TD_QTR),  revenue.shift(_TD_QTR).abs())
    peak   = _rolling_max(revenue, _TD_YEAR)
    dd     = _safe_div(revenue - peak, peak.abs())
    z_yoy  = _zscore_rolling(g_yoy, _TD_2YEAR)
    z_qoq  = _zscore_rolling(g_qoq, _TD_2YEAR)
    z_dd   = _zscore_rolling(dd,    _TD_2YEAR)
    return (z_yoy + z_qoq + z_dd) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

REVENUE_DETERIORATION_REGISTRY_076_150 = {
    "rvd_076_cor_yoy_pct": {"inputs": ["cor"], "func": rvd_076_cor_yoy_pct},
    "rvd_077_cor_qoq_pct": {"inputs": ["cor"], "func": rvd_077_cor_qoq_pct},
    "rvd_078_rev_cor_spread_qoq": {"inputs": ["revenue", "cor"], "func": rvd_078_rev_cor_spread_qoq},
    "rvd_079_rev_cor_spread_yoy": {"inputs": ["revenue", "cor"], "func": rvd_079_rev_cor_spread_yoy},
    "rvd_080_rev_declining_cor_flat_flag": {"inputs": ["revenue", "cor"], "func": rvd_080_rev_declining_cor_flat_flag},
    "rvd_081_gp_yoy_pct": {"inputs": ["gp"], "func": rvd_081_gp_yoy_pct},
    "rvd_082_gp_qoq_pct": {"inputs": ["gp"], "func": rvd_082_gp_qoq_pct},
    "rvd_083_gp_rev_growth_divergence_qoq": {"inputs": ["revenue", "gp"], "func": rvd_083_gp_rev_growth_divergence_qoq},
    "rvd_084_gp_rev_growth_divergence_yoy": {"inputs": ["revenue", "gp"], "func": rvd_084_gp_rev_growth_divergence_yoy},
    "rvd_085_gp_vs_4q_avg": {"inputs": ["gp"], "func": rvd_085_gp_vs_4q_avg},
    "rvd_086_gp_dd_from_4q_peak": {"inputs": ["gp"], "func": rvd_086_gp_dd_from_4q_peak},
    "rvd_087_gp_dd_from_ath": {"inputs": ["gp"], "func": rvd_087_gp_dd_from_ath},
    "rvd_088_gp_new_4q_low_flag": {"inputs": ["gp"], "func": rvd_088_gp_new_4q_low_flag},
    "rvd_089_gp_zscore_4q": {"inputs": ["gp"], "func": rvd_089_gp_zscore_4q},
    "rvd_090_cor_to_rev_rising_trend": {"inputs": ["revenue", "cor"], "func": rvd_090_cor_to_rev_rising_trend},
    "rvd_091_receivables_yoy_pct": {"inputs": ["receivables"], "func": rvd_091_receivables_yoy_pct},
    "rvd_092_receivables_qoq_pct": {"inputs": ["receivables"], "func": rvd_092_receivables_qoq_pct},
    "rvd_093_inventory_yoy_pct": {"inputs": ["inventory"], "func": rvd_093_inventory_yoy_pct},
    "rvd_094_inventory_qoq_pct": {"inputs": ["inventory"], "func": rvd_094_inventory_qoq_pct},
    "rvd_095_receivables_growth_vs_rev_growth_qoq": {"inputs": ["revenue", "receivables"], "func": rvd_095_receivables_growth_vs_rev_growth_qoq},
    "rvd_096_receivables_growth_vs_rev_growth_yoy": {"inputs": ["revenue", "receivables"], "func": rvd_096_receivables_growth_vs_rev_growth_yoy},
    "rvd_097_inventory_growth_vs_rev_growth_qoq": {"inputs": ["revenue", "inventory"], "func": rvd_097_inventory_growth_vs_rev_growth_qoq},
    "rvd_098_inventory_growth_vs_rev_growth_yoy": {"inputs": ["revenue", "inventory"], "func": rvd_098_inventory_growth_vs_rev_growth_yoy},
    "rvd_099_receivables_plus_inventory_to_rev": {"inputs": ["revenue", "receivables", "inventory"], "func": rvd_099_receivables_plus_inventory_to_rev},
    "rvd_100_rec_inv_to_rev_qoq_chg": {"inputs": ["revenue", "receivables", "inventory"], "func": rvd_100_rec_inv_to_rev_qoq_chg},
    "rvd_101_rec_inv_to_rev_yoy_chg": {"inputs": ["revenue", "receivables", "inventory"], "func": rvd_101_rec_inv_to_rev_yoy_chg},
    "rvd_102_receivables_to_rev_4q_avg": {"inputs": ["revenue", "receivables"], "func": rvd_102_receivables_to_rev_4q_avg},
    "rvd_103_inventory_to_rev_4q_avg": {"inputs": ["revenue", "inventory"], "func": rvd_103_inventory_to_rev_4q_avg},
    "rvd_104_receivables_to_rev_zscore_4q": {"inputs": ["revenue", "receivables"], "func": rvd_104_receivables_to_rev_zscore_4q},
    "rvd_105_inventory_to_rev_zscore_4q": {"inputs": ["revenue", "inventory"], "func": rvd_105_inventory_to_rev_zscore_4q},
    "rvd_106_deferredrev_yoy_pct": {"inputs": ["deferredrev"], "func": rvd_106_deferredrev_yoy_pct},
    "rvd_107_deferredrev_qoq_pct": {"inputs": ["deferredrev"], "func": rvd_107_deferredrev_qoq_pct},
    "rvd_108_deferredrev_to_rev_zscore_4q": {"inputs": ["revenue", "deferredrev"], "func": rvd_108_deferredrev_to_rev_zscore_4q},
    "rvd_109_deferredrev_growth_vs_rev_growth_qoq": {"inputs": ["revenue", "deferredrev"], "func": rvd_109_deferredrev_growth_vs_rev_growth_qoq},
    "rvd_110_rev_to_assets_ratio": {"inputs": ["revenue", "assets"], "func": rvd_110_rev_to_assets_ratio},
    "rvd_111_rev_to_assets_pct_rank_8q": {"inputs": ["revenue", "assets"], "func": rvd_111_rev_to_assets_pct_rank_8q},
    "rvd_112_rev_to_assets_yoy_chg": {"inputs": ["revenue", "assets"], "func": rvd_112_rev_to_assets_yoy_chg},
    "rvd_113_rev_to_assets_zscore_4q": {"inputs": ["revenue", "assets"], "func": rvd_113_rev_to_assets_zscore_4q},
    "rvd_114_rev_per_share_level": {"inputs": ["revenue", "shareswa"], "func": rvd_114_rev_per_share_level},
    "rvd_115_rev_per_share_dd_from_4q_peak": {"inputs": ["revenue", "shareswa"], "func": rvd_115_rev_per_share_dd_from_4q_peak},
    "rvd_116_rev_per_share_dd_from_ath": {"inputs": ["revenue", "shareswa"], "func": rvd_116_rev_per_share_dd_from_ath},
    "rvd_117_rev_per_share_zscore_4q": {"inputs": ["revenue", "shareswa"], "func": rvd_117_rev_per_share_zscore_4q},
    "rvd_118_shareswa_yoy_pct": {"inputs": ["shareswa"], "func": rvd_118_shareswa_yoy_pct},
    "rvd_119_rev_4q_cagr": {"inputs": ["revenue"], "func": rvd_119_rev_4q_cagr},
    "rvd_120_rev_8q_cagr": {"inputs": ["revenue"], "func": rvd_120_rev_8q_cagr},
    "rvd_121_rev_20q_cagr": {"inputs": ["revenue"], "func": rvd_121_rev_20q_cagr},
    "rvd_122_rev_growth_regime_flag": {"inputs": ["revenue"], "func": rvd_122_rev_growth_regime_flag},
    "rvd_123_rev_growth_decel_flag": {"inputs": ["revenue"], "func": rvd_123_rev_growth_decel_flag},
    "rvd_124_rev_below_2q_and_4q_avg_flag": {"inputs": ["revenue"], "func": rvd_124_rev_below_2q_and_4q_avg_flag},
    "rvd_125_rev_3q_consecutive_yoy_decline_flag": {"inputs": ["revenue"], "func": rvd_125_rev_3q_consecutive_yoy_decline_flag},
    "rvd_126_rev_4q_consecutive_yoy_decline_flag": {"inputs": ["revenue"], "func": rvd_126_rev_4q_consecutive_yoy_decline_flag},
    "rvd_127_rev_reversal_from_growth_to_decline": {"inputs": ["revenue"], "func": rvd_127_rev_reversal_from_growth_to_decline},
    "rvd_128_rev_qoq_pct_4q_rolling_min": {"inputs": ["revenue"], "func": rvd_128_rev_qoq_pct_4q_rolling_min},
    "rvd_129_rev_qoq_pct_4q_range": {"inputs": ["revenue"], "func": rvd_129_rev_qoq_pct_4q_range},
    "rvd_130_rev_level_new_8q_low_flag": {"inputs": ["revenue"], "func": rvd_130_rev_level_new_8q_low_flag},
    "rvd_131_rev_expanding_pct_rank": {"inputs": ["revenue"], "func": rvd_131_rev_expanding_pct_rank},
    "rvd_132_rev_4q_pct_above_trend": {"inputs": ["revenue"], "func": rvd_132_rev_4q_pct_above_trend},
    "rvd_133_rev_yoy_pct_4q_avg": {"inputs": ["revenue"], "func": rvd_133_rev_yoy_pct_4q_avg},
    "rvd_134_rev_qoq_pct_4q_avg": {"inputs": ["revenue"], "func": rvd_134_rev_qoq_pct_4q_avg},
    "rvd_135_rev_qoq_pct_8q_avg": {"inputs": ["revenue"], "func": rvd_135_rev_qoq_pct_8q_avg},
    "rvd_136_rev_yoy_vs_2y_avg_growth": {"inputs": ["revenue"], "func": rvd_136_rev_yoy_vs_2y_avg_growth},
    "rvd_137_rev_growth_vs_5y_avg_growth": {"inputs": ["revenue"], "func": rvd_137_rev_growth_vs_5y_avg_growth},
    "rvd_138_rev_yoy_zscore_4q": {"inputs": ["revenue"], "func": rvd_138_rev_yoy_zscore_4q},
    "rvd_139_rev_yoy_zscore_8q": {"inputs": ["revenue"], "func": rvd_139_rev_yoy_zscore_8q},
    "rvd_140_rev_qoq_zscore_4q": {"inputs": ["revenue"], "func": rvd_140_rev_qoq_zscore_4q},
    "rvd_141_rev_dd_4q_pct_rank": {"inputs": ["revenue"], "func": rvd_141_rev_dd_4q_pct_rank},
    "rvd_142_rev_3factor_deterioration_score": {"inputs": ["revenue"], "func": rvd_142_rev_3factor_deterioration_score},
    "rvd_143_rev_payables_ratio": {"inputs": ["revenue", "payables"], "func": rvd_143_rev_payables_ratio},
    "rvd_144_rev_payables_ratio_qoq_chg": {"inputs": ["revenue", "payables"], "func": rvd_144_rev_payables_ratio_qoq_chg},
    "rvd_145_rev_payables_ratio_yoy_chg": {"inputs": ["revenue", "payables"], "func": rvd_145_rev_payables_ratio_yoy_chg},
    "rvd_146_rev_payables_ratio_zscore_4q": {"inputs": ["revenue", "payables"], "func": rvd_146_rev_payables_ratio_zscore_4q},
    "rvd_147_rev_growth_to_assets_ratio": {"inputs": ["revenue", "assets"], "func": rvd_147_rev_growth_to_assets_ratio},
    "rvd_148_rev_yoy_below_zero_fraction_8q": {"inputs": ["revenue"], "func": rvd_148_rev_yoy_below_zero_fraction_8q},
    "rvd_149_rev_qoq_sum_4q": {"inputs": ["revenue"], "func": rvd_149_rev_qoq_sum_4q},
    "rvd_150_rev_composite_deterioration_index": {"inputs": ["revenue"], "func": rvd_150_rev_composite_deterioration_index},
}
