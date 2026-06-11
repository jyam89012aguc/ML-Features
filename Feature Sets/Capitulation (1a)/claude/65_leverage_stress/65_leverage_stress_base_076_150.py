"""
65_leverage_stress — Base Features 076-150
Domain: debt/equity and debt/assets escalation, capital-structure stress
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
    """
    Element-wise division; replaces zero denominator with NaN.
    Negative denominators (e.g. negative equity) are preserved as-is —
    they carry economic meaning (technical insolvency) and must not be masked.
    Only exact-zero denominators are replaced with NaN to avoid inf.
    """
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of denominator; avoids sign confusion in pct features."""
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

# --- Group F (076-090): Debt growth rate, acceleration, and velocity ---

def lvs_076_debt_growth_rate_qoq(debt: pd.Series) -> pd.Series:
    """QoQ absolute change in total debt."""
    return debt - debt.shift(_TD_QTR)


def lvs_077_debt_growth_rate_yoy(debt: pd.Series) -> pd.Series:
    """YoY absolute change in total debt."""
    return debt - debt.shift(_TD_YEAR)


def lvs_078_debt_growth_acceleration_qoq(debt: pd.Series) -> pd.Series:
    """2nd difference of debt over 63-day steps: QoQ change in QoQ debt growth."""
    d1 = debt - debt.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_079_debt_growth_acceleration_yoy(debt: pd.Series) -> pd.Series:
    """YoY change in the YoY debt growth (2nd-order YoY debt acceleration)."""
    d1 = debt - debt.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def lvs_080_debtnc_growth_rate_qoq(debtnc: pd.Series) -> pd.Series:
    """QoQ change in long-term debt."""
    return debtnc - debtnc.shift(_TD_QTR)


def lvs_081_debtc_growth_rate_qoq(debtc: pd.Series) -> pd.Series:
    """QoQ change in short-term / current debt."""
    return debtc - debtc.shift(_TD_QTR)


def lvs_082_debt_2y_pct_change(debt: pd.Series) -> pd.Series:
    """Debt 2-year percent change (504-day lag)."""
    prior = debt.shift(_TD_2Y)
    return _safe_div_abs(debt - prior, prior)


def lvs_083_debt_3y_pct_change(debt: pd.Series) -> pd.Series:
    """Debt 3-year percent change (756-day lag)."""
    prior = debt.shift(_TD_3Y)
    return _safe_div_abs(debt - prior, prior)


def lvs_084_debt_rolling_4q_avg(debt: pd.Series) -> pd.Series:
    """Trailing 4-quarter (252-day) mean of total debt."""
    return _rolling_mean(debt, _TD_YEAR)


def lvs_085_debt_vs_4q_avg(debt: pd.Series) -> pd.Series:
    """Current debt minus trailing 4-quarter mean (level above average)."""
    return debt - _rolling_mean(debt, _TD_YEAR)


def lvs_086_debt_vs_8q_avg(debt: pd.Series) -> pd.Series:
    """Current debt minus trailing 8-quarter mean."""
    return debt - _rolling_mean(debt, _TD_2Y)


def lvs_087_debt_pct_above_4q_avg(debt: pd.Series) -> pd.Series:
    """Percent by which current debt exceeds trailing 4-quarter mean."""
    avg = _rolling_mean(debt, _TD_YEAR)
    return _safe_div_abs(debt - avg, avg)


def lvs_088_equity_qoq_change(equity: pd.Series) -> pd.Series:
    """QoQ absolute change in equity."""
    return equity - equity.shift(_TD_QTR)


def lvs_089_equity_yoy_change(equity: pd.Series) -> pd.Series:
    """YoY absolute change in equity."""
    return equity - equity.shift(_TD_YEAR)


def lvs_090_equity_yoy_pct_change(equity: pd.Series) -> pd.Series:
    """YoY percent change in equity."""
    prior = equity.shift(_TD_YEAR)
    return _safe_div_abs(equity - prior, prior)


# --- Group G (091-105): Net-debt ratio expansions and cash-buffer erosion ---

def lvs_091_cash_to_debt_ratio(cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """Cash & equivalents / total debt (inverse leverage buffer)."""
    return _safe_div(cashnequiv, debt)


def lvs_092_cash_to_debt_qoq_change(cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """QoQ change in cash/debt ratio."""
    ratio = _safe_div(cashnequiv, debt)
    return ratio - ratio.shift(_TD_QTR)


def lvs_093_cash_to_debt_yoy_change(cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """YoY change in cash/debt ratio."""
    ratio = _safe_div(cashnequiv, debt)
    return ratio - ratio.shift(_TD_YEAR)


def lvs_094_cash_cover_eroding_flag(cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """1 if cash/debt ratio is lower than it was 4 quarters ago."""
    ratio = _safe_div(cashnequiv, debt)
    return (ratio < ratio.shift(_TD_QTR)).astype(float)


def lvs_095_net_debt_to_equity_abs(debt: pd.Series, cashnequiv: pd.Series, equity: pd.Series) -> pd.Series:
    """Net debt / |equity| — magnitude of leverage regardless of equity sign."""
    return _safe_div(debt - cashnequiv, equity.abs().replace(0, np.nan))


def lvs_096_net_debt_zscore_4q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Z-score of net debt level within trailing 4-quarter window."""
    nd = debt - cashnequiv
    return _zscore_rolling(nd, _TD_YEAR)


def lvs_097_net_debt_zscore_8q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Z-score of net debt level within trailing 8-quarter window."""
    nd = debt - cashnequiv
    return _zscore_rolling(nd, _TD_2Y)


def lvs_098_net_debt_expanding_pct_rank(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Expanding percentile rank of net debt vs all-history."""
    nd = debt - cashnequiv
    return nd.expanding(min_periods=2).rank(pct=True)


def lvs_099_net_debt_rank_4q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of net debt within trailing 4-quarter window."""
    nd = debt - cashnequiv
    return _rolling_rank_pct(nd, _TD_YEAR)


def lvs_100_liabilitiesnc_to_equity(liabilitiesnc: pd.Series, equity: pd.Series) -> pd.Series:
    """Non-current liabilities / equity."""
    return _safe_div(liabilitiesnc, equity)


def lvs_101_liabilitiesnc_to_equity_qoq_change(liabilitiesnc: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in non-current liabilities / equity."""
    ratio = _safe_div(liabilitiesnc, equity)
    return ratio - ratio.shift(_TD_QTR)


def lvs_102_total_debt_drawup_from_expanding_min(debt: pd.Series) -> pd.Series:
    """Total debt minus its all-history expanding minimum."""
    return debt - debt.expanding(min_periods=1).min()


def lvs_103_net_debt_drawup_from_expanding_min(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Net debt minus its all-history expanding minimum."""
    nd = debt - cashnequiv
    return nd - nd.expanding(min_periods=1).min()


def lvs_104_equity_drawdown_from_expanding_peak(equity: pd.Series) -> pd.Series:
    """Equity minus its all-history expanding maximum (capital erosion)."""
    return equity - equity.expanding(min_periods=1).max()


def lvs_105_equity_pct_drawdown_from_expanding_peak(equity: pd.Series) -> pd.Series:
    """Equity percent drawdown from all-history expanding peak."""
    peak = equity.expanding(min_periods=1).max()
    return _safe_div_abs(equity - peak, peak)


# --- Group H (106-120): Liabilities structure and multi-year stress ---

def lvs_106_liabilities_qoq_change(liabilities: pd.Series) -> pd.Series:
    """QoQ absolute change in total liabilities."""
    return liabilities - liabilities.shift(_TD_QTR)


def lvs_107_liabilities_yoy_change(liabilities: pd.Series) -> pd.Series:
    """YoY absolute change in total liabilities."""
    return liabilities - liabilities.shift(_TD_YEAR)


def lvs_108_liabilities_yoy_pct_change(liabilities: pd.Series) -> pd.Series:
    """YoY percent change in total liabilities."""
    prior = liabilities.shift(_TD_YEAR)
    return _safe_div_abs(liabilities - prior, prior)


def lvs_109_liabilitiesc_qoq_change(liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in current liabilities."""
    return liabilitiesc - liabilitiesc.shift(_TD_QTR)


def lvs_110_liabilitiesnc_qoq_change(liabilitiesnc: pd.Series) -> pd.Series:
    """QoQ change in non-current liabilities."""
    return liabilitiesnc - liabilitiesnc.shift(_TD_QTR)


def lvs_111_liabilities_to_assets_zscore_4q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of L/A ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(liabilities, assets), _TD_YEAR)


def lvs_112_liabilities_to_assets_rank_4q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of L/A ratio within trailing 4-quarter window."""
    return _rolling_rank_pct(_safe_div(liabilities, assets), _TD_YEAR)


def lvs_113_liabilities_to_assets_2y_change(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """L/A ratio change over 2 years."""
    ratio = _safe_div(liabilities, assets)
    return ratio - ratio.shift(_TD_2Y)


def lvs_114_liabilities_to_assets_3y_change(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """L/A ratio change over 3 years."""
    ratio = _safe_div(liabilities, assets)
    return ratio - ratio.shift(_TD_3Y)


def lvs_115_liabilities_growing_faster_than_assets(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """1 if liabilities grew YoY faster (in pct) than assets."""
    liab_g = _safe_div_abs(liabilities - liabilities.shift(_TD_YEAR), liabilities.shift(_TD_YEAR))
    asset_g = _safe_div_abs(assets - assets.shift(_TD_YEAR), assets.shift(_TD_YEAR))
    return (liab_g > asset_g).astype(float)


def lvs_116_debt_to_equity_expanding_zscore(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Expanding z-score of D/E ratio (how extreme vs entire history)."""
    ratio = _safe_div(debt, equity)
    m  = ratio.expanding(min_periods=2).mean()
    sd = ratio.expanding(min_periods=2).std()
    return _safe_div(ratio - m, sd)


def lvs_117_debt_to_assets_expanding_zscore(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Expanding z-score of D/A ratio."""
    ratio = _safe_div(debt, assets)
    m  = ratio.expanding(min_periods=2).mean()
    sd = ratio.expanding(min_periods=2).std()
    return _safe_div(ratio - m, sd)


def lvs_118_equity_shrinking_3y_flag(equity: pd.Series) -> pd.Series:
    """1 if equity is lower than it was 3 years ago."""
    return (equity < equity.shift(_TD_3Y)).astype(float)


def lvs_119_equity_shrinking_2y_flag(equity: pd.Series) -> pd.Series:
    """1 if equity is lower than it was 2 years ago."""
    return (equity < equity.shift(_TD_2Y)).astype(float)


def lvs_120_debt_equity_divergence_3y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    3-year divergence: (debt / debt_3y_ago) - (equity / equity_3y_ago).
    Positive means debt grew faster than equity over 3 years.
    """
    debt_ratio   = _safe_div(debt,   debt.shift(_TD_3Y))
    equity_ratio = _safe_div_abs(equity, equity.shift(_TD_3Y))
    return debt_ratio - equity_ratio


# --- Group I (121-135): Short-term stress mix and rolling-window indicators ---

def lvs_121_debtc_to_assets(debtc: pd.Series, assets: pd.Series) -> pd.Series:
    """Short-term debt / total assets."""
    return _safe_div(debtc, assets)


def lvs_122_debtc_to_assets_qoq_change(debtc: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in short-term debt / assets."""
    ratio = _safe_div(debtc, assets)
    return ratio - ratio.shift(_TD_QTR)


def lvs_123_debtnc_to_assets(debtnc: pd.Series, assets: pd.Series) -> pd.Series:
    """Long-term debt / total assets."""
    return _safe_div(debtnc, assets)


def lvs_124_debtnc_to_assets_qoq_change(debtnc: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in long-term debt / assets."""
    ratio = _safe_div(debtnc, assets)
    return ratio - ratio.shift(_TD_QTR)


def lvs_125_st_debt_pct_above_4q_avg(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """ST-debt-mix percent deviation from its trailing 4-quarter average."""
    mix = _safe_div(debtc, debt)
    avg = _rolling_mean(mix, _TD_YEAR)
    return _safe_div_abs(mix - avg, avg)


def lvs_126_debtc_yoy_pct_change(debtc: pd.Series) -> pd.Series:
    """YoY percent change in short-term debt."""
    prior = debtc.shift(_TD_YEAR)
    return _safe_div_abs(debtc - prior, prior)


def lvs_127_debtnc_yoy_pct_change(debtnc: pd.Series) -> pd.Series:
    """YoY percent change in long-term debt."""
    prior = debtnc.shift(_TD_YEAR)
    return _safe_div_abs(debtnc - prior, prior)


def lvs_128_st_debt_rising_faster_than_lt(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    """1 if short-term debt grew QoQ faster (in pct) than long-term debt."""
    st_g = _safe_div_abs(debtc - debtc.shift(_TD_QTR), debtc.shift(_TD_QTR))
    lt_g = _safe_div_abs(debtnc - debtnc.shift(_TD_QTR), debtnc.shift(_TD_QTR))
    return (st_g > lt_g).astype(float)


def lvs_129_debt_to_equity_rolling_median_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 4-quarter median of D/E ratio."""
    return _rolling_median(_safe_div(debt, equity), _TD_YEAR)


def lvs_130_leverage_above_rolling_median_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1 if current D/E is above its trailing 4-quarter median."""
    ratio  = _safe_div(debt, equity)
    median = _rolling_median(ratio, _TD_YEAR)
    return (ratio > median).astype(float)


def lvs_131_debt_to_ebitda_above_5x_flag(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Binary: 1 if D/EBITDA > 5 (highly leveraged threshold)."""
    return (_safe_div(debt, ebitda) > 5.0).astype(float)


def lvs_132_debt_to_ebitda_above_8x_flag(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Binary: 1 if D/EBITDA > 8 (extreme leverage threshold)."""
    return (_safe_div(debt, ebitda) > 8.0).astype(float)


def lvs_133_net_debt_to_ebitda_above_5x_flag(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Binary: 1 if net-D/EBITDA > 5."""
    return (_safe_div(debt - cashnequiv, ebitda) > 5.0).astype(float)


def lvs_134_leverage_stress_above_8q_avg(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1 if current D/E ratio is above its trailing 8-quarter average."""
    ratio = _safe_div(debt, equity)
    avg   = _rolling_mean(ratio, _TD_2Y)
    return (ratio > avg).astype(float)


def lvs_135_leverage_stress_above_12q_avg(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1 if current D/E ratio is above its trailing 12-quarter average."""
    ratio = _safe_div(debt, equity)
    avg   = _rolling_mean(ratio, _TD_3Y)
    return (ratio > avg).astype(float)


# --- Group J (136-150): Composite, multi-metric, and advanced signals ---

def lvs_136_leverage_stress_score_3metric(debt: pd.Series, equity: pd.Series, assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """
    Composite: z-score average of D/E, D/A, and L/A in trailing 4-quarter window.
    """
    z_de = _zscore_rolling(_safe_div(debt, equity),      _TD_YEAR)
    z_da = _zscore_rolling(_safe_div(debt, assets),      _TD_YEAR)
    z_la = _zscore_rolling(_safe_div(liabilities, assets), _TD_YEAR)
    return (z_de + z_da + z_la) / 3.0


def lvs_137_leverage_stress_score_5metric(debt: pd.Series, equity: pd.Series, assets: pd.Series, liabilities: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """
    Composite: z-score average of D/E, D/A, L/A, net-D/E, net-D/EBITDA.
    """
    z_de  = _zscore_rolling(_safe_div(debt, equity),             _TD_YEAR)
    z_da  = _zscore_rolling(_safe_div(debt, assets),             _TD_YEAR)
    z_la  = _zscore_rolling(_safe_div(liabilities, assets),      _TD_YEAR)
    z_nde = _zscore_rolling(_safe_div(debt - cashnequiv, equity), _TD_YEAR)
    z_ndb = _zscore_rolling(_safe_div(debt - cashnequiv, ebitda), _TD_YEAR)
    return (z_de + z_da + z_la + z_nde + z_ndb) / 5.0


def lvs_138_leverage_deterioration_composite_qoq(debt: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """
    QoQ change in average of D/E and D/A z-scores.
    """
    z_de = _zscore_rolling(_safe_div(debt, equity), _TD_YEAR)
    z_da = _zscore_rolling(_safe_div(debt, assets), _TD_YEAR)
    comp = (z_de + z_da) / 2.0
    return comp - comp.shift(_TD_QTR)


def lvs_139_debt_equity_ratio_slope_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    OLS slope of D/E ratio over trailing 4-quarter (252-day) window.
    """
    ratio = _safe_div(debt, equity)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return ratio.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def lvs_140_debt_to_assets_slope_4q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """
    OLS slope of D/A ratio over trailing 4-quarter window.
    """
    ratio = _safe_div(debt, assets)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return ratio.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def lvs_141_net_debt_slope_4q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    OLS slope of net debt level over trailing 4-quarter window.
    """
    nd = debt - cashnequiv

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return nd.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def lvs_142_equity_slope_4q(equity: pd.Series) -> pd.Series:
    """
    OLS slope of equity level over trailing 4-quarter window.
    Negative slope = eroding capital base.
    """
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return equity.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def lvs_143_leverage_ewm_deviation_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio minus its 8-quarter EWM (span=504)."""
    ratio = _safe_div(debt, equity)
    ewm   = _ewm_mean(ratio, _TD_2Y)
    return ratio - ewm


def lvs_144_debt_to_ebitda_zscore_8q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of D/EBITDA within trailing 8-quarter window."""
    return _zscore_rolling(_safe_div(debt, ebitda), _TD_2Y)


def lvs_145_financial_leverage_rank_4q(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """Percentile rank of financial leverage multiplier within trailing 4-quarter window."""
    return _rolling_rank_pct(_safe_div(assets, equity), _TD_YEAR)


def lvs_146_assets_financed_by_debt_fraction(debt: pd.Series, assets: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Fraction of assets financed by debt vs equity:
    debt / (debt + |equity|). A purely structural signal.
    """
    denom = debt + equity.abs().replace(0, np.nan)
    return _safe_div(debt, denom)


def lvs_147_leverage_stress_worst_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 4-quarter maximum (worst) D/E ratio."""
    return _rolling_max(_safe_div(debt, equity), _TD_YEAR)


def lvs_148_leverage_stress_worst_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 8-quarter maximum (worst) D/E ratio."""
    return _rolling_max(_safe_div(debt, equity), _TD_2Y)


def lvs_149_leverage_stress_worst_12q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 12-quarter maximum (worst) D/E ratio."""
    return _rolling_max(_safe_div(debt, equity), _TD_3Y)


def lvs_150_leverage_capital_structure_stress_index(debt: pd.Series, equity: pd.Series, assets: pd.Series, liabilities: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """
    Full capital-structure stress index: equally-weighted expanding z-score
    of six leverage dimensions: D/E, D/A, L/A, net-D/E, net-D/EBITDA, L/equity.
    Captures maximum distress breadth across the balance sheet.
    """
    nd = debt - cashnequiv

    def _exp_z(s):
        m  = s.expanding(min_periods=2).mean()
        sd = s.expanding(min_periods=2).std()
        return _safe_div(s - m, sd)

    z1 = _exp_z(_safe_div(debt,       equity))
    z2 = _exp_z(_safe_div(debt,       assets))
    z3 = _exp_z(_safe_div(liabilities, assets))
    z4 = _exp_z(_safe_div(nd,         equity))
    z5 = _exp_z(_safe_div(nd,         ebitda))
    z6 = _exp_z(_safe_div(liabilities, equity))
    return (z1 + z2 + z3 + z4 + z5 + z6) / 6.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

LEVERAGE_STRESS_REGISTRY_076_150 = {
    "lvs_076_debt_growth_rate_qoq":                  {"inputs": ["debt"],                                                    "func": lvs_076_debt_growth_rate_qoq},
    "lvs_077_debt_growth_rate_yoy":                  {"inputs": ["debt"],                                                    "func": lvs_077_debt_growth_rate_yoy},
    "lvs_078_debt_growth_acceleration_qoq":          {"inputs": ["debt"],                                                    "func": lvs_078_debt_growth_acceleration_qoq},
    "lvs_079_debt_growth_acceleration_yoy":          {"inputs": ["debt"],                                                    "func": lvs_079_debt_growth_acceleration_yoy},
    "lvs_080_debtnc_growth_rate_qoq":                {"inputs": ["debtnc"],                                                  "func": lvs_080_debtnc_growth_rate_qoq},
    "lvs_081_debtc_growth_rate_qoq":                 {"inputs": ["debtc"],                                                   "func": lvs_081_debtc_growth_rate_qoq},
    "lvs_082_debt_2y_pct_change":                    {"inputs": ["debt"],                                                    "func": lvs_082_debt_2y_pct_change},
    "lvs_083_debt_3y_pct_change":                    {"inputs": ["debt"],                                                    "func": lvs_083_debt_3y_pct_change},
    "lvs_084_debt_rolling_4q_avg":                   {"inputs": ["debt"],                                                    "func": lvs_084_debt_rolling_4q_avg},
    "lvs_085_debt_vs_4q_avg":                        {"inputs": ["debt"],                                                    "func": lvs_085_debt_vs_4q_avg},
    "lvs_086_debt_vs_8q_avg":                        {"inputs": ["debt"],                                                    "func": lvs_086_debt_vs_8q_avg},
    "lvs_087_debt_pct_above_4q_avg":                 {"inputs": ["debt"],                                                    "func": lvs_087_debt_pct_above_4q_avg},
    "lvs_088_equity_qoq_change":                     {"inputs": ["equity"],                                                  "func": lvs_088_equity_qoq_change},
    "lvs_089_equity_yoy_change":                     {"inputs": ["equity"],                                                  "func": lvs_089_equity_yoy_change},
    "lvs_090_equity_yoy_pct_change":                 {"inputs": ["equity"],                                                  "func": lvs_090_equity_yoy_pct_change},
    "lvs_091_cash_to_debt_ratio":                    {"inputs": ["cashnequiv", "debt"],                                      "func": lvs_091_cash_to_debt_ratio},
    "lvs_092_cash_to_debt_qoq_change":               {"inputs": ["cashnequiv", "debt"],                                      "func": lvs_092_cash_to_debt_qoq_change},
    "lvs_093_cash_to_debt_yoy_change":               {"inputs": ["cashnequiv", "debt"],                                      "func": lvs_093_cash_to_debt_yoy_change},
    "lvs_094_cash_cover_eroding_flag":               {"inputs": ["cashnequiv", "debt"],                                      "func": lvs_094_cash_cover_eroding_flag},
    "lvs_095_net_debt_to_equity_abs":                {"inputs": ["debt", "cashnequiv", "equity"],                            "func": lvs_095_net_debt_to_equity_abs},
    "lvs_096_net_debt_zscore_4q":                    {"inputs": ["debt", "cashnequiv"],                                      "func": lvs_096_net_debt_zscore_4q},
    "lvs_097_net_debt_zscore_8q":                    {"inputs": ["debt", "cashnequiv"],                                      "func": lvs_097_net_debt_zscore_8q},
    "lvs_098_net_debt_expanding_pct_rank":           {"inputs": ["debt", "cashnequiv"],                                      "func": lvs_098_net_debt_expanding_pct_rank},
    "lvs_099_net_debt_rank_4q":                      {"inputs": ["debt", "cashnequiv"],                                      "func": lvs_099_net_debt_rank_4q},
    "lvs_100_liabilitiesnc_to_equity":               {"inputs": ["liabilitiesnc", "equity"],                                 "func": lvs_100_liabilitiesnc_to_equity},
    "lvs_101_liabilitiesnc_to_equity_qoq_change":    {"inputs": ["liabilitiesnc", "equity"],                                 "func": lvs_101_liabilitiesnc_to_equity_qoq_change},
    "lvs_102_total_debt_drawup_from_expanding_min":  {"inputs": ["debt"],                                                    "func": lvs_102_total_debt_drawup_from_expanding_min},
    "lvs_103_net_debt_drawup_from_expanding_min":    {"inputs": ["debt", "cashnequiv"],                                      "func": lvs_103_net_debt_drawup_from_expanding_min},
    "lvs_104_equity_drawdown_from_expanding_peak":   {"inputs": ["equity"],                                                  "func": lvs_104_equity_drawdown_from_expanding_peak},
    "lvs_105_equity_pct_drawdown_from_expanding_peak": {"inputs": ["equity"],                                                "func": lvs_105_equity_pct_drawdown_from_expanding_peak},
    "lvs_106_liabilities_qoq_change":                {"inputs": ["liabilities"],                                             "func": lvs_106_liabilities_qoq_change},
    "lvs_107_liabilities_yoy_change":                {"inputs": ["liabilities"],                                             "func": lvs_107_liabilities_yoy_change},
    "lvs_108_liabilities_yoy_pct_change":            {"inputs": ["liabilities"],                                             "func": lvs_108_liabilities_yoy_pct_change},
    "lvs_109_liabilitiesc_qoq_change":               {"inputs": ["liabilitiesc"],                                            "func": lvs_109_liabilitiesc_qoq_change},
    "lvs_110_liabilitiesnc_qoq_change":              {"inputs": ["liabilitiesnc"],                                           "func": lvs_110_liabilitiesnc_qoq_change},
    "lvs_111_liabilities_to_assets_zscore_4q":       {"inputs": ["liabilities", "assets"],                                   "func": lvs_111_liabilities_to_assets_zscore_4q},
    "lvs_112_liabilities_to_assets_rank_4q":         {"inputs": ["liabilities", "assets"],                                   "func": lvs_112_liabilities_to_assets_rank_4q},
    "lvs_113_liabilities_to_assets_2y_change":       {"inputs": ["liabilities", "assets"],                                   "func": lvs_113_liabilities_to_assets_2y_change},
    "lvs_114_liabilities_to_assets_3y_change":       {"inputs": ["liabilities", "assets"],                                   "func": lvs_114_liabilities_to_assets_3y_change},
    "lvs_115_liabilities_growing_faster_than_assets":{"inputs": ["liabilities", "assets"],                                   "func": lvs_115_liabilities_growing_faster_than_assets},
    "lvs_116_debt_to_equity_expanding_zscore":       {"inputs": ["debt", "equity"],                                          "func": lvs_116_debt_to_equity_expanding_zscore},
    "lvs_117_debt_to_assets_expanding_zscore":       {"inputs": ["debt", "assets"],                                          "func": lvs_117_debt_to_assets_expanding_zscore},
    "lvs_118_equity_shrinking_3y_flag":              {"inputs": ["equity"],                                                  "func": lvs_118_equity_shrinking_3y_flag},
    "lvs_119_equity_shrinking_2y_flag":              {"inputs": ["equity"],                                                  "func": lvs_119_equity_shrinking_2y_flag},
    "lvs_120_debt_equity_divergence_3y":             {"inputs": ["debt", "equity"],                                          "func": lvs_120_debt_equity_divergence_3y},
    "lvs_121_debtc_to_assets":                       {"inputs": ["debtc", "assets"],                                         "func": lvs_121_debtc_to_assets},
    "lvs_122_debtc_to_assets_qoq_change":            {"inputs": ["debtc", "assets"],                                         "func": lvs_122_debtc_to_assets_qoq_change},
    "lvs_123_debtnc_to_assets":                      {"inputs": ["debtnc", "assets"],                                        "func": lvs_123_debtnc_to_assets},
    "lvs_124_debtnc_to_assets_qoq_change":           {"inputs": ["debtnc", "assets"],                                        "func": lvs_124_debtnc_to_assets_qoq_change},
    "lvs_125_st_debt_pct_above_4q_avg":              {"inputs": ["debtc", "debt"],                                           "func": lvs_125_st_debt_pct_above_4q_avg},
    "lvs_126_debtc_yoy_pct_change":                  {"inputs": ["debtc"],                                                   "func": lvs_126_debtc_yoy_pct_change},
    "lvs_127_debtnc_yoy_pct_change":                 {"inputs": ["debtnc"],                                                  "func": lvs_127_debtnc_yoy_pct_change},
    "lvs_128_st_debt_rising_faster_than_lt":         {"inputs": ["debtc", "debtnc"],                                         "func": lvs_128_st_debt_rising_faster_than_lt},
    "lvs_129_debt_to_equity_rolling_median_4q":      {"inputs": ["debt", "equity"],                                          "func": lvs_129_debt_to_equity_rolling_median_4q},
    "lvs_130_leverage_above_rolling_median_flag":    {"inputs": ["debt", "equity"],                                          "func": lvs_130_leverage_above_rolling_median_flag},
    "lvs_131_debt_to_ebitda_above_5x_flag":          {"inputs": ["debt", "ebitda"],                                          "func": lvs_131_debt_to_ebitda_above_5x_flag},
    "lvs_132_debt_to_ebitda_above_8x_flag":          {"inputs": ["debt", "ebitda"],                                          "func": lvs_132_debt_to_ebitda_above_8x_flag},
    "lvs_133_net_debt_to_ebitda_above_5x_flag":      {"inputs": ["debt", "cashnequiv", "ebitda"],                            "func": lvs_133_net_debt_to_ebitda_above_5x_flag},
    "lvs_134_leverage_stress_above_8q_avg":          {"inputs": ["debt", "equity"],                                          "func": lvs_134_leverage_stress_above_8q_avg},
    "lvs_135_leverage_stress_above_12q_avg":         {"inputs": ["debt", "equity"],                                          "func": lvs_135_leverage_stress_above_12q_avg},
    "lvs_136_leverage_stress_score_3metric":         {"inputs": ["debt", "equity", "assets", "liabilities"],                 "func": lvs_136_leverage_stress_score_3metric},
    "lvs_137_leverage_stress_score_5metric":         {"inputs": ["debt", "equity", "assets", "liabilities", "cashnequiv", "ebitda"], "func": lvs_137_leverage_stress_score_5metric},
    "lvs_138_leverage_deterioration_composite_qoq":  {"inputs": ["debt", "equity", "assets"],                                "func": lvs_138_leverage_deterioration_composite_qoq},
    "lvs_139_debt_equity_ratio_slope_4q":            {"inputs": ["debt", "equity"],                                          "func": lvs_139_debt_equity_ratio_slope_4q},
    "lvs_140_debt_to_assets_slope_4q":              {"inputs": ["debt", "assets"],                                           "func": lvs_140_debt_to_assets_slope_4q},
    "lvs_141_net_debt_slope_4q":                     {"inputs": ["debt", "cashnequiv"],                                      "func": lvs_141_net_debt_slope_4q},
    "lvs_142_equity_slope_4q":                       {"inputs": ["equity"],                                                  "func": lvs_142_equity_slope_4q},
    "lvs_143_leverage_ewm_deviation_8q":             {"inputs": ["debt", "equity"],                                          "func": lvs_143_leverage_ewm_deviation_8q},
    "lvs_144_debt_to_ebitda_zscore_8q":              {"inputs": ["debt", "ebitda"],                                          "func": lvs_144_debt_to_ebitda_zscore_8q},
    "lvs_145_financial_leverage_rank_4q":            {"inputs": ["assets", "equity"],                                        "func": lvs_145_financial_leverage_rank_4q},
    "lvs_146_assets_financed_by_debt_fraction":      {"inputs": ["debt", "assets", "equity"],                                "func": lvs_146_assets_financed_by_debt_fraction},
    "lvs_147_leverage_stress_worst_4q":              {"inputs": ["debt", "equity"],                                          "func": lvs_147_leverage_stress_worst_4q},
    "lvs_148_leverage_stress_worst_8q":              {"inputs": ["debt", "equity"],                                          "func": lvs_148_leverage_stress_worst_8q},
    "lvs_149_leverage_stress_worst_12q":             {"inputs": ["debt", "equity"],                                          "func": lvs_149_leverage_stress_worst_12q},
    "lvs_150_leverage_capital_structure_stress_index": {"inputs": ["debt", "equity", "assets", "liabilities", "cashnequiv", "ebitda"], "func": lvs_150_leverage_capital_structure_stress_index},
}
