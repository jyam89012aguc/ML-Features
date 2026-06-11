"""revenue_quality_level base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py (volatility, cash conversion, per-share, capital efficiency,
and composite revenue-quality flags). Self-contained: helpers redefined locally per HANDOFF.
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


def _sign_change(s):
    sgn = np.sign(s.fillna(0.0))
    return (sgn != sgn.shift(1)).fillna(False).astype(float)


# ============================================================
#                    FEATURES 076-150
# ============================================================

# ---- Block F (cont): revenue volatility / smoothness (076-090) ----

def f11_rqlv_076_revenue_qoq_max_drop_12q(revenue):
    return revenue.diff().rolling(12, min_periods=4).min()


def f11_rqlv_077_revenue_qoq_skew_8q(revenue):
    return revenue.diff().rolling(8, min_periods=4).skew()


def f11_rqlv_078_revenue_qoq_kurtosis_12q(revenue):
    return revenue.diff().rolling(12, min_periods=5).kurt()


def f11_rqlv_079_revenue_minus_4q_mean_to_4q_mean(revenue):
    m = revenue.rolling(4, min_periods=2).mean()
    return _safe_div(revenue - m, m.abs())


def f11_rqlv_080_revenue_ttm_dispersion_4q(revenue):
    rev_ttm = _ttm(revenue).replace(0, np.nan)
    quarters_share = revenue / rev_ttm
    return quarters_share.rolling(4, min_periods=2).std()


def f11_rqlv_081_revenue_negative_q_count_8q(revenue):
    return (revenue.diff() < 0).rolling(8, min_periods=3).sum()


def f11_rqlv_082_revenue_acceleration_q_count_8q(revenue):
    return (revenue.diff().diff() > 0).rolling(8, min_periods=3).sum()


def f11_rqlv_083_revenue_qoq_run_length_max_down_12q(revenue):
    d = revenue.diff()
    streak = (d < 0).astype(int)
    # rolling count of consecutive negative quarters ending at window end
    return streak.rolling(12, min_periods=3).apply(
        lambda w: int(w[::-1].cumprod().sum()), raw=True
    )


def f11_rqlv_084_revenue_qoq_run_length_max_up_12q(revenue):
    d = revenue.diff()
    streak = (d > 0).astype(int)
    return streak.rolling(12, min_periods=3).apply(
        lambda w: int(w[::-1].cumprod().sum()), raw=True
    )


def f11_rqlv_085_revenue_max_q_to_min_q_ratio_8q(revenue):
    mx = revenue.rolling(8, min_periods=3).max()
    mn = revenue.rolling(8, min_periods=3).min()
    return _safe_div(mx, mn)


def f11_rqlv_086_revenue_smoothness_lag1_autocorr_8q(revenue):
    d = revenue.diff()
    return d.rolling(8, min_periods=4).apply(
        lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if np.std(w[:-1]) > 0 and np.std(w[1:]) > 0 else np.nan,
        raw=True,
    )


def f11_rqlv_087_revenue_yoy_dispersion_8q(revenue):
    return _yoy_pct(_ttm(revenue)).rolling(8, min_periods=3).std()


def f11_rqlv_088_revenue_q_below_trailing_max_share_8q(revenue):
    rmax = revenue.rolling(8, min_periods=3).max()
    return _safe_div(revenue, rmax)


def f11_rqlv_089_revenue_q_above_trailing_min_share_8q(revenue):
    rmin = revenue.rolling(8, min_periods=3).min()
    return _safe_div(revenue, rmin)


def f11_rqlv_090_revenue_qoq_sign_change_count_8q(revenue):
    return _sign_change(revenue.diff()).rolling(8, min_periods=3).sum()


# ---- Block G: earnings / cash conversion from revenue (091-110) ----

def f11_rqlv_091_ncfo_to_revenue_ttm(ncfo, revenue):
    return _safe_div(_ttm(ncfo), _ttm(revenue))


def f11_rqlv_092_ncfo_to_revenue_q(ncfo, revenue):
    return _safe_div(ncfo, revenue)


def f11_rqlv_093_fcf_to_revenue_q(fcf, revenue):
    return _safe_div(fcf, revenue)


def f11_rqlv_094_netinc_to_revenue_ttm(netinc, revenue):
    return _safe_div(_ttm(netinc), _ttm(revenue))


def f11_rqlv_095_ncfo_minus_netinc_to_revenue(ncfo, netinc, revenue):
    return _safe_div(_ttm(ncfo) - _ttm(netinc), _ttm(revenue).abs())


def f11_rqlv_096_cash_conversion_ratio_ttm(ncfo, netinc):
    return _safe_div(_ttm(ncfo), _ttm(netinc).abs())


def f11_rqlv_097_capex_to_revenue_ttm(capex, revenue):
    return _safe_div(_ttm(capex).abs(), _ttm(revenue))


def f11_rqlv_098_ebitda_margin_minus_fcf_margin_ttm(ebitda, fcf, revenue):
    rev = _ttm(revenue)
    return _safe_div(_ttm(ebitda), rev) - _safe_div(_ttm(fcf), rev)


def f11_rqlv_099_taxexp_to_revenue_ttm(taxexp, revenue):
    return _safe_div(_ttm(taxexp), _ttm(revenue))


def f11_rqlv_100_intexp_to_revenue_ttm(intexp, revenue):
    return _safe_div(_ttm(intexp), _ttm(revenue))


def f11_rqlv_101_depamor_to_revenue_ttm(depamor, revenue):
    return _safe_div(_ttm(depamor), _ttm(revenue))


def f11_rqlv_102_accrual_ratio_bs_to_revenue(workingcapital, revenue):
    return _safe_div(workingcapital.diff(), _ttm(revenue).abs())


def f11_rqlv_103_accrual_ratio_cf_to_revenue(netinc, ncfo, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs())


def f11_rqlv_104_opcf_q_minus_ttm_avg_to_revenue(ncfo, revenue):
    ttm = _ttm(ncfo) / 4.0
    return _safe_div(ncfo - ttm, _ttm(revenue).abs())


def f11_rqlv_105_ebit_minus_ncfo_to_revenue(ebit, ncfo, revenue):
    return _safe_div(_ttm(ebit) - _ttm(ncfo), _ttm(revenue).abs())


def f11_rqlv_106_revenue_minus_cogs_minus_sgna_to_revenue(revenue, cor, sgna):
    return _safe_div(_ttm(revenue) - _ttm(cor) - _ttm(sgna), _ttm(revenue).abs())


def f11_rqlv_107_dps_to_revenue_per_share(dps, revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(dps, rps)


def f11_rqlv_108_eps_to_revenue_per_share(eps, revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(eps, rps)


def f11_rqlv_109_fcf_to_netinc_ttm(fcf, netinc):
    return _safe_div(_ttm(fcf), _ttm(netinc).abs())


def f11_rqlv_110_netinc_minus_ncfo_to_assets(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets)


# ---- Block H: per-share / dilution-adjusted revenue (111-125) ----

def f11_rqlv_111_log_revenue_per_dilshare_ttm(revenue, shareswadil):
    return _safe_log(_safe_div(_ttm(revenue), shareswadil))


def f11_rqlv_112_log_revenue_per_basicshare_ttm(revenue, shareswa):
    return _safe_log(_safe_div(_ttm(revenue), shareswa))


def f11_rqlv_113_revenue_per_share_qoq_pct_dil(revenue, shareswadil):
    return _qoq_pct(_safe_div(_ttm(revenue), shareswadil))


def f11_rqlv_114_revenue_per_share_yoy_pct_dil(revenue, shareswadil):
    return _yoy_pct(_safe_div(_ttm(revenue), shareswadil))


def f11_rqlv_115_share_growth_minus_revenue_growth_yoy(shareswadil, revenue):
    return _yoy_pct(shareswadil) - _yoy_pct(_ttm(revenue))


def f11_rqlv_116_dil_minus_basic_share_gap_to_basic(shareswadil, shareswa):
    return _safe_div(shareswadil - shareswa, shareswa)


def f11_rqlv_117_revenue_per_share_dispersion_8q(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return rps.rolling(8, min_periods=3).std()


def f11_rqlv_118_revenue_per_share_zscore_8q(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _rolling_zscore(rps, 8, min_periods=3)


def f11_rqlv_119_revenue_per_share_q_to_4q_max(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(rps, rps.rolling(4, min_periods=2).max())


def f11_rqlv_120_revenue_per_share_q_to_4q_min(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(rps, rps.rolling(4, min_periods=2).min())


def f11_rqlv_121_revenue_per_basic_share_growth_yoy(revenue, shareswa):
    return _yoy_pct(_safe_div(_ttm(revenue), shareswa))


def f11_rqlv_122_revenue_per_share_qoq_cv_8q(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(rps.rolling(8, min_periods=3).std(), rps.rolling(8, min_periods=3).mean().abs())


def f11_rqlv_123_basic_minus_diluted_share_gap_growth_yoy(shareswa, shareswadil):
    return _yoy_pct(shareswadil) - _yoy_pct(shareswa)


def f11_rqlv_124_revenue_per_share_yoy_minus_share_growth(revenue, shareswadil):
    return _yoy_pct(_safe_div(_ttm(revenue), shareswadil)) + _yoy_pct(shareswadil)


def f11_rqlv_125_revenue_per_share_log_qoq(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_log(rps).diff()


# ---- Block I: revenue-vs-capital efficiency (126-140) ----

def f11_rqlv_126_revenue_ttm_to_capex_ttm(revenue, capex):
    return _safe_div(_ttm(revenue), _ttm(capex).abs())


def f11_rqlv_127_revenue_ttm_to_cum_capex_4q(revenue, capex):
    return _safe_div(_ttm(revenue), capex.abs().rolling(4, min_periods=2).sum())


def f11_rqlv_128_revenue_ttm_to_debt(revenue, debt):
    return _safe_div(_ttm(revenue), debt)


def f11_rqlv_129_revenue_ttm_to_netdebt(revenue, debt, cashneq):
    return _safe_div(_ttm(revenue), debt - cashneq)


def f11_rqlv_130_revenue_ttm_to_operating_assets(revenue, assets, cashneq):
    return _safe_div(_ttm(revenue), assets - cashneq)


def f11_rqlv_131_revenue_ttm_to_tangible_assets(revenue, assets, intangibles):
    return _safe_div(_ttm(revenue), assets - intangibles)


def f11_rqlv_132_revenue_ttm_to_retained_earnings(revenue, retearn):
    return _safe_div(_ttm(revenue), retearn.abs())


def f11_rqlv_133_revenue_ttm_to_tangible_book(revenue, equity, intangibles):
    return _safe_div(_ttm(revenue), equity - intangibles)


def f11_rqlv_134_revenue_to_invested_capital_minus_goodwill(revenue, equity, debt, intangibles):
    return _safe_div(_ttm(revenue), equity + debt - intangibles)


def f11_rqlv_135_revenue_q_to_q_invested_capital(revenue, equity, debt):
    return _safe_div(revenue * 4.0, equity + debt)


def f11_rqlv_136_revenue_ttm_to_assets_minus_ttm_avg(revenue, assets):
    ratio = _safe_div(_ttm(revenue), assets)
    return ratio - ratio.rolling(4, min_periods=2).mean()


def f11_rqlv_137_revenue_ttm_per_dollar_intangible(revenue, intangibles):
    return _safe_div(_ttm(revenue), intangibles)


def f11_rqlv_138_revenue_ttm_per_dollar_ppe_gross(revenue, ppnenet):
    return _safe_div(_ttm(revenue), ppnenet)


def f11_rqlv_139_revenue_yoy_minus_capex_yoy(revenue, capex):
    return _yoy_pct(_ttm(revenue)) - _yoy_pct(_ttm(capex).abs())


def f11_rqlv_140_revenue_yoy_minus_assets_yoy(revenue, assets):
    return _yoy_pct(_ttm(revenue)) - _yoy_pct(assets)


# ---- Block J: composite revenue-quality flags (141-150) ----

def f11_rqlv_141_revenue_quality_aggregate_zscore(revenue, ncfo, receivables, inventory):
    cash_conv = _safe_div(_ttm(ncfo), _ttm(revenue).abs())
    dso = _safe_div(receivables, _ttm(revenue).abs())
    dio = _safe_div(inventory, _ttm(revenue).abs())
    z_cc = _rolling_zscore(cash_conv, 12, min_periods=4)
    z_dso = _rolling_zscore(dso, 12, min_periods=4)
    z_dio = _rolling_zscore(dio, 12, min_periods=4)
    return z_cc - z_dso - z_dio


def f11_rqlv_142_channel_stuffing_composite(receivables, revenue):
    rec_yoy = _yoy_pct(receivables)
    rev_yoy = _yoy_pct(_ttm(revenue))
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    dso_zscore = _rolling_zscore(dso, 8, min_periods=3)
    return (rec_yoy - rev_yoy).clip(lower=-5, upper=5) + dso_zscore.clip(lower=-5, upper=5)


def f11_rqlv_143_accrual_pollution_index(netinc, ncfo, receivables, assets):
    accrual_share = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    rec_share = _safe_div(receivables, assets)
    return _rolling_zscore(accrual_share, 8, 3) + _rolling_zscore(rec_share, 8, 3)


def f11_rqlv_144_revenue_overstatement_flag(receivables, revenue, ncfo):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    cash_conv = _safe_div(_ttm(ncfo), _ttm(revenue).abs())
    return _rolling_zscore(dso, 12, 4) - _rolling_zscore(cash_conv, 12, 4)


def f11_rqlv_145_one_time_revenue_spike_score(revenue):
    q_ann = revenue * 4.0
    ttm = _ttm(revenue)
    z = _rolling_zscore(_safe_div(q_ann, ttm.abs()), 8, min_periods=3)
    return z


def f11_rqlv_146_recurring_revenue_health_score(deferredrev, revenue):
    ratio = _safe_div(deferredrev * 4.0, _ttm(revenue))
    return _rolling_zscore(ratio, 8, 3)


def f11_rqlv_147_revenue_quality_collapse_signal(ncfo, revenue):
    cash_conv = _safe_div(ncfo, revenue.abs())
    return cash_conv - cash_conv.rolling(4, min_periods=2).mean().shift(1)


def f11_rqlv_148_revenue_smoothing_suspicion_8q(revenue):
    # very small qoq dispersion despite nonzero level — smoothing red flag at high level
    cv = _safe_div(revenue.diff().rolling(8, min_periods=3).std(),
                    revenue.rolling(8, min_periods=3).mean().abs())
    return -cv  # higher = more suspicious of smoothing


def f11_rqlv_149_revenue_yoy_below_seasonal_avg(revenue):
    yoy = _yoy_pct(_ttm(revenue))
    return yoy - yoy.rolling(8, min_periods=4).mean()


def f11_rqlv_150_revenue_quality_4q_aggregate_score(ncfo, netinc, receivables, inventory, revenue):
    cash_conv = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    rec_intensity = _safe_div(receivables, _ttm(revenue).abs())
    inv_intensity = _safe_div(inventory, _ttm(revenue).abs())
    z_cc = _rolling_zscore(cash_conv, 4, 2)
    z_ri = _rolling_zscore(rec_intensity, 4, 2)
    z_ii = _rolling_zscore(inv_intensity, 4, 2)
    return z_cc - z_ri - z_ii


# ============================================================
#                        REGISTRY
# ============================================================

REVENUE_QUALITY_LEVEL_BASE_REGISTRY_076_150 = {
    "f11_rqlv_076_revenue_qoq_max_drop_12q": {"inputs": ["revenue"], "func": f11_rqlv_076_revenue_qoq_max_drop_12q},
    "f11_rqlv_077_revenue_qoq_skew_8q": {"inputs": ["revenue"], "func": f11_rqlv_077_revenue_qoq_skew_8q},
    "f11_rqlv_078_revenue_qoq_kurtosis_12q": {"inputs": ["revenue"], "func": f11_rqlv_078_revenue_qoq_kurtosis_12q},
    "f11_rqlv_079_revenue_minus_4q_mean_to_4q_mean": {"inputs": ["revenue"], "func": f11_rqlv_079_revenue_minus_4q_mean_to_4q_mean},
    "f11_rqlv_080_revenue_ttm_dispersion_4q": {"inputs": ["revenue"], "func": f11_rqlv_080_revenue_ttm_dispersion_4q},
    "f11_rqlv_081_revenue_negative_q_count_8q": {"inputs": ["revenue"], "func": f11_rqlv_081_revenue_negative_q_count_8q},
    "f11_rqlv_082_revenue_acceleration_q_count_8q": {"inputs": ["revenue"], "func": f11_rqlv_082_revenue_acceleration_q_count_8q},
    "f11_rqlv_083_revenue_qoq_run_length_max_down_12q": {"inputs": ["revenue"], "func": f11_rqlv_083_revenue_qoq_run_length_max_down_12q},
    "f11_rqlv_084_revenue_qoq_run_length_max_up_12q": {"inputs": ["revenue"], "func": f11_rqlv_084_revenue_qoq_run_length_max_up_12q},
    "f11_rqlv_085_revenue_max_q_to_min_q_ratio_8q": {"inputs": ["revenue"], "func": f11_rqlv_085_revenue_max_q_to_min_q_ratio_8q},
    "f11_rqlv_086_revenue_smoothness_lag1_autocorr_8q": {"inputs": ["revenue"], "func": f11_rqlv_086_revenue_smoothness_lag1_autocorr_8q},
    "f11_rqlv_087_revenue_yoy_dispersion_8q": {"inputs": ["revenue"], "func": f11_rqlv_087_revenue_yoy_dispersion_8q},
    "f11_rqlv_088_revenue_q_below_trailing_max_share_8q": {"inputs": ["revenue"], "func": f11_rqlv_088_revenue_q_below_trailing_max_share_8q},
    "f11_rqlv_089_revenue_q_above_trailing_min_share_8q": {"inputs": ["revenue"], "func": f11_rqlv_089_revenue_q_above_trailing_min_share_8q},
    "f11_rqlv_090_revenue_qoq_sign_change_count_8q": {"inputs": ["revenue"], "func": f11_rqlv_090_revenue_qoq_sign_change_count_8q},
    "f11_rqlv_091_ncfo_to_revenue_ttm": {"inputs": ["ncfo", "revenue"], "func": f11_rqlv_091_ncfo_to_revenue_ttm},
    "f11_rqlv_092_ncfo_to_revenue_q": {"inputs": ["ncfo", "revenue"], "func": f11_rqlv_092_ncfo_to_revenue_q},
    "f11_rqlv_093_fcf_to_revenue_q": {"inputs": ["fcf", "revenue"], "func": f11_rqlv_093_fcf_to_revenue_q},
    "f11_rqlv_094_netinc_to_revenue_ttm": {"inputs": ["netinc", "revenue"], "func": f11_rqlv_094_netinc_to_revenue_ttm},
    "f11_rqlv_095_ncfo_minus_netinc_to_revenue": {"inputs": ["ncfo", "netinc", "revenue"], "func": f11_rqlv_095_ncfo_minus_netinc_to_revenue},
    "f11_rqlv_096_cash_conversion_ratio_ttm": {"inputs": ["ncfo", "netinc"], "func": f11_rqlv_096_cash_conversion_ratio_ttm},
    "f11_rqlv_097_capex_to_revenue_ttm": {"inputs": ["capex", "revenue"], "func": f11_rqlv_097_capex_to_revenue_ttm},
    "f11_rqlv_098_ebitda_margin_minus_fcf_margin_ttm": {"inputs": ["ebitda", "fcf", "revenue"], "func": f11_rqlv_098_ebitda_margin_minus_fcf_margin_ttm},
    "f11_rqlv_099_taxexp_to_revenue_ttm": {"inputs": ["taxexp", "revenue"], "func": f11_rqlv_099_taxexp_to_revenue_ttm},
    "f11_rqlv_100_intexp_to_revenue_ttm": {"inputs": ["intexp", "revenue"], "func": f11_rqlv_100_intexp_to_revenue_ttm},
    "f11_rqlv_101_depamor_to_revenue_ttm": {"inputs": ["depamor", "revenue"], "func": f11_rqlv_101_depamor_to_revenue_ttm},
    "f11_rqlv_102_accrual_ratio_bs_to_revenue": {"inputs": ["workingcapital", "revenue"], "func": f11_rqlv_102_accrual_ratio_bs_to_revenue},
    "f11_rqlv_103_accrual_ratio_cf_to_revenue": {"inputs": ["netinc", "ncfo", "revenue"], "func": f11_rqlv_103_accrual_ratio_cf_to_revenue},
    "f11_rqlv_104_opcf_q_minus_ttm_avg_to_revenue": {"inputs": ["ncfo", "revenue"], "func": f11_rqlv_104_opcf_q_minus_ttm_avg_to_revenue},
    "f11_rqlv_105_ebit_minus_ncfo_to_revenue": {"inputs": ["ebit", "ncfo", "revenue"], "func": f11_rqlv_105_ebit_minus_ncfo_to_revenue},
    "f11_rqlv_106_revenue_minus_cogs_minus_sgna_to_revenue": {"inputs": ["revenue", "cor", "sgna"], "func": f11_rqlv_106_revenue_minus_cogs_minus_sgna_to_revenue},
    "f11_rqlv_107_dps_to_revenue_per_share": {"inputs": ["dps", "revenue", "shareswadil"], "func": f11_rqlv_107_dps_to_revenue_per_share},
    "f11_rqlv_108_eps_to_revenue_per_share": {"inputs": ["eps", "revenue", "shareswadil"], "func": f11_rqlv_108_eps_to_revenue_per_share},
    "f11_rqlv_109_fcf_to_netinc_ttm": {"inputs": ["fcf", "netinc"], "func": f11_rqlv_109_fcf_to_netinc_ttm},
    "f11_rqlv_110_netinc_minus_ncfo_to_assets": {"inputs": ["netinc", "ncfo", "assets"], "func": f11_rqlv_110_netinc_minus_ncfo_to_assets},
    "f11_rqlv_111_log_revenue_per_dilshare_ttm": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_111_log_revenue_per_dilshare_ttm},
    "f11_rqlv_112_log_revenue_per_basicshare_ttm": {"inputs": ["revenue", "shareswa"], "func": f11_rqlv_112_log_revenue_per_basicshare_ttm},
    "f11_rqlv_113_revenue_per_share_qoq_pct_dil": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_113_revenue_per_share_qoq_pct_dil},
    "f11_rqlv_114_revenue_per_share_yoy_pct_dil": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_114_revenue_per_share_yoy_pct_dil},
    "f11_rqlv_115_share_growth_minus_revenue_growth_yoy": {"inputs": ["shareswadil", "revenue"], "func": f11_rqlv_115_share_growth_minus_revenue_growth_yoy},
    "f11_rqlv_116_dil_minus_basic_share_gap_to_basic": {"inputs": ["shareswadil", "shareswa"], "func": f11_rqlv_116_dil_minus_basic_share_gap_to_basic},
    "f11_rqlv_117_revenue_per_share_dispersion_8q": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_117_revenue_per_share_dispersion_8q},
    "f11_rqlv_118_revenue_per_share_zscore_8q": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_118_revenue_per_share_zscore_8q},
    "f11_rqlv_119_revenue_per_share_q_to_4q_max": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_119_revenue_per_share_q_to_4q_max},
    "f11_rqlv_120_revenue_per_share_q_to_4q_min": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_120_revenue_per_share_q_to_4q_min},
    "f11_rqlv_121_revenue_per_basic_share_growth_yoy": {"inputs": ["revenue", "shareswa"], "func": f11_rqlv_121_revenue_per_basic_share_growth_yoy},
    "f11_rqlv_122_revenue_per_share_qoq_cv_8q": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_122_revenue_per_share_qoq_cv_8q},
    "f11_rqlv_123_basic_minus_diluted_share_gap_growth_yoy": {"inputs": ["shareswa", "shareswadil"], "func": f11_rqlv_123_basic_minus_diluted_share_gap_growth_yoy},
    "f11_rqlv_124_revenue_per_share_yoy_minus_share_growth": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_124_revenue_per_share_yoy_minus_share_growth},
    "f11_rqlv_125_revenue_per_share_log_qoq": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_125_revenue_per_share_log_qoq},
    "f11_rqlv_126_revenue_ttm_to_capex_ttm": {"inputs": ["revenue", "capex"], "func": f11_rqlv_126_revenue_ttm_to_capex_ttm},
    "f11_rqlv_127_revenue_ttm_to_cum_capex_4q": {"inputs": ["revenue", "capex"], "func": f11_rqlv_127_revenue_ttm_to_cum_capex_4q},
    "f11_rqlv_128_revenue_ttm_to_debt": {"inputs": ["revenue", "debt"], "func": f11_rqlv_128_revenue_ttm_to_debt},
    "f11_rqlv_129_revenue_ttm_to_netdebt": {"inputs": ["revenue", "debt", "cashneq"], "func": f11_rqlv_129_revenue_ttm_to_netdebt},
    "f11_rqlv_130_revenue_ttm_to_operating_assets": {"inputs": ["revenue", "assets", "cashneq"], "func": f11_rqlv_130_revenue_ttm_to_operating_assets},
    "f11_rqlv_131_revenue_ttm_to_tangible_assets": {"inputs": ["revenue", "assets", "intangibles"], "func": f11_rqlv_131_revenue_ttm_to_tangible_assets},
    "f11_rqlv_132_revenue_ttm_to_retained_earnings": {"inputs": ["revenue", "retearn"], "func": f11_rqlv_132_revenue_ttm_to_retained_earnings},
    "f11_rqlv_133_revenue_ttm_to_tangible_book": {"inputs": ["revenue", "equity", "intangibles"], "func": f11_rqlv_133_revenue_ttm_to_tangible_book},
    "f11_rqlv_134_revenue_to_invested_capital_minus_goodwill": {"inputs": ["revenue", "equity", "debt", "intangibles"], "func": f11_rqlv_134_revenue_to_invested_capital_minus_goodwill},
    "f11_rqlv_135_revenue_q_to_q_invested_capital": {"inputs": ["revenue", "equity", "debt"], "func": f11_rqlv_135_revenue_q_to_q_invested_capital},
    "f11_rqlv_136_revenue_ttm_to_assets_minus_ttm_avg": {"inputs": ["revenue", "assets"], "func": f11_rqlv_136_revenue_ttm_to_assets_minus_ttm_avg},
    "f11_rqlv_137_revenue_ttm_per_dollar_intangible": {"inputs": ["revenue", "intangibles"], "func": f11_rqlv_137_revenue_ttm_per_dollar_intangible},
    "f11_rqlv_138_revenue_ttm_per_dollar_ppe_gross": {"inputs": ["revenue", "ppnenet"], "func": f11_rqlv_138_revenue_ttm_per_dollar_ppe_gross},
    "f11_rqlv_139_revenue_yoy_minus_capex_yoy": {"inputs": ["revenue", "capex"], "func": f11_rqlv_139_revenue_yoy_minus_capex_yoy},
    "f11_rqlv_140_revenue_yoy_minus_assets_yoy": {"inputs": ["revenue", "assets"], "func": f11_rqlv_140_revenue_yoy_minus_assets_yoy},
    "f11_rqlv_141_revenue_quality_aggregate_zscore": {"inputs": ["revenue", "ncfo", "receivables", "inventory"], "func": f11_rqlv_141_revenue_quality_aggregate_zscore},
    "f11_rqlv_142_channel_stuffing_composite": {"inputs": ["receivables", "revenue"], "func": f11_rqlv_142_channel_stuffing_composite},
    "f11_rqlv_143_accrual_pollution_index": {"inputs": ["netinc", "ncfo", "receivables", "assets"], "func": f11_rqlv_143_accrual_pollution_index},
    "f11_rqlv_144_revenue_overstatement_flag": {"inputs": ["receivables", "revenue", "ncfo"], "func": f11_rqlv_144_revenue_overstatement_flag},
    "f11_rqlv_145_one_time_revenue_spike_score": {"inputs": ["revenue"], "func": f11_rqlv_145_one_time_revenue_spike_score},
    "f11_rqlv_146_recurring_revenue_health_score": {"inputs": ["deferredrev", "revenue"], "func": f11_rqlv_146_recurring_revenue_health_score},
    "f11_rqlv_147_revenue_quality_collapse_signal": {"inputs": ["ncfo", "revenue"], "func": f11_rqlv_147_revenue_quality_collapse_signal},
    "f11_rqlv_148_revenue_smoothing_suspicion_8q": {"inputs": ["revenue"], "func": f11_rqlv_148_revenue_smoothing_suspicion_8q},
    "f11_rqlv_149_revenue_yoy_below_seasonal_avg": {"inputs": ["revenue"], "func": f11_rqlv_149_revenue_yoy_below_seasonal_avg},
    "f11_rqlv_150_revenue_quality_4q_aggregate_score": {"inputs": ["ncfo", "netinc", "receivables", "inventory", "revenue"], "func": f11_rqlv_150_revenue_quality_4q_aggregate_score},
}
