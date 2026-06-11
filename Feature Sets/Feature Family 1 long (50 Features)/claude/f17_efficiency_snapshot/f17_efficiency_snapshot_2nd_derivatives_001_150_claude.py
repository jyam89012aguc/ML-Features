import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f17_efficiency_ratio(numerator, denominator, w):
    n = _mean(numerator, w)
    d = _mean(denominator, w)
    return n / d.replace(0, np.nan).abs()


def _f17_turnover_rate(flow, stock, w):
    f = _mean(flow, w)
    s = _mean(stock, w)
    return f / s.replace(0, np.nan).abs()


# 5d slope of 21d AT
def f17es_f17_efficiency_snapshot_at_21d_slope_v001_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21) * marketcap
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d AT
def f17es_f17_efficiency_snapshot_at_21d_slope_v002_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d AT
def f17es_f17_efficiency_snapshot_at_63d_slope_v003_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 63) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d AT
def f17es_f17_efficiency_snapshot_at_63d_slope_v004_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 63) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d AT
def f17es_f17_efficiency_snapshot_at_126d_slope_v005_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 126) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d AT
def f17es_f17_efficiency_snapshot_at_252d_slope_v006_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d AT
def f17es_f17_efficiency_snapshot_at_504d_slope_v007_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d EQT
def f17es_f17_efficiency_snapshot_eqt_21d_slope_v008_signal(revenue, equity, marketcap):
    base = _f17_turnover_rate(revenue, equity, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EQT
def f17es_f17_efficiency_snapshot_eqt_252d_slope_v009_signal(revenue, equity, marketcap):
    base = _f17_turnover_rate(revenue, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d EQT
def f17es_f17_efficiency_snapshot_eqt_504d_slope_v010_signal(revenue, equity, marketcap):
    base = _f17_turnover_rate(revenue, equity, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d WCT
def f17es_f17_efficiency_snapshot_wct_21d_slope_v011_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d WCT
def f17es_f17_efficiency_snapshot_wct_252d_slope_v012_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d WCT
def f17es_f17_efficiency_snapshot_wct_504d_slope_v013_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capex/assets
def f17es_f17_efficiency_snapshot_capa_21d_slope_v014_signal(capex, assets, marketcap):
    base = _f17_efficiency_ratio(capex, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex/assets
def f17es_f17_efficiency_snapshot_capa_252d_slope_v015_signal(capex, assets, marketcap):
    base = _f17_efficiency_ratio(capex, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d capex/assets
def f17es_f17_efficiency_snapshot_capa_504d_slope_v016_signal(capex, assets, marketcap):
    base = _f17_efficiency_ratio(capex, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capex/revenue
def f17es_f17_efficiency_snapshot_capr_21d_slope_v017_signal(capex, revenue, marketcap):
    base = _f17_efficiency_ratio(capex, revenue, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex/revenue
def f17es_f17_efficiency_snapshot_capr_252d_slope_v018_signal(capex, revenue, marketcap):
    base = _f17_efficiency_ratio(capex, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ROA
def f17es_f17_efficiency_snapshot_roa_21d_slope_v019_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21) * marketcap
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ROA
def f17es_f17_efficiency_snapshot_roa_21d_slope_v020_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ROA
def f17es_f17_efficiency_snapshot_roa_63d_slope_v021_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 63) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ROA
def f17es_f17_efficiency_snapshot_roa_252d_slope_v022_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ROA
def f17es_f17_efficiency_snapshot_roa_504d_slope_v023_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ROE
def f17es_f17_efficiency_snapshot_roe_21d_slope_v024_signal(netinc, equity, marketcap):
    base = _f17_efficiency_ratio(netinc, equity, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ROE
def f17es_f17_efficiency_snapshot_roe_252d_slope_v025_signal(netinc, equity, marketcap):
    base = _f17_efficiency_ratio(netinc, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ROE
def f17es_f17_efficiency_snapshot_roe_504d_slope_v026_signal(netinc, equity, marketcap):
    base = _f17_efficiency_ratio(netinc, equity, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ROIC
def f17es_f17_efficiency_snapshot_roic_21d_slope_v027_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    base = _f17_efficiency_ratio(opinc, cap, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ROIC
def f17es_f17_efficiency_snapshot_roic_252d_slope_v028_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    base = _f17_efficiency_ratio(opinc, cap, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ROIC
def f17es_f17_efficiency_snapshot_roic_504d_slope_v029_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    base = _f17_efficiency_ratio(opinc, cap, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d CCC
def f17es_f17_efficiency_snapshot_ccc_21d_slope_v030_signal(ncfo, netinc, marketcap):
    base = _f17_efficiency_ratio(ncfo, netinc, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d CCC
def f17es_f17_efficiency_snapshot_ccc_252d_slope_v031_signal(ncfo, netinc, marketcap):
    base = _f17_efficiency_ratio(ncfo, netinc, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d CCC
def f17es_f17_efficiency_snapshot_ccc_504d_slope_v032_signal(ncfo, netinc, marketcap):
    base = _f17_efficiency_ratio(ncfo, netinc, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d FCF quality
def f17es_f17_efficiency_snapshot_fcfquality_21d_slope_v033_signal(fcf, netinc, marketcap):
    base = _f17_efficiency_ratio(fcf, netinc, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF quality
def f17es_f17_efficiency_snapshot_fcfquality_252d_slope_v034_signal(fcf, netinc, marketcap):
    base = _f17_efficiency_ratio(fcf, netinc, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d FCF margin
def f17es_f17_efficiency_snapshot_fcfmargin_21d_slope_v035_signal(fcf, revenue, marketcap):
    base = _f17_efficiency_ratio(fcf, revenue, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF margin
def f17es_f17_efficiency_snapshot_fcfmargin_252d_slope_v036_signal(fcf, revenue, marketcap):
    base = _f17_efficiency_ratio(fcf, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF margin
def f17es_f17_efficiency_snapshot_fcfmargin_504d_slope_v037_signal(fcf, revenue, marketcap):
    base = _f17_efficiency_ratio(fcf, revenue, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d EBITDA/assets
def f17es_f17_efficiency_snapshot_ebitdaassets_21d_slope_v038_signal(ebitda, assets, marketcap):
    base = _f17_efficiency_ratio(ebitda, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EBITDA/assets
def f17es_f17_efficiency_snapshot_ebitdaassets_252d_slope_v039_signal(ebitda, assets, marketcap):
    base = _f17_efficiency_ratio(ebitda, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d EBITDA/assets
def f17es_f17_efficiency_snapshot_ebitdaassets_504d_slope_v040_signal(ebitda, assets, marketcap):
    base = _f17_efficiency_ratio(ebitda, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF/assets
def f17es_f17_efficiency_snapshot_fcfassets_21d_slope_v041_signal(fcf, assets, marketcap):
    base = _f17_efficiency_ratio(fcf, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF/assets
def f17es_f17_efficiency_snapshot_fcfassets_252d_slope_v042_signal(fcf, assets, marketcap):
    base = _f17_efficiency_ratio(fcf, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF/assets
def f17es_f17_efficiency_snapshot_fcfassets_504d_slope_v043_signal(fcf, assets, marketcap):
    base = _f17_efficiency_ratio(fcf, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of NCFO/assets
def f17es_f17_efficiency_snapshot_ncfoassets_21d_slope_v044_signal(ncfo, assets, marketcap):
    base = _f17_efficiency_ratio(ncfo, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO/assets
def f17es_f17_efficiency_snapshot_ncfoassets_252d_slope_v045_signal(ncfo, assets, marketcap):
    base = _f17_efficiency_ratio(ncfo, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of GM
def f17es_f17_efficiency_snapshot_gm_21d_slope_v046_signal(gp, revenue, marketcap):
    base = _f17_efficiency_ratio(gp, revenue, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d GM
def f17es_f17_efficiency_snapshot_gm_252d_slope_v047_signal(gp, revenue, marketcap):
    base = _f17_efficiency_ratio(gp, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of OM
def f17es_f17_efficiency_snapshot_om_21d_slope_v048_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OM
def f17es_f17_efficiency_snapshot_om_252d_slope_v049_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of GP/Opinc ratio
def f17es_f17_efficiency_snapshot_gpopinc_21d_slope_v050_signal(gp, opinc, marketcap):
    base = _f17_efficiency_ratio(gp, opinc, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of GP/Opinc 252d
def f17es_f17_efficiency_snapshot_gpopinc_252d_slope_v051_signal(gp, opinc, marketcap):
    base = _f17_efficiency_ratio(gp, opinc, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of WC/Rev
def f17es_f17_efficiency_snapshot_wcrev_21d_slope_v052_signal(workingcapital, revenue, marketcap):
    base = _f17_efficiency_ratio(workingcapital, revenue, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d WC/Rev
def f17es_f17_efficiency_snapshot_wcrev_252d_slope_v053_signal(workingcapital, revenue, marketcap):
    base = _f17_efficiency_ratio(workingcapital, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d WC/Rev
def f17es_f17_efficiency_snapshot_wcrev_504d_slope_v054_signal(workingcapital, revenue, marketcap):
    base = _f17_efficiency_ratio(workingcapital, revenue, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of WC/Assets
def f17es_f17_efficiency_snapshot_wcassets_21d_slope_v055_signal(workingcapital, assets, marketcap):
    base = _f17_efficiency_ratio(workingcapital, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d WC/Assets
def f17es_f17_efficiency_snapshot_wcassets_252d_slope_v056_signal(workingcapital, assets, marketcap):
    base = _f17_efficiency_ratio(workingcapital, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revenue per share
def f17es_f17_efficiency_snapshot_revps_21d_slope_v057_signal(revenue, sharesbas, marketcap):
    base = _f17_efficiency_ratio(revenue, sharesbas, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue per share
def f17es_f17_efficiency_snapshot_revps_252d_slope_v058_signal(revenue, sharesbas, marketcap):
    base = _f17_efficiency_ratio(revenue, sharesbas, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EBITDA per share
def f17es_f17_efficiency_snapshot_ebitdaps_21d_slope_v059_signal(ebitda, sharesbas, marketcap):
    base = _f17_efficiency_ratio(ebitda, sharesbas, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EBITDA per share
def f17es_f17_efficiency_snapshot_ebitdaps_252d_slope_v060_signal(ebitda, sharesbas, marketcap):
    base = _f17_efficiency_ratio(ebitda, sharesbas, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of GP per share
def f17es_f17_efficiency_snapshot_gpps_21d_slope_v061_signal(gp, sharesbas, marketcap):
    base = _f17_efficiency_ratio(gp, sharesbas, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d GP per share
def f17es_f17_efficiency_snapshot_gpps_252d_slope_v062_signal(gp, sharesbas, marketcap):
    base = _f17_efficiency_ratio(gp, sharesbas, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d GP per Asset (Novy-Marx)
def f17es_f17_efficiency_snapshot_gpa_252d_slope_v063_signal(gp, assets, marketcap):
    base = _f17_efficiency_ratio(gp, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ROA z-score 252d
def f17es_f17_efficiency_snapshot_roaz_252d_slope_v064_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA z-score 504d
def f17es_f17_efficiency_snapshot_roaz_504d_slope_v065_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 63)
    base = _z(p, 504) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE z-score 252d
def f17es_f17_efficiency_snapshot_roez_252d_slope_v066_signal(netinc, equity, marketcap):
    p = _f17_efficiency_ratio(netinc, equity, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of AT z-score 252d
def f17es_f17_efficiency_snapshot_atz_252d_slope_v067_signal(revenue, assets, marketcap):
    p = _f17_turnover_rate(revenue, assets, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of GM z-score
def f17es_f17_efficiency_snapshot_gmz_252d_slope_v068_signal(gp, revenue, marketcap):
    p = _f17_efficiency_ratio(gp, revenue, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of OM z-score
def f17es_f17_efficiency_snapshot_omz_252d_slope_v069_signal(opinc, revenue, marketcap):
    p = _f17_efficiency_ratio(opinc, revenue, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin z-score
def f17es_f17_efficiency_snapshot_fcfmarginz_252d_slope_v070_signal(fcf, revenue, marketcap):
    p = _f17_efficiency_ratio(fcf, revenue, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of CCC z-score
def f17es_f17_efficiency_snapshot_cccz_252d_slope_v071_signal(ncfo, netinc, marketcap):
    p = _f17_efficiency_ratio(ncfo, netinc, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROIC z-score
def f17es_f17_efficiency_snapshot_roicz_252d_slope_v072_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    p = _f17_efficiency_ratio(opinc, cap, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA deviation
def f17es_f17_efficiency_snapshot_roadev_252d_slope_v073_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of OM deviation
def f17es_f17_efficiency_snapshot_omdev_252d_slope_v074_signal(opinc, revenue, marketcap):
    p = _f17_efficiency_ratio(opinc, revenue, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of AT deviation
def f17es_f17_efficiency_snapshot_atdev_252d_slope_v075_signal(revenue, assets, marketcap):
    p = _f17_turnover_rate(revenue, assets, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of GM deviation
def f17es_f17_efficiency_snapshot_gmdev_252d_slope_v076_signal(gp, revenue, marketcap):
    p = _f17_efficiency_ratio(gp, revenue, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA relative to 504d hi
def f17es_f17_efficiency_snapshot_roarelhi_504d_slope_v077_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of OM relative to 504d hi
def f17es_f17_efficiency_snapshot_omrelhi_504d_slope_v078_signal(opinc, revenue, marketcap):
    p = _f17_efficiency_ratio(opinc, revenue, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of AT relative to 504d hi
def f17es_f17_efficiency_snapshot_atrelhi_504d_slope_v079_signal(revenue, assets, marketcap):
    p = _f17_turnover_rate(revenue, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA position 504d
def f17es_f17_efficiency_snapshot_roapos_504d_slope_v080_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of OM position 504d
def f17es_f17_efficiency_snapshot_ompos_504d_slope_v081_signal(opinc, revenue, marketcap):
    p = _f17_efficiency_ratio(opinc, revenue, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of AT position 504d
def f17es_f17_efficiency_snapshot_atpos_504d_slope_v082_signal(revenue, assets, marketcap):
    p = _f17_turnover_rate(revenue, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of high-ROA count
def f17es_f17_efficiency_snapshot_highroa_count_252d_slope_v083_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    s = flag.rolling(252, min_periods=63).sum() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of high-OM count
def f17es_f17_efficiency_snapshot_highom_count_252d_slope_v084_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    s = flag.rolling(252, min_periods=63).sum() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of low-AT count
def f17es_f17_efficiency_snapshot_lowat_count_504d_slope_v085_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21)
    avg = _mean(base, 504)
    flag = (base < avg).astype(float)
    s = flag.rolling(504, min_periods=126).sum() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of blended efficiency 252d
def f17es_f17_efficiency_snapshot_blendedeff_252d_slope_v086_signal(netinc, assets, equity, opinc, debt, marketcap):
    a = _f17_efficiency_ratio(netinc, assets, 252)
    b = _f17_efficiency_ratio(netinc, equity, 252)
    cap = equity + debt
    c = _f17_efficiency_ratio(opinc, cap, 252)
    base = (a + b + c) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of blended margin 252d
def f17es_f17_efficiency_snapshot_blendedmargin_252d_slope_v087_signal(gp, opinc, fcf, revenue, marketcap):
    a = _f17_efficiency_ratio(gp, revenue, 252)
    b = _f17_efficiency_ratio(opinc, revenue, 252)
    c = _f17_efficiency_ratio(fcf, revenue, 252)
    base = (a + b + c) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA recent vs trend
def f17es_f17_efficiency_snapshot_roa_recent_vs_trend_slope_v088_signal(netinc, assets, marketcap):
    a = _f17_efficiency_ratio(netinc, assets, 63)
    b = _f17_efficiency_ratio(netinc, assets, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of OM recent vs trend
def f17es_f17_efficiency_snapshot_om_recent_vs_trend_slope_v089_signal(opinc, revenue, marketcap):
    a = _f17_efficiency_ratio(opinc, revenue, 63)
    b = _f17_efficiency_ratio(opinc, revenue, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of AT recent vs trend
def f17es_f17_efficiency_snapshot_at_recent_vs_trend_slope_v090_signal(revenue, assets, marketcap):
    a = _f17_turnover_rate(revenue, assets, 63)
    b = _f17_turnover_rate(revenue, assets, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of log ROA
def f17es_f17_efficiency_snapshot_logroa_21d_slope_v091_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _slope_diff_norm(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log ROA 252d
def f17es_f17_efficiency_snapshot_logroa_252d_slope_v092_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log OM 252d
def f17es_f17_efficiency_snapshot_logom_252d_slope_v093_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log AT 252d
def f17es_f17_efficiency_snapshot_logat_252d_slope_v094_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 252)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA squared
def f17es_f17_efficiency_snapshot_roasq_252d_slope_v095_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252)
    s = base * base.abs() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of OM squared
def f17es_f17_efficiency_snapshot_omsq_252d_slope_v096_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252)
    s = base * base.abs() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ROA EMA
def f17es_f17_efficiency_snapshot_roa_ema_21d_slope_v097_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA EMA 252d
def f17es_f17_efficiency_snapshot_roa_ema_252d_slope_v098_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of OM EMA 252d
def f17es_f17_efficiency_snapshot_om_ema_252d_slope_v099_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of AT EMA 252d
def f17es_f17_efficiency_snapshot_at_ema_252d_slope_v100_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of cash productivity
def f17es_f17_efficiency_snapshot_cashprod_21d_slope_v101_signal(ebitda, capex, assets, marketcap):
    num = ebitda - capex
    base = _f17_efficiency_ratio(num, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of cash productivity 252d
def f17es_f17_efficiency_snapshot_cashprod_252d_slope_v102_signal(ebitda, capex, assets, marketcap):
    num = ebitda - capex
    base = _f17_efficiency_ratio(num, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of core efficiency
def f17es_f17_efficiency_snapshot_coreeff_21d_slope_v103_signal(ncfo, capex, revenue, marketcap):
    num = ncfo - capex
    base = _f17_efficiency_ratio(num, revenue, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of core efficiency 252d
def f17es_f17_efficiency_snapshot_coreeff_252d_slope_v104_signal(ncfo, capex, revenue, marketcap):
    num = ncfo - capex
    base = _f17_efficiency_ratio(num, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of core efficiency 504d
def f17es_f17_efficiency_snapshot_coreeff_504d_slope_v105_signal(ncfo, capex, assets, marketcap):
    num = ncfo - capex
    base = _f17_efficiency_ratio(num, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retention/revenue
def f17es_f17_efficiency_snapshot_retentionrev_21d_slope_v106_signal(retearn, revenue, marketcap):
    base = _f17_efficiency_ratio(retearn, revenue, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retention/revenue 252d
def f17es_f17_efficiency_snapshot_retentionrev_252d_slope_v107_signal(retearn, revenue, marketcap):
    base = _f17_efficiency_ratio(retearn, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retention/netinc
def f17es_f17_efficiency_snapshot_retentionni_21d_slope_v108_signal(retearn, netinc, marketcap):
    base = _f17_efficiency_ratio(retearn, netinc, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retention/netinc 252d
def f17es_f17_efficiency_snapshot_retentionni_252d_slope_v109_signal(retearn, netinc, marketcap):
    base = _f17_efficiency_ratio(retearn, netinc, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revenue/wc
def f17es_f17_efficiency_snapshot_revwc_21d_slope_v110_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revenue/wc 252d
def f17es_f17_efficiency_snapshot_revwc_252d_slope_v111_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revenue/wc 504d
def f17es_f17_efficiency_snapshot_revwc_504d_slope_v112_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ebitda/opinc
def f17es_f17_efficiency_snapshot_ebitdaopinc_21d_slope_v113_signal(ebitda, opinc, marketcap):
    base = _f17_efficiency_ratio(ebitda, opinc, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda/opinc 252d
def f17es_f17_efficiency_snapshot_ebitdaopinc_252d_slope_v114_signal(ebitda, opinc, marketcap):
    base = _f17_efficiency_ratio(ebitda, opinc, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncfo/fcf
def f17es_f17_efficiency_snapshot_ncfofcf_21d_slope_v115_signal(ncfo, fcf, marketcap):
    base = _f17_efficiency_ratio(ncfo, fcf, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncfo/fcf 252d
def f17es_f17_efficiency_snapshot_ncfofcf_252d_slope_v116_signal(ncfo, fcf, marketcap):
    base = _f17_efficiency_ratio(ncfo, fcf, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/ncfo
def f17es_f17_efficiency_snapshot_capncfo_21d_slope_v117_signal(capex, ncfo, marketcap):
    base = _f17_efficiency_ratio(capex, ncfo, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/ncfo 252d
def f17es_f17_efficiency_snapshot_capncfo_252d_slope_v118_signal(capex, ncfo, marketcap):
    base = _f17_efficiency_ratio(capex, ncfo, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/ncfo 504d
def f17es_f17_efficiency_snapshot_capncfo_504d_slope_v119_signal(capex, ncfo, marketcap):
    base = _f17_efficiency_ratio(capex, ncfo, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gp/equity
def f17es_f17_efficiency_snapshot_gpequity_21d_slope_v120_signal(gp, equity, marketcap):
    base = _f17_efficiency_ratio(gp, equity, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gp/equity 252d
def f17es_f17_efficiency_snapshot_gpequity_252d_slope_v121_signal(gp, equity, marketcap):
    base = _f17_efficiency_ratio(gp, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gp/equity 504d
def f17es_f17_efficiency_snapshot_gpequity_504d_slope_v122_signal(gp, equity, marketcap):
    base = _f17_efficiency_ratio(gp, equity, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of opinc/assets 252d
def f17es_f17_efficiency_snapshot_opincassets_252d_slope_v123_signal(opinc, assets, marketcap):
    base = _f17_efficiency_ratio(opinc, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of opinc/assets 504d
def f17es_f17_efficiency_snapshot_opincassets_504d_slope_v124_signal(opinc, assets, marketcap):
    base = _f17_efficiency_ratio(opinc, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of opinc/equity 252d
def f17es_f17_efficiency_snapshot_opincequity_252d_slope_v125_signal(opinc, equity, marketcap):
    base = _f17_efficiency_ratio(opinc, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda/equity 504d
def f17es_f17_efficiency_snapshot_ebitdaequity_504d_slope_v126_signal(ebitda, equity, marketcap):
    base = _f17_efficiency_ratio(ebitda, equity, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revenue/liabilities 252d
def f17es_f17_efficiency_snapshot_revliab_252d_slope_v127_signal(revenue, liabilities, marketcap):
    base = _f17_turnover_rate(revenue, liabilities, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda/liabilities 252d
def f17es_f17_efficiency_snapshot_ebitdaliab_252d_slope_v128_signal(ebitda, liabilities, marketcap):
    base = _f17_efficiency_ratio(ebitda, liabilities, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncfo/liabilities 252d
def f17es_f17_efficiency_snapshot_ncfoliab_252d_slope_v129_signal(ncfo, liabilities, marketcap):
    base = _f17_efficiency_ratio(ncfo, liabilities, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/wc 252d
def f17es_f17_efficiency_snapshot_capwc_252d_slope_v130_signal(capex, workingcapital, marketcap):
    base = _f17_efficiency_ratio(capex, workingcapital, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of DuPont GM x AT 252d
def f17es_f17_efficiency_snapshot_dupont_252d_slope_v131_signal(gp, revenue, assets, marketcap):
    gm = _f17_efficiency_ratio(gp, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    base = (gm * at) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of DuPont OM x AT 252d
def f17es_f17_efficiency_snapshot_dupontom_252d_slope_v132_signal(opinc, revenue, assets, marketcap):
    om = _f17_efficiency_ratio(opinc, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    base = (om * at) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of full DuPont 252d
def f17es_f17_efficiency_snapshot_fulldupont_252d_slope_v133_signal(netinc, revenue, assets, equity, marketcap):
    nm = _f17_efficiency_ratio(netinc, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    em = _f17_efficiency_ratio(assets, equity, 252)
    base = (nm * at * em) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of investment efficiency 252d
def f17es_f17_efficiency_snapshot_invest_eff_252d_slope_v134_signal(netinc, capex, assets, marketcap):
    roa = _f17_efficiency_ratio(netinc, assets, 252)
    ci = _f17_efficiency_ratio(capex, assets, 252)
    base = (roa / ci.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net surplus efficiency 252d
def f17es_f17_efficiency_snapshot_net_surplus_252d_slope_v135_signal(netinc, capex, assets, marketcap):
    roa = _f17_efficiency_ratio(netinc, assets, 252)
    ci = _f17_efficiency_ratio(capex, assets, 252)
    base = (roa - ci) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (gp/assets * netinc/equity)
def f17es_f17_efficiency_snapshot_gpa_x_roe_252d_slope_v136_signal(gp, assets, netinc, equity, marketcap):
    a = _f17_efficiency_ratio(gp, assets, 252)
    b = _f17_efficiency_ratio(netinc, equity, 252)
    base = (a * b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (revenue per share x netinc per share)
def f17es_f17_efficiency_snapshot_revps_x_nips_252d_slope_v137_signal(revenue, sharesbas, netinc, marketcap):
    a = _f17_efficiency_ratio(revenue, sharesbas, 252)
    b = _f17_efficiency_ratio(netinc, sharesbas, 252)
    base = (a * b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF per share 252d
def f17es_f17_efficiency_snapshot_fcfps_252d_slope_v138_signal(fcf, sharesbas, marketcap):
    base = _f17_efficiency_ratio(fcf, sharesbas, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NCFO per share 252d
def f17es_f17_efficiency_snapshot_ncfops_252d_slope_v139_signal(ncfo, sharesbas, marketcap):
    base = _f17_efficiency_ratio(ncfo, sharesbas, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of opinc per share 252d
def f17es_f17_efficiency_snapshot_opincps_252d_slope_v140_signal(opinc, sharesbas, marketcap):
    base = _f17_efficiency_ratio(opinc, sharesbas, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (gp - opinc)/revenue (sg&a-like efficiency)
def f17es_f17_efficiency_snapshot_sga_252d_slope_v141_signal(gp, opinc, revenue, marketcap):
    sga = gp - opinc
    base = _f17_efficiency_ratio(sga, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (assets/revenue) - inverse asset turnover
def f17es_f17_efficiency_snapshot_assetsrev_252d_slope_v142_signal(assets, revenue, marketcap):
    base = _f17_efficiency_ratio(assets, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of equity/assets (financial leverage measure)
def f17es_f17_efficiency_snapshot_eqa_252d_slope_v143_signal(equity, assets, marketcap):
    base = _f17_efficiency_ratio(equity, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net working capital efficiency (rev / wc) 504d
def f17es_f17_efficiency_snapshot_revwc_eff_504d_slope_v144_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (ebitda/revenue) 252d EBITDA margin
def f17es_f17_efficiency_snapshot_ebitdamargin_252d_slope_v145_signal(ebitda, revenue, marketcap):
    base = _f17_efficiency_ratio(ebitda, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NM (net margin) x AT
def f17es_f17_efficiency_snapshot_nm_x_at_252d_slope_v146_signal(netinc, revenue, assets, marketcap):
    nm = _f17_efficiency_ratio(netinc, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    base = (nm * at) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex / ebitda (reinvestment intensity)
def f17es_f17_efficiency_snapshot_capebitda_252d_slope_v147_signal(capex, ebitda, marketcap):
    base = _f17_efficiency_ratio(capex, ebitda, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (ebitda - intexp)/assets - net cash productivity
def f17es_f17_efficiency_snapshot_netcash_a_252d_slope_v148_signal(ebitda, intexp, assets, marketcap):
    nc = ebitda - intexp
    base = _f17_efficiency_ratio(nc, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (revenue + ncfo)/assets composite
def f17es_f17_efficiency_snapshot_combo_a_252d_slope_v149_signal(revenue, ncfo, assets, marketcap):
    cb = revenue + ncfo
    base = _f17_turnover_rate(cb, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of full efficiency composite (ROA + OM + AT + GM)
def f17es_f17_efficiency_snapshot_fullcomp_252d_slope_v150_signal(netinc, assets, opinc, revenue, gp, marketcap):
    a = _f17_efficiency_ratio(netinc, assets, 252)
    b = _f17_efficiency_ratio(opinc, revenue, 252)
    c = _f17_turnover_rate(revenue, assets, 252)
    d = _f17_efficiency_ratio(gp, revenue, 252)
    base = (a + b + c + d) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17es_f17_efficiency_snapshot_at_21d_slope_v001_signal,
    f17es_f17_efficiency_snapshot_at_21d_slope_v002_signal,
    f17es_f17_efficiency_snapshot_at_63d_slope_v003_signal,
    f17es_f17_efficiency_snapshot_at_63d_slope_v004_signal,
    f17es_f17_efficiency_snapshot_at_126d_slope_v005_signal,
    f17es_f17_efficiency_snapshot_at_252d_slope_v006_signal,
    f17es_f17_efficiency_snapshot_at_504d_slope_v007_signal,
    f17es_f17_efficiency_snapshot_eqt_21d_slope_v008_signal,
    f17es_f17_efficiency_snapshot_eqt_252d_slope_v009_signal,
    f17es_f17_efficiency_snapshot_eqt_504d_slope_v010_signal,
    f17es_f17_efficiency_snapshot_wct_21d_slope_v011_signal,
    f17es_f17_efficiency_snapshot_wct_252d_slope_v012_signal,
    f17es_f17_efficiency_snapshot_wct_504d_slope_v013_signal,
    f17es_f17_efficiency_snapshot_capa_21d_slope_v014_signal,
    f17es_f17_efficiency_snapshot_capa_252d_slope_v015_signal,
    f17es_f17_efficiency_snapshot_capa_504d_slope_v016_signal,
    f17es_f17_efficiency_snapshot_capr_21d_slope_v017_signal,
    f17es_f17_efficiency_snapshot_capr_252d_slope_v018_signal,
    f17es_f17_efficiency_snapshot_roa_21d_slope_v019_signal,
    f17es_f17_efficiency_snapshot_roa_21d_slope_v020_signal,
    f17es_f17_efficiency_snapshot_roa_63d_slope_v021_signal,
    f17es_f17_efficiency_snapshot_roa_252d_slope_v022_signal,
    f17es_f17_efficiency_snapshot_roa_504d_slope_v023_signal,
    f17es_f17_efficiency_snapshot_roe_21d_slope_v024_signal,
    f17es_f17_efficiency_snapshot_roe_252d_slope_v025_signal,
    f17es_f17_efficiency_snapshot_roe_504d_slope_v026_signal,
    f17es_f17_efficiency_snapshot_roic_21d_slope_v027_signal,
    f17es_f17_efficiency_snapshot_roic_252d_slope_v028_signal,
    f17es_f17_efficiency_snapshot_roic_504d_slope_v029_signal,
    f17es_f17_efficiency_snapshot_ccc_21d_slope_v030_signal,
    f17es_f17_efficiency_snapshot_ccc_252d_slope_v031_signal,
    f17es_f17_efficiency_snapshot_ccc_504d_slope_v032_signal,
    f17es_f17_efficiency_snapshot_fcfquality_21d_slope_v033_signal,
    f17es_f17_efficiency_snapshot_fcfquality_252d_slope_v034_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_21d_slope_v035_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_252d_slope_v036_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_504d_slope_v037_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_21d_slope_v038_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_252d_slope_v039_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_504d_slope_v040_signal,
    f17es_f17_efficiency_snapshot_fcfassets_21d_slope_v041_signal,
    f17es_f17_efficiency_snapshot_fcfassets_252d_slope_v042_signal,
    f17es_f17_efficiency_snapshot_fcfassets_504d_slope_v043_signal,
    f17es_f17_efficiency_snapshot_ncfoassets_21d_slope_v044_signal,
    f17es_f17_efficiency_snapshot_ncfoassets_252d_slope_v045_signal,
    f17es_f17_efficiency_snapshot_gm_21d_slope_v046_signal,
    f17es_f17_efficiency_snapshot_gm_252d_slope_v047_signal,
    f17es_f17_efficiency_snapshot_om_21d_slope_v048_signal,
    f17es_f17_efficiency_snapshot_om_252d_slope_v049_signal,
    f17es_f17_efficiency_snapshot_gpopinc_21d_slope_v050_signal,
    f17es_f17_efficiency_snapshot_gpopinc_252d_slope_v051_signal,
    f17es_f17_efficiency_snapshot_wcrev_21d_slope_v052_signal,
    f17es_f17_efficiency_snapshot_wcrev_252d_slope_v053_signal,
    f17es_f17_efficiency_snapshot_wcrev_504d_slope_v054_signal,
    f17es_f17_efficiency_snapshot_wcassets_21d_slope_v055_signal,
    f17es_f17_efficiency_snapshot_wcassets_252d_slope_v056_signal,
    f17es_f17_efficiency_snapshot_revps_21d_slope_v057_signal,
    f17es_f17_efficiency_snapshot_revps_252d_slope_v058_signal,
    f17es_f17_efficiency_snapshot_ebitdaps_21d_slope_v059_signal,
    f17es_f17_efficiency_snapshot_ebitdaps_252d_slope_v060_signal,
    f17es_f17_efficiency_snapshot_gpps_21d_slope_v061_signal,
    f17es_f17_efficiency_snapshot_gpps_252d_slope_v062_signal,
    f17es_f17_efficiency_snapshot_gpa_252d_slope_v063_signal,
    f17es_f17_efficiency_snapshot_roaz_252d_slope_v064_signal,
    f17es_f17_efficiency_snapshot_roaz_504d_slope_v065_signal,
    f17es_f17_efficiency_snapshot_roez_252d_slope_v066_signal,
    f17es_f17_efficiency_snapshot_atz_252d_slope_v067_signal,
    f17es_f17_efficiency_snapshot_gmz_252d_slope_v068_signal,
    f17es_f17_efficiency_snapshot_omz_252d_slope_v069_signal,
    f17es_f17_efficiency_snapshot_fcfmarginz_252d_slope_v070_signal,
    f17es_f17_efficiency_snapshot_cccz_252d_slope_v071_signal,
    f17es_f17_efficiency_snapshot_roicz_252d_slope_v072_signal,
    f17es_f17_efficiency_snapshot_roadev_252d_slope_v073_signal,
    f17es_f17_efficiency_snapshot_omdev_252d_slope_v074_signal,
    f17es_f17_efficiency_snapshot_atdev_252d_slope_v075_signal,
    f17es_f17_efficiency_snapshot_gmdev_252d_slope_v076_signal,
    f17es_f17_efficiency_snapshot_roarelhi_504d_slope_v077_signal,
    f17es_f17_efficiency_snapshot_omrelhi_504d_slope_v078_signal,
    f17es_f17_efficiency_snapshot_atrelhi_504d_slope_v079_signal,
    f17es_f17_efficiency_snapshot_roapos_504d_slope_v080_signal,
    f17es_f17_efficiency_snapshot_ompos_504d_slope_v081_signal,
    f17es_f17_efficiency_snapshot_atpos_504d_slope_v082_signal,
    f17es_f17_efficiency_snapshot_highroa_count_252d_slope_v083_signal,
    f17es_f17_efficiency_snapshot_highom_count_252d_slope_v084_signal,
    f17es_f17_efficiency_snapshot_lowat_count_504d_slope_v085_signal,
    f17es_f17_efficiency_snapshot_blendedeff_252d_slope_v086_signal,
    f17es_f17_efficiency_snapshot_blendedmargin_252d_slope_v087_signal,
    f17es_f17_efficiency_snapshot_roa_recent_vs_trend_slope_v088_signal,
    f17es_f17_efficiency_snapshot_om_recent_vs_trend_slope_v089_signal,
    f17es_f17_efficiency_snapshot_at_recent_vs_trend_slope_v090_signal,
    f17es_f17_efficiency_snapshot_logroa_21d_slope_v091_signal,
    f17es_f17_efficiency_snapshot_logroa_252d_slope_v092_signal,
    f17es_f17_efficiency_snapshot_logom_252d_slope_v093_signal,
    f17es_f17_efficiency_snapshot_logat_252d_slope_v094_signal,
    f17es_f17_efficiency_snapshot_roasq_252d_slope_v095_signal,
    f17es_f17_efficiency_snapshot_omsq_252d_slope_v096_signal,
    f17es_f17_efficiency_snapshot_roa_ema_21d_slope_v097_signal,
    f17es_f17_efficiency_snapshot_roa_ema_252d_slope_v098_signal,
    f17es_f17_efficiency_snapshot_om_ema_252d_slope_v099_signal,
    f17es_f17_efficiency_snapshot_at_ema_252d_slope_v100_signal,
    f17es_f17_efficiency_snapshot_cashprod_21d_slope_v101_signal,
    f17es_f17_efficiency_snapshot_cashprod_252d_slope_v102_signal,
    f17es_f17_efficiency_snapshot_coreeff_21d_slope_v103_signal,
    f17es_f17_efficiency_snapshot_coreeff_252d_slope_v104_signal,
    f17es_f17_efficiency_snapshot_coreeff_504d_slope_v105_signal,
    f17es_f17_efficiency_snapshot_retentionrev_21d_slope_v106_signal,
    f17es_f17_efficiency_snapshot_retentionrev_252d_slope_v107_signal,
    f17es_f17_efficiency_snapshot_retentionni_21d_slope_v108_signal,
    f17es_f17_efficiency_snapshot_retentionni_252d_slope_v109_signal,
    f17es_f17_efficiency_snapshot_revwc_21d_slope_v110_signal,
    f17es_f17_efficiency_snapshot_revwc_252d_slope_v111_signal,
    f17es_f17_efficiency_snapshot_revwc_504d_slope_v112_signal,
    f17es_f17_efficiency_snapshot_ebitdaopinc_21d_slope_v113_signal,
    f17es_f17_efficiency_snapshot_ebitdaopinc_252d_slope_v114_signal,
    f17es_f17_efficiency_snapshot_ncfofcf_21d_slope_v115_signal,
    f17es_f17_efficiency_snapshot_ncfofcf_252d_slope_v116_signal,
    f17es_f17_efficiency_snapshot_capncfo_21d_slope_v117_signal,
    f17es_f17_efficiency_snapshot_capncfo_252d_slope_v118_signal,
    f17es_f17_efficiency_snapshot_capncfo_504d_slope_v119_signal,
    f17es_f17_efficiency_snapshot_gpequity_21d_slope_v120_signal,
    f17es_f17_efficiency_snapshot_gpequity_252d_slope_v121_signal,
    f17es_f17_efficiency_snapshot_gpequity_504d_slope_v122_signal,
    f17es_f17_efficiency_snapshot_opincassets_252d_slope_v123_signal,
    f17es_f17_efficiency_snapshot_opincassets_504d_slope_v124_signal,
    f17es_f17_efficiency_snapshot_opincequity_252d_slope_v125_signal,
    f17es_f17_efficiency_snapshot_ebitdaequity_504d_slope_v126_signal,
    f17es_f17_efficiency_snapshot_revliab_252d_slope_v127_signal,
    f17es_f17_efficiency_snapshot_ebitdaliab_252d_slope_v128_signal,
    f17es_f17_efficiency_snapshot_ncfoliab_252d_slope_v129_signal,
    f17es_f17_efficiency_snapshot_capwc_252d_slope_v130_signal,
    f17es_f17_efficiency_snapshot_dupont_252d_slope_v131_signal,
    f17es_f17_efficiency_snapshot_dupontom_252d_slope_v132_signal,
    f17es_f17_efficiency_snapshot_fulldupont_252d_slope_v133_signal,
    f17es_f17_efficiency_snapshot_invest_eff_252d_slope_v134_signal,
    f17es_f17_efficiency_snapshot_net_surplus_252d_slope_v135_signal,
    f17es_f17_efficiency_snapshot_gpa_x_roe_252d_slope_v136_signal,
    f17es_f17_efficiency_snapshot_revps_x_nips_252d_slope_v137_signal,
    f17es_f17_efficiency_snapshot_fcfps_252d_slope_v138_signal,
    f17es_f17_efficiency_snapshot_ncfops_252d_slope_v139_signal,
    f17es_f17_efficiency_snapshot_opincps_252d_slope_v140_signal,
    f17es_f17_efficiency_snapshot_sga_252d_slope_v141_signal,
    f17es_f17_efficiency_snapshot_assetsrev_252d_slope_v142_signal,
    f17es_f17_efficiency_snapshot_eqa_252d_slope_v143_signal,
    f17es_f17_efficiency_snapshot_revwc_eff_504d_slope_v144_signal,
    f17es_f17_efficiency_snapshot_ebitdamargin_252d_slope_v145_signal,
    f17es_f17_efficiency_snapshot_nm_x_at_252d_slope_v146_signal,
    f17es_f17_efficiency_snapshot_capebitda_252d_slope_v147_signal,
    f17es_f17_efficiency_snapshot_netcash_a_252d_slope_v148_signal,
    f17es_f17_efficiency_snapshot_combo_a_252d_slope_v149_signal,
    f17es_f17_efficiency_snapshot_fullcomp_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_EFFICIENCY_SNAPSHOT_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    eps = pd.Series(1.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="eps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    workingcapital = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.006, n))), name="workingcapital")
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(np.random.normal(0.0, 0.003, n))), name="currentratio")
    intexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.004, n))), name="intexp")
    liabilities = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="liabilities")
    retearn = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="retearn")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = marketcap + debt - 0.3 * marketcap
    ev = pd.Series(ev.values, name="ev")
    evebit = ev / opinc.replace(0, np.nan)
    evebit = pd.Series(evebit.values, name="evebit")
    evebitda = ev / ebitda.replace(0, np.nan)
    evebitda = pd.Series(evebitda.values, name="evebitda")
    pe = marketcap / netinc.replace(0, np.nan)
    pe = pd.Series(pe.values, name="pe")
    pb = marketcap / equity.replace(0, np.nan)
    pb = pd.Series(pb.values, name="pb")
    ps = marketcap / revenue.replace(0, np.nan)
    ps = pd.Series(ps.values, name="ps")
    cols = {"closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "eps": eps, "sharesbas": sharesbas, "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
            "currentratio": currentratio, "intexp": intexp, "liabilities": liabilities, "retearn": retearn,
            "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f17_efficiency", "_f17_turnover")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_efficiency_snapshot_2nd_derivatives_001_150_claude: {n_features} features pass")
