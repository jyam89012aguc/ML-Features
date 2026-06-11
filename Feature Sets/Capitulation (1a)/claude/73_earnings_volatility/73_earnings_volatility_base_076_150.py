"""
73_earnings_volatility — Base Features 076-150
Domain: instability / variance of the earnings series — volatility-of-volatility,
        margin dispersion, residual variance around trend, unpredictability metrics,
        rising-volatility trend signals, and multi-series dispersion composites.
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
days, 1 year = 252 trading days.  All feature functions in this file look
strictly backward.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(2, span // 4)).std()


def _qoq_diff(s: pd.Series) -> pd.Series:
    return s - s.shift(_TD_QTR)


def _yoy_diff(s: pd.Series) -> pd.Series:
    return s - s.shift(_TD_YEAR)


def _cv(s: pd.Series, w: int) -> pd.Series:
    return _safe_div_abs(_rolling_std(s, w), _rolling_mean(s, w))


def _ols_slope(arr: np.ndarray) -> float:
    """Scalar OLS slope for a 1-D array; used in rolling.apply(raw=True)."""
    n = len(arr)
    if n < 2:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = float(((x - xm) ** 2).sum())
    if denom == 0.0:
        return np.nan
    return float(((x - xm) * (arr - ym)).sum() / denom)


def _residual_std(arr: np.ndarray) -> float:
    """
    Scalar: fit linear trend to arr, return std of residuals.
    Used in rolling.apply(raw=True).
    """
    n = len(arr)
    if n < 3:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = float(((x - xm) ** 2).sum())
    if denom == 0.0:
        return float(arr.std()) if arr.std() > 0 else np.nan
    slope = float(((x - xm) * (arr - ym)).sum() / denom)
    intercept = ym - slope * xm
    resid = arr - (slope * x + intercept)
    return float(resid.std())


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-090): Volatility-of-volatility (vol-of-vol) ---

def evl_076_netinc_vol_of_vol_4q_8q(netinc: pd.Series) -> pd.Series:
    """
    Volatility-of-volatility: rolling std of the trailing-4q rolling std of
    net income, computed over an 8q (504-day) outer window.
    """
    inner_vol = _rolling_std(netinc, _TD_YEAR)
    return _rolling_std(inner_vol, _TD_2Y)


def evl_077_netinc_vol_of_vol_4q_12q(netinc: pd.Series) -> pd.Series:
    """Volatility-of-volatility: rolling std of the 4q-std over a 12q outer window."""
    inner_vol = _rolling_std(netinc, _TD_YEAR)
    return _rolling_std(inner_vol, _TD_3Y)


def evl_078_eps_vol_of_vol_4q_8q(eps: pd.Series) -> pd.Series:
    """Volatility-of-volatility of EPS: std of 4q-std over an 8q outer window."""
    inner_vol = _rolling_std(eps, _TD_YEAR)
    return _rolling_std(inner_vol, _TD_2Y)


def evl_079_ebit_vol_of_vol_4q_8q(ebit: pd.Series) -> pd.Series:
    """Volatility-of-volatility of EBIT: std of 4q-std over an 8q outer window."""
    inner_vol = _rolling_std(ebit, _TD_YEAR)
    return _rolling_std(inner_vol, _TD_2Y)


def evl_080_netinc_cv_of_cv_4q_8q(netinc: pd.Series) -> pd.Series:
    """CV-of-CV: rolling std of the 4q CV of net income over an 8q outer window."""
    inner_cv = _cv(netinc, _TD_YEAR)
    return _rolling_std(inner_cv, _TD_2Y)


def evl_081_netinc_ewm_vol_vs_longrun_vol(netinc: pd.Series) -> pd.Series:
    """
    Ratio of short-term (EWM span=63) std to long-term (EWM span=504) std of
    net income — rising ratio indicates increasing instability.
    """
    short_vol = _ewm_std(netinc, _TD_QTR)
    long_vol  = _ewm_std(netinc, _TD_2Y)
    return _safe_div(short_vol, long_vol)


def evl_082_netinc_vol_pct_rank_8q(netinc: pd.Series) -> pd.Series:
    """
    Percentile rank of the current 4q rolling std of net income within its
    own trailing 8q (504-day) window.  High rank = volatility is near its
    recent peak; low rank = volatility is near its recent floor.
    """
    vol = _rolling_std(netinc, _TD_YEAR)
    return vol.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def evl_083_eps_vol_pct_rank_8q(eps: pd.Series) -> pd.Series:
    """
    Percentile rank of the current 4q rolling std of EPS within its own
    trailing 8q (504-day) window.  High rank = EPS volatility near recent peak.
    """
    vol = _rolling_std(eps, _TD_YEAR)
    return vol.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def evl_084_netinc_vol_distance_to_expanding_max(netinc: pd.Series) -> pd.Series:
    """
    Distance of the current 4q rolling std of net income from its all-history
    expanding maximum.  Zero = volatility is at an all-time high; larger positive
    value = further below peak volatility.
    """
    vol = _rolling_std(netinc, _TD_YEAR)
    peak = vol.expanding(min_periods=2).max()
    return vol - peak


def evl_085_netinc_vol_expanding_vs_4q(netinc: pd.Series) -> pd.Series:
    """
    Ratio of trailing-4q std to expanding all-history std of net income.
    > 1 means recent volatility exceeds long-run average.
    """
    short_vol = _rolling_std(netinc, _TD_YEAR)
    long_vol  = netinc.expanding(min_periods=2).std()
    return _safe_div(short_vol, long_vol)


def evl_086_netinc_vol_trend_slope_8q(netinc: pd.Series) -> pd.Series:
    """
    OLS slope of the 4q-rolling-std series over an 8q (504-day) window.
    Positive slope = rising volatility trend.
    """
    vol = _rolling_std(netinc, _TD_YEAR)
    return vol.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(_ols_slope, raw=True)


def evl_087_eps_vol_trend_slope_8q(eps: pd.Series) -> pd.Series:
    """OLS slope of the EPS 4q-rolling-std series over an 8q window."""
    vol = _rolling_std(eps, _TD_YEAR)
    return vol.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(_ols_slope, raw=True)


def evl_088_netinc_high_vol_regime_flag(netinc: pd.Series) -> pd.Series:
    """
    Regime flag: 1 if the current 4q rolling std of net income exceeds its own
    trailing 8q (504-day) 75th percentile (elevated-volatility regime), else 0.
    """
    vol = _rolling_std(netinc, _TD_YEAR)
    q75 = vol.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).quantile(0.75)
    return (vol > q75).astype(float)


def evl_089_ncfo_vol_of_vol_4q_8q(ncfo: pd.Series) -> pd.Series:
    """Volatility-of-volatility of operating cash flow over 4q/8q windows."""
    inner_vol = _rolling_std(ncfo, _TD_YEAR)
    return _rolling_std(inner_vol, _TD_2Y)


def evl_090_ebitda_vol_regime_change_4q(ebitda: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling std of EBITDA."""
    vol = _rolling_std(ebitda, _TD_YEAR)
    return vol - vol.shift(_TD_QTR)


# --- Group H (091-105): Margin dispersion ---

def evl_091_net_margin_std_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of net margin (netinc/revenue) over 4 quarters."""
    margin = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return _rolling_std(margin, _TD_YEAR)


def evl_092_net_margin_std_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of net margin over 8 quarters."""
    margin = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return _rolling_std(margin, _TD_2Y)


def evl_093_net_margin_cv_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """CV of net margin over 4 quarters."""
    margin = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return _cv(margin, _TD_YEAR)


def evl_094_gross_margin_std_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of gross margin (gp/revenue) over 4 quarters."""
    margin = _safe_div(gp, revenue.abs().replace(0, np.nan))
    return _rolling_std(margin, _TD_YEAR)


def evl_095_gross_margin_std_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of gross margin over 8 quarters."""
    margin = _safe_div(gp, revenue.abs().replace(0, np.nan))
    return _rolling_std(margin, _TD_2Y)


def evl_096_op_margin_std_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of operating margin (opinc/revenue) over 4 quarters."""
    margin = _safe_div(opinc, revenue.abs().replace(0, np.nan))
    return _rolling_std(margin, _TD_YEAR)


def evl_097_op_margin_cv_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """CV of operating margin over 4 quarters."""
    margin = _safe_div(opinc, revenue.abs().replace(0, np.nan))
    return _cv(margin, _TD_YEAR)


def evl_098_ebit_margin_std_4q(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of EBIT margin (ebit/revenue) over 4 quarters."""
    margin = _safe_div(ebit, revenue.abs().replace(0, np.nan))
    return _rolling_std(margin, _TD_YEAR)


def evl_099_ebitda_margin_std_4q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of EBITDA margin over 4 quarters."""
    margin = _safe_div(ebitda, revenue.abs().replace(0, np.nan))
    return _rolling_std(margin, _TD_YEAR)


def evl_100_netinc_margin_range_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Range (max - min) of net margin over trailing 4 quarters."""
    margin = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return _rolling_max(margin, _TD_YEAR) - _rolling_min(margin, _TD_YEAR)


def evl_101_gross_margin_range_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Range of gross margin over trailing 4 quarters."""
    margin = _safe_div(gp, revenue.abs().replace(0, np.nan))
    return _rolling_max(margin, _TD_YEAR) - _rolling_min(margin, _TD_YEAR)


def evl_102_op_margin_range_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Range of operating margin over trailing 4 quarters."""
    margin = _safe_div(opinc, revenue.abs().replace(0, np.nan))
    return _rolling_max(margin, _TD_YEAR) - _rolling_min(margin, _TD_YEAR)


def evl_103_margin_stack_dispersion_4q(
    netinc: pd.Series,
    opinc: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """
    Average of the 4q stds of net-margin, op-margin, and gross-margin —
    composite margin instability signal.
    """
    rev_safe = revenue.abs().replace(0, np.nan)
    std_net = _rolling_std(_safe_div(netinc, rev_safe), _TD_YEAR)
    std_op  = _rolling_std(_safe_div(opinc,  rev_safe), _TD_YEAR)
    std_gp  = _rolling_std(_safe_div(gp,     rev_safe), _TD_YEAR)
    return (std_net + std_op + std_gp) / 3.0


def evl_104_ncfo_margin_std_4q(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of operating cash-flow margin (ncfo/revenue) over 4 quarters."""
    margin = _safe_div(ncfo, revenue.abs().replace(0, np.nan))
    return _rolling_std(margin, _TD_YEAR)


def evl_105_ebit_margin_range_8q(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """Range of EBIT margin over 8 quarters."""
    margin = _safe_div(ebit, revenue.abs().replace(0, np.nan))
    return _rolling_max(margin, _TD_2Y) - _rolling_min(margin, _TD_2Y)


# --- Group I (106-120): Residual variance — unpredictability vs trend ---

def evl_106_netinc_resid_std_4q(netinc: pd.Series) -> pd.Series:
    """
    Std of residuals around a linear trend fitted to net income over 4 quarters.
    Measures unpredictability beyond a simple trend.
    """
    return netinc.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def evl_107_netinc_resid_std_8q(netinc: pd.Series) -> pd.Series:
    """Residual std around a linear trend of net income over 8 quarters."""
    return netinc.rolling(_TD_2Y, min_periods=max(3, _TD_2Y // 4)).apply(
        _residual_std, raw=True
    )


def evl_108_eps_resid_std_4q(eps: pd.Series) -> pd.Series:
    """Residual std around a linear trend of EPS over 4 quarters."""
    return eps.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def evl_109_ebit_resid_std_4q(ebit: pd.Series) -> pd.Series:
    """Residual std around a linear trend of EBIT over 4 quarters."""
    return ebit.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def evl_110_ebitda_resid_std_4q(ebitda: pd.Series) -> pd.Series:
    """Residual std around a linear trend of EBITDA over 4 quarters."""
    return ebitda.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def evl_111_opinc_resid_std_4q(opinc: pd.Series) -> pd.Series:
    """Residual std around a linear trend of operating income over 4 quarters."""
    return opinc.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def evl_112_netinc_resid_std_12q(netinc: pd.Series) -> pd.Series:
    """Residual std around a linear trend of net income over 12 quarters."""
    return netinc.rolling(_TD_3Y, min_periods=max(3, _TD_3Y // 4)).apply(
        _residual_std, raw=True
    )


def evl_113_netinc_resid_cv_4q(netinc: pd.Series) -> pd.Series:
    """
    Residual std of net income trend (4q) divided by |rolling mean| —
    normalized unpredictability.
    """
    resid_std = netinc.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )
    return _safe_div_abs(resid_std, _rolling_mean(netinc, _TD_YEAR))


def evl_114_revenue_resid_std_4q(revenue: pd.Series) -> pd.Series:
    """Residual std around a linear trend of revenue over 4 quarters."""
    return revenue.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def evl_115_ncfo_resid_std_4q(ncfo: pd.Series) -> pd.Series:
    """Residual std around a linear trend of operating cash flow over 4 quarters."""
    return ncfo.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def evl_116_gp_resid_std_4q(gp: pd.Series) -> pd.Series:
    """Residual std around a linear trend of gross profit over 4 quarters."""
    return gp.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def evl_117_netinc_resid_vs_total_std_4q(netinc: pd.Series) -> pd.Series:
    """
    Ratio of trend-residual std to total std over 4 quarters.
    High value means earnings are highly unpredictable even accounting for trend.
    """
    resid = netinc.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )
    total = _rolling_std(netinc, _TD_YEAR)
    return _safe_div(resid, total)


def evl_118_eps_resid_std_8q(eps: pd.Series) -> pd.Series:
    """Residual std around a linear trend of EPS over 8 quarters."""
    return eps.rolling(_TD_2Y, min_periods=max(3, _TD_2Y // 4)).apply(
        _residual_std, raw=True
    )


def evl_119_fcf_resid_std_4q(fcf: pd.Series) -> pd.Series:
    """Residual std around a linear trend of free cash flow over 4 quarters."""
    return fcf.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def evl_120_netinc_ewm_resid_std(netinc: pd.Series) -> pd.Series:
    """
    EWM-based unpredictability: std of (netinc - EWM-mean(span=63)) over a
    trailing 4q (252-day) window — short-EWM deviation dispersion.
    """
    trend = _ewm_mean(netinc, _TD_QTR)
    resid = netinc - trend
    return _rolling_std(resid, _TD_YEAR)


# --- Group J (121-135): QoQ pct-swing distribution and large-swing flags ---

def evl_121_netinc_qoq_pct_swing_std_4q(netinc: pd.Series) -> pd.Series:
    """Std of the QoQ percent-change series of net income over 4 quarters."""
    pct = _safe_div_abs(_qoq_diff(netinc), netinc.shift(_TD_QTR))
    return _rolling_std(pct, _TD_YEAR)


def evl_122_netinc_qoq_pct_swing_std_8q(netinc: pd.Series) -> pd.Series:
    """Std of the QoQ percent-change series of net income over 8 quarters."""
    pct = _safe_div_abs(_qoq_diff(netinc), netinc.shift(_TD_QTR))
    return _rolling_std(pct, _TD_2Y)


def evl_123_eps_qoq_pct_swing_std_4q(eps: pd.Series) -> pd.Series:
    """Std of the QoQ percent-change series of EPS over 4 quarters."""
    pct = _safe_div_abs(_qoq_diff(eps), eps.shift(_TD_QTR))
    return _rolling_std(pct, _TD_YEAR)


def evl_124_netinc_large_swing_count_4q(netinc: pd.Series) -> pd.Series:
    """
    Count of quarters in trailing 4q where |QoQ pct change| exceeds 50%.
    Captures frequency of large earnings surprises.
    """
    pct = _safe_div_abs(_qoq_diff(netinc), netinc.shift(_TD_QTR)).abs()
    large = (pct > 0.5).astype(float)
    return _rolling_sum(large, _TD_YEAR)


def evl_125_netinc_large_swing_count_8q(netinc: pd.Series) -> pd.Series:
    """Count of large QoQ swings (|pct|>50%) in trailing 8 quarters."""
    pct = _safe_div_abs(_qoq_diff(netinc), netinc.shift(_TD_QTR)).abs()
    large = (pct > 0.5).astype(float)
    return _rolling_sum(large, _TD_2Y)


def evl_126_eps_large_swing_count_4q(eps: pd.Series) -> pd.Series:
    """Count of large EPS QoQ swings (|pct|>50%) in trailing 4 quarters."""
    pct = _safe_div_abs(_qoq_diff(eps), eps.shift(_TD_QTR)).abs()
    large = (pct > 0.5).astype(float)
    return _rolling_sum(large, _TD_YEAR)


def evl_127_netinc_extreme_swing_4q(netinc: pd.Series) -> pd.Series:
    """Count of QoQ swings where |pct change| > 100% in trailing 4 quarters."""
    pct = _safe_div_abs(_qoq_diff(netinc), netinc.shift(_TD_QTR)).abs()
    extreme = (pct > 1.0).astype(float)
    return _rolling_sum(extreme, _TD_YEAR)


def evl_128_netinc_pos_swing_count_4q(netinc: pd.Series) -> pd.Series:
    """Count of positive QoQ net-income changes in trailing 4 quarters."""
    pos = (_qoq_diff(netinc) > 0).astype(float)
    return _rolling_sum(pos, _TD_YEAR)


def evl_129_netinc_neg_swing_count_4q(netinc: pd.Series) -> pd.Series:
    """Count of negative QoQ net-income changes in trailing 4 quarters."""
    neg = (_qoq_diff(netinc) < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR)


def evl_130_netinc_direction_alternation_4q(netinc: pd.Series) -> pd.Series:
    """
    Fraction of consecutive QoQ steps that alternate sign (up then down or vice versa)
    in trailing 4 quarters — high value = erratic earnings path.
    """
    diff = _qoq_diff(netinc)
    sign_diff = np.sign(diff)
    alternates = (sign_diff != sign_diff.shift(_TD_QTR)).astype(float)
    return _rolling_mean(alternates, _TD_YEAR)


def evl_131_ebit_qoq_pct_swing_std_4q(ebit: pd.Series) -> pd.Series:
    """Std of the QoQ percent-change series of EBIT over 4 quarters."""
    pct = _safe_div_abs(_qoq_diff(ebit), ebit.shift(_TD_QTR))
    return _rolling_std(pct, _TD_YEAR)


def evl_132_ncfo_qoq_pct_swing_std_4q(ncfo: pd.Series) -> pd.Series:
    """Std of the QoQ percent-change series of operating cash flow over 4 quarters."""
    pct = _safe_div_abs(_qoq_diff(ncfo), ncfo.shift(_TD_QTR))
    return _rolling_std(pct, _TD_YEAR)


def evl_133_netinc_max_pos_swing_4q(netinc: pd.Series) -> pd.Series:
    """Maximum positive QoQ swing of net income in trailing 4 quarters."""
    swings = _qoq_diff(netinc)
    pos_swings = swings.clip(lower=0)
    return _rolling_max(pos_swings, _TD_YEAR)


def evl_134_netinc_max_neg_swing_4q(netinc: pd.Series) -> pd.Series:
    """Maximum downward QoQ swing (most negative) of net income in trailing 4 quarters."""
    swings = _qoq_diff(netinc)
    neg_swings = swings.clip(upper=0)
    return _rolling_min(neg_swings, _TD_YEAR)


def evl_135_netinc_swing_asymmetry_4q(netinc: pd.Series) -> pd.Series:
    """
    Asymmetry of QoQ swings: mean(positive swings) + mean(negative swings) over 4q.
    Negative result means downside swings dominate.
    """
    swings = _qoq_diff(netinc)
    pos_mean = _rolling_mean(swings.clip(lower=0), _TD_YEAR)
    neg_mean = _rolling_mean(swings.clip(upper=0), _TD_YEAR)
    return pos_mean + neg_mean


# --- Group K (136-150): Multi-field dispersion and composite instability ---

def evl_136_netinc_vs_ebit_spread_std_4q(netinc: pd.Series, ebit: pd.Series) -> pd.Series:
    """Rolling std of (netinc - ebit) spread over 4 quarters."""
    spread = netinc - ebit
    return _rolling_std(spread, _TD_YEAR)


def evl_137_ebit_vs_ebitda_spread_std_4q(ebit: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Rolling std of (ebit - ebitda) spread over 4 quarters."""
    spread = ebit - ebitda
    return _rolling_std(spread, _TD_YEAR)


def evl_138_ncfo_vs_netinc_spread_std_4q(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """Rolling std of (ncfo - netinc) spread — earnings quality dispersion."""
    spread = ncfo - netinc
    return _rolling_std(spread, _TD_YEAR)


def evl_139_gp_vs_netinc_spread_std_4q(gp: pd.Series, netinc: pd.Series) -> pd.Series:
    """Rolling std of (gp - netinc) spread over 4 quarters."""
    spread = gp - netinc
    return _rolling_std(spread, _TD_YEAR)


def evl_140_netinc_std_ratio_4q_vs_8q(netinc: pd.Series) -> pd.Series:
    """
    Ratio of 4q rolling std to 8q rolling std of net income.
    > 1 means short-term volatility exceeds medium-term volatility.
    """
    std_4q = _rolling_std(netinc, _TD_YEAR)
    std_8q = _rolling_std(netinc, _TD_2Y)
    return _safe_div(std_4q, std_8q)


def evl_141_netinc_std_ratio_8q_vs_12q(netinc: pd.Series) -> pd.Series:
    """Ratio of 8q rolling std to 12q rolling std of net income."""
    std_8q  = _rolling_std(netinc, _TD_2Y)
    std_12q = _rolling_std(netinc, _TD_3Y)
    return _safe_div(std_8q, std_12q)


def evl_142_eps_std_ratio_4q_vs_8q(eps: pd.Series) -> pd.Series:
    """Ratio of EPS 4q std to 8q std."""
    std_4q = _rolling_std(eps, _TD_YEAR)
    std_8q = _rolling_std(eps, _TD_2Y)
    return _safe_div(std_4q, std_8q)


def evl_143_netinc_downside_to_total_std_4q(netinc: pd.Series) -> pd.Series:
    """
    Downside semi-deviation (below zero) divided by total std — fraction of
    total volatility attributable to loss-side variance.
    """
    below = netinc.clip(upper=0)
    downside = _rolling_mean(below ** 2, _TD_YEAR).apply(np.sqrt)
    total = _rolling_std(netinc, _TD_YEAR)
    return _safe_div(downside, total)


def evl_144_eps_downside_to_total_std_4q(eps: pd.Series) -> pd.Series:
    """Downside semi-deviation of EPS divided by total std over 4 quarters."""
    below = eps.clip(upper=0)
    downside = _rolling_mean(below ** 2, _TD_YEAR).apply(np.sqrt)
    total = _rolling_std(eps, _TD_YEAR)
    return _safe_div(downside, total)


def evl_145_multi_field_vol_composite_4q(
    netinc: pd.Series,
    eps: pd.Series,
    ebit: pd.Series,
    ebitda: pd.Series,
) -> pd.Series:
    """
    Composite volatility score: z-score normalized sum of 4q-stds of
    netinc, eps, ebit, ebitda (each normalized to its own expanding std).
    """
    def _z(s):
        v = _rolling_std(s, _TD_YEAR)
        mu = v.expanding(min_periods=2).mean()
        sd = v.expanding(min_periods=2).std()
        return _safe_div(v - mu, sd)
    return (_z(netinc) + _z(eps) + _z(ebit) + _z(ebitda)) / 4.0


def evl_146_netinc_cv_expanding(netinc: pd.Series) -> pd.Series:
    """Expanding (all-history) coefficient of variation of net income."""
    return _safe_div_abs(
        netinc.expanding(min_periods=2).std(),
        netinc.expanding(min_periods=1).mean()
    )


def evl_147_ncfo_vs_netinc_cv_divergence_4q(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    Difference between the 4q CV of ncfo and the 4q CV of netinc.
    High divergence = cash flow and earnings are moving erratically relative
    to each other.
    """
    cv_ncfo = _cv(ncfo, _TD_YEAR).abs()
    cv_ni   = _cv(netinc, _TD_YEAR).abs()
    return cv_ncfo - cv_ni


def evl_148_revenue_cv_vs_netinc_cv_4q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    Ratio of 4q CV of revenue to 4q CV of net income.
    Low ratio (earnings much more volatile than revenue) signals margin instability.
    """
    cv_rev = _cv(revenue, _TD_YEAR).abs()
    cv_ni  = _cv(netinc, _TD_YEAR).abs()
    return _safe_div(cv_rev, cv_ni)


def evl_149_netinc_vol_z_score_expanding(netinc: pd.Series) -> pd.Series:
    """
    Z-score of the current 4q rolling std relative to its own expanding history.
    High positive value = current volatility is extreme vs history.
    """
    vol = _rolling_std(netinc, _TD_YEAR)
    mu  = vol.expanding(min_periods=2).mean()
    sd  = vol.expanding(min_periods=2).std()
    return _safe_div(vol - mu, sd)


def evl_150_earnings_instability_composite_8q(
    netinc: pd.Series,
    eps: pd.Series,
    ebit: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """
    Broad earnings-instability composite: average of 8q CVs of netinc, eps,
    ebit, and ncfo (absolute values), representing multi-field instability.
    """
    cv_ni   = _cv(netinc, _TD_2Y).abs()
    cv_eps  = _cv(eps,    _TD_2Y).abs()
    cv_ebit = _cv(ebit,   _TD_2Y).abs()
    cv_ncfo = _cv(ncfo,   _TD_2Y).abs()
    return (cv_ni + cv_eps + cv_ebit + cv_ncfo) / 4.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

EARNINGS_VOLATILITY_REGISTRY_076_150 = {
    "evl_076_netinc_vol_of_vol_4q_8q":            {"inputs": ["netinc"],                            "func": evl_076_netinc_vol_of_vol_4q_8q},
    "evl_077_netinc_vol_of_vol_4q_12q":           {"inputs": ["netinc"],                            "func": evl_077_netinc_vol_of_vol_4q_12q},
    "evl_078_eps_vol_of_vol_4q_8q":               {"inputs": ["eps"],                               "func": evl_078_eps_vol_of_vol_4q_8q},
    "evl_079_ebit_vol_of_vol_4q_8q":              {"inputs": ["ebit"],                              "func": evl_079_ebit_vol_of_vol_4q_8q},
    "evl_080_netinc_cv_of_cv_4q_8q":              {"inputs": ["netinc"],                            "func": evl_080_netinc_cv_of_cv_4q_8q},
    "evl_081_netinc_ewm_vol_vs_longrun_vol":       {"inputs": ["netinc"],                            "func": evl_081_netinc_ewm_vol_vs_longrun_vol},
    "evl_082_netinc_vol_pct_rank_8q":              {"inputs": ["netinc"],                            "func": evl_082_netinc_vol_pct_rank_8q},
    "evl_083_eps_vol_pct_rank_8q":                 {"inputs": ["eps"],                               "func": evl_083_eps_vol_pct_rank_8q},
    "evl_084_netinc_vol_distance_to_expanding_max": {"inputs": ["netinc"],                           "func": evl_084_netinc_vol_distance_to_expanding_max},
    "evl_085_netinc_vol_expanding_vs_4q":          {"inputs": ["netinc"],                            "func": evl_085_netinc_vol_expanding_vs_4q},
    "evl_086_netinc_vol_trend_slope_8q":           {"inputs": ["netinc"],                            "func": evl_086_netinc_vol_trend_slope_8q},
    "evl_087_eps_vol_trend_slope_8q":              {"inputs": ["eps"],                               "func": evl_087_eps_vol_trend_slope_8q},
    "evl_088_netinc_high_vol_regime_flag":          {"inputs": ["netinc"],                            "func": evl_088_netinc_high_vol_regime_flag},
    "evl_089_ncfo_vol_of_vol_4q_8q":              {"inputs": ["ncfo"],                              "func": evl_089_ncfo_vol_of_vol_4q_8q},
    "evl_090_ebitda_vol_regime_change_4q":         {"inputs": ["ebitda"],                            "func": evl_090_ebitda_vol_regime_change_4q},
    "evl_091_net_margin_std_4q":                   {"inputs": ["netinc", "revenue"],                 "func": evl_091_net_margin_std_4q},
    "evl_092_net_margin_std_8q":                   {"inputs": ["netinc", "revenue"],                 "func": evl_092_net_margin_std_8q},
    "evl_093_net_margin_cv_4q":                    {"inputs": ["netinc", "revenue"],                 "func": evl_093_net_margin_cv_4q},
    "evl_094_gross_margin_std_4q":                 {"inputs": ["gp", "revenue"],                     "func": evl_094_gross_margin_std_4q},
    "evl_095_gross_margin_std_8q":                 {"inputs": ["gp", "revenue"],                     "func": evl_095_gross_margin_std_8q},
    "evl_096_op_margin_std_4q":                    {"inputs": ["opinc", "revenue"],                  "func": evl_096_op_margin_std_4q},
    "evl_097_op_margin_cv_4q":                     {"inputs": ["opinc", "revenue"],                  "func": evl_097_op_margin_cv_4q},
    "evl_098_ebit_margin_std_4q":                  {"inputs": ["ebit", "revenue"],                   "func": evl_098_ebit_margin_std_4q},
    "evl_099_ebitda_margin_std_4q":                {"inputs": ["ebitda", "revenue"],                 "func": evl_099_ebitda_margin_std_4q},
    "evl_100_netinc_margin_range_4q":              {"inputs": ["netinc", "revenue"],                 "func": evl_100_netinc_margin_range_4q},
    "evl_101_gross_margin_range_4q":               {"inputs": ["gp", "revenue"],                     "func": evl_101_gross_margin_range_4q},
    "evl_102_op_margin_range_4q":                  {"inputs": ["opinc", "revenue"],                  "func": evl_102_op_margin_range_4q},
    "evl_103_margin_stack_dispersion_4q":          {"inputs": ["netinc", "opinc", "gp", "revenue"],  "func": evl_103_margin_stack_dispersion_4q},
    "evl_104_ncfo_margin_std_4q":                  {"inputs": ["ncfo", "revenue"],                   "func": evl_104_ncfo_margin_std_4q},
    "evl_105_ebit_margin_range_8q":                {"inputs": ["ebit", "revenue"],                   "func": evl_105_ebit_margin_range_8q},
    "evl_106_netinc_resid_std_4q":                 {"inputs": ["netinc"],                            "func": evl_106_netinc_resid_std_4q},
    "evl_107_netinc_resid_std_8q":                 {"inputs": ["netinc"],                            "func": evl_107_netinc_resid_std_8q},
    "evl_108_eps_resid_std_4q":                    {"inputs": ["eps"],                               "func": evl_108_eps_resid_std_4q},
    "evl_109_ebit_resid_std_4q":                   {"inputs": ["ebit"],                              "func": evl_109_ebit_resid_std_4q},
    "evl_110_ebitda_resid_std_4q":                 {"inputs": ["ebitda"],                            "func": evl_110_ebitda_resid_std_4q},
    "evl_111_opinc_resid_std_4q":                  {"inputs": ["opinc"],                             "func": evl_111_opinc_resid_std_4q},
    "evl_112_netinc_resid_std_12q":                {"inputs": ["netinc"],                            "func": evl_112_netinc_resid_std_12q},
    "evl_113_netinc_resid_cv_4q":                  {"inputs": ["netinc"],                            "func": evl_113_netinc_resid_cv_4q},
    "evl_114_revenue_resid_std_4q":                {"inputs": ["revenue"],                           "func": evl_114_revenue_resid_std_4q},
    "evl_115_ncfo_resid_std_4q":                   {"inputs": ["ncfo"],                              "func": evl_115_ncfo_resid_std_4q},
    "evl_116_gp_resid_std_4q":                     {"inputs": ["gp"],                                "func": evl_116_gp_resid_std_4q},
    "evl_117_netinc_resid_vs_total_std_4q":        {"inputs": ["netinc"],                            "func": evl_117_netinc_resid_vs_total_std_4q},
    "evl_118_eps_resid_std_8q":                    {"inputs": ["eps"],                               "func": evl_118_eps_resid_std_8q},
    "evl_119_fcf_resid_std_4q":                    {"inputs": ["fcf"],                               "func": evl_119_fcf_resid_std_4q},
    "evl_120_netinc_ewm_resid_std":                {"inputs": ["netinc"],                            "func": evl_120_netinc_ewm_resid_std},
    "evl_121_netinc_qoq_pct_swing_std_4q":         {"inputs": ["netinc"],                            "func": evl_121_netinc_qoq_pct_swing_std_4q},
    "evl_122_netinc_qoq_pct_swing_std_8q":         {"inputs": ["netinc"],                            "func": evl_122_netinc_qoq_pct_swing_std_8q},
    "evl_123_eps_qoq_pct_swing_std_4q":            {"inputs": ["eps"],                               "func": evl_123_eps_qoq_pct_swing_std_4q},
    "evl_124_netinc_large_swing_count_4q":         {"inputs": ["netinc"],                            "func": evl_124_netinc_large_swing_count_4q},
    "evl_125_netinc_large_swing_count_8q":         {"inputs": ["netinc"],                            "func": evl_125_netinc_large_swing_count_8q},
    "evl_126_eps_large_swing_count_4q":            {"inputs": ["eps"],                               "func": evl_126_eps_large_swing_count_4q},
    "evl_127_netinc_extreme_swing_4q":             {"inputs": ["netinc"],                            "func": evl_127_netinc_extreme_swing_4q},
    "evl_128_netinc_pos_swing_count_4q":           {"inputs": ["netinc"],                            "func": evl_128_netinc_pos_swing_count_4q},
    "evl_129_netinc_neg_swing_count_4q":           {"inputs": ["netinc"],                            "func": evl_129_netinc_neg_swing_count_4q},
    "evl_130_netinc_direction_alternation_4q":     {"inputs": ["netinc"],                            "func": evl_130_netinc_direction_alternation_4q},
    "evl_131_ebit_qoq_pct_swing_std_4q":           {"inputs": ["ebit"],                              "func": evl_131_ebit_qoq_pct_swing_std_4q},
    "evl_132_ncfo_qoq_pct_swing_std_4q":           {"inputs": ["ncfo"],                              "func": evl_132_ncfo_qoq_pct_swing_std_4q},
    "evl_133_netinc_max_pos_swing_4q":             {"inputs": ["netinc"],                            "func": evl_133_netinc_max_pos_swing_4q},
    "evl_134_netinc_max_neg_swing_4q":             {"inputs": ["netinc"],                            "func": evl_134_netinc_max_neg_swing_4q},
    "evl_135_netinc_swing_asymmetry_4q":           {"inputs": ["netinc"],                            "func": evl_135_netinc_swing_asymmetry_4q},
    "evl_136_netinc_vs_ebit_spread_std_4q":        {"inputs": ["netinc", "ebit"],                    "func": evl_136_netinc_vs_ebit_spread_std_4q},
    "evl_137_ebit_vs_ebitda_spread_std_4q":        {"inputs": ["ebit", "ebitda"],                    "func": evl_137_ebit_vs_ebitda_spread_std_4q},
    "evl_138_ncfo_vs_netinc_spread_std_4q":        {"inputs": ["ncfo", "netinc"],                    "func": evl_138_ncfo_vs_netinc_spread_std_4q},
    "evl_139_gp_vs_netinc_spread_std_4q":          {"inputs": ["gp", "netinc"],                      "func": evl_139_gp_vs_netinc_spread_std_4q},
    "evl_140_netinc_std_ratio_4q_vs_8q":           {"inputs": ["netinc"],                            "func": evl_140_netinc_std_ratio_4q_vs_8q},
    "evl_141_netinc_std_ratio_8q_vs_12q":          {"inputs": ["netinc"],                            "func": evl_141_netinc_std_ratio_8q_vs_12q},
    "evl_142_eps_std_ratio_4q_vs_8q":              {"inputs": ["eps"],                               "func": evl_142_eps_std_ratio_4q_vs_8q},
    "evl_143_netinc_downside_to_total_std_4q":     {"inputs": ["netinc"],                            "func": evl_143_netinc_downside_to_total_std_4q},
    "evl_144_eps_downside_to_total_std_4q":        {"inputs": ["eps"],                               "func": evl_144_eps_downside_to_total_std_4q},
    "evl_145_multi_field_vol_composite_4q":        {"inputs": ["netinc", "eps", "ebit", "ebitda"],   "func": evl_145_multi_field_vol_composite_4q},
    "evl_146_netinc_cv_expanding":                 {"inputs": ["netinc"],                            "func": evl_146_netinc_cv_expanding},
    "evl_147_ncfo_vs_netinc_cv_divergence_4q":     {"inputs": ["ncfo", "netinc"],                    "func": evl_147_ncfo_vs_netinc_cv_divergence_4q},
    "evl_148_revenue_cv_vs_netinc_cv_4q":          {"inputs": ["revenue", "netinc"],                 "func": evl_148_revenue_cv_vs_netinc_cv_4q},
    "evl_149_netinc_vol_z_score_expanding":        {"inputs": ["netinc"],                            "func": evl_149_netinc_vol_z_score_expanding},
    "evl_150_earnings_instability_composite_8q":   {"inputs": ["netinc", "eps", "ebit", "ncfo"],     "func": evl_150_earnings_instability_composite_8q},
}
