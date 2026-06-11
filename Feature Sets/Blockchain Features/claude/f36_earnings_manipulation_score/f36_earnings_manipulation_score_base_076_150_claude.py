import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (Beneish earnings-manipulation components) =====
def _f36_dsri(receivables, revenue, w):
    # days-sales-in-receivables index: (receivables/revenue) vs its value w days prior
    r = _safe_div(receivables, revenue)
    return _safe_div(r, r.shift(w))


def _f36_tata(netinc, ncfo, assets):
    # total accruals to total assets = (net income - operating cash flow) / assets
    return _safe_div(netinc - ncfo, assets)


def _f36_gmi(revenue, gp, w):
    # gross-margin index = prior gross margin / current gross margin
    gm = _safe_div(gp, revenue)
    return _safe_div(gm.shift(w), gm)


def _f36_sgi(revenue, w):
    # sales growth index = current revenue / prior revenue
    return _safe_div(revenue, revenue.shift(w))


# ============ FEATURES 076-150 ============

# 84d days-sales-in-receivables index
def f36em_f36_earnings_manipulation_score_dsri_84d_base_v076_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d days-sales-in-receivables index
def f36em_f36_earnings_manipulation_score_dsri_189d_base_v077_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d days-sales-in-receivables index
def f36em_f36_earnings_manipulation_score_dsri_42d_base_v078_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d DSRI over 504d
def f36em_f36_earnings_manipulation_score_zdsri_252d_base_v079_signal(receivables, revenue):
    result = _z(_f36_dsri(receivables, revenue, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed DSRI (126d mean of 63d DSRI)
def f36em_f36_earnings_manipulation_score_smdsri_126d_base_v080_signal(receivables, revenue):
    result = _mean(_f36_dsri(receivables, revenue, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dispersion of 21d DSRI (receivables-quality instability)
def f36em_f36_earnings_manipulation_score_dsridisp_126d_base_v081_signal(receivables, revenue):
    result = _std(_f36_dsri(receivables, revenue, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dispersion of 21d DSRI
def f36em_f36_earnings_manipulation_score_dsridisp_252d_base_v082_signal(receivables, revenue):
    result = _std(_f36_dsri(receivables, revenue, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d gross-margin index
def f36em_f36_earnings_manipulation_score_gmi_84d_base_v083_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d gross-margin index
def f36em_f36_earnings_manipulation_score_gmi_189d_base_v084_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed GMI (126d mean of 63d GMI)
def f36em_f36_earnings_manipulation_score_smgmi_126d_base_v085_signal(revenue, gp):
    result = _mean(_f36_gmi(revenue, gp, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dispersion of 21d GMI (margin instability)
def f36em_f36_earnings_manipulation_score_gmidisp_126d_base_v086_signal(revenue, gp):
    result = _std(_f36_gmi(revenue, gp, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d GMI over 504d
def f36em_f36_earnings_manipulation_score_zgmi_126d_base_v087_signal(revenue, gp):
    result = _z(_f36_gmi(revenue, gp, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d sales growth index
def f36em_f36_earnings_manipulation_score_sgi_84d_base_v088_signal(revenue):
    result = _f36_sgi(revenue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d sales growth index
def f36em_f36_earnings_manipulation_score_sgi_189d_base_v089_signal(revenue):
    result = _f36_sgi(revenue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d sales growth index
def f36em_f36_earnings_manipulation_score_sgi_42d_base_v090_signal(revenue):
    result = _f36_sgi(revenue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed SGI (126d mean of 63d SGI)
def f36em_f36_earnings_manipulation_score_smsgi_126d_base_v091_signal(revenue):
    result = _mean(_f36_sgi(revenue, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dispersion of 21d SGI (growth instability)
def f36em_f36_earnings_manipulation_score_sgidisp_126d_base_v092_signal(revenue):
    result = _std(_f36_sgi(revenue, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d SGI over 504d
def f36em_f36_earnings_manipulation_score_zsgi_252d_base_v093_signal(revenue):
    result = _z(_f36_sgi(revenue, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dispersion of TATA (accrual-quality instability)
def f36em_f36_earnings_manipulation_score_tatadisp_252d_base_v094_signal(netinc, ncfo, assets):
    result = _std(_f36_tata(netinc, ncfo, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dispersion of TATA
def f36em_f36_earnings_manipulation_score_tatadisp_126d_base_v095_signal(netinc, ncfo, assets):
    result = _std(_f36_tata(netinc, ncfo, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed TATA
def f36em_f36_earnings_manipulation_score_smtata_252d_base_v096_signal(netinc, ncfo, assets):
    result = _mean(_f36_tata(netinc, ncfo, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in TATA (short-horizon accrual jump)
def f36em_f36_earnings_manipulation_score_tatachg_63d_base_v097_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    result = t - t.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in TATA (long-horizon accrual drift)
def f36em_f36_earnings_manipulation_score_tatachg_252d_base_v098_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    result = t - t.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d asset-quality index
def f36em_f36_earnings_manipulation_score_aqi_84d_base_v099_signal(intangibles, ppnenet, assets, netinc, ncfo):
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    result = _safe_div(q, q.shift(84)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of asset-quality ratio over 252d
def f36em_f36_earnings_manipulation_score_zaq_252d_base_v100_signal(intangibles, ppnenet, assets, netinc, ncfo):
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    result = _z(q, 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in intangibles share
def f36em_f36_earnings_manipulation_score_intchg_252d_base_v101_signal(intangibles, assets, netinc, ncfo):
    s = _safe_div(intangibles, assets)
    result = s - s.shift(252) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d depreciation index
def f36em_f36_earnings_manipulation_score_depi_84d_base_v102_signal(depamor, ppnenet, revenue):
    rate = _safe_div(depamor, ppnenet + depamor)
    result = _safe_div(rate.shift(84), rate) + _f36_sgi(revenue, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of depreciation rate over 252d
def f36em_f36_earnings_manipulation_score_zdeprate_252d_base_v103_signal(depamor, ppnenet, revenue):
    result = _z(_safe_div(depamor, ppnenet + depamor), 252) + _f36_sgi(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in depreciation rate (slowing depreciation = aggressive)
def f36em_f36_earnings_manipulation_score_depratechg_126d_base_v104_signal(depamor, ppnenet, revenue):
    rate = _safe_div(depamor, ppnenet + depamor)
    result = rate - rate.shift(126) + _f36_sgi(revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d SGA-to-sales index
def f36em_f36_earnings_manipulation_score_sgai_84d_base_v105_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = _safe_div(r, r.shift(84)) + _f36_sgi(revenue, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of sga-to-sales over 252d
def f36em_f36_earnings_manipulation_score_zsga_252d_base_v106_signal(sgna, revenue):
    result = _z(_safe_div(sgna, revenue), 252) + _f36_sgi(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in sga-to-sales (efficiency drift)
def f36em_f36_earnings_manipulation_score_sgachg_126d_base_v107_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = r - r.shift(126) + _f36_sgi(revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d leverage index
def f36em_f36_earnings_manipulation_score_lvgi_84d_base_v108_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = _safe_div(lev, lev.shift(84)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of liabilities/assets over 252d
def f36em_f36_earnings_manipulation_score_zlev_252d_base_v109_signal(liabilities, assets, netinc, ncfo):
    result = _z(_safe_div(liabilities, assets), 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in leverage (balance-sheet expansion)
def f36em_f36_earnings_manipulation_score_levchg_126d_base_v110_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = lev - lev.shift(126) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt-leverage index
def f36em_f36_earnings_manipulation_score_dlvgi_252d_base_v111_signal(debt, assets, netinc, ncfo):
    lev = _safe_div(debt, assets)
    result = _safe_div(lev, lev.shift(252)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-liabilities mix anchored (financing aggressiveness)
def f36em_f36_earnings_manipulation_score_debtmix_063d_base_v112_signal(debt, liabilities, netinc, ncfo, assets):
    result = _safe_div(debt, liabilities) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d full 8-component M-score blend
def f36em_f36_earnings_manipulation_score_mscore8_84d_base_v113_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
    dsri = _f36_dsri(receivables, revenue, 84)
    gmi = _f36_gmi(revenue, gp, 84)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(84))
    sgi = _f36_sgi(revenue, 84)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(84), rate)
    sg = _safe_div(sgna, revenue)
    sgai = _safe_div(sg, sg.shift(84))
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(84))
    tata = _f36_tata(netinc, ncfo, assets)
    result = (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
              + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d M-score over 504d
def f36em_f36_earnings_manipulation_score_zmscore_252d_base_v114_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
    dsri = _f36_dsri(receivables, revenue, 252)
    gmi = _f36_gmi(revenue, gp, 252)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(252))
    sgi = _f36_sgi(revenue, 252)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(252), rate)
    sg = _safe_div(sgna, revenue)
    sgai = _safe_div(sg, sg.shift(252))
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(252))
    tata = _f36_tata(netinc, ncfo, assets)
    m = (0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
         + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 252d M-score over 504d
def f36em_f36_earnings_manipulation_score_mrank_252d_base_v115_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
    dsri = _f36_dsri(receivables, revenue, 252)
    gmi = _f36_gmi(revenue, gp, 252)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(252))
    sgi = _f36_sgi(revenue, 252)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(252), rate)
    sg = _safe_div(sgna, revenue)
    sgai = _safe_div(sg, sg.shift(252))
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(252))
    tata = _f36_tata(netinc, ncfo, assets)
    m = (0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
         + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    result = m.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 5-component partial M-score blend at 252d
def f36em_f36_earnings_manipulation_score_mscore5_252d_base_v116_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor):
    dsri = _f36_dsri(receivables, revenue, 252)
    gmi = _f36_gmi(revenue, gp, 252)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(252))
    sgi = _f36_sgi(revenue, 252)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(252), rate)
    result = 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi + 0.115 * depi
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-component sub-score (TATA + DSRI), 126d
def f36em_f36_earnings_manipulation_score_accrsub_126d_base_v117_signal(receivables, revenue, netinc, ncfo, assets):
    result = 4.679 * _f36_tata(netinc, ncfo, assets) + 0.92 * _f36_dsri(receivables, revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-quality sub-score (DSRI + SGI - GMI), 126d
def f36em_f36_earnings_manipulation_score_revqual_126d_base_v118_signal(receivables, revenue, gp):
    result = (0.92 * _f36_dsri(receivables, revenue, 126)
              + 0.892 * _f36_sgi(revenue, 126)
              + 0.528 * _f36_gmi(revenue, gp, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# DSRI x SGI interaction at 252d (aggressive-growth receivables)
def f36em_f36_earnings_manipulation_score_dsrisgi_252d_base_v119_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 252) * _f36_sgi(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# GMI x TATA interaction at 126d (margin-pressure accrual)
def f36em_f36_earnings_manipulation_score_gmitata_126d_base_v120_signal(revenue, gp, netinc, ncfo, assets):
    result = _f36_gmi(revenue, gp, 126) * _f36_tata(netinc, ncfo, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 84d and 252d DSRI
def f36em_f36_earnings_manipulation_score_dsrispread_84_252_base_v121_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 84) - _f36_dsri(receivables, revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 126d and 252d GMI
def f36em_f36_earnings_manipulation_score_gmispread_126_252_base_v122_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 126) - _f36_gmi(revenue, gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 84d and 252d SGI
def f36em_f36_earnings_manipulation_score_sgispread_84_252_base_v123_signal(revenue):
    result = _f36_sgi(revenue, 84) - _f36_sgi(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend of SGI (short mean minus long mean)
def f36em_f36_earnings_manipulation_score_sgitrend_252d_base_v124_signal(revenue):
    s = _f36_sgi(revenue, 63)
    result = _mean(s, 63) - _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend of leverage index
def f36em_f36_earnings_manipulation_score_lvgitrend_252d_base_v125_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(63))
    result = _mean(lvgi, 63) - _mean(lvgi, 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-to-assets turnover change (asset-use efficiency), anchored
def f36em_f36_earnings_manipulation_score_turnidx_126d_base_v126_signal(revenue, assets, netinc, ncfo):
    t = _safe_div(revenue, assets)
    result = _safe_div(t, t.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow margin (ncfo/revenue) deterioration index, anchored
def f36em_f36_earnings_manipulation_score_cfmidx_126d_base_v127_signal(ncfo, revenue, netinc, assets):
    c = _safe_div(ncfo, revenue)
    result = _safe_div(c.shift(126), c) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin (netinc/revenue) z-score over 252d, anchored
def f36em_f36_earnings_manipulation_score_znetmargin_252d_base_v128_signal(netinc, revenue, ncfo, assets):
    result = _z(_safe_div(netinc, revenue), 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accruals minus depreciation (discretionary accrual proxy) over assets
def f36em_f36_earnings_manipulation_score_discaccr_126d_base_v129_signal(netinc, ncfo, depamor, assets):
    result = _mean(_safe_div((netinc - ncfo) - depamor, assets), 126) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite manipulation z-blend (DSRI, GMI, SGI, AQI, TATA)
def f36em_f36_earnings_manipulation_score_zblend5_126d_base_v130_signal(receivables, revenue, gp, intangibles, ppnenet, assets, netinc, ncfo):
    a = _z(_f36_dsri(receivables, revenue, 126), 252)
    b = _z(_f36_gmi(revenue, gp, 126), 252)
    c = _z(_f36_sgi(revenue, 126), 252)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    d = _z(_safe_div(q, q.shift(126)), 252)
    e = _z(_f36_tata(netinc, ncfo, assets), 252)
    result = (a + b + c + d + e) / 5.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite manipulation z-blend
def f36em_f36_earnings_manipulation_score_zblend5_252d_base_v131_signal(receivables, revenue, gp, intangibles, ppnenet, assets, netinc, ncfo):
    a = _z(_f36_dsri(receivables, revenue, 252), 504)
    b = _z(_f36_gmi(revenue, gp, 252), 504)
    c = _z(_f36_sgi(revenue, 252), 504)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    d = _z(_safe_div(q, q.shift(252)), 504)
    e = _z(_f36_tata(netinc, ncfo, assets), 504)
    result = (a + b + c + d + e) / 5.0
    return result.replace([np.inf, -np.inf], np.nan)


# DSRI scaled by sales-growth (receivables build per unit growth)
def f36em_f36_earnings_manipulation_score_dsripersgi_126d_base_v132_signal(receivables, revenue):
    result = _safe_div(_f36_dsri(receivables, revenue, 126), _f36_sgi(revenue, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# TATA scaled by sales-growth (accrual build per unit growth)
def f36em_f36_earnings_manipulation_score_tatapersgi_126d_base_v133_signal(netinc, ncfo, assets, revenue):
    result = _safe_div(_f36_tata(netinc, ncfo, assets), _f36_sgi(revenue, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit-to-assets change (productivity), anchored
def f36em_f36_earnings_manipulation_score_gpassetidx_126d_base_v134_signal(gp, assets, netinc, ncfo):
    g = _safe_div(gp, assets)
    result = _safe_div(g, g.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d full M-score percentile rank over 252d
def f36em_f36_earnings_manipulation_score_mrank84_252d_base_v135_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
    dsri = _f36_dsri(receivables, revenue, 84)
    gmi = _f36_gmi(revenue, gp, 84)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(84))
    sgi = _f36_sgi(revenue, 84)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(84), rate)
    sg = _safe_div(sgna, revenue)
    sgai = _safe_div(sg, sg.shift(84))
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(84))
    tata = _f36_tata(netinc, ncfo, assets)
    m = (0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
         + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    result = m.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# DSRI deviation magnitude z-scored (abs receivables anomaly)
def f36em_f36_earnings_manipulation_score_absdsri_z252_base_v136_signal(receivables, revenue):
    result = _z((_f36_dsri(receivables, revenue, 126) - 1.0).abs(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# combined revenue-recognition stress (DSRI + COR index), 126d
def f36em_f36_earnings_manipulation_score_revrec_126d_base_v137_signal(receivables, revenue, cor):
    c = _safe_div(cor, revenue)
    cori = _safe_div(c, c.shift(126))
    result = 0.92 * _f36_dsri(receivables, revenue, 126) + 0.5 * cori
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities-to-equity proxy via assets (financial-risk index), anchored
def f36em_f36_earnings_manipulation_score_deidx_126d_base_v138_signal(liabilities, assets, netinc, ncfo):
    eq = (assets - liabilities)
    de = _safe_div(liabilities, eq)
    result = _safe_div(de, de.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d full 8-component M-score blend
def f36em_f36_earnings_manipulation_score_mscore8_189d_base_v139_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
    dsri = _f36_dsri(receivables, revenue, 189)
    gmi = _f36_gmi(revenue, gp, 189)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(189))
    sgi = _f36_sgi(revenue, 189)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(189), rate)
    sg = _safe_div(sgna, revenue)
    sgai = _safe_div(sg, sg.shift(189))
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(189))
    tata = _f36_tata(netinc, ncfo, assets)
    result = (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
              + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-to-cashflow coverage (TATA over cash-flow margin), 126d
def f36em_f36_earnings_manipulation_score_accrcover_126d_base_v140_signal(netinc, ncfo, assets, revenue):
    tata = _f36_tata(netinc, ncfo, assets)
    result = _safe_div(tata, _safe_div(ncfo, revenue))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EWMA of DSRI (decay-weighted receivables index)
def f36em_f36_earnings_manipulation_score_ewmdsri_126d_base_v141_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 21).ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EWMA of TATA (decay-weighted accruals)
def f36em_f36_earnings_manipulation_score_ewmtata_126d_base_v142_signal(netinc, ncfo, assets):
    result = _f36_tata(netinc, ncfo, assets).ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EWMA of GMI (decay-weighted margin index)
def f36em_f36_earnings_manipulation_score_ewmgmi_252d_base_v143_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 21).ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d full M-score minus its own 126d mean (M-score surprise)
def f36em_f36_earnings_manipulation_score_msurp_252d_base_v144_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
    dsri = _f36_dsri(receivables, revenue, 252)
    gmi = _f36_gmi(revenue, gp, 252)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(252))
    sgi = _f36_sgi(revenue, 252)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(252), rate)
    sg = _safe_div(sgna, revenue)
    sgai = _safe_div(sg, sg.shift(252))
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(252))
    tata = _f36_tata(netinc, ncfo, assets)
    m = (0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
         + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-to-assets z-score (balance-sheet receivables stress), anchored
def f36em_f36_earnings_manipulation_score_zrecasset_252d_base_v145_signal(receivables, assets, revenue):
    result = _z(_safe_div(receivables, assets), 252) + _f36_dsri(receivables, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-plus-ppnenet (capitalization base) growth index, anchored
def f36em_f36_earnings_manipulation_score_capidx_126d_base_v146_signal(intangibles, ppnenet, assets, netinc, ncfo):
    cap = _safe_div(ppnenet + intangibles, assets)
    result = _safe_div(cap, cap.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# combined leverage+accrual+receivable composite (3-factor risk), 126d
def f36em_f36_earnings_manipulation_score_riskcomp_126d_base_v147_signal(liabilities, assets, netinc, ncfo, receivables, revenue):
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(126))
    result = (0.327 * lvgi + 4.679 * _f36_tata(netinc, ncfo, assets)
              + 0.92 * _f36_dsri(receivables, revenue, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d M-score trend (short mean minus long mean)
def f36em_f36_earnings_manipulation_score_mtrend_252d_base_v148_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
    dsri = _f36_dsri(receivables, revenue, 126)
    gmi = _f36_gmi(revenue, gp, 126)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(126))
    sgi = _f36_sgi(revenue, 126)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(126), rate)
    sg = _safe_div(sgna, revenue)
    sgai = _safe_div(sg, sg.shift(126))
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(126))
    tata = _f36_tata(netinc, ncfo, assets)
    m = (0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
         + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    result = _mean(m, 63) - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d cost-of-revenue index minus gross-margin index (cost-side aggressiveness)
def f36em_f36_earnings_manipulation_score_costgap_126d_base_v149_signal(cor, revenue, gp):
    c = _safe_div(cor, revenue)
    cori = _safe_div(c, c.shift(126))
    result = cori - _f36_gmi(revenue, gp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon DSRI composite (63/126/252)
def f36em_f36_earnings_manipulation_score_dsriblend_multi_base_v150_signal(receivables, revenue):
    result = (_f36_dsri(receivables, revenue, 63)
              + _f36_dsri(receivables, revenue, 126)
              + _f36_dsri(receivables, revenue, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36em_f36_earnings_manipulation_score_dsri_84d_base_v076_signal,
    f36em_f36_earnings_manipulation_score_dsri_189d_base_v077_signal,
    f36em_f36_earnings_manipulation_score_dsri_42d_base_v078_signal,
    f36em_f36_earnings_manipulation_score_zdsri_252d_base_v079_signal,
    f36em_f36_earnings_manipulation_score_smdsri_126d_base_v080_signal,
    f36em_f36_earnings_manipulation_score_dsridisp_126d_base_v081_signal,
    f36em_f36_earnings_manipulation_score_dsridisp_252d_base_v082_signal,
    f36em_f36_earnings_manipulation_score_gmi_84d_base_v083_signal,
    f36em_f36_earnings_manipulation_score_gmi_189d_base_v084_signal,
    f36em_f36_earnings_manipulation_score_smgmi_126d_base_v085_signal,
    f36em_f36_earnings_manipulation_score_gmidisp_126d_base_v086_signal,
    f36em_f36_earnings_manipulation_score_zgmi_126d_base_v087_signal,
    f36em_f36_earnings_manipulation_score_sgi_84d_base_v088_signal,
    f36em_f36_earnings_manipulation_score_sgi_189d_base_v089_signal,
    f36em_f36_earnings_manipulation_score_sgi_42d_base_v090_signal,
    f36em_f36_earnings_manipulation_score_smsgi_126d_base_v091_signal,
    f36em_f36_earnings_manipulation_score_sgidisp_126d_base_v092_signal,
    f36em_f36_earnings_manipulation_score_zsgi_252d_base_v093_signal,
    f36em_f36_earnings_manipulation_score_tatadisp_252d_base_v094_signal,
    f36em_f36_earnings_manipulation_score_tatadisp_126d_base_v095_signal,
    f36em_f36_earnings_manipulation_score_smtata_252d_base_v096_signal,
    f36em_f36_earnings_manipulation_score_tatachg_63d_base_v097_signal,
    f36em_f36_earnings_manipulation_score_tatachg_252d_base_v098_signal,
    f36em_f36_earnings_manipulation_score_aqi_84d_base_v099_signal,
    f36em_f36_earnings_manipulation_score_zaq_252d_base_v100_signal,
    f36em_f36_earnings_manipulation_score_intchg_252d_base_v101_signal,
    f36em_f36_earnings_manipulation_score_depi_84d_base_v102_signal,
    f36em_f36_earnings_manipulation_score_zdeprate_252d_base_v103_signal,
    f36em_f36_earnings_manipulation_score_depratechg_126d_base_v104_signal,
    f36em_f36_earnings_manipulation_score_sgai_84d_base_v105_signal,
    f36em_f36_earnings_manipulation_score_zsga_252d_base_v106_signal,
    f36em_f36_earnings_manipulation_score_sgachg_126d_base_v107_signal,
    f36em_f36_earnings_manipulation_score_lvgi_84d_base_v108_signal,
    f36em_f36_earnings_manipulation_score_zlev_252d_base_v109_signal,
    f36em_f36_earnings_manipulation_score_levchg_126d_base_v110_signal,
    f36em_f36_earnings_manipulation_score_dlvgi_252d_base_v111_signal,
    f36em_f36_earnings_manipulation_score_debtmix_063d_base_v112_signal,
    f36em_f36_earnings_manipulation_score_mscore8_84d_base_v113_signal,
    f36em_f36_earnings_manipulation_score_zmscore_252d_base_v114_signal,
    f36em_f36_earnings_manipulation_score_mrank_252d_base_v115_signal,
    f36em_f36_earnings_manipulation_score_mscore5_252d_base_v116_signal,
    f36em_f36_earnings_manipulation_score_accrsub_126d_base_v117_signal,
    f36em_f36_earnings_manipulation_score_revqual_126d_base_v118_signal,
    f36em_f36_earnings_manipulation_score_dsrisgi_252d_base_v119_signal,
    f36em_f36_earnings_manipulation_score_gmitata_126d_base_v120_signal,
    f36em_f36_earnings_manipulation_score_dsrispread_84_252_base_v121_signal,
    f36em_f36_earnings_manipulation_score_gmispread_126_252_base_v122_signal,
    f36em_f36_earnings_manipulation_score_sgispread_84_252_base_v123_signal,
    f36em_f36_earnings_manipulation_score_sgitrend_252d_base_v124_signal,
    f36em_f36_earnings_manipulation_score_lvgitrend_252d_base_v125_signal,
    f36em_f36_earnings_manipulation_score_turnidx_126d_base_v126_signal,
    f36em_f36_earnings_manipulation_score_cfmidx_126d_base_v127_signal,
    f36em_f36_earnings_manipulation_score_znetmargin_252d_base_v128_signal,
    f36em_f36_earnings_manipulation_score_discaccr_126d_base_v129_signal,
    f36em_f36_earnings_manipulation_score_zblend5_126d_base_v130_signal,
    f36em_f36_earnings_manipulation_score_zblend5_252d_base_v131_signal,
    f36em_f36_earnings_manipulation_score_dsripersgi_126d_base_v132_signal,
    f36em_f36_earnings_manipulation_score_tatapersgi_126d_base_v133_signal,
    f36em_f36_earnings_manipulation_score_gpassetidx_126d_base_v134_signal,
    f36em_f36_earnings_manipulation_score_mrank84_252d_base_v135_signal,
    f36em_f36_earnings_manipulation_score_absdsri_z252_base_v136_signal,
    f36em_f36_earnings_manipulation_score_revrec_126d_base_v137_signal,
    f36em_f36_earnings_manipulation_score_deidx_126d_base_v138_signal,
    f36em_f36_earnings_manipulation_score_mscore8_189d_base_v139_signal,
    f36em_f36_earnings_manipulation_score_accrcover_126d_base_v140_signal,
    f36em_f36_earnings_manipulation_score_ewmdsri_126d_base_v141_signal,
    f36em_f36_earnings_manipulation_score_ewmtata_126d_base_v142_signal,
    f36em_f36_earnings_manipulation_score_ewmgmi_252d_base_v143_signal,
    f36em_f36_earnings_manipulation_score_msurp_252d_base_v144_signal,
    f36em_f36_earnings_manipulation_score_zrecasset_252d_base_v145_signal,
    f36em_f36_earnings_manipulation_score_capidx_126d_base_v146_signal,
    f36em_f36_earnings_manipulation_score_riskcomp_126d_base_v147_signal,
    f36em_f36_earnings_manipulation_score_mtrend_252d_base_v148_signal,
    f36em_f36_earnings_manipulation_score_costgap_126d_base_v149_signal,
    f36em_f36_earnings_manipulation_score_dsriblend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_EARNINGS_MANIPULATION_SCORE_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f36_dsri", "_f36_tata", "_f36_gmi", "_f36_sgi")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f36_earnings_manipulation_score_base_076_150_claude: %d features pass" % n_features)
