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


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f17_efficiency_ratio(numerator, denominator, w):
    n = _mean(numerator, w)
    d = _mean(denominator, w)
    return n / d.replace(0, np.nan).abs()


def _f17_turnover_rate(flow, stock, w):
    f = _mean(flow, w)
    s = _mean(stock, w)
    return f / s.replace(0, np.nan).abs()


# 5d jerk of 21d AT
def f17es_f17_efficiency_snapshot_at_21d_jerk_v001_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21) * marketcap
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d AT
def f17es_f17_efficiency_snapshot_at_21d_jerk_v002_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d AT
def f17es_f17_efficiency_snapshot_at_63d_jerk_v003_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d AT
def f17es_f17_efficiency_snapshot_at_63d_jerk_v004_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 63) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d AT
def f17es_f17_efficiency_snapshot_at_126d_jerk_v005_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 126) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d AT
def f17es_f17_efficiency_snapshot_at_252d_jerk_v006_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d AT
def f17es_f17_efficiency_snapshot_at_504d_jerk_v007_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d EQT
def f17es_f17_efficiency_snapshot_eqt_21d_jerk_v008_signal(revenue, equity, marketcap):
    base = _f17_turnover_rate(revenue, equity, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EQT
def f17es_f17_efficiency_snapshot_eqt_252d_jerk_v009_signal(revenue, equity, marketcap):
    base = _f17_turnover_rate(revenue, equity, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d EQT
def f17es_f17_efficiency_snapshot_eqt_504d_jerk_v010_signal(revenue, equity, marketcap):
    base = _f17_turnover_rate(revenue, equity, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d WCT
def f17es_f17_efficiency_snapshot_wct_21d_jerk_v011_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d WCT
def f17es_f17_efficiency_snapshot_wct_252d_jerk_v012_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d WCT
def f17es_f17_efficiency_snapshot_wct_504d_jerk_v013_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d capex/assets
def f17es_f17_efficiency_snapshot_capa_21d_jerk_v014_signal(capex, assets, marketcap):
    base = _f17_efficiency_ratio(capex, assets, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d capex/assets
def f17es_f17_efficiency_snapshot_capa_252d_jerk_v015_signal(capex, assets, marketcap):
    base = _f17_efficiency_ratio(capex, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d capex/assets
def f17es_f17_efficiency_snapshot_capa_504d_jerk_v016_signal(capex, assets, marketcap):
    base = _f17_efficiency_ratio(capex, assets, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d capex/revenue
def f17es_f17_efficiency_snapshot_capr_21d_jerk_v017_signal(capex, revenue, marketcap):
    base = _f17_efficiency_ratio(capex, revenue, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d capex/revenue
def f17es_f17_efficiency_snapshot_capr_252d_jerk_v018_signal(capex, revenue, marketcap):
    base = _f17_efficiency_ratio(capex, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ROA
def f17es_f17_efficiency_snapshot_roa_21d_jerk_v019_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21) * marketcap
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROA
def f17es_f17_efficiency_snapshot_roa_21d_jerk_v020_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ROA
def f17es_f17_efficiency_snapshot_roa_63d_jerk_v021_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROA
def f17es_f17_efficiency_snapshot_roa_252d_jerk_v022_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ROA
def f17es_f17_efficiency_snapshot_roa_504d_jerk_v023_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROE
def f17es_f17_efficiency_snapshot_roe_21d_jerk_v024_signal(netinc, equity, marketcap):
    base = _f17_efficiency_ratio(netinc, equity, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROE
def f17es_f17_efficiency_snapshot_roe_252d_jerk_v025_signal(netinc, equity, marketcap):
    base = _f17_efficiency_ratio(netinc, equity, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ROE
def f17es_f17_efficiency_snapshot_roe_504d_jerk_v026_signal(netinc, equity, marketcap):
    base = _f17_efficiency_ratio(netinc, equity, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ROIC
def f17es_f17_efficiency_snapshot_roic_21d_jerk_v027_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    base = _f17_efficiency_ratio(opinc, cap, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ROIC
def f17es_f17_efficiency_snapshot_roic_252d_jerk_v028_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    base = _f17_efficiency_ratio(opinc, cap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ROIC
def f17es_f17_efficiency_snapshot_roic_504d_jerk_v029_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    base = _f17_efficiency_ratio(opinc, cap, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d CCC
def f17es_f17_efficiency_snapshot_ccc_21d_jerk_v030_signal(ncfo, netinc, marketcap):
    base = _f17_efficiency_ratio(ncfo, netinc, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d CCC
def f17es_f17_efficiency_snapshot_ccc_252d_jerk_v031_signal(ncfo, netinc, marketcap):
    base = _f17_efficiency_ratio(ncfo, netinc, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d CCC
def f17es_f17_efficiency_snapshot_ccc_504d_jerk_v032_signal(ncfo, netinc, marketcap):
    base = _f17_efficiency_ratio(ncfo, netinc, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d FCF quality
def f17es_f17_efficiency_snapshot_fcfquality_21d_jerk_v033_signal(fcf, netinc, marketcap):
    base = _f17_efficiency_ratio(fcf, netinc, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d FCF quality
def f17es_f17_efficiency_snapshot_fcfquality_252d_jerk_v034_signal(fcf, netinc, marketcap):
    base = _f17_efficiency_ratio(fcf, netinc, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d FCF margin
def f17es_f17_efficiency_snapshot_fcfmargin_21d_jerk_v035_signal(fcf, revenue, marketcap):
    base = _f17_efficiency_ratio(fcf, revenue, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d FCF margin
def f17es_f17_efficiency_snapshot_fcfmargin_252d_jerk_v036_signal(fcf, revenue, marketcap):
    base = _f17_efficiency_ratio(fcf, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d FCF margin
def f17es_f17_efficiency_snapshot_fcfmargin_504d_jerk_v037_signal(fcf, revenue, marketcap):
    base = _f17_efficiency_ratio(fcf, revenue, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d EBITDA/assets
def f17es_f17_efficiency_snapshot_ebitdaassets_21d_jerk_v038_signal(ebitda, assets, marketcap):
    base = _f17_efficiency_ratio(ebitda, assets, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EBITDA/assets
def f17es_f17_efficiency_snapshot_ebitdaassets_252d_jerk_v039_signal(ebitda, assets, marketcap):
    base = _f17_efficiency_ratio(ebitda, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d EBITDA/assets
def f17es_f17_efficiency_snapshot_ebitdaassets_504d_jerk_v040_signal(ebitda, assets, marketcap):
    base = _f17_efficiency_ratio(ebitda, assets, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF/assets
def f17es_f17_efficiency_snapshot_fcfassets_21d_jerk_v041_signal(fcf, assets, marketcap):
    base = _f17_efficiency_ratio(fcf, assets, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d FCF/assets
def f17es_f17_efficiency_snapshot_fcfassets_252d_jerk_v042_signal(fcf, assets, marketcap):
    base = _f17_efficiency_ratio(fcf, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d FCF/assets
def f17es_f17_efficiency_snapshot_fcfassets_504d_jerk_v043_signal(fcf, assets, marketcap):
    base = _f17_efficiency_ratio(fcf, assets, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of NCFO/assets
def f17es_f17_efficiency_snapshot_ncfoassets_21d_jerk_v044_signal(ncfo, assets, marketcap):
    base = _f17_efficiency_ratio(ncfo, assets, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d NCFO/assets
def f17es_f17_efficiency_snapshot_ncfoassets_252d_jerk_v045_signal(ncfo, assets, marketcap):
    base = _f17_efficiency_ratio(ncfo, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of GM
def f17es_f17_efficiency_snapshot_gm_21d_jerk_v046_signal(gp, revenue, marketcap):
    base = _f17_efficiency_ratio(gp, revenue, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d GM
def f17es_f17_efficiency_snapshot_gm_252d_jerk_v047_signal(gp, revenue, marketcap):
    base = _f17_efficiency_ratio(gp, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of OM
def f17es_f17_efficiency_snapshot_om_21d_jerk_v048_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d OM
def f17es_f17_efficiency_snapshot_om_252d_jerk_v049_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of GP/Opinc
def f17es_f17_efficiency_snapshot_gpopinc_21d_jerk_v050_signal(gp, opinc, marketcap):
    base = _f17_efficiency_ratio(gp, opinc, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of GP/Opinc 252d
def f17es_f17_efficiency_snapshot_gpopinc_252d_jerk_v051_signal(gp, opinc, marketcap):
    base = _f17_efficiency_ratio(gp, opinc, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of WC/Rev
def f17es_f17_efficiency_snapshot_wcrev_21d_jerk_v052_signal(workingcapital, revenue, marketcap):
    base = _f17_efficiency_ratio(workingcapital, revenue, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d WC/Rev
def f17es_f17_efficiency_snapshot_wcrev_252d_jerk_v053_signal(workingcapital, revenue, marketcap):
    base = _f17_efficiency_ratio(workingcapital, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d WC/Rev
def f17es_f17_efficiency_snapshot_wcrev_504d_jerk_v054_signal(workingcapital, revenue, marketcap):
    base = _f17_efficiency_ratio(workingcapital, revenue, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of WC/Assets
def f17es_f17_efficiency_snapshot_wcassets_21d_jerk_v055_signal(workingcapital, assets, marketcap):
    base = _f17_efficiency_ratio(workingcapital, assets, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d WC/Assets
def f17es_f17_efficiency_snapshot_wcassets_252d_jerk_v056_signal(workingcapital, assets, marketcap):
    base = _f17_efficiency_ratio(workingcapital, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revenue per share
def f17es_f17_efficiency_snapshot_revps_21d_jerk_v057_signal(revenue, sharesbas, marketcap):
    base = _f17_efficiency_ratio(revenue, sharesbas, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d revenue per share
def f17es_f17_efficiency_snapshot_revps_252d_jerk_v058_signal(revenue, sharesbas, marketcap):
    base = _f17_efficiency_ratio(revenue, sharesbas, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of EBITDA per share
def f17es_f17_efficiency_snapshot_ebitdaps_21d_jerk_v059_signal(ebitda, sharesbas, marketcap):
    base = _f17_efficiency_ratio(ebitda, sharesbas, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EBITDA per share
def f17es_f17_efficiency_snapshot_ebitdaps_252d_jerk_v060_signal(ebitda, sharesbas, marketcap):
    base = _f17_efficiency_ratio(ebitda, sharesbas, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of GP per share
def f17es_f17_efficiency_snapshot_gpps_21d_jerk_v061_signal(gp, sharesbas, marketcap):
    base = _f17_efficiency_ratio(gp, sharesbas, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d GP per share
def f17es_f17_efficiency_snapshot_gpps_252d_jerk_v062_signal(gp, sharesbas, marketcap):
    base = _f17_efficiency_ratio(gp, sharesbas, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d GP per Asset
def f17es_f17_efficiency_snapshot_gpa_252d_jerk_v063_signal(gp, assets, marketcap):
    base = _f17_efficiency_ratio(gp, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ROA z-score 252d
def f17es_f17_efficiency_snapshot_roaz_252d_jerk_v064_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 21)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 21)
    result = _diff(sl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ROA z-score 504d
def f17es_f17_efficiency_snapshot_roaz_504d_jerk_v065_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 63)
    base = _z(p, 504) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ROE z-score 252d
def f17es_f17_efficiency_snapshot_roez_252d_jerk_v066_signal(netinc, equity, marketcap):
    p = _f17_efficiency_ratio(netinc, equity, 21)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of AT z-score 252d
def f17es_f17_efficiency_snapshot_atz_252d_jerk_v067_signal(revenue, assets, marketcap):
    p = _f17_turnover_rate(revenue, assets, 21)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of GM z-score
def f17es_f17_efficiency_snapshot_gmz_252d_jerk_v068_signal(gp, revenue, marketcap):
    p = _f17_efficiency_ratio(gp, revenue, 21)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of OM z-score
def f17es_f17_efficiency_snapshot_omz_252d_jerk_v069_signal(opinc, revenue, marketcap):
    p = _f17_efficiency_ratio(opinc, revenue, 21)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin z-score
def f17es_f17_efficiency_snapshot_fcfmarginz_252d_jerk_v070_signal(fcf, revenue, marketcap):
    p = _f17_efficiency_ratio(fcf, revenue, 21)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of CCC z-score
def f17es_f17_efficiency_snapshot_cccz_252d_jerk_v071_signal(ncfo, netinc, marketcap):
    p = _f17_efficiency_ratio(ncfo, netinc, 21)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ROIC z-score
def f17es_f17_efficiency_snapshot_roicz_252d_jerk_v072_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    p = _f17_efficiency_ratio(opinc, cap, 21)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ROA deviation
def f17es_f17_efficiency_snapshot_roadev_252d_jerk_v073_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of OM deviation
def f17es_f17_efficiency_snapshot_omdev_252d_jerk_v074_signal(opinc, revenue, marketcap):
    p = _f17_efficiency_ratio(opinc, revenue, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of AT deviation
def f17es_f17_efficiency_snapshot_atdev_252d_jerk_v075_signal(revenue, assets, marketcap):
    p = _f17_turnover_rate(revenue, assets, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of GM deviation
def f17es_f17_efficiency_snapshot_gmdev_252d_jerk_v076_signal(gp, revenue, marketcap):
    p = _f17_efficiency_ratio(gp, revenue, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ROA relative to 504d hi
def f17es_f17_efficiency_snapshot_roarelhi_504d_jerk_v077_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of OM relative to 504d hi
def f17es_f17_efficiency_snapshot_omrelhi_504d_jerk_v078_signal(opinc, revenue, marketcap):
    p = _f17_efficiency_ratio(opinc, revenue, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of AT relative to 504d hi
def f17es_f17_efficiency_snapshot_atrelhi_504d_jerk_v079_signal(revenue, assets, marketcap):
    p = _f17_turnover_rate(revenue, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ROA position 504d
def f17es_f17_efficiency_snapshot_roapos_504d_jerk_v080_signal(netinc, assets, marketcap):
    p = _f17_efficiency_ratio(netinc, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of OM position 504d
def f17es_f17_efficiency_snapshot_ompos_504d_jerk_v081_signal(opinc, revenue, marketcap):
    p = _f17_efficiency_ratio(opinc, revenue, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of AT position 504d
def f17es_f17_efficiency_snapshot_atpos_504d_jerk_v082_signal(revenue, assets, marketcap):
    p = _f17_turnover_rate(revenue, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of high-ROA count
def f17es_f17_efficiency_snapshot_highroa_count_252d_jerk_v083_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    s = flag.rolling(252, min_periods=63).sum() * marketcap
    result = _jerk(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of high-OM count
def f17es_f17_efficiency_snapshot_highom_count_252d_jerk_v084_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    s = flag.rolling(252, min_periods=63).sum() * marketcap
    result = _jerk(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of low-AT count
def f17es_f17_efficiency_snapshot_lowat_count_504d_jerk_v085_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21)
    avg = _mean(base, 504)
    flag = (base < avg).astype(float)
    s = flag.rolling(504, min_periods=126).sum() * marketcap
    result = _jerk(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of blended efficiency
def f17es_f17_efficiency_snapshot_blendedeff_252d_jerk_v086_signal(netinc, assets, equity, opinc, debt, marketcap):
    a = _f17_efficiency_ratio(netinc, assets, 252)
    b = _f17_efficiency_ratio(netinc, equity, 252)
    cap = equity + debt
    c = _f17_efficiency_ratio(opinc, cap, 252)
    base = (a + b + c) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of blended margin
def f17es_f17_efficiency_snapshot_blendedmargin_252d_jerk_v087_signal(gp, opinc, fcf, revenue, marketcap):
    a = _f17_efficiency_ratio(gp, revenue, 252)
    b = _f17_efficiency_ratio(opinc, revenue, 252)
    c = _f17_efficiency_ratio(fcf, revenue, 252)
    base = (a + b + c) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ROA recent vs trend
def f17es_f17_efficiency_snapshot_roa_recent_vs_trend_jerk_v088_signal(netinc, assets, marketcap):
    a = _f17_efficiency_ratio(netinc, assets, 63)
    b = _f17_efficiency_ratio(netinc, assets, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of OM recent vs trend
def f17es_f17_efficiency_snapshot_om_recent_vs_trend_jerk_v089_signal(opinc, revenue, marketcap):
    a = _f17_efficiency_ratio(opinc, revenue, 63)
    b = _f17_efficiency_ratio(opinc, revenue, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of AT recent vs trend
def f17es_f17_efficiency_snapshot_at_recent_vs_trend_jerk_v090_signal(revenue, assets, marketcap):
    a = _f17_turnover_rate(revenue, assets, 63)
    b = _f17_turnover_rate(revenue, assets, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log ROA
def f17es_f17_efficiency_snapshot_logroa_21d_jerk_v091_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _jerk(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log ROA 252d
def f17es_f17_efficiency_snapshot_logroa_252d_jerk_v092_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _jerk(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log OM 252d
def f17es_f17_efficiency_snapshot_logom_252d_jerk_v093_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _jerk(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log AT 252d
def f17es_f17_efficiency_snapshot_logat_252d_jerk_v094_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 252)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _jerk(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ROA squared
def f17es_f17_efficiency_snapshot_roasq_252d_jerk_v095_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252)
    s = base * base.abs() * marketcap
    result = _jerk(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of OM squared
def f17es_f17_efficiency_snapshot_omsq_252d_jerk_v096_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252)
    s = base * base.abs() * marketcap
    result = _jerk(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ROA EMA
def f17es_f17_efficiency_snapshot_roa_ema_21d_jerk_v097_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21).ewm(span=21, adjust=False).mean() * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ROA EMA 252d
def f17es_f17_efficiency_snapshot_roa_ema_252d_jerk_v098_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of OM EMA 252d
def f17es_f17_efficiency_snapshot_om_ema_252d_jerk_v099_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of AT EMA 252d
def f17es_f17_efficiency_snapshot_at_ema_252d_jerk_v100_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cash productivity
def f17es_f17_efficiency_snapshot_cashprod_21d_jerk_v101_signal(ebitda, capex, assets, marketcap):
    num = ebitda - capex
    base = _f17_efficiency_ratio(num, assets, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cash productivity 252d
def f17es_f17_efficiency_snapshot_cashprod_252d_jerk_v102_signal(ebitda, capex, assets, marketcap):
    num = ebitda - capex
    base = _f17_efficiency_ratio(num, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of core efficiency
def f17es_f17_efficiency_snapshot_coreeff_21d_jerk_v103_signal(ncfo, capex, revenue, marketcap):
    num = ncfo - capex
    base = _f17_efficiency_ratio(num, revenue, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of core efficiency 252d
def f17es_f17_efficiency_snapshot_coreeff_252d_jerk_v104_signal(ncfo, capex, revenue, marketcap):
    num = ncfo - capex
    base = _f17_efficiency_ratio(num, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of core efficiency 504d
def f17es_f17_efficiency_snapshot_coreeff_504d_jerk_v105_signal(ncfo, capex, assets, marketcap):
    num = ncfo - capex
    base = _f17_efficiency_ratio(num, assets, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of retention/revenue
def f17es_f17_efficiency_snapshot_retentionrev_21d_jerk_v106_signal(retearn, revenue, marketcap):
    base = _f17_efficiency_ratio(retearn, revenue, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of retention/revenue 252d
def f17es_f17_efficiency_snapshot_retentionrev_252d_jerk_v107_signal(retearn, revenue, marketcap):
    base = _f17_efficiency_ratio(retearn, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of retention/netinc
def f17es_f17_efficiency_snapshot_retentionni_21d_jerk_v108_signal(retearn, netinc, marketcap):
    base = _f17_efficiency_ratio(retearn, netinc, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of retention/netinc 252d
def f17es_f17_efficiency_snapshot_retentionni_252d_jerk_v109_signal(retearn, netinc, marketcap):
    base = _f17_efficiency_ratio(retearn, netinc, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revenue/wc
def f17es_f17_efficiency_snapshot_revwc_21d_jerk_v110_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revenue/wc 252d
def f17es_f17_efficiency_snapshot_revwc_252d_jerk_v111_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revenue/wc 504d
def f17es_f17_efficiency_snapshot_revwc_504d_jerk_v112_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ebitda/opinc
def f17es_f17_efficiency_snapshot_ebitdaopinc_21d_jerk_v113_signal(ebitda, opinc, marketcap):
    base = _f17_efficiency_ratio(ebitda, opinc, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ebitda/opinc 252d
def f17es_f17_efficiency_snapshot_ebitdaopinc_252d_jerk_v114_signal(ebitda, opinc, marketcap):
    base = _f17_efficiency_ratio(ebitda, opinc, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ncfo/fcf
def f17es_f17_efficiency_snapshot_ncfofcf_21d_jerk_v115_signal(ncfo, fcf, marketcap):
    base = _f17_efficiency_ratio(ncfo, fcf, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo/fcf 252d
def f17es_f17_efficiency_snapshot_ncfofcf_252d_jerk_v116_signal(ncfo, fcf, marketcap):
    base = _f17_efficiency_ratio(ncfo, fcf, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capex/ncfo
def f17es_f17_efficiency_snapshot_capncfo_21d_jerk_v117_signal(capex, ncfo, marketcap):
    base = _f17_efficiency_ratio(capex, ncfo, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/ncfo 252d
def f17es_f17_efficiency_snapshot_capncfo_252d_jerk_v118_signal(capex, ncfo, marketcap):
    base = _f17_efficiency_ratio(capex, ncfo, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/ncfo 504d
def f17es_f17_efficiency_snapshot_capncfo_504d_jerk_v119_signal(capex, ncfo, marketcap):
    base = _f17_efficiency_ratio(capex, ncfo, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of gp/equity
def f17es_f17_efficiency_snapshot_gpequity_21d_jerk_v120_signal(gp, equity, marketcap):
    base = _f17_efficiency_ratio(gp, equity, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of gp/equity 252d
def f17es_f17_efficiency_snapshot_gpequity_252d_jerk_v121_signal(gp, equity, marketcap):
    base = _f17_efficiency_ratio(gp, equity, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of gp/equity 504d
def f17es_f17_efficiency_snapshot_gpequity_504d_jerk_v122_signal(gp, equity, marketcap):
    base = _f17_efficiency_ratio(gp, equity, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of opinc/assets 252d
def f17es_f17_efficiency_snapshot_opincassets_252d_jerk_v123_signal(opinc, assets, marketcap):
    base = _f17_efficiency_ratio(opinc, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of opinc/assets 504d
def f17es_f17_efficiency_snapshot_opincassets_504d_jerk_v124_signal(opinc, assets, marketcap):
    base = _f17_efficiency_ratio(opinc, assets, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of opinc/equity 252d
def f17es_f17_efficiency_snapshot_opincequity_252d_jerk_v125_signal(opinc, equity, marketcap):
    base = _f17_efficiency_ratio(opinc, equity, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ebitda/equity 504d
def f17es_f17_efficiency_snapshot_ebitdaequity_504d_jerk_v126_signal(ebitda, equity, marketcap):
    base = _f17_efficiency_ratio(ebitda, equity, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revenue/liabilities 252d
def f17es_f17_efficiency_snapshot_revliab_252d_jerk_v127_signal(revenue, liabilities, marketcap):
    base = _f17_turnover_rate(revenue, liabilities, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ebitda/liabilities 252d
def f17es_f17_efficiency_snapshot_ebitdaliab_252d_jerk_v128_signal(ebitda, liabilities, marketcap):
    base = _f17_efficiency_ratio(ebitda, liabilities, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo/liabilities 252d
def f17es_f17_efficiency_snapshot_ncfoliab_252d_jerk_v129_signal(ncfo, liabilities, marketcap):
    base = _f17_efficiency_ratio(ncfo, liabilities, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/wc 252d
def f17es_f17_efficiency_snapshot_capwc_252d_jerk_v130_signal(capex, workingcapital, marketcap):
    base = _f17_efficiency_ratio(capex, workingcapital, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of DuPont GM x AT 252d
def f17es_f17_efficiency_snapshot_dupont_252d_jerk_v131_signal(gp, revenue, assets, marketcap):
    gm = _f17_efficiency_ratio(gp, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    base = (gm * at) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of DuPont OM x AT 252d
def f17es_f17_efficiency_snapshot_dupontom_252d_jerk_v132_signal(opinc, revenue, assets, marketcap):
    om = _f17_efficiency_ratio(opinc, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    base = (om * at) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of full DuPont 252d
def f17es_f17_efficiency_snapshot_fulldupont_252d_jerk_v133_signal(netinc, revenue, assets, equity, marketcap):
    nm = _f17_efficiency_ratio(netinc, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    em = _f17_efficiency_ratio(assets, equity, 252)
    base = (nm * at * em) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of investment efficiency 252d
def f17es_f17_efficiency_snapshot_invest_eff_252d_jerk_v134_signal(netinc, capex, assets, marketcap):
    roa = _f17_efficiency_ratio(netinc, assets, 252)
    ci = _f17_efficiency_ratio(capex, assets, 252)
    base = (roa / ci.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of net surplus efficiency 252d
def f17es_f17_efficiency_snapshot_net_surplus_252d_jerk_v135_signal(netinc, capex, assets, marketcap):
    roa = _f17_efficiency_ratio(netinc, assets, 252)
    ci = _f17_efficiency_ratio(capex, assets, 252)
    base = (roa - ci) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (gp/assets * netinc/equity)
def f17es_f17_efficiency_snapshot_gpa_x_roe_252d_jerk_v136_signal(gp, assets, netinc, equity, marketcap):
    a = _f17_efficiency_ratio(gp, assets, 252)
    b = _f17_efficiency_ratio(netinc, equity, 252)
    base = (a * b) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (revenue per share x netinc per share)
def f17es_f17_efficiency_snapshot_revps_x_nips_252d_jerk_v137_signal(revenue, sharesbas, netinc, marketcap):
    a = _f17_efficiency_ratio(revenue, sharesbas, 252)
    b = _f17_efficiency_ratio(netinc, sharesbas, 252)
    base = (a * b) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF per share 252d
def f17es_f17_efficiency_snapshot_fcfps_252d_jerk_v138_signal(fcf, sharesbas, marketcap):
    base = _f17_efficiency_ratio(fcf, sharesbas, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of NCFO per share 252d
def f17es_f17_efficiency_snapshot_ncfops_252d_jerk_v139_signal(ncfo, sharesbas, marketcap):
    base = _f17_efficiency_ratio(ncfo, sharesbas, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of opinc per share 252d
def f17es_f17_efficiency_snapshot_opincps_252d_jerk_v140_signal(opinc, sharesbas, marketcap):
    base = _f17_efficiency_ratio(opinc, sharesbas, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (gp - opinc)/revenue (sg&a-like efficiency)
def f17es_f17_efficiency_snapshot_sga_252d_jerk_v141_signal(gp, opinc, revenue, marketcap):
    sga = gp - opinc
    base = _f17_efficiency_ratio(sga, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of assets/revenue
def f17es_f17_efficiency_snapshot_assetsrev_252d_jerk_v142_signal(assets, revenue, marketcap):
    base = _f17_efficiency_ratio(assets, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of equity/assets (financial leverage measure)
def f17es_f17_efficiency_snapshot_eqa_252d_jerk_v143_signal(equity, assets, marketcap):
    base = _f17_efficiency_ratio(equity, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of net working capital efficiency
def f17es_f17_efficiency_snapshot_revwc_eff_504d_jerk_v144_signal(revenue, workingcapital, marketcap):
    base = _f17_turnover_rate(revenue, workingcapital, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EBITDA margin
def f17es_f17_efficiency_snapshot_ebitdamargin_252d_jerk_v145_signal(ebitda, revenue, marketcap):
    base = _f17_efficiency_ratio(ebitda, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of NM x AT 252d
def f17es_f17_efficiency_snapshot_nm_x_at_252d_jerk_v146_signal(netinc, revenue, assets, marketcap):
    nm = _f17_efficiency_ratio(netinc, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    base = (nm * at) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/ebitda 252d
def f17es_f17_efficiency_snapshot_capebitda_252d_jerk_v147_signal(capex, ebitda, marketcap):
    base = _f17_efficiency_ratio(capex, ebitda, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (ebitda - intexp)/assets net cash productivity
def f17es_f17_efficiency_snapshot_netcash_a_252d_jerk_v148_signal(ebitda, intexp, assets, marketcap):
    nc = ebitda - intexp
    base = _f17_efficiency_ratio(nc, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (revenue + ncfo)/assets composite
def f17es_f17_efficiency_snapshot_combo_a_252d_jerk_v149_signal(revenue, ncfo, assets, marketcap):
    cb = revenue + ncfo
    base = _f17_turnover_rate(cb, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of full efficiency composite
def f17es_f17_efficiency_snapshot_fullcomp_252d_jerk_v150_signal(netinc, assets, opinc, revenue, gp, marketcap):
    a = _f17_efficiency_ratio(netinc, assets, 252)
    b = _f17_efficiency_ratio(opinc, revenue, 252)
    c = _f17_turnover_rate(revenue, assets, 252)
    d = _f17_efficiency_ratio(gp, revenue, 252)
    base = (a + b + c + d) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17es_f17_efficiency_snapshot_at_21d_jerk_v001_signal,
    f17es_f17_efficiency_snapshot_at_21d_jerk_v002_signal,
    f17es_f17_efficiency_snapshot_at_63d_jerk_v003_signal,
    f17es_f17_efficiency_snapshot_at_63d_jerk_v004_signal,
    f17es_f17_efficiency_snapshot_at_126d_jerk_v005_signal,
    f17es_f17_efficiency_snapshot_at_252d_jerk_v006_signal,
    f17es_f17_efficiency_snapshot_at_504d_jerk_v007_signal,
    f17es_f17_efficiency_snapshot_eqt_21d_jerk_v008_signal,
    f17es_f17_efficiency_snapshot_eqt_252d_jerk_v009_signal,
    f17es_f17_efficiency_snapshot_eqt_504d_jerk_v010_signal,
    f17es_f17_efficiency_snapshot_wct_21d_jerk_v011_signal,
    f17es_f17_efficiency_snapshot_wct_252d_jerk_v012_signal,
    f17es_f17_efficiency_snapshot_wct_504d_jerk_v013_signal,
    f17es_f17_efficiency_snapshot_capa_21d_jerk_v014_signal,
    f17es_f17_efficiency_snapshot_capa_252d_jerk_v015_signal,
    f17es_f17_efficiency_snapshot_capa_504d_jerk_v016_signal,
    f17es_f17_efficiency_snapshot_capr_21d_jerk_v017_signal,
    f17es_f17_efficiency_snapshot_capr_252d_jerk_v018_signal,
    f17es_f17_efficiency_snapshot_roa_21d_jerk_v019_signal,
    f17es_f17_efficiency_snapshot_roa_21d_jerk_v020_signal,
    f17es_f17_efficiency_snapshot_roa_63d_jerk_v021_signal,
    f17es_f17_efficiency_snapshot_roa_252d_jerk_v022_signal,
    f17es_f17_efficiency_snapshot_roa_504d_jerk_v023_signal,
    f17es_f17_efficiency_snapshot_roe_21d_jerk_v024_signal,
    f17es_f17_efficiency_snapshot_roe_252d_jerk_v025_signal,
    f17es_f17_efficiency_snapshot_roe_504d_jerk_v026_signal,
    f17es_f17_efficiency_snapshot_roic_21d_jerk_v027_signal,
    f17es_f17_efficiency_snapshot_roic_252d_jerk_v028_signal,
    f17es_f17_efficiency_snapshot_roic_504d_jerk_v029_signal,
    f17es_f17_efficiency_snapshot_ccc_21d_jerk_v030_signal,
    f17es_f17_efficiency_snapshot_ccc_252d_jerk_v031_signal,
    f17es_f17_efficiency_snapshot_ccc_504d_jerk_v032_signal,
    f17es_f17_efficiency_snapshot_fcfquality_21d_jerk_v033_signal,
    f17es_f17_efficiency_snapshot_fcfquality_252d_jerk_v034_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_21d_jerk_v035_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_252d_jerk_v036_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_504d_jerk_v037_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_21d_jerk_v038_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_252d_jerk_v039_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_504d_jerk_v040_signal,
    f17es_f17_efficiency_snapshot_fcfassets_21d_jerk_v041_signal,
    f17es_f17_efficiency_snapshot_fcfassets_252d_jerk_v042_signal,
    f17es_f17_efficiency_snapshot_fcfassets_504d_jerk_v043_signal,
    f17es_f17_efficiency_snapshot_ncfoassets_21d_jerk_v044_signal,
    f17es_f17_efficiency_snapshot_ncfoassets_252d_jerk_v045_signal,
    f17es_f17_efficiency_snapshot_gm_21d_jerk_v046_signal,
    f17es_f17_efficiency_snapshot_gm_252d_jerk_v047_signal,
    f17es_f17_efficiency_snapshot_om_21d_jerk_v048_signal,
    f17es_f17_efficiency_snapshot_om_252d_jerk_v049_signal,
    f17es_f17_efficiency_snapshot_gpopinc_21d_jerk_v050_signal,
    f17es_f17_efficiency_snapshot_gpopinc_252d_jerk_v051_signal,
    f17es_f17_efficiency_snapshot_wcrev_21d_jerk_v052_signal,
    f17es_f17_efficiency_snapshot_wcrev_252d_jerk_v053_signal,
    f17es_f17_efficiency_snapshot_wcrev_504d_jerk_v054_signal,
    f17es_f17_efficiency_snapshot_wcassets_21d_jerk_v055_signal,
    f17es_f17_efficiency_snapshot_wcassets_252d_jerk_v056_signal,
    f17es_f17_efficiency_snapshot_revps_21d_jerk_v057_signal,
    f17es_f17_efficiency_snapshot_revps_252d_jerk_v058_signal,
    f17es_f17_efficiency_snapshot_ebitdaps_21d_jerk_v059_signal,
    f17es_f17_efficiency_snapshot_ebitdaps_252d_jerk_v060_signal,
    f17es_f17_efficiency_snapshot_gpps_21d_jerk_v061_signal,
    f17es_f17_efficiency_snapshot_gpps_252d_jerk_v062_signal,
    f17es_f17_efficiency_snapshot_gpa_252d_jerk_v063_signal,
    f17es_f17_efficiency_snapshot_roaz_252d_jerk_v064_signal,
    f17es_f17_efficiency_snapshot_roaz_504d_jerk_v065_signal,
    f17es_f17_efficiency_snapshot_roez_252d_jerk_v066_signal,
    f17es_f17_efficiency_snapshot_atz_252d_jerk_v067_signal,
    f17es_f17_efficiency_snapshot_gmz_252d_jerk_v068_signal,
    f17es_f17_efficiency_snapshot_omz_252d_jerk_v069_signal,
    f17es_f17_efficiency_snapshot_fcfmarginz_252d_jerk_v070_signal,
    f17es_f17_efficiency_snapshot_cccz_252d_jerk_v071_signal,
    f17es_f17_efficiency_snapshot_roicz_252d_jerk_v072_signal,
    f17es_f17_efficiency_snapshot_roadev_252d_jerk_v073_signal,
    f17es_f17_efficiency_snapshot_omdev_252d_jerk_v074_signal,
    f17es_f17_efficiency_snapshot_atdev_252d_jerk_v075_signal,
    f17es_f17_efficiency_snapshot_gmdev_252d_jerk_v076_signal,
    f17es_f17_efficiency_snapshot_roarelhi_504d_jerk_v077_signal,
    f17es_f17_efficiency_snapshot_omrelhi_504d_jerk_v078_signal,
    f17es_f17_efficiency_snapshot_atrelhi_504d_jerk_v079_signal,
    f17es_f17_efficiency_snapshot_roapos_504d_jerk_v080_signal,
    f17es_f17_efficiency_snapshot_ompos_504d_jerk_v081_signal,
    f17es_f17_efficiency_snapshot_atpos_504d_jerk_v082_signal,
    f17es_f17_efficiency_snapshot_highroa_count_252d_jerk_v083_signal,
    f17es_f17_efficiency_snapshot_highom_count_252d_jerk_v084_signal,
    f17es_f17_efficiency_snapshot_lowat_count_504d_jerk_v085_signal,
    f17es_f17_efficiency_snapshot_blendedeff_252d_jerk_v086_signal,
    f17es_f17_efficiency_snapshot_blendedmargin_252d_jerk_v087_signal,
    f17es_f17_efficiency_snapshot_roa_recent_vs_trend_jerk_v088_signal,
    f17es_f17_efficiency_snapshot_om_recent_vs_trend_jerk_v089_signal,
    f17es_f17_efficiency_snapshot_at_recent_vs_trend_jerk_v090_signal,
    f17es_f17_efficiency_snapshot_logroa_21d_jerk_v091_signal,
    f17es_f17_efficiency_snapshot_logroa_252d_jerk_v092_signal,
    f17es_f17_efficiency_snapshot_logom_252d_jerk_v093_signal,
    f17es_f17_efficiency_snapshot_logat_252d_jerk_v094_signal,
    f17es_f17_efficiency_snapshot_roasq_252d_jerk_v095_signal,
    f17es_f17_efficiency_snapshot_omsq_252d_jerk_v096_signal,
    f17es_f17_efficiency_snapshot_roa_ema_21d_jerk_v097_signal,
    f17es_f17_efficiency_snapshot_roa_ema_252d_jerk_v098_signal,
    f17es_f17_efficiency_snapshot_om_ema_252d_jerk_v099_signal,
    f17es_f17_efficiency_snapshot_at_ema_252d_jerk_v100_signal,
    f17es_f17_efficiency_snapshot_cashprod_21d_jerk_v101_signal,
    f17es_f17_efficiency_snapshot_cashprod_252d_jerk_v102_signal,
    f17es_f17_efficiency_snapshot_coreeff_21d_jerk_v103_signal,
    f17es_f17_efficiency_snapshot_coreeff_252d_jerk_v104_signal,
    f17es_f17_efficiency_snapshot_coreeff_504d_jerk_v105_signal,
    f17es_f17_efficiency_snapshot_retentionrev_21d_jerk_v106_signal,
    f17es_f17_efficiency_snapshot_retentionrev_252d_jerk_v107_signal,
    f17es_f17_efficiency_snapshot_retentionni_21d_jerk_v108_signal,
    f17es_f17_efficiency_snapshot_retentionni_252d_jerk_v109_signal,
    f17es_f17_efficiency_snapshot_revwc_21d_jerk_v110_signal,
    f17es_f17_efficiency_snapshot_revwc_252d_jerk_v111_signal,
    f17es_f17_efficiency_snapshot_revwc_504d_jerk_v112_signal,
    f17es_f17_efficiency_snapshot_ebitdaopinc_21d_jerk_v113_signal,
    f17es_f17_efficiency_snapshot_ebitdaopinc_252d_jerk_v114_signal,
    f17es_f17_efficiency_snapshot_ncfofcf_21d_jerk_v115_signal,
    f17es_f17_efficiency_snapshot_ncfofcf_252d_jerk_v116_signal,
    f17es_f17_efficiency_snapshot_capncfo_21d_jerk_v117_signal,
    f17es_f17_efficiency_snapshot_capncfo_252d_jerk_v118_signal,
    f17es_f17_efficiency_snapshot_capncfo_504d_jerk_v119_signal,
    f17es_f17_efficiency_snapshot_gpequity_21d_jerk_v120_signal,
    f17es_f17_efficiency_snapshot_gpequity_252d_jerk_v121_signal,
    f17es_f17_efficiency_snapshot_gpequity_504d_jerk_v122_signal,
    f17es_f17_efficiency_snapshot_opincassets_252d_jerk_v123_signal,
    f17es_f17_efficiency_snapshot_opincassets_504d_jerk_v124_signal,
    f17es_f17_efficiency_snapshot_opincequity_252d_jerk_v125_signal,
    f17es_f17_efficiency_snapshot_ebitdaequity_504d_jerk_v126_signal,
    f17es_f17_efficiency_snapshot_revliab_252d_jerk_v127_signal,
    f17es_f17_efficiency_snapshot_ebitdaliab_252d_jerk_v128_signal,
    f17es_f17_efficiency_snapshot_ncfoliab_252d_jerk_v129_signal,
    f17es_f17_efficiency_snapshot_capwc_252d_jerk_v130_signal,
    f17es_f17_efficiency_snapshot_dupont_252d_jerk_v131_signal,
    f17es_f17_efficiency_snapshot_dupontom_252d_jerk_v132_signal,
    f17es_f17_efficiency_snapshot_fulldupont_252d_jerk_v133_signal,
    f17es_f17_efficiency_snapshot_invest_eff_252d_jerk_v134_signal,
    f17es_f17_efficiency_snapshot_net_surplus_252d_jerk_v135_signal,
    f17es_f17_efficiency_snapshot_gpa_x_roe_252d_jerk_v136_signal,
    f17es_f17_efficiency_snapshot_revps_x_nips_252d_jerk_v137_signal,
    f17es_f17_efficiency_snapshot_fcfps_252d_jerk_v138_signal,
    f17es_f17_efficiency_snapshot_ncfops_252d_jerk_v139_signal,
    f17es_f17_efficiency_snapshot_opincps_252d_jerk_v140_signal,
    f17es_f17_efficiency_snapshot_sga_252d_jerk_v141_signal,
    f17es_f17_efficiency_snapshot_assetsrev_252d_jerk_v142_signal,
    f17es_f17_efficiency_snapshot_eqa_252d_jerk_v143_signal,
    f17es_f17_efficiency_snapshot_revwc_eff_504d_jerk_v144_signal,
    f17es_f17_efficiency_snapshot_ebitdamargin_252d_jerk_v145_signal,
    f17es_f17_efficiency_snapshot_nm_x_at_252d_jerk_v146_signal,
    f17es_f17_efficiency_snapshot_capebitda_252d_jerk_v147_signal,
    f17es_f17_efficiency_snapshot_netcash_a_252d_jerk_v148_signal,
    f17es_f17_efficiency_snapshot_combo_a_252d_jerk_v149_signal,
    f17es_f17_efficiency_snapshot_fullcomp_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_EFFICIENCY_SNAPSHOT_REGISTRY_JERK = REGISTRY


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
    print(f"OK f17_efficiency_snapshot_3rd_derivatives_001_150_claude: {n_features} features pass")
