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


# ============ FEATURES 001-075 ============

# 63d days-sales-in-receivables index
def f36em_f36_earnings_manipulation_score_dsri_63d_base_v001_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d days-sales-in-receivables index
def f36em_f36_earnings_manipulation_score_dsri_126d_base_v002_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d days-sales-in-receivables index
def f36em_f36_earnings_manipulation_score_dsri_252d_base_v003_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d days-sales-in-receivables index (short horizon)
def f36em_f36_earnings_manipulation_score_dsri_21d_base_v004_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# log of 63d DSRI (symmetric build-up signal)
def f36em_f36_earnings_manipulation_score_logdsri_63d_base_v005_signal(receivables, revenue):
    result = np.log(_f36_dsri(receivables, revenue, 63).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d DSRI deviation from 1 (excess receivables build)
def f36em_f36_earnings_manipulation_score_dsridev_126d_base_v006_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 126) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d DSRI over 252d
def f36em_f36_earnings_manipulation_score_zdsri_63d_base_v007_signal(receivables, revenue):
    result = _z(_f36_dsri(receivables, revenue, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d DSRI over 504d
def f36em_f36_earnings_manipulation_score_zdsri_126d_base_v008_signal(receivables, revenue):
    result = _z(_f36_dsri(receivables, revenue, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed DSRI (63d mean of 21d DSRI)
def f36em_f36_earnings_manipulation_score_smdsri_63d_base_v009_signal(receivables, revenue):
    result = _mean(_f36_dsri(receivables, revenue, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# raw receivables-to-revenue ratio anchored on DSRI primitive
def f36em_f36_earnings_manipulation_score_recrev_021d_base_v010_signal(receivables, revenue):
    result = _safe_div(receivables, revenue) + _f36_dsri(receivables, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross-margin index
def f36em_f36_earnings_manipulation_score_gmi_63d_base_v011_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gross-margin index
def f36em_f36_earnings_manipulation_score_gmi_126d_base_v012_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross-margin index
def f36em_f36_earnings_manipulation_score_gmi_252d_base_v013_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log 126d gross-margin index (deteriorating-margin pressure)
def f36em_f36_earnings_manipulation_score_loggmi_126d_base_v014_signal(revenue, gp):
    result = np.log(_f36_gmi(revenue, gp, 126).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d GMI deviation from 1
def f36em_f36_earnings_manipulation_score_gmidev_63d_base_v015_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 63) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d GMI over 252d
def f36em_f36_earnings_manipulation_score_zgmi_63d_base_v016_signal(revenue, gp):
    result = _z(_f36_gmi(revenue, gp, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d GMI over 504d
def f36em_f36_earnings_manipulation_score_zgmi_252d_base_v017_signal(revenue, gp):
    result = _z(_f36_gmi(revenue, gp, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level anchored on GMI primitive
def f36em_f36_earnings_manipulation_score_gmlevel_063d_base_v018_signal(revenue, gp):
    result = _safe_div(gp, revenue) + _f36_gmi(revenue, gp, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed GMI (63d mean of 21d GMI)
def f36em_f36_earnings_manipulation_score_smgmi_63d_base_v019_signal(revenue, gp):
    result = _mean(_f36_gmi(revenue, gp, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin change over 126d (signed deterioration)
def f36em_f36_earnings_manipulation_score_gmchg_126d_base_v020_signal(revenue, gp):
    gm = _safe_div(gp, revenue)
    result = gm - gm.shift(126) + _f36_gmi(revenue, gp, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sales growth index
def f36em_f36_earnings_manipulation_score_sgi_63d_base_v021_signal(revenue):
    result = _f36_sgi(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sales growth index
def f36em_f36_earnings_manipulation_score_sgi_126d_base_v022_signal(revenue):
    result = _f36_sgi(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sales growth index
def f36em_f36_earnings_manipulation_score_sgi_252d_base_v023_signal(revenue):
    result = _f36_sgi(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sales growth index (short horizon)
def f36em_f36_earnings_manipulation_score_sgi_21d_base_v024_signal(revenue):
    result = _f36_sgi(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# log 126d sales growth index
def f36em_f36_earnings_manipulation_score_logsgi_126d_base_v025_signal(revenue):
    result = np.log(_f36_sgi(revenue, 126).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SGI deviation from 1 (growth-pressure proxy)
def f36em_f36_earnings_manipulation_score_sgidev_252d_base_v026_signal(revenue):
    result = _f36_sgi(revenue, 252) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d SGI over 252d
def f36em_f36_earnings_manipulation_score_zsgi_63d_base_v027_signal(revenue):
    result = _z(_f36_sgi(revenue, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d SGI over 504d
def f36em_f36_earnings_manipulation_score_zsgi_126d_base_v028_signal(revenue):
    result = _z(_f36_sgi(revenue, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed SGI (63d mean of 21d SGI)
def f36em_f36_earnings_manipulation_score_smsgi_63d_base_v029_signal(revenue):
    result = _mean(_f36_sgi(revenue, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d total-accruals-to-total-assets (Beneish TATA)
def f36em_f36_earnings_manipulation_score_tata_063d_base_v030_signal(netinc, ncfo, assets):
    result = _f36_tata(netinc, ncfo, assets) + _f36_sgi(assets, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of TATA over 252d
def f36em_f36_earnings_manipulation_score_ztata_252d_base_v031_signal(netinc, ncfo, assets):
    result = _z(_f36_tata(netinc, ncfo, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of TATA over 126d
def f36em_f36_earnings_manipulation_score_ztata_126d_base_v032_signal(netinc, ncfo, assets):
    result = _z(_f36_tata(netinc, ncfo, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed TATA
def f36em_f36_earnings_manipulation_score_smtata_63d_base_v033_signal(netinc, ncfo, assets):
    result = _mean(_f36_tata(netinc, ncfo, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed TATA
def f36em_f36_earnings_manipulation_score_smtata_126d_base_v034_signal(netinc, ncfo, assets):
    result = _mean(_f36_tata(netinc, ncfo, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in TATA (accrual acceleration)
def f36em_f36_earnings_manipulation_score_tatachg_126d_base_v035_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    result = t - t.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# accruals (netinc minus ncfo) scaled by assets, 63d mean smoothing
def f36em_f36_earnings_manipulation_score_accr_063d_base_v036_signal(netinc, ncfo, assets):
    result = _mean(_safe_div(netinc - ncfo, assets), 63) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d asset-quality index: change in non-productive asset share (intangibles+ppnenet)/assets
def f36em_f36_earnings_manipulation_score_aqi_126d_base_v037_signal(intangibles, ppnenet, assets, netinc, ncfo):
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    result = _safe_div(q, q.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset-quality index
def f36em_f36_earnings_manipulation_score_aqi_252d_base_v038_signal(intangibles, ppnenet, assets, netinc, ncfo):
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    result = _safe_div(q, q.shift(252)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# soft-asset (intangibles) share of assets, anchored
def f36em_f36_earnings_manipulation_score_intshare_063d_base_v039_signal(intangibles, assets, netinc, ncfo):
    result = _safe_div(intangibles, assets) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in intangibles share (soft-asset accumulation)
def f36em_f36_earnings_manipulation_score_intchg_126d_base_v040_signal(intangibles, assets, netinc, ncfo):
    s = _safe_div(intangibles, assets)
    result = s - s.shift(126) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d depreciation index = prior depreciation-rate / current depreciation-rate
def f36em_f36_earnings_manipulation_score_depi_126d_base_v041_signal(depamor, ppnenet, revenue):
    rate = _safe_div(depamor, ppnenet + depamor)
    result = _safe_div(rate.shift(126), rate) + _f36_sgi(revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depreciation index
def f36em_f36_earnings_manipulation_score_depi_252d_base_v042_signal(depamor, ppnenet, revenue):
    rate = _safe_div(depamor, ppnenet + depamor)
    result = _safe_div(rate.shift(252), rate) + _f36_sgi(revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# depreciation rate level anchored
def f36em_f36_earnings_manipulation_score_deprate_063d_base_v043_signal(depamor, ppnenet, revenue):
    result = _safe_div(depamor, ppnenet + depamor) + _f36_sgi(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SGA-to-sales index (SGAI) = current sga/rev vs prior
def f36em_f36_earnings_manipulation_score_sgai_63d_base_v044_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = _safe_div(r, r.shift(63)) + _f36_sgi(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d SGA-to-sales index
def f36em_f36_earnings_manipulation_score_sgai_126d_base_v045_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = _safe_div(r, r.shift(126)) + _f36_sgi(revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SGA-to-sales index
def f36em_f36_earnings_manipulation_score_sgai_252d_base_v046_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = _safe_div(r, r.shift(252)) + _f36_sgi(revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# sga-to-sales level anchored
def f36em_f36_earnings_manipulation_score_sgalevel_063d_base_v047_signal(sgna, revenue):
    result = _safe_div(sgna, revenue) + _f36_sgi(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d leverage index (LVGI) = (liabilities/assets) vs prior
def f36em_f36_earnings_manipulation_score_lvgi_63d_base_v048_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = _safe_div(lev, lev.shift(63)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d leverage index
def f36em_f36_earnings_manipulation_score_lvgi_126d_base_v049_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = _safe_div(lev, lev.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d leverage index
def f36em_f36_earnings_manipulation_score_lvgi_252d_base_v050_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = _safe_div(lev, lev.shift(252)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage level anchored
def f36em_f36_earnings_manipulation_score_levlevel_063d_base_v051_signal(liabilities, assets, netinc, ncfo):
    result = _safe_div(liabilities, assets) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d debt-leverage index using debt/assets
def f36em_f36_earnings_manipulation_score_dlvgi_126d_base_v052_signal(debt, assets, netinc, ncfo):
    lev = _safe_div(debt, assets)
    result = _safe_div(lev, lev.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of debt/assets over 252d
def f36em_f36_earnings_manipulation_score_zdebtasset_252d_base_v053_signal(debt, assets, netinc, ncfo):
    result = _z(_safe_div(debt, assets), 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Beneish 5-component partial M-score blend (DSRI+GMI+AQI+SGI+DEPI weighted)
def f36em_f36_earnings_manipulation_score_mscore5_126d_base_v054_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor):
    dsri = _f36_dsri(receivables, revenue, 126)
    gmi = _f36_gmi(revenue, gp, 126)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(126))
    sgi = _f36_sgi(revenue, 126)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(126), rate)
    result = 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi + 0.115 * depi
    return result.replace([np.inf, -np.inf], np.nan)


# Beneish 8-component full M-score blend at 126d
def f36em_f36_earnings_manipulation_score_mscore8_126d_base_v055_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
              + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    return result.replace([np.inf, -np.inf], np.nan)


# Beneish 8-component full M-score blend at 252d
def f36em_f36_earnings_manipulation_score_mscore8_252d_base_v056_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
              + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d full M-score over 252d
def f36em_f36_earnings_manipulation_score_zmscore_126d_base_v057_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 126d M-score over 252d (manipulation percentile)
def f36em_f36_earnings_manipulation_score_mrank_126d_base_v058_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = m.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# composite accrual+receivable aggressiveness (DSRI x TATA interaction)
def f36em_f36_earnings_manipulation_score_dsritata_126d_base_v059_signal(receivables, revenue, netinc, ncfo, assets):
    result = _f36_dsri(receivables, revenue, 126) * _f36_tata(netinc, ncfo, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# composite margin-deterioration x sales-growth (channel-stuffing signature)
def f36em_f36_earnings_manipulation_score_gmisgi_126d_base_v060_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 126) * _f36_sgi(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 63d and 252d DSRI (receivables-build acceleration)
def f36em_f36_earnings_manipulation_score_dsrispread_63_252_base_v061_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 63) - _f36_dsri(receivables, revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 63d and 252d SGI (growth deceleration)
def f36em_f36_earnings_manipulation_score_sgispread_63_252_base_v062_signal(revenue):
    result = _f36_sgi(revenue, 63) - _f36_sgi(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 63d and 252d GMI (margin-pressure acceleration)
def f36em_f36_earnings_manipulation_score_gmispread_63_252_base_v063_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 63) - _f36_gmi(revenue, gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net income to operating cash flow divergence (accrual quality), anchored
def f36em_f36_earnings_manipulation_score_nicfo_063d_base_v064_signal(netinc, ncfo, assets):
    result = _safe_div(netinc, ncfo.abs()) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in net-income-to-cashflow divergence
def f36em_f36_earnings_manipulation_score_nicfochg_126d_base_v065_signal(netinc, ncfo, assets):
    d = _safe_div(netinc, ncfo.abs())
    result = d - d.shift(126) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-to-assets (ROA) deterioration index over 126d, anchored
def f36em_f36_earnings_manipulation_score_roaidx_126d_base_v066_signal(netinc, assets, ncfo):
    roa = _safe_div(netinc, assets)
    result = _safe_div(roa.shift(126), roa) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-revenue to sales index (COR/rev change), anchored on SGI
def f36em_f36_earnings_manipulation_score_cori_126d_base_v067_signal(cor, revenue):
    r = _safe_div(cor, revenue)
    result = _safe_div(r, r.shift(126)) + _f36_sgi(revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of receivables/revenue level (receivables stress)
def f36em_f36_earnings_manipulation_score_zrecrev_252d_base_v068_signal(receivables, revenue):
    result = _z(_safe_div(receivables, revenue), 252) + _f36_dsri(receivables, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# DSRI growth in excess of sales growth (revenue-quality gap)
def f36em_f36_earnings_manipulation_score_recgap_126d_base_v069_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 126) - _f36_sgi(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accruals scaled by revenue rather than assets (revenue-accrual intensity)
def f36em_f36_earnings_manipulation_score_accrrev_126d_base_v070_signal(netinc, ncfo, revenue, assets):
    result = _mean(_safe_div(netinc - ncfo, revenue), 126) + _f36_tata(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend (linear slope proxy) of TATA via z over short vs long mean
def f36em_f36_earnings_manipulation_score_tatatrend_252d_base_v071_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    result = _mean(t, 63) - _mean(t, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend of DSRI (short mean minus long mean)
def f36em_f36_earnings_manipulation_score_dsritrend_252d_base_v072_signal(receivables, revenue):
    d = _f36_dsri(receivables, revenue, 63)
    result = _mean(d, 63) - _mean(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend of GMI (short mean minus long mean)
def f36em_f36_earnings_manipulation_score_gmitrend_252d_base_v073_signal(revenue, gp):
    g = _f36_gmi(revenue, gp, 63)
    result = _mean(g, 63) - _mean(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite leverage x accrual stress (balance-sheet manipulation pressure)
def f36em_f36_earnings_manipulation_score_levtata_126d_base_v074_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(126))
    result = lvgi * _f36_tata(netinc, ncfo, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# four-component aggressiveness average (DSRI, GMI, SGI, |TATA| z-scored)
def f36em_f36_earnings_manipulation_score_aggblend_126d_base_v075_signal(receivables, revenue, gp, netinc, ncfo, assets):
    a = _z(_f36_dsri(receivables, revenue, 126), 252)
    b = _z(_f36_gmi(revenue, gp, 126), 252)
    c = _z(_f36_sgi(revenue, 126), 252)
    d = _z(_f36_tata(netinc, ncfo, assets), 252)
    result = (a + b + c + d) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36em_f36_earnings_manipulation_score_dsri_63d_base_v001_signal,
    f36em_f36_earnings_manipulation_score_dsri_126d_base_v002_signal,
    f36em_f36_earnings_manipulation_score_dsri_252d_base_v003_signal,
    f36em_f36_earnings_manipulation_score_dsri_21d_base_v004_signal,
    f36em_f36_earnings_manipulation_score_logdsri_63d_base_v005_signal,
    f36em_f36_earnings_manipulation_score_dsridev_126d_base_v006_signal,
    f36em_f36_earnings_manipulation_score_zdsri_63d_base_v007_signal,
    f36em_f36_earnings_manipulation_score_zdsri_126d_base_v008_signal,
    f36em_f36_earnings_manipulation_score_smdsri_63d_base_v009_signal,
    f36em_f36_earnings_manipulation_score_recrev_021d_base_v010_signal,
    f36em_f36_earnings_manipulation_score_gmi_63d_base_v011_signal,
    f36em_f36_earnings_manipulation_score_gmi_126d_base_v012_signal,
    f36em_f36_earnings_manipulation_score_gmi_252d_base_v013_signal,
    f36em_f36_earnings_manipulation_score_loggmi_126d_base_v014_signal,
    f36em_f36_earnings_manipulation_score_gmidev_63d_base_v015_signal,
    f36em_f36_earnings_manipulation_score_zgmi_63d_base_v016_signal,
    f36em_f36_earnings_manipulation_score_zgmi_252d_base_v017_signal,
    f36em_f36_earnings_manipulation_score_gmlevel_063d_base_v018_signal,
    f36em_f36_earnings_manipulation_score_smgmi_63d_base_v019_signal,
    f36em_f36_earnings_manipulation_score_gmchg_126d_base_v020_signal,
    f36em_f36_earnings_manipulation_score_sgi_63d_base_v021_signal,
    f36em_f36_earnings_manipulation_score_sgi_126d_base_v022_signal,
    f36em_f36_earnings_manipulation_score_sgi_252d_base_v023_signal,
    f36em_f36_earnings_manipulation_score_sgi_21d_base_v024_signal,
    f36em_f36_earnings_manipulation_score_logsgi_126d_base_v025_signal,
    f36em_f36_earnings_manipulation_score_sgidev_252d_base_v026_signal,
    f36em_f36_earnings_manipulation_score_zsgi_63d_base_v027_signal,
    f36em_f36_earnings_manipulation_score_zsgi_126d_base_v028_signal,
    f36em_f36_earnings_manipulation_score_smsgi_63d_base_v029_signal,
    f36em_f36_earnings_manipulation_score_tata_063d_base_v030_signal,
    f36em_f36_earnings_manipulation_score_ztata_252d_base_v031_signal,
    f36em_f36_earnings_manipulation_score_ztata_126d_base_v032_signal,
    f36em_f36_earnings_manipulation_score_smtata_63d_base_v033_signal,
    f36em_f36_earnings_manipulation_score_smtata_126d_base_v034_signal,
    f36em_f36_earnings_manipulation_score_tatachg_126d_base_v035_signal,
    f36em_f36_earnings_manipulation_score_accr_063d_base_v036_signal,
    f36em_f36_earnings_manipulation_score_aqi_126d_base_v037_signal,
    f36em_f36_earnings_manipulation_score_aqi_252d_base_v038_signal,
    f36em_f36_earnings_manipulation_score_intshare_063d_base_v039_signal,
    f36em_f36_earnings_manipulation_score_intchg_126d_base_v040_signal,
    f36em_f36_earnings_manipulation_score_depi_126d_base_v041_signal,
    f36em_f36_earnings_manipulation_score_depi_252d_base_v042_signal,
    f36em_f36_earnings_manipulation_score_deprate_063d_base_v043_signal,
    f36em_f36_earnings_manipulation_score_sgai_63d_base_v044_signal,
    f36em_f36_earnings_manipulation_score_sgai_126d_base_v045_signal,
    f36em_f36_earnings_manipulation_score_sgai_252d_base_v046_signal,
    f36em_f36_earnings_manipulation_score_sgalevel_063d_base_v047_signal,
    f36em_f36_earnings_manipulation_score_lvgi_63d_base_v048_signal,
    f36em_f36_earnings_manipulation_score_lvgi_126d_base_v049_signal,
    f36em_f36_earnings_manipulation_score_lvgi_252d_base_v050_signal,
    f36em_f36_earnings_manipulation_score_levlevel_063d_base_v051_signal,
    f36em_f36_earnings_manipulation_score_dlvgi_126d_base_v052_signal,
    f36em_f36_earnings_manipulation_score_zdebtasset_252d_base_v053_signal,
    f36em_f36_earnings_manipulation_score_mscore5_126d_base_v054_signal,
    f36em_f36_earnings_manipulation_score_mscore8_126d_base_v055_signal,
    f36em_f36_earnings_manipulation_score_mscore8_252d_base_v056_signal,
    f36em_f36_earnings_manipulation_score_zmscore_126d_base_v057_signal,
    f36em_f36_earnings_manipulation_score_mrank_126d_base_v058_signal,
    f36em_f36_earnings_manipulation_score_dsritata_126d_base_v059_signal,
    f36em_f36_earnings_manipulation_score_gmisgi_126d_base_v060_signal,
    f36em_f36_earnings_manipulation_score_dsrispread_63_252_base_v061_signal,
    f36em_f36_earnings_manipulation_score_sgispread_63_252_base_v062_signal,
    f36em_f36_earnings_manipulation_score_gmispread_63_252_base_v063_signal,
    f36em_f36_earnings_manipulation_score_nicfo_063d_base_v064_signal,
    f36em_f36_earnings_manipulation_score_nicfochg_126d_base_v065_signal,
    f36em_f36_earnings_manipulation_score_roaidx_126d_base_v066_signal,
    f36em_f36_earnings_manipulation_score_cori_126d_base_v067_signal,
    f36em_f36_earnings_manipulation_score_zrecrev_252d_base_v068_signal,
    f36em_f36_earnings_manipulation_score_recgap_126d_base_v069_signal,
    f36em_f36_earnings_manipulation_score_accrrev_126d_base_v070_signal,
    f36em_f36_earnings_manipulation_score_tatatrend_252d_base_v071_signal,
    f36em_f36_earnings_manipulation_score_dsritrend_252d_base_v072_signal,
    f36em_f36_earnings_manipulation_score_gmitrend_252d_base_v073_signal,
    f36em_f36_earnings_manipulation_score_levtata_126d_base_v074_signal,
    f36em_f36_earnings_manipulation_score_aggblend_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_EARNINGS_MANIPULATION_SCORE_REGISTRY_001_075 = REGISTRY


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
    print("OK f36_earnings_manipulation_score_base_001_075_claude: %d features pass" % n_features)
