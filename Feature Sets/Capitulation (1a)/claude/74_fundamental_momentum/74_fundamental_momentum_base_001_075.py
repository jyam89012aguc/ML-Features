"""
74_fundamental_momentum — Base Features 001-075
Domain: QoQ/YoY trend, slope, and momentum of core fundamental metrics
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


def _sign_change_fraction(s: pd.Series, w: int) -> pd.Series:
    """Fraction of rolling window where sign differs from previous observation."""
    sign_flip = (s * s.shift(1) < 0).astype(float)
    return _rolling_mean(sign_flip, w)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Single-metric OLS slope over multiple horizons ---

def fmo_001_revenue_slope_4q(revenue: pd.Series) -> pd.Series:
    """OLS slope of revenue over trailing 4-quarter (252-day) window."""
    return _rolling_slope(revenue, _TD_YEAR)


def fmo_002_revenue_slope_8q(revenue: pd.Series) -> pd.Series:
    """OLS slope of revenue over trailing 8-quarter (504-day) window."""
    return _rolling_slope(revenue, _TD_2Y)


def fmo_003_netinc_slope_4q(netinc: pd.Series) -> pd.Series:
    """OLS slope of net income over trailing 4-quarter window."""
    return _rolling_slope(netinc, _TD_YEAR)


def fmo_004_netinc_slope_8q(netinc: pd.Series) -> pd.Series:
    """OLS slope of net income over trailing 8-quarter window."""
    return _rolling_slope(netinc, _TD_2Y)


def fmo_005_eps_slope_4q(eps: pd.Series) -> pd.Series:
    """OLS slope of EPS over trailing 4-quarter window."""
    return _rolling_slope(eps, _TD_YEAR)


def fmo_006_eps_slope_8q(eps: pd.Series) -> pd.Series:
    """OLS slope of EPS over trailing 8-quarter window."""
    return _rolling_slope(eps, _TD_2Y)


def fmo_007_gp_slope_4q(gp: pd.Series) -> pd.Series:
    """OLS slope of gross profit over trailing 4-quarter window."""
    return _rolling_slope(gp, _TD_YEAR)


def fmo_008_opinc_slope_4q(opinc: pd.Series) -> pd.Series:
    """OLS slope of operating income over trailing 4-quarter window."""
    return _rolling_slope(opinc, _TD_YEAR)


def fmo_009_ebitda_slope_4q(ebitda: pd.Series) -> pd.Series:
    """OLS slope of EBITDA over trailing 4-quarter window."""
    return _rolling_slope(ebitda, _TD_YEAR)


def fmo_010_fcf_slope_4q(fcf: pd.Series) -> pd.Series:
    """OLS slope of free cash flow over trailing 4-quarter window."""
    return _rolling_slope(fcf, _TD_YEAR)


def fmo_011_ncfo_slope_4q(ncfo: pd.Series) -> pd.Series:
    """OLS slope of operating cash flow over trailing 4-quarter window."""
    return _rolling_slope(ncfo, _TD_YEAR)


def fmo_012_equity_slope_4q(equity: pd.Series) -> pd.Series:
    """OLS slope of shareholders equity over trailing 4-quarter window."""
    return _rolling_slope(equity, _TD_YEAR)


def fmo_013_assets_slope_4q(assets: pd.Series) -> pd.Series:
    """OLS slope of total assets over trailing 4-quarter window."""
    return _rolling_slope(assets, _TD_YEAR)


def fmo_014_revenue_slope_12q(revenue: pd.Series) -> pd.Series:
    """OLS slope of revenue over trailing 12-quarter (756-day) window."""
    return _rolling_slope(revenue, _TD_3Y)


def fmo_015_netinc_slope_12q(netinc: pd.Series) -> pd.Series:
    """OLS slope of net income over trailing 12-quarter (756-day) window."""
    return _rolling_slope(netinc, _TD_3Y)


# --- Group B (016-030): QoQ momentum sign, strength, and streak ---

def fmo_016_revenue_qoq_sign(revenue: pd.Series) -> pd.Series:
    """Sign of revenue QoQ change: +1 improving, -1 deteriorating, 0 flat."""
    return np.sign(revenue - revenue.shift(_TD_QTR)).astype(float)


def fmo_017_netinc_qoq_sign(netinc: pd.Series) -> pd.Series:
    """Sign of net income QoQ change."""
    return np.sign(netinc - netinc.shift(_TD_QTR)).astype(float)


def fmo_018_eps_qoq_sign(eps: pd.Series) -> pd.Series:
    """Sign of EPS QoQ change."""
    return np.sign(eps - eps.shift(_TD_QTR)).astype(float)


def fmo_019_gp_qoq_sign(gp: pd.Series) -> pd.Series:
    """Sign of gross profit QoQ change."""
    return np.sign(gp - gp.shift(_TD_QTR)).astype(float)


def fmo_020_opinc_qoq_sign(opinc: pd.Series) -> pd.Series:
    """Sign of operating income QoQ change."""
    return np.sign(opinc - opinc.shift(_TD_QTR)).astype(float)


def fmo_021_ebitda_qoq_sign(ebitda: pd.Series) -> pd.Series:
    """Sign of EBITDA QoQ change."""
    return np.sign(ebitda - ebitda.shift(_TD_QTR)).astype(float)


def fmo_022_fcf_qoq_sign(fcf: pd.Series) -> pd.Series:
    """Sign of free cash flow QoQ change."""
    return np.sign(fcf - fcf.shift(_TD_QTR)).astype(float)


def fmo_023_ncfo_qoq_sign(ncfo: pd.Series) -> pd.Series:
    """Sign of operating cash flow QoQ change."""
    return np.sign(ncfo - ncfo.shift(_TD_QTR)).astype(float)


def fmo_024_equity_qoq_sign(equity: pd.Series) -> pd.Series:
    """Sign of equity QoQ change."""
    return np.sign(equity - equity.shift(_TD_QTR)).astype(float)


def fmo_025_assets_qoq_sign(assets: pd.Series) -> pd.Series:
    """Sign of total assets QoQ change."""
    return np.sign(assets - assets.shift(_TD_QTR)).astype(float)


def fmo_026_revenue_positive_qoq_streak_4q(revenue: pd.Series) -> pd.Series:
    """Rolling 4-quarter count of positive QoQ revenue changes."""
    positive = (revenue > revenue.shift(_TD_QTR)).astype(float)
    return _rolling_sum(positive, _TD_YEAR)


def fmo_027_netinc_positive_qoq_streak_4q(netinc: pd.Series) -> pd.Series:
    """Rolling 4-quarter count of positive QoQ net income changes."""
    positive = (netinc > netinc.shift(_TD_QTR)).astype(float)
    return _rolling_sum(positive, _TD_YEAR)


def fmo_028_eps_positive_qoq_streak_4q(eps: pd.Series) -> pd.Series:
    """Rolling 4-quarter count of positive QoQ EPS changes."""
    positive = (eps > eps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(positive, _TD_YEAR)


def fmo_029_netinc_consecutive_improving_streak(netinc: pd.Series) -> pd.Series:
    """
    Current consecutive-improvement streak length (daily observations).
    Resets to 0 whenever QoQ net income is not improving.
    """
    improving = (netinc > netinc.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(improving), dtype=float)
    arr = improving.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=netinc.index)


def fmo_030_revenue_consecutive_improving_streak(revenue: pd.Series) -> pd.Series:
    """
    Current consecutive-improvement streak length for revenue (daily obs).
    Resets to 0 whenever QoQ revenue is not improving.
    """
    improving = (revenue > revenue.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(improving), dtype=float)
    arr = improving.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=revenue.index)


# --- Group C (031-045): Momentum vs trailing average (strength) ---

def fmo_031_revenue_vs_4q_avg(revenue: pd.Series) -> pd.Series:
    """Revenue minus its trailing 4-quarter mean — momentum-vs-average level."""
    return revenue - _rolling_mean(revenue, _TD_YEAR)


def fmo_032_revenue_pct_vs_4q_avg(revenue: pd.Series) -> pd.Series:
    """Revenue percent deviation above/below its trailing 4-quarter mean."""
    avg = _rolling_mean(revenue, _TD_YEAR)
    return _safe_div_abs(revenue - avg, avg)


def fmo_033_netinc_vs_4q_avg(netinc: pd.Series) -> pd.Series:
    """Net income minus its trailing 4-quarter mean."""
    return netinc - _rolling_mean(netinc, _TD_YEAR)


def fmo_034_netinc_pct_vs_4q_avg(netinc: pd.Series) -> pd.Series:
    """Net income percent deviation from trailing 4-quarter mean."""
    avg = _rolling_mean(netinc, _TD_YEAR)
    return _safe_div_abs(netinc - avg, avg)


def fmo_035_eps_vs_4q_avg(eps: pd.Series) -> pd.Series:
    """EPS minus trailing 4-quarter mean."""
    return eps - _rolling_mean(eps, _TD_YEAR)


def fmo_036_gp_vs_4q_avg(gp: pd.Series) -> pd.Series:
    """Gross profit minus trailing 4-quarter mean."""
    return gp - _rolling_mean(gp, _TD_YEAR)


def fmo_037_opinc_vs_4q_avg(opinc: pd.Series) -> pd.Series:
    """Operating income minus trailing 4-quarter mean."""
    return opinc - _rolling_mean(opinc, _TD_YEAR)


def fmo_038_ebitda_vs_4q_avg(ebitda: pd.Series) -> pd.Series:
    """EBITDA minus trailing 4-quarter mean."""
    return ebitda - _rolling_mean(ebitda, _TD_YEAR)


def fmo_039_fcf_vs_4q_avg(fcf: pd.Series) -> pd.Series:
    """Free cash flow minus trailing 4-quarter mean."""
    return fcf - _rolling_mean(fcf, _TD_YEAR)


def fmo_040_ncfo_vs_4q_avg(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow minus trailing 4-quarter mean."""
    return ncfo - _rolling_mean(ncfo, _TD_YEAR)


def fmo_041_revenue_vs_8q_avg(revenue: pd.Series) -> pd.Series:
    """Revenue minus its trailing 8-quarter mean."""
    return revenue - _rolling_mean(revenue, _TD_2Y)


def fmo_042_netinc_vs_8q_avg(netinc: pd.Series) -> pd.Series:
    """Net income minus its trailing 8-quarter mean."""
    return netinc - _rolling_mean(netinc, _TD_2Y)


def fmo_043_eps_vs_8q_avg(eps: pd.Series) -> pd.Series:
    """EPS minus trailing 8-quarter mean."""
    return eps - _rolling_mean(eps, _TD_2Y)


def fmo_044_ebitda_pct_vs_8q_avg(ebitda: pd.Series) -> pd.Series:
    """EBITDA percent deviation from trailing 8-quarter mean."""
    avg = _rolling_mean(ebitda, _TD_2Y)
    return _safe_div_abs(ebitda - avg, avg)


def fmo_045_fcf_pct_vs_8q_avg(fcf: pd.Series) -> pd.Series:
    """FCF percent deviation from trailing 8-quarter mean."""
    avg = _rolling_mean(fcf, _TD_2Y)
    return _safe_div_abs(fcf - avg, avg)


# --- Group D (046-060): Momentum breadth — how many metrics are improving ---

def fmo_046_breadth_qoq_improving_count(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """Count of core metrics with positive QoQ change (0-10 scale)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    improving = sum((m > m.shift(_TD_QTR)).astype(float) for m in metrics)
    return improving


def fmo_047_breadth_qoq_improving_fraction(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """Fraction of core metrics with positive QoQ change (0.0-1.0)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    improving = sum((m > m.shift(_TD_QTR)).astype(float) for m in metrics)
    return improving / 10.0


def fmo_048_breadth_yoy_improving_count(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """Count of core metrics with positive YoY change (0-10 scale)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    improving = sum((m > m.shift(_TD_YEAR)).astype(float) for m in metrics)
    return improving


def fmo_049_breadth_yoy_improving_fraction(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """Fraction of core metrics with positive YoY change (0.0-1.0)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    improving = sum((m > m.shift(_TD_YEAR)).astype(float) for m in metrics)
    return improving / 10.0


def fmo_050_breadth_net_improving_qoq(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """Net-improving count QoQ: #improving minus #deteriorating (-10 to +10)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    net = sum(np.sign(m - m.shift(_TD_QTR)) for m in metrics)
    return net.astype(float)


def fmo_051_breadth_net_improving_yoy(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """Net-improving count YoY: #improving minus #deteriorating (-10 to +10)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    net = sum(np.sign(m - m.shift(_TD_YEAR)) for m in metrics)
    return net.astype(float)


def fmo_052_breadth_all_improving_qoq_flag(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """1 if all 10 core metrics show positive QoQ change, else 0."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    all_up = (sum((m > m.shift(_TD_QTR)).astype(float) for m in metrics) == 10.0)
    return all_up.astype(float)


def fmo_053_breadth_all_deteriorating_qoq_flag(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """1 if all 10 core metrics show negative QoQ change (full breadth deterioration)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    all_down = (sum((m < m.shift(_TD_QTR)).astype(float) for m in metrics) == 10.0)
    return all_down.astype(float)


def fmo_054_breadth_income_metrics_improving_qoq(
    netinc: pd.Series, eps: pd.Series, gp: pd.Series,
    opinc: pd.Series, ebitda: pd.Series
) -> pd.Series:
    """Count of income-statement metrics (5) improving QoQ."""
    metrics = [netinc, eps, gp, opinc, ebitda]
    return sum((m > m.shift(_TD_QTR)).astype(float) for m in metrics)


def fmo_055_breadth_cashflow_metrics_improving_qoq(
    fcf: pd.Series, ncfo: pd.Series
) -> pd.Series:
    """Count of cash flow metrics (2) improving QoQ (0-2 scale)."""
    metrics = [fcf, ncfo]
    return sum((m > m.shift(_TD_QTR)).astype(float) for m in metrics)


# --- Group E (056-075): Percentile rank, composite index, multi-quarter lows ---

def fmo_056_revenue_pct_rank_4q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of revenue within trailing 4-quarter (252-day) window."""
    return _rolling_rank_pct(revenue, _TD_YEAR)


def fmo_057_revenue_pct_rank_8q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of revenue within trailing 8-quarter window."""
    return _rolling_rank_pct(revenue, _TD_2Y)


def fmo_058_netinc_pct_rank_4q(netinc: pd.Series) -> pd.Series:
    """Percentile rank of net income within trailing 4-quarter window."""
    return _rolling_rank_pct(netinc, _TD_YEAR)


def fmo_059_eps_pct_rank_4q(eps: pd.Series) -> pd.Series:
    """Percentile rank of EPS within trailing 4-quarter window."""
    return _rolling_rank_pct(eps, _TD_YEAR)


def fmo_060_ebitda_pct_rank_4q(ebitda: pd.Series) -> pd.Series:
    """Percentile rank of EBITDA within trailing 4-quarter window."""
    return _rolling_rank_pct(ebitda, _TD_YEAR)


def fmo_061_fcf_pct_rank_4q(fcf: pd.Series) -> pd.Series:
    """Percentile rank of FCF within trailing 4-quarter window."""
    return _rolling_rank_pct(fcf, _TD_YEAR)


def fmo_062_revenue_expanding_pct_rank(revenue: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of revenue."""
    return revenue.expanding(min_periods=2).rank(pct=True)


def fmo_063_netinc_expanding_pct_rank(netinc: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of net income."""
    return netinc.expanding(min_periods=2).rank(pct=True)


def fmo_064_eps_expanding_pct_rank(eps: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of EPS."""
    return eps.expanding(min_periods=2).rank(pct=True)


def fmo_065_count_metrics_at_new_4q_low(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """Count of core metrics currently at a 4-quarter (252-day) rolling minimum."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    at_low = sum(
        (m <= _rolling_min(m, _TD_YEAR)).astype(float)
        for m in metrics
    )
    return at_low


def fmo_066_count_metrics_at_new_8q_low(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """Count of core metrics currently at a 8-quarter (504-day) rolling minimum."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    at_low = sum(
        (m <= _rolling_min(m, _TD_2Y)).astype(float)
        for m in metrics
    )
    return at_low


def fmo_067_composite_fmo_zscore_index(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Composite fundamental-momentum index: equally weighted mean of 4-quarter
    z-scores across all 10 core metrics.
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    zscores = [_zscore_rolling(m, _TD_YEAR) for m in metrics]
    total = zscores[0].copy()
    for z in zscores[1:]:
        total = total + z
    return total / 10.0


def fmo_068_composite_fmo_pct_rank_index(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Composite fundamental-momentum index: equally weighted mean of 4-quarter
    percentile ranks across all 10 core metrics.
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    ranks = [_rolling_rank_pct(m, _TD_YEAR) for m in metrics]
    total = ranks[0].copy()
    for r in ranks[1:]:
        total = total + r
    return total / 10.0


def fmo_069_momentum_diffusion_index_4q(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Momentum diffusion index: rolling 4-quarter (252-day) mean of the
    net-improving-count series.  Measures sustained multi-metric breadth trend.
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    net = sum(np.sign(m - m.shift(_TD_QTR)) for m in metrics).astype(float)
    return _rolling_mean(net, _TD_YEAR)


def fmo_070_momentum_diffusion_index_8q(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Momentum diffusion index: rolling 8-quarter (504-day) mean of the
    net-improving-count series.
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    net = sum(np.sign(m - m.shift(_TD_QTR)) for m in metrics).astype(float)
    return _rolling_mean(net, _TD_2Y)


def fmo_071_revenue_ewm_momentum(revenue: pd.Series) -> pd.Series:
    """Revenue minus its 4-quarter EWM (span=252); EWM-based momentum signal."""
    return revenue - _ewm_mean(revenue, _TD_YEAR)


def fmo_072_netinc_ewm_momentum(netinc: pd.Series) -> pd.Series:
    """Net income minus its 4-quarter EWM (span=252); momentum signal."""
    return netinc - _ewm_mean(netinc, _TD_YEAR)


def fmo_073_eps_ewm_momentum(eps: pd.Series) -> pd.Series:
    """EPS minus its 4-quarter EWM (span=252); momentum signal."""
    return eps - _ewm_mean(eps, _TD_YEAR)


def fmo_074_breadth_improving_4q_rolling_mean(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Rolling 4-quarter (252-day) mean of the QoQ-improving-count series.
    Captures sustained breadth vs point-in-time breadth.
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    improving = sum((m > m.shift(_TD_QTR)).astype(float) for m in metrics)
    return _rolling_mean(improving, _TD_YEAR)


def fmo_075_composite_slope_index(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Composite slope index: equally weighted sum of the sign of the 4-quarter
    OLS slope across all 10 core metrics (-10 to +10 scale).
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    slope_signs = sum(np.sign(_rolling_slope(m, _TD_YEAR)) for m in metrics)
    return slope_signs.astype(float)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

FUNDAMENTAL_MOMENTUM_REGISTRY_001_075 = {
    "fmo_001_revenue_slope_4q":                    {"inputs": ["revenue"],                                                                                           "func": fmo_001_revenue_slope_4q},
    "fmo_002_revenue_slope_8q":                    {"inputs": ["revenue"],                                                                                           "func": fmo_002_revenue_slope_8q},
    "fmo_003_netinc_slope_4q":                     {"inputs": ["netinc"],                                                                                            "func": fmo_003_netinc_slope_4q},
    "fmo_004_netinc_slope_8q":                     {"inputs": ["netinc"],                                                                                            "func": fmo_004_netinc_slope_8q},
    "fmo_005_eps_slope_4q":                        {"inputs": ["eps"],                                                                                               "func": fmo_005_eps_slope_4q},
    "fmo_006_eps_slope_8q":                        {"inputs": ["eps"],                                                                                               "func": fmo_006_eps_slope_8q},
    "fmo_007_gp_slope_4q":                         {"inputs": ["gp"],                                                                                                "func": fmo_007_gp_slope_4q},
    "fmo_008_opinc_slope_4q":                      {"inputs": ["opinc"],                                                                                             "func": fmo_008_opinc_slope_4q},
    "fmo_009_ebitda_slope_4q":                     {"inputs": ["ebitda"],                                                                                            "func": fmo_009_ebitda_slope_4q},
    "fmo_010_fcf_slope_4q":                        {"inputs": ["fcf"],                                                                                               "func": fmo_010_fcf_slope_4q},
    "fmo_011_ncfo_slope_4q":                       {"inputs": ["ncfo"],                                                                                              "func": fmo_011_ncfo_slope_4q},
    "fmo_012_equity_slope_4q":                     {"inputs": ["equity"],                                                                                            "func": fmo_012_equity_slope_4q},
    "fmo_013_assets_slope_4q":                     {"inputs": ["assets"],                                                                                            "func": fmo_013_assets_slope_4q},
    "fmo_014_revenue_slope_12q":                   {"inputs": ["revenue"],                                                                                           "func": fmo_014_revenue_slope_12q},
    "fmo_015_netinc_slope_12q":                    {"inputs": ["netinc"],                                                                                            "func": fmo_015_netinc_slope_12q},
    "fmo_016_revenue_qoq_sign":                    {"inputs": ["revenue"],                                                                                           "func": fmo_016_revenue_qoq_sign},
    "fmo_017_netinc_qoq_sign":                     {"inputs": ["netinc"],                                                                                            "func": fmo_017_netinc_qoq_sign},
    "fmo_018_eps_qoq_sign":                        {"inputs": ["eps"],                                                                                               "func": fmo_018_eps_qoq_sign},
    "fmo_019_gp_qoq_sign":                         {"inputs": ["gp"],                                                                                               "func": fmo_019_gp_qoq_sign},
    "fmo_020_opinc_qoq_sign":                      {"inputs": ["opinc"],                                                                                             "func": fmo_020_opinc_qoq_sign},
    "fmo_021_ebitda_qoq_sign":                     {"inputs": ["ebitda"],                                                                                            "func": fmo_021_ebitda_qoq_sign},
    "fmo_022_fcf_qoq_sign":                        {"inputs": ["fcf"],                                                                                               "func": fmo_022_fcf_qoq_sign},
    "fmo_023_ncfo_qoq_sign":                       {"inputs": ["ncfo"],                                                                                              "func": fmo_023_ncfo_qoq_sign},
    "fmo_024_equity_qoq_sign":                     {"inputs": ["equity"],                                                                                            "func": fmo_024_equity_qoq_sign},
    "fmo_025_assets_qoq_sign":                     {"inputs": ["assets"],                                                                                            "func": fmo_025_assets_qoq_sign},
    "fmo_026_revenue_positive_qoq_streak_4q":      {"inputs": ["revenue"],                                                                                           "func": fmo_026_revenue_positive_qoq_streak_4q},
    "fmo_027_netinc_positive_qoq_streak_4q":       {"inputs": ["netinc"],                                                                                            "func": fmo_027_netinc_positive_qoq_streak_4q},
    "fmo_028_eps_positive_qoq_streak_4q":          {"inputs": ["eps"],                                                                                               "func": fmo_028_eps_positive_qoq_streak_4q},
    "fmo_029_netinc_consecutive_improving_streak": {"inputs": ["netinc"],                                                                                            "func": fmo_029_netinc_consecutive_improving_streak},
    "fmo_030_revenue_consecutive_improving_streak":{"inputs": ["revenue"],                                                                                           "func": fmo_030_revenue_consecutive_improving_streak},
    "fmo_031_revenue_vs_4q_avg":                   {"inputs": ["revenue"],                                                                                           "func": fmo_031_revenue_vs_4q_avg},
    "fmo_032_revenue_pct_vs_4q_avg":               {"inputs": ["revenue"],                                                                                           "func": fmo_032_revenue_pct_vs_4q_avg},
    "fmo_033_netinc_vs_4q_avg":                    {"inputs": ["netinc"],                                                                                            "func": fmo_033_netinc_vs_4q_avg},
    "fmo_034_netinc_pct_vs_4q_avg":                {"inputs": ["netinc"],                                                                                            "func": fmo_034_netinc_pct_vs_4q_avg},
    "fmo_035_eps_vs_4q_avg":                       {"inputs": ["eps"],                                                                                               "func": fmo_035_eps_vs_4q_avg},
    "fmo_036_gp_vs_4q_avg":                        {"inputs": ["gp"],                                                                                                "func": fmo_036_gp_vs_4q_avg},
    "fmo_037_opinc_vs_4q_avg":                     {"inputs": ["opinc"],                                                                                             "func": fmo_037_opinc_vs_4q_avg},
    "fmo_038_ebitda_vs_4q_avg":                    {"inputs": ["ebitda"],                                                                                            "func": fmo_038_ebitda_vs_4q_avg},
    "fmo_039_fcf_vs_4q_avg":                       {"inputs": ["fcf"],                                                                                               "func": fmo_039_fcf_vs_4q_avg},
    "fmo_040_ncfo_vs_4q_avg":                      {"inputs": ["ncfo"],                                                                                              "func": fmo_040_ncfo_vs_4q_avg},
    "fmo_041_revenue_vs_8q_avg":                   {"inputs": ["revenue"],                                                                                           "func": fmo_041_revenue_vs_8q_avg},
    "fmo_042_netinc_vs_8q_avg":                    {"inputs": ["netinc"],                                                                                            "func": fmo_042_netinc_vs_8q_avg},
    "fmo_043_eps_vs_8q_avg":                       {"inputs": ["eps"],                                                                                               "func": fmo_043_eps_vs_8q_avg},
    "fmo_044_ebitda_pct_vs_8q_avg":                {"inputs": ["ebitda"],                                                                                            "func": fmo_044_ebitda_pct_vs_8q_avg},
    "fmo_045_fcf_pct_vs_8q_avg":                   {"inputs": ["fcf"],                                                                                               "func": fmo_045_fcf_pct_vs_8q_avg},
    "fmo_046_breadth_qoq_improving_count":         {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_046_breadth_qoq_improving_count},
    "fmo_047_breadth_qoq_improving_fraction":      {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_047_breadth_qoq_improving_fraction},
    "fmo_048_breadth_yoy_improving_count":         {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_048_breadth_yoy_improving_count},
    "fmo_049_breadth_yoy_improving_fraction":      {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_049_breadth_yoy_improving_fraction},
    "fmo_050_breadth_net_improving_qoq":           {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_050_breadth_net_improving_qoq},
    "fmo_051_breadth_net_improving_yoy":           {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_051_breadth_net_improving_yoy},
    "fmo_052_breadth_all_improving_qoq_flag":      {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_052_breadth_all_improving_qoq_flag},
    "fmo_053_breadth_all_deteriorating_qoq_flag":  {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_053_breadth_all_deteriorating_qoq_flag},
    "fmo_054_breadth_income_metrics_improving_qoq":{"inputs": ["netinc", "eps", "gp", "opinc", "ebitda"],                                                            "func": fmo_054_breadth_income_metrics_improving_qoq},
    "fmo_055_breadth_cashflow_metrics_improving_qoq": {"inputs": ["fcf", "ncfo"],                                                                                    "func": fmo_055_breadth_cashflow_metrics_improving_qoq},
    "fmo_056_revenue_pct_rank_4q":                 {"inputs": ["revenue"],                                                                                           "func": fmo_056_revenue_pct_rank_4q},
    "fmo_057_revenue_pct_rank_8q":                 {"inputs": ["revenue"],                                                                                           "func": fmo_057_revenue_pct_rank_8q},
    "fmo_058_netinc_pct_rank_4q":                  {"inputs": ["netinc"],                                                                                            "func": fmo_058_netinc_pct_rank_4q},
    "fmo_059_eps_pct_rank_4q":                     {"inputs": ["eps"],                                                                                               "func": fmo_059_eps_pct_rank_4q},
    "fmo_060_ebitda_pct_rank_4q":                  {"inputs": ["ebitda"],                                                                                            "func": fmo_060_ebitda_pct_rank_4q},
    "fmo_061_fcf_pct_rank_4q":                     {"inputs": ["fcf"],                                                                                               "func": fmo_061_fcf_pct_rank_4q},
    "fmo_062_revenue_expanding_pct_rank":          {"inputs": ["revenue"],                                                                                           "func": fmo_062_revenue_expanding_pct_rank},
    "fmo_063_netinc_expanding_pct_rank":           {"inputs": ["netinc"],                                                                                            "func": fmo_063_netinc_expanding_pct_rank},
    "fmo_064_eps_expanding_pct_rank":              {"inputs": ["eps"],                                                                                               "func": fmo_064_eps_expanding_pct_rank},
    "fmo_065_count_metrics_at_new_4q_low":         {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_065_count_metrics_at_new_4q_low},
    "fmo_066_count_metrics_at_new_8q_low":         {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_066_count_metrics_at_new_8q_low},
    "fmo_067_composite_fmo_zscore_index":          {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_067_composite_fmo_zscore_index},
    "fmo_068_composite_fmo_pct_rank_index":        {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_068_composite_fmo_pct_rank_index},
    "fmo_069_momentum_diffusion_index_4q":         {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_069_momentum_diffusion_index_4q},
    "fmo_070_momentum_diffusion_index_8q":         {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_070_momentum_diffusion_index_8q},
    "fmo_071_revenue_ewm_momentum":                {"inputs": ["revenue"],                                                                                           "func": fmo_071_revenue_ewm_momentum},
    "fmo_072_netinc_ewm_momentum":                 {"inputs": ["netinc"],                                                                                            "func": fmo_072_netinc_ewm_momentum},
    "fmo_073_eps_ewm_momentum":                    {"inputs": ["eps"],                                                                                               "func": fmo_073_eps_ewm_momentum},
    "fmo_074_breadth_improving_4q_rolling_mean":   {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_074_breadth_improving_4q_rolling_mean},
    "fmo_075_composite_slope_index":               {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_075_composite_slope_index},
}
