"""profitability_snapshot base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py: per-share profitability, composition decomposition,
coverage ratios, dispersion/consistency, and composite quality scores. Self-contained;
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


def _sign_change(s):
    sgn = np.sign(s.fillna(0.0))
    return (sgn != sgn.shift(1)).fillna(False).astype(float)


# ============================================================
#                    FEATURES 076-150
# ============================================================

# ---- Block E: profitability per share (076-095) ----

def f12_psnp_076_signed_log_eps_ttm(eps):
    return _signed_log_abs(_ttm(eps))


def f12_psnp_077_signed_log_eps_dil_ttm(epsdil):
    return _signed_log_abs(_ttm(epsdil))


def f12_psnp_078_eps_growth_yoy(eps):
    return _yoy_pct(_ttm(eps))


def f12_psnp_079_eps_growth_qoq(eps):
    return _yoy_pct(eps)  # q vs q-4 (still yoy on raw eps to avoid 0-base issues)


def f12_psnp_080_payout_ratio_dps_to_eps(dps, eps):
    return _safe_div(dps, eps.abs())


def f12_psnp_081_dps_growth_yoy(dps):
    return _yoy_pct(dps)


def f12_psnp_082_ebitda_per_share_ttm(ebitda, shareswadil):
    return _safe_div(_ttm(ebitda), shareswadil)


def f12_psnp_083_fcf_per_share_ttm(fcf, shareswadil):
    return _safe_div(_ttm(fcf), shareswadil)


def f12_psnp_084_ocf_per_share_ttm(ncfo, shareswadil):
    return _safe_div(_ttm(ncfo), shareswadil)


def f12_psnp_085_book_value_per_share(equity, shareswadil):
    return _safe_div(equity, shareswadil)


def f12_psnp_086_tangible_book_per_share(equity, intangibles, shareswadil):
    return _safe_div(equity - intangibles, shareswadil)


def f12_psnp_087_eps_dil_minus_basic_drag(eps, epsdil):
    return _safe_div(eps - epsdil, eps.abs())


def f12_psnp_088_eps_zscore_8q(eps):
    return _rolling_zscore(_ttm(eps), 8, 3)


def f12_psnp_089_ebitda_per_share_zscore_8q(ebitda, shareswadil):
    return _rolling_zscore(_safe_div(_ttm(ebitda), shareswadil), 8, 3)


def f12_psnp_090_fcf_per_share_growth_yoy(fcf, shareswadil):
    return _yoy_pct(_safe_div(_ttm(fcf), shareswadil))


def f12_psnp_091_dps_yield_to_bvps(dps, equity, shareswadil):
    bvps = _safe_div(equity, shareswadil)
    return _safe_div(dps, bvps)


def f12_psnp_092_payout_to_fcf_ttm(dps, fcf, shareswadil):
    fcfps = _safe_div(_ttm(fcf), shareswadil)
    return _safe_div(dps, fcfps.abs())


def f12_psnp_093_eps_yoy_minus_revenue_yoy(eps, revenue):
    return _yoy_pct(_ttm(eps)) - _yoy_pct(_ttm(revenue))


def f12_psnp_094_ebitda_per_share_yoy_minus_revenue_per_share_yoy(ebitda, revenue, shareswadil):
    return _yoy_pct(_safe_div(_ttm(ebitda), shareswadil)) - _yoy_pct(_safe_div(_ttm(revenue), shareswadil))


def f12_psnp_095_bvps_growth_yoy(equity, shareswadil):
    return _yoy_pct(_safe_div(equity, shareswadil))


# ---- Block F: profitability composition (096-110) ----

def f12_psnp_096_gross_profit_to_assets(gp, assets):
    return _safe_div(_ttm(gp), assets)


def f12_psnp_097_operating_income_to_assets(opinc, assets):
    return _safe_div(_ttm(opinc), assets)


def f12_psnp_098_ebitda_to_assets(ebitda, assets):
    return _safe_div(_ttm(ebitda), assets)


def f12_psnp_099_netinc_share_of_opinc(netinc, opinc):
    return _safe_div(_ttm(netinc), _ttm(opinc).abs())


def f12_psnp_100_ebit_to_total_capital(ebit, equity, debt):
    return _safe_div(_ttm(ebit), equity + debt)


def f12_psnp_101_opinc_to_invested_capital(opinc, equity, debt):
    return _safe_div(_ttm(opinc), equity + debt)


def f12_psnp_102_fcf_to_total_capital(fcf, equity, debt):
    return _safe_div(_ttm(fcf), equity + debt)


def f12_psnp_103_ebitda_to_total_capital(ebitda, equity, debt):
    return _safe_div(_ttm(ebitda), equity + debt)


def f12_psnp_104_operating_leverage_yoy(ebit, revenue):
    return _safe_div(_yoy_pct(_ttm(ebit)), _yoy_pct(_ttm(revenue)).abs())


def f12_psnp_105_financial_leverage_yoy(netinc, ebit):
    return _safe_div(_yoy_pct(_ttm(netinc)), _yoy_pct(_ttm(ebit)).abs())


def f12_psnp_106_total_leverage_yoy(netinc, revenue):
    return _safe_div(_yoy_pct(_ttm(netinc)), _yoy_pct(_ttm(revenue)).abs())


def f12_psnp_107_gross_to_operating_margin_gap(gp, opinc, revenue):
    return _safe_div(_ttm(gp) - _ttm(opinc), _ttm(revenue).abs())


def f12_psnp_108_ebitda_to_ebit_ratio(ebitda, ebit):
    return _safe_div(_ttm(ebitda), _ttm(ebit).abs())


def f12_psnp_109_opinc_to_ebitda(opinc, ebitda):
    return _safe_div(_ttm(opinc), _ttm(ebitda).abs())


def f12_psnp_110_netinc_share_of_ebitda(netinc, ebitda):
    return _safe_div(_ttm(netinc), _ttm(ebitda).abs())


# ---- Block G: tax / interest burden (111-120) ----

def f12_psnp_111_effective_tax_rate_ttm(taxexp, ebit):
    return _safe_div(_ttm(taxexp), _ttm(ebit))


def f12_psnp_112_tax_to_revenue_volatility_8q(taxexp, revenue):
    return _safe_div(_ttm(taxexp), _ttm(revenue)).rolling(8, min_periods=3).std()


def f12_psnp_113_interest_coverage_ebit(ebit, intexp):
    return _safe_div(_ttm(ebit), _ttm(intexp).abs())


def f12_psnp_114_interest_coverage_ebitda(ebitda, intexp):
    return _safe_div(_ttm(ebitda), _ttm(intexp).abs())


def f12_psnp_115_opinc_minus_interest_margin(opinc, intexp, revenue):
    return _safe_div(_ttm(opinc) - _ttm(intexp), _ttm(revenue).abs())


def f12_psnp_116_cash_to_book_tax_ratio(taxexp, ncfo, ebit):
    # cash tax proxy: derived from cf gap; this is a rough surrogate
    return _safe_div(_ttm(taxexp), _ttm(ebit).abs() - _ttm(ncfo).abs() + 1e-9)


def f12_psnp_117_negative_tax_q_share_8q(taxexp):
    return (taxexp < 0).rolling(8, min_periods=3).mean()


def f12_psnp_118_pretax_to_ebit_ratio(ebit, intexp):
    return _safe_div(_ttm(ebit) - _ttm(intexp), _ttm(ebit).abs())


def f12_psnp_119_fcf_after_interest_margin(fcf, intexp, revenue):
    return _safe_div(_ttm(fcf) - _ttm(intexp).abs(), _ttm(revenue).abs())


def f12_psnp_120_nopat_to_ebit_ratio(ebit, taxexp):
    eff_tax = _safe_div(_ttm(taxexp), _ttm(ebit).abs()).clip(lower=0.0, upper=0.6)
    return 1.0 - eff_tax


# ---- Block H: dispersion / consistency (121-135) ----

def f12_psnp_121_roa_cv_8q(netinc, assets):
    r = _safe_div(_ttm(netinc), assets)
    return _safe_div(r.rolling(8, min_periods=3).std(), r.rolling(8, min_periods=3).mean().abs())


def f12_psnp_122_roe_cv_8q(netinc, equity):
    r = _safe_div(_ttm(netinc), equity)
    return _safe_div(r.rolling(8, min_periods=3).std(), r.rolling(8, min_periods=3).mean().abs())


def f12_psnp_123_ebitda_margin_cv_12q(ebitda, revenue):
    m = _safe_div(_ttm(ebitda), _ttm(revenue))
    return _safe_div(m.rolling(12, min_periods=4).std(), m.rolling(12, min_periods=4).mean().abs())


def f12_psnp_124_operating_margin_cv_12q(opinc, revenue):
    m = _safe_div(_ttm(opinc), _ttm(revenue))
    return _safe_div(m.rolling(12, min_periods=4).std(), m.rolling(12, min_periods=4).mean().abs())


def f12_psnp_125_gross_margin_cv_12q(gp, revenue):
    m = _safe_div(_ttm(gp), _ttm(revenue))
    return _safe_div(m.rolling(12, min_periods=4).std(), m.rolling(12, min_periods=4).mean().abs())


def f12_psnp_126_negative_netinc_q_share_8q(netinc):
    return (netinc < 0).rolling(8, min_periods=3).mean()


def f12_psnp_127_negative_opinc_q_share_8q(opinc):
    return (opinc < 0).rolling(8, min_periods=3).mean()


def f12_psnp_128_negative_fcf_q_share_8q(fcf):
    return (fcf < 0).rolling(8, min_periods=3).mean()


def f12_psnp_129_negative_ebitda_q_share_8q(ebitda):
    return (ebitda < 0).rolling(8, min_periods=3).mean()


def f12_psnp_130_eps_sign_change_count_8q(eps):
    return _sign_change(eps).rolling(8, min_periods=3).sum()


def f12_psnp_131_consecutive_profitable_q_streak_12q(netinc):
    pos = (netinc > 0).astype(int)
    return pos.rolling(12, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True)


def f12_psnp_132_consecutive_unprofitable_q_streak_12q(netinc):
    neg = (netinc <= 0).astype(int)
    return neg.rolling(12, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True)


def f12_psnp_133_earnings_seasonality_q4_vs_q1(netinc):
    # rolling proxy: ratio of latest q to q lagged 2 (half-year ago) — captures cyclical asymmetry
    return _safe_div(netinc, netinc.shift(2).abs())


def f12_psnp_134_margin_compression_q_count_8q(opinc, revenue):
    m = _safe_div(opinc, revenue)
    return (m.diff() < 0).rolling(8, min_periods=3).sum()


def f12_psnp_135_profitability_consistency_composite(netinc, ncfo, opinc):
    z_ni = _rolling_zscore(_ttm(netinc), 12, 4)
    z_cf = _rolling_zscore(_ttm(ncfo), 12, 4)
    z_op = _rolling_zscore(_ttm(opinc), 12, 4)
    # average — high & stable → high score; volatility lowers composite
    return (z_ni + z_cf + z_op) / 3.0


# ---- Block I: composite quality scores (136-150) ----

def f12_psnp_136_piotroski_partial_5sig(netinc, ncfo, assets, revenue, gp):
    s1 = (netinc > 0).astype(float)
    s2 = (ncfo > 0).astype(float)
    s3 = (_ttm(netinc) - _ttm(netinc).shift(4) > 0).astype(float)
    s4 = (_ttm(ncfo) > _ttm(netinc)).astype(float)
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    s5 = (gm - gm.shift(4) > 0).astype(float)
    return s1 + s2 + s3 + s4 + s5


def f12_psnp_137_quality_composite_zscore(netinc, gp, ebitda, fcf, assets, revenue):
    z_roa = _rolling_zscore(_safe_div(_ttm(netinc), assets), 12, 4)
    z_gm = _rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 12, 4)
    z_em = _rolling_zscore(_safe_div(_ttm(ebitda), _ttm(revenue)), 12, 4)
    z_fm = _rolling_zscore(_safe_div(_ttm(fcf), _ttm(revenue)), 12, 4)
    return (z_roa + z_gm + z_em + z_fm) / 4.0


def f12_psnp_138_profitability_history_decile_proxy(netinc, assets):
    r = _safe_div(_ttm(netinc), assets)
    return r.rolling(20, min_periods=6).rank(pct=True)


def f12_psnp_139_core_profitability_research_adj(ebit, rnd, assets):
    return _safe_div(_ttm(ebit) + _ttm(rnd), assets)


def f12_psnp_140_margin_minus_revenue_growth_gap(opinc, revenue):
    return _safe_div(_ttm(opinc), _ttm(revenue)) - _yoy_pct(_ttm(revenue))


def f12_psnp_141_owner_earnings_proxy_to_assets(ncfo, capex, assets):
    return _safe_div(_ttm(ncfo) - _ttm(capex).abs(), assets)


def f12_psnp_142_cash_earnings_yield_to_invcap(ncfo, equity, debt):
    return _safe_div(_ttm(ncfo), equity + debt)


def f12_psnp_143_roic_minus_8q_avg(ebit, equity, debt):
    r = _safe_div(_ttm(ebit), equity + debt)
    return r - r.rolling(8, min_periods=3).mean()


def f12_psnp_144_novymarx_gp_to_assets(gp, assets):
    return _safe_div(_ttm(gp), assets)


def f12_psnp_145_operating_efficiency_composite(gp, opinc, ebitda, revenue):
    rev = _ttm(revenue).replace(0, np.nan)
    return (_ttm(gp) + _ttm(opinc) + _ttm(ebitda)) / (3.0 * rev)


def f12_psnp_146_capital_efficiency_composite(netinc, ebit, ebitda, assets, equity, debt):
    roa = _safe_div(_ttm(netinc), assets)
    roe = _safe_div(_ttm(netinc), equity)
    roic = _safe_div(_ttm(ebit), equity + debt)
    return (roa + roe + roic) / 3.0


def f12_psnp_147_earnings_diversity_score(netinc, opinc, ncfo):
    # how aligned are three earnings measures (low std = high agreement = quality)
    df = pd.concat([_ttm(netinc), _ttm(opinc), _ttm(ncfo)], axis=1)
    return -df.std(axis=1)


def f12_psnp_148_cash_quality_4q_min_to_avg(ncfo, netinc):
    return _safe_div(ncfo.rolling(4, min_periods=2).min(), netinc.rolling(4, min_periods=2).mean().abs())


def f12_psnp_149_negative_growth_negative_margin_composite(opinc, revenue):
    m = _safe_div(_ttm(opinc), _ttm(revenue))
    rev_yoy = _yoy_pct(_ttm(revenue))
    return -(m.clip(upper=0).abs() * rev_yoy.clip(upper=0).abs())


def f12_psnp_150_profitability_collapse_signal(opinc, revenue):
    m = _safe_div(opinc, revenue)
    return m - m.rolling(4, min_periods=2).mean().shift(1)


# ============================================================
#                        REGISTRY
# ============================================================

PROFITABILITY_SNAPSHOT_BASE_REGISTRY_076_150 = {
    "f12_psnp_076_signed_log_eps_ttm": {"inputs": ["eps"], "func": f12_psnp_076_signed_log_eps_ttm},
    "f12_psnp_077_signed_log_eps_dil_ttm": {"inputs": ["epsdil"], "func": f12_psnp_077_signed_log_eps_dil_ttm},
    "f12_psnp_078_eps_growth_yoy": {"inputs": ["eps"], "func": f12_psnp_078_eps_growth_yoy},
    "f12_psnp_079_eps_growth_qoq": {"inputs": ["eps"], "func": f12_psnp_079_eps_growth_qoq},
    "f12_psnp_080_payout_ratio_dps_to_eps": {"inputs": ["dps", "eps"], "func": f12_psnp_080_payout_ratio_dps_to_eps},
    "f12_psnp_081_dps_growth_yoy": {"inputs": ["dps"], "func": f12_psnp_081_dps_growth_yoy},
    "f12_psnp_082_ebitda_per_share_ttm": {"inputs": ["ebitda", "shareswadil"], "func": f12_psnp_082_ebitda_per_share_ttm},
    "f12_psnp_083_fcf_per_share_ttm": {"inputs": ["fcf", "shareswadil"], "func": f12_psnp_083_fcf_per_share_ttm},
    "f12_psnp_084_ocf_per_share_ttm": {"inputs": ["ncfo", "shareswadil"], "func": f12_psnp_084_ocf_per_share_ttm},
    "f12_psnp_085_book_value_per_share": {"inputs": ["equity", "shareswadil"], "func": f12_psnp_085_book_value_per_share},
    "f12_psnp_086_tangible_book_per_share": {"inputs": ["equity", "intangibles", "shareswadil"], "func": f12_psnp_086_tangible_book_per_share},
    "f12_psnp_087_eps_dil_minus_basic_drag": {"inputs": ["eps", "epsdil"], "func": f12_psnp_087_eps_dil_minus_basic_drag},
    "f12_psnp_088_eps_zscore_8q": {"inputs": ["eps"], "func": f12_psnp_088_eps_zscore_8q},
    "f12_psnp_089_ebitda_per_share_zscore_8q": {"inputs": ["ebitda", "shareswadil"], "func": f12_psnp_089_ebitda_per_share_zscore_8q},
    "f12_psnp_090_fcf_per_share_growth_yoy": {"inputs": ["fcf", "shareswadil"], "func": f12_psnp_090_fcf_per_share_growth_yoy},
    "f12_psnp_091_dps_yield_to_bvps": {"inputs": ["dps", "equity", "shareswadil"], "func": f12_psnp_091_dps_yield_to_bvps},
    "f12_psnp_092_payout_to_fcf_ttm": {"inputs": ["dps", "fcf", "shareswadil"], "func": f12_psnp_092_payout_to_fcf_ttm},
    "f12_psnp_093_eps_yoy_minus_revenue_yoy": {"inputs": ["eps", "revenue"], "func": f12_psnp_093_eps_yoy_minus_revenue_yoy},
    "f12_psnp_094_ebitda_per_share_yoy_minus_revenue_per_share_yoy": {"inputs": ["ebitda", "revenue", "shareswadil"], "func": f12_psnp_094_ebitda_per_share_yoy_minus_revenue_per_share_yoy},
    "f12_psnp_095_bvps_growth_yoy": {"inputs": ["equity", "shareswadil"], "func": f12_psnp_095_bvps_growth_yoy},
    "f12_psnp_096_gross_profit_to_assets": {"inputs": ["gp", "assets"], "func": f12_psnp_096_gross_profit_to_assets},
    "f12_psnp_097_operating_income_to_assets": {"inputs": ["opinc", "assets"], "func": f12_psnp_097_operating_income_to_assets},
    "f12_psnp_098_ebitda_to_assets": {"inputs": ["ebitda", "assets"], "func": f12_psnp_098_ebitda_to_assets},
    "f12_psnp_099_netinc_share_of_opinc": {"inputs": ["netinc", "opinc"], "func": f12_psnp_099_netinc_share_of_opinc},
    "f12_psnp_100_ebit_to_total_capital": {"inputs": ["ebit", "equity", "debt"], "func": f12_psnp_100_ebit_to_total_capital},
    "f12_psnp_101_opinc_to_invested_capital": {"inputs": ["opinc", "equity", "debt"], "func": f12_psnp_101_opinc_to_invested_capital},
    "f12_psnp_102_fcf_to_total_capital": {"inputs": ["fcf", "equity", "debt"], "func": f12_psnp_102_fcf_to_total_capital},
    "f12_psnp_103_ebitda_to_total_capital": {"inputs": ["ebitda", "equity", "debt"], "func": f12_psnp_103_ebitda_to_total_capital},
    "f12_psnp_104_operating_leverage_yoy": {"inputs": ["ebit", "revenue"], "func": f12_psnp_104_operating_leverage_yoy},
    "f12_psnp_105_financial_leverage_yoy": {"inputs": ["netinc", "ebit"], "func": f12_psnp_105_financial_leverage_yoy},
    "f12_psnp_106_total_leverage_yoy": {"inputs": ["netinc", "revenue"], "func": f12_psnp_106_total_leverage_yoy},
    "f12_psnp_107_gross_to_operating_margin_gap": {"inputs": ["gp", "opinc", "revenue"], "func": f12_psnp_107_gross_to_operating_margin_gap},
    "f12_psnp_108_ebitda_to_ebit_ratio": {"inputs": ["ebitda", "ebit"], "func": f12_psnp_108_ebitda_to_ebit_ratio},
    "f12_psnp_109_opinc_to_ebitda": {"inputs": ["opinc", "ebitda"], "func": f12_psnp_109_opinc_to_ebitda},
    "f12_psnp_110_netinc_share_of_ebitda": {"inputs": ["netinc", "ebitda"], "func": f12_psnp_110_netinc_share_of_ebitda},
    "f12_psnp_111_effective_tax_rate_ttm": {"inputs": ["taxexp", "ebit"], "func": f12_psnp_111_effective_tax_rate_ttm},
    "f12_psnp_112_tax_to_revenue_volatility_8q": {"inputs": ["taxexp", "revenue"], "func": f12_psnp_112_tax_to_revenue_volatility_8q},
    "f12_psnp_113_interest_coverage_ebit": {"inputs": ["ebit", "intexp"], "func": f12_psnp_113_interest_coverage_ebit},
    "f12_psnp_114_interest_coverage_ebitda": {"inputs": ["ebitda", "intexp"], "func": f12_psnp_114_interest_coverage_ebitda},
    "f12_psnp_115_opinc_minus_interest_margin": {"inputs": ["opinc", "intexp", "revenue"], "func": f12_psnp_115_opinc_minus_interest_margin},
    "f12_psnp_116_cash_to_book_tax_ratio": {"inputs": ["taxexp", "ncfo", "ebit"], "func": f12_psnp_116_cash_to_book_tax_ratio},
    "f12_psnp_117_negative_tax_q_share_8q": {"inputs": ["taxexp"], "func": f12_psnp_117_negative_tax_q_share_8q},
    "f12_psnp_118_pretax_to_ebit_ratio": {"inputs": ["ebit", "intexp"], "func": f12_psnp_118_pretax_to_ebit_ratio},
    "f12_psnp_119_fcf_after_interest_margin": {"inputs": ["fcf", "intexp", "revenue"], "func": f12_psnp_119_fcf_after_interest_margin},
    "f12_psnp_120_nopat_to_ebit_ratio": {"inputs": ["ebit", "taxexp"], "func": f12_psnp_120_nopat_to_ebit_ratio},
    "f12_psnp_121_roa_cv_8q": {"inputs": ["netinc", "assets"], "func": f12_psnp_121_roa_cv_8q},
    "f12_psnp_122_roe_cv_8q": {"inputs": ["netinc", "equity"], "func": f12_psnp_122_roe_cv_8q},
    "f12_psnp_123_ebitda_margin_cv_12q": {"inputs": ["ebitda", "revenue"], "func": f12_psnp_123_ebitda_margin_cv_12q},
    "f12_psnp_124_operating_margin_cv_12q": {"inputs": ["opinc", "revenue"], "func": f12_psnp_124_operating_margin_cv_12q},
    "f12_psnp_125_gross_margin_cv_12q": {"inputs": ["gp", "revenue"], "func": f12_psnp_125_gross_margin_cv_12q},
    "f12_psnp_126_negative_netinc_q_share_8q": {"inputs": ["netinc"], "func": f12_psnp_126_negative_netinc_q_share_8q},
    "f12_psnp_127_negative_opinc_q_share_8q": {"inputs": ["opinc"], "func": f12_psnp_127_negative_opinc_q_share_8q},
    "f12_psnp_128_negative_fcf_q_share_8q": {"inputs": ["fcf"], "func": f12_psnp_128_negative_fcf_q_share_8q},
    "f12_psnp_129_negative_ebitda_q_share_8q": {"inputs": ["ebitda"], "func": f12_psnp_129_negative_ebitda_q_share_8q},
    "f12_psnp_130_eps_sign_change_count_8q": {"inputs": ["eps"], "func": f12_psnp_130_eps_sign_change_count_8q},
    "f12_psnp_131_consecutive_profitable_q_streak_12q": {"inputs": ["netinc"], "func": f12_psnp_131_consecutive_profitable_q_streak_12q},
    "f12_psnp_132_consecutive_unprofitable_q_streak_12q": {"inputs": ["netinc"], "func": f12_psnp_132_consecutive_unprofitable_q_streak_12q},
    "f12_psnp_133_earnings_seasonality_q4_vs_q1": {"inputs": ["netinc"], "func": f12_psnp_133_earnings_seasonality_q4_vs_q1},
    "f12_psnp_134_margin_compression_q_count_8q": {"inputs": ["opinc", "revenue"], "func": f12_psnp_134_margin_compression_q_count_8q},
    "f12_psnp_135_profitability_consistency_composite": {"inputs": ["netinc", "ncfo", "opinc"], "func": f12_psnp_135_profitability_consistency_composite},
    "f12_psnp_136_piotroski_partial_5sig": {"inputs": ["netinc", "ncfo", "assets", "revenue", "gp"], "func": f12_psnp_136_piotroski_partial_5sig},
    "f12_psnp_137_quality_composite_zscore": {"inputs": ["netinc", "gp", "ebitda", "fcf", "assets", "revenue"], "func": f12_psnp_137_quality_composite_zscore},
    "f12_psnp_138_profitability_history_decile_proxy": {"inputs": ["netinc", "assets"], "func": f12_psnp_138_profitability_history_decile_proxy},
    "f12_psnp_139_core_profitability_research_adj": {"inputs": ["ebit", "rnd", "assets"], "func": f12_psnp_139_core_profitability_research_adj},
    "f12_psnp_140_margin_minus_revenue_growth_gap": {"inputs": ["opinc", "revenue"], "func": f12_psnp_140_margin_minus_revenue_growth_gap},
    "f12_psnp_141_owner_earnings_proxy_to_assets": {"inputs": ["ncfo", "capex", "assets"], "func": f12_psnp_141_owner_earnings_proxy_to_assets},
    "f12_psnp_142_cash_earnings_yield_to_invcap": {"inputs": ["ncfo", "equity", "debt"], "func": f12_psnp_142_cash_earnings_yield_to_invcap},
    "f12_psnp_143_roic_minus_8q_avg": {"inputs": ["ebit", "equity", "debt"], "func": f12_psnp_143_roic_minus_8q_avg},
    "f12_psnp_144_novymarx_gp_to_assets": {"inputs": ["gp", "assets"], "func": f12_psnp_144_novymarx_gp_to_assets},
    "f12_psnp_145_operating_efficiency_composite": {"inputs": ["gp", "opinc", "ebitda", "revenue"], "func": f12_psnp_145_operating_efficiency_composite},
    "f12_psnp_146_capital_efficiency_composite": {"inputs": ["netinc", "ebit", "ebitda", "assets", "equity", "debt"], "func": f12_psnp_146_capital_efficiency_composite},
    "f12_psnp_147_earnings_diversity_score": {"inputs": ["netinc", "opinc", "ncfo"], "func": f12_psnp_147_earnings_diversity_score},
    "f12_psnp_148_cash_quality_4q_min_to_avg": {"inputs": ["ncfo", "netinc"], "func": f12_psnp_148_cash_quality_4q_min_to_avg},
    "f12_psnp_149_negative_growth_negative_margin_composite": {"inputs": ["opinc", "revenue"], "func": f12_psnp_149_negative_growth_negative_margin_composite},
    "f12_psnp_150_profitability_collapse_signal": {"inputs": ["opinc", "revenue"], "func": f12_psnp_150_profitability_collapse_signal},
}
