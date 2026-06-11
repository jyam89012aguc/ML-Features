"""cash_flow_deterioration_trajectory base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py: cash position erosion / runway, investing-financing mix,
cash-coverage ratios, OCF/FCF volatility statistics, persistence flags, regime changes, and
composite cash-deterioration arcs. Self-contained: helpers redefined locally per HANDOFF.
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


# ============================================================
#                    FEATURES 076-150
# ============================================================

# ---- Block F: cash position erosion & runway (076-090) ----

def f23_cfdt_076_cashneq_to_assets(cashneq, assets):
    return _safe_div(cashneq, assets)


def f23_cfdt_077_cashneq_qoq_pct(cashneq):
    return _qoq_pct(cashneq)


def f23_cfdt_078_cashneq_yoy_pct(cashneq):
    return _yoy_pct(cashneq)


def f23_cfdt_079_cashneq_trend_decay_8q(cashneq):
    m = cashneq.rolling(8, min_periods=3).mean()
    return _safe_div(cashneq - m, m.abs())


def f23_cfdt_080_runway_quarters_from_ncfo(cashneq, ncfo):
    burn = (-_avg4(ncfo)).clip(lower=0)
    return _safe_div(cashneq, burn)


def f23_cfdt_081_runway_quarters_from_fcf(cashneq, fcf):
    burn = (-_avg4(fcf)).clip(lower=0)
    return _safe_div(cashneq, burn)


def f23_cfdt_082_runway_from_total_burn(cashneq, ncfo, capex):
    burn = (-_avg4(ncfo - capex.abs())).clip(lower=0)
    return _safe_div(cashneq, burn)


def f23_cfdt_083_cashneq_share_of_currentassets(cashneq, assetsc):
    return _safe_div(cashneq, assetsc)


def f23_cfdt_084_cashneq_to_currentliabilities(cashneq, liabilitiesc):
    return _safe_div(cashneq, liabilitiesc)


def f23_cfdt_085_cashneq_to_debtc(cashneq, debtc):
    return _safe_div(cashneq, debtc)


def f23_cfdt_086_cashneq_drawdown_from_8q_max(cashneq):
    peak = cashneq.rolling(8, min_periods=2).max()
    return _safe_div(cashneq - peak, peak.abs())


def f23_cfdt_087_cashneq_drawdown_from_12q_max(cashneq):
    peak = cashneq.rolling(12, min_periods=3).max()
    return _safe_div(cashneq - peak, peak.abs())


def f23_cfdt_088_cash_burn_q_to_assets(cashneq, assets):
    return _safe_div(-cashneq.diff(), assets)


def f23_cfdt_089_consecutive_cash_decline_4q(cashneq):
    decl = (cashneq.diff() < 0).astype(float)
    return decl.rolling(4, min_periods=1).sum()


def f23_cfdt_090_cashneq_plus_investments_to_assets(cashneq, investments, assets):
    return _safe_div(cashneq + investments, assets)


# ---- Block G: financing dependence & investing mix (091-105) ----

def f23_cfdt_091_ncff_to_assets_ttm(ncff, assets):
    return _safe_div(_ttm(ncff), assets)


def f23_cfdt_092_ncfi_to_assets_ttm(ncfi, assets):
    return _safe_div(_ttm(ncfi), assets)


def f23_cfdt_093_ncff_positive_persistence_4q(ncff):
    pos = (ncff > 0).astype(float)
    return pos.rolling(4, min_periods=1).sum()


def f23_cfdt_094_ncff_to_neg_ncfo_dependence(ncff, ncfo):
    funding_need = (-ncfo).clip(lower=0)
    return _safe_div(ncff.clip(lower=0), _ttm(funding_need))


def f23_cfdt_095_ncff_yoy_pct_ttm(ncff):
    return _yoy_pct(_ttm(ncff))


def f23_cfdt_096_ncfi_minus_capex_to_assets(ncfi, capex, assets):
    return _safe_div(_ttm(ncfi) + _ttm(capex).abs(), assets)


def f23_cfdt_097_external_funding_share_of_capex(ncff, capex):
    return _safe_div(_ttm(ncff).clip(lower=0), _ttm(capex).abs())


def f23_cfdt_098_ncf_total_to_assets(ncf, assets):
    return _safe_div(_ttm(ncf), assets)


def f23_cfdt_099_ncf_total_decay_yoy(ncf, assets):
    r = _safe_div(_ttm(ncf), assets)
    return r - r.shift(4)


def f23_cfdt_100_ncff_share_of_total_cf(ncff, ncfo, ncfi):
    denom = _ttm(ncfo).abs() + _ttm(ncfi).abs() + _ttm(ncff).abs()
    return _safe_div(_ttm(ncff), denom)


def f23_cfdt_101_internal_cf_self_sufficiency(ncfo, capex):
    return _safe_div(_ttm(ncfo) - _ttm(capex).abs(), _ttm(capex).abs())


def f23_cfdt_102_debt_growth_yoy_pct(debt):
    return _yoy_pct(debt)


def f23_cfdt_103_debt_minus_cash_qoq_change(debt, cashneq):
    return (debt - cashneq).diff()


def f23_cfdt_104_net_debt_to_ncfo(debt, cashneq, ncfo):
    return _safe_div(debt - cashneq, _ttm(ncfo).abs())


def f23_cfdt_105_ncff_minus_ncfo_to_assets(ncff, ncfo, assets):
    return _safe_div(_ttm(ncff) - _ttm(ncfo), assets)


# ---- Block H: cash-flow volatility & distribution stats (106-120) ----

def f23_cfdt_106_ncfo_qoq_stddev_4q(ncfo):
    return ncfo.diff().rolling(4, min_periods=2).std()


def f23_cfdt_107_ncfo_qoq_stddev_8q(ncfo):
    return ncfo.diff().rolling(8, min_periods=3).std()


def f23_cfdt_108_fcf_qoq_stddev_8q(fcf):
    return fcf.diff().rolling(8, min_periods=3).std()


def f23_cfdt_109_ncfo_cv_8q(ncfo):
    m = ncfo.rolling(8, min_periods=3).mean()
    sd = ncfo.rolling(8, min_periods=3).std()
    return _safe_div(sd, m.abs())


def f23_cfdt_110_fcf_cv_8q(fcf):
    m = fcf.rolling(8, min_periods=3).mean()
    sd = fcf.rolling(8, min_periods=3).std()
    return _safe_div(sd, m.abs())


def f23_cfdt_111_ncfo_qoq_skew_8q(ncfo):
    return ncfo.diff().rolling(8, min_periods=4).skew()


def f23_cfdt_112_fcf_qoq_kurt_12q(fcf):
    return fcf.diff().rolling(12, min_periods=5).kurt()


def f23_cfdt_113_ncfo_max_qoq_drop_8q(ncfo):
    return ncfo.diff().rolling(8, min_periods=3).min()


def f23_cfdt_114_fcf_min_share_of_8q(fcf):
    mn = fcf.rolling(8, min_periods=3).min()
    md = fcf.rolling(8, min_periods=3).median()
    return _safe_div(mn, md.abs())


def f23_cfdt_115_ncfo_share_negative_quarters_12q(ncfo):
    neg = (ncfo < 0).astype(float)
    return neg.rolling(12, min_periods=3).mean()


def f23_cfdt_116_fcf_share_negative_quarters_12q(fcf):
    neg = (fcf < 0).astype(float)
    return neg.rolling(12, min_periods=3).mean()


def f23_cfdt_117_ncfo_yoy_disp_8q(ncfo):
    return _yoy(_ttm(ncfo)).rolling(8, min_periods=3).std()


def f23_cfdt_118_cash_flow_iqr_proxy_12q(ncfo):
    q75 = ncfo.rolling(12, min_periods=4).quantile(0.75)
    q25 = ncfo.rolling(12, min_periods=4).quantile(0.25)
    md = ncfo.rolling(12, min_periods=4).median()
    return _safe_div(q75 - q25, md.abs())


def f23_cfdt_119_fcf_severity_below_mean_8q(fcf):
    m = fcf.rolling(8, min_periods=3).mean()
    dev = (fcf - m).clip(upper=0)
    return _safe_div(dev, m.abs())


def f23_cfdt_120_ncfo_dispersion_ratio_4q_vs_12q(ncfo):
    s4 = ncfo.rolling(4, min_periods=2).std()
    s12 = ncfo.rolling(12, min_periods=4).std()
    return _safe_div(s4, s12)


# ---- Block I: cash coverage & cross-ratio decay (121-135) ----

def f23_cfdt_121_fcf_to_intexp_coverage(fcf, intexp):
    return _safe_div(_ttm(fcf), _ttm(intexp).abs())


def f23_cfdt_122_ncfo_to_intexp_coverage(ncfo, intexp):
    return _safe_div(_ttm(ncfo), _ttm(intexp).abs())


def f23_cfdt_123_fcf_to_debt_service_proxy(fcf, debtc, intexp):
    return _safe_div(_ttm(fcf), debtc + _ttm(intexp).abs())


def f23_cfdt_124_ebitda_minus_capex_to_debt(ebitda, capex, debt):
    return _safe_div(_ttm(ebitda) - _ttm(capex).abs(), debt)


def f23_cfdt_125_fcf_to_taxexp(fcf, taxexp):
    return _safe_div(_ttm(fcf), _ttm(taxexp).abs())


def f23_cfdt_126_fcf_coverage_decay_yoy(fcf, debt):
    c = _safe_div(_ttm(fcf), debt)
    return c - c.shift(4)


def f23_cfdt_127_ncfo_to_total_capex_payables_drag(ncfo, capex, payables):
    return _safe_div(_ttm(ncfo) - _ttm(capex).abs(), payables)


def f23_cfdt_128_fcf_coverage_of_dividends_proxy(fcf, ncff):
    div_proxy = (-ncff).clip(lower=0)
    return _safe_div(_ttm(fcf), _ttm(div_proxy))


def f23_cfdt_129_ebitda_growth_minus_ncfo_growth_yoy(ebitda, ncfo):
    return _yoy_pct(_ttm(ebitda)) - _yoy_pct(_ttm(ncfo))


def f23_cfdt_130_opinc_minus_ncfo_to_assets(opinc, ncfo, assets):
    return _safe_div(_ttm(opinc) - _ttm(ncfo), assets)


def f23_cfdt_131_cash_flow_to_equity_decay_yoy(ncfo, equity):
    r = _safe_div(_ttm(ncfo), equity)
    return r - r.shift(4)


def f23_cfdt_132_fcf_yield_decay_yoy(fcf, equity):
    r = _safe_div(_ttm(fcf), equity)
    return r - r.shift(4)


def f23_cfdt_133_fcf_to_tangibles_coverage(fcf, tangibles):
    return _safe_div(_ttm(fcf), tangibles)


def f23_cfdt_134_ncfo_per_unit_revenue_decay_8q(ncfo, revenue):
    r = _safe_div(_ttm(ncfo), _ttm(revenue))
    m = r.rolling(8, min_periods=3).mean()
    return r - m


def f23_cfdt_135_neg_ncfo_severity_avg4(ncfo, assets):
    sev = ncfo.clip(upper=0)
    return _safe_div(_avg4(sev), assets)


# ---- Block J: cash conversion cycle & composite trajectory arcs (136-150) ----

def f23_cfdt_136_cash_conversion_cycle_widening(receivables, inventory, payables, revenue, cor):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    dio = _safe_div(365.0 * inventory, _ttm(cor))
    dpo = _safe_div(365.0 * payables, _ttm(cor))
    ccc = dso + dio - dpo
    return ccc - ccc.shift(4)


def f23_cfdt_137_ccc_qoq_trend_4q(receivables, inventory, payables, revenue, cor):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    dio = _safe_div(365.0 * inventory, _ttm(cor))
    dpo = _safe_div(365.0 * payables, _ttm(cor))
    ccc = dso + dio - dpo
    return ccc - ccc.rolling(4, min_periods=2).mean()


def f23_cfdt_138_ocf_to_netinc_quality_decay_8q(ncfo, netinc):
    q = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    return q - q.rolling(8, min_periods=3).mean()


def f23_cfdt_139_cash_burn_acceleration_ttm(cashneq):
    burn = -cashneq.diff()
    return burn - burn.shift(4)


def f23_cfdt_140_fcf_below_zero_severity_avg4(fcf, revenue):
    sev = fcf.clip(upper=0)
    return _safe_div(_avg4(sev), _ttm(revenue).abs())


def f23_cfdt_141_ncfo_regime_change_8q_vs_prior(ncfo):
    recent = ncfo.rolling(8, min_periods=3).mean()
    prior = ncfo.shift(8).rolling(8, min_periods=3).mean()
    return _safe_div(recent - prior, prior.abs())


def f23_cfdt_142_fcf_regime_change_8q_vs_prior(fcf):
    recent = fcf.rolling(8, min_periods=3).mean()
    prior = fcf.shift(8).rolling(8, min_periods=3).mean()
    return _safe_div(recent - prior, prior.abs())


def f23_cfdt_143_cash_to_opex_runway(cashneq, opex):
    return _safe_div(cashneq, _ttm(opex) / 4.0)


def f23_cfdt_144_fcf_share_of_total_cash_flow_decline(fcf, ncfo, ncfi, ncff):
    total = _ttm(ncfo).abs() + _ttm(ncfi).abs() + _ttm(ncff).abs()
    share = _safe_div(_ttm(fcf), total)
    return share - share.shift(4)


def f23_cfdt_145_capex_funded_by_external_share(capex, ncfo, ncff):
    cap = _ttm(capex).abs()
    internal_avail = (_ttm(ncfo)).clip(lower=0)
    external = (cap - internal_avail).clip(lower=0)
    return _safe_div(external, cap)


def f23_cfdt_146_quick_cash_runway_q(cashneq, ncfo, capex, ncff):
    burn_q = (-(ncfo - capex.abs() + ncff.clip(upper=0))).clip(lower=0)
    return _safe_div(cashneq, _avg4(burn_q))


def f23_cfdt_147_composite_cf_distress_score(ncfo, fcf, cashneq, assets):
    neg_ncfo = (ncfo < 0).astype(float).rolling(4, min_periods=1).sum() / 4.0
    neg_fcf = (fcf < 0).astype(float).rolling(4, min_periods=1).sum() / 4.0
    cash_decline = (cashneq.diff() < 0).astype(float).rolling(4, min_periods=1).sum() / 4.0
    cash_intensity = _safe_div(cashneq, assets)
    return neg_ncfo + neg_fcf + cash_decline - cash_intensity


def f23_cfdt_148_ncfo_ttm_below_4q_lag_streak(ncfo):
    t = _ttm(ncfo)
    below = (t < t.shift(4)).astype(float)
    return below.rolling(4, min_periods=1).sum()


def f23_cfdt_149_cash_position_volatility_8q(cashneq):
    return _qoq_pct(cashneq).rolling(8, min_periods=3).std()


def f23_cfdt_150_terminal_burn_severity_ratio(ncfo, fcf, cashneq):
    recent_burn = (-_avg4(ncfo)).clip(lower=0) + (-_avg4(fcf)).clip(lower=0)
    return _safe_div(recent_burn, cashneq.abs())


# ============================================================
#                        REGISTRY
# ============================================================

CASH_FLOW_DETERIORATION_TRAJECTORY_BASE_REGISTRY_076_150 = {
    "f23_cfdt_076_cashneq_to_assets": {"inputs": ["cashneq", "assets"], "func": f23_cfdt_076_cashneq_to_assets},
    "f23_cfdt_077_cashneq_qoq_pct": {"inputs": ["cashneq"], "func": f23_cfdt_077_cashneq_qoq_pct},
    "f23_cfdt_078_cashneq_yoy_pct": {"inputs": ["cashneq"], "func": f23_cfdt_078_cashneq_yoy_pct},
    "f23_cfdt_079_cashneq_trend_decay_8q": {"inputs": ["cashneq"], "func": f23_cfdt_079_cashneq_trend_decay_8q},
    "f23_cfdt_080_runway_quarters_from_ncfo": {"inputs": ["cashneq", "ncfo"], "func": f23_cfdt_080_runway_quarters_from_ncfo},
    "f23_cfdt_081_runway_quarters_from_fcf": {"inputs": ["cashneq", "fcf"], "func": f23_cfdt_081_runway_quarters_from_fcf},
    "f23_cfdt_082_runway_from_total_burn": {"inputs": ["cashneq", "ncfo", "capex"], "func": f23_cfdt_082_runway_from_total_burn},
    "f23_cfdt_083_cashneq_share_of_currentassets": {"inputs": ["cashneq", "assetsc"], "func": f23_cfdt_083_cashneq_share_of_currentassets},
    "f23_cfdt_084_cashneq_to_currentliabilities": {"inputs": ["cashneq", "liabilitiesc"], "func": f23_cfdt_084_cashneq_to_currentliabilities},
    "f23_cfdt_085_cashneq_to_debtc": {"inputs": ["cashneq", "debtc"], "func": f23_cfdt_085_cashneq_to_debtc},
    "f23_cfdt_086_cashneq_drawdown_from_8q_max": {"inputs": ["cashneq"], "func": f23_cfdt_086_cashneq_drawdown_from_8q_max},
    "f23_cfdt_087_cashneq_drawdown_from_12q_max": {"inputs": ["cashneq"], "func": f23_cfdt_087_cashneq_drawdown_from_12q_max},
    "f23_cfdt_088_cash_burn_q_to_assets": {"inputs": ["cashneq", "assets"], "func": f23_cfdt_088_cash_burn_q_to_assets},
    "f23_cfdt_089_consecutive_cash_decline_4q": {"inputs": ["cashneq"], "func": f23_cfdt_089_consecutive_cash_decline_4q},
    "f23_cfdt_090_cashneq_plus_investments_to_assets": {"inputs": ["cashneq", "investments", "assets"], "func": f23_cfdt_090_cashneq_plus_investments_to_assets},
    "f23_cfdt_091_ncff_to_assets_ttm": {"inputs": ["ncff", "assets"], "func": f23_cfdt_091_ncff_to_assets_ttm},
    "f23_cfdt_092_ncfi_to_assets_ttm": {"inputs": ["ncfi", "assets"], "func": f23_cfdt_092_ncfi_to_assets_ttm},
    "f23_cfdt_093_ncff_positive_persistence_4q": {"inputs": ["ncff"], "func": f23_cfdt_093_ncff_positive_persistence_4q},
    "f23_cfdt_094_ncff_to_neg_ncfo_dependence": {"inputs": ["ncff", "ncfo"], "func": f23_cfdt_094_ncff_to_neg_ncfo_dependence},
    "f23_cfdt_095_ncff_yoy_pct_ttm": {"inputs": ["ncff"], "func": f23_cfdt_095_ncff_yoy_pct_ttm},
    "f23_cfdt_096_ncfi_minus_capex_to_assets": {"inputs": ["ncfi", "capex", "assets"], "func": f23_cfdt_096_ncfi_minus_capex_to_assets},
    "f23_cfdt_097_external_funding_share_of_capex": {"inputs": ["ncff", "capex"], "func": f23_cfdt_097_external_funding_share_of_capex},
    "f23_cfdt_098_ncf_total_to_assets": {"inputs": ["ncf", "assets"], "func": f23_cfdt_098_ncf_total_to_assets},
    "f23_cfdt_099_ncf_total_decay_yoy": {"inputs": ["ncf", "assets"], "func": f23_cfdt_099_ncf_total_decay_yoy},
    "f23_cfdt_100_ncff_share_of_total_cf": {"inputs": ["ncff", "ncfo", "ncfi"], "func": f23_cfdt_100_ncff_share_of_total_cf},
    "f23_cfdt_101_internal_cf_self_sufficiency": {"inputs": ["ncfo", "capex"], "func": f23_cfdt_101_internal_cf_self_sufficiency},
    "f23_cfdt_102_debt_growth_yoy_pct": {"inputs": ["debt"], "func": f23_cfdt_102_debt_growth_yoy_pct},
    "f23_cfdt_103_debt_minus_cash_qoq_change": {"inputs": ["debt", "cashneq"], "func": f23_cfdt_103_debt_minus_cash_qoq_change},
    "f23_cfdt_104_net_debt_to_ncfo": {"inputs": ["debt", "cashneq", "ncfo"], "func": f23_cfdt_104_net_debt_to_ncfo},
    "f23_cfdt_105_ncff_minus_ncfo_to_assets": {"inputs": ["ncff", "ncfo", "assets"], "func": f23_cfdt_105_ncff_minus_ncfo_to_assets},
    "f23_cfdt_106_ncfo_qoq_stddev_4q": {"inputs": ["ncfo"], "func": f23_cfdt_106_ncfo_qoq_stddev_4q},
    "f23_cfdt_107_ncfo_qoq_stddev_8q": {"inputs": ["ncfo"], "func": f23_cfdt_107_ncfo_qoq_stddev_8q},
    "f23_cfdt_108_fcf_qoq_stddev_8q": {"inputs": ["fcf"], "func": f23_cfdt_108_fcf_qoq_stddev_8q},
    "f23_cfdt_109_ncfo_cv_8q": {"inputs": ["ncfo"], "func": f23_cfdt_109_ncfo_cv_8q},
    "f23_cfdt_110_fcf_cv_8q": {"inputs": ["fcf"], "func": f23_cfdt_110_fcf_cv_8q},
    "f23_cfdt_111_ncfo_qoq_skew_8q": {"inputs": ["ncfo"], "func": f23_cfdt_111_ncfo_qoq_skew_8q},
    "f23_cfdt_112_fcf_qoq_kurt_12q": {"inputs": ["fcf"], "func": f23_cfdt_112_fcf_qoq_kurt_12q},
    "f23_cfdt_113_ncfo_max_qoq_drop_8q": {"inputs": ["ncfo"], "func": f23_cfdt_113_ncfo_max_qoq_drop_8q},
    "f23_cfdt_114_fcf_min_share_of_8q": {"inputs": ["fcf"], "func": f23_cfdt_114_fcf_min_share_of_8q},
    "f23_cfdt_115_ncfo_share_negative_quarters_12q": {"inputs": ["ncfo"], "func": f23_cfdt_115_ncfo_share_negative_quarters_12q},
    "f23_cfdt_116_fcf_share_negative_quarters_12q": {"inputs": ["fcf"], "func": f23_cfdt_116_fcf_share_negative_quarters_12q},
    "f23_cfdt_117_ncfo_yoy_disp_8q": {"inputs": ["ncfo"], "func": f23_cfdt_117_ncfo_yoy_disp_8q},
    "f23_cfdt_118_cash_flow_iqr_proxy_12q": {"inputs": ["ncfo"], "func": f23_cfdt_118_cash_flow_iqr_proxy_12q},
    "f23_cfdt_119_fcf_severity_below_mean_8q": {"inputs": ["fcf"], "func": f23_cfdt_119_fcf_severity_below_mean_8q},
    "f23_cfdt_120_ncfo_dispersion_ratio_4q_vs_12q": {"inputs": ["ncfo"], "func": f23_cfdt_120_ncfo_dispersion_ratio_4q_vs_12q},
    "f23_cfdt_121_fcf_to_intexp_coverage": {"inputs": ["fcf", "intexp"], "func": f23_cfdt_121_fcf_to_intexp_coverage},
    "f23_cfdt_122_ncfo_to_intexp_coverage": {"inputs": ["ncfo", "intexp"], "func": f23_cfdt_122_ncfo_to_intexp_coverage},
    "f23_cfdt_123_fcf_to_debt_service_proxy": {"inputs": ["fcf", "debtc", "intexp"], "func": f23_cfdt_123_fcf_to_debt_service_proxy},
    "f23_cfdt_124_ebitda_minus_capex_to_debt": {"inputs": ["ebitda", "capex", "debt"], "func": f23_cfdt_124_ebitda_minus_capex_to_debt},
    "f23_cfdt_125_fcf_to_taxexp": {"inputs": ["fcf", "taxexp"], "func": f23_cfdt_125_fcf_to_taxexp},
    "f23_cfdt_126_fcf_coverage_decay_yoy": {"inputs": ["fcf", "debt"], "func": f23_cfdt_126_fcf_coverage_decay_yoy},
    "f23_cfdt_127_ncfo_to_total_capex_payables_drag": {"inputs": ["ncfo", "capex", "payables"], "func": f23_cfdt_127_ncfo_to_total_capex_payables_drag},
    "f23_cfdt_128_fcf_coverage_of_dividends_proxy": {"inputs": ["fcf", "ncff"], "func": f23_cfdt_128_fcf_coverage_of_dividends_proxy},
    "f23_cfdt_129_ebitda_growth_minus_ncfo_growth_yoy": {"inputs": ["ebitda", "ncfo"], "func": f23_cfdt_129_ebitda_growth_minus_ncfo_growth_yoy},
    "f23_cfdt_130_opinc_minus_ncfo_to_assets": {"inputs": ["opinc", "ncfo", "assets"], "func": f23_cfdt_130_opinc_minus_ncfo_to_assets},
    "f23_cfdt_131_cash_flow_to_equity_decay_yoy": {"inputs": ["ncfo", "equity"], "func": f23_cfdt_131_cash_flow_to_equity_decay_yoy},
    "f23_cfdt_132_fcf_yield_decay_yoy": {"inputs": ["fcf", "equity"], "func": f23_cfdt_132_fcf_yield_decay_yoy},
    "f23_cfdt_133_fcf_to_tangibles_coverage": {"inputs": ["fcf", "tangibles"], "func": f23_cfdt_133_fcf_to_tangibles_coverage},
    "f23_cfdt_134_ncfo_per_unit_revenue_decay_8q": {"inputs": ["ncfo", "revenue"], "func": f23_cfdt_134_ncfo_per_unit_revenue_decay_8q},
    "f23_cfdt_135_neg_ncfo_severity_avg4": {"inputs": ["ncfo", "assets"], "func": f23_cfdt_135_neg_ncfo_severity_avg4},
    "f23_cfdt_136_cash_conversion_cycle_widening": {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"], "func": f23_cfdt_136_cash_conversion_cycle_widening},
    "f23_cfdt_137_ccc_qoq_trend_4q": {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"], "func": f23_cfdt_137_ccc_qoq_trend_4q},
    "f23_cfdt_138_ocf_to_netinc_quality_decay_8q": {"inputs": ["ncfo", "netinc"], "func": f23_cfdt_138_ocf_to_netinc_quality_decay_8q},
    "f23_cfdt_139_cash_burn_acceleration_ttm": {"inputs": ["cashneq"], "func": f23_cfdt_139_cash_burn_acceleration_ttm},
    "f23_cfdt_140_fcf_below_zero_severity_avg4": {"inputs": ["fcf", "revenue"], "func": f23_cfdt_140_fcf_below_zero_severity_avg4},
    "f23_cfdt_141_ncfo_regime_change_8q_vs_prior": {"inputs": ["ncfo"], "func": f23_cfdt_141_ncfo_regime_change_8q_vs_prior},
    "f23_cfdt_142_fcf_regime_change_8q_vs_prior": {"inputs": ["fcf"], "func": f23_cfdt_142_fcf_regime_change_8q_vs_prior},
    "f23_cfdt_143_cash_to_opex_runway": {"inputs": ["cashneq", "opex"], "func": f23_cfdt_143_cash_to_opex_runway},
    "f23_cfdt_144_fcf_share_of_total_cash_flow_decline": {"inputs": ["fcf", "ncfo", "ncfi", "ncff"], "func": f23_cfdt_144_fcf_share_of_total_cash_flow_decline},
    "f23_cfdt_145_capex_funded_by_external_share": {"inputs": ["capex", "ncfo", "ncff"], "func": f23_cfdt_145_capex_funded_by_external_share},
    "f23_cfdt_146_quick_cash_runway_q": {"inputs": ["cashneq", "ncfo", "capex", "ncff"], "func": f23_cfdt_146_quick_cash_runway_q},
    "f23_cfdt_147_composite_cf_distress_score": {"inputs": ["ncfo", "fcf", "cashneq", "assets"], "func": f23_cfdt_147_composite_cf_distress_score},
    "f23_cfdt_148_ncfo_ttm_below_4q_lag_streak": {"inputs": ["ncfo"], "func": f23_cfdt_148_ncfo_ttm_below_4q_lag_streak},
    "f23_cfdt_149_cash_position_volatility_8q": {"inputs": ["cashneq"], "func": f23_cfdt_149_cash_position_volatility_8q},
    "f23_cfdt_150_terminal_burn_severity_ratio": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f23_cfdt_150_terminal_burn_severity_ratio},
}
