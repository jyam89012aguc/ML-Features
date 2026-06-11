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
def _f15_valuation_level(numerator, denominator, w):
    n = _mean(numerator, w)
    d = _mean(denominator, w)
    return n / d.replace(0, np.nan).abs()


def _f15_pe_level(netinc, marketcap, w):
    e = _mean(netinc, w)
    return marketcap / e.replace(0, np.nan).abs()


def _f15_ev_multiple(ev, fund, w):
    f = _mean(fund, w)
    return ev / f.replace(0, np.nan).abs()


# zscore of 63d PE level over 252d
def f15ve_f15_valuation_at_entry_pelevelz_252d_base_v076_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 63)
    result = _z(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d PE over 504d
def f15ve_f15_valuation_at_entry_pelevelz_504d_base_v077_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 252)
    result = _z(p, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d PB over 252d
def f15ve_f15_valuation_at_entry_pblevelz_252d_base_v078_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 63)
    result = _z(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d PB over 504d
def f15ve_f15_valuation_at_entry_pblevelz_504d_base_v079_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 252)
    result = _z(p, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d PS over 252d
def f15ve_f15_valuation_at_entry_pslevelz_252d_base_v080_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 63)
    result = _z(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d PS over 504d
def f15ve_f15_valuation_at_entry_pslevelz_504d_base_v081_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 252)
    result = _z(p, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d EV/EBITDA over 252d
def f15ve_f15_valuation_at_entry_evebitdaz_252d_base_v082_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 63)
    result = _z(p, 252) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d EV/EBITDA over 504d
def f15ve_f15_valuation_at_entry_evebitdaz_504d_base_v083_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 252)
    result = _z(p, 504) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d EV/EBIT over 252d
def f15ve_f15_valuation_at_entry_evebitz_252d_base_v084_signal(ev, opinc):
    p = _f15_ev_multiple(ev, opinc, 63)
    result = _z(p, 252) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d EV/Rev over 504d
def f15ve_f15_valuation_at_entry_evrevz_504d_base_v085_signal(ev, revenue):
    p = _f15_ev_multiple(ev, revenue, 252)
    result = _z(p, 504) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d EV/FCF over 504d
def f15ve_f15_valuation_at_entry_evfcfz_504d_base_v086_signal(ev, fcf):
    p = _f15_ev_multiple(ev, fcf, 252)
    result = _z(p, 504) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of PE level over 252d window
def f15ve_f15_valuation_at_entry_pelevelstd_252d_base_v087_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 21)
    result = _std(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of EV/EBITDA over 504d
def f15ve_f15_valuation_at_entry_evebitdastd_504d_base_v088_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 21)
    result = _std(p, 504) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of PB level over 252d
def f15ve_f15_valuation_at_entry_pblevelstd_252d_base_v089_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 21)
    result = _std(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days where PE smoothed > 252d mean PE
def f15ve_f15_valuation_at_entry_richpe_count_252d_base_v090_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 21)
    avg = _mean(p, 252)
    flag = (p > avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days where EV/EBITDA smoothed > 252d mean
def f15ve_f15_valuation_at_entry_richevebitda_count_252d_base_v091_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 21)
    avg = _mean(p, 252)
    flag = (p > avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days PS smoothed > 504d mean PS
def f15ve_f15_valuation_at_entry_richps_count_504d_base_v092_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 21)
    avg = _mean(p, 504)
    flag = (p > avg).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days PB smoothed > 504d mean
def f15ve_f15_valuation_at_entry_richpb_count_504d_base_v093_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 21)
    avg = _mean(p, 504)
    flag = (p > avg).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBITDA - 252d mean (deviation), x ev
def f15ve_f15_valuation_at_entry_evebitdadev_252d_base_v094_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 21)
    avg = _mean(p, 252)
    result = (p - avg) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# PE - 252d mean PE, scaled by marketcap
def f15ve_f15_valuation_at_entry_pelevdev_252d_base_v095_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 21)
    avg = _mean(p, 252)
    result = (p - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# PB - 504d mean PB, scaled by marketcap
def f15ve_f15_valuation_at_entry_pblevdev_504d_base_v096_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 21)
    avg = _mean(p, 504)
    result = (p - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# PS - 504d mean PS, scaled by marketcap
def f15ve_f15_valuation_at_entry_pslevdev_504d_base_v097_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 21)
    avg = _mean(p, 504)
    result = (p - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# PE relative to 504d historic max PE * marketcap
def f15ve_f15_valuation_at_entry_perelhi_504d_base_v098_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 63)
    hi = p.rolling(504, min_periods=126).max()
    result = (p / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# PB relative to 504d historic max
def f15ve_f15_valuation_at_entry_pbrelhi_504d_base_v099_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 63)
    hi = p.rolling(504, min_periods=126).max()
    result = (p / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# PS relative to 504d historic max
def f15ve_f15_valuation_at_entry_psrelhi_504d_base_v100_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 63)
    hi = p.rolling(504, min_periods=126).max()
    result = (p / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA relative to 504d historic max
def f15ve_f15_valuation_at_entry_evebitdarelhi_504d_base_v101_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 63)
    hi = p.rolling(504, min_periods=126).max()
    result = (p / hi.replace(0, np.nan)) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT relative to 504d historic max
def f15ve_f15_valuation_at_entry_evebitrelhi_504d_base_v102_signal(ev, opinc):
    p = _f15_ev_multiple(ev, opinc, 63)
    hi = p.rolling(504, min_periods=126).max()
    result = (p / hi.replace(0, np.nan)) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# (PE - 504d min PE) / 504d range, x marketcap
def f15ve_f15_valuation_at_entry_pelevpos_504d_base_v103_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    pos = (p - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# (PB position) within 504d range x marketcap
def f15ve_f15_valuation_at_entry_pblevpos_504d_base_v104_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    pos = (p - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# (EV/EBITDA position) within 504d range x ev
def f15ve_f15_valuation_at_entry_evebitdapos_504d_base_v105_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    pos = (p - lo) / (hi - lo).replace(0, np.nan)
    result = pos * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# blended valuation: (PE + PB + PS) at 252d, scaled marketcap
def f15ve_f15_valuation_at_entry_blendedval_252d_base_v106_signal(netinc, equity, revenue, marketcap):
    pe_l = _f15_pe_level(netinc, marketcap, 252)
    pb_l = _f15_valuation_level(marketcap, equity, 252)
    ps_l = _f15_valuation_level(marketcap, revenue, 252)
    result = (pe_l + pb_l + ps_l) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# blended EV multiples (EV/EBITDA + EV/EBIT)
def f15ve_f15_valuation_at_entry_blendedevmult_252d_base_v107_signal(ev, ebitda, opinc):
    e1 = _f15_ev_multiple(ev, ebitda, 252)
    e2 = _f15_ev_multiple(ev, opinc, 252)
    result = (e1 + e2) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite earnings yield: netinc / marketcap, smoothed 252d
def f15ve_f15_valuation_at_entry_earningyieldraw_252d_base_v108_signal(netinc, marketcap):
    inv_pe = _f15_valuation_level(netinc, marketcap, 252)
    result = inv_pe * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite sales yield: revenue / marketcap, smoothed 252d x marketcap
def f15ve_f15_valuation_at_entry_salesyieldraw_252d_base_v109_signal(revenue, marketcap):
    inv_ps = _f15_valuation_level(revenue, marketcap, 252)
    result = inv_ps * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite book yield: equity / marketcap, smoothed 252d x marketcap
def f15ve_f15_valuation_at_entry_bookyieldraw_252d_base_v110_signal(equity, marketcap):
    inv_pb = _f15_valuation_level(equity, marketcap, 252)
    result = inv_pb * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite ebitda yield: ebitda / ev, smoothed 252d x ev
def f15ve_f15_valuation_at_entry_ebitdayieldraw_252d_base_v111_signal(ebitda, ev):
    inv = _f15_valuation_level(ebitda, ev, 252)
    result = inv * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite fcf yield: fcf / ev, smoothed 252d x ev
def f15ve_f15_valuation_at_entry_fcfyieldraw_252d_base_v112_signal(fcf, ev):
    inv = _f15_valuation_level(fcf, ev, 252)
    result = inv * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite gp yield: gp / ev, smoothed 252d x ev
def f15ve_f15_valuation_at_entry_gpyieldraw_252d_base_v113_signal(gp, ev):
    inv = _f15_valuation_level(gp, ev, 252)
    result = inv * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite ncfo yield: ncfo / ev, smoothed 252d x ev
def f15ve_f15_valuation_at_entry_ncfoyieldraw_252d_base_v114_signal(ncfo, ev):
    inv = _f15_valuation_level(ncfo, ev, 252)
    result = inv * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d eps / closeadj proxy times marketcap
def f15ve_f15_valuation_at_entry_epsxprice_21d_base_v115_signal(eps, marketcap, closeadj):
    val = _f15_valuation_level(eps * closeadj, closeadj, 21)
    result = val * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps / closeadj earnings yield x marketcap
def f15ve_f15_valuation_at_entry_epsyield_252d_base_v116_signal(eps, marketcap, closeadj):
    val = _f15_valuation_level(eps, closeadj, 252)
    result = val * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# pe column relative to 252d mean pe column, weighted by mcap
def f15ve_f15_valuation_at_entry_perelmean_252d_base_v117_signal(pe, marketcap):
    smoothed = _f15_valuation_level(pe * marketcap, marketcap, 21)
    avg = _mean(smoothed, 252)
    result = (smoothed - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ps column relative to 252d mean ps column, weighted by mcap
def f15ve_f15_valuation_at_entry_psrelmean_252d_base_v118_signal(ps, marketcap):
    smoothed = _f15_valuation_level(ps * marketcap, marketcap, 21)
    avg = _mean(smoothed, 252)
    result = (smoothed - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# pb column relative to 252d mean pb column
def f15ve_f15_valuation_at_entry_pbrelmean_252d_base_v119_signal(pb, marketcap):
    smoothed = _f15_valuation_level(pb * marketcap, marketcap, 21)
    avg = _mean(smoothed, 252)
    result = (smoothed - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# evebitda column relative to 252d mean
def f15ve_f15_valuation_at_entry_evebitdarelmean_252d_base_v120_signal(evebitda, ev):
    smoothed = _f15_valuation_level(evebitda * ev, ev, 21)
    avg = _mean(smoothed, 252)
    result = (smoothed - avg) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# evebit column relative to 252d mean
def f15ve_f15_valuation_at_entry_evebitrelmean_252d_base_v121_signal(evebit, ev):
    smoothed = _f15_valuation_level(evebit * ev, ev, 21)
    avg = _mean(smoothed, 252)
    result = (smoothed - avg) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of EV/EBITDA to PE both smoothed 252d
def f15ve_f15_valuation_at_entry_evebitda_to_pe_252d_base_v122_signal(ev, ebitda, netinc, marketcap):
    a = _f15_ev_multiple(ev, ebitda, 252)
    b = _f15_pe_level(netinc, marketcap, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of PB to PS both 252d
def f15ve_f15_valuation_at_entry_pb_to_ps_252d_base_v123_signal(equity, revenue, marketcap):
    a = _f15_valuation_level(marketcap, equity, 252)
    b = _f15_valuation_level(marketcap, revenue, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of EV/EBIT to EV/EBITDA both 252d
def f15ve_f15_valuation_at_entry_evebit_to_evebitda_252d_base_v124_signal(ev, opinc, ebitda):
    a = _f15_ev_multiple(ev, opinc, 252)
    b = _f15_ev_multiple(ev, ebitda, 252)
    result = (a / b.replace(0, np.nan)) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of PE 63d to PE 252d (recent vs trend)
def f15ve_f15_valuation_at_entry_pe_recent_vs_trend_base_v125_signal(netinc, marketcap):
    a = _f15_pe_level(netinc, marketcap, 63)
    b = _f15_pe_level(netinc, marketcap, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of PS 63d to PS 252d
def f15ve_f15_valuation_at_entry_ps_recent_vs_trend_base_v126_signal(revenue, marketcap):
    a = _f15_valuation_level(marketcap, revenue, 63)
    b = _f15_valuation_level(marketcap, revenue, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of EV/EBITDA 63d to 252d
def f15ve_f15_valuation_at_entry_evebitda_recent_vs_trend_base_v127_signal(ev, ebitda):
    a = _f15_ev_multiple(ev, ebitda, 63)
    b = _f15_ev_multiple(ev, ebitda, 252)
    result = (a / b.replace(0, np.nan)) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite cheapness 252d: 1 / (PE + PB + PS) * marketcap
def f15ve_f15_valuation_at_entry_cheapcomp_252d_base_v128_signal(netinc, equity, revenue, marketcap):
    pe_l = _f15_pe_level(netinc, marketcap, 252)
    pb_l = _f15_valuation_level(marketcap, equity, 252)
    ps_l = _f15_valuation_level(marketcap, revenue, 252)
    s = (pe_l + pb_l + ps_l).replace(0, np.nan)
    result = (1.0 / s) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EV total scaled by liabilities (capital intensity)
def f15ve_f15_valuation_at_entry_evintens_21d_base_v129_signal(ev, liabilities):
    a = _f15_ev_multiple(ev, liabilities, 21)
    result = a * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev / assets x ev
def f15ve_f15_valuation_at_entry_evassets_252d_base_v130_signal(ev, assets):
    a = _f15_ev_multiple(ev, assets, 252)
    result = a * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap / retearn
def f15ve_f15_valuation_at_entry_pretearn_21d_base_v131_signal(retearn, marketcap):
    a = _f15_valuation_level(marketcap, retearn, 21)
    result = a * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap / retearn
def f15ve_f15_valuation_at_entry_pretearn_252d_base_v132_signal(retearn, marketcap):
    a = _f15_valuation_level(marketcap, retearn, 252)
    result = a * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap / workingcapital
def f15ve_f15_valuation_at_entry_pwc_252d_base_v133_signal(workingcapital, marketcap):
    a = _f15_valuation_level(marketcap, workingcapital, 252)
    result = a * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# EV / debt 252d
def f15ve_f15_valuation_at_entry_evdebt_252d_base_v134_signal(ev, debt):
    a = _f15_ev_multiple(ev, debt, 252)
    result = a * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# EV / equity 252d
def f15ve_f15_valuation_at_entry_evequity_252d_base_v135_signal(ev, equity):
    a = _f15_ev_multiple(ev, equity, 252)
    result = a * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# EV - marketcap (proxy for net debt) 252d * marketcap
def f15ve_f15_valuation_at_entry_netdebt_252d_base_v136_signal(ev, marketcap):
    a = _f15_valuation_level(ev - marketcap, marketcap, 252)
    result = a * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# EV / sharesbas 252d (per share enterprise value)
def f15ve_f15_valuation_at_entry_evpershare_252d_base_v137_signal(ev, sharesbas):
    a = _f15_ev_multiple(ev, sharesbas, 252)
    result = a * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap / sharesbas (price per share level proxy)
def f15ve_f15_valuation_at_entry_pricepershare_252d_base_v138_signal(sharesbas, marketcap):
    a = _f15_valuation_level(marketcap, sharesbas, 252)
    result = a * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap / capex (P/Investment)
def f15ve_f15_valuation_at_entry_pcapex_252d_base_v139_signal(capex, marketcap):
    a = _f15_valuation_level(marketcap, capex, 252)
    result = a * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap / capex
def f15ve_f15_valuation_at_entry_pcapex_504d_base_v140_signal(capex, marketcap):
    a = _f15_valuation_level(marketcap, capex, 504)
    result = a * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV / capex
def f15ve_f15_valuation_at_entry_evcapex_252d_base_v141_signal(ev, capex):
    a = _f15_ev_multiple(ev, capex, 252)
    result = a * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days where EV/EBITDA crossed below 252d mean (cheap entries)
def f15ve_f15_valuation_at_entry_cheapevebitda_count_252d_base_v142_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 21)
    avg = _mean(p, 252)
    flag = (p < avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of cheap PE days
def f15ve_f15_valuation_at_entry_cheappe_count_504d_base_v143_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 21)
    avg = _mean(p, 504)
    flag = (p < avg).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of marketcap to assets * marketcap
def f15ve_f15_valuation_at_entry_passet_252d_base_v144_signal(assets, marketcap):
    a = _f15_valuation_level(marketcap, assets, 252)
    result = a * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of marketcap to assets * marketcap
def f15ve_f15_valuation_at_entry_passet_504d_base_v145_signal(assets, marketcap):
    a = _f15_valuation_level(marketcap, assets, 504)
    result = a * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of EV to revenue + EV to EBITDA combined
def f15ve_f15_valuation_at_entry_evcomp_252d_base_v146_signal(ev, revenue, ebitda):
    a = _f15_ev_multiple(ev, revenue, 252)
    b = _f15_ev_multiple(ev, ebitda, 252)
    result = (a + b) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cheap_signal: lower of PE to PS multiples, weighted
def f15ve_f15_valuation_at_entry_lowmult_252d_base_v147_signal(netinc, revenue, marketcap):
    pe_l = _f15_pe_level(netinc, marketcap, 252)
    ps_l = _f15_valuation_level(marketcap, revenue, 252)
    lo = pd.concat([pe_l, ps_l], axis=1).min(axis=1)
    result = lo * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d highest of EV/EBITDA vs EV/EBIT
def f15ve_f15_valuation_at_entry_highevmult_252d_base_v148_signal(ev, ebitda, opinc):
    a = _f15_ev_multiple(ev, ebitda, 252)
    b = _f15_ev_multiple(ev, opinc, 252)
    hi = pd.concat([a, b], axis=1).max(axis=1)
    result = hi * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# log(PE) at 252d * marketcap (compresses outliers)
def f15ve_f15_valuation_at_entry_logpe_252d_base_v149_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 252)
    result = np.log(p.replace(0, np.nan).abs()) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# log(EV/EBITDA) at 252d * ev
def f15ve_f15_valuation_at_entry_logevebitda_252d_base_v150_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 252)
    result = np.log(p.replace(0, np.nan).abs()) * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15ve_f15_valuation_at_entry_pelevelz_252d_base_v076_signal,
    f15ve_f15_valuation_at_entry_pelevelz_504d_base_v077_signal,
    f15ve_f15_valuation_at_entry_pblevelz_252d_base_v078_signal,
    f15ve_f15_valuation_at_entry_pblevelz_504d_base_v079_signal,
    f15ve_f15_valuation_at_entry_pslevelz_252d_base_v080_signal,
    f15ve_f15_valuation_at_entry_pslevelz_504d_base_v081_signal,
    f15ve_f15_valuation_at_entry_evebitdaz_252d_base_v082_signal,
    f15ve_f15_valuation_at_entry_evebitdaz_504d_base_v083_signal,
    f15ve_f15_valuation_at_entry_evebitz_252d_base_v084_signal,
    f15ve_f15_valuation_at_entry_evrevz_504d_base_v085_signal,
    f15ve_f15_valuation_at_entry_evfcfz_504d_base_v086_signal,
    f15ve_f15_valuation_at_entry_pelevelstd_252d_base_v087_signal,
    f15ve_f15_valuation_at_entry_evebitdastd_504d_base_v088_signal,
    f15ve_f15_valuation_at_entry_pblevelstd_252d_base_v089_signal,
    f15ve_f15_valuation_at_entry_richpe_count_252d_base_v090_signal,
    f15ve_f15_valuation_at_entry_richevebitda_count_252d_base_v091_signal,
    f15ve_f15_valuation_at_entry_richps_count_504d_base_v092_signal,
    f15ve_f15_valuation_at_entry_richpb_count_504d_base_v093_signal,
    f15ve_f15_valuation_at_entry_evebitdadev_252d_base_v094_signal,
    f15ve_f15_valuation_at_entry_pelevdev_252d_base_v095_signal,
    f15ve_f15_valuation_at_entry_pblevdev_504d_base_v096_signal,
    f15ve_f15_valuation_at_entry_pslevdev_504d_base_v097_signal,
    f15ve_f15_valuation_at_entry_perelhi_504d_base_v098_signal,
    f15ve_f15_valuation_at_entry_pbrelhi_504d_base_v099_signal,
    f15ve_f15_valuation_at_entry_psrelhi_504d_base_v100_signal,
    f15ve_f15_valuation_at_entry_evebitdarelhi_504d_base_v101_signal,
    f15ve_f15_valuation_at_entry_evebitrelhi_504d_base_v102_signal,
    f15ve_f15_valuation_at_entry_pelevpos_504d_base_v103_signal,
    f15ve_f15_valuation_at_entry_pblevpos_504d_base_v104_signal,
    f15ve_f15_valuation_at_entry_evebitdapos_504d_base_v105_signal,
    f15ve_f15_valuation_at_entry_blendedval_252d_base_v106_signal,
    f15ve_f15_valuation_at_entry_blendedevmult_252d_base_v107_signal,
    f15ve_f15_valuation_at_entry_earningyieldraw_252d_base_v108_signal,
    f15ve_f15_valuation_at_entry_salesyieldraw_252d_base_v109_signal,
    f15ve_f15_valuation_at_entry_bookyieldraw_252d_base_v110_signal,
    f15ve_f15_valuation_at_entry_ebitdayieldraw_252d_base_v111_signal,
    f15ve_f15_valuation_at_entry_fcfyieldraw_252d_base_v112_signal,
    f15ve_f15_valuation_at_entry_gpyieldraw_252d_base_v113_signal,
    f15ve_f15_valuation_at_entry_ncfoyieldraw_252d_base_v114_signal,
    f15ve_f15_valuation_at_entry_epsxprice_21d_base_v115_signal,
    f15ve_f15_valuation_at_entry_epsyield_252d_base_v116_signal,
    f15ve_f15_valuation_at_entry_perelmean_252d_base_v117_signal,
    f15ve_f15_valuation_at_entry_psrelmean_252d_base_v118_signal,
    f15ve_f15_valuation_at_entry_pbrelmean_252d_base_v119_signal,
    f15ve_f15_valuation_at_entry_evebitdarelmean_252d_base_v120_signal,
    f15ve_f15_valuation_at_entry_evebitrelmean_252d_base_v121_signal,
    f15ve_f15_valuation_at_entry_evebitda_to_pe_252d_base_v122_signal,
    f15ve_f15_valuation_at_entry_pb_to_ps_252d_base_v123_signal,
    f15ve_f15_valuation_at_entry_evebit_to_evebitda_252d_base_v124_signal,
    f15ve_f15_valuation_at_entry_pe_recent_vs_trend_base_v125_signal,
    f15ve_f15_valuation_at_entry_ps_recent_vs_trend_base_v126_signal,
    f15ve_f15_valuation_at_entry_evebitda_recent_vs_trend_base_v127_signal,
    f15ve_f15_valuation_at_entry_cheapcomp_252d_base_v128_signal,
    f15ve_f15_valuation_at_entry_evintens_21d_base_v129_signal,
    f15ve_f15_valuation_at_entry_evassets_252d_base_v130_signal,
    f15ve_f15_valuation_at_entry_pretearn_21d_base_v131_signal,
    f15ve_f15_valuation_at_entry_pretearn_252d_base_v132_signal,
    f15ve_f15_valuation_at_entry_pwc_252d_base_v133_signal,
    f15ve_f15_valuation_at_entry_evdebt_252d_base_v134_signal,
    f15ve_f15_valuation_at_entry_evequity_252d_base_v135_signal,
    f15ve_f15_valuation_at_entry_netdebt_252d_base_v136_signal,
    f15ve_f15_valuation_at_entry_evpershare_252d_base_v137_signal,
    f15ve_f15_valuation_at_entry_pricepershare_252d_base_v138_signal,
    f15ve_f15_valuation_at_entry_pcapex_252d_base_v139_signal,
    f15ve_f15_valuation_at_entry_pcapex_504d_base_v140_signal,
    f15ve_f15_valuation_at_entry_evcapex_252d_base_v141_signal,
    f15ve_f15_valuation_at_entry_cheapevebitda_count_252d_base_v142_signal,
    f15ve_f15_valuation_at_entry_cheappe_count_504d_base_v143_signal,
    f15ve_f15_valuation_at_entry_passet_252d_base_v144_signal,
    f15ve_f15_valuation_at_entry_passet_504d_base_v145_signal,
    f15ve_f15_valuation_at_entry_evcomp_252d_base_v146_signal,
    f15ve_f15_valuation_at_entry_lowmult_252d_base_v147_signal,
    f15ve_f15_valuation_at_entry_highevmult_252d_base_v148_signal,
    f15ve_f15_valuation_at_entry_logpe_252d_base_v149_signal,
    f15ve_f15_valuation_at_entry_logevebitda_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_VALUATION_AT_ENTRY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f15_valuation", "_f15_pe", "_f15_ev")
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
    print(f"OK f15_valuation_at_entry_base_076_150_claude: {n_features} features pass")
