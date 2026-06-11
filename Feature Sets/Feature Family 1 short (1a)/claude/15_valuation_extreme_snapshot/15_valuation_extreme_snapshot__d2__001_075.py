"""valuation_extreme_snapshot d2 features — second-derivative wrappers (acceleration)."""
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
#                    D2 FEATURES
# ============================================================

def f15_vesp_001_pe_level_raw_d2(pe: pd.Series):
    return (pe.astype(float)).diff().diff()


def f15_vesp_002_log_pe_level_d2(pe: pd.Series):
    return (_safe_log(pe)).diff().diff()


def f15_vesp_003_ps_level_raw_d2(ps: pd.Series):
    return (ps.astype(float)).diff().diff()


def f15_vesp_004_log_ps_level_d2(ps: pd.Series):
    return (_safe_log(ps)).diff().diff()


def f15_vesp_005_pb_level_raw_d2(pb: pd.Series):
    return (pb.astype(float)).diff().diff()


def f15_vesp_006_log_pb_level_d2(pb: pd.Series):
    return (_safe_log(pb)).diff().diff()


def f15_vesp_007_evebitda_level_d2(evebitda: pd.Series):
    return (evebitda.astype(float)).diff().diff()


def f15_vesp_008_log_evebitda_level_d2(evebitda: pd.Series):
    return (_safe_log(evebitda)).diff().diff()


def f15_vesp_009_evebit_level_d2(evebit: pd.Series):
    return (evebit.astype(float)).diff().diff()


def f15_vesp_010_evsales_level_d2(evsales: pd.Series):
    return (evsales.astype(float)).diff().diff()


def f15_vesp_011_ev_to_fcf_d2(ev: pd.Series, fcf: pd.Series):
    return (_safe_div(ev, fcf)).diff().diff()


def f15_vesp_012_ev_to_cfo_d2(ev: pd.Series, ncfo: pd.Series):
    return (_safe_div(ev, ncfo)).diff().diff()


def f15_vesp_013_mcap_to_tangibles_d2(marketcap: pd.Series, tangibles: pd.Series):
    return (_safe_div(marketcap, tangibles)).diff().diff()


def f15_vesp_014_mcap_to_retearn_d2(marketcap: pd.Series, retearn: pd.Series):
    return (_safe_div(marketcap, retearn)).diff().diff()


def f15_vesp_015_fcfp_inverse_d2(fcfp: pd.Series):
    return (_safe_div(1.0, fcfp)).diff().diff()


def f15_vesp_016_earnings_yield_d2(pe: pd.Series):
    return (_safe_div(1.0, pe)).diff().diff()


def f15_vesp_017_fcf_yield_level_d2(fcfp: pd.Series):
    return (fcfp.astype(float)).diff().diff()


def f15_vesp_018_cfo_yield_d2(ncfo: pd.Series, marketcap: pd.Series):
    return (_safe_div(ncfo, marketcap)).diff().diff()


def f15_vesp_019_sales_yield_d2(revenue: pd.Series, marketcap: pd.Series):
    return (_safe_div(revenue, marketcap)).diff().diff()


def f15_vesp_020_ebitda_yield_d2(ebitda: pd.Series, ev: pd.Series):
    return (_safe_div(ebitda, ev)).diff().diff()


def f15_vesp_021_ebit_yield_d2(ebit: pd.Series, ev: pd.Series):
    return (_safe_div(ebit, ev)).diff().diff()


def f15_vesp_022_book_yield_d2(equity: pd.Series, marketcap: pd.Series):
    return (_safe_div(equity, marketcap)).diff().diff()


def f15_vesp_023_dividend_yield_level_d2(divyield: pd.Series):
    return (divyield.astype(float)).diff().diff()


def f15_vesp_024_pe_to_revenue_growth_d2(pe: pd.Series, revenue: pd.Series):
    rev_growth = revenue.pct_change(YDAYS)
    return (_safe_div(pe, rev_growth)).diff().diff()


def f15_vesp_025_ps_to_revenue_growth_d2(ps: pd.Series, revenue: pd.Series):
    rev_growth = revenue.pct_change(YDAYS)
    return (_safe_div(ps, rev_growth)).diff().diff()


def f15_vesp_026_evebitda_to_ebitda_growth_d2(evebitda: pd.Series, ebitda: pd.Series):
    eg = ebitda.pct_change(YDAYS)
    return (_safe_div(evebitda, eg)).diff().diff()


def f15_vesp_027_evsales_to_revenue_growth_d2(evsales: pd.Series, revenue: pd.Series):
    rev_growth = revenue.pct_change(YDAYS)
    return (_safe_div(evsales, rev_growth)).diff().diff()


def f15_vesp_028_pe_to_earnings_growth_d2(pe: pd.Series, netinc: pd.Series):
    ng = netinc.pct_change(YDAYS)
    return (_safe_div(pe, ng)).diff().diff()


def f15_vesp_029_pb_to_equity_growth_d2(pb: pd.Series, equity: pd.Series):
    eg = equity.pct_change(YDAYS)
    return (_safe_div(pb, eg)).diff().diff()


def f15_vesp_030_ps_to_revenue_growth_63d_d2(ps: pd.Series, revenue: pd.Series):
    rev_growth = revenue.pct_change(QDAYS)
    return (_safe_div(ps, rev_growth)).diff().diff()


def f15_vesp_031_pe_to_eps_growth_d2(pe: pd.Series, eps: pd.Series):
    eg = eps.pct_change(YDAYS)
    return (_safe_div(pe, eg)).diff().diff()


def f15_vesp_032_evebit_to_ebit_growth_d2(evebit: pd.Series, ebit: pd.Series):
    g = ebit.pct_change(YDAYS)
    return (_safe_div(evebit, g)).diff().diff()


def f15_vesp_033_ev_to_fcf_growth_d2(ev: pd.Series, fcf: pd.Series):
    g = fcf.pct_change(YDAYS)
    fg_eff = ev / fcf.replace(0, np.nan)
    return (_safe_div(fg_eff, g)).diff().diff()


def f15_vesp_034_pe_zscore_252d_d2(pe: pd.Series):
    return (_rolling_zscore(pe, YDAYS)).diff().diff()


def f15_vesp_035_pe_zscore_504d_d2(pe: pd.Series):
    return (_rolling_zscore(pe, 504)).diff().diff()


def f15_vesp_036_pe_zscore_1260d_d2(pe: pd.Series):
    return (_rolling_zscore(pe, 1260)).diff().diff()


def f15_vesp_037_ps_zscore_252d_d2(ps: pd.Series):
    return (_rolling_zscore(ps, YDAYS)).diff().diff()


def f15_vesp_038_ps_zscore_504d_d2(ps: pd.Series):
    return (_rolling_zscore(ps, 504)).diff().diff()


def f15_vesp_039_ps_zscore_1260d_d2(ps: pd.Series):
    return (_rolling_zscore(ps, 1260)).diff().diff()


def f15_vesp_040_evebitda_zscore_252d_d2(evebitda: pd.Series):
    return (_rolling_zscore(evebitda, YDAYS)).diff().diff()


def f15_vesp_041_evebitda_zscore_504d_d2(evebitda: pd.Series):
    return (_rolling_zscore(evebitda, 504)).diff().diff()


def f15_vesp_042_evebitda_zscore_1260d_d2(evebitda: pd.Series):
    return (_rolling_zscore(evebitda, 1260)).diff().diff()


def f15_vesp_043_pb_zscore_252d_d2(pb: pd.Series):
    return (_rolling_zscore(pb, YDAYS)).diff().diff()


def f15_vesp_044_pb_zscore_1260d_d2(pb: pd.Series):
    return (_rolling_zscore(pb, 1260)).diff().diff()


def f15_vesp_045_evsales_zscore_504d_d2(evsales: pd.Series):
    return (_rolling_zscore(evsales, 504)).diff().diff()


def f15_vesp_046_pe_over_252d_mean_d2(pe: pd.Series):
    m = pe.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(pe, m)).diff().diff()


def f15_vesp_047_pe_over_252d_median_d2(pe: pd.Series):
    m = pe.rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(pe, m)).diff().diff()


def f15_vesp_048_pe_over_1260d_max_d2(pe: pd.Series):
    m = pe.rolling(1260, min_periods=YDAYS).max()
    return (_safe_div(pe, m)).diff().diff()


def f15_vesp_049_pe_over_252d_p90_d2(pe: pd.Series):
    q = pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    return (_safe_div(pe, q)).diff().diff()


def f15_vesp_050_ps_over_252d_mean_d2(ps: pd.Series):
    m = ps.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(ps, m)).diff().diff()


def f15_vesp_051_ps_over_1260d_max_d2(ps: pd.Series):
    m = ps.rolling(1260, min_periods=YDAYS).max()
    return (_safe_div(ps, m)).diff().diff()


def f15_vesp_052_evebitda_over_504d_mean_d2(evebitda: pd.Series):
    m = evebitda.rolling(504, min_periods=YDAYS).mean()
    return (_safe_div(evebitda, m)).diff().diff()


def f15_vesp_053_evebitda_over_1260d_p90_d2(evebitda: pd.Series):
    q = evebitda.rolling(1260, min_periods=YDAYS).quantile(0.9)
    return (_safe_div(evebitda, q)).diff().diff()


def f15_vesp_054_pb_over_1260d_median_d2(pb: pd.Series):
    m = pb.rolling(1260, min_periods=YDAYS).median()
    return (_safe_div(pb, m)).diff().diff()


def f15_vesp_055_evsales_over_1260d_max_d2(evsales: pd.Series):
    m = evsales.rolling(1260, min_periods=YDAYS).max()
    return (_safe_div(evsales, m)).diff().diff()


def f15_vesp_056_ev_to_invested_capital_d2(ev: pd.Series, equity: pd.Series, debt: pd.Series):
    ic = equity.fillna(0) + debt.fillna(0)
    return (_safe_div(ev, ic)).diff().diff()


def f15_vesp_057_ev_to_equity_plus_debtnc_d2(ev: pd.Series, equity: pd.Series, debtnc: pd.Series):
    ic = equity.fillna(0) + debtnc.fillna(0)
    return (_safe_div(ev, ic)).diff().diff()


def f15_vesp_058_ev_to_tangible_ic_d2(ev: pd.Series, tangibles: pd.Series, debt: pd.Series):
    ic = tangibles.fillna(0) + debt.fillna(0)
    return (_safe_div(ev, ic)).diff().diff()


def f15_vesp_059_ev_to_assets_d2(ev: pd.Series, assets: pd.Series):
    return (_safe_div(ev, assets)).diff().diff()


def f15_vesp_060_ev_to_equity_only_d2(ev: pd.Series, equity: pd.Series):
    return (_safe_div(ev, equity)).diff().diff()


def f15_vesp_061_ev_to_tangibles_only_d2(ev: pd.Series, tangibles: pd.Series):
    return (_safe_div(ev, tangibles)).diff().diff()


def f15_vesp_062_ev_minus_cash_to_ic_d2(ev: pd.Series, cashneq: pd.Series, equity: pd.Series, debt: pd.Series):
    ic = equity.fillna(0) + debt.fillna(0)
    return (_safe_div(ev - cashneq.fillna(0), ic)).diff().diff()


def f15_vesp_063_ev_to_equity_plus_debtc_d2(ev: pd.Series, equity: pd.Series, debtc: pd.Series):
    ic = equity.fillna(0) + debtc.fillna(0)
    return (_safe_div(ev, ic)).diff().diff()


def f15_vesp_064_loss_making_bubble_flag_d2(pe: pd.Series, netinc: pd.Series):
    flag = ((netinc < 0) & (pe > 0)).astype(float)
    return (flag.where(~(pe.isna() | netinc.isna()), np.nan)).diff().diff()


def f15_vesp_065_negative_fcf_high_evsales_flag_d2(fcf: pd.Series, evsales: pd.Series):
    flag = ((fcf < 0) & (evsales > 5)).astype(float)
    return (flag.where(~(fcf.isna() | evsales.isna()), np.nan)).diff().diff()


def f15_vesp_066_negative_ebitda_high_mcap_flag_d2(ebitda: pd.Series, marketcap: pd.Series):
    flag = ((ebitda < 0) & (marketcap > 500000000.0)).astype(float)
    return (flag.where(~(ebitda.isna() | marketcap.isna()), np.nan)).diff().diff()


def f15_vesp_067_negative_retearn_with_premium_flag_d2(retearn: pd.Series, marketcap: pd.Series, equity: pd.Series):
    pb_eff = _safe_div(marketcap, equity)
    flag = ((retearn < 0) & (pb_eff > 3)).astype(float)
    return (flag.where(~(retearn.isna() | pb_eff.isna()), np.nan)).diff().diff()


def f15_vesp_068_negative_netinc_persistent_count_4q_d2(netinc: pd.Series):
    return ((netinc < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()


def f15_vesp_069_negative_fcf_persistent_count_4q_d2(fcf: pd.Series):
    return ((fcf < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()


def f15_vesp_070_intangible_dominance_flag_d2(intangibles: pd.Series, assets: pd.Series):
    share = _safe_div(intangibles, assets)
    flag = (share > 0.5).astype(float)
    return (flag.where(~share.isna(), np.nan)).diff().diff()


def f15_vesp_071_debt_exceeds_equity_flag_d2(debt: pd.Series, equity: pd.Series):
    flag = (debt > equity).astype(float)
    return (flag.where(~(debt.isna() | equity.isna()), np.nan)).diff().diff()


def f15_vesp_072_composite_z_pe_ps_pb_evebitda_252d_d2(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series):
    z = (_rolling_zscore(pe, YDAYS) + _rolling_zscore(ps, YDAYS) + _rolling_zscore(pb, YDAYS) + _rolling_zscore(evebitda, YDAYS)) / 4.0
    return (z).diff().diff()


def f15_vesp_073_composite_z_pe_ps_pb_evebitda_1260d_d2(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series):
    z = (_rolling_zscore(pe, 1260) + _rolling_zscore(ps, 1260) + _rolling_zscore(pb, 1260) + _rolling_zscore(evebitda, 1260)) / 4.0
    return (z).diff().diff()


def f15_vesp_074_composite_z_ev_multiples_504d_d2(evebitda: pd.Series, evebit: pd.Series, evsales: pd.Series):
    z = (_rolling_zscore(evebitda, 504) + _rolling_zscore(evebit, 504) + _rolling_zscore(evsales, 504)) / 3.0
    return (z).diff().diff()


def f15_vesp_075_composite_z_equity_multiples_252d_d2(pe: pd.Series, ps: pd.Series, pb: pd.Series):
    z = (_rolling_zscore(pe, YDAYS) + _rolling_zscore(ps, YDAYS) + _rolling_zscore(pb, YDAYS)) / 3.0
    return (z).diff().diff()



# ============================================================
#                        REGISTRY
# ============================================================

VALUATION_EXTREME_SNAPSHOT_D2_REGISTRY_001_075 = {
    "f15_vesp_001_pe_level_raw_d2": {"inputs": ["pe"], "func": f15_vesp_001_pe_level_raw_d2},
    "f15_vesp_002_log_pe_level_d2": {"inputs": ["pe"], "func": f15_vesp_002_log_pe_level_d2},
    "f15_vesp_003_ps_level_raw_d2": {"inputs": ["ps"], "func": f15_vesp_003_ps_level_raw_d2},
    "f15_vesp_004_log_ps_level_d2": {"inputs": ["ps"], "func": f15_vesp_004_log_ps_level_d2},
    "f15_vesp_005_pb_level_raw_d2": {"inputs": ["pb"], "func": f15_vesp_005_pb_level_raw_d2},
    "f15_vesp_006_log_pb_level_d2": {"inputs": ["pb"], "func": f15_vesp_006_log_pb_level_d2},
    "f15_vesp_007_evebitda_level_d2": {"inputs": ["evebitda"], "func": f15_vesp_007_evebitda_level_d2},
    "f15_vesp_008_log_evebitda_level_d2": {"inputs": ["evebitda"], "func": f15_vesp_008_log_evebitda_level_d2},
    "f15_vesp_009_evebit_level_d2": {"inputs": ["evebit"], "func": f15_vesp_009_evebit_level_d2},
    "f15_vesp_010_evsales_level_d2": {"inputs": ["evsales"], "func": f15_vesp_010_evsales_level_d2},
    "f15_vesp_011_ev_to_fcf_d2": {"inputs": ["ev", "fcf"], "func": f15_vesp_011_ev_to_fcf_d2},
    "f15_vesp_012_ev_to_cfo_d2": {"inputs": ["ev", "ncfo"], "func": f15_vesp_012_ev_to_cfo_d2},
    "f15_vesp_013_mcap_to_tangibles_d2": {"inputs": ["marketcap", "tangibles"], "func": f15_vesp_013_mcap_to_tangibles_d2},
    "f15_vesp_014_mcap_to_retearn_d2": {"inputs": ["marketcap", "retearn"], "func": f15_vesp_014_mcap_to_retearn_d2},
    "f15_vesp_015_fcfp_inverse_d2": {"inputs": ["fcfp"], "func": f15_vesp_015_fcfp_inverse_d2},
    "f15_vesp_016_earnings_yield_d2": {"inputs": ["pe"], "func": f15_vesp_016_earnings_yield_d2},
    "f15_vesp_017_fcf_yield_level_d2": {"inputs": ["fcfp"], "func": f15_vesp_017_fcf_yield_level_d2},
    "f15_vesp_018_cfo_yield_d2": {"inputs": ["ncfo", "marketcap"], "func": f15_vesp_018_cfo_yield_d2},
    "f15_vesp_019_sales_yield_d2": {"inputs": ["revenue", "marketcap"], "func": f15_vesp_019_sales_yield_d2},
    "f15_vesp_020_ebitda_yield_d2": {"inputs": ["ebitda", "ev"], "func": f15_vesp_020_ebitda_yield_d2},
    "f15_vesp_021_ebit_yield_d2": {"inputs": ["ebit", "ev"], "func": f15_vesp_021_ebit_yield_d2},
    "f15_vesp_022_book_yield_d2": {"inputs": ["equity", "marketcap"], "func": f15_vesp_022_book_yield_d2},
    "f15_vesp_023_dividend_yield_level_d2": {"inputs": ["divyield"], "func": f15_vesp_023_dividend_yield_level_d2},
    "f15_vesp_024_pe_to_revenue_growth_d2": {"inputs": ["pe", "revenue"], "func": f15_vesp_024_pe_to_revenue_growth_d2},
    "f15_vesp_025_ps_to_revenue_growth_d2": {"inputs": ["ps", "revenue"], "func": f15_vesp_025_ps_to_revenue_growth_d2},
    "f15_vesp_026_evebitda_to_ebitda_growth_d2": {"inputs": ["evebitda", "ebitda"], "func": f15_vesp_026_evebitda_to_ebitda_growth_d2},
    "f15_vesp_027_evsales_to_revenue_growth_d2": {"inputs": ["evsales", "revenue"], "func": f15_vesp_027_evsales_to_revenue_growth_d2},
    "f15_vesp_028_pe_to_earnings_growth_d2": {"inputs": ["pe", "netinc"], "func": f15_vesp_028_pe_to_earnings_growth_d2},
    "f15_vesp_029_pb_to_equity_growth_d2": {"inputs": ["pb", "equity"], "func": f15_vesp_029_pb_to_equity_growth_d2},
    "f15_vesp_030_ps_to_revenue_growth_63d_d2": {"inputs": ["ps", "revenue"], "func": f15_vesp_030_ps_to_revenue_growth_63d_d2},
    "f15_vesp_031_pe_to_eps_growth_d2": {"inputs": ["pe", "eps"], "func": f15_vesp_031_pe_to_eps_growth_d2},
    "f15_vesp_032_evebit_to_ebit_growth_d2": {"inputs": ["evebit", "ebit"], "func": f15_vesp_032_evebit_to_ebit_growth_d2},
    "f15_vesp_033_ev_to_fcf_growth_d2": {"inputs": ["ev", "fcf"], "func": f15_vesp_033_ev_to_fcf_growth_d2},
    "f15_vesp_034_pe_zscore_252d_d2": {"inputs": ["pe"], "func": f15_vesp_034_pe_zscore_252d_d2},
    "f15_vesp_035_pe_zscore_504d_d2": {"inputs": ["pe"], "func": f15_vesp_035_pe_zscore_504d_d2},
    "f15_vesp_036_pe_zscore_1260d_d2": {"inputs": ["pe"], "func": f15_vesp_036_pe_zscore_1260d_d2},
    "f15_vesp_037_ps_zscore_252d_d2": {"inputs": ["ps"], "func": f15_vesp_037_ps_zscore_252d_d2},
    "f15_vesp_038_ps_zscore_504d_d2": {"inputs": ["ps"], "func": f15_vesp_038_ps_zscore_504d_d2},
    "f15_vesp_039_ps_zscore_1260d_d2": {"inputs": ["ps"], "func": f15_vesp_039_ps_zscore_1260d_d2},
    "f15_vesp_040_evebitda_zscore_252d_d2": {"inputs": ["evebitda"], "func": f15_vesp_040_evebitda_zscore_252d_d2},
    "f15_vesp_041_evebitda_zscore_504d_d2": {"inputs": ["evebitda"], "func": f15_vesp_041_evebitda_zscore_504d_d2},
    "f15_vesp_042_evebitda_zscore_1260d_d2": {"inputs": ["evebitda"], "func": f15_vesp_042_evebitda_zscore_1260d_d2},
    "f15_vesp_043_pb_zscore_252d_d2": {"inputs": ["pb"], "func": f15_vesp_043_pb_zscore_252d_d2},
    "f15_vesp_044_pb_zscore_1260d_d2": {"inputs": ["pb"], "func": f15_vesp_044_pb_zscore_1260d_d2},
    "f15_vesp_045_evsales_zscore_504d_d2": {"inputs": ["evsales"], "func": f15_vesp_045_evsales_zscore_504d_d2},
    "f15_vesp_046_pe_over_252d_mean_d2": {"inputs": ["pe"], "func": f15_vesp_046_pe_over_252d_mean_d2},
    "f15_vesp_047_pe_over_252d_median_d2": {"inputs": ["pe"], "func": f15_vesp_047_pe_over_252d_median_d2},
    "f15_vesp_048_pe_over_1260d_max_d2": {"inputs": ["pe"], "func": f15_vesp_048_pe_over_1260d_max_d2},
    "f15_vesp_049_pe_over_252d_p90_d2": {"inputs": ["pe"], "func": f15_vesp_049_pe_over_252d_p90_d2},
    "f15_vesp_050_ps_over_252d_mean_d2": {"inputs": ["ps"], "func": f15_vesp_050_ps_over_252d_mean_d2},
    "f15_vesp_051_ps_over_1260d_max_d2": {"inputs": ["ps"], "func": f15_vesp_051_ps_over_1260d_max_d2},
    "f15_vesp_052_evebitda_over_504d_mean_d2": {"inputs": ["evebitda"], "func": f15_vesp_052_evebitda_over_504d_mean_d2},
    "f15_vesp_053_evebitda_over_1260d_p90_d2": {"inputs": ["evebitda"], "func": f15_vesp_053_evebitda_over_1260d_p90_d2},
    "f15_vesp_054_pb_over_1260d_median_d2": {"inputs": ["pb"], "func": f15_vesp_054_pb_over_1260d_median_d2},
    "f15_vesp_055_evsales_over_1260d_max_d2": {"inputs": ["evsales"], "func": f15_vesp_055_evsales_over_1260d_max_d2},
    "f15_vesp_056_ev_to_invested_capital_d2": {"inputs": ["ev", "equity", "debt"], "func": f15_vesp_056_ev_to_invested_capital_d2},
    "f15_vesp_057_ev_to_equity_plus_debtnc_d2": {"inputs": ["ev", "equity", "debtnc"], "func": f15_vesp_057_ev_to_equity_plus_debtnc_d2},
    "f15_vesp_058_ev_to_tangible_ic_d2": {"inputs": ["ev", "tangibles", "debt"], "func": f15_vesp_058_ev_to_tangible_ic_d2},
    "f15_vesp_059_ev_to_assets_d2": {"inputs": ["ev", "assets"], "func": f15_vesp_059_ev_to_assets_d2},
    "f15_vesp_060_ev_to_equity_only_d2": {"inputs": ["ev", "equity"], "func": f15_vesp_060_ev_to_equity_only_d2},
    "f15_vesp_061_ev_to_tangibles_only_d2": {"inputs": ["ev", "tangibles"], "func": f15_vesp_061_ev_to_tangibles_only_d2},
    "f15_vesp_062_ev_minus_cash_to_ic_d2": {"inputs": ["ev", "cashneq", "equity", "debt"], "func": f15_vesp_062_ev_minus_cash_to_ic_d2},
    "f15_vesp_063_ev_to_equity_plus_debtc_d2": {"inputs": ["ev", "equity", "debtc"], "func": f15_vesp_063_ev_to_equity_plus_debtc_d2},
    "f15_vesp_064_loss_making_bubble_flag_d2": {"inputs": ["pe", "netinc"], "func": f15_vesp_064_loss_making_bubble_flag_d2},
    "f15_vesp_065_negative_fcf_high_evsales_flag_d2": {"inputs": ["fcf", "evsales"], "func": f15_vesp_065_negative_fcf_high_evsales_flag_d2},
    "f15_vesp_066_negative_ebitda_high_mcap_flag_d2": {"inputs": ["ebitda", "marketcap"], "func": f15_vesp_066_negative_ebitda_high_mcap_flag_d2},
    "f15_vesp_067_negative_retearn_with_premium_flag_d2": {"inputs": ["retearn", "marketcap", "equity"], "func": f15_vesp_067_negative_retearn_with_premium_flag_d2},
    "f15_vesp_068_negative_netinc_persistent_count_4q_d2": {"inputs": ["netinc"], "func": f15_vesp_068_negative_netinc_persistent_count_4q_d2},
    "f15_vesp_069_negative_fcf_persistent_count_4q_d2": {"inputs": ["fcf"], "func": f15_vesp_069_negative_fcf_persistent_count_4q_d2},
    "f15_vesp_070_intangible_dominance_flag_d2": {"inputs": ["intangibles", "assets"], "func": f15_vesp_070_intangible_dominance_flag_d2},
    "f15_vesp_071_debt_exceeds_equity_flag_d2": {"inputs": ["debt", "equity"], "func": f15_vesp_071_debt_exceeds_equity_flag_d2},
    "f15_vesp_072_composite_z_pe_ps_pb_evebitda_252d_d2": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_072_composite_z_pe_ps_pb_evebitda_252d_d2},
    "f15_vesp_073_composite_z_pe_ps_pb_evebitda_1260d_d2": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_073_composite_z_pe_ps_pb_evebitda_1260d_d2},
    "f15_vesp_074_composite_z_ev_multiples_504d_d2": {"inputs": ["evebitda", "evebit", "evsales"], "func": f15_vesp_074_composite_z_ev_multiples_504d_d2},
    "f15_vesp_075_composite_z_equity_multiples_252d_d2": {"inputs": ["pe", "ps", "pb"], "func": f15_vesp_075_composite_z_equity_multiples_252d_d2},
}
