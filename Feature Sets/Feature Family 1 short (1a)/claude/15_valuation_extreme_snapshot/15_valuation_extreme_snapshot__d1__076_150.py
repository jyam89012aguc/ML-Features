"""valuation_extreme_snapshot d1 features — first-derivative wrappers (rate)."""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _winsorize(s, lower=0.01, upper=0.99):
    lo = s.quantile(lower)
    hi = s.quantile(upper)
    return s.clip(lower=lo, upper=hi)


# ============================================================
#                    D1 FEATURES
# ============================================================

def f15_vesp_076_composite_z_pe_evebitda_1260d_d1(pe: pd.Series, evebitda: pd.Series):
    return ((_rolling_zscore(pe, 1260) + _rolling_zscore(evebitda, 1260)) / 2.0).diff()


def f15_vesp_077_composite_z_ps_evsales_504d_d1(ps: pd.Series, evsales: pd.Series):
    return ((_rolling_zscore(ps, 504) + _rolling_zscore(evsales, 504)) / 2.0).diff()


def f15_vesp_078_composite_z_pb_mcap_tangibles_1260d_d1(pb: pd.Series, marketcap: pd.Series, tangibles: pd.Series):
    mt = _safe_div(marketcap, tangibles)
    return ((_rolling_zscore(pb, 1260) + _rolling_zscore(mt, 1260)) / 2.0).diff()


def f15_vesp_079_max_z_across_multiples_252d_d1(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series):
    df = pd.concat([_rolling_zscore(pe, YDAYS), _rolling_zscore(ps, YDAYS), _rolling_zscore(pb, YDAYS), _rolling_zscore(evebitda, YDAYS)], axis=1)
    return (df.max(axis=1)).diff()


def f15_vesp_080_min_z_across_multiples_252d_d1(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series):
    df = pd.concat([_rolling_zscore(pe, YDAYS), _rolling_zscore(ps, YDAYS), _rolling_zscore(pb, YDAYS), _rolling_zscore(evebitda, YDAYS)], axis=1)
    return (df.min(axis=1)).diff()


def f15_vesp_081_count_multiples_above_z2_252d_d1(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series):
    df = pd.concat([_rolling_zscore(pe, YDAYS), _rolling_zscore(ps, YDAYS), _rolling_zscore(pb, YDAYS), _rolling_zscore(evebitda, YDAYS)], axis=1)
    return ((df > 2.0).sum(axis=1).astype(float)).diff()


def f15_vesp_082_mcap_gt_10x_revenue_flag_d1(marketcap: pd.Series, revenue: pd.Series):
    flag = (marketcap > 10.0 * revenue).astype(float)
    return (flag.where(~(marketcap.isna() | revenue.isna()), np.nan)).diff()


def f15_vesp_083_mcap_gt_5x_book_flag_d1(marketcap: pd.Series, equity: pd.Series):
    flag = (marketcap > 5.0 * equity).astype(float)
    return (flag.where(~(marketcap.isna() | equity.isna()), np.nan)).diff()


def f15_vesp_084_evsales_gt_20_flag_d1(evsales: pd.Series):
    flag = (evsales > 20.0).astype(float)
    return (flag.where(~evsales.isna(), np.nan)).diff()


def f15_vesp_085_evebitda_gt_50_flag_d1(evebitda: pd.Series):
    flag = (evebitda > 50.0).astype(float)
    return (flag.where(~evebitda.isna(), np.nan)).diff()


def f15_vesp_086_pe_gt_100_flag_d1(pe: pd.Series):
    flag = (pe > 100.0).astype(float)
    return (flag.where(~pe.isna(), np.nan)).diff()


def f15_vesp_087_ps_gt_15_flag_d1(ps: pd.Series):
    flag = (ps > 15.0).astype(float)
    return (flag.where(~ps.isna(), np.nan)).diff()


def f15_vesp_088_pb_gt_10_flag_d1(pb: pd.Series):
    flag = (pb > 10.0).astype(float)
    return (flag.where(~pb.isna(), np.nan)).diff()


def f15_vesp_089_mcap_gt_20x_fcf_flag_d1(marketcap: pd.Series, fcf: pd.Series):
    flag = ((fcf > 0) & (marketcap > 20.0 * fcf)).astype(float)
    return (flag.where(~(marketcap.isna() | fcf.isna()), np.nan)).diff()


def f15_vesp_090_evebit_gt_40_flag_d1(evebit: pd.Series):
    flag = (evebit > 40.0).astype(float)
    return (flag.where(~evebit.isna(), np.nan)).diff()


def f15_vesp_091_bubble_count_total_d1(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series, evsales: pd.Series):
    c = (pe > 100.0).astype(float) + (ps > 15.0).astype(float) + (pb > 10.0).astype(float) + (evebitda > 50.0).astype(float) + (evsales > 20.0).astype(float)
    return (c).diff()


def f15_vesp_092_bvps_growth_minus_price_growth_252d_d1(equity: pd.Series, shareswa: pd.Series, marketcap: pd.Series):
    bvps = _safe_div(equity, shareswa)
    pps = _safe_div(marketcap, shareswa)
    return (bvps.pct_change(YDAYS) - pps.pct_change(YDAYS)).diff()


def f15_vesp_093_eps_yield_d1(eps: pd.Series, marketcap: pd.Series, shareswa: pd.Series):
    pps = _safe_div(marketcap, shareswa)
    return (_safe_div(eps, pps)).diff()


def f15_vesp_094_eps_growth_minus_price_growth_252d_d1(eps: pd.Series, marketcap: pd.Series, shareswa: pd.Series):
    pps = _safe_div(marketcap, shareswa)
    return (eps.pct_change(YDAYS) - pps.pct_change(YDAYS)).diff()


def f15_vesp_095_bvps_minus_eps_growth_252d_d1(equity: pd.Series, shareswa: pd.Series, eps: pd.Series):
    bvps = _safe_div(equity, shareswa)
    return (bvps.pct_change(YDAYS) - eps.pct_change(YDAYS)).diff()


def f15_vesp_096_eps_to_epsdil_gap_d1(eps: pd.Series, epsdil: pd.Series):
    return (eps - epsdil).diff()


def f15_vesp_097_pps_growth_252d_d1(marketcap: pd.Series, shareswa: pd.Series):
    pps = _safe_div(marketcap, shareswa)
    return (pps.pct_change(YDAYS)).diff()


def f15_vesp_098_bvps_level_d1(equity: pd.Series, shareswa: pd.Series):
    return (_safe_div(equity, shareswa)).diff()


def f15_vesp_099_eps_yield_dilution_adjusted_d1(epsdil: pd.Series, marketcap: pd.Series, shareswadil: pd.Series):
    pps_d = _safe_div(marketcap, shareswadil)
    return (_safe_div(epsdil, pps_d)).diff()


def f15_vesp_100_mcap_to_cashneq_d1(marketcap: pd.Series, cashneq: pd.Series):
    return (_safe_div(marketcap, cashneq)).diff()


def f15_vesp_101_mcap_to_assets_d1(marketcap: pd.Series, assets: pd.Series):
    return (_safe_div(marketcap, assets)).diff()


def f15_vesp_102_mcap_to_equity_d1(marketcap: pd.Series, equity: pd.Series):
    return (_safe_div(marketcap, equity)).diff()


def f15_vesp_103_mcap_to_tangible_book_d1(marketcap: pd.Series, tangibles: pd.Series):
    return (_safe_div(marketcap, tangibles)).diff()


def f15_vesp_104_mcap_minus_cash_to_equity_d1(marketcap: pd.Series, cashneq: pd.Series, equity: pd.Series):
    return (_safe_div(marketcap - cashneq.fillna(0), equity)).diff()


def f15_vesp_105_mcap_to_debt_d1(marketcap: pd.Series, debt: pd.Series):
    return (_safe_div(marketcap, debt)).diff()


def f15_vesp_106_mcap_to_retained_earnings_d1(marketcap: pd.Series, retearn: pd.Series):
    return (_safe_div(marketcap, retearn)).diff()


def f15_vesp_107_mcap_to_capex_d1(marketcap: pd.Series, capex: pd.Series):
    return (_safe_div(marketcap, capex.abs())).diff()


def f15_vesp_108_mcap_to_sbcomp_d1(marketcap: pd.Series, sbcomp: pd.Series):
    return (_safe_div(marketcap, sbcomp)).diff()


def f15_vesp_109_mcap_to_gp_d1(marketcap: pd.Series, gp: pd.Series):
    return (_safe_div(marketcap, gp)).diff()


def f15_vesp_110_dilution_adjusted_pe_d1(pe: pd.Series, shareswadil: pd.Series, shareswa: pd.Series):
    factor = _safe_div(shareswadil, shareswa)
    return (pe * factor).diff()


def f15_vesp_111_dilution_adjusted_ps_d1(ps: pd.Series, shareswadil: pd.Series, shareswa: pd.Series):
    factor = _safe_div(shareswadil, shareswa)
    return (ps * factor).diff()


def f15_vesp_112_dilution_adjusted_pb_d1(pb: pd.Series, shareswadil: pd.Series, shareswa: pd.Series):
    factor = _safe_div(shareswadil, shareswa)
    return (pb * factor).diff()


def f15_vesp_113_dilution_adjusted_evsales_d1(evsales: pd.Series, shareswadil: pd.Series, shareswa: pd.Series):
    factor = _safe_div(shareswadil, shareswa)
    return (evsales * factor).diff()


def f15_vesp_114_dilution_factor_level_d1(shareswadil: pd.Series, shareswa: pd.Series):
    return (_safe_div(shareswadil, shareswa)).diff()


def f15_vesp_115_dilution_overhang_minus_one_d1(shareswadil: pd.Series, shareswa: pd.Series):
    return (_safe_div(shareswadil, shareswa) - 1.0).diff()


def f15_vesp_116_pe_frac_above_p80_252d_d1(pe: pd.Series):
    q = pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    return ((pe > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f15_vesp_117_ps_frac_above_p80_252d_d1(ps: pd.Series):
    q = ps.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    return ((ps > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f15_vesp_118_pb_frac_above_p80_252d_d1(pb: pd.Series):
    q = pb.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    return ((pb > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f15_vesp_119_evebitda_frac_above_p80_252d_d1(evebitda: pd.Series):
    q = evebitda.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    return ((evebitda > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f15_vesp_120_pe_frac_above_p80_1260d_d1(pe: pd.Series):
    q = pe.rolling(1260, min_periods=YDAYS).quantile(0.8)
    return ((pe > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f15_vesp_121_ps_frac_above_p80_1260d_d1(ps: pd.Series):
    q = ps.rolling(1260, min_periods=YDAYS).quantile(0.8)
    return ((ps > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f15_vesp_122_evsales_frac_above_p80_1260d_d1(evsales: pd.Series):
    q = evsales.rolling(1260, min_periods=YDAYS).quantile(0.8)
    return ((evsales > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f15_vesp_123_composite_persistence_above_p80_d1(pe: pd.Series, ps: pd.Series, evebitda: pd.Series):
    qe = pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    qs = ps.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    qb = evebitda.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    return (((pe > qe).astype(float).rolling(YDAYS, min_periods=QDAYS).mean() + (ps > qs).astype(float).rolling(YDAYS, min_periods=QDAYS).mean() + (evebitda > qb).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()) / 3.0).diff()


def f15_vesp_124_pe_change_minus_earnings_change_252d_d1(pe: pd.Series, netinc: pd.Series):
    return (pe.pct_change(YDAYS) - netinc.pct_change(YDAYS)).diff()


def f15_vesp_125_ps_change_minus_revenue_change_252d_d1(ps: pd.Series, revenue: pd.Series):
    return (ps.pct_change(YDAYS) - revenue.pct_change(YDAYS)).diff()


def f15_vesp_126_evebitda_change_minus_ebitda_change_252d_d1(evebitda: pd.Series, ebitda: pd.Series):
    return (evebitda.pct_change(YDAYS) - ebitda.pct_change(YDAYS)).diff()


def f15_vesp_127_pb_change_minus_equity_change_252d_d1(pb: pd.Series, equity: pd.Series):
    return (pb.pct_change(YDAYS) - equity.pct_change(YDAYS)).diff()


def f15_vesp_128_evsales_change_minus_revenue_change_252d_d1(evsales: pd.Series, revenue: pd.Series):
    return (evsales.pct_change(YDAYS) - revenue.pct_change(YDAYS)).diff()


def f15_vesp_129_mcap_change_minus_book_change_252d_d1(marketcap: pd.Series, equity: pd.Series):
    return (marketcap.pct_change(YDAYS) - equity.pct_change(YDAYS)).diff()


def f15_vesp_130_mcap_change_minus_fcf_change_252d_d1(marketcap: pd.Series, fcf: pd.Series):
    return (marketcap.pct_change(YDAYS) - fcf.pct_change(YDAYS)).diff()


def f15_vesp_131_mcap_change_minus_revenue_change_504d_d1(marketcap: pd.Series, revenue: pd.Series):
    return (marketcap.pct_change(504) - revenue.pct_change(504)).diff()


def f15_vesp_132_ps_over_gm_times_rev_growth_d1(ps: pd.Series, gp: pd.Series, revenue: pd.Series):
    gm = _safe_div(gp, revenue)
    rg = revenue.pct_change(YDAYS)
    return (_safe_div(ps, gm * rg)).diff()


def f15_vesp_133_evsales_over_gm_times_rev_growth_d1(evsales: pd.Series, gp: pd.Series, revenue: pd.Series):
    gm = _safe_div(gp, revenue)
    rg = revenue.pct_change(YDAYS)
    return (_safe_div(evsales, gm * rg)).diff()


def f15_vesp_134_pe_over_eps_growth_times_roa_d1(pe: pd.Series, eps: pd.Series, netinc: pd.Series, assets: pd.Series):
    eg = eps.pct_change(YDAYS)
    roa = _safe_div(netinc, assets)
    return (_safe_div(pe, eg * roa)).diff()


def f15_vesp_135_evebitda_over_ebitda_margin_d1(evebitda: pd.Series, ebitda: pd.Series, revenue: pd.Series):
    margin = _safe_div(ebitda, revenue)
    return (_safe_div(evebitda, margin)).diff()


def f15_vesp_136_pb_over_roe_d1(pb: pd.Series, netinc: pd.Series, equity: pd.Series):
    roe = _safe_div(netinc, equity)
    return (_safe_div(pb, roe)).diff()


def f15_vesp_137_ps_over_ebitda_margin_d1(ps: pd.Series, ebitda: pd.Series, revenue: pd.Series):
    margin = _safe_div(ebitda, revenue)
    return (_safe_div(ps, margin)).diff()


def f15_vesp_138_pe_distance_to_p50_252d_d1(pe: pd.Series):
    return (pe - pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.5)).diff()


def f15_vesp_139_pe_distance_to_p90_1260d_d1(pe: pd.Series):
    return (pe - pe.rolling(1260, min_periods=YDAYS).quantile(0.9)).diff()


def f15_vesp_140_pe_distance_to_p99_1260d_d1(pe: pd.Series):
    return (pe - pe.rolling(1260, min_periods=YDAYS).quantile(0.99)).diff()


def f15_vesp_141_ps_distance_to_p50_252d_d1(ps: pd.Series):
    return (ps - ps.rolling(YDAYS, min_periods=QDAYS).quantile(0.5)).diff()


def f15_vesp_142_ps_distance_to_p90_1260d_d1(ps: pd.Series):
    return (ps - ps.rolling(1260, min_periods=YDAYS).quantile(0.9)).diff()


def f15_vesp_143_evebitda_distance_to_p90_1260d_d1(evebitda: pd.Series):
    return (evebitda - evebitda.rolling(1260, min_periods=YDAYS).quantile(0.9)).diff()


def f15_vesp_144_pb_distance_to_p90_1260d_d1(pb: pd.Series):
    return (pb - pb.rolling(1260, min_periods=YDAYS).quantile(0.9)).diff()


def f15_vesp_145_evsales_distance_to_p99_1260d_d1(evsales: pd.Series):
    return (evsales - evsales.rolling(1260, min_periods=YDAYS).quantile(0.99)).diff()


def f15_vesp_146_ev_to_revenue_plus_ebitda_d1(ev: pd.Series, revenue: pd.Series, ebitda: pd.Series):
    return (_safe_div(ev, revenue.fillna(0) + ebitda.fillna(0))).diff()


def f15_vesp_147_log_mcap_to_cash_minus_debt_d1(marketcap: pd.Series, cashneq: pd.Series, debt: pd.Series):
    net_cash = cashneq.fillna(0) - debt.fillna(0)
    return (_safe_log(_safe_div(marketcap, net_cash))).diff()


def f15_vesp_148_extreme_breadth_252d_d1(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series, evsales: pd.Series):
    df = pd.concat([_rolling_zscore(pe, YDAYS), _rolling_zscore(ps, YDAYS), _rolling_zscore(pb, YDAYS), _rolling_zscore(evebitda, YDAYS), _rolling_zscore(evsales, YDAYS)], axis=1)
    return ((df > 1.0).astype(float).mean(axis=1)).diff()


def f15_vesp_149_valuation_to_quality_index_d1(ps: pd.Series, pb: pd.Series, netinc: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series):
    roe = _safe_div(netinc, equity)
    margin = _safe_div(ebitda, revenue)
    return (_safe_div(ps.fillna(0) + pb.fillna(0), roe.fillna(0) + margin.fillna(0))).diff()


def f15_vesp_150_log_extreme_intensity_d1(pe: pd.Series, ps: pd.Series, evsales: pd.Series, evebitda: pd.Series):
    return (_safe_log(pe) + _safe_log(ps) + _safe_log(evsales) + _safe_log(evebitda)).diff()



# ============================================================
#                        REGISTRY
# ============================================================

VALUATION_EXTREME_SNAPSHOT_D1_REGISTRY_076_150 = {
    "f15_vesp_076_composite_z_pe_evebitda_1260d_d1": {"inputs": ["pe", "evebitda"], "func": f15_vesp_076_composite_z_pe_evebitda_1260d_d1},
    "f15_vesp_077_composite_z_ps_evsales_504d_d1": {"inputs": ["ps", "evsales"], "func": f15_vesp_077_composite_z_ps_evsales_504d_d1},
    "f15_vesp_078_composite_z_pb_mcap_tangibles_1260d_d1": {"inputs": ["pb", "marketcap", "tangibles"], "func": f15_vesp_078_composite_z_pb_mcap_tangibles_1260d_d1},
    "f15_vesp_079_max_z_across_multiples_252d_d1": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_079_max_z_across_multiples_252d_d1},
    "f15_vesp_080_min_z_across_multiples_252d_d1": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_080_min_z_across_multiples_252d_d1},
    "f15_vesp_081_count_multiples_above_z2_252d_d1": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_081_count_multiples_above_z2_252d_d1},
    "f15_vesp_082_mcap_gt_10x_revenue_flag_d1": {"inputs": ["marketcap", "revenue"], "func": f15_vesp_082_mcap_gt_10x_revenue_flag_d1},
    "f15_vesp_083_mcap_gt_5x_book_flag_d1": {"inputs": ["marketcap", "equity"], "func": f15_vesp_083_mcap_gt_5x_book_flag_d1},
    "f15_vesp_084_evsales_gt_20_flag_d1": {"inputs": ["evsales"], "func": f15_vesp_084_evsales_gt_20_flag_d1},
    "f15_vesp_085_evebitda_gt_50_flag_d1": {"inputs": ["evebitda"], "func": f15_vesp_085_evebitda_gt_50_flag_d1},
    "f15_vesp_086_pe_gt_100_flag_d1": {"inputs": ["pe"], "func": f15_vesp_086_pe_gt_100_flag_d1},
    "f15_vesp_087_ps_gt_15_flag_d1": {"inputs": ["ps"], "func": f15_vesp_087_ps_gt_15_flag_d1},
    "f15_vesp_088_pb_gt_10_flag_d1": {"inputs": ["pb"], "func": f15_vesp_088_pb_gt_10_flag_d1},
    "f15_vesp_089_mcap_gt_20x_fcf_flag_d1": {"inputs": ["marketcap", "fcf"], "func": f15_vesp_089_mcap_gt_20x_fcf_flag_d1},
    "f15_vesp_090_evebit_gt_40_flag_d1": {"inputs": ["evebit"], "func": f15_vesp_090_evebit_gt_40_flag_d1},
    "f15_vesp_091_bubble_count_total_d1": {"inputs": ["pe", "ps", "pb", "evebitda", "evsales"], "func": f15_vesp_091_bubble_count_total_d1},
    "f15_vesp_092_bvps_growth_minus_price_growth_252d_d1": {"inputs": ["equity", "shareswa", "marketcap"], "func": f15_vesp_092_bvps_growth_minus_price_growth_252d_d1},
    "f15_vesp_093_eps_yield_d1": {"inputs": ["eps", "marketcap", "shareswa"], "func": f15_vesp_093_eps_yield_d1},
    "f15_vesp_094_eps_growth_minus_price_growth_252d_d1": {"inputs": ["eps", "marketcap", "shareswa"], "func": f15_vesp_094_eps_growth_minus_price_growth_252d_d1},
    "f15_vesp_095_bvps_minus_eps_growth_252d_d1": {"inputs": ["equity", "shareswa", "eps"], "func": f15_vesp_095_bvps_minus_eps_growth_252d_d1},
    "f15_vesp_096_eps_to_epsdil_gap_d1": {"inputs": ["eps", "epsdil"], "func": f15_vesp_096_eps_to_epsdil_gap_d1},
    "f15_vesp_097_pps_growth_252d_d1": {"inputs": ["marketcap", "shareswa"], "func": f15_vesp_097_pps_growth_252d_d1},
    "f15_vesp_098_bvps_level_d1": {"inputs": ["equity", "shareswa"], "func": f15_vesp_098_bvps_level_d1},
    "f15_vesp_099_eps_yield_dilution_adjusted_d1": {"inputs": ["epsdil", "marketcap", "shareswadil"], "func": f15_vesp_099_eps_yield_dilution_adjusted_d1},
    "f15_vesp_100_mcap_to_cashneq_d1": {"inputs": ["marketcap", "cashneq"], "func": f15_vesp_100_mcap_to_cashneq_d1},
    "f15_vesp_101_mcap_to_assets_d1": {"inputs": ["marketcap", "assets"], "func": f15_vesp_101_mcap_to_assets_d1},
    "f15_vesp_102_mcap_to_equity_d1": {"inputs": ["marketcap", "equity"], "func": f15_vesp_102_mcap_to_equity_d1},
    "f15_vesp_103_mcap_to_tangible_book_d1": {"inputs": ["marketcap", "tangibles"], "func": f15_vesp_103_mcap_to_tangible_book_d1},
    "f15_vesp_104_mcap_minus_cash_to_equity_d1": {"inputs": ["marketcap", "cashneq", "equity"], "func": f15_vesp_104_mcap_minus_cash_to_equity_d1},
    "f15_vesp_105_mcap_to_debt_d1": {"inputs": ["marketcap", "debt"], "func": f15_vesp_105_mcap_to_debt_d1},
    "f15_vesp_106_mcap_to_retained_earnings_d1": {"inputs": ["marketcap", "retearn"], "func": f15_vesp_106_mcap_to_retained_earnings_d1},
    "f15_vesp_107_mcap_to_capex_d1": {"inputs": ["marketcap", "capex"], "func": f15_vesp_107_mcap_to_capex_d1},
    "f15_vesp_108_mcap_to_sbcomp_d1": {"inputs": ["marketcap", "sbcomp"], "func": f15_vesp_108_mcap_to_sbcomp_d1},
    "f15_vesp_109_mcap_to_gp_d1": {"inputs": ["marketcap", "gp"], "func": f15_vesp_109_mcap_to_gp_d1},
    "f15_vesp_110_dilution_adjusted_pe_d1": {"inputs": ["pe", "shareswadil", "shareswa"], "func": f15_vesp_110_dilution_adjusted_pe_d1},
    "f15_vesp_111_dilution_adjusted_ps_d1": {"inputs": ["ps", "shareswadil", "shareswa"], "func": f15_vesp_111_dilution_adjusted_ps_d1},
    "f15_vesp_112_dilution_adjusted_pb_d1": {"inputs": ["pb", "shareswadil", "shareswa"], "func": f15_vesp_112_dilution_adjusted_pb_d1},
    "f15_vesp_113_dilution_adjusted_evsales_d1": {"inputs": ["evsales", "shareswadil", "shareswa"], "func": f15_vesp_113_dilution_adjusted_evsales_d1},
    "f15_vesp_114_dilution_factor_level_d1": {"inputs": ["shareswadil", "shareswa"], "func": f15_vesp_114_dilution_factor_level_d1},
    "f15_vesp_115_dilution_overhang_minus_one_d1": {"inputs": ["shareswadil", "shareswa"], "func": f15_vesp_115_dilution_overhang_minus_one_d1},
    "f15_vesp_116_pe_frac_above_p80_252d_d1": {"inputs": ["pe"], "func": f15_vesp_116_pe_frac_above_p80_252d_d1},
    "f15_vesp_117_ps_frac_above_p80_252d_d1": {"inputs": ["ps"], "func": f15_vesp_117_ps_frac_above_p80_252d_d1},
    "f15_vesp_118_pb_frac_above_p80_252d_d1": {"inputs": ["pb"], "func": f15_vesp_118_pb_frac_above_p80_252d_d1},
    "f15_vesp_119_evebitda_frac_above_p80_252d_d1": {"inputs": ["evebitda"], "func": f15_vesp_119_evebitda_frac_above_p80_252d_d1},
    "f15_vesp_120_pe_frac_above_p80_1260d_d1": {"inputs": ["pe"], "func": f15_vesp_120_pe_frac_above_p80_1260d_d1},
    "f15_vesp_121_ps_frac_above_p80_1260d_d1": {"inputs": ["ps"], "func": f15_vesp_121_ps_frac_above_p80_1260d_d1},
    "f15_vesp_122_evsales_frac_above_p80_1260d_d1": {"inputs": ["evsales"], "func": f15_vesp_122_evsales_frac_above_p80_1260d_d1},
    "f15_vesp_123_composite_persistence_above_p80_d1": {"inputs": ["pe", "ps", "evebitda"], "func": f15_vesp_123_composite_persistence_above_p80_d1},
    "f15_vesp_124_pe_change_minus_earnings_change_252d_d1": {"inputs": ["pe", "netinc"], "func": f15_vesp_124_pe_change_minus_earnings_change_252d_d1},
    "f15_vesp_125_ps_change_minus_revenue_change_252d_d1": {"inputs": ["ps", "revenue"], "func": f15_vesp_125_ps_change_minus_revenue_change_252d_d1},
    "f15_vesp_126_evebitda_change_minus_ebitda_change_252d_d1": {"inputs": ["evebitda", "ebitda"], "func": f15_vesp_126_evebitda_change_minus_ebitda_change_252d_d1},
    "f15_vesp_127_pb_change_minus_equity_change_252d_d1": {"inputs": ["pb", "equity"], "func": f15_vesp_127_pb_change_minus_equity_change_252d_d1},
    "f15_vesp_128_evsales_change_minus_revenue_change_252d_d1": {"inputs": ["evsales", "revenue"], "func": f15_vesp_128_evsales_change_minus_revenue_change_252d_d1},
    "f15_vesp_129_mcap_change_minus_book_change_252d_d1": {"inputs": ["marketcap", "equity"], "func": f15_vesp_129_mcap_change_minus_book_change_252d_d1},
    "f15_vesp_130_mcap_change_minus_fcf_change_252d_d1": {"inputs": ["marketcap", "fcf"], "func": f15_vesp_130_mcap_change_minus_fcf_change_252d_d1},
    "f15_vesp_131_mcap_change_minus_revenue_change_504d_d1": {"inputs": ["marketcap", "revenue"], "func": f15_vesp_131_mcap_change_minus_revenue_change_504d_d1},
    "f15_vesp_132_ps_over_gm_times_rev_growth_d1": {"inputs": ["ps", "gp", "revenue"], "func": f15_vesp_132_ps_over_gm_times_rev_growth_d1},
    "f15_vesp_133_evsales_over_gm_times_rev_growth_d1": {"inputs": ["evsales", "gp", "revenue"], "func": f15_vesp_133_evsales_over_gm_times_rev_growth_d1},
    "f15_vesp_134_pe_over_eps_growth_times_roa_d1": {"inputs": ["pe", "eps", "netinc", "assets"], "func": f15_vesp_134_pe_over_eps_growth_times_roa_d1},
    "f15_vesp_135_evebitda_over_ebitda_margin_d1": {"inputs": ["evebitda", "ebitda", "revenue"], "func": f15_vesp_135_evebitda_over_ebitda_margin_d1},
    "f15_vesp_136_pb_over_roe_d1": {"inputs": ["pb", "netinc", "equity"], "func": f15_vesp_136_pb_over_roe_d1},
    "f15_vesp_137_ps_over_ebitda_margin_d1": {"inputs": ["ps", "ebitda", "revenue"], "func": f15_vesp_137_ps_over_ebitda_margin_d1},
    "f15_vesp_138_pe_distance_to_p50_252d_d1": {"inputs": ["pe"], "func": f15_vesp_138_pe_distance_to_p50_252d_d1},
    "f15_vesp_139_pe_distance_to_p90_1260d_d1": {"inputs": ["pe"], "func": f15_vesp_139_pe_distance_to_p90_1260d_d1},
    "f15_vesp_140_pe_distance_to_p99_1260d_d1": {"inputs": ["pe"], "func": f15_vesp_140_pe_distance_to_p99_1260d_d1},
    "f15_vesp_141_ps_distance_to_p50_252d_d1": {"inputs": ["ps"], "func": f15_vesp_141_ps_distance_to_p50_252d_d1},
    "f15_vesp_142_ps_distance_to_p90_1260d_d1": {"inputs": ["ps"], "func": f15_vesp_142_ps_distance_to_p90_1260d_d1},
    "f15_vesp_143_evebitda_distance_to_p90_1260d_d1": {"inputs": ["evebitda"], "func": f15_vesp_143_evebitda_distance_to_p90_1260d_d1},
    "f15_vesp_144_pb_distance_to_p90_1260d_d1": {"inputs": ["pb"], "func": f15_vesp_144_pb_distance_to_p90_1260d_d1},
    "f15_vesp_145_evsales_distance_to_p99_1260d_d1": {"inputs": ["evsales"], "func": f15_vesp_145_evsales_distance_to_p99_1260d_d1},
    "f15_vesp_146_ev_to_revenue_plus_ebitda_d1": {"inputs": ["ev", "revenue", "ebitda"], "func": f15_vesp_146_ev_to_revenue_plus_ebitda_d1},
    "f15_vesp_147_log_mcap_to_cash_minus_debt_d1": {"inputs": ["marketcap", "cashneq", "debt"], "func": f15_vesp_147_log_mcap_to_cash_minus_debt_d1},
    "f15_vesp_148_extreme_breadth_252d_d1": {"inputs": ["pe", "ps", "pb", "evebitda", "evsales"], "func": f15_vesp_148_extreme_breadth_252d_d1},
    "f15_vesp_149_valuation_to_quality_index_d1": {"inputs": ["ps", "pb", "netinc", "equity", "ebitda", "revenue"], "func": f15_vesp_149_valuation_to_quality_index_d1},
    "f15_vesp_150_log_extreme_intensity_d1": {"inputs": ["pe", "ps", "evsales", "evebitda"], "func": f15_vesp_150_log_extreme_intensity_d1},
}
