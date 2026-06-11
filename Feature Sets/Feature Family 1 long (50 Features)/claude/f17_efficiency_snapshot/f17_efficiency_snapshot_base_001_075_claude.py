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


# ===== folder domain primitives =====
def _f17_efficiency_ratio(numerator, denominator, w):
    n = _mean(numerator, w)
    d = _mean(denominator, w)
    return n / d.replace(0, np.nan).abs()


def _f17_turnover_rate(flow, stock, w):
    f = _mean(flow, w)
    s = _mean(stock, w)
    return f / s.replace(0, np.nan).abs()


# 21d asset turnover: revenue / assets
def f17es_f17_efficiency_snapshot_at_21d_base_v001_signal(revenue, assets, marketcap):
    result = _f17_turnover_rate(revenue, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover
def f17es_f17_efficiency_snapshot_at_63d_base_v002_signal(revenue, assets, marketcap):
    result = _f17_turnover_rate(revenue, assets, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 126d asset turnover
def f17es_f17_efficiency_snapshot_at_126d_base_v003_signal(revenue, assets, marketcap):
    result = _f17_turnover_rate(revenue, assets, 126) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover
def f17es_f17_efficiency_snapshot_at_252d_base_v004_signal(revenue, assets, marketcap):
    result = _f17_turnover_rate(revenue, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d asset turnover
def f17es_f17_efficiency_snapshot_at_504d_base_v005_signal(revenue, assets, marketcap):
    result = _f17_turnover_rate(revenue, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d equity turnover: revenue / equity
def f17es_f17_efficiency_snapshot_eqt_21d_base_v006_signal(revenue, equity, marketcap):
    result = _f17_turnover_rate(revenue, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity turnover
def f17es_f17_efficiency_snapshot_eqt_63d_base_v007_signal(revenue, equity, marketcap):
    result = _f17_turnover_rate(revenue, equity, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity turnover
def f17es_f17_efficiency_snapshot_eqt_252d_base_v008_signal(revenue, equity, marketcap):
    result = _f17_turnover_rate(revenue, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d equity turnover
def f17es_f17_efficiency_snapshot_eqt_504d_base_v009_signal(revenue, equity, marketcap):
    result = _f17_turnover_rate(revenue, equity, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d wc turnover: revenue / workingcapital
def f17es_f17_efficiency_snapshot_wct_21d_base_v010_signal(revenue, workingcapital, marketcap):
    result = _f17_turnover_rate(revenue, workingcapital, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d wc turnover
def f17es_f17_efficiency_snapshot_wct_63d_base_v011_signal(revenue, workingcapital, marketcap):
    result = _f17_turnover_rate(revenue, workingcapital, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d wc turnover
def f17es_f17_efficiency_snapshot_wct_252d_base_v012_signal(revenue, workingcapital, marketcap):
    result = _f17_turnover_rate(revenue, workingcapital, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d wc turnover
def f17es_f17_efficiency_snapshot_wct_504d_base_v013_signal(revenue, workingcapital, marketcap):
    result = _f17_turnover_rate(revenue, workingcapital, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex / assets - capital intensity
def f17es_f17_efficiency_snapshot_capa_21d_base_v014_signal(capex, assets, marketcap):
    result = _f17_efficiency_ratio(capex, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex / assets
def f17es_f17_efficiency_snapshot_capa_63d_base_v015_signal(capex, assets, marketcap):
    result = _f17_efficiency_ratio(capex, assets, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / assets
def f17es_f17_efficiency_snapshot_capa_252d_base_v016_signal(capex, assets, marketcap):
    result = _f17_efficiency_ratio(capex, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex / assets
def f17es_f17_efficiency_snapshot_capa_504d_base_v017_signal(capex, assets, marketcap):
    result = _f17_efficiency_ratio(capex, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex / revenue
def f17es_f17_efficiency_snapshot_capr_21d_base_v018_signal(capex, revenue, marketcap):
    result = _f17_efficiency_ratio(capex, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex / revenue
def f17es_f17_efficiency_snapshot_capr_63d_base_v019_signal(capex, revenue, marketcap):
    result = _f17_efficiency_ratio(capex, revenue, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / revenue
def f17es_f17_efficiency_snapshot_capr_252d_base_v020_signal(capex, revenue, marketcap):
    result = _f17_efficiency_ratio(capex, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROA: netinc / assets (efficiency of capital)
def f17es_f17_efficiency_snapshot_roa_21d_base_v021_signal(netinc, assets, marketcap):
    result = _f17_efficiency_ratio(netinc, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROA
def f17es_f17_efficiency_snapshot_roa_63d_base_v022_signal(netinc, assets, marketcap):
    result = _f17_efficiency_ratio(netinc, assets, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA
def f17es_f17_efficiency_snapshot_roa_252d_base_v023_signal(netinc, assets, marketcap):
    result = _f17_efficiency_ratio(netinc, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROA
def f17es_f17_efficiency_snapshot_roa_504d_base_v024_signal(netinc, assets, marketcap):
    result = _f17_efficiency_ratio(netinc, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE: netinc / equity
def f17es_f17_efficiency_snapshot_roe_21d_base_v025_signal(netinc, equity, marketcap):
    result = _f17_efficiency_ratio(netinc, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE
def f17es_f17_efficiency_snapshot_roe_63d_base_v026_signal(netinc, equity, marketcap):
    result = _f17_efficiency_ratio(netinc, equity, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE
def f17es_f17_efficiency_snapshot_roe_252d_base_v027_signal(netinc, equity, marketcap):
    result = _f17_efficiency_ratio(netinc, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROE
def f17es_f17_efficiency_snapshot_roe_504d_base_v028_signal(netinc, equity, marketcap):
    result = _f17_efficiency_ratio(netinc, equity, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROIC proxy: opinc / (equity + debt)
def f17es_f17_efficiency_snapshot_roic_21d_base_v029_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    result = _f17_efficiency_ratio(opinc, cap, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROIC
def f17es_f17_efficiency_snapshot_roic_63d_base_v030_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    result = _f17_efficiency_ratio(opinc, cap, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROIC
def f17es_f17_efficiency_snapshot_roic_252d_base_v031_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    result = _f17_efficiency_ratio(opinc, cap, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROIC
def f17es_f17_efficiency_snapshot_roic_504d_base_v032_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    result = _f17_efficiency_ratio(opinc, cap, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash conversion: ncfo / netinc
def f17es_f17_efficiency_snapshot_ccc_21d_base_v033_signal(ncfo, netinc, marketcap):
    result = _f17_efficiency_ratio(ncfo, netinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash conversion
def f17es_f17_efficiency_snapshot_ccc_63d_base_v034_signal(ncfo, netinc, marketcap):
    result = _f17_efficiency_ratio(ncfo, netinc, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash conversion
def f17es_f17_efficiency_snapshot_ccc_252d_base_v035_signal(ncfo, netinc, marketcap):
    result = _f17_efficiency_ratio(ncfo, netinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash conversion
def f17es_f17_efficiency_snapshot_ccc_504d_base_v036_signal(ncfo, netinc, marketcap):
    result = _f17_efficiency_ratio(ncfo, netinc, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF / netinc cash quality
def f17es_f17_efficiency_snapshot_fcfquality_21d_base_v037_signal(fcf, netinc, marketcap):
    result = _f17_efficiency_ratio(fcf, netinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF / netinc
def f17es_f17_efficiency_snapshot_fcfquality_63d_base_v038_signal(fcf, netinc, marketcap):
    result = _f17_efficiency_ratio(fcf, netinc, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF / netinc
def f17es_f17_efficiency_snapshot_fcfquality_252d_base_v039_signal(fcf, netinc, marketcap):
    result = _f17_efficiency_ratio(fcf, netinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF / revenue (margin)
def f17es_f17_efficiency_snapshot_fcfmargin_21d_base_v040_signal(fcf, revenue, marketcap):
    result = _f17_efficiency_ratio(fcf, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF / revenue
def f17es_f17_efficiency_snapshot_fcfmargin_63d_base_v041_signal(fcf, revenue, marketcap):
    result = _f17_efficiency_ratio(fcf, revenue, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF / revenue
def f17es_f17_efficiency_snapshot_fcfmargin_252d_base_v042_signal(fcf, revenue, marketcap):
    result = _f17_efficiency_ratio(fcf, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF / revenue
def f17es_f17_efficiency_snapshot_fcfmargin_504d_base_v043_signal(fcf, revenue, marketcap):
    result = _f17_efficiency_ratio(fcf, revenue, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EBITDA / assets - asset productivity
def f17es_f17_efficiency_snapshot_ebitdaassets_21d_base_v044_signal(ebitda, assets, marketcap):
    result = _f17_efficiency_ratio(ebitda, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EBITDA / assets
def f17es_f17_efficiency_snapshot_ebitdaassets_63d_base_v045_signal(ebitda, assets, marketcap):
    result = _f17_efficiency_ratio(ebitda, assets, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EBITDA / assets
def f17es_f17_efficiency_snapshot_ebitdaassets_252d_base_v046_signal(ebitda, assets, marketcap):
    result = _f17_efficiency_ratio(ebitda, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EBITDA / assets
def f17es_f17_efficiency_snapshot_ebitdaassets_504d_base_v047_signal(ebitda, assets, marketcap):
    result = _f17_efficiency_ratio(ebitda, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF / assets
def f17es_f17_efficiency_snapshot_fcfassets_21d_base_v048_signal(fcf, assets, marketcap):
    result = _f17_efficiency_ratio(fcf, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF / assets
def f17es_f17_efficiency_snapshot_fcfassets_252d_base_v049_signal(fcf, assets, marketcap):
    result = _f17_efficiency_ratio(fcf, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF / assets
def f17es_f17_efficiency_snapshot_fcfassets_504d_base_v050_signal(fcf, assets, marketcap):
    result = _f17_efficiency_ratio(fcf, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d NCFO / assets
def f17es_f17_efficiency_snapshot_ncfoassets_21d_base_v051_signal(ncfo, assets, marketcap):
    result = _f17_efficiency_ratio(ncfo, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO / assets
def f17es_f17_efficiency_snapshot_ncfoassets_252d_base_v052_signal(ncfo, assets, marketcap):
    result = _f17_efficiency_ratio(ncfo, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gross margin: gp / revenue
def f17es_f17_efficiency_snapshot_gm_21d_base_v053_signal(gp, revenue, marketcap):
    result = _f17_efficiency_ratio(gp, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross margin
def f17es_f17_efficiency_snapshot_gm_63d_base_v054_signal(gp, revenue, marketcap):
    result = _f17_efficiency_ratio(gp, revenue, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin
def f17es_f17_efficiency_snapshot_gm_252d_base_v055_signal(gp, revenue, marketcap):
    result = _f17_efficiency_ratio(gp, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d operating margin: opinc / revenue
def f17es_f17_efficiency_snapshot_om_21d_base_v056_signal(opinc, revenue, marketcap):
    result = _f17_efficiency_ratio(opinc, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin
def f17es_f17_efficiency_snapshot_om_63d_base_v057_signal(opinc, revenue, marketcap):
    result = _f17_efficiency_ratio(opinc, revenue, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin
def f17es_f17_efficiency_snapshot_om_252d_base_v058_signal(opinc, revenue, marketcap):
    result = _f17_efficiency_ratio(opinc, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gp / opinc - operating leverage proxy
def f17es_f17_efficiency_snapshot_gpopinc_21d_base_v059_signal(gp, opinc, marketcap):
    result = _f17_efficiency_ratio(gp, opinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp / opinc
def f17es_f17_efficiency_snapshot_gpopinc_63d_base_v060_signal(gp, opinc, marketcap):
    result = _f17_efficiency_ratio(gp, opinc, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp / opinc
def f17es_f17_efficiency_snapshot_gpopinc_252d_base_v061_signal(gp, opinc, marketcap):
    result = _f17_efficiency_ratio(gp, opinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d wc / revenue (working capital efficiency)
def f17es_f17_efficiency_snapshot_wcrev_21d_base_v062_signal(workingcapital, revenue, marketcap):
    result = _f17_efficiency_ratio(workingcapital, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d wc / revenue
def f17es_f17_efficiency_snapshot_wcrev_63d_base_v063_signal(workingcapital, revenue, marketcap):
    result = _f17_efficiency_ratio(workingcapital, revenue, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d wc / revenue
def f17es_f17_efficiency_snapshot_wcrev_252d_base_v064_signal(workingcapital, revenue, marketcap):
    result = _f17_efficiency_ratio(workingcapital, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d wc / revenue
def f17es_f17_efficiency_snapshot_wcrev_504d_base_v065_signal(workingcapital, revenue, marketcap):
    result = _f17_efficiency_ratio(workingcapital, revenue, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d wc / assets
def f17es_f17_efficiency_snapshot_wcassets_21d_base_v066_signal(workingcapital, assets, marketcap):
    result = _f17_efficiency_ratio(workingcapital, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d wc / assets
def f17es_f17_efficiency_snapshot_wcassets_252d_base_v067_signal(workingcapital, assets, marketcap):
    result = _f17_efficiency_ratio(workingcapital, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d wc / assets
def f17es_f17_efficiency_snapshot_wcassets_504d_base_v068_signal(workingcapital, assets, marketcap):
    result = _f17_efficiency_ratio(workingcapital, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sales per share: revenue / sharesbas (efficiency per share)
def f17es_f17_efficiency_snapshot_revps_21d_base_v069_signal(revenue, sharesbas, marketcap):
    result = _f17_efficiency_ratio(revenue, sharesbas, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sales per share
def f17es_f17_efficiency_snapshot_revps_252d_base_v070_signal(revenue, sharesbas, marketcap):
    result = _f17_efficiency_ratio(revenue, sharesbas, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda per share
def f17es_f17_efficiency_snapshot_ebitdaps_21d_base_v071_signal(ebitda, sharesbas, marketcap):
    result = _f17_efficiency_ratio(ebitda, sharesbas, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda per share
def f17es_f17_efficiency_snapshot_ebitdaps_252d_base_v072_signal(ebitda, sharesbas, marketcap):
    result = _f17_efficiency_ratio(ebitda, sharesbas, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gp per share
def f17es_f17_efficiency_snapshot_gpps_21d_base_v073_signal(gp, sharesbas, marketcap):
    result = _f17_efficiency_ratio(gp, sharesbas, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp per share
def f17es_f17_efficiency_snapshot_gpps_252d_base_v074_signal(gp, sharesbas, marketcap):
    result = _f17_efficiency_ratio(gp, sharesbas, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp per asset (gross profit asset productivity)
def f17es_f17_efficiency_snapshot_gpa_252d_base_v075_signal(gp, assets, marketcap):
    result = _f17_efficiency_ratio(gp, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17es_f17_efficiency_snapshot_at_21d_base_v001_signal,
    f17es_f17_efficiency_snapshot_at_63d_base_v002_signal,
    f17es_f17_efficiency_snapshot_at_126d_base_v003_signal,
    f17es_f17_efficiency_snapshot_at_252d_base_v004_signal,
    f17es_f17_efficiency_snapshot_at_504d_base_v005_signal,
    f17es_f17_efficiency_snapshot_eqt_21d_base_v006_signal,
    f17es_f17_efficiency_snapshot_eqt_63d_base_v007_signal,
    f17es_f17_efficiency_snapshot_eqt_252d_base_v008_signal,
    f17es_f17_efficiency_snapshot_eqt_504d_base_v009_signal,
    f17es_f17_efficiency_snapshot_wct_21d_base_v010_signal,
    f17es_f17_efficiency_snapshot_wct_63d_base_v011_signal,
    f17es_f17_efficiency_snapshot_wct_252d_base_v012_signal,
    f17es_f17_efficiency_snapshot_wct_504d_base_v013_signal,
    f17es_f17_efficiency_snapshot_capa_21d_base_v014_signal,
    f17es_f17_efficiency_snapshot_capa_63d_base_v015_signal,
    f17es_f17_efficiency_snapshot_capa_252d_base_v016_signal,
    f17es_f17_efficiency_snapshot_capa_504d_base_v017_signal,
    f17es_f17_efficiency_snapshot_capr_21d_base_v018_signal,
    f17es_f17_efficiency_snapshot_capr_63d_base_v019_signal,
    f17es_f17_efficiency_snapshot_capr_252d_base_v020_signal,
    f17es_f17_efficiency_snapshot_roa_21d_base_v021_signal,
    f17es_f17_efficiency_snapshot_roa_63d_base_v022_signal,
    f17es_f17_efficiency_snapshot_roa_252d_base_v023_signal,
    f17es_f17_efficiency_snapshot_roa_504d_base_v024_signal,
    f17es_f17_efficiency_snapshot_roe_21d_base_v025_signal,
    f17es_f17_efficiency_snapshot_roe_63d_base_v026_signal,
    f17es_f17_efficiency_snapshot_roe_252d_base_v027_signal,
    f17es_f17_efficiency_snapshot_roe_504d_base_v028_signal,
    f17es_f17_efficiency_snapshot_roic_21d_base_v029_signal,
    f17es_f17_efficiency_snapshot_roic_63d_base_v030_signal,
    f17es_f17_efficiency_snapshot_roic_252d_base_v031_signal,
    f17es_f17_efficiency_snapshot_roic_504d_base_v032_signal,
    f17es_f17_efficiency_snapshot_ccc_21d_base_v033_signal,
    f17es_f17_efficiency_snapshot_ccc_63d_base_v034_signal,
    f17es_f17_efficiency_snapshot_ccc_252d_base_v035_signal,
    f17es_f17_efficiency_snapshot_ccc_504d_base_v036_signal,
    f17es_f17_efficiency_snapshot_fcfquality_21d_base_v037_signal,
    f17es_f17_efficiency_snapshot_fcfquality_63d_base_v038_signal,
    f17es_f17_efficiency_snapshot_fcfquality_252d_base_v039_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_21d_base_v040_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_63d_base_v041_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_252d_base_v042_signal,
    f17es_f17_efficiency_snapshot_fcfmargin_504d_base_v043_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_21d_base_v044_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_63d_base_v045_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_252d_base_v046_signal,
    f17es_f17_efficiency_snapshot_ebitdaassets_504d_base_v047_signal,
    f17es_f17_efficiency_snapshot_fcfassets_21d_base_v048_signal,
    f17es_f17_efficiency_snapshot_fcfassets_252d_base_v049_signal,
    f17es_f17_efficiency_snapshot_fcfassets_504d_base_v050_signal,
    f17es_f17_efficiency_snapshot_ncfoassets_21d_base_v051_signal,
    f17es_f17_efficiency_snapshot_ncfoassets_252d_base_v052_signal,
    f17es_f17_efficiency_snapshot_gm_21d_base_v053_signal,
    f17es_f17_efficiency_snapshot_gm_63d_base_v054_signal,
    f17es_f17_efficiency_snapshot_gm_252d_base_v055_signal,
    f17es_f17_efficiency_snapshot_om_21d_base_v056_signal,
    f17es_f17_efficiency_snapshot_om_63d_base_v057_signal,
    f17es_f17_efficiency_snapshot_om_252d_base_v058_signal,
    f17es_f17_efficiency_snapshot_gpopinc_21d_base_v059_signal,
    f17es_f17_efficiency_snapshot_gpopinc_63d_base_v060_signal,
    f17es_f17_efficiency_snapshot_gpopinc_252d_base_v061_signal,
    f17es_f17_efficiency_snapshot_wcrev_21d_base_v062_signal,
    f17es_f17_efficiency_snapshot_wcrev_63d_base_v063_signal,
    f17es_f17_efficiency_snapshot_wcrev_252d_base_v064_signal,
    f17es_f17_efficiency_snapshot_wcrev_504d_base_v065_signal,
    f17es_f17_efficiency_snapshot_wcassets_21d_base_v066_signal,
    f17es_f17_efficiency_snapshot_wcassets_252d_base_v067_signal,
    f17es_f17_efficiency_snapshot_wcassets_504d_base_v068_signal,
    f17es_f17_efficiency_snapshot_revps_21d_base_v069_signal,
    f17es_f17_efficiency_snapshot_revps_252d_base_v070_signal,
    f17es_f17_efficiency_snapshot_ebitdaps_21d_base_v071_signal,
    f17es_f17_efficiency_snapshot_ebitdaps_252d_base_v072_signal,
    f17es_f17_efficiency_snapshot_gpps_21d_base_v073_signal,
    f17es_f17_efficiency_snapshot_gpps_252d_base_v074_signal,
    f17es_f17_efficiency_snapshot_gpa_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_EFFICIENCY_SNAPSHOT_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_efficiency_snapshot_base_001_075_claude: {n_features} features pass")
