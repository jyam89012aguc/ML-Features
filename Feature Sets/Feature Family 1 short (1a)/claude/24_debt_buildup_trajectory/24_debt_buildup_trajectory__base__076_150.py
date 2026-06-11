"""debt_buildup_trajectory base features - Pipeline 1a-inverse short-side blowup family.

Multi-quarter trajectory of debt buildup, coverage erosion, and refinancing pressure
preceding price peaks. Inputs: SF1 quarterly fundamentals. PIT-clean: right-anchored
rolling, explicit min_periods, no centered windows, no forward-looking shifts.
Self-contained per HANDOFF; helpers redefined locally.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq(s):
    return s.diff()


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())



def f24_dbtj_076_debt_issuance_minus_capex_to_assets(debt, capex, assets):
    return _safe_div(debt.diff().clip(lower=0).rolling(4, min_periods=1).sum() - _ttm(capex).abs(), _avg4(assets))

def f24_dbtj_077_ncff_minus_capex_4q_to_debt(ncff, capex, debt):
    return _safe_div(_ttm(ncff) - _ttm(capex).abs(), _avg4(debt))

def f24_dbtj_078_debt_funded_buyback_proxy(debt, ncff):
    return _safe_div(debt.diff().rolling(4, min_periods=1).sum(), _ttm(ncff).abs())

def f24_dbtj_079_external_financing_share_8q(debt, equity):
    return _safe_div(debt.diff().rolling(8, min_periods=2).sum(), debt.diff().rolling(8, min_periods=2).sum().abs() + equity.diff().rolling(8, min_periods=2).sum().abs())

def f24_dbtj_080_debt_issuance_zscore_12q(debt):
    return _rolling_zscore(debt.diff(), 12, min_periods=4)

def f24_dbtj_081_debt_to_equity_zscore_12q(debt, equity):
    return _rolling_zscore(_safe_div(debt, equity), 12, min_periods=4)

def f24_dbtj_082_debt_to_assets_zscore_8q(debt, assets):
    return _rolling_zscore(_safe_div(debt, assets), 8, min_periods=3)

def f24_dbtj_083_net_debt_to_ebitda_zscore_12q(debt, cashneq, ebitda):
    return _rolling_zscore(_safe_div(debt - cashneq, _ttm(ebitda)), 12, min_periods=4)

def f24_dbtj_084_interest_coverage_zscore_12q(ebit, intexp):
    return _rolling_zscore(_safe_div(_ttm(ebit), _ttm(intexp)), 12, min_periods=4)

def f24_dbtj_085_leverage_max_minus_min_8q(debt, equity):
    return _safe_div(debt, equity).rolling(8, min_periods=3).max() - _safe_div(debt, equity).rolling(8, min_periods=3).min()

def f24_dbtj_086_leverage_at_max_8q_indicator(debt, equity):
    return (_safe_div(debt, equity) >= _safe_div(debt, equity).rolling(8, min_periods=3).max() - 1e-9).astype(float)

def f24_dbtj_087_debt_to_assets_above_4q_mean(debt, assets):
    return _safe_div(debt, assets) - _safe_div(debt, assets).rolling(4, min_periods=2).mean()

def f24_dbtj_088_leverage_volatility_8q(debt, equity):
    return _safe_div(debt, equity).rolling(8, min_periods=3).std()

def f24_dbtj_089_leverage_cv_12q(debt, equity):
    return _safe_div(_safe_div(debt, equity).rolling(12, min_periods=4).std(), _safe_div(debt, equity).rolling(12, min_periods=4).mean().abs())

def f24_dbtj_090_leverage_drift_8q_to_12q(debt, assets):
    return _safe_div(debt, assets).rolling(8, min_periods=3).mean() - _safe_div(debt, assets).rolling(12, min_periods=4).mean()

def f24_dbtj_091_debt_share_assets_percentile_rank_12q(debt, assets):
    return _safe_div(debt, assets).rolling(12, min_periods=4).rank(pct=True)

def f24_dbtj_092_net_leverage_percentile_rank_12q(debt, cashneq, ebitda):
    return _safe_div(debt - cashneq, _ttm(ebitda)).rolling(12, min_periods=4).rank(pct=True)

def f24_dbtj_093_interest_coverage_percentile_rank_12q(ebit, intexp):
    return _safe_div(_ttm(ebit), _ttm(intexp)).rolling(12, min_periods=4).rank(pct=True)

def f24_dbtj_094_debt_yoy_pct_rolling_max_8q(debt):
    return _yoy_pct(debt).rolling(8, min_periods=2).max()

def f24_dbtj_095_leverage_regime_break_indicator(debt, assets):
    return (_safe_div(debt, assets) > _safe_div(debt, assets).rolling(12, min_periods=4).mean() + _safe_div(debt, assets).rolling(12, min_periods=4).std()).astype(float)

def f24_dbtj_096_debt_to_ebitda_above_4x_persistence(debt, ebitda):
    return (_safe_div(_avg4(debt), _ttm(ebitda)) > 4.0).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_097_interest_coverage_below_2x_persistence(ebit, intexp):
    return (_safe_div(_ttm(ebit), _ttm(intexp)) < 2.0).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_098_currentratio_below_1_persistence(assetsc, liabilitiesc):
    return (_safe_div(_avg4(assetsc), _avg4(liabilitiesc)) < 1.0).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_099_negative_fcf_with_rising_debt_8q(fcf, debt):
    return ((_ttm(fcf) < 0) & (debt.diff(4) > 0)).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_100_debt_to_capital_above_60pct_persistence(debt, equity):
    return (_safe_div(_avg4(debt), _avg4(debt) + _avg4(equity)) > 0.6).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_101_interest_to_ocf_above_30pct_persistence(intexp, ncfo):
    return (_safe_div(_ttm(intexp), _ttm(ncfo).abs()) > 0.3).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_102_debt_growth_above_25pct_yoy_persistence(debt):
    return (_yoy_pct(_avg4(debt)) > 0.25).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_103_negative_workingcapital_persistence(workingcapital):
    return (workingcapital < 0).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_104_cash_burn_with_rising_debt_persistence(cashneq, debt):
    return ((cashneq.diff() < 0) & (debt.diff() > 0)).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_105_debtc_above_cash_persistence(debtc, cashneq):
    return (_avg4(debtc) > _avg4(cashneq)).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_106_altman_z_proxy_below_1p8_persistence(workingcapital, retearn, ebit, equity, revenue, assets, liabilities):
    return ((_safe_div(1.2 * workingcapital + 1.4 * retearn + 3.3 * _ttm(ebit) + 0.6 * equity + _ttm(revenue), assets) - _safe_div(liabilities, assets)) < 1.8).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_107_debt_to_revenue_above_1_persistence(debt, revenue):
    return (_safe_div(_avg4(debt), _ttm(revenue)) > 1.0).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_108_net_debt_to_ebitda_above_5x_persistence(debt, cashneq, ebitda):
    return (_safe_div(_avg4(debt - cashneq), _ttm(ebitda)) > 5.0).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_109_negative_equity_emerging_indicator(equity):
    return ((equity < 0) & (equity.shift(4) >= 0)).astype(float).rolling(4, min_periods=1).max()

def f24_dbtj_110_tangible_equity_negative_persistence(equity, intangibles):
    return ((equity - intangibles) < 0).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_111_liabilitiesc_share_of_liabilities_avg4(liabilitiesc, liabilities):
    return _safe_div(_avg4(liabilitiesc), _avg4(liabilities))

def f24_dbtj_112_noncurrent_liab_growth_yoy_pct(liabilities, liabilitiesc):
    return _yoy_pct(_avg4(liabilities - liabilitiesc))

def f24_dbtj_113_current_liab_growth_minus_revenue_growth(liabilitiesc, revenue):
    return _yoy_pct(_avg4(liabilitiesc)) - _yoy_pct(_ttm(revenue))

def f24_dbtj_114_liabilities_to_equity_avg4(liabilities, equity):
    return _safe_div(_avg4(liabilities), _avg4(equity))

def f24_dbtj_115_non_debt_liab_share_trend(liabilities, debt):
    return _safe_div(_avg4(liabilities - debt), _avg4(liabilities))

def f24_dbtj_116_payables_funding_share_of_liabilities(payables, liabilities):
    return _safe_div(_avg4(payables), _avg4(liabilities))

def f24_dbtj_117_payables_to_debt_avg4(payables, debt):
    return _safe_div(_avg4(payables), _avg4(debt))

def f24_dbtj_118_liabilities_growth_persistence_12q(liabilities):
    return (liabilities.diff() > 0).astype(float).rolling(12, min_periods=3).mean()

def f24_dbtj_119_liabilities_yoy_pct_zscore_12q(liabilities):
    return _rolling_zscore(_yoy_pct(liabilities), 12, min_periods=4)

def f24_dbtj_120_liabilities_to_assets_zscore_12q(liabilities, assets):
    return _rolling_zscore(_safe_div(liabilities, assets), 12, min_periods=4)

def f24_dbtj_121_current_liab_to_cash_trend(liabilitiesc, cashneq):
    return _safe_div(_avg4(liabilitiesc), _avg4(cashneq))

def f24_dbtj_122_liabilities_minus_assets_to_assets(liabilities, assets):
    return _safe_div(_avg4(liabilities) - _avg4(assets), _avg4(assets).abs())

def f24_dbtj_123_tangibles_share_of_assets_avg4(tangibles, assets):
    return _safe_div(_avg4(tangibles), _avg4(assets))

def f24_dbtj_124_tangibles_growth_minus_debt_growth_yoy(tangibles, debt):
    return _yoy_pct(_avg4(tangibles)) - _yoy_pct(_avg4(debt))

def f24_dbtj_125_ppnenet_share_of_assets_decline(ppnenet, assets):
    return _safe_div(_avg4(ppnenet), _avg4(assets)).diff(8)

def f24_dbtj_126_intangibles_growth_yoy_pct(intangibles):
    return _yoy_pct(_avg4(intangibles))

def f24_dbtj_127_goodwill_proxy_to_debt_trend(intangibles, debt):
    return _safe_div(_avg4(intangibles), _avg4(debt))

def f24_dbtj_128_asset_growth_funded_by_debt_share_yoy(assets, debt):
    return _safe_div(_avg4(debt) - _avg4(debt).shift(4), (_avg4(assets) - _avg4(assets).shift(4)).abs())

def f24_dbtj_129_tangible_assets_per_dollar_debt_trend(tangibles, debt):
    return _safe_div(_avg4(tangibles), _avg4(debt))

def f24_dbtj_130_asset_backing_erosion_8q(tangibles, debt):
    return -_safe_div(_avg4(tangibles), _avg4(debt)).diff(8)

def f24_dbtj_131_investments_to_debt_trend(investments, debt):
    return _safe_div(_avg4(investments), _avg4(debt))

def f24_dbtj_132_ppnenet_per_dollar_debt_avg4(ppnenet, debt):
    return _safe_div(_avg4(ppnenet), _avg4(debt))

def f24_dbtj_133_leverage_up_coverage_down_indicator(debt, assets, ebit, intexp):
    return ((_safe_div(debt, assets).diff(4) > 0) & (_safe_div(_ttm(ebit), _ttm(intexp)).diff(4) < 0)).astype(float).rolling(4, min_periods=1).mean()

def f24_dbtj_134_net_debt_up_cash_down_indicator(debt, cashneq):
    return ((debt.diff(4) > 0) & (cashneq.diff(4) < 0)).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_135_debt_up_revenue_down_8q(debt, revenue):
    return ((debt.diff(4) > 0) & (_ttm(revenue).diff(4) < 0)).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_136_debt_up_margin_down_indicator(debt, opinc, revenue):
    return ((debt.diff(4) > 0) & (_safe_div(_ttm(opinc), _ttm(revenue)).diff(4) < 0)).astype(float).rolling(8, min_periods=2).mean()

def f24_dbtj_137_leverage_acceleration_into_peak_proxy(debt, assets):
    return _safe_div(debt, assets).diff(4) - _safe_div(debt, assets).diff(4).shift(4)

def f24_dbtj_138_compound_stress_score_avg4(debt, ebitda, ebit, intexp, cashneq):
    return (_safe_div(_avg4(debt - cashneq), _ttm(ebitda)) - _safe_div(_ttm(ebit), _ttm(intexp))).rolling(4, min_periods=2).mean()

def f24_dbtj_139_drawdown_in_coverage_from_8q_max(ebit, intexp):
    return _safe_div(_ttm(ebit), _ttm(intexp)) - _safe_div(_ttm(ebit), _ttm(intexp)).rolling(8, min_periods=3).max()

def f24_dbtj_140_drawup_in_leverage_from_8q_min(debt, assets):
    return _safe_div(debt, assets) - _safe_div(debt, assets).rolling(8, min_periods=3).min()

def f24_dbtj_141_log_debt_minus_log_ebitda_ttm(debt, ebitda):
    return _safe_log(_avg4(debt)) - _safe_log(_ttm(ebitda))

def f24_dbtj_142_debt_ema_trend_4q_minus_8q(debt):
    return debt.rolling(4, min_periods=1).mean() - debt.rolling(8, min_periods=2).mean()

def f24_dbtj_143_net_debt_ema_trend_4q_minus_12q(debt, cashneq):
    return (debt - cashneq).rolling(4, min_periods=1).mean() - (debt - cashneq).rolling(12, min_periods=3).mean()

def f24_dbtj_144_debt_change_to_ocf_change_ratio_4q(debt, ncfo):
    return _safe_div(_avg4(debt).diff(4), _ttm(ncfo).diff(4).abs())

def f24_dbtj_145_leverage_trend_consistency_8q(debt, assets):
    return (_safe_div(debt, assets).diff() > 0).astype(float).rolling(8, min_periods=3).mean()

def f24_dbtj_146_coverage_trend_consistency_8q(ebit, intexp):
    return (_safe_div(_ttm(ebit), _ttm(intexp)).diff() < 0).astype(float).rolling(8, min_periods=3).mean()

def f24_dbtj_147_debt_to_assets_acceleration_4q_vs_12q(debt, assets):
    return _safe_div(debt, assets).diff(4) - _safe_div(debt, assets).diff(12)

def f24_dbtj_148_interest_burden_growth_yoy_pct(intexp):
    return _yoy_pct(_ttm(intexp))

def f24_dbtj_149_net_debt_to_marketcap_proxy_trend(debt, cashneq, equity):
    return _safe_div(_avg4(debt - cashneq), _avg4(equity).abs())

def f24_dbtj_150_compound_leverage_coverage_index(debt, assets, ebit, intexp, cashneq):
    return _safe_div(_avg4(debt - cashneq), _avg4(assets)) - _safe_div(_ttm(ebit), _ttm(intexp))


DEBT_BUILDUP_TRAJECTORY_BASE_REGISTRY_076_150 = {
    "f24_dbtj_076_debt_issuance_minus_capex_to_assets": {"inputs": ["debt", "capex", "assets"], "func": f24_dbtj_076_debt_issuance_minus_capex_to_assets},
    "f24_dbtj_077_ncff_minus_capex_4q_to_debt": {"inputs": ["ncff", "capex", "debt"], "func": f24_dbtj_077_ncff_minus_capex_4q_to_debt},
    "f24_dbtj_078_debt_funded_buyback_proxy": {"inputs": ["debt", "ncff"], "func": f24_dbtj_078_debt_funded_buyback_proxy},
    "f24_dbtj_079_external_financing_share_8q": {"inputs": ["debt", "equity"], "func": f24_dbtj_079_external_financing_share_8q},
    "f24_dbtj_080_debt_issuance_zscore_12q": {"inputs": ["debt"], "func": f24_dbtj_080_debt_issuance_zscore_12q},
    "f24_dbtj_081_debt_to_equity_zscore_12q": {"inputs": ["debt", "equity"], "func": f24_dbtj_081_debt_to_equity_zscore_12q},
    "f24_dbtj_082_debt_to_assets_zscore_8q": {"inputs": ["debt", "assets"], "func": f24_dbtj_082_debt_to_assets_zscore_8q},
    "f24_dbtj_083_net_debt_to_ebitda_zscore_12q": {"inputs": ["debt", "cashneq", "ebitda"], "func": f24_dbtj_083_net_debt_to_ebitda_zscore_12q},
    "f24_dbtj_084_interest_coverage_zscore_12q": {"inputs": ["ebit", "intexp"], "func": f24_dbtj_084_interest_coverage_zscore_12q},
    "f24_dbtj_085_leverage_max_minus_min_8q": {"inputs": ["debt", "equity"], "func": f24_dbtj_085_leverage_max_minus_min_8q},
    "f24_dbtj_086_leverage_at_max_8q_indicator": {"inputs": ["debt", "equity"], "func": f24_dbtj_086_leverage_at_max_8q_indicator},
    "f24_dbtj_087_debt_to_assets_above_4q_mean": {"inputs": ["debt", "assets"], "func": f24_dbtj_087_debt_to_assets_above_4q_mean},
    "f24_dbtj_088_leverage_volatility_8q": {"inputs": ["debt", "equity"], "func": f24_dbtj_088_leverage_volatility_8q},
    "f24_dbtj_089_leverage_cv_12q": {"inputs": ["debt", "equity"], "func": f24_dbtj_089_leverage_cv_12q},
    "f24_dbtj_090_leverage_drift_8q_to_12q": {"inputs": ["debt", "assets"], "func": f24_dbtj_090_leverage_drift_8q_to_12q},
    "f24_dbtj_091_debt_share_assets_percentile_rank_12q": {"inputs": ["debt", "assets"], "func": f24_dbtj_091_debt_share_assets_percentile_rank_12q},
    "f24_dbtj_092_net_leverage_percentile_rank_12q": {"inputs": ["debt", "cashneq", "ebitda"], "func": f24_dbtj_092_net_leverage_percentile_rank_12q},
    "f24_dbtj_093_interest_coverage_percentile_rank_12q": {"inputs": ["ebit", "intexp"], "func": f24_dbtj_093_interest_coverage_percentile_rank_12q},
    "f24_dbtj_094_debt_yoy_pct_rolling_max_8q": {"inputs": ["debt"], "func": f24_dbtj_094_debt_yoy_pct_rolling_max_8q},
    "f24_dbtj_095_leverage_regime_break_indicator": {"inputs": ["debt", "assets"], "func": f24_dbtj_095_leverage_regime_break_indicator},
    "f24_dbtj_096_debt_to_ebitda_above_4x_persistence": {"inputs": ["debt", "ebitda"], "func": f24_dbtj_096_debt_to_ebitda_above_4x_persistence},
    "f24_dbtj_097_interest_coverage_below_2x_persistence": {"inputs": ["ebit", "intexp"], "func": f24_dbtj_097_interest_coverage_below_2x_persistence},
    "f24_dbtj_098_currentratio_below_1_persistence": {"inputs": ["assetsc", "liabilitiesc"], "func": f24_dbtj_098_currentratio_below_1_persistence},
    "f24_dbtj_099_negative_fcf_with_rising_debt_8q": {"inputs": ["fcf", "debt"], "func": f24_dbtj_099_negative_fcf_with_rising_debt_8q},
    "f24_dbtj_100_debt_to_capital_above_60pct_persistence": {"inputs": ["debt", "equity"], "func": f24_dbtj_100_debt_to_capital_above_60pct_persistence},
    "f24_dbtj_101_interest_to_ocf_above_30pct_persistence": {"inputs": ["intexp", "ncfo"], "func": f24_dbtj_101_interest_to_ocf_above_30pct_persistence},
    "f24_dbtj_102_debt_growth_above_25pct_yoy_persistence": {"inputs": ["debt"], "func": f24_dbtj_102_debt_growth_above_25pct_yoy_persistence},
    "f24_dbtj_103_negative_workingcapital_persistence": {"inputs": ["workingcapital"], "func": f24_dbtj_103_negative_workingcapital_persistence},
    "f24_dbtj_104_cash_burn_with_rising_debt_persistence": {"inputs": ["cashneq", "debt"], "func": f24_dbtj_104_cash_burn_with_rising_debt_persistence},
    "f24_dbtj_105_debtc_above_cash_persistence": {"inputs": ["debtc", "cashneq"], "func": f24_dbtj_105_debtc_above_cash_persistence},
    "f24_dbtj_106_altman_z_proxy_below_1p8_persistence": {"inputs": ["workingcapital", "retearn", "ebit", "equity", "revenue", "assets", "liabilities"], "func": f24_dbtj_106_altman_z_proxy_below_1p8_persistence},
    "f24_dbtj_107_debt_to_revenue_above_1_persistence": {"inputs": ["debt", "revenue"], "func": f24_dbtj_107_debt_to_revenue_above_1_persistence},
    "f24_dbtj_108_net_debt_to_ebitda_above_5x_persistence": {"inputs": ["debt", "cashneq", "ebitda"], "func": f24_dbtj_108_net_debt_to_ebitda_above_5x_persistence},
    "f24_dbtj_109_negative_equity_emerging_indicator": {"inputs": ["equity"], "func": f24_dbtj_109_negative_equity_emerging_indicator},
    "f24_dbtj_110_tangible_equity_negative_persistence": {"inputs": ["equity", "intangibles"], "func": f24_dbtj_110_tangible_equity_negative_persistence},
    "f24_dbtj_111_liabilitiesc_share_of_liabilities_avg4": {"inputs": ["liabilitiesc", "liabilities"], "func": f24_dbtj_111_liabilitiesc_share_of_liabilities_avg4},
    "f24_dbtj_112_noncurrent_liab_growth_yoy_pct": {"inputs": ["liabilities", "liabilitiesc"], "func": f24_dbtj_112_noncurrent_liab_growth_yoy_pct},
    "f24_dbtj_113_current_liab_growth_minus_revenue_growth": {"inputs": ["liabilitiesc", "revenue"], "func": f24_dbtj_113_current_liab_growth_minus_revenue_growth},
    "f24_dbtj_114_liabilities_to_equity_avg4": {"inputs": ["liabilities", "equity"], "func": f24_dbtj_114_liabilities_to_equity_avg4},
    "f24_dbtj_115_non_debt_liab_share_trend": {"inputs": ["liabilities", "debt"], "func": f24_dbtj_115_non_debt_liab_share_trend},
    "f24_dbtj_116_payables_funding_share_of_liabilities": {"inputs": ["payables", "liabilities"], "func": f24_dbtj_116_payables_funding_share_of_liabilities},
    "f24_dbtj_117_payables_to_debt_avg4": {"inputs": ["payables", "debt"], "func": f24_dbtj_117_payables_to_debt_avg4},
    "f24_dbtj_118_liabilities_growth_persistence_12q": {"inputs": ["liabilities"], "func": f24_dbtj_118_liabilities_growth_persistence_12q},
    "f24_dbtj_119_liabilities_yoy_pct_zscore_12q": {"inputs": ["liabilities"], "func": f24_dbtj_119_liabilities_yoy_pct_zscore_12q},
    "f24_dbtj_120_liabilities_to_assets_zscore_12q": {"inputs": ["liabilities", "assets"], "func": f24_dbtj_120_liabilities_to_assets_zscore_12q},
    "f24_dbtj_121_current_liab_to_cash_trend": {"inputs": ["liabilitiesc", "cashneq"], "func": f24_dbtj_121_current_liab_to_cash_trend},
    "f24_dbtj_122_liabilities_minus_assets_to_assets": {"inputs": ["liabilities", "assets"], "func": f24_dbtj_122_liabilities_minus_assets_to_assets},
    "f24_dbtj_123_tangibles_share_of_assets_avg4": {"inputs": ["tangibles", "assets"], "func": f24_dbtj_123_tangibles_share_of_assets_avg4},
    "f24_dbtj_124_tangibles_growth_minus_debt_growth_yoy": {"inputs": ["tangibles", "debt"], "func": f24_dbtj_124_tangibles_growth_minus_debt_growth_yoy},
    "f24_dbtj_125_ppnenet_share_of_assets_decline": {"inputs": ["ppnenet", "assets"], "func": f24_dbtj_125_ppnenet_share_of_assets_decline},
    "f24_dbtj_126_intangibles_growth_yoy_pct": {"inputs": ["intangibles"], "func": f24_dbtj_126_intangibles_growth_yoy_pct},
    "f24_dbtj_127_goodwill_proxy_to_debt_trend": {"inputs": ["intangibles", "debt"], "func": f24_dbtj_127_goodwill_proxy_to_debt_trend},
    "f24_dbtj_128_asset_growth_funded_by_debt_share_yoy": {"inputs": ["assets", "debt"], "func": f24_dbtj_128_asset_growth_funded_by_debt_share_yoy},
    "f24_dbtj_129_tangible_assets_per_dollar_debt_trend": {"inputs": ["tangibles", "debt"], "func": f24_dbtj_129_tangible_assets_per_dollar_debt_trend},
    "f24_dbtj_130_asset_backing_erosion_8q": {"inputs": ["tangibles", "debt"], "func": f24_dbtj_130_asset_backing_erosion_8q},
    "f24_dbtj_131_investments_to_debt_trend": {"inputs": ["investments", "debt"], "func": f24_dbtj_131_investments_to_debt_trend},
    "f24_dbtj_132_ppnenet_per_dollar_debt_avg4": {"inputs": ["ppnenet", "debt"], "func": f24_dbtj_132_ppnenet_per_dollar_debt_avg4},
    "f24_dbtj_133_leverage_up_coverage_down_indicator": {"inputs": ["debt", "assets", "ebit", "intexp"], "func": f24_dbtj_133_leverage_up_coverage_down_indicator},
    "f24_dbtj_134_net_debt_up_cash_down_indicator": {"inputs": ["debt", "cashneq"], "func": f24_dbtj_134_net_debt_up_cash_down_indicator},
    "f24_dbtj_135_debt_up_revenue_down_8q": {"inputs": ["debt", "revenue"], "func": f24_dbtj_135_debt_up_revenue_down_8q},
    "f24_dbtj_136_debt_up_margin_down_indicator": {"inputs": ["debt", "opinc", "revenue"], "func": f24_dbtj_136_debt_up_margin_down_indicator},
    "f24_dbtj_137_leverage_acceleration_into_peak_proxy": {"inputs": ["debt", "assets"], "func": f24_dbtj_137_leverage_acceleration_into_peak_proxy},
    "f24_dbtj_138_compound_stress_score_avg4": {"inputs": ["debt", "ebitda", "ebit", "intexp", "cashneq"], "func": f24_dbtj_138_compound_stress_score_avg4},
    "f24_dbtj_139_drawdown_in_coverage_from_8q_max": {"inputs": ["ebit", "intexp"], "func": f24_dbtj_139_drawdown_in_coverage_from_8q_max},
    "f24_dbtj_140_drawup_in_leverage_from_8q_min": {"inputs": ["debt", "assets"], "func": f24_dbtj_140_drawup_in_leverage_from_8q_min},
    "f24_dbtj_141_log_debt_minus_log_ebitda_ttm": {"inputs": ["debt", "ebitda"], "func": f24_dbtj_141_log_debt_minus_log_ebitda_ttm},
    "f24_dbtj_142_debt_ema_trend_4q_minus_8q": {"inputs": ["debt"], "func": f24_dbtj_142_debt_ema_trend_4q_minus_8q},
    "f24_dbtj_143_net_debt_ema_trend_4q_minus_12q": {"inputs": ["debt", "cashneq"], "func": f24_dbtj_143_net_debt_ema_trend_4q_minus_12q},
    "f24_dbtj_144_debt_change_to_ocf_change_ratio_4q": {"inputs": ["debt", "ncfo"], "func": f24_dbtj_144_debt_change_to_ocf_change_ratio_4q},
    "f24_dbtj_145_leverage_trend_consistency_8q": {"inputs": ["debt", "assets"], "func": f24_dbtj_145_leverage_trend_consistency_8q},
    "f24_dbtj_146_coverage_trend_consistency_8q": {"inputs": ["ebit", "intexp"], "func": f24_dbtj_146_coverage_trend_consistency_8q},
    "f24_dbtj_147_debt_to_assets_acceleration_4q_vs_12q": {"inputs": ["debt", "assets"], "func": f24_dbtj_147_debt_to_assets_acceleration_4q_vs_12q},
    "f24_dbtj_148_interest_burden_growth_yoy_pct": {"inputs": ["intexp"], "func": f24_dbtj_148_interest_burden_growth_yoy_pct},
    "f24_dbtj_149_net_debt_to_marketcap_proxy_trend": {"inputs": ["debt", "cashneq", "equity"], "func": f24_dbtj_149_net_debt_to_marketcap_proxy_trend},
    "f24_dbtj_150_compound_leverage_coverage_index": {"inputs": ["debt", "assets", "ebit", "intexp", "cashneq"], "func": f24_dbtj_150_compound_leverage_coverage_index},
}
