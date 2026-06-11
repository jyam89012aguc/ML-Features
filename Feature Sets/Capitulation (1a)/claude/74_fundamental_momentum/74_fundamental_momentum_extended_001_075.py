"""
74_fundamental_momentum — Extended Features 001-075
Domain: QoQ/YoY trend, slope, and momentum of core fundamentals — additional
        variants: growth rates, acceleration, normalized slopes, distance from
        rolling extremes, YoY streaks, EWM-cross momentum, multi-horizon
        composites and capitulation diagnostics not covered by the base files.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

These features are NET-NEW relative to base_001_075, base_076_150,
2nd_derivatives and 3rd_derivatives — they explore different angles
(percentage growth, normalized slope, distance-from-extreme, YoY streaks,
EWM crossovers, deceleration) rather than duplicating the OLS-slope,
QoQ-sign and breadth features in the base files.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  Functions look strictly backward using
.shift(positive), .rolling(), or .expanding().
Quarterly cadence on the daily index: 1 quarter = 63 trading days,
1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252   # 1 year in trading days
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_TD_QTR  = 63    # 1 quarter in trading days
_TD_2Q   = 126
_TD_3Q   = 189
_EPS     = 1e-9

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
    """Element-wise division; replaces zero denominators with NaN."""
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
    m = _rolling_mean(s, w)
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


def _qoq_pct(s: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change, sign-safe denominator."""
    prev = s.shift(_TD_QTR)
    return _safe_div_abs(s - prev, prev)


def _yoy_pct(s: pd.Series) -> pd.Series:
    """Year-over-year percentage change, sign-safe denominator."""
    prev = s.shift(_TD_YEAR)
    return _safe_div_abs(s - prev, prev)


def _streak_true(cond: pd.Series) -> pd.Series:
    """Consecutive-True streak length up to each row (backward-looking)."""
    arr = cond.astype(int).values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = (out[i - 1] + 1) * arr[i]
    if len(arr) > 0:
        out[0] = float(arr[0])
    return pd.Series(out, index=cond.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): QoQ percentage growth rates ---

def fmo_ext_001_revenue_qoq_pct(revenue: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in revenue."""
    return _qoq_pct(revenue)


def fmo_ext_002_netinc_qoq_pct(netinc: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in net income."""
    return _qoq_pct(netinc)


def fmo_ext_003_eps_qoq_pct(eps: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in EPS."""
    return _qoq_pct(eps)


def fmo_ext_004_gp_qoq_pct(gp: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in gross profit."""
    return _qoq_pct(gp)


def fmo_ext_005_opinc_qoq_pct(opinc: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in operating income."""
    return _qoq_pct(opinc)


def fmo_ext_006_ebitda_qoq_pct(ebitda: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in EBITDA."""
    return _qoq_pct(ebitda)


def fmo_ext_007_fcf_qoq_pct(fcf: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in free cash flow."""
    return _qoq_pct(fcf)


def fmo_ext_008_ncfo_qoq_pct(ncfo: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in operating cash flow."""
    return _qoq_pct(ncfo)


def fmo_ext_009_equity_qoq_pct(equity: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in shareholders equity."""
    return _qoq_pct(equity)


def fmo_ext_010_assets_qoq_pct(assets: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in total assets."""
    return _qoq_pct(assets)


def fmo_ext_011_ebit_qoq_pct(ebitda: pd.Series) -> pd.Series:
    """Quarter-over-quarter percentage change in EBITDA (EBIT proxy)."""
    return _qoq_pct(ebitda)


def fmo_ext_012_revenue_qoq_pct_smoothed_4q(revenue: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of revenue QoQ percentage change (smoothed growth)."""
    return _rolling_mean(_qoq_pct(revenue), _TD_YEAR)


# --- Group B (013-024): YoY percentage growth rates ---

def fmo_ext_013_revenue_yoy_pct(revenue: pd.Series) -> pd.Series:
    """Year-over-year percentage change in revenue."""
    return _yoy_pct(revenue)


def fmo_ext_014_netinc_yoy_pct(netinc: pd.Series) -> pd.Series:
    """Year-over-year percentage change in net income."""
    return _yoy_pct(netinc)


def fmo_ext_015_eps_yoy_pct(eps: pd.Series) -> pd.Series:
    """Year-over-year percentage change in EPS."""
    return _yoy_pct(eps)


def fmo_ext_016_gp_yoy_pct(gp: pd.Series) -> pd.Series:
    """Year-over-year percentage change in gross profit."""
    return _yoy_pct(gp)


def fmo_ext_017_opinc_yoy_pct(opinc: pd.Series) -> pd.Series:
    """Year-over-year percentage change in operating income."""
    return _yoy_pct(opinc)


def fmo_ext_018_ebitda_yoy_pct(ebitda: pd.Series) -> pd.Series:
    """Year-over-year percentage change in EBITDA."""
    return _yoy_pct(ebitda)


def fmo_ext_019_fcf_yoy_pct(fcf: pd.Series) -> pd.Series:
    """Year-over-year percentage change in free cash flow."""
    return _yoy_pct(fcf)


def fmo_ext_020_ncfo_yoy_pct(ncfo: pd.Series) -> pd.Series:
    """Year-over-year percentage change in operating cash flow."""
    return _yoy_pct(ncfo)


def fmo_ext_021_equity_yoy_pct(equity: pd.Series) -> pd.Series:
    """Year-over-year percentage change in shareholders equity."""
    return _yoy_pct(equity)


def fmo_ext_022_assets_yoy_pct(assets: pd.Series) -> pd.Series:
    """Year-over-year percentage change in total assets."""
    return _yoy_pct(assets)


def fmo_ext_023_ebit_yoy_pct(ebitda: pd.Series) -> pd.Series:
    """Year-over-year percentage change in EBITDA (EBIT proxy)."""
    return _yoy_pct(ebitda)


def fmo_ext_024_revenue_2y_pct(revenue: pd.Series) -> pd.Series:
    """Two-year (504-day) percentage change in revenue — multi-year momentum."""
    prev = revenue.shift(_TD_2Y)
    return _safe_div_abs(revenue - prev, prev)


# --- Group C (025-036): Momentum acceleration / deceleration ---

def fmo_ext_025_revenue_growth_acceleration(revenue: pd.Series) -> pd.Series:
    """Change in revenue QoQ growth vs the prior quarter's QoQ growth (acceleration)."""
    g = _qoq_pct(revenue)
    return g - g.shift(_TD_QTR)


def fmo_ext_026_netinc_growth_acceleration(netinc: pd.Series) -> pd.Series:
    """Change in net income QoQ growth vs the prior quarter's QoQ growth."""
    g = _qoq_pct(netinc)
    return g - g.shift(_TD_QTR)


def fmo_ext_027_eps_growth_acceleration(eps: pd.Series) -> pd.Series:
    """Change in EPS QoQ growth vs the prior quarter's QoQ growth."""
    g = _qoq_pct(eps)
    return g - g.shift(_TD_QTR)


def fmo_ext_028_ebitda_growth_acceleration(ebitda: pd.Series) -> pd.Series:
    """Change in EBITDA QoQ growth vs the prior quarter's QoQ growth."""
    g = _qoq_pct(ebitda)
    return g - g.shift(_TD_QTR)


def fmo_ext_029_revenue_slope_acceleration(revenue: pd.Series) -> pd.Series:
    """QoQ change in the 4q OLS slope of revenue — slope acceleration."""
    sl = _rolling_slope(revenue, _TD_YEAR)
    return sl - sl.shift(_TD_QTR)


def fmo_ext_030_netinc_slope_acceleration(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4q OLS slope of net income — slope acceleration."""
    sl = _rolling_slope(netinc, _TD_YEAR)
    return sl - sl.shift(_TD_QTR)


def fmo_ext_031_eps_slope_acceleration(eps: pd.Series) -> pd.Series:
    """QoQ change in the 4q OLS slope of EPS — slope acceleration."""
    sl = _rolling_slope(eps, _TD_YEAR)
    return sl - sl.shift(_TD_QTR)


def fmo_ext_032_revenue_qoq_minus_yoy(revenue: pd.Series) -> pd.Series:
    """Revenue QoQ growth minus YoY growth — short- vs long-horizon momentum gap."""
    return _qoq_pct(revenue) - _yoy_pct(revenue)


def fmo_ext_033_netinc_qoq_minus_yoy(netinc: pd.Series) -> pd.Series:
    """Net income QoQ growth minus YoY growth — momentum-horizon gap."""
    return _qoq_pct(netinc) - _yoy_pct(netinc)


def fmo_ext_034_eps_qoq_minus_yoy(eps: pd.Series) -> pd.Series:
    """EPS QoQ growth minus YoY growth — momentum-horizon gap."""
    return _qoq_pct(eps) - _yoy_pct(eps)


def fmo_ext_035_revenue_slope_4q_minus_8q(revenue: pd.Series) -> pd.Series:
    """Revenue 4q OLS slope minus its 8q OLS slope — momentum-horizon divergence."""
    return _rolling_slope(revenue, _TD_YEAR) - _rolling_slope(revenue, _TD_2Y)


def fmo_ext_036_netinc_slope_4q_minus_8q(netinc: pd.Series) -> pd.Series:
    """Net income 4q OLS slope minus its 8q OLS slope — momentum-horizon divergence."""
    return _rolling_slope(netinc, _TD_YEAR) - _rolling_slope(netinc, _TD_2Y)


# --- Group D (037-048): Normalized slope and distance-from-extreme momentum ---

def fmo_ext_037_revenue_slope_norm_4q(revenue: pd.Series) -> pd.Series:
    """Revenue 4q OLS slope normalized by its 4q mean level — scale-free slope."""
    return _safe_div_abs(_rolling_slope(revenue, _TD_YEAR), _rolling_mean(revenue, _TD_YEAR))


def fmo_ext_038_netinc_slope_norm_4q(netinc: pd.Series) -> pd.Series:
    """Net income 4q OLS slope normalized by its 4q mean level."""
    return _safe_div_abs(_rolling_slope(netinc, _TD_YEAR), _rolling_mean(netinc, _TD_YEAR))


def fmo_ext_039_eps_slope_norm_4q(eps: pd.Series) -> pd.Series:
    """EPS 4q OLS slope normalized by its 4q mean level."""
    return _safe_div_abs(_rolling_slope(eps, _TD_YEAR), _rolling_mean(eps, _TD_YEAR))


def fmo_ext_040_ebitda_slope_norm_4q(ebitda: pd.Series) -> pd.Series:
    """EBITDA 4q OLS slope normalized by its 4q mean level."""
    return _safe_div_abs(_rolling_slope(ebitda, _TD_YEAR), _rolling_mean(ebitda, _TD_YEAR))


def fmo_ext_041_revenue_dist_below_8q_max(revenue: pd.Series) -> pd.Series:
    """Trailing 8q maximum minus current revenue (distance below the 2-year peak)."""
    return _rolling_max(revenue, _TD_2Y) - revenue


def fmo_ext_042_netinc_dist_below_8q_max(netinc: pd.Series) -> pd.Series:
    """Trailing 8q maximum minus current net income (distance below the 2-year peak)."""
    return _rolling_max(netinc, _TD_2Y) - netinc


def fmo_ext_043_revenue_drawdown_pct_8q(revenue: pd.Series) -> pd.Series:
    """Revenue drawdown from its trailing 8q peak as a fraction of that peak."""
    peak = _rolling_max(revenue, _TD_2Y)
    return _safe_div_abs(revenue - peak, peak)


def fmo_ext_044_netinc_drawdown_pct_8q(netinc: pd.Series) -> pd.Series:
    """Net income drawdown from its trailing 8q peak as a fraction of that peak."""
    peak = _rolling_max(netinc, _TD_2Y)
    return _safe_div_abs(netinc - peak, peak)


def fmo_ext_045_eps_drawdown_pct_8q(eps: pd.Series) -> pd.Series:
    """EPS drawdown from its trailing 8q peak as a fraction of that peak."""
    peak = _rolling_max(eps, _TD_2Y)
    return _safe_div_abs(eps - peak, peak)


def fmo_ext_046_revenue_dist_above_8q_min(revenue: pd.Series) -> pd.Series:
    """Current revenue minus its trailing 8q minimum (distance above the 2-year trough)."""
    return revenue - _rolling_min(revenue, _TD_2Y)


def fmo_ext_047_netinc_at_3y_low_flag(netinc: pd.Series) -> pd.Series:
    """Binary flag: net income at or below its trailing 3-year rolling minimum."""
    return (netinc <= _rolling_min(netinc, _TD_3Y)).astype(float)


def fmo_ext_048_revenue_at_3y_low_flag(revenue: pd.Series) -> pd.Series:
    """Binary flag: revenue at or below its trailing 3-year rolling minimum."""
    return (revenue <= _rolling_min(revenue, _TD_3Y)).astype(float)


# --- Group E (049-060): YoY streaks, deterioration counts, EWM-cross momentum ---

def fmo_ext_049_revenue_yoy_positive_streak(revenue: pd.Series) -> pd.Series:
    """Consecutive daily steps revenue has shown a positive YoY change."""
    return _streak_true(revenue > revenue.shift(_TD_YEAR))


def fmo_ext_050_netinc_yoy_positive_streak(netinc: pd.Series) -> pd.Series:
    """Consecutive daily steps net income has shown a positive YoY change."""
    return _streak_true(netinc > netinc.shift(_TD_YEAR))


def fmo_ext_051_revenue_qoq_negative_streak(revenue: pd.Series) -> pd.Series:
    """Consecutive daily steps revenue has shown a negative QoQ change (deterioration run)."""
    return _streak_true(revenue < revenue.shift(_TD_QTR))


def fmo_ext_052_netinc_qoq_negative_streak(netinc: pd.Series) -> pd.Series:
    """Consecutive daily steps net income has shown a negative QoQ change."""
    return _streak_true(netinc < netinc.shift(_TD_QTR))


def fmo_ext_053_eps_qoq_negative_streak(eps: pd.Series) -> pd.Series:
    """Consecutive daily steps EPS has shown a negative QoQ change."""
    return _streak_true(eps < eps.shift(_TD_QTR))


def fmo_ext_054_revenue_qoq_negative_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of days in trailing 8q with a negative QoQ revenue change."""
    return _rolling_sum((revenue < revenue.shift(_TD_QTR)).astype(float), _TD_2Y)


def fmo_ext_055_netinc_qoq_negative_count_8q(netinc: pd.Series) -> pd.Series:
    """Count of days in trailing 8q with a negative QoQ net income change."""
    return _rolling_sum((netinc < netinc.shift(_TD_QTR)).astype(float), _TD_2Y)


def fmo_ext_056_revenue_ewm_cross_momentum(revenue: pd.Series) -> pd.Series:
    """Fast minus slow EWM of revenue (span 63 vs 252) — EWM-crossover momentum."""
    return _ewm_mean(revenue, _TD_QTR) - _ewm_mean(revenue, _TD_YEAR)


def fmo_ext_057_netinc_ewm_cross_momentum(netinc: pd.Series) -> pd.Series:
    """Fast minus slow EWM of net income (span 63 vs 252) — EWM-crossover momentum."""
    return _ewm_mean(netinc, _TD_QTR) - _ewm_mean(netinc, _TD_YEAR)


def fmo_ext_058_eps_ewm_cross_momentum(eps: pd.Series) -> pd.Series:
    """Fast minus slow EWM of EPS (span 63 vs 252) — EWM-crossover momentum."""
    return _ewm_mean(eps, _TD_QTR) - _ewm_mean(eps, _TD_YEAR)


def fmo_ext_059_ebitda_ewm_cross_momentum(ebitda: pd.Series) -> pd.Series:
    """Fast minus slow EWM of EBITDA (span 63 vs 252) — EWM-crossover momentum."""
    return _ewm_mean(ebitda, _TD_QTR) - _ewm_mean(ebitda, _TD_YEAR)


def fmo_ext_060_revenue_below_8q_avg_flag(revenue: pd.Series) -> pd.Series:
    """Binary flag: revenue below its trailing 8-quarter mean (sub-trend regime)."""
    return (revenue < _rolling_mean(revenue, _TD_2Y)).astype(float)


# --- Group F (061-068): Growth-rate z-scores, ranks, and stability ---

def fmo_ext_061_revenue_growth_zscore_3y(revenue: pd.Series) -> pd.Series:
    """Z-score of revenue QoQ growth within a trailing 3-year window."""
    return _zscore_rolling(_qoq_pct(revenue), _TD_3Y)


def fmo_ext_062_netinc_growth_zscore_3y(netinc: pd.Series) -> pd.Series:
    """Z-score of net income QoQ growth within a trailing 3-year window."""
    return _zscore_rolling(_qoq_pct(netinc), _TD_3Y)


def fmo_ext_063_eps_growth_zscore_3y(eps: pd.Series) -> pd.Series:
    """Z-score of EPS QoQ growth within a trailing 3-year window."""
    return _zscore_rolling(_qoq_pct(eps), _TD_3Y)


def fmo_ext_064_revenue_growth_pct_rank_3y(revenue: pd.Series) -> pd.Series:
    """Percentile rank of revenue QoQ growth within a trailing 3-year window."""
    return _rolling_rank_pct(_qoq_pct(revenue), _TD_3Y)


def fmo_ext_065_netinc_growth_pct_rank_3y(netinc: pd.Series) -> pd.Series:
    """Percentile rank of net income QoQ growth within a trailing 3-year window."""
    return _rolling_rank_pct(_qoq_pct(netinc), _TD_3Y)


def fmo_ext_066_revenue_slope_pct_rank_3y(revenue: pd.Series) -> pd.Series:
    """Percentile rank of the revenue 4q OLS slope within a trailing 3-year window."""
    return _rolling_rank_pct(_rolling_slope(revenue, _TD_YEAR), _TD_3Y)


def fmo_ext_067_netinc_slope_pct_rank_3y(netinc: pd.Series) -> pd.Series:
    """Percentile rank of the net income 4q OLS slope within a trailing 3-year window."""
    return _rolling_rank_pct(_rolling_slope(netinc, _TD_YEAR), _TD_3Y)


def fmo_ext_068_revenue_growth_stability_8q(revenue: pd.Series) -> pd.Series:
    """Std of revenue QoQ growth over trailing 8 quarters — growth-rate instability."""
    return _rolling_std(_qoq_pct(revenue), _TD_2Y)


# --- Group G (069-075): Multi-metric momentum composites and capitulation flags ---

def fmo_ext_069_breadth_qoq_growth_avg(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
) -> pd.Series:
    """Average QoQ percentage growth across six income-statement metrics."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda]
    total = None
    for m in metrics:
        g = _qoq_pct(m)
        total = g if total is None else total + g
    return total / 6.0


def fmo_ext_070_breadth_yoy_growth_avg(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
) -> pd.Series:
    """Average YoY percentage growth across six income-statement metrics."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda]
    total = None
    for m in metrics:
        g = _yoy_pct(m)
        total = g if total is None else total + g
    return total / 6.0


def fmo_ext_071_count_metrics_below_8q_avg(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series,
) -> pd.Series:
    """Count of core metrics currently below their trailing 8-quarter mean (0-10)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    cnt = None
    for m in metrics:
        flag = (m < _rolling_mean(m, _TD_2Y)).astype(float)
        cnt = flag if cnt is None else cnt + flag
    return cnt


def fmo_ext_072_count_metrics_at_3y_low(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series,
) -> pd.Series:
    """Count of core metrics currently at a trailing 3-year (756-day) rolling minimum (0-10)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    cnt = None
    for m in metrics:
        flag = (m <= _rolling_min(m, _TD_3Y)).astype(float)
        cnt = flag if cnt is None else cnt + flag
    return cnt


def fmo_ext_073_composite_growth_zscore_index(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
) -> pd.Series:
    """Composite momentum index: mean 3-year z-score of QoQ growth across six metrics."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda]
    total = None
    for m in metrics:
        z = _zscore_rolling(_qoq_pct(m), _TD_3Y)
        total = z if total is None else total + z
    return total / 6.0


def fmo_ext_074_broad_deterioration_flag(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series,
) -> pd.Series:
    """Binary flag: at least 8 of 10 core metrics show negative QoQ change (broad deterioration)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    cnt = None
    for m in metrics:
        flag = (m < m.shift(_TD_QTR)).astype(float)
        cnt = flag if cnt is None else cnt + flag
    return (cnt >= 8.0).astype(float)


def fmo_ext_075_capitulation_momentum_score(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
) -> pd.Series:
    """Capitulation momentum score: inverse 3y pct-rank of revenue + netinc + eps QoQ growth.
    Higher = momentum at a multi-year low across the three core metrics."""
    r_rev = _rolling_rank_pct(_qoq_pct(revenue), _TD_3Y)
    r_ni = _rolling_rank_pct(_qoq_pct(netinc), _TD_3Y)
    r_eps = _rolling_rank_pct(_qoq_pct(eps), _TD_3Y)
    return ((1.0 - r_rev.fillna(0.5))
            + (1.0 - r_ni.fillna(0.5))
            + (1.0 - r_eps.fillna(0.5)))


# ── Registry 001-075 ──────────────────────────────────────────────────────────

FUNDAMENTAL_MOMENTUM_EXTENDED_REGISTRY_001_075 = {
    "fmo_ext_001_revenue_qoq_pct": {"inputs": ["revenue"], "func": fmo_ext_001_revenue_qoq_pct},
    "fmo_ext_002_netinc_qoq_pct": {"inputs": ["netinc"], "func": fmo_ext_002_netinc_qoq_pct},
    "fmo_ext_003_eps_qoq_pct": {"inputs": ["eps"], "func": fmo_ext_003_eps_qoq_pct},
    "fmo_ext_004_gp_qoq_pct": {"inputs": ["gp"], "func": fmo_ext_004_gp_qoq_pct},
    "fmo_ext_005_opinc_qoq_pct": {"inputs": ["opinc"], "func": fmo_ext_005_opinc_qoq_pct},
    "fmo_ext_006_ebitda_qoq_pct": {"inputs": ["ebitda"], "func": fmo_ext_006_ebitda_qoq_pct},
    "fmo_ext_007_fcf_qoq_pct": {"inputs": ["fcf"], "func": fmo_ext_007_fcf_qoq_pct},
    "fmo_ext_008_ncfo_qoq_pct": {"inputs": ["ncfo"], "func": fmo_ext_008_ncfo_qoq_pct},
    "fmo_ext_009_equity_qoq_pct": {"inputs": ["equity"], "func": fmo_ext_009_equity_qoq_pct},
    "fmo_ext_010_assets_qoq_pct": {"inputs": ["assets"], "func": fmo_ext_010_assets_qoq_pct},
    "fmo_ext_011_ebit_qoq_pct": {"inputs": ["ebitda"], "func": fmo_ext_011_ebit_qoq_pct},
    "fmo_ext_012_revenue_qoq_pct_smoothed_4q": {"inputs": ["revenue"], "func": fmo_ext_012_revenue_qoq_pct_smoothed_4q},
    "fmo_ext_013_revenue_yoy_pct": {"inputs": ["revenue"], "func": fmo_ext_013_revenue_yoy_pct},
    "fmo_ext_014_netinc_yoy_pct": {"inputs": ["netinc"], "func": fmo_ext_014_netinc_yoy_pct},
    "fmo_ext_015_eps_yoy_pct": {"inputs": ["eps"], "func": fmo_ext_015_eps_yoy_pct},
    "fmo_ext_016_gp_yoy_pct": {"inputs": ["gp"], "func": fmo_ext_016_gp_yoy_pct},
    "fmo_ext_017_opinc_yoy_pct": {"inputs": ["opinc"], "func": fmo_ext_017_opinc_yoy_pct},
    "fmo_ext_018_ebitda_yoy_pct": {"inputs": ["ebitda"], "func": fmo_ext_018_ebitda_yoy_pct},
    "fmo_ext_019_fcf_yoy_pct": {"inputs": ["fcf"], "func": fmo_ext_019_fcf_yoy_pct},
    "fmo_ext_020_ncfo_yoy_pct": {"inputs": ["ncfo"], "func": fmo_ext_020_ncfo_yoy_pct},
    "fmo_ext_021_equity_yoy_pct": {"inputs": ["equity"], "func": fmo_ext_021_equity_yoy_pct},
    "fmo_ext_022_assets_yoy_pct": {"inputs": ["assets"], "func": fmo_ext_022_assets_yoy_pct},
    "fmo_ext_023_ebit_yoy_pct": {"inputs": ["ebitda"], "func": fmo_ext_023_ebit_yoy_pct},
    "fmo_ext_024_revenue_2y_pct": {"inputs": ["revenue"], "func": fmo_ext_024_revenue_2y_pct},
    "fmo_ext_025_revenue_growth_acceleration": {"inputs": ["revenue"], "func": fmo_ext_025_revenue_growth_acceleration},
    "fmo_ext_026_netinc_growth_acceleration": {"inputs": ["netinc"], "func": fmo_ext_026_netinc_growth_acceleration},
    "fmo_ext_027_eps_growth_acceleration": {"inputs": ["eps"], "func": fmo_ext_027_eps_growth_acceleration},
    "fmo_ext_028_ebitda_growth_acceleration": {"inputs": ["ebitda"], "func": fmo_ext_028_ebitda_growth_acceleration},
    "fmo_ext_029_revenue_slope_acceleration": {"inputs": ["revenue"], "func": fmo_ext_029_revenue_slope_acceleration},
    "fmo_ext_030_netinc_slope_acceleration": {"inputs": ["netinc"], "func": fmo_ext_030_netinc_slope_acceleration},
    "fmo_ext_031_eps_slope_acceleration": {"inputs": ["eps"], "func": fmo_ext_031_eps_slope_acceleration},
    "fmo_ext_032_revenue_qoq_minus_yoy": {"inputs": ["revenue"], "func": fmo_ext_032_revenue_qoq_minus_yoy},
    "fmo_ext_033_netinc_qoq_minus_yoy": {"inputs": ["netinc"], "func": fmo_ext_033_netinc_qoq_minus_yoy},
    "fmo_ext_034_eps_qoq_minus_yoy": {"inputs": ["eps"], "func": fmo_ext_034_eps_qoq_minus_yoy},
    "fmo_ext_035_revenue_slope_4q_minus_8q": {"inputs": ["revenue"], "func": fmo_ext_035_revenue_slope_4q_minus_8q},
    "fmo_ext_036_netinc_slope_4q_minus_8q": {"inputs": ["netinc"], "func": fmo_ext_036_netinc_slope_4q_minus_8q},
    "fmo_ext_037_revenue_slope_norm_4q": {"inputs": ["revenue"], "func": fmo_ext_037_revenue_slope_norm_4q},
    "fmo_ext_038_netinc_slope_norm_4q": {"inputs": ["netinc"], "func": fmo_ext_038_netinc_slope_norm_4q},
    "fmo_ext_039_eps_slope_norm_4q": {"inputs": ["eps"], "func": fmo_ext_039_eps_slope_norm_4q},
    "fmo_ext_040_ebitda_slope_norm_4q": {"inputs": ["ebitda"], "func": fmo_ext_040_ebitda_slope_norm_4q},
    "fmo_ext_041_revenue_dist_below_8q_max": {"inputs": ["revenue"], "func": fmo_ext_041_revenue_dist_below_8q_max},
    "fmo_ext_042_netinc_dist_below_8q_max": {"inputs": ["netinc"], "func": fmo_ext_042_netinc_dist_below_8q_max},
    "fmo_ext_043_revenue_drawdown_pct_8q": {"inputs": ["revenue"], "func": fmo_ext_043_revenue_drawdown_pct_8q},
    "fmo_ext_044_netinc_drawdown_pct_8q": {"inputs": ["netinc"], "func": fmo_ext_044_netinc_drawdown_pct_8q},
    "fmo_ext_045_eps_drawdown_pct_8q": {"inputs": ["eps"], "func": fmo_ext_045_eps_drawdown_pct_8q},
    "fmo_ext_046_revenue_dist_above_8q_min": {"inputs": ["revenue"], "func": fmo_ext_046_revenue_dist_above_8q_min},
    "fmo_ext_047_netinc_at_3y_low_flag": {"inputs": ["netinc"], "func": fmo_ext_047_netinc_at_3y_low_flag},
    "fmo_ext_048_revenue_at_3y_low_flag": {"inputs": ["revenue"], "func": fmo_ext_048_revenue_at_3y_low_flag},
    "fmo_ext_049_revenue_yoy_positive_streak": {"inputs": ["revenue"], "func": fmo_ext_049_revenue_yoy_positive_streak},
    "fmo_ext_050_netinc_yoy_positive_streak": {"inputs": ["netinc"], "func": fmo_ext_050_netinc_yoy_positive_streak},
    "fmo_ext_051_revenue_qoq_negative_streak": {"inputs": ["revenue"], "func": fmo_ext_051_revenue_qoq_negative_streak},
    "fmo_ext_052_netinc_qoq_negative_streak": {"inputs": ["netinc"], "func": fmo_ext_052_netinc_qoq_negative_streak},
    "fmo_ext_053_eps_qoq_negative_streak": {"inputs": ["eps"], "func": fmo_ext_053_eps_qoq_negative_streak},
    "fmo_ext_054_revenue_qoq_negative_count_8q": {"inputs": ["revenue"], "func": fmo_ext_054_revenue_qoq_negative_count_8q},
    "fmo_ext_055_netinc_qoq_negative_count_8q": {"inputs": ["netinc"], "func": fmo_ext_055_netinc_qoq_negative_count_8q},
    "fmo_ext_056_revenue_ewm_cross_momentum": {"inputs": ["revenue"], "func": fmo_ext_056_revenue_ewm_cross_momentum},
    "fmo_ext_057_netinc_ewm_cross_momentum": {"inputs": ["netinc"], "func": fmo_ext_057_netinc_ewm_cross_momentum},
    "fmo_ext_058_eps_ewm_cross_momentum": {"inputs": ["eps"], "func": fmo_ext_058_eps_ewm_cross_momentum},
    "fmo_ext_059_ebitda_ewm_cross_momentum": {"inputs": ["ebitda"], "func": fmo_ext_059_ebitda_ewm_cross_momentum},
    "fmo_ext_060_revenue_below_8q_avg_flag": {"inputs": ["revenue"], "func": fmo_ext_060_revenue_below_8q_avg_flag},
    "fmo_ext_061_revenue_growth_zscore_3y": {"inputs": ["revenue"], "func": fmo_ext_061_revenue_growth_zscore_3y},
    "fmo_ext_062_netinc_growth_zscore_3y": {"inputs": ["netinc"], "func": fmo_ext_062_netinc_growth_zscore_3y},
    "fmo_ext_063_eps_growth_zscore_3y": {"inputs": ["eps"], "func": fmo_ext_063_eps_growth_zscore_3y},
    "fmo_ext_064_revenue_growth_pct_rank_3y": {"inputs": ["revenue"], "func": fmo_ext_064_revenue_growth_pct_rank_3y},
    "fmo_ext_065_netinc_growth_pct_rank_3y": {"inputs": ["netinc"], "func": fmo_ext_065_netinc_growth_pct_rank_3y},
    "fmo_ext_066_revenue_slope_pct_rank_3y": {"inputs": ["revenue"], "func": fmo_ext_066_revenue_slope_pct_rank_3y},
    "fmo_ext_067_netinc_slope_pct_rank_3y": {"inputs": ["netinc"], "func": fmo_ext_067_netinc_slope_pct_rank_3y},
    "fmo_ext_068_revenue_growth_stability_8q": {"inputs": ["revenue"], "func": fmo_ext_068_revenue_growth_stability_8q},
    "fmo_ext_069_breadth_qoq_growth_avg": {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda"], "func": fmo_ext_069_breadth_qoq_growth_avg},
    "fmo_ext_070_breadth_yoy_growth_avg": {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda"], "func": fmo_ext_070_breadth_yoy_growth_avg},
    "fmo_ext_071_count_metrics_below_8q_avg": {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"], "func": fmo_ext_071_count_metrics_below_8q_avg},
    "fmo_ext_072_count_metrics_at_3y_low": {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"], "func": fmo_ext_072_count_metrics_at_3y_low},
    "fmo_ext_073_composite_growth_zscore_index": {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda"], "func": fmo_ext_073_composite_growth_zscore_index},
    "fmo_ext_074_broad_deterioration_flag": {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"], "func": fmo_ext_074_broad_deterioration_flag},
    "fmo_ext_075_capitulation_momentum_score": {"inputs": ["revenue", "netinc", "eps"], "func": fmo_ext_075_capitulation_momentum_score},
}
