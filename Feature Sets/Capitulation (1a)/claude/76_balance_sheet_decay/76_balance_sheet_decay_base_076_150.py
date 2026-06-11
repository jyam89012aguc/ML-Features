"""
76_balance_sheet_decay — Base Features 076-200
Domain: holistic multi-quarter balance-sheet deterioration
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
    this helper is for documentation and optional manual use.
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Intangibles, PPE, and asset-mix deterioration ---

def bsd_076_intangibles_yoy_change(intangibles: pd.Series) -> pd.Series:
    """Intangibles YoY absolute change (impairments push this negative)."""
    return intangibles - intangibles.shift(_TD_YEAR)


def bsd_077_intangibles_yoy_pct(intangibles: pd.Series) -> pd.Series:
    """Intangibles YoY percent change."""
    prior = intangibles.shift(_TD_YEAR)
    return _safe_div_abs(intangibles - prior, prior)


def bsd_078_ppnenet_yoy_change(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E YoY absolute change."""
    return ppnenet - ppnenet.shift(_TD_YEAR)


def bsd_079_ppnenet_yoy_pct(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E YoY percent change."""
    prior = ppnenet.shift(_TD_YEAR)
    return _safe_div_abs(ppnenet - prior, prior)


def bsd_080_tangibles_yoy_change(tangibles: pd.Series) -> pd.Series:
    """Tangible assets YoY absolute change."""
    return tangibles - tangibles.shift(_TD_YEAR)


def bsd_081_tangibles_yoy_pct(tangibles: pd.Series) -> pd.Series:
    """Tangible assets YoY percent change."""
    prior = tangibles.shift(_TD_YEAR)
    return _safe_div_abs(tangibles - prior, prior)


def bsd_082_intangibles_to_assets_ratio(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Intangibles divided by total assets — goodwill/intangibles concentration risk."""
    return _safe_div(intangibles, assets)


def bsd_083_ppnenet_to_assets_ratio(ppnenet: pd.Series, assets: pd.Series) -> pd.Series:
    """Net PP&E divided by total assets."""
    return _safe_div(ppnenet, assets)


def bsd_084_assetsc_to_assets_ratio(assetsc: pd.Series, assets: pd.Series) -> pd.Series:
    """Current assets divided by total assets — liquidity composition."""
    return _safe_div(assetsc, assets)


def bsd_085_assetsnc_yoy_pct(assetsnc: pd.Series) -> pd.Series:
    """Non-current assets YoY percent change."""
    prior = assetsnc.shift(_TD_YEAR)
    return _safe_div_abs(assetsnc - prior, prior)


def bsd_086_receivables_yoy_pct(receivables: pd.Series) -> pd.Series:
    """Receivables YoY percent change."""
    prior = receivables.shift(_TD_YEAR)
    return _safe_div_abs(receivables - prior, prior)


def bsd_087_inventory_yoy_pct(inventory: pd.Series) -> pd.Series:
    """Inventory YoY percent change."""
    prior = inventory.shift(_TD_YEAR)
    return _safe_div_abs(inventory - prior, prior)


def bsd_088_intangibles_drawdown_from_expanding_peak(intangibles: pd.Series) -> pd.Series:
    """Intangibles vs their all-history expanding maximum (captures write-downs)."""
    peak = intangibles.expanding(min_periods=1).max()
    return intangibles - peak


def bsd_089_ppnenet_drawdown_from_expanding_peak(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E vs its all-history expanding maximum."""
    peak = ppnenet.expanding(min_periods=1).max()
    return ppnenet - peak


def bsd_090_intangibles_drawdown_pct_from_4q_peak(intangibles: pd.Series) -> pd.Series:
    """Intangibles percent drawdown from 4-quarter peak."""
    peak = _rolling_max(intangibles, _TD_YEAR)
    return _safe_div_abs(intangibles - peak, peak)


# --- Group G (091-105): Cross-line ratio trends and leverage trajectory ---

def bsd_091_liab_to_assets_yoy_change(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in the liabilities-to-assets ratio."""
    ratio = _safe_div(liabilities, assets)
    return ratio - ratio.shift(_TD_YEAR)


def bsd_092_debt_to_equity_yoy_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in the debt-to-equity ratio."""
    ratio = _safe_div(debt, equity.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def bsd_093_debt_to_assets_yoy_change(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in the debt-to-assets ratio."""
    ratio = _safe_div(debt, assets)
    return ratio - ratio.shift(_TD_YEAR)


def bsd_094_liab_to_equity_yoy_change(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in the liabilities-to-equity ratio."""
    ratio = _safe_div(liabilities, equity.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def bsd_095_liab_to_assets_zscore_4q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of the liabilities-to-assets ratio in a 4-quarter window."""
    ratio = _safe_div(liabilities, assets)
    return _zscore_rolling(ratio, _TD_YEAR)


def bsd_096_debt_to_assets_zscore_4q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of the debt-to-assets ratio in a 4-quarter window."""
    ratio = _safe_div(debt, assets)
    return _zscore_rolling(ratio, _TD_YEAR)


def bsd_097_debt_to_equity_zscore_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of the debt-to-equity ratio in an 8-quarter window."""
    ratio = _safe_div(debt, equity.abs().replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def bsd_098_liab_to_assets_pct_rank_8q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of the liabilities-to-assets ratio in an 8-quarter window."""
    ratio = _safe_div(liabilities, assets)
    return _rolling_rank_pct(ratio, _TD_2Y)


def bsd_099_debt_rising_quarters_4q(debt: pd.Series) -> pd.Series:
    """Count of quarters with debt rising QoQ in the past 4 quarters."""
    rising = (debt > debt.shift(_TD_QTR)).astype(float)
    return _rolling_sum(rising, _TD_YEAR)


def bsd_100_debt_rising_quarters_8q(debt: pd.Series) -> pd.Series:
    """Count of quarters with debt rising QoQ in the past 8 quarters."""
    rising = (debt > debt.shift(_TD_QTR)).astype(float)
    return _rolling_sum(rising, _TD_2Y)


def bsd_101_liab_rising_quarters_4q(liabilities: pd.Series) -> pd.Series:
    """Count of quarters with liabilities rising QoQ in the past 4 quarters."""
    rising = (liabilities > liabilities.shift(_TD_QTR)).astype(float)
    return _rolling_sum(rising, _TD_YEAR)


def bsd_102_equity_negative_quarters_4q(equity: pd.Series) -> pd.Series:
    """Count of quarters with equity < 0 in the past 4 quarters."""
    neg = (equity < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR)


def bsd_103_retearn_negative_quarters_4q(retearn: pd.Series) -> pd.Series:
    """Count of quarters with retained earnings < 0 in the past 4 quarters."""
    neg = (retearn < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR)


def bsd_104_wc_negative_quarters_4q(workingcapital: pd.Series) -> pd.Series:
    """Count of quarters with working capital < 0 in the past 4 quarters."""
    neg = (workingcapital < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR)


def bsd_105_equity_consecutive_decline_streak(equity: pd.Series) -> pd.Series:
    """
    Current consecutive-decline streak in equity (in daily observations).
    Resets to 0 on any QoQ gain in equity.
    """
    declining = (equity < equity.shift(_TD_QTR)).astype(int)
    arr    = declining.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=equity.index)


# --- Group H (106-120): Persistence of multi-line deterioration over longer windows ---

def bsd_106_bs_deterioration_fraction_4lines_4q(assets: pd.Series, liabilities: pd.Series,
                                                  equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Rolling 4Q mean of the fraction of 4 lines worsening QoQ.
    High = prolonged breadth of deterioration.
    """
    count = (
        (assets < assets.shift(_TD_QTR)).astype(float) +
        (liabilities > liabilities.shift(_TD_QTR)).astype(float) +
        (equity < equity.shift(_TD_QTR)).astype(float) +
        (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float)
    ) / 4.0
    return _rolling_mean(count, _TD_YEAR)


def bsd_107_bs_deterioration_fraction_8lines_4q_avg(assets: pd.Series, liabilities: pd.Series,
                                                      equity: pd.Series, cashnequiv: pd.Series,
                                                      retearn: pd.Series, workingcapital: pd.Series,
                                                      invcap: pd.Series, debt: pd.Series) -> pd.Series:
    """Rolling 4Q mean fraction of 8 balance-sheet lines worsening QoQ."""
    count = (
        (assets < assets.shift(_TD_QTR)).astype(float) +
        (liabilities > liabilities.shift(_TD_QTR)).astype(float) +
        (equity < equity.shift(_TD_QTR)).astype(float) +
        (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float) +
        (retearn < retearn.shift(_TD_QTR)).astype(float) +
        (workingcapital < workingcapital.shift(_TD_QTR)).astype(float) +
        (invcap < invcap.shift(_TD_QTR)).astype(float) +
        (debt > debt.shift(_TD_QTR)).astype(float)
    ) / 8.0
    return _rolling_mean(count, _TD_YEAR)


def bsd_108_equity_mean_4q_declining_depth(equity: pd.Series) -> pd.Series:
    """Mean of QoQ equity declines (negative only) over the past 4 quarters."""
    qoq = equity - equity.shift(_TD_QTR)
    only_declines = qoq.where(qoq < 0, 0.0)
    return _rolling_mean(only_declines, _TD_YEAR)


def bsd_109_retearn_mean_4q_declining_depth(retearn: pd.Series) -> pd.Series:
    """Mean of QoQ retained-earnings declines (negative only) over past 4 quarters."""
    qoq = retearn - retearn.shift(_TD_QTR)
    only_declines = qoq.where(qoq < 0, 0.0)
    return _rolling_mean(only_declines, _TD_YEAR)


def bsd_110_assets_mean_4q_declining_depth(assets: pd.Series) -> pd.Series:
    """Mean of QoQ asset declines (negative only) over past 4 quarters."""
    qoq = assets - assets.shift(_TD_QTR)
    only_declines = qoq.where(qoq < 0, 0.0)
    return _rolling_mean(only_declines, _TD_YEAR)


def bsd_111_nav_declining_quarters_8q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Count of quarters with NAV declining QoQ in the past 8 quarters."""
    nav      = assets - liabilities
    declining = (nav < nav.shift(_TD_QTR)).astype(float)
    return _rolling_sum(declining, _TD_2Y)


def bsd_112_invcap_declining_quarters_8q(invcap: pd.Series) -> pd.Series:
    """Count of quarters with invested capital declining QoQ in the past 8 quarters."""
    declining = (invcap < invcap.shift(_TD_QTR)).astype(float)
    return _rolling_sum(declining, _TD_2Y)


def bsd_113_cashnequiv_declining_quarters_8q(cashnequiv: pd.Series) -> pd.Series:
    """Count of quarters with cash declining QoQ in the past 8 quarters."""
    declining = (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float)
    return _rolling_sum(declining, _TD_2Y)


def bsd_114_liab_rising_quarters_8q(liabilities: pd.Series) -> pd.Series:
    """Count of quarters with liabilities rising QoQ in the past 8 quarters."""
    rising = (liabilities > liabilities.shift(_TD_QTR)).astype(float)
    return _rolling_sum(rising, _TD_2Y)


def bsd_115_bs_all8_worsening_flag(assets: pd.Series, liabilities: pd.Series,
                                    equity: pd.Series, cashnequiv: pd.Series,
                                    retearn: pd.Series, workingcapital: pd.Series,
                                    invcap: pd.Series, debt: pd.Series) -> pd.Series:
    """Binary: 1 when all 8 balance-sheet lines are simultaneously worsening QoQ."""
    return (
        (assets < assets.shift(_TD_QTR)) &
        (liabilities > liabilities.shift(_TD_QTR)) &
        (equity < equity.shift(_TD_QTR)) &
        (cashnequiv < cashnequiv.shift(_TD_QTR)) &
        (retearn < retearn.shift(_TD_QTR)) &
        (workingcapital < workingcapital.shift(_TD_QTR)) &
        (invcap < invcap.shift(_TD_QTR)) &
        (debt > debt.shift(_TD_QTR))
    ).astype(float)


def bsd_116_bs_majority6_worsening_flag(assets: pd.Series, liabilities: pd.Series,
                                         equity: pd.Series, cashnequiv: pd.Series,
                                         retearn: pd.Series, workingcapital: pd.Series,
                                         invcap: pd.Series, debt: pd.Series) -> pd.Series:
    """Binary: 1 when at least 6 of 8 balance-sheet lines are worsening QoQ."""
    count = (
        (assets < assets.shift(_TD_QTR)).astype(float) +
        (liabilities > liabilities.shift(_TD_QTR)).astype(float) +
        (equity < equity.shift(_TD_QTR)).astype(float) +
        (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float) +
        (retearn < retearn.shift(_TD_QTR)).astype(float) +
        (workingcapital < workingcapital.shift(_TD_QTR)).astype(float) +
        (invcap < invcap.shift(_TD_QTR)).astype(float) +
        (debt > debt.shift(_TD_QTR)).astype(float)
    )
    return (count >= 6).astype(float)


def bsd_117_equity_vs_4q_avg(equity: pd.Series) -> pd.Series:
    """Equity minus its trailing 4-quarter mean."""
    return equity - _rolling_mean(equity, _TD_YEAR)


def bsd_118_equity_vs_8q_avg(equity: pd.Series) -> pd.Series:
    """Equity minus its trailing 8-quarter mean."""
    return equity - _rolling_mean(equity, _TD_2Y)


def bsd_119_retearn_vs_4q_avg(retearn: pd.Series) -> pd.Series:
    """Retained earnings minus its trailing 4-quarter mean."""
    return retearn - _rolling_mean(retearn, _TD_YEAR)


def bsd_120_cashnequiv_vs_4q_avg(cashnequiv: pd.Series) -> pd.Series:
    """Cash minus its trailing 4-quarter mean."""
    return cashnequiv - _rolling_mean(cashnequiv, _TD_YEAR)


# --- Group I (121-135): Speed and acceleration of decay ---

def bsd_121_equity_qoq_acceleration(equity: pd.Series) -> pd.Series:
    """Second difference of equity over 63-day steps: acceleration of equity decline."""
    d1 = equity - equity.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def bsd_122_assets_qoq_acceleration(assets: pd.Series) -> pd.Series:
    """Second difference of assets over 63-day steps: acceleration of asset decline."""
    d1 = assets - assets.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def bsd_123_nav_qoq_acceleration(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Second difference of net asset value over 63-day steps."""
    nav = assets - liabilities
    d1  = nav - nav.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def bsd_124_debt_qoq_acceleration(debt: pd.Series) -> pd.Series:
    """Second difference of debt over 63-day steps: acceleration of debt accumulation."""
    d1 = debt - debt.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def bsd_125_retearn_qoq_acceleration(retearn: pd.Series) -> pd.Series:
    """Second difference of retained earnings over 63-day steps."""
    d1 = retearn - retearn.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def bsd_126_bs_health_4q_acceleration(assets: pd.Series, liabilities: pd.Series,
                                       equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Second difference of the 4-quarter BS health index (acceleration of health deterioration).
    """
    idx = (
        _zscore_rolling(assets, _TD_YEAR) +
        _zscore_rolling(-liabilities, _TD_YEAR) +
        _zscore_rolling(equity, _TD_YEAR) +
        _zscore_rolling(cashnequiv, _TD_YEAR)
    ) / 4.0
    d1 = idx - idx.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def bsd_127_equity_ewm_deviation(equity: pd.Series) -> pd.Series:
    """Equity minus its 4-quarter EWM (span=252); captures momentum shift."""
    return equity - _ewm_mean(equity, _TD_YEAR)


def bsd_128_assets_ewm_deviation(assets: pd.Series) -> pd.Series:
    """Total assets minus its 4-quarter EWM."""
    return assets - _ewm_mean(assets, _TD_YEAR)


def bsd_129_retearn_ewm_deviation(retearn: pd.Series) -> pd.Series:
    """Retained earnings minus its 4-quarter EWM."""
    return retearn - _ewm_mean(retearn, _TD_YEAR)


def bsd_130_cashnequiv_ewm_deviation(cashnequiv: pd.Series) -> pd.Series:
    """Cash minus its 4-quarter EWM."""
    return cashnequiv - _ewm_mean(cashnequiv, _TD_YEAR)


def bsd_131_equity_3q_momentum(equity: pd.Series) -> pd.Series:
    """Equity change over 3 quarters (189 days = 3 * 63)."""
    return equity - equity.shift(3 * _TD_QTR)


def bsd_132_equity_pct_rank_8q(equity: pd.Series) -> pd.Series:
    """Percentile rank of equity in a trailing 8-quarter window."""
    return _rolling_rank_pct(equity, _TD_2Y)


def bsd_133_retearn_pct_rank_8q(retearn: pd.Series) -> pd.Series:
    """Percentile rank of retained earnings in a trailing 8-quarter window."""
    return _rolling_rank_pct(retearn, _TD_2Y)


def bsd_134_nav_pct_rank_8q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Percentile rank of net asset value in a trailing 8-quarter window."""
    nav = assets - liabilities
    return _rolling_rank_pct(nav, _TD_2Y)


def bsd_135_bs_health_pct_rank_8q(assets: pd.Series, liabilities: pd.Series,
                                    equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of the 4-line BS health index in a trailing 8-quarter window."""
    idx = (
        _zscore_rolling(assets, _TD_YEAR) +
        _zscore_rolling(-liabilities, _TD_YEAR) +
        _zscore_rolling(equity, _TD_YEAR) +
        _zscore_rolling(cashnequiv, _TD_YEAR)
    ) / 4.0
    return _rolling_rank_pct(idx, _TD_2Y)


# --- Group J (136-150): Multi-year decay and composite distress aggregates ---

def bsd_136_equity_3y_drawdown_from_peak(equity: pd.Series) -> pd.Series:
    """Equity vs its 3-year rolling peak."""
    peak = _rolling_max(equity, _TD_3Y)
    return equity - peak


def bsd_137_nav_3y_drawdown_from_peak(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """NAV vs its 3-year rolling peak."""
    nav  = assets - liabilities
    peak = _rolling_max(nav, _TD_3Y)
    return nav - peak


def bsd_138_equity_5y_pct_change(equity: pd.Series) -> pd.Series:
    """Equity 5-year percent change."""
    prior = equity.shift(_TD_5Y)
    return _safe_div_abs(equity - prior, prior)


def bsd_139_assets_3y_pct_change(assets: pd.Series) -> pd.Series:
    """Total assets 3-year percent change."""
    prior = assets.shift(_TD_3Y)
    return _safe_div_abs(assets - prior, prior)


def bsd_140_retearn_3y_pct_change(retearn: pd.Series) -> pd.Series:
    """Retained earnings 3-year percent change."""
    prior = retearn.shift(_TD_3Y)
    return _safe_div_abs(retearn - prior, prior)


def bsd_141_debt_3y_pct_change(debt: pd.Series) -> pd.Series:
    """Total debt 3-year percent change."""
    prior = debt.shift(_TD_3Y)
    return _safe_div_abs(debt - prior, prior)


def bsd_142_invcap_3y_pct_change(invcap: pd.Series) -> pd.Series:
    """Invested capital 3-year percent change."""
    prior = invcap.shift(_TD_3Y)
    return _safe_div_abs(invcap - prior, prior)


def bsd_143_bs_composite_zscore_expanding(assets: pd.Series, liabilities: pd.Series,
                                           equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Expanding-history composite z-score of 4 balance-sheet lines.
    Extreme negative = historically worst balance-sheet positioning.
    """
    def _exp_z(s):
        m  = s.expanding(min_periods=2).mean()
        sd = s.expanding(min_periods=2).std()
        return _safe_div(s - m, sd)

    z_a = _exp_z(assets)
    z_l = _exp_z(-liabilities)
    z_e = _exp_z(equity)
    z_c = _exp_z(cashnequiv)
    return (z_a + z_l + z_e + z_c) / 4.0


def bsd_144_bs_decay_speed_equity_12q_slope(equity: pd.Series) -> pd.Series:
    """
    OLS slope of equity over the trailing 12 quarters (756 days).
    Negative = sustained multi-year equity erosion.
    """
    def _ols_slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return equity.rolling(_TD_3Y, min_periods=max(2, _TD_3Y // 4)).apply(_ols_slope, raw=True)


def bsd_145_bs_decay_speed_assets_12q_slope(assets: pd.Series) -> pd.Series:
    """OLS slope of total assets over trailing 12 quarters."""
    def _ols_slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return assets.rolling(_TD_3Y, min_periods=max(2, _TD_3Y // 4)).apply(_ols_slope, raw=True)


def bsd_146_bs_decay_speed_nav_8q_slope(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """OLS slope of net asset value over trailing 8 quarters."""
    nav = assets - liabilities

    def _ols_slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return nav.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(_ols_slope, raw=True)


def bsd_147_bs_distress_composite_hard_flags(equity: pd.Series, retearn: pd.Series,
                                              workingcapital: pd.Series, debt: pd.Series,
                                              assets: pd.Series) -> pd.Series:
    """
    Count of hard distress flags (range 0-4):
    equity<0, retearn<0, workingcapital<0, debt > 0.8 * assets.
    """
    f1 = (equity < 0).astype(float)
    f2 = (retearn < 0).astype(float)
    f3 = (workingcapital < 0).astype(float)
    f4 = (debt > 0.8 * assets.abs().replace(0, np.nan)).astype(float)
    return f1 + f2 + f3 + f4


def bsd_148_bs_decay_breadth_persistence_4q(assets: pd.Series, liabilities: pd.Series,
                                              equity: pd.Series, cashnequiv: pd.Series,
                                              retearn: pd.Series, workingcapital: pd.Series,
                                              invcap: pd.Series, debt: pd.Series) -> pd.Series:
    """
    Persistence-weighted breadth: rolling 4Q mean of the 8-line deterioration count.
    Captures both how many lines are worsening and how long it has been happening.
    """
    count = (
        (assets < assets.shift(_TD_QTR)).astype(float) +
        (liabilities > liabilities.shift(_TD_QTR)).astype(float) +
        (equity < equity.shift(_TD_QTR)).astype(float) +
        (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float) +
        (retearn < retearn.shift(_TD_QTR)).astype(float) +
        (workingcapital < workingcapital.shift(_TD_QTR)).astype(float) +
        (invcap < invcap.shift(_TD_QTR)).astype(float) +
        (debt > debt.shift(_TD_QTR)).astype(float)
    )
    return _rolling_mean(count, _TD_YEAR)


def bsd_149_bs_decay_breadth_persistence_8q(assets: pd.Series, liabilities: pd.Series,
                                              equity: pd.Series, cashnequiv: pd.Series,
                                              retearn: pd.Series, workingcapital: pd.Series,
                                              invcap: pd.Series, debt: pd.Series) -> pd.Series:
    """8-quarter persistence-weighted breadth of balance-sheet deterioration."""
    count = (
        (assets < assets.shift(_TD_QTR)).astype(float) +
        (liabilities > liabilities.shift(_TD_QTR)).astype(float) +
        (equity < equity.shift(_TD_QTR)).astype(float) +
        (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float) +
        (retearn < retearn.shift(_TD_QTR)).astype(float) +
        (workingcapital < workingcapital.shift(_TD_QTR)).astype(float) +
        (invcap < invcap.shift(_TD_QTR)).astype(float) +
        (debt > debt.shift(_TD_QTR)).astype(float)
    )
    return _rolling_mean(count, _TD_2Y)


def bsd_150_bs_aggregate_decay_score(assets: pd.Series, liabilities: pd.Series,
                                      equity: pd.Series, cashnequiv: pd.Series,
                                      retearn: pd.Series, workingcapital: pd.Series,
                                      invcap: pd.Series, debt: pd.Series) -> pd.Series:
    """
    Ultimate aggregate balance-sheet decay score: 8-line 8Q composite.
    Average of 8 z-scores (positive lines z-scored, negative lines sign-flipped).
    Extreme negative = maximum multi-line, multi-quarter deterioration.
    """
    z_a  = _zscore_rolling(assets, _TD_2Y)
    z_l  = _zscore_rolling(-liabilities, _TD_2Y)
    z_e  = _zscore_rolling(equity, _TD_2Y)
    z_c  = _zscore_rolling(cashnequiv, _TD_2Y)
    z_r  = _zscore_rolling(retearn, _TD_2Y)
    z_w  = _zscore_rolling(workingcapital, _TD_2Y)
    z_i  = _zscore_rolling(invcap, _TD_2Y)
    z_d  = _zscore_rolling(-debt, _TD_2Y)
    return (z_a + z_l + z_e + z_c + z_r + z_w + z_i + z_d) / 8.0


# --- Group K (176-200): Extended asset-quality, liquidity, and composite features ---

def bsd_176_receivables_yoy_change(receivables: pd.Series) -> pd.Series:
    """Receivables YoY absolute change."""
    return receivables - receivables.shift(_TD_YEAR)


def bsd_177_inventory_yoy_change(inventory: pd.Series) -> pd.Series:
    """Inventory YoY absolute change."""
    return inventory - inventory.shift(_TD_YEAR)


def bsd_178_tangibles_2y_pct(tangibles: pd.Series) -> pd.Series:
    """Tangible assets 2-year percent change."""
    prior = tangibles.shift(_TD_2Y)
    return _safe_div_abs(tangibles - prior, prior)


def bsd_179_ppnenet_2y_pct(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E 2-year percent change."""
    prior = ppnenet.shift(_TD_2Y)
    return _safe_div_abs(ppnenet - prior, prior)


def bsd_180_intangibles_2y_pct(intangibles: pd.Series) -> pd.Series:
    """Intangibles 2-year percent change."""
    prior = intangibles.shift(_TD_2Y)
    return _safe_div_abs(intangibles - prior, prior)


def bsd_181_assetsc_yoy_change(assetsc: pd.Series) -> pd.Series:
    """Current assets YoY absolute change."""
    return assetsc - assetsc.shift(_TD_YEAR)


def bsd_182_assetsnc_yoy_change(assetsnc: pd.Series) -> pd.Series:
    """Non-current assets YoY absolute change."""
    return assetsnc - assetsnc.shift(_TD_YEAR)


def bsd_183_liabilitiesc_yoy_change(liabilitiesc: pd.Series) -> pd.Series:
    """Current liabilities YoY absolute change."""
    return liabilitiesc - liabilitiesc.shift(_TD_YEAR)


def bsd_184_liabilitiesnc_yoy_change(liabilitiesnc: pd.Series) -> pd.Series:
    """Non-current liabilities YoY absolute change."""
    return liabilitiesnc - liabilitiesnc.shift(_TD_YEAR)


def bsd_185_debtnc_yoy_change(debtnc: pd.Series) -> pd.Series:
    """Non-current (long-term) debt YoY absolute change."""
    return debtnc - debtnc.shift(_TD_YEAR)


def bsd_186_tangibles_to_assets_ratio(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Tangible assets divided by total assets — tangibility ratio."""
    return _safe_div(tangibles, assets)


def bsd_187_receivables_to_assets_ratio(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """Receivables divided by total assets — receivables concentration."""
    return _safe_div(receivables, assets)


def bsd_188_inventory_to_assets_ratio(inventory: pd.Series, assets: pd.Series) -> pd.Series:
    """Inventory divided by total assets — inventory concentration."""
    return _safe_div(inventory, assets)


def bsd_189_debtnc_to_debt_ratio(debtnc: pd.Series, debt: pd.Series) -> pd.Series:
    """Non-current debt divided by total debt — long-term debt maturity mix."""
    return _safe_div(debtnc, debt.abs().replace(0, np.nan))


def bsd_190_liabilitiesc_to_liabilities_ratio(liabilitiesc: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Current liabilities divided by total liabilities — short-term liability concentration."""
    return _safe_div(liabilitiesc, liabilities.abs().replace(0, np.nan))


def bsd_191_ppnenet_drawdown_from_4q_peak(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E vs its 4-quarter rolling peak."""
    peak = _rolling_max(ppnenet, _TD_YEAR)
    return ppnenet - peak


def bsd_192_tangibles_drawdown_from_expanding_peak(tangibles: pd.Series) -> pd.Series:
    """Tangible assets vs their all-history expanding maximum."""
    peak = tangibles.expanding(min_periods=1).max()
    return tangibles - peak


def bsd_193_receivables_zscore_4q(receivables: pd.Series) -> pd.Series:
    """Z-score of receivables within a trailing 4-quarter window."""
    return _zscore_rolling(receivables, _TD_YEAR)


def bsd_194_inventory_zscore_4q(inventory: pd.Series) -> pd.Series:
    """Z-score of inventory within a trailing 4-quarter window."""
    return _zscore_rolling(inventory, _TD_YEAR)


def bsd_195_assetsc_zscore_4q(assetsc: pd.Series) -> pd.Series:
    """Z-score of current assets within a trailing 4-quarter window."""
    return _zscore_rolling(assetsc, _TD_YEAR)


def bsd_196_tangibles_zscore_8q(tangibles: pd.Series) -> pd.Series:
    """Z-score of tangible assets within a trailing 8-quarter window."""
    return _zscore_rolling(tangibles, _TD_2Y)


def bsd_197_bs_asset_quality_decay_4q(intangibles: pd.Series, assets: pd.Series,
                                       tangibles: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """
    Asset-quality decay index (4Q): z-scores of intangibles concentration (rising = bad)
    and tangibles/ppnenet concentration (falling = bad). Negative = declining asset quality.
    """
    z_intang_conc = _zscore_rolling(intangibles / assets.abs().replace(0, np.nan), _TD_YEAR)
    z_tang_conc   = _zscore_rolling(tangibles / assets.abs().replace(0, np.nan), _TD_YEAR)
    z_ppe_conc    = _zscore_rolling(ppnenet / assets.abs().replace(0, np.nan), _TD_YEAR)
    return (-z_intang_conc + z_tang_conc + z_ppe_conc) / 3.0


def bsd_198_debt_rising_quarters_12q(debt: pd.Series) -> pd.Series:
    """Count of quarters with debt rising QoQ in the past 12 quarters (3 years)."""
    rising = (debt > debt.shift(_TD_QTR)).astype(float)
    return _rolling_sum(rising, _TD_3Y)


def bsd_199_liab_rising_quarters_12q(liabilities: pd.Series) -> pd.Series:
    """Count of quarters with liabilities rising QoQ in the past 12 quarters."""
    rising = (liabilities > liabilities.shift(_TD_QTR)).astype(float)
    return _rolling_sum(rising, _TD_3Y)


def bsd_200_bs_aggregate_decay_score_12q(assets: pd.Series, liabilities: pd.Series,
                                          equity: pd.Series, cashnequiv: pd.Series,
                                          retearn: pd.Series, workingcapital: pd.Series,
                                          invcap: pd.Series, debt: pd.Series) -> pd.Series:
    """
    Aggregate balance-sheet decay score over 12-quarter (3-year) window.
    Average of 8 z-scores; negative = maximum multi-line multi-year deterioration.
    """
    z_a = _zscore_rolling(assets, _TD_3Y)
    z_l = _zscore_rolling(-liabilities, _TD_3Y)
    z_e = _zscore_rolling(equity, _TD_3Y)
    z_c = _zscore_rolling(cashnequiv, _TD_3Y)
    z_r = _zscore_rolling(retearn, _TD_3Y)
    z_w = _zscore_rolling(workingcapital, _TD_3Y)
    z_i = _zscore_rolling(invcap, _TD_3Y)
    z_d = _zscore_rolling(-debt, _TD_3Y)
    return (z_a + z_l + z_e + z_c + z_r + z_w + z_i + z_d) / 8.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

BALANCE_SHEET_DECAY_REGISTRY_076_150 = {
    "bsd_076_intangibles_yoy_change":                      {"inputs": ["intangibles"],                                                                                           "func": bsd_076_intangibles_yoy_change},
    "bsd_077_intangibles_yoy_pct":                         {"inputs": ["intangibles"],                                                                                           "func": bsd_077_intangibles_yoy_pct},
    "bsd_078_ppnenet_yoy_change":                          {"inputs": ["ppnenet"],                                                                                               "func": bsd_078_ppnenet_yoy_change},
    "bsd_079_ppnenet_yoy_pct":                             {"inputs": ["ppnenet"],                                                                                               "func": bsd_079_ppnenet_yoy_pct},
    "bsd_080_tangibles_yoy_change":                        {"inputs": ["tangibles"],                                                                                             "func": bsd_080_tangibles_yoy_change},
    "bsd_081_tangibles_yoy_pct":                           {"inputs": ["tangibles"],                                                                                             "func": bsd_081_tangibles_yoy_pct},
    "bsd_082_intangibles_to_assets_ratio":                 {"inputs": ["intangibles", "assets"],                                                                                 "func": bsd_082_intangibles_to_assets_ratio},
    "bsd_083_ppnenet_to_assets_ratio":                     {"inputs": ["ppnenet", "assets"],                                                                                     "func": bsd_083_ppnenet_to_assets_ratio},
    "bsd_084_assetsc_to_assets_ratio":                     {"inputs": ["assetsc", "assets"],                                                                                     "func": bsd_084_assetsc_to_assets_ratio},
    "bsd_085_assetsnc_yoy_pct":                            {"inputs": ["assetsnc"],                                                                                              "func": bsd_085_assetsnc_yoy_pct},
    "bsd_086_receivables_yoy_pct":                         {"inputs": ["receivables"],                                                                                           "func": bsd_086_receivables_yoy_pct},
    "bsd_087_inventory_yoy_pct":                           {"inputs": ["inventory"],                                                                                             "func": bsd_087_inventory_yoy_pct},
    "bsd_088_intangibles_drawdown_from_expanding_peak":    {"inputs": ["intangibles"],                                                                                           "func": bsd_088_intangibles_drawdown_from_expanding_peak},
    "bsd_089_ppnenet_drawdown_from_expanding_peak":        {"inputs": ["ppnenet"],                                                                                               "func": bsd_089_ppnenet_drawdown_from_expanding_peak},
    "bsd_090_intangibles_drawdown_pct_from_4q_peak":       {"inputs": ["intangibles"],                                                                                           "func": bsd_090_intangibles_drawdown_pct_from_4q_peak},
    "bsd_091_liab_to_assets_yoy_change":                   {"inputs": ["liabilities", "assets"],                                                                                 "func": bsd_091_liab_to_assets_yoy_change},
    "bsd_092_debt_to_equity_yoy_change":                   {"inputs": ["debt", "equity"],                                                                                        "func": bsd_092_debt_to_equity_yoy_change},
    "bsd_093_debt_to_assets_yoy_change":                   {"inputs": ["debt", "assets"],                                                                                        "func": bsd_093_debt_to_assets_yoy_change},
    "bsd_094_liab_to_equity_yoy_change":                   {"inputs": ["liabilities", "equity"],                                                                                 "func": bsd_094_liab_to_equity_yoy_change},
    "bsd_095_liab_to_assets_zscore_4q":                    {"inputs": ["liabilities", "assets"],                                                                                 "func": bsd_095_liab_to_assets_zscore_4q},
    "bsd_096_debt_to_assets_zscore_4q":                    {"inputs": ["debt", "assets"],                                                                                        "func": bsd_096_debt_to_assets_zscore_4q},
    "bsd_097_debt_to_equity_zscore_8q":                    {"inputs": ["debt", "equity"],                                                                                        "func": bsd_097_debt_to_equity_zscore_8q},
    "bsd_098_liab_to_assets_pct_rank_8q":                  {"inputs": ["liabilities", "assets"],                                                                                 "func": bsd_098_liab_to_assets_pct_rank_8q},
    "bsd_099_debt_rising_quarters_4q":                     {"inputs": ["debt"],                                                                                                  "func": bsd_099_debt_rising_quarters_4q},
    "bsd_100_debt_rising_quarters_8q":                     {"inputs": ["debt"],                                                                                                  "func": bsd_100_debt_rising_quarters_8q},
    "bsd_101_liab_rising_quarters_4q":                     {"inputs": ["liabilities"],                                                                                           "func": bsd_101_liab_rising_quarters_4q},
    "bsd_102_equity_negative_quarters_4q":                 {"inputs": ["equity"],                                                                                                "func": bsd_102_equity_negative_quarters_4q},
    "bsd_103_retearn_negative_quarters_4q":                {"inputs": ["retearn"],                                                                                               "func": bsd_103_retearn_negative_quarters_4q},
    "bsd_104_wc_negative_quarters_4q":                     {"inputs": ["workingcapital"],                                                                                        "func": bsd_104_wc_negative_quarters_4q},
    "bsd_105_equity_consecutive_decline_streak":           {"inputs": ["equity"],                                                                                                "func": bsd_105_equity_consecutive_decline_streak},
    "bsd_106_bs_deterioration_fraction_4lines_4q":         {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                                                        "func": bsd_106_bs_deterioration_fraction_4lines_4q},
    "bsd_107_bs_deterioration_fraction_8lines_4q_avg":     {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital", "invcap", "debt"],         "func": bsd_107_bs_deterioration_fraction_8lines_4q_avg},
    "bsd_108_equity_mean_4q_declining_depth":              {"inputs": ["equity"],                                                                                                "func": bsd_108_equity_mean_4q_declining_depth},
    "bsd_109_retearn_mean_4q_declining_depth":             {"inputs": ["retearn"],                                                                                               "func": bsd_109_retearn_mean_4q_declining_depth},
    "bsd_110_assets_mean_4q_declining_depth":              {"inputs": ["assets"],                                                                                                "func": bsd_110_assets_mean_4q_declining_depth},
    "bsd_111_nav_declining_quarters_8q":                   {"inputs": ["assets", "liabilities"],                                                                                 "func": bsd_111_nav_declining_quarters_8q},
    "bsd_112_invcap_declining_quarters_8q":                {"inputs": ["invcap"],                                                                                                "func": bsd_112_invcap_declining_quarters_8q},
    "bsd_113_cashnequiv_declining_quarters_8q":            {"inputs": ["cashnequiv"],                                                                                            "func": bsd_113_cashnequiv_declining_quarters_8q},
    "bsd_114_liab_rising_quarters_8q":                     {"inputs": ["liabilities"],                                                                                           "func": bsd_114_liab_rising_quarters_8q},
    "bsd_115_bs_all8_worsening_flag":                      {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital", "invcap", "debt"],         "func": bsd_115_bs_all8_worsening_flag},
    "bsd_116_bs_majority6_worsening_flag":                 {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital", "invcap", "debt"],         "func": bsd_116_bs_majority6_worsening_flag},
    "bsd_117_equity_vs_4q_avg":                            {"inputs": ["equity"],                                                                                                "func": bsd_117_equity_vs_4q_avg},
    "bsd_118_equity_vs_8q_avg":                            {"inputs": ["equity"],                                                                                                "func": bsd_118_equity_vs_8q_avg},
    "bsd_119_retearn_vs_4q_avg":                           {"inputs": ["retearn"],                                                                                               "func": bsd_119_retearn_vs_4q_avg},
    "bsd_120_cashnequiv_vs_4q_avg":                        {"inputs": ["cashnequiv"],                                                                                            "func": bsd_120_cashnequiv_vs_4q_avg},
    "bsd_121_equity_qoq_acceleration":                     {"inputs": ["equity"],                                                                                                "func": bsd_121_equity_qoq_acceleration},
    "bsd_122_assets_qoq_acceleration":                     {"inputs": ["assets"],                                                                                                "func": bsd_122_assets_qoq_acceleration},
    "bsd_123_nav_qoq_acceleration":                        {"inputs": ["assets", "liabilities"],                                                                                 "func": bsd_123_nav_qoq_acceleration},
    "bsd_124_debt_qoq_acceleration":                       {"inputs": ["debt"],                                                                                                  "func": bsd_124_debt_qoq_acceleration},
    "bsd_125_retearn_qoq_acceleration":                    {"inputs": ["retearn"],                                                                                               "func": bsd_125_retearn_qoq_acceleration},
    "bsd_126_bs_health_4q_acceleration":                   {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                                                        "func": bsd_126_bs_health_4q_acceleration},
    "bsd_127_equity_ewm_deviation":                        {"inputs": ["equity"],                                                                                                "func": bsd_127_equity_ewm_deviation},
    "bsd_128_assets_ewm_deviation":                        {"inputs": ["assets"],                                                                                                "func": bsd_128_assets_ewm_deviation},
    "bsd_129_retearn_ewm_deviation":                       {"inputs": ["retearn"],                                                                                               "func": bsd_129_retearn_ewm_deviation},
    "bsd_130_cashnequiv_ewm_deviation":                    {"inputs": ["cashnequiv"],                                                                                            "func": bsd_130_cashnequiv_ewm_deviation},
    "bsd_131_equity_3q_momentum":                          {"inputs": ["equity"],                                                                                                "func": bsd_131_equity_3q_momentum},
    "bsd_132_equity_pct_rank_8q":                          {"inputs": ["equity"],                                                                                                "func": bsd_132_equity_pct_rank_8q},
    "bsd_133_retearn_pct_rank_8q":                         {"inputs": ["retearn"],                                                                                               "func": bsd_133_retearn_pct_rank_8q},
    "bsd_134_nav_pct_rank_8q":                             {"inputs": ["assets", "liabilities"],                                                                                 "func": bsd_134_nav_pct_rank_8q},
    "bsd_135_bs_health_pct_rank_8q":                       {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                                                        "func": bsd_135_bs_health_pct_rank_8q},
    "bsd_136_equity_3y_drawdown_from_peak":                {"inputs": ["equity"],                                                                                                "func": bsd_136_equity_3y_drawdown_from_peak},
    "bsd_137_nav_3y_drawdown_from_peak":                   {"inputs": ["assets", "liabilities"],                                                                                 "func": bsd_137_nav_3y_drawdown_from_peak},
    "bsd_138_equity_5y_pct_change":                        {"inputs": ["equity"],                                                                                                "func": bsd_138_equity_5y_pct_change},
    "bsd_139_assets_3y_pct_change":                        {"inputs": ["assets"],                                                                                                "func": bsd_139_assets_3y_pct_change},
    "bsd_140_retearn_3y_pct_change":                       {"inputs": ["retearn"],                                                                                               "func": bsd_140_retearn_3y_pct_change},
    "bsd_141_debt_3y_pct_change":                          {"inputs": ["debt"],                                                                                                  "func": bsd_141_debt_3y_pct_change},
    "bsd_142_invcap_3y_pct_change":                        {"inputs": ["invcap"],                                                                                                "func": bsd_142_invcap_3y_pct_change},
    "bsd_143_bs_composite_zscore_expanding":               {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                                                        "func": bsd_143_bs_composite_zscore_expanding},
    "bsd_144_bs_decay_speed_equity_12q_slope":             {"inputs": ["equity"],                                                                                                "func": bsd_144_bs_decay_speed_equity_12q_slope},
    "bsd_145_bs_decay_speed_assets_12q_slope":             {"inputs": ["assets"],                                                                                                "func": bsd_145_bs_decay_speed_assets_12q_slope},
    "bsd_146_bs_decay_speed_nav_8q_slope":                 {"inputs": ["assets", "liabilities"],                                                                                 "func": bsd_146_bs_decay_speed_nav_8q_slope},
    "bsd_147_bs_distress_composite_hard_flags":            {"inputs": ["equity", "retearn", "workingcapital", "debt", "assets"],                                                 "func": bsd_147_bs_distress_composite_hard_flags},
    "bsd_148_bs_decay_breadth_persistence_4q":             {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital", "invcap", "debt"],         "func": bsd_148_bs_decay_breadth_persistence_4q},
    "bsd_149_bs_decay_breadth_persistence_8q":             {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital", "invcap", "debt"],         "func": bsd_149_bs_decay_breadth_persistence_8q},
    "bsd_150_bs_aggregate_decay_score":                    {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital", "invcap", "debt"],         "func": bsd_150_bs_aggregate_decay_score},
    "bsd_176_receivables_yoy_change":                      {"inputs": ["receivables"],                                                                                            "func": bsd_176_receivables_yoy_change},
    "bsd_177_inventory_yoy_change":                        {"inputs": ["inventory"],                                                                                              "func": bsd_177_inventory_yoy_change},
    "bsd_178_tangibles_2y_pct":                            {"inputs": ["tangibles"],                                                                                              "func": bsd_178_tangibles_2y_pct},
    "bsd_179_ppnenet_2y_pct":                              {"inputs": ["ppnenet"],                                                                                                "func": bsd_179_ppnenet_2y_pct},
    "bsd_180_intangibles_2y_pct":                          {"inputs": ["intangibles"],                                                                                            "func": bsd_180_intangibles_2y_pct},
    "bsd_181_assetsc_yoy_change":                          {"inputs": ["assetsc"],                                                                                                "func": bsd_181_assetsc_yoy_change},
    "bsd_182_assetsnc_yoy_change":                         {"inputs": ["assetsnc"],                                                                                               "func": bsd_182_assetsnc_yoy_change},
    "bsd_183_liabilitiesc_yoy_change":                     {"inputs": ["liabilitiesc"],                                                                                           "func": bsd_183_liabilitiesc_yoy_change},
    "bsd_184_liabilitiesnc_yoy_change":                    {"inputs": ["liabilitiesnc"],                                                                                          "func": bsd_184_liabilitiesnc_yoy_change},
    "bsd_185_debtnc_yoy_change":                           {"inputs": ["debtnc"],                                                                                                 "func": bsd_185_debtnc_yoy_change},
    "bsd_186_tangibles_to_assets_ratio":                   {"inputs": ["tangibles", "assets"],                                                                                    "func": bsd_186_tangibles_to_assets_ratio},
    "bsd_187_receivables_to_assets_ratio":                 {"inputs": ["receivables", "assets"],                                                                                  "func": bsd_187_receivables_to_assets_ratio},
    "bsd_188_inventory_to_assets_ratio":                   {"inputs": ["inventory", "assets"],                                                                                    "func": bsd_188_inventory_to_assets_ratio},
    "bsd_189_debtnc_to_debt_ratio":                        {"inputs": ["debtnc", "debt"],                                                                                         "func": bsd_189_debtnc_to_debt_ratio},
    "bsd_190_liabilitiesc_to_liabilities_ratio":           {"inputs": ["liabilitiesc", "liabilities"],                                                                            "func": bsd_190_liabilitiesc_to_liabilities_ratio},
    "bsd_191_ppnenet_drawdown_from_4q_peak":               {"inputs": ["ppnenet"],                                                                                                "func": bsd_191_ppnenet_drawdown_from_4q_peak},
    "bsd_192_tangibles_drawdown_from_expanding_peak":      {"inputs": ["tangibles"],                                                                                              "func": bsd_192_tangibles_drawdown_from_expanding_peak},
    "bsd_193_receivables_zscore_4q":                       {"inputs": ["receivables"],                                                                                            "func": bsd_193_receivables_zscore_4q},
    "bsd_194_inventory_zscore_4q":                         {"inputs": ["inventory"],                                                                                              "func": bsd_194_inventory_zscore_4q},
    "bsd_195_assetsc_zscore_4q":                           {"inputs": ["assetsc"],                                                                                                "func": bsd_195_assetsc_zscore_4q},
    "bsd_196_tangibles_zscore_8q":                         {"inputs": ["tangibles"],                                                                                              "func": bsd_196_tangibles_zscore_8q},
    "bsd_197_bs_asset_quality_decay_4q":                   {"inputs": ["intangibles", "assets", "tangibles", "ppnenet"],                                                          "func": bsd_197_bs_asset_quality_decay_4q},
    "bsd_198_debt_rising_quarters_12q":                    {"inputs": ["debt"],                                                                                                   "func": bsd_198_debt_rising_quarters_12q},
    "bsd_199_liab_rising_quarters_12q":                    {"inputs": ["liabilities"],                                                                                            "func": bsd_199_liab_rising_quarters_12q},
    "bsd_200_bs_aggregate_decay_score_12q":                {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital", "invcap", "debt"],          "func": bsd_200_bs_aggregate_decay_score_12q},
}
