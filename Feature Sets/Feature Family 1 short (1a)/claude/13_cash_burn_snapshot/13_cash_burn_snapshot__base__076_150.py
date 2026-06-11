"""cash_burn_snapshot base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py: financing dependence, dividend / payout burden,
cash trajectory and depletion signals, and composite cash-burn risk scores. Self-contained;
helpers redefined locally per HANDOFF.
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


def _signed_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.sign(s) * np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.sign(s) * np.log(np.where(a > eps, a, np.nan))


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


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


# ============================================================
#                    FEATURES 076-150
# ============================================================

# ---- Block E: financing dependence (076-095) ----

def f13_cbsp_076_ncff_to_assets(ncff, assets):
    return _safe_div(_ttm(ncff), assets)


def f13_cbsp_077_ncff_to_revenue(ncff, revenue):
    return _safe_div(_ttm(ncff), _ttm(revenue))


def f13_cbsp_078_ncff_share_of_total_cashflows(ncff, ncfo, ncfi):
    total = ncff.abs() + ncfo.abs() + ncfi.abs()
    return _safe_div(ncff.abs(), total)


def f13_cbsp_079_positive_ncff_q_share_8q(ncff):
    return (ncff > 0).rolling(8, min_periods=3).mean()


def f13_cbsp_080_ncff_yoy(ncff):
    return _yoy(_ttm(ncff))


def f13_cbsp_081_ncfdebt_to_assets(ncfdebt, assets):
    return _safe_div(_ttm(ncfdebt), assets)


def f13_cbsp_082_ncfcommon_to_equity(ncfcommon, equity):
    return _safe_div(_ttm(ncfcommon), equity.abs())


def f13_cbsp_083_ncfdiv_to_revenue(ncfdiv, revenue):
    return _safe_div(_ttm(ncfdiv).abs(), _ttm(revenue))


def f13_cbsp_084_ncfdebt_to_ncfo(ncfdebt, ncfo):
    return _safe_div(_ttm(ncfdebt), _ttm(ncfo).abs())


def f13_cbsp_085_debt_issuance_dependence(ncfdebt, ncfo):
    num = _ttm(ncfdebt).clip(lower=0)
    return _safe_div(num, num + _ttm(ncfo).clip(lower=0))


def f13_cbsp_086_equity_issuance_dependence(ncfcommon, ncfo):
    num = _ttm(ncfcommon).clip(lower=0)
    return _safe_div(num, num + _ttm(ncfo).clip(lower=0))


def f13_cbsp_087_external_financing_share_of_assets(ncfdebt, ncfcommon, assets):
    return _safe_div(_ttm(ncfdebt).clip(lower=0) + _ttm(ncfcommon).clip(lower=0), assets)


def f13_cbsp_088_external_financing_zscore_12q(ncfdebt, ncfcommon, assets):
    s = _safe_div(_ttm(ncfdebt).clip(lower=0) + _ttm(ncfcommon).clip(lower=0), assets)
    return _rolling_zscore(s, 12, 4)


def f13_cbsp_089_financing_inflow_streak_12q(ncff):
    pos = (ncff > 0).astype(int)
    return pos.rolling(12, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True)


def f13_cbsp_090_share_issuance_intensity_yoy(sharesbas, revenue):
    return _yoy_pct(sharesbas) - _yoy_pct(_ttm(revenue))


def f13_cbsp_091_cash_from_financing_log_abs(ncff):
    return _signed_log_abs(_ttm(ncff))


def f13_cbsp_092_share_count_qoq_pct(sharesbas):
    return _qoq_pct(sharesbas)


def f13_cbsp_093_equity_issuance_to_ocf(ncfcommon, ncfo):
    return _safe_div(_ttm(ncfcommon).clip(lower=0), _ttm(ncfo).abs())


def f13_cbsp_094_buyback_minus_issuance_to_revenue(ncfcommon, revenue):
    # ncfcommon negative = buyback per Sharadar convention
    return _safe_div(-_ttm(ncfcommon).clip(upper=0).abs(), _ttm(revenue))


def f13_cbsp_095_financing_dependence_composite(ncff, ncfdebt, ncfcommon, assets):
    z_ncff = _rolling_zscore(_safe_div(_ttm(ncff), assets), 12, 4)
    z_debt = _rolling_zscore(_safe_div(_ttm(ncfdebt), assets), 12, 4)
    z_eq = _rolling_zscore(_safe_div(_ttm(ncfcommon), assets), 12, 4)
    return (z_ncff + z_debt + z_eq) / 3.0


# ---- Block F: dividend / payout burden (096-110) ----

def f13_cbsp_096_dps_to_fcf_ps(dps, fcf, shareswadil):
    fcfps = _safe_div(_ttm(fcf), shareswadil)
    return _safe_div(dps, fcfps.abs())


def f13_cbsp_097_dps_to_ocf_ps(dps, ncfo, shareswadil):
    ocfps = _safe_div(_ttm(ncfo), shareswadil)
    return _safe_div(dps, ocfps.abs())


def f13_cbsp_098_dividend_payout_to_ocf_ttm(ncfdiv, ncfo):
    return _safe_div(_ttm(ncfdiv).abs(), _ttm(ncfo).abs())


def f13_cbsp_099_dividend_yield_to_book(dps, equity, shareswadil):
    bvps = _safe_div(equity, shareswadil)
    return _safe_div(dps, bvps.abs())


def f13_cbsp_100_dps_growth_minus_ocf_ps_growth(dps, ncfo, shareswadil):
    return _yoy_pct(dps) - _yoy_pct(_safe_div(_ttm(ncfo), shareswadil))


def f13_cbsp_101_negative_payout_coverage_q_count_8q(ncfo, ncfdiv):
    uncov = (ncfo + ncfdiv) < 0  # ncfdiv typically negative; if ocf+ncfdiv<0 cash deficit
    return uncov.rolling(8, min_periods=3).sum()


def f13_cbsp_102_dividend_minus_buyback_to_ocf(ncfdiv, ncfcommon, ncfo):
    return _safe_div(_ttm(ncfdiv).abs() + _ttm(ncfcommon).clip(upper=0).abs(), _ttm(ncfo).abs())


def f13_cbsp_103_ncfdiv_to_ncfo(ncfdiv, ncfo):
    return _safe_div(_ttm(ncfdiv).abs(), _ttm(ncfo).abs())


def f13_cbsp_104_payout_ratio_to_fcf_ttm(ncfdiv, fcf):
    return _safe_div(_ttm(ncfdiv).abs(), _ttm(fcf).abs())


def f13_cbsp_105_payout_to_capex_balance(ncfdiv, capex):
    return _safe_div(_ttm(ncfdiv).abs(), _ttm(capex).abs())


def f13_cbsp_106_cash_distributions_to_ocf(ncfdiv, ncfcommon, ncfo):
    dist = _ttm(ncfdiv).abs() + _ttm(ncfcommon).clip(upper=0).abs()
    return _safe_div(dist, _ttm(ncfo).abs())


def f13_cbsp_107_dividend_consistency_8q(dps):
    return dps.rolling(8, min_periods=3).std()


def f13_cbsp_108_fcf_minus_dividends_to_revenue(fcf, ncfdiv, revenue):
    return _safe_div(_ttm(fcf) - _ttm(ncfdiv).abs(), _ttm(revenue).abs())


def f13_cbsp_109_dividend_freeze_proxy_8q(dps):
    return (dps.diff() == 0).rolling(8, min_periods=3).sum()


def f13_cbsp_110_payout_burden_zscore_8q(ncfdiv, ncfo):
    burden = _safe_div(_ttm(ncfdiv).abs(), _ttm(ncfo).abs())
    return _rolling_zscore(burden, 8, 3)


# ---- Block G: cash trajectory / depletion signals (111-130) ----

def f13_cbsp_111_cashneq_minus_8q_max(cashneq):
    return cashneq - cashneq.rolling(8, min_periods=3).max()


def f13_cbsp_112_cashneq_minus_8q_min(cashneq):
    return cashneq - cashneq.rolling(8, min_periods=3).min()


def f13_cbsp_113_cashneq_qoq_drop_max_8q(cashneq):
    return cashneq.diff().rolling(8, min_periods=3).min()


def f13_cbsp_114_cashneq_drawdown_from_8q_peak(cashneq):
    peak = cashneq.rolling(8, min_periods=3).max()
    return _safe_div(cashneq - peak, peak.abs())


def f13_cbsp_115_cash_consecutive_down_q_streak_12q(cashneq):
    down = (cashneq.diff() < 0).astype(int)
    return down.rolling(12, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True)


def f13_cbsp_116_cash_below_4q_avg_q_count_8q(cashneq):
    avg4 = cashneq.rolling(4, min_periods=2).mean()
    return (cashneq < avg4).rolling(8, min_periods=3).sum()


def f13_cbsp_117_cash_minus_4q_avg_to_avg(cashneq):
    m = cashneq.rolling(4, min_periods=2).mean()
    return _safe_div(cashneq - m, m.abs())


def f13_cbsp_118_cash_to_avg4q_burn_ratio(cashneq, fcf):
    burn = (-fcf).rolling(4, min_periods=2).mean().clip(lower=1e-6)
    return _safe_div(cashneq, burn).clip(upper=40.0)


def f13_cbsp_119_cash_yoy_minus_ocf_yoy(cashneq, ncfo):
    return _yoy_pct(cashneq) - _yoy_pct(_ttm(ncfo))


def f13_cbsp_120_cash_zscore_12q(cashneq):
    return _rolling_zscore(cashneq, 12, 4)


def f13_cbsp_121_cash_log_qoq(cashneq):
    return _signed_log_abs(cashneq).diff()


def f13_cbsp_122_cash_acceleration_zscore_8q(cashneq):
    return _rolling_zscore(cashneq.diff().diff(), 8, 3)


def f13_cbsp_123_cashneq_q_to_lag1_ratio(cashneq):
    return _safe_div(cashneq, cashneq.shift(1).abs())


def f13_cbsp_124_cashneq_to_revenue_8q_min(cashneq, revenue):
    r = _safe_div(cashneq, _ttm(revenue))
    return r.rolling(8, min_periods=3).min()


def f13_cbsp_125_cashneq_to_assets_4q_min(cashneq, assets):
    r = _safe_div(cashneq, assets)
    return r.rolling(4, min_periods=2).min()


def f13_cbsp_126_discretionary_cash_flow_to_assets(ncfo, capex, intexp, assets):
    return _safe_div(_ttm(ncfo) - _ttm(capex).abs() - _ttm(intexp).abs(), assets)


def f13_cbsp_127_burn_acceleration_capex_minus_ocf_yoy(capex, ncfo):
    return _yoy_pct(_ttm(capex).abs()) - _yoy_pct(_ttm(ncfo))


def f13_cbsp_128_cash_decay_rate_4q(cashneq):
    return _safe_div(cashneq - cashneq.shift(4), cashneq.shift(4).abs())


def f13_cbsp_129_burn_runway_ratio(cashneq, capex, ncfo):
    burn = (_ttm(capex).abs() - _ttm(ncfo)).clip(lower=1e-6)
    return _safe_div(cashneq, burn).clip(upper=40.0)


def f13_cbsp_130_cash_below_currentliabilities_flag(cashneq, liabilitiesc):
    return (cashneq < liabilitiesc).astype(float)


# ---- Block H: composite cash-burn risk scores (131-150) ----

def f13_cbsp_131_burn_risk_composite(cashneq, capex, ncff, assets):
    z_cash = -_rolling_zscore(_safe_div(cashneq, assets), 12, 4)
    z_capex = _rolling_zscore(_safe_div(_ttm(capex).abs(), assets), 12, 4)
    z_fin = _rolling_zscore(_safe_div(_ttm(ncff), assets), 12, 4)
    return (z_cash + z_capex + z_fin) / 3.0


def f13_cbsp_132_altman_modified_cashburn(workingcapital, retearn, ebit, revenue, assets):
    return _safe_div(workingcapital, assets) + _safe_div(retearn, assets) + _safe_div(_ttm(ebit), assets) + _safe_div(_ttm(revenue), assets)


def f13_cbsp_133_interest_coverage_ocf(ncfo, intexp):
    return _safe_div(_ttm(ncfo), _ttm(intexp).abs())


def f13_cbsp_134_fixed_charge_coverage_proxy(ncfo, capex, intexp):
    return _safe_div(_ttm(ncfo) - _ttm(capex).abs(), _ttm(intexp).abs())


def f13_cbsp_135_burn_minus_growth_proxy(fcf, revenue, assets):
    return -_safe_div(_ttm(fcf), assets) - _yoy_pct(_ttm(revenue))


def f13_cbsp_136_liquidity_health_zscore(cashneq, receivables, liabilitiesc):
    h = _safe_div(cashneq + receivables - liabilitiesc, liabilitiesc.abs())
    return _rolling_zscore(h, 12, 4)


def f13_cbsp_137_negative_fcf_streak_12q(fcf):
    neg = (fcf < 0).astype(int)
    return neg.rolling(12, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True)


def f13_cbsp_138_cash_to_burn_8q_avg_ratio(cashneq, fcf):
    burn8 = (-fcf).rolling(8, min_periods=3).mean().clip(lower=1e-6)
    return _safe_div(cashneq, burn8).clip(upper=40.0)


def f13_cbsp_139_survival_score_proxy(cashneq, fcf, equity):
    runway = _safe_div(cashneq, (-_ttm(fcf) / 4.0).clip(lower=1e-6)).clip(upper=40.0)
    buffer = _safe_div(equity, (-_ttm(fcf)).clip(lower=1e-6)).clip(upper=40.0)
    return np.minimum(runway, buffer)


def f13_cbsp_140_capital_intensity_composite(capex, rnd, revenue):
    return _safe_div(_ttm(capex).abs() + _ttm(rnd), _ttm(revenue))


def f13_cbsp_141_cash_outflow_q_count_8q(ncfo, capex):
    deficit = (ncfo - capex.abs()) < 0
    return deficit.rolling(8, min_periods=3).sum()


def f13_cbsp_142_ocf_failure_q_count_8q(ncfo):
    return (ncfo < 0).rolling(8, min_periods=3).sum()


def f13_cbsp_143_liquidity_compression_yoy(assetsc, liabilitiesc):
    return _yoy_pct(_safe_div(assetsc, liabilitiesc))


def f13_cbsp_144_burn_growth_decoupling(fcf, revenue):
    return _yoy_pct(_ttm(fcf)) - _yoy_pct(_ttm(revenue))


def f13_cbsp_145_burn_severity_score(fcf, cashneq):
    return -_safe_div(_ttm(fcf), cashneq.abs())


def f13_cbsp_146_cash_collapse_signal(cashneq):
    return cashneq - cashneq.rolling(4, min_periods=2).mean().shift(1)


def f13_cbsp_147_financing_dependence_zscore_12q(ncfdebt, ncfcommon, assets):
    s = _safe_div(_ttm(ncfdebt).clip(lower=0) + _ttm(ncfcommon).clip(lower=0), assets)
    return _rolling_zscore(s, 12, 4)


def f13_cbsp_148_cash_runway_short_flag_proxy(cashneq, fcf):
    burn = (-_ttm(fcf) / 4.0).clip(lower=1e-6)
    return _safe_div(cashneq, burn).clip(upper=20.0)


def f13_cbsp_149_burn_volatility_8q(fcf):
    return _ttm(fcf).rolling(8, min_periods=3).std()


def f13_cbsp_150_cash_burn_aggregate_composite(cashneq, fcf, ncff, capex, assets):
    z_cash = -_rolling_zscore(_safe_div(cashneq, assets), 12, 4)
    z_fcf = -_rolling_zscore(_safe_div(_ttm(fcf), assets), 12, 4)
    z_fin = _rolling_zscore(_safe_div(_ttm(ncff), assets), 12, 4)
    z_cap = _rolling_zscore(_safe_div(_ttm(capex).abs(), assets), 12, 4)
    return (z_cash + z_fcf + z_fin + z_cap) / 4.0


# ============================================================
#                        REGISTRY
# ============================================================

CASH_BURN_SNAPSHOT_BASE_REGISTRY_076_150 = {
    "f13_cbsp_076_ncff_to_assets": {"inputs": ["ncff", "assets"], "func": f13_cbsp_076_ncff_to_assets},
    "f13_cbsp_077_ncff_to_revenue": {"inputs": ["ncff", "revenue"], "func": f13_cbsp_077_ncff_to_revenue},
    "f13_cbsp_078_ncff_share_of_total_cashflows": {"inputs": ["ncff", "ncfo", "ncfi"], "func": f13_cbsp_078_ncff_share_of_total_cashflows},
    "f13_cbsp_079_positive_ncff_q_share_8q": {"inputs": ["ncff"], "func": f13_cbsp_079_positive_ncff_q_share_8q},
    "f13_cbsp_080_ncff_yoy": {"inputs": ["ncff"], "func": f13_cbsp_080_ncff_yoy},
    "f13_cbsp_081_ncfdebt_to_assets": {"inputs": ["ncfdebt", "assets"], "func": f13_cbsp_081_ncfdebt_to_assets},
    "f13_cbsp_082_ncfcommon_to_equity": {"inputs": ["ncfcommon", "equity"], "func": f13_cbsp_082_ncfcommon_to_equity},
    "f13_cbsp_083_ncfdiv_to_revenue": {"inputs": ["ncfdiv", "revenue"], "func": f13_cbsp_083_ncfdiv_to_revenue},
    "f13_cbsp_084_ncfdebt_to_ncfo": {"inputs": ["ncfdebt", "ncfo"], "func": f13_cbsp_084_ncfdebt_to_ncfo},
    "f13_cbsp_085_debt_issuance_dependence": {"inputs": ["ncfdebt", "ncfo"], "func": f13_cbsp_085_debt_issuance_dependence},
    "f13_cbsp_086_equity_issuance_dependence": {"inputs": ["ncfcommon", "ncfo"], "func": f13_cbsp_086_equity_issuance_dependence},
    "f13_cbsp_087_external_financing_share_of_assets": {"inputs": ["ncfdebt", "ncfcommon", "assets"], "func": f13_cbsp_087_external_financing_share_of_assets},
    "f13_cbsp_088_external_financing_zscore_12q": {"inputs": ["ncfdebt", "ncfcommon", "assets"], "func": f13_cbsp_088_external_financing_zscore_12q},
    "f13_cbsp_089_financing_inflow_streak_12q": {"inputs": ["ncff"], "func": f13_cbsp_089_financing_inflow_streak_12q},
    "f13_cbsp_090_share_issuance_intensity_yoy": {"inputs": ["sharesbas", "revenue"], "func": f13_cbsp_090_share_issuance_intensity_yoy},
    "f13_cbsp_091_cash_from_financing_log_abs": {"inputs": ["ncff"], "func": f13_cbsp_091_cash_from_financing_log_abs},
    "f13_cbsp_092_share_count_qoq_pct": {"inputs": ["sharesbas"], "func": f13_cbsp_092_share_count_qoq_pct},
    "f13_cbsp_093_equity_issuance_to_ocf": {"inputs": ["ncfcommon", "ncfo"], "func": f13_cbsp_093_equity_issuance_to_ocf},
    "f13_cbsp_094_buyback_minus_issuance_to_revenue": {"inputs": ["ncfcommon", "revenue"], "func": f13_cbsp_094_buyback_minus_issuance_to_revenue},
    "f13_cbsp_095_financing_dependence_composite": {"inputs": ["ncff", "ncfdebt", "ncfcommon", "assets"], "func": f13_cbsp_095_financing_dependence_composite},
    "f13_cbsp_096_dps_to_fcf_ps": {"inputs": ["dps", "fcf", "shareswadil"], "func": f13_cbsp_096_dps_to_fcf_ps},
    "f13_cbsp_097_dps_to_ocf_ps": {"inputs": ["dps", "ncfo", "shareswadil"], "func": f13_cbsp_097_dps_to_ocf_ps},
    "f13_cbsp_098_dividend_payout_to_ocf_ttm": {"inputs": ["ncfdiv", "ncfo"], "func": f13_cbsp_098_dividend_payout_to_ocf_ttm},
    "f13_cbsp_099_dividend_yield_to_book": {"inputs": ["dps", "equity", "shareswadil"], "func": f13_cbsp_099_dividend_yield_to_book},
    "f13_cbsp_100_dps_growth_minus_ocf_ps_growth": {"inputs": ["dps", "ncfo", "shareswadil"], "func": f13_cbsp_100_dps_growth_minus_ocf_ps_growth},
    "f13_cbsp_101_negative_payout_coverage_q_count_8q": {"inputs": ["ncfo", "ncfdiv"], "func": f13_cbsp_101_negative_payout_coverage_q_count_8q},
    "f13_cbsp_102_dividend_minus_buyback_to_ocf": {"inputs": ["ncfdiv", "ncfcommon", "ncfo"], "func": f13_cbsp_102_dividend_minus_buyback_to_ocf},
    "f13_cbsp_103_ncfdiv_to_ncfo": {"inputs": ["ncfdiv", "ncfo"], "func": f13_cbsp_103_ncfdiv_to_ncfo},
    "f13_cbsp_104_payout_ratio_to_fcf_ttm": {"inputs": ["ncfdiv", "fcf"], "func": f13_cbsp_104_payout_ratio_to_fcf_ttm},
    "f13_cbsp_105_payout_to_capex_balance": {"inputs": ["ncfdiv", "capex"], "func": f13_cbsp_105_payout_to_capex_balance},
    "f13_cbsp_106_cash_distributions_to_ocf": {"inputs": ["ncfdiv", "ncfcommon", "ncfo"], "func": f13_cbsp_106_cash_distributions_to_ocf},
    "f13_cbsp_107_dividend_consistency_8q": {"inputs": ["dps"], "func": f13_cbsp_107_dividend_consistency_8q},
    "f13_cbsp_108_fcf_minus_dividends_to_revenue": {"inputs": ["fcf", "ncfdiv", "revenue"], "func": f13_cbsp_108_fcf_minus_dividends_to_revenue},
    "f13_cbsp_109_dividend_freeze_proxy_8q": {"inputs": ["dps"], "func": f13_cbsp_109_dividend_freeze_proxy_8q},
    "f13_cbsp_110_payout_burden_zscore_8q": {"inputs": ["ncfdiv", "ncfo"], "func": f13_cbsp_110_payout_burden_zscore_8q},
    "f13_cbsp_111_cashneq_minus_8q_max": {"inputs": ["cashneq"], "func": f13_cbsp_111_cashneq_minus_8q_max},
    "f13_cbsp_112_cashneq_minus_8q_min": {"inputs": ["cashneq"], "func": f13_cbsp_112_cashneq_minus_8q_min},
    "f13_cbsp_113_cashneq_qoq_drop_max_8q": {"inputs": ["cashneq"], "func": f13_cbsp_113_cashneq_qoq_drop_max_8q},
    "f13_cbsp_114_cashneq_drawdown_from_8q_peak": {"inputs": ["cashneq"], "func": f13_cbsp_114_cashneq_drawdown_from_8q_peak},
    "f13_cbsp_115_cash_consecutive_down_q_streak_12q": {"inputs": ["cashneq"], "func": f13_cbsp_115_cash_consecutive_down_q_streak_12q},
    "f13_cbsp_116_cash_below_4q_avg_q_count_8q": {"inputs": ["cashneq"], "func": f13_cbsp_116_cash_below_4q_avg_q_count_8q},
    "f13_cbsp_117_cash_minus_4q_avg_to_avg": {"inputs": ["cashneq"], "func": f13_cbsp_117_cash_minus_4q_avg_to_avg},
    "f13_cbsp_118_cash_to_avg4q_burn_ratio": {"inputs": ["cashneq", "fcf"], "func": f13_cbsp_118_cash_to_avg4q_burn_ratio},
    "f13_cbsp_119_cash_yoy_minus_ocf_yoy": {"inputs": ["cashneq", "ncfo"], "func": f13_cbsp_119_cash_yoy_minus_ocf_yoy},
    "f13_cbsp_120_cash_zscore_12q": {"inputs": ["cashneq"], "func": f13_cbsp_120_cash_zscore_12q},
    "f13_cbsp_121_cash_log_qoq": {"inputs": ["cashneq"], "func": f13_cbsp_121_cash_log_qoq},
    "f13_cbsp_122_cash_acceleration_zscore_8q": {"inputs": ["cashneq"], "func": f13_cbsp_122_cash_acceleration_zscore_8q},
    "f13_cbsp_123_cashneq_q_to_lag1_ratio": {"inputs": ["cashneq"], "func": f13_cbsp_123_cashneq_q_to_lag1_ratio},
    "f13_cbsp_124_cashneq_to_revenue_8q_min": {"inputs": ["cashneq", "revenue"], "func": f13_cbsp_124_cashneq_to_revenue_8q_min},
    "f13_cbsp_125_cashneq_to_assets_4q_min": {"inputs": ["cashneq", "assets"], "func": f13_cbsp_125_cashneq_to_assets_4q_min},
    "f13_cbsp_126_discretionary_cash_flow_to_assets": {"inputs": ["ncfo", "capex", "intexp", "assets"], "func": f13_cbsp_126_discretionary_cash_flow_to_assets},
    "f13_cbsp_127_burn_acceleration_capex_minus_ocf_yoy": {"inputs": ["capex", "ncfo"], "func": f13_cbsp_127_burn_acceleration_capex_minus_ocf_yoy},
    "f13_cbsp_128_cash_decay_rate_4q": {"inputs": ["cashneq"], "func": f13_cbsp_128_cash_decay_rate_4q},
    "f13_cbsp_129_burn_runway_ratio": {"inputs": ["cashneq", "capex", "ncfo"], "func": f13_cbsp_129_burn_runway_ratio},
    "f13_cbsp_130_cash_below_currentliabilities_flag": {"inputs": ["cashneq", "liabilitiesc"], "func": f13_cbsp_130_cash_below_currentliabilities_flag},
    "f13_cbsp_131_burn_risk_composite": {"inputs": ["cashneq", "capex", "ncff", "assets"], "func": f13_cbsp_131_burn_risk_composite},
    "f13_cbsp_132_altman_modified_cashburn": {"inputs": ["workingcapital", "retearn", "ebit", "revenue", "assets"], "func": f13_cbsp_132_altman_modified_cashburn},
    "f13_cbsp_133_interest_coverage_ocf": {"inputs": ["ncfo", "intexp"], "func": f13_cbsp_133_interest_coverage_ocf},
    "f13_cbsp_134_fixed_charge_coverage_proxy": {"inputs": ["ncfo", "capex", "intexp"], "func": f13_cbsp_134_fixed_charge_coverage_proxy},
    "f13_cbsp_135_burn_minus_growth_proxy": {"inputs": ["fcf", "revenue", "assets"], "func": f13_cbsp_135_burn_minus_growth_proxy},
    "f13_cbsp_136_liquidity_health_zscore": {"inputs": ["cashneq", "receivables", "liabilitiesc"], "func": f13_cbsp_136_liquidity_health_zscore},
    "f13_cbsp_137_negative_fcf_streak_12q": {"inputs": ["fcf"], "func": f13_cbsp_137_negative_fcf_streak_12q},
    "f13_cbsp_138_cash_to_burn_8q_avg_ratio": {"inputs": ["cashneq", "fcf"], "func": f13_cbsp_138_cash_to_burn_8q_avg_ratio},
    "f13_cbsp_139_survival_score_proxy": {"inputs": ["cashneq", "fcf", "equity"], "func": f13_cbsp_139_survival_score_proxy},
    "f13_cbsp_140_capital_intensity_composite": {"inputs": ["capex", "rnd", "revenue"], "func": f13_cbsp_140_capital_intensity_composite},
    "f13_cbsp_141_cash_outflow_q_count_8q": {"inputs": ["ncfo", "capex"], "func": f13_cbsp_141_cash_outflow_q_count_8q},
    "f13_cbsp_142_ocf_failure_q_count_8q": {"inputs": ["ncfo"], "func": f13_cbsp_142_ocf_failure_q_count_8q},
    "f13_cbsp_143_liquidity_compression_yoy": {"inputs": ["assetsc", "liabilitiesc"], "func": f13_cbsp_143_liquidity_compression_yoy},
    "f13_cbsp_144_burn_growth_decoupling": {"inputs": ["fcf", "revenue"], "func": f13_cbsp_144_burn_growth_decoupling},
    "f13_cbsp_145_burn_severity_score": {"inputs": ["fcf", "cashneq"], "func": f13_cbsp_145_burn_severity_score},
    "f13_cbsp_146_cash_collapse_signal": {"inputs": ["cashneq"], "func": f13_cbsp_146_cash_collapse_signal},
    "f13_cbsp_147_financing_dependence_zscore_12q": {"inputs": ["ncfdebt", "ncfcommon", "assets"], "func": f13_cbsp_147_financing_dependence_zscore_12q},
    "f13_cbsp_148_cash_runway_short_flag_proxy": {"inputs": ["cashneq", "fcf"], "func": f13_cbsp_148_cash_runway_short_flag_proxy},
    "f13_cbsp_149_burn_volatility_8q": {"inputs": ["fcf"], "func": f13_cbsp_149_burn_volatility_8q},
    "f13_cbsp_150_cash_burn_aggregate_composite": {"inputs": ["cashneq", "fcf", "ncff", "capex", "assets"], "func": f13_cbsp_150_cash_burn_aggregate_composite},
}
