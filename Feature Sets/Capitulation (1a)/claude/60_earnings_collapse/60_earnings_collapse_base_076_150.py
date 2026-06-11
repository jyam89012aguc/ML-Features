"""
60_earnings_collapse — Base Features 076-150
Domain: net-income decline, loss onset, magnitude of earnings collapse
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

# --- Group F (076-090): EPS-focused collapse measures ---

def ecl_076_epsdil_yoy_pct(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS YoY percent change."""
    prior = epsdil.shift(_TD_YEAR)
    return _safe_div_abs(epsdil - prior, prior)


def ecl_077_epsdil_2y_pct(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS 2-year percent change."""
    prior = epsdil.shift(_TD_2Y)
    return _safe_div_abs(epsdil - prior, prior)


def ecl_078_epsdil_drawdown_from_4q_peak(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(epsdil, _TD_YEAR)
    return epsdil - peak


def ecl_079_epsdil_drawdown_from_8q_peak(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS drawdown from 8-quarter rolling peak."""
    peak = _rolling_max(epsdil, _TD_2Y)
    return epsdil - peak


def ecl_080_epsdil_pct_drawdown_from_4q_peak(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS percent drawdown from 4-quarter peak."""
    peak = _rolling_max(epsdil, _TD_YEAR)
    return _safe_div_abs(epsdil - peak, peak)


def ecl_081_eps_vs_epsdil_divergence(eps: pd.Series, epsdil: pd.Series) -> pd.Series:
    """Basic EPS minus diluted EPS (dilution drag widening)."""
    return eps - epsdil


def ecl_082_epsdil_consecutive_decline_quarters(epsdil: pd.Series) -> pd.Series:
    """
    Consecutive quarters of YoY diluted EPS decline (QoQ step version).
    Increments each period when epsdil < prior-period epsdil, resets otherwise.
    """
    worse = (epsdil < epsdil.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(worse), dtype=float)
    arr = worse.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=epsdil.index)


def ecl_083_eps_to_revenue_ratio(eps: pd.Series, revenue: pd.Series) -> pd.Series:
    """EPS divided by revenue per share proxy (eps / revenue)."""
    return _safe_div(eps, revenue.abs().replace(0, np.nan))


def ecl_084_epsdil_zscore_4q(epsdil: pd.Series) -> pd.Series:
    """Z-score of diluted EPS within a trailing 4-quarter window."""
    return _zscore_rolling(epsdil, _TD_YEAR)


def ecl_085_epsdil_pct_rank_4q(epsdil: pd.Series) -> pd.Series:
    """Percentile rank of diluted EPS within a trailing 4-quarter window."""
    return _rolling_rank_pct(epsdil, _TD_YEAR)


def ecl_086_eps_expanding_pct_rank(eps: pd.Series) -> pd.Series:
    """Expanding percentile rank of EPS (all-history rank)."""
    return eps.expanding(min_periods=2).rank(pct=True)


def ecl_087_epsdil_expanding_zscore(epsdil: pd.Series) -> pd.Series:
    """Expanding z-score of diluted EPS."""
    m  = epsdil.expanding(min_periods=2).mean()
    sd = epsdil.expanding(min_periods=2).std()
    return _safe_div(epsdil - m, sd)


def ecl_088_eps_qoq_negative_acceleration(eps: pd.Series) -> pd.Series:
    """QoQ change in EPS, clipped at 0 (keeps only deteriorations)."""
    chg = eps - eps.shift(_TD_QTR)
    return chg.clip(upper=0)


def ecl_089_eps_pct_rank_12q(eps: pd.Series) -> pd.Series:
    """Percentile rank of EPS within a trailing 12-quarter (756-day) window.
    Low rank (near 0) signals EPS is at or near a 3-year low."""
    return _rolling_rank_pct(eps, _TD_3Y)


def ecl_090_epsdil_worst_3y(epsdil: pd.Series) -> pd.Series:
    """Worst (minimum) diluted EPS over trailing 3 years."""
    return _rolling_min(epsdil, _TD_3Y)


# --- Group G (091-105): EBIT/EBITDA/EBT collapse measures ---

def ecl_091_ebit_qoq_pct(ebit: pd.Series) -> pd.Series:
    """EBIT QoQ percent change."""
    prior = ebit.shift(_TD_QTR)
    return _safe_div_abs(ebit - prior, prior)


def ecl_092_ebit_yoy_pct(ebit: pd.Series) -> pd.Series:
    """EBIT YoY percent change."""
    prior = ebit.shift(_TD_YEAR)
    return _safe_div_abs(ebit - prior, prior)


def ecl_093_ebitda_yoy_pct(ebitda: pd.Series) -> pd.Series:
    """EBITDA YoY percent change."""
    prior = ebitda.shift(_TD_YEAR)
    return _safe_div_abs(ebitda - prior, prior)


def ecl_094_ebt_yoy_pct(ebt: pd.Series) -> pd.Series:
    """EBT YoY percent change."""
    prior = ebt.shift(_TD_YEAR)
    return _safe_div_abs(ebt - prior, prior)


def ecl_095_ebit_pct_drawdown_from_4q_peak(ebit: pd.Series) -> pd.Series:
    """EBIT percent drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(ebit, _TD_YEAR)
    return _safe_div_abs(ebit - peak, peak)


def ecl_096_ebitda_pct_drawdown_from_4q_peak(ebitda: pd.Series) -> pd.Series:
    """EBITDA percent drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(ebitda, _TD_YEAR)
    return _safe_div_abs(ebitda - peak, peak)


def ecl_097_ebt_pct_drawdown_from_4q_peak(ebt: pd.Series) -> pd.Series:
    """EBT percent drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(ebt, _TD_YEAR)
    return _safe_div_abs(ebt - peak, peak)


def ecl_098_ebit_zscore_8q(ebit: pd.Series) -> pd.Series:
    """Z-score of EBIT within a trailing 8-quarter window."""
    return _zscore_rolling(ebit, _TD_2Y)


def ecl_099_ebitda_zscore_4q(ebitda: pd.Series) -> pd.Series:
    """Z-score of EBITDA within a trailing 4-quarter window."""
    return _zscore_rolling(ebitda, _TD_YEAR)


def ecl_100_ebt_zscore_4q(ebt: pd.Series) -> pd.Series:
    """Z-score of EBT within a trailing 4-quarter window."""
    return _zscore_rolling(ebt, _TD_YEAR)


def ecl_101_ebit_loss_fraction_3y(ebit: pd.Series) -> pd.Series:
    """Fraction of 3-year window where EBIT was negative."""
    return _rolling_mean((ebit < 0).astype(float), _TD_3Y)


def ecl_102_ebitda_loss_fraction_2y(ebitda: pd.Series) -> pd.Series:
    """Fraction of 2-year window where EBITDA was negative."""
    return _rolling_mean((ebitda < 0).astype(float), _TD_2Y)


def ecl_103_ebit_to_netinc_convergence(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    EBIT minus netinc, normalized by abs(EBIT).
    Tracks how much of operating profit is consumed below the line.
    """
    return _safe_div_abs(ebit - netinc, ebit)


def ecl_104_ebitda_to_ebit_gap(ebitda: pd.Series, ebit: pd.Series) -> pd.Series:
    """EBITDA minus EBIT (D&A proxy); large gap can mask operating deterioration."""
    return ebitda - ebit


def ecl_105_ebit_consecutive_decline_streak(ebit: pd.Series) -> pd.Series:
    """Consecutive quarters of EBIT decline (resets on any improvement)."""
    worse = (ebit < ebit.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(worse), dtype=float)
    arr = worse.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=ebit.index)


# --- Group H (106-120): Cumulative earnings, drawdown from cumulative peak ---

def ecl_106_netinc_ttm_zscore_5y(netinc: pd.Series) -> pd.Series:
    """Z-score of TTM net income (4Q rolling sum) within a trailing 5-year (1260-day) window.
    Negative z-score signals TTM earnings are well below their 5-year distribution."""
    ttm = _rolling_sum(netinc, _TD_YEAR)
    return _zscore_rolling(ttm, _TD_5Y)


def ecl_107_netinc_ttm_pct_chg(netinc: pd.Series) -> pd.Series:
    """TTM net income year-over-year percent change."""
    ttm       = _rolling_sum(netinc, _TD_YEAR)
    prior_ttm = ttm.shift(_TD_YEAR)
    return _safe_div_abs(ttm - prior_ttm, prior_ttm)


def ecl_108_netinc_ttm_drawdown_from_peak(netinc: pd.Series) -> pd.Series:
    """TTM net income drawdown from its expanding peak."""
    ttm  = _rolling_sum(netinc, _TD_YEAR)
    peak = ttm.expanding(min_periods=1).max()
    return ttm - peak


def ecl_109_netinc_ttm_pct_drawdown_from_peak(netinc: pd.Series) -> pd.Series:
    """TTM net income percent drawdown from expanding peak."""
    ttm  = _rolling_sum(netinc, _TD_YEAR)
    peak = ttm.expanding(min_periods=1).max()
    return _safe_div_abs(ttm - peak, peak)


def ecl_110_netinc_ttm_is_negative(netinc: pd.Series) -> pd.Series:
    """1 if TTM net income sum is negative."""
    ttm = _rolling_sum(netinc, _TD_YEAR)
    return (ttm < 0).astype(float)


def ecl_111_eps_ttm_sum(eps: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of EPS (TTM EPS proxy)."""
    return _rolling_sum(eps, _TD_YEAR)


def ecl_112_eps_ttm_drawdown_from_peak(eps: pd.Series) -> pd.Series:
    """TTM EPS drawdown from its expanding maximum."""
    ttm_eps = _rolling_sum(eps, _TD_YEAR)
    peak    = ttm_eps.expanding(min_periods=1).max()
    return ttm_eps - peak


def ecl_113_ebit_ttm_sum(ebit: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of EBIT."""
    return _rolling_sum(ebit, _TD_YEAR)


def ecl_114_ebitda_ttm_sum(ebitda: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of EBITDA."""
    return _rolling_sum(ebitda, _TD_YEAR)


def ecl_115_ebit_ttm_drawdown_from_peak(ebit: pd.Series) -> pd.Series:
    """TTM EBIT drawdown from its expanding maximum."""
    ttm_ebit = _rolling_sum(ebit, _TD_YEAR)
    peak     = ttm_ebit.expanding(min_periods=1).max()
    return ttm_ebit - peak


def ecl_116_netinc_2y_sum(netinc: pd.Series) -> pd.Series:
    """Rolling 2-year (504-day) cumulative net income sum."""
    return _rolling_sum(netinc, _TD_2Y)


def ecl_117_netinc_3y_sum(netinc: pd.Series) -> pd.Series:
    """Rolling 3-year (756-day) cumulative net income sum."""
    return _rolling_sum(netinc, _TD_3Y)


def ecl_118_netinccmn_ttm_sum(netinccmn: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of net income common (TTM)."""
    return _rolling_sum(netinccmn, _TD_YEAR)


def ecl_119_netinccmn_ttm_drawdown_from_peak(netinccmn: pd.Series) -> pd.Series:
    """TTM netinccmn drawdown from expanding peak."""
    ttm  = _rolling_sum(netinccmn, _TD_YEAR)
    peak = ttm.expanding(min_periods=1).max()
    return ttm - peak


def ecl_120_ebt_ttm_sum(ebt: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of EBT."""
    return _rolling_sum(ebt, _TD_YEAR)


# --- Group I (121-135): Earnings collapse speed and momentum ---

def ecl_121_netinc_slope_4q(netinc: pd.Series) -> pd.Series:
    """
    OLS slope of net income over the last 4 quarters (252-day window).
    Scalar scalar helper avoids passing np.polyfit to rolling.apply directly.
    """
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

    return netinc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def ecl_122_netinc_slope_8q(netinc: pd.Series) -> pd.Series:
    """OLS slope of net income over the last 8 quarters (504-day window)."""
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

    return netinc.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(_slope, raw=True)


def ecl_123_eps_slope_4q(eps: pd.Series) -> pd.Series:
    """OLS slope of EPS over the last 4 quarters."""
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

    return eps.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def ecl_124_netinc_momentum_qoq_vs_yoy(netinc: pd.Series) -> pd.Series:
    """QoQ change minus YoY change / 4 — short-term momentum vs long-term trend."""
    qoq = netinc - netinc.shift(_TD_QTR)
    yoy = netinc - netinc.shift(_TD_YEAR)
    return qoq - yoy / 4.0


def ecl_125_netinc_at_3y_low_flag(netinc: pd.Series) -> pd.Series:
    """1 if current net income is at or below its trailing 3-year (756-day) minimum.
    Extreme-low regime flag: signals a fresh multi-year earnings trough."""
    hist_min = _rolling_min(netinc, _TD_3Y)
    return (netinc <= hist_min).astype(float)


def ecl_126_eps_deceleration_flag(eps: pd.Series) -> pd.Series:
    """1 when EPS QoQ change deteriorates vs prior quarter's QoQ change."""
    qoq  = eps - eps.shift(_TD_QTR)
    prev = qoq.shift(_TD_QTR)
    return (qoq < prev).astype(float)


def ecl_127_netinc_4q_decline_count(netinc: pd.Series) -> pd.Series:
    """Count of quarters with QoQ net-income decline in trailing 4 quarters."""
    decline = (netinc < netinc.shift(_TD_QTR)).astype(float)
    return _rolling_sum(decline, _TD_YEAR)


def ecl_128_netinc_8q_decline_count(netinc: pd.Series) -> pd.Series:
    """Count of quarters with QoQ net-income decline in trailing 8 quarters."""
    decline = (netinc < netinc.shift(_TD_QTR)).astype(float)
    return _rolling_sum(decline, _TD_2Y)


def ecl_129_eps_4q_decline_count(eps: pd.Series) -> pd.Series:
    """Count of quarters with QoQ EPS decline in trailing 4 quarters."""
    decline = (eps < eps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(decline, _TD_YEAR)


def ecl_130_netinc_max_single_qoq_drop(netinc: pd.Series) -> pd.Series:
    """Worst single QoQ net-income drop (most negative QoQ change) in trailing 8Q."""
    qoq = netinc - netinc.shift(_TD_QTR)
    return _rolling_min(qoq, _TD_2Y)


def ecl_131_netinc_max_single_yoy_drop(netinc: pd.Series) -> pd.Series:
    """Worst single YoY net-income drop in trailing 8Q."""
    yoy = netinc - netinc.shift(_TD_YEAR)
    return _rolling_min(yoy, _TD_2Y)


def ecl_132_eps_max_single_qoq_drop(eps: pd.Series) -> pd.Series:
    """Worst single QoQ EPS drop in trailing 4Q."""
    qoq = eps - eps.shift(_TD_QTR)
    return _rolling_min(qoq, _TD_YEAR)


def ecl_133_netinc_4q_range(netinc: pd.Series) -> pd.Series:
    """Range of net income values over trailing 4 quarters (max - min)."""
    return _rolling_max(netinc, _TD_YEAR) - _rolling_min(netinc, _TD_YEAR)


def ecl_134_netinc_8q_range(netinc: pd.Series) -> pd.Series:
    """Range of net income values over trailing 8 quarters."""
    return _rolling_max(netinc, _TD_2Y) - _rolling_min(netinc, _TD_2Y)


def ecl_135_netinc_volatility_4q(netinc: pd.Series) -> pd.Series:
    """Standard deviation of net income over trailing 4 quarters."""
    return _rolling_std(netinc, _TD_YEAR)


# --- Group J (136-150): Cross-earnings-line comparisons and advanced severity ---

def ecl_136_netinc_to_gp_ratio(netinc: pd.Series, gp: pd.Series) -> pd.Series:
    """Net income divided by gross profit (below-gross conversion rate)."""
    return _safe_div(netinc, gp.abs().replace(0, np.nan))


def ecl_137_netinc_to_ebt_ratio(netinc: pd.Series, ebt: pd.Series) -> pd.Series:
    """Net income divided by EBT (effective tax and extra-item retention)."""
    return _safe_div(netinc, ebt.abs().replace(0, np.nan))


def ecl_138_netinc_to_ebit_ratio(netinc: pd.Series, ebit: pd.Series) -> pd.Series:
    """Net income divided by EBIT."""
    return _safe_div(netinc, ebit.abs().replace(0, np.nan))


def ecl_139_opinc_to_netinc_yoy_divergence(opinc: pd.Series, netinc: pd.Series) -> pd.Series:
    """YoY change in (opinc - netinc) gap; growing gap signals below-line collapse."""
    gap     = opinc - netinc
    gap_1y  = gap.shift(_TD_YEAR)
    return gap - gap_1y


def ecl_140_gp_to_netinc_yoy_divergence(gp: pd.Series, netinc: pd.Series) -> pd.Series:
    """YoY change in (gp - netinc) gap."""
    gap    = gp - netinc
    gap_1y = gap.shift(_TD_YEAR)
    return gap - gap_1y


def ecl_141_netinc_vs_prior_peak_pct_3y(netinc: pd.Series) -> pd.Series:
    """Net income vs its 3-year peak, percent drawdown."""
    peak = _rolling_max(netinc, _TD_3Y)
    return _safe_div_abs(netinc - peak, peak)


def ecl_142_netinc_vs_prior_peak_pct_5y(netinc: pd.Series) -> pd.Series:
    """Net income vs its 5-year peak, percent drawdown."""
    peak = _rolling_max(netinc, _TD_5Y)
    return _safe_div_abs(netinc - peak, peak)


def ecl_143_netinc_at_historical_low_flag(netinc: pd.Series) -> pd.Series:
    """1 if current net income equals its expanding all-history minimum."""
    hist_min = netinc.expanding(min_periods=1).min()
    return (netinc <= hist_min).astype(float)


def ecl_144_eps_at_historical_low_flag(eps: pd.Series) -> pd.Series:
    """1 if current EPS equals its expanding all-history minimum."""
    hist_min = eps.expanding(min_periods=1).min()
    return (eps <= hist_min).astype(float)


def ecl_145_ebit_at_historical_low_flag(ebit: pd.Series) -> pd.Series:
    """1 if current EBIT equals its expanding all-history minimum."""
    hist_min = ebit.expanding(min_periods=1).min()
    return (ebit <= hist_min).astype(float)


def ecl_146_netinc_median_deviation_4q(netinc: pd.Series) -> pd.Series:
    """Net income minus its 4-quarter rolling median."""
    return netinc - _rolling_median(netinc, _TD_YEAR)


def ecl_147_netinc_median_deviation_8q(netinc: pd.Series) -> pd.Series:
    """Net income minus its 8-quarter rolling median."""
    return netinc - _rolling_median(netinc, _TD_2Y)


def ecl_148_netinc_interquartile_position_4q(netinc: pd.Series) -> pd.Series:
    """
    Position of current net income within the 4-quarter IQR:
    (netinc - Q25) / (Q75 - Q25). Zero means at Q25, one means at Q75.
    """
    q75 = netinc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.75)
    q25 = netinc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.25)
    return _safe_div(netinc - q25, q75 - q25)


def ecl_149_netinc_tail_q05_4q(netinc: pd.Series) -> pd.Series:
    """5th percentile of net income over trailing 4-quarter window."""
    return netinc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.05)


def ecl_150_earnings_collapse_severity_index(
    netinc: pd.Series, eps: pd.Series, ebit: pd.Series, ebitda: pd.Series
) -> pd.Series:
    """
    Earnings collapse severity index: equally-weighted sum of four 4Q z-scores
    (netinc, eps, ebit, ebitda).  Negative values signal broad collapse.
    """
    z_ni    = _zscore_rolling(netinc, _TD_YEAR)
    z_eps   = _zscore_rolling(eps,    _TD_YEAR)
    z_ebit  = _zscore_rolling(ebit,   _TD_YEAR)
    z_ebitda = _zscore_rolling(ebitda, _TD_YEAR)
    return (z_ni + z_eps + z_ebit + z_ebitda) / 4.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

EARNINGS_COLLAPSE_REGISTRY_076_150 = {
    "ecl_076_epsdil_yoy_pct":                       {"inputs": ["epsdil"],                              "func": ecl_076_epsdil_yoy_pct},
    "ecl_077_epsdil_2y_pct":                         {"inputs": ["epsdil"],                              "func": ecl_077_epsdil_2y_pct},
    "ecl_078_epsdil_drawdown_from_4q_peak":          {"inputs": ["epsdil"],                              "func": ecl_078_epsdil_drawdown_from_4q_peak},
    "ecl_079_epsdil_drawdown_from_8q_peak":          {"inputs": ["epsdil"],                              "func": ecl_079_epsdil_drawdown_from_8q_peak},
    "ecl_080_epsdil_pct_drawdown_from_4q_peak":      {"inputs": ["epsdil"],                              "func": ecl_080_epsdil_pct_drawdown_from_4q_peak},
    "ecl_081_eps_vs_epsdil_divergence":              {"inputs": ["eps", "epsdil"],                       "func": ecl_081_eps_vs_epsdil_divergence},
    "ecl_082_epsdil_consecutive_decline_quarters":   {"inputs": ["epsdil"],                              "func": ecl_082_epsdil_consecutive_decline_quarters},
    "ecl_083_eps_to_revenue_ratio":                  {"inputs": ["eps", "revenue"],                      "func": ecl_083_eps_to_revenue_ratio},
    "ecl_084_epsdil_zscore_4q":                      {"inputs": ["epsdil"],                              "func": ecl_084_epsdil_zscore_4q},
    "ecl_085_epsdil_pct_rank_4q":                    {"inputs": ["epsdil"],                              "func": ecl_085_epsdil_pct_rank_4q},
    "ecl_086_eps_expanding_pct_rank":                {"inputs": ["eps"],                                 "func": ecl_086_eps_expanding_pct_rank},
    "ecl_087_epsdil_expanding_zscore":               {"inputs": ["epsdil"],                              "func": ecl_087_epsdil_expanding_zscore},
    "ecl_088_eps_qoq_negative_acceleration":         {"inputs": ["eps"],                                 "func": ecl_088_eps_qoq_negative_acceleration},
    "ecl_089_eps_pct_rank_12q":                       {"inputs": ["eps"],                                 "func": ecl_089_eps_pct_rank_12q},
    "ecl_090_epsdil_worst_3y":                       {"inputs": ["epsdil"],                              "func": ecl_090_epsdil_worst_3y},
    "ecl_091_ebit_qoq_pct":                          {"inputs": ["ebit"],                                "func": ecl_091_ebit_qoq_pct},
    "ecl_092_ebit_yoy_pct":                          {"inputs": ["ebit"],                                "func": ecl_092_ebit_yoy_pct},
    "ecl_093_ebitda_yoy_pct":                        {"inputs": ["ebitda"],                              "func": ecl_093_ebitda_yoy_pct},
    "ecl_094_ebt_yoy_pct":                           {"inputs": ["ebt"],                                 "func": ecl_094_ebt_yoy_pct},
    "ecl_095_ebit_pct_drawdown_from_4q_peak":        {"inputs": ["ebit"],                                "func": ecl_095_ebit_pct_drawdown_from_4q_peak},
    "ecl_096_ebitda_pct_drawdown_from_4q_peak":      {"inputs": ["ebitda"],                              "func": ecl_096_ebitda_pct_drawdown_from_4q_peak},
    "ecl_097_ebt_pct_drawdown_from_4q_peak":         {"inputs": ["ebt"],                                 "func": ecl_097_ebt_pct_drawdown_from_4q_peak},
    "ecl_098_ebit_zscore_8q":                        {"inputs": ["ebit"],                                "func": ecl_098_ebit_zscore_8q},
    "ecl_099_ebitda_zscore_4q":                      {"inputs": ["ebitda"],                              "func": ecl_099_ebitda_zscore_4q},
    "ecl_100_ebt_zscore_4q":                         {"inputs": ["ebt"],                                 "func": ecl_100_ebt_zscore_4q},
    "ecl_101_ebit_loss_fraction_3y":                 {"inputs": ["ebit"],                                "func": ecl_101_ebit_loss_fraction_3y},
    "ecl_102_ebitda_loss_fraction_2y":               {"inputs": ["ebitda"],                              "func": ecl_102_ebitda_loss_fraction_2y},
    "ecl_103_ebit_to_netinc_convergence":            {"inputs": ["ebit", "netinc"],                      "func": ecl_103_ebit_to_netinc_convergence},
    "ecl_104_ebitda_to_ebit_gap":                    {"inputs": ["ebitda", "ebit"],                      "func": ecl_104_ebitda_to_ebit_gap},
    "ecl_105_ebit_consecutive_decline_streak":       {"inputs": ["ebit"],                                "func": ecl_105_ebit_consecutive_decline_streak},
    "ecl_106_netinc_ttm_zscore_5y":                  {"inputs": ["netinc"],                              "func": ecl_106_netinc_ttm_zscore_5y},
    "ecl_107_netinc_ttm_pct_chg":                    {"inputs": ["netinc"],                              "func": ecl_107_netinc_ttm_pct_chg},
    "ecl_108_netinc_ttm_drawdown_from_peak":         {"inputs": ["netinc"],                              "func": ecl_108_netinc_ttm_drawdown_from_peak},
    "ecl_109_netinc_ttm_pct_drawdown_from_peak":     {"inputs": ["netinc"],                              "func": ecl_109_netinc_ttm_pct_drawdown_from_peak},
    "ecl_110_netinc_ttm_is_negative":                {"inputs": ["netinc"],                              "func": ecl_110_netinc_ttm_is_negative},
    "ecl_111_eps_ttm_sum":                           {"inputs": ["eps"],                                 "func": ecl_111_eps_ttm_sum},
    "ecl_112_eps_ttm_drawdown_from_peak":            {"inputs": ["eps"],                                 "func": ecl_112_eps_ttm_drawdown_from_peak},
    "ecl_113_ebit_ttm_sum":                          {"inputs": ["ebit"],                                "func": ecl_113_ebit_ttm_sum},
    "ecl_114_ebitda_ttm_sum":                        {"inputs": ["ebitda"],                              "func": ecl_114_ebitda_ttm_sum},
    "ecl_115_ebit_ttm_drawdown_from_peak":           {"inputs": ["ebit"],                                "func": ecl_115_ebit_ttm_drawdown_from_peak},
    "ecl_116_netinc_2y_sum":                         {"inputs": ["netinc"],                              "func": ecl_116_netinc_2y_sum},
    "ecl_117_netinc_3y_sum":                         {"inputs": ["netinc"],                              "func": ecl_117_netinc_3y_sum},
    "ecl_118_netinccmn_ttm_sum":                     {"inputs": ["netinccmn"],                           "func": ecl_118_netinccmn_ttm_sum},
    "ecl_119_netinccmn_ttm_drawdown_from_peak":      {"inputs": ["netinccmn"],                           "func": ecl_119_netinccmn_ttm_drawdown_from_peak},
    "ecl_120_ebt_ttm_sum":                           {"inputs": ["ebt"],                                 "func": ecl_120_ebt_ttm_sum},
    "ecl_121_netinc_slope_4q":                       {"inputs": ["netinc"],                              "func": ecl_121_netinc_slope_4q},
    "ecl_122_netinc_slope_8q":                       {"inputs": ["netinc"],                              "func": ecl_122_netinc_slope_8q},
    "ecl_123_eps_slope_4q":                          {"inputs": ["eps"],                                 "func": ecl_123_eps_slope_4q},
    "ecl_124_netinc_momentum_qoq_vs_yoy":            {"inputs": ["netinc"],                              "func": ecl_124_netinc_momentum_qoq_vs_yoy},
    "ecl_125_netinc_at_3y_low_flag":                 {"inputs": ["netinc"],                              "func": ecl_125_netinc_at_3y_low_flag},
    "ecl_126_eps_deceleration_flag":                 {"inputs": ["eps"],                                 "func": ecl_126_eps_deceleration_flag},
    "ecl_127_netinc_4q_decline_count":               {"inputs": ["netinc"],                              "func": ecl_127_netinc_4q_decline_count},
    "ecl_128_netinc_8q_decline_count":               {"inputs": ["netinc"],                              "func": ecl_128_netinc_8q_decline_count},
    "ecl_129_eps_4q_decline_count":                  {"inputs": ["eps"],                                 "func": ecl_129_eps_4q_decline_count},
    "ecl_130_netinc_max_single_qoq_drop":            {"inputs": ["netinc"],                              "func": ecl_130_netinc_max_single_qoq_drop},
    "ecl_131_netinc_max_single_yoy_drop":            {"inputs": ["netinc"],                              "func": ecl_131_netinc_max_single_yoy_drop},
    "ecl_132_eps_max_single_qoq_drop":               {"inputs": ["eps"],                                 "func": ecl_132_eps_max_single_qoq_drop},
    "ecl_133_netinc_4q_range":                       {"inputs": ["netinc"],                              "func": ecl_133_netinc_4q_range},
    "ecl_134_netinc_8q_range":                       {"inputs": ["netinc"],                              "func": ecl_134_netinc_8q_range},
    "ecl_135_netinc_volatility_4q":                  {"inputs": ["netinc"],                              "func": ecl_135_netinc_volatility_4q},
    "ecl_136_netinc_to_gp_ratio":                    {"inputs": ["netinc", "gp"],                        "func": ecl_136_netinc_to_gp_ratio},
    "ecl_137_netinc_to_ebt_ratio":                   {"inputs": ["netinc", "ebt"],                       "func": ecl_137_netinc_to_ebt_ratio},
    "ecl_138_netinc_to_ebit_ratio":                  {"inputs": ["netinc", "ebit"],                      "func": ecl_138_netinc_to_ebit_ratio},
    "ecl_139_opinc_to_netinc_yoy_divergence":        {"inputs": ["opinc", "netinc"],                     "func": ecl_139_opinc_to_netinc_yoy_divergence},
    "ecl_140_gp_to_netinc_yoy_divergence":           {"inputs": ["gp", "netinc"],                        "func": ecl_140_gp_to_netinc_yoy_divergence},
    "ecl_141_netinc_vs_prior_peak_pct_3y":           {"inputs": ["netinc"],                              "func": ecl_141_netinc_vs_prior_peak_pct_3y},
    "ecl_142_netinc_vs_prior_peak_pct_5y":           {"inputs": ["netinc"],                              "func": ecl_142_netinc_vs_prior_peak_pct_5y},
    "ecl_143_netinc_at_historical_low_flag":         {"inputs": ["netinc"],                              "func": ecl_143_netinc_at_historical_low_flag},
    "ecl_144_eps_at_historical_low_flag":            {"inputs": ["eps"],                                 "func": ecl_144_eps_at_historical_low_flag},
    "ecl_145_ebit_at_historical_low_flag":           {"inputs": ["ebit"],                                "func": ecl_145_ebit_at_historical_low_flag},
    "ecl_146_netinc_median_deviation_4q":            {"inputs": ["netinc"],                              "func": ecl_146_netinc_median_deviation_4q},
    "ecl_147_netinc_median_deviation_8q":            {"inputs": ["netinc"],                              "func": ecl_147_netinc_median_deviation_8q},
    "ecl_148_netinc_interquartile_position_4q":      {"inputs": ["netinc"],                              "func": ecl_148_netinc_interquartile_position_4q},
    "ecl_149_netinc_tail_q05_4q":                    {"inputs": ["netinc"],                              "func": ecl_149_netinc_tail_q05_4q},
    "ecl_150_earnings_collapse_severity_index":      {"inputs": ["netinc", "eps", "ebit", "ebitda"],     "func": ecl_150_earnings_collapse_severity_index},
}
