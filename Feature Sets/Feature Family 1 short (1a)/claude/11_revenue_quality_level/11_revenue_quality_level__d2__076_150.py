"""revenue_quality_level d2 features 076-150 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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
    idx = num.index if hasattr(num, 'index') else None
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

def f11_rqlv_076_revenue_qoq_max_drop_12q_d2(revenue):
    return revenue.diff().rolling(12, min_periods=4).min().diff().diff()

def f11_rqlv_077_revenue_qoq_skew_8q_d2(revenue):
    return revenue.diff().rolling(8, min_periods=4).skew().diff().diff()

def f11_rqlv_078_revenue_qoq_kurtosis_12q_d2(revenue):
    return revenue.diff().rolling(12, min_periods=5).kurt().diff().diff()

def f11_rqlv_079_revenue_minus_4q_mean_to_4q_mean_d2(revenue):
    m = revenue.rolling(4, min_periods=2).mean()
    return _safe_div(revenue - m, m.abs()).diff().diff()

def f11_rqlv_080_revenue_ttm_dispersion_4q_d2(revenue):
    rev_ttm = _ttm(revenue).replace(0, np.nan)
    quarters_share = revenue / rev_ttm
    return quarters_share.rolling(4, min_periods=2).std().diff().diff()

def f11_rqlv_081_revenue_negative_q_count_8q_d2(revenue):
    return (revenue.diff() < 0).rolling(8, min_periods=3).sum().diff().diff()

def f11_rqlv_082_revenue_acceleration_q_count_8q_d2(revenue):
    return (revenue.diff().diff() > 0).rolling(8, min_periods=3).sum().diff().diff()

def f11_rqlv_083_revenue_qoq_run_length_max_down_12q_d2(revenue):
    d = revenue.diff()
    streak = (d < 0).astype(int)
    return streak.rolling(12, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True).diff().diff()

def f11_rqlv_084_revenue_qoq_run_length_max_up_12q_d2(revenue):
    d = revenue.diff()
    streak = (d > 0).astype(int)
    return streak.rolling(12, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True).diff().diff()

def f11_rqlv_085_revenue_max_q_to_min_q_ratio_8q_d2(revenue):
    mx = revenue.rolling(8, min_periods=3).max()
    mn = revenue.rolling(8, min_periods=3).min()
    return _safe_div(mx, mn).diff().diff()

def f11_rqlv_086_revenue_smoothness_lag1_autocorr_8q_d2(revenue):
    d = revenue.diff()
    return d.rolling(8, min_periods=4).apply(lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if np.std(w[:-1]) > 0 and np.std(w[1:]) > 0 else np.nan, raw=True).diff().diff()

def f11_rqlv_087_revenue_yoy_dispersion_8q_d2(revenue):
    return _yoy_pct(_ttm(revenue)).rolling(8, min_periods=3).std().diff().diff()

def f11_rqlv_088_revenue_q_below_trailing_max_share_8q_d2(revenue):
    rmax = revenue.rolling(8, min_periods=3).max()
    return _safe_div(revenue, rmax).diff().diff()

def f11_rqlv_089_revenue_q_above_trailing_min_share_8q_d2(revenue):
    rmin = revenue.rolling(8, min_periods=3).min()
    return _safe_div(revenue, rmin).diff().diff()

def f11_rqlv_090_revenue_qoq_sign_change_count_8q_d2(revenue):
    return _sign_change(revenue.diff()).rolling(8, min_periods=3).sum().diff().diff()

def f11_rqlv_091_ncfo_to_revenue_ttm_d2(ncfo, revenue):
    return _safe_div(_ttm(ncfo), _ttm(revenue)).diff().diff()

def f11_rqlv_092_ncfo_to_revenue_q_d2(ncfo, revenue):
    return _safe_div(ncfo, revenue).diff().diff()

def f11_rqlv_093_fcf_to_revenue_q_d2(fcf, revenue):
    return _safe_div(fcf, revenue).diff().diff()

def f11_rqlv_094_netinc_to_revenue_ttm_d2(netinc, revenue):
    return _safe_div(_ttm(netinc), _ttm(revenue)).diff().diff()

def f11_rqlv_095_ncfo_minus_netinc_to_revenue_d2(ncfo, netinc, revenue):
    return _safe_div(_ttm(ncfo) - _ttm(netinc), _ttm(revenue).abs()).diff().diff()

def f11_rqlv_096_cash_conversion_ratio_ttm_d2(ncfo, netinc):
    return _safe_div(_ttm(ncfo), _ttm(netinc).abs()).diff().diff()

def f11_rqlv_097_capex_to_revenue_ttm_d2(capex, revenue):
    return _safe_div(_ttm(capex).abs(), _ttm(revenue)).diff().diff()

def f11_rqlv_098_ebitda_margin_minus_fcf_margin_ttm_d2(ebitda, fcf, revenue):
    rev = _ttm(revenue)
    return (_safe_div(_ttm(ebitda), rev) - _safe_div(_ttm(fcf), rev)).diff().diff()

def f11_rqlv_099_taxexp_to_revenue_ttm_d2(taxexp, revenue):
    return _safe_div(_ttm(taxexp), _ttm(revenue)).diff().diff()

def f11_rqlv_100_intexp_to_revenue_ttm_d2(intexp, revenue):
    return _safe_div(_ttm(intexp), _ttm(revenue)).diff().diff()

def f11_rqlv_101_depamor_to_revenue_ttm_d2(depamor, revenue):
    return _safe_div(_ttm(depamor), _ttm(revenue)).diff().diff()

def f11_rqlv_102_accrual_ratio_bs_to_revenue_d2(workingcapital, revenue):
    return _safe_div(workingcapital.diff(), _ttm(revenue).abs()).diff().diff()

def f11_rqlv_103_accrual_ratio_cf_to_revenue_d2(netinc, ncfo, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs()).diff().diff()

def f11_rqlv_104_opcf_q_minus_ttm_avg_to_revenue_d2(ncfo, revenue):
    ttm = _ttm(ncfo) / 4.0
    return _safe_div(ncfo - ttm, _ttm(revenue).abs()).diff().diff()

def f11_rqlv_105_ebit_minus_ncfo_to_revenue_d2(ebit, ncfo, revenue):
    return _safe_div(_ttm(ebit) - _ttm(ncfo), _ttm(revenue).abs()).diff().diff()

def f11_rqlv_106_revenue_minus_cogs_minus_sgna_to_revenue_d2(revenue, cor, sgna):
    return _safe_div(_ttm(revenue) - _ttm(cor) - _ttm(sgna), _ttm(revenue).abs()).diff().diff()

def f11_rqlv_107_dps_to_revenue_per_share_d2(dps, revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(dps, rps).diff().diff()

def f11_rqlv_108_eps_to_revenue_per_share_d2(eps, revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(eps, rps).diff().diff()

def f11_rqlv_109_fcf_to_netinc_ttm_d2(fcf, netinc):
    return _safe_div(_ttm(fcf), _ttm(netinc).abs()).diff().diff()

def f11_rqlv_110_netinc_minus_ncfo_to_assets_d2(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets).diff().diff()

def f11_rqlv_111_log_revenue_per_dilshare_ttm_d2(revenue, shareswadil):
    return _safe_log(_safe_div(_ttm(revenue), shareswadil)).diff().diff()

def f11_rqlv_112_log_revenue_per_basicshare_ttm_d2(revenue, shareswa):
    return _safe_log(_safe_div(_ttm(revenue), shareswa)).diff().diff()

def f11_rqlv_113_revenue_per_share_qoq_pct_dil_d2(revenue, shareswadil):
    return _qoq_pct(_safe_div(_ttm(revenue), shareswadil)).diff().diff()

def f11_rqlv_114_revenue_per_share_yoy_pct_dil_d2(revenue, shareswadil):
    return _yoy_pct(_safe_div(_ttm(revenue), shareswadil)).diff().diff()

def f11_rqlv_115_share_growth_minus_revenue_growth_yoy_d2(shareswadil, revenue):
    return (_yoy_pct(shareswadil) - _yoy_pct(_ttm(revenue))).diff().diff()

def f11_rqlv_116_dil_minus_basic_share_gap_to_basic_d2(shareswadil, shareswa):
    return _safe_div(shareswadil - shareswa, shareswa).diff().diff()

def f11_rqlv_117_revenue_per_share_dispersion_8q_d2(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return rps.rolling(8, min_periods=3).std().diff().diff()

def f11_rqlv_118_revenue_per_share_zscore_8q_d2(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _rolling_zscore(rps, 8, min_periods=3).diff().diff()

def f11_rqlv_119_revenue_per_share_q_to_4q_max_d2(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(rps, rps.rolling(4, min_periods=2).max()).diff().diff()

def f11_rqlv_120_revenue_per_share_q_to_4q_min_d2(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(rps, rps.rolling(4, min_periods=2).min()).diff().diff()

def f11_rqlv_121_revenue_per_basic_share_growth_yoy_d2(revenue, shareswa):
    return _yoy_pct(_safe_div(_ttm(revenue), shareswa)).diff().diff()

def f11_rqlv_122_revenue_per_share_qoq_cv_8q_d2(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_div(rps.rolling(8, min_periods=3).std(), rps.rolling(8, min_periods=3).mean().abs()).diff().diff()

def f11_rqlv_123_basic_minus_diluted_share_gap_growth_yoy_d2(shareswa, shareswadil):
    return (_yoy_pct(shareswadil) - _yoy_pct(shareswa)).diff().diff()

def f11_rqlv_124_revenue_per_share_yoy_minus_share_growth_d2(revenue, shareswadil):
    return (_yoy_pct(_safe_div(_ttm(revenue), shareswadil)) + _yoy_pct(shareswadil)).diff().diff()

def f11_rqlv_125_revenue_per_share_log_qoq_d2(revenue, shareswadil):
    rps = _safe_div(_ttm(revenue), shareswadil)
    return _safe_log(rps).diff().diff().diff()

def f11_rqlv_126_revenue_ttm_to_capex_ttm_d2(revenue, capex):
    return _safe_div(_ttm(revenue), _ttm(capex).abs()).diff().diff()

def f11_rqlv_127_revenue_ttm_to_cum_capex_4q_d2(revenue, capex):
    return _safe_div(_ttm(revenue), capex.abs().rolling(4, min_periods=2).sum()).diff().diff()

def f11_rqlv_128_revenue_ttm_to_debt_d2(revenue, debt):
    return _safe_div(_ttm(revenue), debt).diff().diff()

def f11_rqlv_129_revenue_ttm_to_netdebt_d2(revenue, debt, cashneq):
    return _safe_div(_ttm(revenue), debt - cashneq).diff().diff()

def f11_rqlv_130_revenue_ttm_to_operating_assets_d2(revenue, assets, cashneq):
    return _safe_div(_ttm(revenue), assets - cashneq).diff().diff()

def f11_rqlv_131_revenue_ttm_to_tangible_assets_d2(revenue, assets, intangibles):
    return _safe_div(_ttm(revenue), assets - intangibles).diff().diff()

def f11_rqlv_132_revenue_ttm_to_retained_earnings_d2(revenue, retearn):
    return _safe_div(_ttm(revenue), retearn.abs()).diff().diff()

def f11_rqlv_133_revenue_ttm_to_tangible_book_d2(revenue, equity, intangibles):
    return _safe_div(_ttm(revenue), equity - intangibles).diff().diff()

def f11_rqlv_134_revenue_to_invested_capital_minus_goodwill_d2(revenue, equity, debt, intangibles):
    return _safe_div(_ttm(revenue), equity + debt - intangibles).diff().diff()

def f11_rqlv_135_revenue_q_to_q_invested_capital_d2(revenue, equity, debt):
    return _safe_div(revenue * 4.0, equity + debt).diff().diff()

def f11_rqlv_136_revenue_ttm_to_assets_minus_ttm_avg_d2(revenue, assets):
    ratio = _safe_div(_ttm(revenue), assets)
    return (ratio - ratio.rolling(4, min_periods=2).mean()).diff().diff()

def f11_rqlv_137_revenue_ttm_per_dollar_intangible_d2(revenue, intangibles):
    return _safe_div(_ttm(revenue), intangibles).diff().diff()

def f11_rqlv_138_revenue_ttm_per_dollar_ppe_gross_d2(revenue, ppnenet):
    return _safe_div(_ttm(revenue), ppnenet).diff().diff()

def f11_rqlv_139_revenue_yoy_minus_capex_yoy_d2(revenue, capex):
    return (_yoy_pct(_ttm(revenue)) - _yoy_pct(_ttm(capex).abs())).diff().diff()

def f11_rqlv_140_revenue_yoy_minus_assets_yoy_d2(revenue, assets):
    return (_yoy_pct(_ttm(revenue)) - _yoy_pct(assets)).diff().diff()

def f11_rqlv_141_revenue_quality_aggregate_zscore_d2(revenue, ncfo, receivables, inventory):
    cash_conv = _safe_div(_ttm(ncfo), _ttm(revenue).abs())
    dso = _safe_div(receivables, _ttm(revenue).abs())
    dio = _safe_div(inventory, _ttm(revenue).abs())
    z_cc = _rolling_zscore(cash_conv, 12, min_periods=4)
    z_dso = _rolling_zscore(dso, 12, min_periods=4)
    z_dio = _rolling_zscore(dio, 12, min_periods=4)
    return (z_cc - z_dso - z_dio).diff().diff()

def f11_rqlv_142_channel_stuffing_composite_d2(receivables, revenue):
    rec_yoy = _yoy_pct(receivables)
    rev_yoy = _yoy_pct(_ttm(revenue))
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    dso_zscore = _rolling_zscore(dso, 8, min_periods=3)
    return ((rec_yoy - rev_yoy).clip(lower=-5, upper=5) + dso_zscore.clip(lower=-5, upper=5)).diff().diff()

def f11_rqlv_143_accrual_pollution_index_d2(netinc, ncfo, receivables, assets):
    accrual_share = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    rec_share = _safe_div(receivables, assets)
    return (_rolling_zscore(accrual_share, 8, 3) + _rolling_zscore(rec_share, 8, 3)).diff().diff()

def f11_rqlv_144_revenue_overstatement_flag_d2(receivables, revenue, ncfo):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    cash_conv = _safe_div(_ttm(ncfo), _ttm(revenue).abs())
    return (_rolling_zscore(dso, 12, 4) - _rolling_zscore(cash_conv, 12, 4)).diff().diff()

def f11_rqlv_145_one_time_revenue_spike_score_d2(revenue):
    q_ann = revenue * 4.0
    ttm = _ttm(revenue)
    z = _rolling_zscore(_safe_div(q_ann, ttm.abs()), 8, min_periods=3)
    return z.diff().diff()

def f11_rqlv_146_recurring_revenue_health_score_d2(deferredrev, revenue):
    ratio = _safe_div(deferredrev * 4.0, _ttm(revenue))
    return _rolling_zscore(ratio, 8, 3).diff().diff()

def f11_rqlv_147_revenue_quality_collapse_signal_d2(ncfo, revenue):
    cash_conv = _safe_div(ncfo, revenue.abs())
    return (cash_conv - cash_conv.rolling(4, min_periods=2).mean().shift(1)).diff().diff()

def f11_rqlv_148_revenue_smoothing_suspicion_8q_d2(revenue):
    cv = _safe_div(revenue.diff().rolling(8, min_periods=3).std(), revenue.rolling(8, min_periods=3).mean().abs())
    return (-cv).diff().diff()

def f11_rqlv_149_revenue_yoy_below_seasonal_avg_d2(revenue):
    yoy = _yoy_pct(_ttm(revenue))
    return (yoy - yoy.rolling(8, min_periods=4).mean()).diff().diff()

def f11_rqlv_150_revenue_quality_4q_aggregate_score_d2(ncfo, netinc, receivables, inventory, revenue):
    cash_conv = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    rec_intensity = _safe_div(receivables, _ttm(revenue).abs())
    inv_intensity = _safe_div(inventory, _ttm(revenue).abs())
    z_cc = _rolling_zscore(cash_conv, 4, 2)
    z_ri = _rolling_zscore(rec_intensity, 4, 2)
    z_ii = _rolling_zscore(inv_intensity, 4, 2)
    return (z_cc - z_ri - z_ii).diff().diff()
REVENUE_QUALITY_LEVEL_D2_REGISTRY_076_150 = {'f11_rqlv_076_revenue_qoq_max_drop_12q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_076_revenue_qoq_max_drop_12q_d2}, 'f11_rqlv_077_revenue_qoq_skew_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_077_revenue_qoq_skew_8q_d2}, 'f11_rqlv_078_revenue_qoq_kurtosis_12q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_078_revenue_qoq_kurtosis_12q_d2}, 'f11_rqlv_079_revenue_minus_4q_mean_to_4q_mean_d2': {'inputs': ['revenue'], 'func': f11_rqlv_079_revenue_minus_4q_mean_to_4q_mean_d2}, 'f11_rqlv_080_revenue_ttm_dispersion_4q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_080_revenue_ttm_dispersion_4q_d2}, 'f11_rqlv_081_revenue_negative_q_count_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_081_revenue_negative_q_count_8q_d2}, 'f11_rqlv_082_revenue_acceleration_q_count_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_082_revenue_acceleration_q_count_8q_d2}, 'f11_rqlv_083_revenue_qoq_run_length_max_down_12q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_083_revenue_qoq_run_length_max_down_12q_d2}, 'f11_rqlv_084_revenue_qoq_run_length_max_up_12q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_084_revenue_qoq_run_length_max_up_12q_d2}, 'f11_rqlv_085_revenue_max_q_to_min_q_ratio_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_085_revenue_max_q_to_min_q_ratio_8q_d2}, 'f11_rqlv_086_revenue_smoothness_lag1_autocorr_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_086_revenue_smoothness_lag1_autocorr_8q_d2}, 'f11_rqlv_087_revenue_yoy_dispersion_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_087_revenue_yoy_dispersion_8q_d2}, 'f11_rqlv_088_revenue_q_below_trailing_max_share_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_088_revenue_q_below_trailing_max_share_8q_d2}, 'f11_rqlv_089_revenue_q_above_trailing_min_share_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_089_revenue_q_above_trailing_min_share_8q_d2}, 'f11_rqlv_090_revenue_qoq_sign_change_count_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_090_revenue_qoq_sign_change_count_8q_d2}, 'f11_rqlv_091_ncfo_to_revenue_ttm_d2': {'inputs': ['ncfo', 'revenue'], 'func': f11_rqlv_091_ncfo_to_revenue_ttm_d2}, 'f11_rqlv_092_ncfo_to_revenue_q_d2': {'inputs': ['ncfo', 'revenue'], 'func': f11_rqlv_092_ncfo_to_revenue_q_d2}, 'f11_rqlv_093_fcf_to_revenue_q_d2': {'inputs': ['fcf', 'revenue'], 'func': f11_rqlv_093_fcf_to_revenue_q_d2}, 'f11_rqlv_094_netinc_to_revenue_ttm_d2': {'inputs': ['netinc', 'revenue'], 'func': f11_rqlv_094_netinc_to_revenue_ttm_d2}, 'f11_rqlv_095_ncfo_minus_netinc_to_revenue_d2': {'inputs': ['ncfo', 'netinc', 'revenue'], 'func': f11_rqlv_095_ncfo_minus_netinc_to_revenue_d2}, 'f11_rqlv_096_cash_conversion_ratio_ttm_d2': {'inputs': ['ncfo', 'netinc'], 'func': f11_rqlv_096_cash_conversion_ratio_ttm_d2}, 'f11_rqlv_097_capex_to_revenue_ttm_d2': {'inputs': ['capex', 'revenue'], 'func': f11_rqlv_097_capex_to_revenue_ttm_d2}, 'f11_rqlv_098_ebitda_margin_minus_fcf_margin_ttm_d2': {'inputs': ['ebitda', 'fcf', 'revenue'], 'func': f11_rqlv_098_ebitda_margin_minus_fcf_margin_ttm_d2}, 'f11_rqlv_099_taxexp_to_revenue_ttm_d2': {'inputs': ['taxexp', 'revenue'], 'func': f11_rqlv_099_taxexp_to_revenue_ttm_d2}, 'f11_rqlv_100_intexp_to_revenue_ttm_d2': {'inputs': ['intexp', 'revenue'], 'func': f11_rqlv_100_intexp_to_revenue_ttm_d2}, 'f11_rqlv_101_depamor_to_revenue_ttm_d2': {'inputs': ['depamor', 'revenue'], 'func': f11_rqlv_101_depamor_to_revenue_ttm_d2}, 'f11_rqlv_102_accrual_ratio_bs_to_revenue_d2': {'inputs': ['workingcapital', 'revenue'], 'func': f11_rqlv_102_accrual_ratio_bs_to_revenue_d2}, 'f11_rqlv_103_accrual_ratio_cf_to_revenue_d2': {'inputs': ['netinc', 'ncfo', 'revenue'], 'func': f11_rqlv_103_accrual_ratio_cf_to_revenue_d2}, 'f11_rqlv_104_opcf_q_minus_ttm_avg_to_revenue_d2': {'inputs': ['ncfo', 'revenue'], 'func': f11_rqlv_104_opcf_q_minus_ttm_avg_to_revenue_d2}, 'f11_rqlv_105_ebit_minus_ncfo_to_revenue_d2': {'inputs': ['ebit', 'ncfo', 'revenue'], 'func': f11_rqlv_105_ebit_minus_ncfo_to_revenue_d2}, 'f11_rqlv_106_revenue_minus_cogs_minus_sgna_to_revenue_d2': {'inputs': ['revenue', 'cor', 'sgna'], 'func': f11_rqlv_106_revenue_minus_cogs_minus_sgna_to_revenue_d2}, 'f11_rqlv_107_dps_to_revenue_per_share_d2': {'inputs': ['dps', 'revenue', 'shareswadil'], 'func': f11_rqlv_107_dps_to_revenue_per_share_d2}, 'f11_rqlv_108_eps_to_revenue_per_share_d2': {'inputs': ['eps', 'revenue', 'shareswadil'], 'func': f11_rqlv_108_eps_to_revenue_per_share_d2}, 'f11_rqlv_109_fcf_to_netinc_ttm_d2': {'inputs': ['fcf', 'netinc'], 'func': f11_rqlv_109_fcf_to_netinc_ttm_d2}, 'f11_rqlv_110_netinc_minus_ncfo_to_assets_d2': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f11_rqlv_110_netinc_minus_ncfo_to_assets_d2}, 'f11_rqlv_111_log_revenue_per_dilshare_ttm_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_111_log_revenue_per_dilshare_ttm_d2}, 'f11_rqlv_112_log_revenue_per_basicshare_ttm_d2': {'inputs': ['revenue', 'shareswa'], 'func': f11_rqlv_112_log_revenue_per_basicshare_ttm_d2}, 'f11_rqlv_113_revenue_per_share_qoq_pct_dil_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_113_revenue_per_share_qoq_pct_dil_d2}, 'f11_rqlv_114_revenue_per_share_yoy_pct_dil_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_114_revenue_per_share_yoy_pct_dil_d2}, 'f11_rqlv_115_share_growth_minus_revenue_growth_yoy_d2': {'inputs': ['shareswadil', 'revenue'], 'func': f11_rqlv_115_share_growth_minus_revenue_growth_yoy_d2}, 'f11_rqlv_116_dil_minus_basic_share_gap_to_basic_d2': {'inputs': ['shareswadil', 'shareswa'], 'func': f11_rqlv_116_dil_minus_basic_share_gap_to_basic_d2}, 'f11_rqlv_117_revenue_per_share_dispersion_8q_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_117_revenue_per_share_dispersion_8q_d2}, 'f11_rqlv_118_revenue_per_share_zscore_8q_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_118_revenue_per_share_zscore_8q_d2}, 'f11_rqlv_119_revenue_per_share_q_to_4q_max_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_119_revenue_per_share_q_to_4q_max_d2}, 'f11_rqlv_120_revenue_per_share_q_to_4q_min_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_120_revenue_per_share_q_to_4q_min_d2}, 'f11_rqlv_121_revenue_per_basic_share_growth_yoy_d2': {'inputs': ['revenue', 'shareswa'], 'func': f11_rqlv_121_revenue_per_basic_share_growth_yoy_d2}, 'f11_rqlv_122_revenue_per_share_qoq_cv_8q_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_122_revenue_per_share_qoq_cv_8q_d2}, 'f11_rqlv_123_basic_minus_diluted_share_gap_growth_yoy_d2': {'inputs': ['shareswa', 'shareswadil'], 'func': f11_rqlv_123_basic_minus_diluted_share_gap_growth_yoy_d2}, 'f11_rqlv_124_revenue_per_share_yoy_minus_share_growth_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_124_revenue_per_share_yoy_minus_share_growth_d2}, 'f11_rqlv_125_revenue_per_share_log_qoq_d2': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_125_revenue_per_share_log_qoq_d2}, 'f11_rqlv_126_revenue_ttm_to_capex_ttm_d2': {'inputs': ['revenue', 'capex'], 'func': f11_rqlv_126_revenue_ttm_to_capex_ttm_d2}, 'f11_rqlv_127_revenue_ttm_to_cum_capex_4q_d2': {'inputs': ['revenue', 'capex'], 'func': f11_rqlv_127_revenue_ttm_to_cum_capex_4q_d2}, 'f11_rqlv_128_revenue_ttm_to_debt_d2': {'inputs': ['revenue', 'debt'], 'func': f11_rqlv_128_revenue_ttm_to_debt_d2}, 'f11_rqlv_129_revenue_ttm_to_netdebt_d2': {'inputs': ['revenue', 'debt', 'cashneq'], 'func': f11_rqlv_129_revenue_ttm_to_netdebt_d2}, 'f11_rqlv_130_revenue_ttm_to_operating_assets_d2': {'inputs': ['revenue', 'assets', 'cashneq'], 'func': f11_rqlv_130_revenue_ttm_to_operating_assets_d2}, 'f11_rqlv_131_revenue_ttm_to_tangible_assets_d2': {'inputs': ['revenue', 'assets', 'intangibles'], 'func': f11_rqlv_131_revenue_ttm_to_tangible_assets_d2}, 'f11_rqlv_132_revenue_ttm_to_retained_earnings_d2': {'inputs': ['revenue', 'retearn'], 'func': f11_rqlv_132_revenue_ttm_to_retained_earnings_d2}, 'f11_rqlv_133_revenue_ttm_to_tangible_book_d2': {'inputs': ['revenue', 'equity', 'intangibles'], 'func': f11_rqlv_133_revenue_ttm_to_tangible_book_d2}, 'f11_rqlv_134_revenue_to_invested_capital_minus_goodwill_d2': {'inputs': ['revenue', 'equity', 'debt', 'intangibles'], 'func': f11_rqlv_134_revenue_to_invested_capital_minus_goodwill_d2}, 'f11_rqlv_135_revenue_q_to_q_invested_capital_d2': {'inputs': ['revenue', 'equity', 'debt'], 'func': f11_rqlv_135_revenue_q_to_q_invested_capital_d2}, 'f11_rqlv_136_revenue_ttm_to_assets_minus_ttm_avg_d2': {'inputs': ['revenue', 'assets'], 'func': f11_rqlv_136_revenue_ttm_to_assets_minus_ttm_avg_d2}, 'f11_rqlv_137_revenue_ttm_per_dollar_intangible_d2': {'inputs': ['revenue', 'intangibles'], 'func': f11_rqlv_137_revenue_ttm_per_dollar_intangible_d2}, 'f11_rqlv_138_revenue_ttm_per_dollar_ppe_gross_d2': {'inputs': ['revenue', 'ppnenet'], 'func': f11_rqlv_138_revenue_ttm_per_dollar_ppe_gross_d2}, 'f11_rqlv_139_revenue_yoy_minus_capex_yoy_d2': {'inputs': ['revenue', 'capex'], 'func': f11_rqlv_139_revenue_yoy_minus_capex_yoy_d2}, 'f11_rqlv_140_revenue_yoy_minus_assets_yoy_d2': {'inputs': ['revenue', 'assets'], 'func': f11_rqlv_140_revenue_yoy_minus_assets_yoy_d2}, 'f11_rqlv_141_revenue_quality_aggregate_zscore_d2': {'inputs': ['revenue', 'ncfo', 'receivables', 'inventory'], 'func': f11_rqlv_141_revenue_quality_aggregate_zscore_d2}, 'f11_rqlv_142_channel_stuffing_composite_d2': {'inputs': ['receivables', 'revenue'], 'func': f11_rqlv_142_channel_stuffing_composite_d2}, 'f11_rqlv_143_accrual_pollution_index_d2': {'inputs': ['netinc', 'ncfo', 'receivables', 'assets'], 'func': f11_rqlv_143_accrual_pollution_index_d2}, 'f11_rqlv_144_revenue_overstatement_flag_d2': {'inputs': ['receivables', 'revenue', 'ncfo'], 'func': f11_rqlv_144_revenue_overstatement_flag_d2}, 'f11_rqlv_145_one_time_revenue_spike_score_d2': {'inputs': ['revenue'], 'func': f11_rqlv_145_one_time_revenue_spike_score_d2}, 'f11_rqlv_146_recurring_revenue_health_score_d2': {'inputs': ['deferredrev', 'revenue'], 'func': f11_rqlv_146_recurring_revenue_health_score_d2}, 'f11_rqlv_147_revenue_quality_collapse_signal_d2': {'inputs': ['ncfo', 'revenue'], 'func': f11_rqlv_147_revenue_quality_collapse_signal_d2}, 'f11_rqlv_148_revenue_smoothing_suspicion_8q_d2': {'inputs': ['revenue'], 'func': f11_rqlv_148_revenue_smoothing_suspicion_8q_d2}, 'f11_rqlv_149_revenue_yoy_below_seasonal_avg_d2': {'inputs': ['revenue'], 'func': f11_rqlv_149_revenue_yoy_below_seasonal_avg_d2}, 'f11_rqlv_150_revenue_quality_4q_aggregate_score_d2': {'inputs': ['ncfo', 'netinc', 'receivables', 'inventory', 'revenue'], 'func': f11_rqlv_150_revenue_quality_4q_aggregate_score_d2}}