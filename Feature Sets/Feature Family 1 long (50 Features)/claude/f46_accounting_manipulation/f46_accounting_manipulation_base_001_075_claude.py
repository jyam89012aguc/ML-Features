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
def _f46_accounting_manip_earnings_fcf_gap(netinc, fcf):
    return (netinc - fcf) / netinc.abs().replace(0, np.nan)


def _f46_accounting_manip_accruals_quality(netinc, ncfo, assets):
    return (netinc - ncfo) / assets.abs().replace(0, np.nan)


def _f46_accounting_manip_ni_minus_ncfo(netinc, ncfo):
    return netinc - ncfo


# 21d earnings vs FCF gap × marketcap
def f46am_f46_accounting_manipulation_earnfcf_21d_base_v001_signal(netinc, fcf, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d earnings vs FCF gap × marketcap
def f46am_f46_accounting_manipulation_earnfcf_63d_base_v002_signal(netinc, fcf, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings vs FCF gap × marketcap
def f46am_f46_accounting_manipulation_earnfcf_252d_base_v003_signal(netinc, fcf, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d earnings vs FCF gap × marketcap
def f46am_f46_accounting_manipulation_earnfcf_504d_base_v004_signal(netinc, fcf, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accruals quality × marketcap
def f46am_f46_accounting_manipulation_accruals_21d_base_v005_signal(netinc, ncfo, assets, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accruals quality × marketcap
def f46am_f46_accounting_manipulation_accruals_63d_base_v006_signal(netinc, ncfo, assets, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals quality × marketcap
def f46am_f46_accounting_manipulation_accruals_252d_base_v007_signal(netinc, ncfo, assets, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals quality × marketcap
def f46am_f46_accounting_manipulation_accruals_504d_base_v008_signal(netinc, ncfo, assets, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d NI minus NCFO × marketcap
def f46am_f46_accounting_manipulation_nimncfo_21d_base_v009_signal(netinc, ncfo, marketcap):
    result = _mean(_f46_accounting_manip_ni_minus_ncfo(netinc, ncfo), 21) / marketcap.replace(0, np.nan).abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NI minus NCFO × marketcap
def f46am_f46_accounting_manipulation_nimncfo_63d_base_v010_signal(netinc, ncfo, marketcap):
    result = _mean(_f46_accounting_manip_ni_minus_ncfo(netinc, ncfo), 63) / marketcap.replace(0, np.nan).abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NI minus NCFO × marketcap
def f46am_f46_accounting_manipulation_nimncfo_252d_base_v011_signal(netinc, ncfo, marketcap):
    result = _mean(_f46_accounting_manip_ni_minus_ncfo(netinc, ncfo), 252) / marketcap.replace(0, np.nan).abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d NI minus NCFO × marketcap
def f46am_f46_accounting_manipulation_nimncfo_504d_base_v012_signal(netinc, ncfo, marketcap):
    result = _mean(_f46_accounting_manip_ni_minus_ncfo(netinc, ncfo), 504) / marketcap.replace(0, np.nan).abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × ev
def f46am_f46_accounting_manipulation_earnfcf_xev_252d_base_v013_signal(netinc, fcf, ev):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d earnings-fcf gap × ev
def f46am_f46_accounting_manipulation_earnfcf_xev_504d_base_v014_signal(netinc, fcf, ev):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals × ev
def f46am_f46_accounting_manipulation_accxev_252d_base_v015_signal(netinc, ncfo, assets, ev):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals × ev
def f46am_f46_accounting_manipulation_accxev_504d_base_v016_signal(netinc, ncfo, assets, ev):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap z-score × marketcap
def f46am_f46_accounting_manipulation_earnfcfz_252d_base_v017_signal(netinc, fcf, marketcap):
    result = _z(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d earnings-fcf gap z-score × marketcap
def f46am_f46_accounting_manipulation_earnfcfz_504d_base_v018_signal(netinc, fcf, marketcap):
    result = _z(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals z × marketcap
def f46am_f46_accounting_manipulation_accz_252d_base_v019_signal(netinc, ncfo, assets, marketcap):
    result = _z(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals z × marketcap
def f46am_f46_accounting_manipulation_accz_504d_base_v020_signal(netinc, ncfo, assets, marketcap):
    result = _z(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d earnings-fcf gap × pe (rich-mispriced)
def f46am_f46_accounting_manipulation_earnfcfxpe_21d_base_v021_signal(netinc, fcf, pe, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 21) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × pe
def f46am_f46_accounting_manipulation_earnfcfxpe_252d_base_v022_signal(netinc, fcf, pe, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d earnings-fcf gap × pe
def f46am_f46_accounting_manipulation_earnfcfxpe_504d_base_v023_signal(netinc, fcf, pe, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 504) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals × pe
def f46am_f46_accounting_manipulation_accxpe_252d_base_v024_signal(netinc, ncfo, assets, pe, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals × pe
def f46am_f46_accounting_manipulation_accxpe_504d_base_v025_signal(netinc, ncfo, assets, pe, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 504) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × pb
def f46am_f46_accounting_manipulation_earnfcfxpb_252d_base_v026_signal(netinc, fcf, pb, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals × pb
def f46am_f46_accounting_manipulation_accxpb_252d_base_v027_signal(netinc, ncfo, assets, pb, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × ps
def f46am_f46_accounting_manipulation_earnfcfxps_252d_base_v028_signal(netinc, fcf, ps, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals × ps
def f46am_f46_accounting_manipulation_accxps_252d_base_v029_signal(netinc, ncfo, assets, ps, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × evebit
def f46am_f46_accounting_manipulation_earnfcfxevebit_252d_base_v030_signal(netinc, fcf, evebit, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × evebitda
def f46am_f46_accounting_manipulation_earnfcfxevebitda_252d_base_v031_signal(netinc, fcf, evebitda, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals × evebit
def f46am_f46_accounting_manipulation_accxevebit_252d_base_v032_signal(netinc, ncfo, assets, evebit, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals × evebitda
def f46am_f46_accounting_manipulation_accxevebitda_252d_base_v033_signal(netinc, ncfo, assets, evebitda, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × sf3a value (smart money flag)
def f46am_f46_accounting_manipulation_earnfcfxsf3a_252d_base_v034_signal(netinc, fcf, sf3a_value):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * _mean(sf3a_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals × sf3b value
def f46am_f46_accounting_manipulation_accxsf3b_252d_base_v035_signal(netinc, ncfo, assets, sf3b_value):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * _mean(sf3b_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × log marketcap
def f46am_f46_accounting_manipulation_earnfcfxlogmc_252d_base_v036_signal(netinc, fcf, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * np.log(marketcap.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals × log marketcap
def f46am_f46_accounting_manipulation_accxlogmc_252d_base_v037_signal(netinc, ncfo, assets, marketcap):
    result = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252) * np.log(marketcap.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × log ev
def f46am_f46_accounting_manipulation_earnfcfxlogev_252d_base_v038_signal(netinc, fcf, ev, marketcap):
    result = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252) * np.log(ev.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d earnings-fcf gap squared × marketcap (severity emphasis)
def f46am_f46_accounting_manipulation_earnfcfsq_21d_base_v039_signal(netinc, fcf, marketcap):
    g = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 21)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap squared × marketcap
def f46am_f46_accounting_manipulation_earnfcfsq_252d_base_v040_signal(netinc, fcf, marketcap):
    g = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d earnings-fcf gap squared × marketcap
def f46am_f46_accounting_manipulation_earnfcfsq_504d_base_v041_signal(netinc, fcf, marketcap):
    g = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 504)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals squared × marketcap
def f46am_f46_accounting_manipulation_accsq_252d_base_v042_signal(netinc, ncfo, assets, marketcap):
    a = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252)
    result = a * a.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals squared × marketcap
def f46am_f46_accounting_manipulation_accsq_504d_base_v043_signal(netinc, ncfo, assets, marketcap):
    a = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 504)
    result = a * a.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d earnings-fcf gap EWM × marketcap
def f46am_f46_accounting_manipulation_earnfcfewm_63d_base_v044_signal(netinc, fcf, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = g.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap EWM × marketcap
def f46am_f46_accounting_manipulation_earnfcfewm_252d_base_v045_signal(netinc, fcf, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = g.ewm(span=126, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d earnings-fcf gap EWM × marketcap
def f46am_f46_accounting_manipulation_earnfcfewm_504d_base_v046_signal(netinc, fcf, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = g.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals EWM × marketcap
def f46am_f46_accounting_manipulation_accewm_252d_base_v047_signal(netinc, ncfo, assets, marketcap):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = a.ewm(span=126, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals EWM × marketcap
def f46am_f46_accounting_manipulation_accewm_504d_base_v048_signal(netinc, ncfo, assets, marketcap):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = a.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d NI minus NCFO scaled by ev
def f46am_f46_accounting_manipulation_nimnxev_21d_base_v049_signal(netinc, ncfo, ev):
    g = _f46_accounting_manip_ni_minus_ncfo(netinc, ncfo)
    result = _mean(g, 21) / ev.replace(0, np.nan).abs() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NI minus NCFO scaled by ev
def f46am_f46_accounting_manipulation_nimnxev_252d_base_v050_signal(netinc, ncfo, ev):
    g = _f46_accounting_manip_ni_minus_ncfo(netinc, ncfo)
    result = _mean(g, 252) / ev.replace(0, np.nan).abs() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d NI minus NCFO scaled by ev
def f46am_f46_accounting_manipulation_nimnxev_504d_base_v051_signal(netinc, ncfo, ev):
    g = _f46_accounting_manip_ni_minus_ncfo(netinc, ncfo)
    result = _mean(g, 504) / ev.replace(0, np.nan).abs() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d earnings-fcf gap × log ev
def f46am_f46_accounting_manipulation_earnfcfxlogev_21d_base_v052_signal(netinc, fcf, ev, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 21) * np.log(ev.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals × log ev
def f46am_f46_accounting_manipulation_accxlogev_504d_base_v053_signal(netinc, ncfo, assets, ev, marketcap):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = _mean(a, 504) * np.log(ev.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × marketcap × ev composite (manipulation premium)
def f46am_f46_accounting_manipulation_efgxmcxev_252d_base_v054_signal(netinc, fcf, marketcap, ev):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 252) * marketcap * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals × marketcap × ev composite
def f46am_f46_accounting_manipulation_accxmcxev_504d_base_v055_signal(netinc, ncfo, assets, marketcap, ev):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = _mean(a, 504) * marketcap * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × debt (debt-fueled accruals)
def f46am_f46_accounting_manipulation_earnfcfxdebt_252d_base_v056_signal(netinc, fcf, debt, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 252) * debt * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals × debt
def f46am_f46_accounting_manipulation_accxdebt_504d_base_v057_signal(netinc, ncfo, assets, debt, marketcap):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = _mean(a, 504) * debt * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap std × marketcap (volatile accruals)
def f46am_f46_accounting_manipulation_earnfcfstd_252d_base_v058_signal(netinc, fcf, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _std(g, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d earnings-fcf gap std × marketcap
def f46am_f46_accounting_manipulation_earnfcfstd_504d_base_v059_signal(netinc, fcf, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _std(g, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals std × marketcap
def f46am_f46_accounting_manipulation_accstd_252d_base_v060_signal(netinc, ncfo, assets, marketcap):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = _std(a, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals std × marketcap
def f46am_f46_accounting_manipulation_accstd_504d_base_v061_signal(netinc, ncfo, assets, marketcap):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = _std(a, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap mean × ev × marketcap (super manipulation)
def f46am_f46_accounting_manipulation_supermanip_252d_base_v062_signal(netinc, fcf, ev, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 252) * np.sqrt(ev.abs() * marketcap.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals × sqrt(mc * ev)
def f46am_f46_accounting_manipulation_accxsqrt_504d_base_v063_signal(netinc, ncfo, assets, marketcap, ev):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = _mean(a, 504) * np.sqrt(marketcap.abs() * ev.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite manipulation: earnings-fcf gap × accruals × marketcap
def f46am_f46_accounting_manipulation_compmanip_252d_base_v064_signal(netinc, fcf, ncfo, assets, marketcap):
    g = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 252)
    a = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 252)
    result = g * a * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite manipulation × ev
def f46am_f46_accounting_manipulation_compmanip_504d_base_v065_signal(netinc, fcf, ncfo, assets, ev):
    g = _mean(_f46_accounting_manip_earnings_fcf_gap(netinc, fcf), 504)
    a = _mean(_f46_accounting_manip_accruals_quality(netinc, ncfo, assets), 504)
    result = g * a * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × sf3a shares mean
def f46am_f46_accounting_manipulation_earnfcfxsf3ash_252d_base_v066_signal(netinc, fcf, sf3a_shares):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 252) * _mean(sf3a_shares, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals × sf3b shares mean
def f46am_f46_accounting_manipulation_accxsf3bsh_504d_base_v067_signal(netinc, ncfo, assets, sf3b_shares):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = _mean(a, 504) * _mean(sf3b_shares, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d earnings-fcf gap × revenue
def f46am_f46_accounting_manipulation_earnfcfxrev_21d_base_v068_signal(netinc, fcf, revenue, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 21) * revenue * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × revenue
def f46am_f46_accounting_manipulation_earnfcfxrev_252d_base_v069_signal(netinc, fcf, revenue, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 252) * revenue * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d earnings-fcf gap × revenue
def f46am_f46_accounting_manipulation_earnfcfxrev_504d_base_v070_signal(netinc, fcf, revenue, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 504) * revenue * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accruals × revenue × marketcap
def f46am_f46_accounting_manipulation_accxrev_252d_base_v071_signal(netinc, ncfo, assets, revenue, marketcap):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = _mean(a, 252) * revenue * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × ebitda × marketcap
def f46am_f46_accounting_manipulation_earnfcfxeb_252d_base_v072_signal(netinc, fcf, ebitda, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 252) * ebitda * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accruals × opinc × marketcap
def f46am_f46_accounting_manipulation_accxop_504d_base_v073_signal(netinc, ncfo, assets, opinc, marketcap):
    a = _f46_accounting_manip_accruals_quality(netinc, ncfo, assets)
    result = _mean(a, 504) * opinc * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × evebit × marketcap (rich-mispriced)
def f46am_f46_accounting_manipulation_earnfcfxevebit_504d_base_v074_signal(netinc, fcf, evebit, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 504) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings-fcf gap × evebitda
def f46am_f46_accounting_manipulation_earnfcfxevebitda_504d_base_v075_signal(netinc, fcf, evebitda, marketcap):
    g = _f46_accounting_manip_earnings_fcf_gap(netinc, fcf)
    result = _mean(g, 504) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46am_f46_accounting_manipulation_earnfcf_21d_base_v001_signal,
    f46am_f46_accounting_manipulation_earnfcf_63d_base_v002_signal,
    f46am_f46_accounting_manipulation_earnfcf_252d_base_v003_signal,
    f46am_f46_accounting_manipulation_earnfcf_504d_base_v004_signal,
    f46am_f46_accounting_manipulation_accruals_21d_base_v005_signal,
    f46am_f46_accounting_manipulation_accruals_63d_base_v006_signal,
    f46am_f46_accounting_manipulation_accruals_252d_base_v007_signal,
    f46am_f46_accounting_manipulation_accruals_504d_base_v008_signal,
    f46am_f46_accounting_manipulation_nimncfo_21d_base_v009_signal,
    f46am_f46_accounting_manipulation_nimncfo_63d_base_v010_signal,
    f46am_f46_accounting_manipulation_nimncfo_252d_base_v011_signal,
    f46am_f46_accounting_manipulation_nimncfo_504d_base_v012_signal,
    f46am_f46_accounting_manipulation_earnfcf_xev_252d_base_v013_signal,
    f46am_f46_accounting_manipulation_earnfcf_xev_504d_base_v014_signal,
    f46am_f46_accounting_manipulation_accxev_252d_base_v015_signal,
    f46am_f46_accounting_manipulation_accxev_504d_base_v016_signal,
    f46am_f46_accounting_manipulation_earnfcfz_252d_base_v017_signal,
    f46am_f46_accounting_manipulation_earnfcfz_504d_base_v018_signal,
    f46am_f46_accounting_manipulation_accz_252d_base_v019_signal,
    f46am_f46_accounting_manipulation_accz_504d_base_v020_signal,
    f46am_f46_accounting_manipulation_earnfcfxpe_21d_base_v021_signal,
    f46am_f46_accounting_manipulation_earnfcfxpe_252d_base_v022_signal,
    f46am_f46_accounting_manipulation_earnfcfxpe_504d_base_v023_signal,
    f46am_f46_accounting_manipulation_accxpe_252d_base_v024_signal,
    f46am_f46_accounting_manipulation_accxpe_504d_base_v025_signal,
    f46am_f46_accounting_manipulation_earnfcfxpb_252d_base_v026_signal,
    f46am_f46_accounting_manipulation_accxpb_252d_base_v027_signal,
    f46am_f46_accounting_manipulation_earnfcfxps_252d_base_v028_signal,
    f46am_f46_accounting_manipulation_accxps_252d_base_v029_signal,
    f46am_f46_accounting_manipulation_earnfcfxevebit_252d_base_v030_signal,
    f46am_f46_accounting_manipulation_earnfcfxevebitda_252d_base_v031_signal,
    f46am_f46_accounting_manipulation_accxevebit_252d_base_v032_signal,
    f46am_f46_accounting_manipulation_accxevebitda_252d_base_v033_signal,
    f46am_f46_accounting_manipulation_earnfcfxsf3a_252d_base_v034_signal,
    f46am_f46_accounting_manipulation_accxsf3b_252d_base_v035_signal,
    f46am_f46_accounting_manipulation_earnfcfxlogmc_252d_base_v036_signal,
    f46am_f46_accounting_manipulation_accxlogmc_252d_base_v037_signal,
    f46am_f46_accounting_manipulation_earnfcfxlogev_252d_base_v038_signal,
    f46am_f46_accounting_manipulation_earnfcfsq_21d_base_v039_signal,
    f46am_f46_accounting_manipulation_earnfcfsq_252d_base_v040_signal,
    f46am_f46_accounting_manipulation_earnfcfsq_504d_base_v041_signal,
    f46am_f46_accounting_manipulation_accsq_252d_base_v042_signal,
    f46am_f46_accounting_manipulation_accsq_504d_base_v043_signal,
    f46am_f46_accounting_manipulation_earnfcfewm_63d_base_v044_signal,
    f46am_f46_accounting_manipulation_earnfcfewm_252d_base_v045_signal,
    f46am_f46_accounting_manipulation_earnfcfewm_504d_base_v046_signal,
    f46am_f46_accounting_manipulation_accewm_252d_base_v047_signal,
    f46am_f46_accounting_manipulation_accewm_504d_base_v048_signal,
    f46am_f46_accounting_manipulation_nimnxev_21d_base_v049_signal,
    f46am_f46_accounting_manipulation_nimnxev_252d_base_v050_signal,
    f46am_f46_accounting_manipulation_nimnxev_504d_base_v051_signal,
    f46am_f46_accounting_manipulation_earnfcfxlogev_21d_base_v052_signal,
    f46am_f46_accounting_manipulation_accxlogev_504d_base_v053_signal,
    f46am_f46_accounting_manipulation_efgxmcxev_252d_base_v054_signal,
    f46am_f46_accounting_manipulation_accxmcxev_504d_base_v055_signal,
    f46am_f46_accounting_manipulation_earnfcfxdebt_252d_base_v056_signal,
    f46am_f46_accounting_manipulation_accxdebt_504d_base_v057_signal,
    f46am_f46_accounting_manipulation_earnfcfstd_252d_base_v058_signal,
    f46am_f46_accounting_manipulation_earnfcfstd_504d_base_v059_signal,
    f46am_f46_accounting_manipulation_accstd_252d_base_v060_signal,
    f46am_f46_accounting_manipulation_accstd_504d_base_v061_signal,
    f46am_f46_accounting_manipulation_supermanip_252d_base_v062_signal,
    f46am_f46_accounting_manipulation_accxsqrt_504d_base_v063_signal,
    f46am_f46_accounting_manipulation_compmanip_252d_base_v064_signal,
    f46am_f46_accounting_manipulation_compmanip_504d_base_v065_signal,
    f46am_f46_accounting_manipulation_earnfcfxsf3ash_252d_base_v066_signal,
    f46am_f46_accounting_manipulation_accxsf3bsh_504d_base_v067_signal,
    f46am_f46_accounting_manipulation_earnfcfxrev_21d_base_v068_signal,
    f46am_f46_accounting_manipulation_earnfcfxrev_252d_base_v069_signal,
    f46am_f46_accounting_manipulation_earnfcfxrev_504d_base_v070_signal,
    f46am_f46_accounting_manipulation_accxrev_252d_base_v071_signal,
    f46am_f46_accounting_manipulation_earnfcfxeb_252d_base_v072_signal,
    f46am_f46_accounting_manipulation_accxop_504d_base_v073_signal,
    f46am_f46_accounting_manipulation_earnfcfxevebit_504d_base_v074_signal,
    f46am_f46_accounting_manipulation_earnfcfxevebitda_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_ACCOUNTING_MANIPULATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    ev = pd.Series((marketcap + debt).values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")
    sf3a_shares = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="sf3a_shares")
    sf3a_value = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0005, 0.012, n))), name="sf3a_value")
    sf3b_shares = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.006, n))), name="sf3b_shares")
    sf3b_value = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0004, 0.013, n))), name="sf3b_value")

    cols = {
        "closeadj": closeadj, "marketcap": marketcap, "revenue": revenue,
        "netinc": netinc, "fcf": fcf, "ncfo": ncfo, "equity": equity,
        "debt": debt, "assets": assets, "ebitda": ebitda, "opinc": opinc,
        "sharesbas": sharesbas, "ev": ev, "evebit": evebit, "evebitda": evebitda,
        "pe": pe, "pb": pb, "ps": ps,
        "sf3a_shares": sf3a_shares, "sf3a_value": sf3a_value,
        "sf3b_shares": sf3b_shares, "sf3b_value": sf3b_value,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f46_accounting_manip_earnings_fcf_gap", "_f46_accounting_manip_accruals_quality",
                         "_f46_accounting_manip_ni_minus_ncfo")
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
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f46_accounting_manipulation_base_001_075_claude: {n_features} features pass")
