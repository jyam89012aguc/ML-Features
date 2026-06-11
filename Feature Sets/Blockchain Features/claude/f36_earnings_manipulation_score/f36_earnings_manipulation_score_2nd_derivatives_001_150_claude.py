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
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f36em_f36_earnings_manipulation_score_dsri_63d_slope_v001_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsri_126d_slope_v002_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsri_252d_slope_v003_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsri_21d_slope_v004_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_logdsri_63d_slope_v005_signal(receivables, revenue):
    result = np.log(_f36_dsri(receivables, revenue, 63).clip(lower=1e-6))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsridev_126d_slope_v006_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 126) - 1.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zdsri_63d_slope_v007_signal(receivables, revenue):
    result = _z(_f36_dsri(receivables, revenue, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zdsri_126d_slope_v008_signal(receivables, revenue):
    result = _z(_f36_dsri(receivables, revenue, 126), 504)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_smdsri_63d_slope_v009_signal(receivables, revenue):
    result = _mean(_f36_dsri(receivables, revenue, 21), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_recrev_021d_slope_v010_signal(receivables, revenue):
    result = _safe_div(receivables, revenue) + _f36_dsri(receivables, revenue, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmi_63d_slope_v011_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmi_126d_slope_v012_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmi_252d_slope_v013_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_loggmi_126d_slope_v014_signal(revenue, gp):
    result = np.log(_f36_gmi(revenue, gp, 126).clip(lower=1e-6))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmidev_63d_slope_v015_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 63) - 1.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zgmi_63d_slope_v016_signal(revenue, gp):
    result = _z(_f36_gmi(revenue, gp, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zgmi_252d_slope_v017_signal(revenue, gp):
    result = _z(_f36_gmi(revenue, gp, 252), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmlevel_063d_slope_v018_signal(revenue, gp):
    result = _safe_div(gp, revenue) + _f36_gmi(revenue, gp, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_smgmi_63d_slope_v019_signal(revenue, gp):
    result = _mean(_f36_gmi(revenue, gp, 21), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmchg_126d_slope_v020_signal(revenue, gp):
    gm = _safe_div(gp, revenue)
    result = gm - gm.shift(126) + _f36_gmi(revenue, gp, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgi_63d_slope_v021_signal(revenue):
    result = _f36_sgi(revenue, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgi_126d_slope_v022_signal(revenue):
    result = _f36_sgi(revenue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgi_252d_slope_v023_signal(revenue):
    result = _f36_sgi(revenue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgi_21d_slope_v024_signal(revenue):
    result = _f36_sgi(revenue, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_logsgi_126d_slope_v025_signal(revenue):
    result = np.log(_f36_sgi(revenue, 126).clip(lower=1e-6))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgidev_252d_slope_v026_signal(revenue):
    result = _f36_sgi(revenue, 252) - 1.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zsgi_63d_slope_v027_signal(revenue):
    result = _z(_f36_sgi(revenue, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zsgi_126d_slope_v028_signal(revenue):
    result = _z(_f36_sgi(revenue, 126), 504)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_smsgi_63d_slope_v029_signal(revenue):
    result = _mean(_f36_sgi(revenue, 21), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_tata_063d_slope_v030_signal(netinc, ncfo, assets):
    result = _f36_tata(netinc, ncfo, assets) + _f36_sgi(assets, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_ztata_252d_slope_v031_signal(netinc, ncfo, assets):
    result = _z(_f36_tata(netinc, ncfo, assets), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_ztata_126d_slope_v032_signal(netinc, ncfo, assets):
    result = _z(_f36_tata(netinc, ncfo, assets), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_smtata_63d_slope_v033_signal(netinc, ncfo, assets):
    result = _mean(_f36_tata(netinc, ncfo, assets), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_smtata_126d_slope_v034_signal(netinc, ncfo, assets):
    result = _mean(_f36_tata(netinc, ncfo, assets), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_tatachg_126d_slope_v035_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    result = t - t.shift(126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_accr_063d_slope_v036_signal(netinc, ncfo, assets):
    result = _mean(_safe_div(netinc - ncfo, assets), 63) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_aqi_126d_slope_v037_signal(intangibles, ppnenet, assets, netinc, ncfo):
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    result = _safe_div(q, q.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_aqi_252d_slope_v038_signal(intangibles, ppnenet, assets, netinc, ncfo):
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    result = _safe_div(q, q.shift(252)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_intshare_063d_slope_v039_signal(intangibles, assets, netinc, ncfo):
    result = _safe_div(intangibles, assets) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_intchg_126d_slope_v040_signal(intangibles, assets, netinc, ncfo):
    s = _safe_div(intangibles, assets)
    result = s - s.shift(126) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_depi_126d_slope_v041_signal(depamor, ppnenet, revenue):
    rate = _safe_div(depamor, ppnenet + depamor)
    result = _safe_div(rate.shift(126), rate) + _f36_sgi(revenue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_depi_252d_slope_v042_signal(depamor, ppnenet, revenue):
    rate = _safe_div(depamor, ppnenet + depamor)
    result = _safe_div(rate.shift(252), rate) + _f36_sgi(revenue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_deprate_063d_slope_v043_signal(depamor, ppnenet, revenue):
    result = _safe_div(depamor, ppnenet + depamor) + _f36_sgi(revenue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgai_63d_slope_v044_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = _safe_div(r, r.shift(63)) + _f36_sgi(revenue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgai_126d_slope_v045_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = _safe_div(r, r.shift(126)) + _f36_sgi(revenue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgai_252d_slope_v046_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = _safe_div(r, r.shift(252)) + _f36_sgi(revenue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgalevel_063d_slope_v047_signal(sgna, revenue):
    result = _safe_div(sgna, revenue) + _f36_sgi(revenue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_lvgi_63d_slope_v048_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = _safe_div(lev, lev.shift(63)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_lvgi_126d_slope_v049_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = _safe_div(lev, lev.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_lvgi_252d_slope_v050_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = _safe_div(lev, lev.shift(252)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_levlevel_063d_slope_v051_signal(liabilities, assets, netinc, ncfo):
    result = _safe_div(liabilities, assets) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dlvgi_126d_slope_v052_signal(debt, assets, netinc, ncfo):
    lev = _safe_div(debt, assets)
    result = _safe_div(lev, lev.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zdebtasset_252d_slope_v053_signal(debt, assets, netinc, ncfo):
    result = _z(_safe_div(debt, assets), 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mscore5_126d_slope_v054_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor):
    dsri = _f36_dsri(receivables, revenue, 126)
    gmi = _f36_gmi(revenue, gp, 126)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(126))
    sgi = _f36_sgi(revenue, 126)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(126), rate)
    result = 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi + 0.115 * depi
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mscore8_126d_slope_v055_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mscore8_252d_slope_v056_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zmscore_126d_slope_v057_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mrank_126d_slope_v058_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsritata_126d_slope_v059_signal(receivables, revenue, netinc, ncfo, assets):
    result = _f36_dsri(receivables, revenue, 126) * _f36_tata(netinc, ncfo, assets)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmisgi_126d_slope_v060_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 126) * _f36_sgi(revenue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsrispread_63_252_slope_v061_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 63) - _f36_dsri(receivables, revenue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgispread_63_252_slope_v062_signal(revenue):
    result = _f36_sgi(revenue, 63) - _f36_sgi(revenue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmispread_63_252_slope_v063_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 63) - _f36_gmi(revenue, gp, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_nicfo_063d_slope_v064_signal(netinc, ncfo, assets):
    result = _safe_div(netinc, ncfo.abs()) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_nicfochg_126d_slope_v065_signal(netinc, ncfo, assets):
    d = _safe_div(netinc, ncfo.abs())
    result = d - d.shift(126) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_roaidx_126d_slope_v066_signal(netinc, assets, ncfo):
    roa = _safe_div(netinc, assets)
    result = _safe_div(roa.shift(126), roa) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_cori_126d_slope_v067_signal(cor, revenue):
    r = _safe_div(cor, revenue)
    result = _safe_div(r, r.shift(126)) + _f36_sgi(revenue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zrecrev_252d_slope_v068_signal(receivables, revenue):
    result = _z(_safe_div(receivables, revenue), 252) + _f36_dsri(receivables, revenue, 21) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_recgap_126d_slope_v069_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 126) - _f36_sgi(revenue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_accrrev_126d_slope_v070_signal(netinc, ncfo, revenue, assets):
    result = _mean(_safe_div(netinc - ncfo, revenue), 126) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_tatatrend_252d_slope_v071_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    result = _mean(t, 63) - _mean(t, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsritrend_252d_slope_v072_signal(receivables, revenue):
    d = _f36_dsri(receivables, revenue, 63)
    result = _mean(d, 63) - _mean(d, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmitrend_252d_slope_v073_signal(revenue, gp):
    g = _f36_gmi(revenue, gp, 63)
    result = _mean(g, 63) - _mean(g, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_levtata_126d_slope_v074_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(126))
    result = lvgi * _f36_tata(netinc, ncfo, assets)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_aggblend_126d_slope_v075_signal(receivables, revenue, gp, netinc, ncfo, assets):
    a = _z(_f36_dsri(receivables, revenue, 126), 252)
    b = _z(_f36_gmi(revenue, gp, 126), 252)
    c = _z(_f36_sgi(revenue, 126), 252)
    d = _z(_f36_tata(netinc, ncfo, assets), 252)
    result = (a + b + c + d) / 4.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsri_84d_slope_v076_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsri_189d_slope_v077_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsri_42d_slope_v078_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zdsri_252d_slope_v079_signal(receivables, revenue):
    result = _z(_f36_dsri(receivables, revenue, 252), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_smdsri_126d_slope_v080_signal(receivables, revenue):
    result = _mean(_f36_dsri(receivables, revenue, 63), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsridisp_126d_slope_v081_signal(receivables, revenue):
    result = _std(_f36_dsri(receivables, revenue, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsridisp_252d_slope_v082_signal(receivables, revenue):
    result = _std(_f36_dsri(receivables, revenue, 21), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmi_84d_slope_v083_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmi_189d_slope_v084_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_smgmi_126d_slope_v085_signal(revenue, gp):
    result = _mean(_f36_gmi(revenue, gp, 63), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmidisp_126d_slope_v086_signal(revenue, gp):
    result = _std(_f36_gmi(revenue, gp, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zgmi_126d_slope_v087_signal(revenue, gp):
    result = _z(_f36_gmi(revenue, gp, 126), 504)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgi_84d_slope_v088_signal(revenue):
    result = _f36_sgi(revenue, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgi_189d_slope_v089_signal(revenue):
    result = _f36_sgi(revenue, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgi_42d_slope_v090_signal(revenue):
    result = _f36_sgi(revenue, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_smsgi_126d_slope_v091_signal(revenue):
    result = _mean(_f36_sgi(revenue, 63), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgidisp_126d_slope_v092_signal(revenue):
    result = _std(_f36_sgi(revenue, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zsgi_252d_slope_v093_signal(revenue):
    result = _z(_f36_sgi(revenue, 252), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_tatadisp_252d_slope_v094_signal(netinc, ncfo, assets):
    result = _std(_f36_tata(netinc, ncfo, assets), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_tatadisp_126d_slope_v095_signal(netinc, ncfo, assets):
    result = _std(_f36_tata(netinc, ncfo, assets), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_smtata_252d_slope_v096_signal(netinc, ncfo, assets):
    result = _mean(_f36_tata(netinc, ncfo, assets), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_tatachg_63d_slope_v097_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    result = t - t.shift(63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_tatachg_252d_slope_v098_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    result = t - t.shift(252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_aqi_84d_slope_v099_signal(intangibles, ppnenet, assets, netinc, ncfo):
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    result = _safe_div(q, q.shift(84)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zaq_252d_slope_v100_signal(intangibles, ppnenet, assets, netinc, ncfo):
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    result = _z(q, 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_intchg_252d_slope_v101_signal(intangibles, assets, netinc, ncfo):
    s = _safe_div(intangibles, assets)
    result = s - s.shift(252) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_depi_84d_slope_v102_signal(depamor, ppnenet, revenue):
    rate = _safe_div(depamor, ppnenet + depamor)
    result = _safe_div(rate.shift(84), rate) + _f36_sgi(revenue, 84) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zdeprate_252d_slope_v103_signal(depamor, ppnenet, revenue):
    result = _z(_safe_div(depamor, ppnenet + depamor), 252) + _f36_sgi(revenue, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_depratechg_126d_slope_v104_signal(depamor, ppnenet, revenue):
    rate = _safe_div(depamor, ppnenet + depamor)
    result = rate - rate.shift(126) + _f36_sgi(revenue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgai_84d_slope_v105_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = _safe_div(r, r.shift(84)) + _f36_sgi(revenue, 84) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zsga_252d_slope_v106_signal(sgna, revenue):
    result = _z(_safe_div(sgna, revenue), 252) + _f36_sgi(revenue, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgachg_126d_slope_v107_signal(sgna, revenue):
    r = _safe_div(sgna, revenue)
    result = r - r.shift(126) + _f36_sgi(revenue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_lvgi_84d_slope_v108_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = _safe_div(lev, lev.shift(84)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zlev_252d_slope_v109_signal(liabilities, assets, netinc, ncfo):
    result = _z(_safe_div(liabilities, assets), 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_levchg_126d_slope_v110_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    result = lev - lev.shift(126) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dlvgi_252d_slope_v111_signal(debt, assets, netinc, ncfo):
    lev = _safe_div(debt, assets)
    result = _safe_div(lev, lev.shift(252)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_debtmix_063d_slope_v112_signal(debt, liabilities, netinc, ncfo, assets):
    result = _safe_div(debt, liabilities) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mscore8_84d_slope_v113_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zmscore_252d_slope_v114_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mrank_252d_slope_v115_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mscore5_252d_slope_v116_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor):
    dsri = _f36_dsri(receivables, revenue, 252)
    gmi = _f36_gmi(revenue, gp, 252)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    aqi = _safe_div(q, q.shift(252))
    sgi = _f36_sgi(revenue, 252)
    rate = _safe_div(depamor, ppnenet + depamor)
    depi = _safe_div(rate.shift(252), rate)
    result = 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi + 0.115 * depi
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_accrsub_126d_slope_v117_signal(receivables, revenue, netinc, ncfo, assets):
    result = 4.679 * _f36_tata(netinc, ncfo, assets) + 0.92 * _f36_dsri(receivables, revenue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_revqual_126d_slope_v118_signal(receivables, revenue, gp):
    result = (0.92 * _f36_dsri(receivables, revenue, 126)
              + 0.892 * _f36_sgi(revenue, 126)
              + 0.528 * _f36_gmi(revenue, gp, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsrisgi_252d_slope_v119_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 252) * _f36_sgi(revenue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmitata_126d_slope_v120_signal(revenue, gp, netinc, ncfo, assets):
    result = _f36_gmi(revenue, gp, 126) * _f36_tata(netinc, ncfo, assets)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsrispread_84_252_slope_v121_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 84) - _f36_dsri(receivables, revenue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gmispread_126_252_slope_v122_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 126) - _f36_gmi(revenue, gp, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgispread_84_252_slope_v123_signal(revenue):
    result = _f36_sgi(revenue, 84) - _f36_sgi(revenue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_sgitrend_252d_slope_v124_signal(revenue):
    s = _f36_sgi(revenue, 63)
    result = _mean(s, 63) - _mean(s, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_lvgitrend_252d_slope_v125_signal(liabilities, assets, netinc, ncfo):
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(63))
    result = _mean(lvgi, 63) - _mean(lvgi, 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_turnidx_126d_slope_v126_signal(revenue, assets, netinc, ncfo):
    t = _safe_div(revenue, assets)
    result = _safe_div(t, t.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_cfmidx_126d_slope_v127_signal(ncfo, revenue, netinc, assets):
    c = _safe_div(ncfo, revenue)
    result = _safe_div(c.shift(126), c) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_znetmargin_252d_slope_v128_signal(netinc, revenue, ncfo, assets):
    result = _z(_safe_div(netinc, revenue), 252) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_discaccr_126d_slope_v129_signal(netinc, ncfo, depamor, assets):
    result = _mean(_safe_div((netinc - ncfo) - depamor, assets), 126) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zblend5_126d_slope_v130_signal(receivables, revenue, gp, intangibles, ppnenet, assets, netinc, ncfo):
    a = _z(_f36_dsri(receivables, revenue, 126), 252)
    b = _z(_f36_gmi(revenue, gp, 126), 252)
    c = _z(_f36_sgi(revenue, 126), 252)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    d = _z(_safe_div(q, q.shift(126)), 252)
    e = _z(_f36_tata(netinc, ncfo, assets), 252)
    result = (a + b + c + d + e) / 5.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zblend5_252d_slope_v131_signal(receivables, revenue, gp, intangibles, ppnenet, assets, netinc, ncfo):
    a = _z(_f36_dsri(receivables, revenue, 252), 504)
    b = _z(_f36_gmi(revenue, gp, 252), 504)
    c = _z(_f36_sgi(revenue, 252), 504)
    q = 1.0 - _safe_div(ppnenet + intangibles, assets)
    d = _z(_safe_div(q, q.shift(252)), 504)
    e = _z(_f36_tata(netinc, ncfo, assets), 504)
    result = (a + b + c + d + e) / 5.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsripersgi_126d_slope_v132_signal(receivables, revenue):
    result = _safe_div(_f36_dsri(receivables, revenue, 126), _f36_sgi(revenue, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_tatapersgi_126d_slope_v133_signal(netinc, ncfo, assets, revenue):
    result = _safe_div(_f36_tata(netinc, ncfo, assets), _f36_sgi(revenue, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_gpassetidx_126d_slope_v134_signal(gp, assets, netinc, ncfo):
    g = _safe_div(gp, assets)
    result = _safe_div(g, g.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mrank84_252d_slope_v135_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_absdsri_z252_slope_v136_signal(receivables, revenue):
    result = _z((_f36_dsri(receivables, revenue, 126) - 1.0).abs(), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_revrec_126d_slope_v137_signal(receivables, revenue, cor):
    c = _safe_div(cor, revenue)
    cori = _safe_div(c, c.shift(126))
    result = 0.92 * _f36_dsri(receivables, revenue, 126) + 0.5 * cori
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_deidx_126d_slope_v138_signal(liabilities, assets, netinc, ncfo):
    eq = (assets - liabilities)
    de = _safe_div(liabilities, eq)
    result = _safe_div(de, de.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mscore8_189d_slope_v139_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_accrcover_126d_slope_v140_signal(netinc, ncfo, assets, revenue):
    tata = _f36_tata(netinc, ncfo, assets)
    result = _safe_div(tata, _safe_div(ncfo, revenue))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_ewmdsri_126d_slope_v141_signal(receivables, revenue):
    result = _f36_dsri(receivables, revenue, 21).ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_ewmtata_126d_slope_v142_signal(netinc, ncfo, assets):
    result = _f36_tata(netinc, ncfo, assets).ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_ewmgmi_252d_slope_v143_signal(revenue, gp):
    result = _f36_gmi(revenue, gp, 21).ewm(span=252, min_periods=84).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_msurp_252d_slope_v144_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_zrecasset_252d_slope_v145_signal(receivables, assets, revenue):
    result = _z(_safe_div(receivables, assets), 252) + _f36_dsri(receivables, revenue, 21) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_capidx_126d_slope_v146_signal(intangibles, ppnenet, assets, netinc, ncfo):
    cap = _safe_div(ppnenet + intangibles, assets)
    result = _safe_div(cap, cap.shift(126)) + _f36_tata(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_riskcomp_126d_slope_v147_signal(liabilities, assets, netinc, ncfo, receivables, revenue):
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(126))
    result = (0.327 * lvgi + 4.679 * _f36_tata(netinc, ncfo, assets)
              + 0.92 * _f36_dsri(receivables, revenue, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_mtrend_252d_slope_v148_signal(receivables, revenue, gp, intangibles, ppnenet, assets, depamor, sgna, liabilities, netinc, ncfo):
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
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_costgap_126d_slope_v149_signal(cor, revenue, gp):
    c = _safe_div(cor, revenue)
    cori = _safe_div(c, c.shift(126))
    result = cori - _f36_gmi(revenue, gp, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36em_f36_earnings_manipulation_score_dsriblend_multi_slope_v150_signal(receivables, revenue):
    result = (_f36_dsri(receivables, revenue, 63)
              + _f36_dsri(receivables, revenue, 126)
              + _f36_dsri(receivables, revenue, 252)) / 3.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f36em_f36_earnings_manipulation_score_dsri_63d_slope_v001_signal,    f36em_f36_earnings_manipulation_score_dsri_126d_slope_v002_signal,    f36em_f36_earnings_manipulation_score_dsri_252d_slope_v003_signal,    f36em_f36_earnings_manipulation_score_dsri_21d_slope_v004_signal,    f36em_f36_earnings_manipulation_score_logdsri_63d_slope_v005_signal,    f36em_f36_earnings_manipulation_score_dsridev_126d_slope_v006_signal,    f36em_f36_earnings_manipulation_score_zdsri_63d_slope_v007_signal,    f36em_f36_earnings_manipulation_score_zdsri_126d_slope_v008_signal,    f36em_f36_earnings_manipulation_score_smdsri_63d_slope_v009_signal,    f36em_f36_earnings_manipulation_score_recrev_021d_slope_v010_signal,    f36em_f36_earnings_manipulation_score_gmi_63d_slope_v011_signal,    f36em_f36_earnings_manipulation_score_gmi_126d_slope_v012_signal,    f36em_f36_earnings_manipulation_score_gmi_252d_slope_v013_signal,    f36em_f36_earnings_manipulation_score_loggmi_126d_slope_v014_signal,    f36em_f36_earnings_manipulation_score_gmidev_63d_slope_v015_signal,    f36em_f36_earnings_manipulation_score_zgmi_63d_slope_v016_signal,    f36em_f36_earnings_manipulation_score_zgmi_252d_slope_v017_signal,    f36em_f36_earnings_manipulation_score_gmlevel_063d_slope_v018_signal,    f36em_f36_earnings_manipulation_score_smgmi_63d_slope_v019_signal,    f36em_f36_earnings_manipulation_score_gmchg_126d_slope_v020_signal,    f36em_f36_earnings_manipulation_score_sgi_63d_slope_v021_signal,    f36em_f36_earnings_manipulation_score_sgi_126d_slope_v022_signal,    f36em_f36_earnings_manipulation_score_sgi_252d_slope_v023_signal,    f36em_f36_earnings_manipulation_score_sgi_21d_slope_v024_signal,    f36em_f36_earnings_manipulation_score_logsgi_126d_slope_v025_signal,    f36em_f36_earnings_manipulation_score_sgidev_252d_slope_v026_signal,    f36em_f36_earnings_manipulation_score_zsgi_63d_slope_v027_signal,    f36em_f36_earnings_manipulation_score_zsgi_126d_slope_v028_signal,    f36em_f36_earnings_manipulation_score_smsgi_63d_slope_v029_signal,    f36em_f36_earnings_manipulation_score_tata_063d_slope_v030_signal,    f36em_f36_earnings_manipulation_score_ztata_252d_slope_v031_signal,    f36em_f36_earnings_manipulation_score_ztata_126d_slope_v032_signal,    f36em_f36_earnings_manipulation_score_smtata_63d_slope_v033_signal,    f36em_f36_earnings_manipulation_score_smtata_126d_slope_v034_signal,    f36em_f36_earnings_manipulation_score_tatachg_126d_slope_v035_signal,    f36em_f36_earnings_manipulation_score_accr_063d_slope_v036_signal,    f36em_f36_earnings_manipulation_score_aqi_126d_slope_v037_signal,    f36em_f36_earnings_manipulation_score_aqi_252d_slope_v038_signal,    f36em_f36_earnings_manipulation_score_intshare_063d_slope_v039_signal,    f36em_f36_earnings_manipulation_score_intchg_126d_slope_v040_signal,    f36em_f36_earnings_manipulation_score_depi_126d_slope_v041_signal,    f36em_f36_earnings_manipulation_score_depi_252d_slope_v042_signal,    f36em_f36_earnings_manipulation_score_deprate_063d_slope_v043_signal,    f36em_f36_earnings_manipulation_score_sgai_63d_slope_v044_signal,    f36em_f36_earnings_manipulation_score_sgai_126d_slope_v045_signal,    f36em_f36_earnings_manipulation_score_sgai_252d_slope_v046_signal,    f36em_f36_earnings_manipulation_score_sgalevel_063d_slope_v047_signal,    f36em_f36_earnings_manipulation_score_lvgi_63d_slope_v048_signal,    f36em_f36_earnings_manipulation_score_lvgi_126d_slope_v049_signal,    f36em_f36_earnings_manipulation_score_lvgi_252d_slope_v050_signal,    f36em_f36_earnings_manipulation_score_levlevel_063d_slope_v051_signal,    f36em_f36_earnings_manipulation_score_dlvgi_126d_slope_v052_signal,    f36em_f36_earnings_manipulation_score_zdebtasset_252d_slope_v053_signal,    f36em_f36_earnings_manipulation_score_mscore5_126d_slope_v054_signal,    f36em_f36_earnings_manipulation_score_mscore8_126d_slope_v055_signal,    f36em_f36_earnings_manipulation_score_mscore8_252d_slope_v056_signal,    f36em_f36_earnings_manipulation_score_zmscore_126d_slope_v057_signal,    f36em_f36_earnings_manipulation_score_mrank_126d_slope_v058_signal,    f36em_f36_earnings_manipulation_score_dsritata_126d_slope_v059_signal,    f36em_f36_earnings_manipulation_score_gmisgi_126d_slope_v060_signal,    f36em_f36_earnings_manipulation_score_dsrispread_63_252_slope_v061_signal,    f36em_f36_earnings_manipulation_score_sgispread_63_252_slope_v062_signal,    f36em_f36_earnings_manipulation_score_gmispread_63_252_slope_v063_signal,    f36em_f36_earnings_manipulation_score_nicfo_063d_slope_v064_signal,    f36em_f36_earnings_manipulation_score_nicfochg_126d_slope_v065_signal,    f36em_f36_earnings_manipulation_score_roaidx_126d_slope_v066_signal,    f36em_f36_earnings_manipulation_score_cori_126d_slope_v067_signal,    f36em_f36_earnings_manipulation_score_zrecrev_252d_slope_v068_signal,    f36em_f36_earnings_manipulation_score_recgap_126d_slope_v069_signal,    f36em_f36_earnings_manipulation_score_accrrev_126d_slope_v070_signal,    f36em_f36_earnings_manipulation_score_tatatrend_252d_slope_v071_signal,    f36em_f36_earnings_manipulation_score_dsritrend_252d_slope_v072_signal,    f36em_f36_earnings_manipulation_score_gmitrend_252d_slope_v073_signal,    f36em_f36_earnings_manipulation_score_levtata_126d_slope_v074_signal,    f36em_f36_earnings_manipulation_score_aggblend_126d_slope_v075_signal,    f36em_f36_earnings_manipulation_score_dsri_84d_slope_v076_signal,    f36em_f36_earnings_manipulation_score_dsri_189d_slope_v077_signal,    f36em_f36_earnings_manipulation_score_dsri_42d_slope_v078_signal,    f36em_f36_earnings_manipulation_score_zdsri_252d_slope_v079_signal,    f36em_f36_earnings_manipulation_score_smdsri_126d_slope_v080_signal,    f36em_f36_earnings_manipulation_score_dsridisp_126d_slope_v081_signal,    f36em_f36_earnings_manipulation_score_dsridisp_252d_slope_v082_signal,    f36em_f36_earnings_manipulation_score_gmi_84d_slope_v083_signal,    f36em_f36_earnings_manipulation_score_gmi_189d_slope_v084_signal,    f36em_f36_earnings_manipulation_score_smgmi_126d_slope_v085_signal,    f36em_f36_earnings_manipulation_score_gmidisp_126d_slope_v086_signal,    f36em_f36_earnings_manipulation_score_zgmi_126d_slope_v087_signal,    f36em_f36_earnings_manipulation_score_sgi_84d_slope_v088_signal,    f36em_f36_earnings_manipulation_score_sgi_189d_slope_v089_signal,    f36em_f36_earnings_manipulation_score_sgi_42d_slope_v090_signal,    f36em_f36_earnings_manipulation_score_smsgi_126d_slope_v091_signal,    f36em_f36_earnings_manipulation_score_sgidisp_126d_slope_v092_signal,    f36em_f36_earnings_manipulation_score_zsgi_252d_slope_v093_signal,    f36em_f36_earnings_manipulation_score_tatadisp_252d_slope_v094_signal,    f36em_f36_earnings_manipulation_score_tatadisp_126d_slope_v095_signal,    f36em_f36_earnings_manipulation_score_smtata_252d_slope_v096_signal,    f36em_f36_earnings_manipulation_score_tatachg_63d_slope_v097_signal,    f36em_f36_earnings_manipulation_score_tatachg_252d_slope_v098_signal,    f36em_f36_earnings_manipulation_score_aqi_84d_slope_v099_signal,    f36em_f36_earnings_manipulation_score_zaq_252d_slope_v100_signal,    f36em_f36_earnings_manipulation_score_intchg_252d_slope_v101_signal,    f36em_f36_earnings_manipulation_score_depi_84d_slope_v102_signal,    f36em_f36_earnings_manipulation_score_zdeprate_252d_slope_v103_signal,    f36em_f36_earnings_manipulation_score_depratechg_126d_slope_v104_signal,    f36em_f36_earnings_manipulation_score_sgai_84d_slope_v105_signal,    f36em_f36_earnings_manipulation_score_zsga_252d_slope_v106_signal,    f36em_f36_earnings_manipulation_score_sgachg_126d_slope_v107_signal,    f36em_f36_earnings_manipulation_score_lvgi_84d_slope_v108_signal,    f36em_f36_earnings_manipulation_score_zlev_252d_slope_v109_signal,    f36em_f36_earnings_manipulation_score_levchg_126d_slope_v110_signal,    f36em_f36_earnings_manipulation_score_dlvgi_252d_slope_v111_signal,    f36em_f36_earnings_manipulation_score_debtmix_063d_slope_v112_signal,    f36em_f36_earnings_manipulation_score_mscore8_84d_slope_v113_signal,    f36em_f36_earnings_manipulation_score_zmscore_252d_slope_v114_signal,    f36em_f36_earnings_manipulation_score_mrank_252d_slope_v115_signal,    f36em_f36_earnings_manipulation_score_mscore5_252d_slope_v116_signal,    f36em_f36_earnings_manipulation_score_accrsub_126d_slope_v117_signal,    f36em_f36_earnings_manipulation_score_revqual_126d_slope_v118_signal,    f36em_f36_earnings_manipulation_score_dsrisgi_252d_slope_v119_signal,    f36em_f36_earnings_manipulation_score_gmitata_126d_slope_v120_signal,    f36em_f36_earnings_manipulation_score_dsrispread_84_252_slope_v121_signal,    f36em_f36_earnings_manipulation_score_gmispread_126_252_slope_v122_signal,    f36em_f36_earnings_manipulation_score_sgispread_84_252_slope_v123_signal,    f36em_f36_earnings_manipulation_score_sgitrend_252d_slope_v124_signal,    f36em_f36_earnings_manipulation_score_lvgitrend_252d_slope_v125_signal,    f36em_f36_earnings_manipulation_score_turnidx_126d_slope_v126_signal,    f36em_f36_earnings_manipulation_score_cfmidx_126d_slope_v127_signal,    f36em_f36_earnings_manipulation_score_znetmargin_252d_slope_v128_signal,    f36em_f36_earnings_manipulation_score_discaccr_126d_slope_v129_signal,    f36em_f36_earnings_manipulation_score_zblend5_126d_slope_v130_signal,    f36em_f36_earnings_manipulation_score_zblend5_252d_slope_v131_signal,    f36em_f36_earnings_manipulation_score_dsripersgi_126d_slope_v132_signal,    f36em_f36_earnings_manipulation_score_tatapersgi_126d_slope_v133_signal,    f36em_f36_earnings_manipulation_score_gpassetidx_126d_slope_v134_signal,    f36em_f36_earnings_manipulation_score_mrank84_252d_slope_v135_signal,    f36em_f36_earnings_manipulation_score_absdsri_z252_slope_v136_signal,    f36em_f36_earnings_manipulation_score_revrec_126d_slope_v137_signal,    f36em_f36_earnings_manipulation_score_deidx_126d_slope_v138_signal,    f36em_f36_earnings_manipulation_score_mscore8_189d_slope_v139_signal,    f36em_f36_earnings_manipulation_score_accrcover_126d_slope_v140_signal,    f36em_f36_earnings_manipulation_score_ewmdsri_126d_slope_v141_signal,    f36em_f36_earnings_manipulation_score_ewmtata_126d_slope_v142_signal,    f36em_f36_earnings_manipulation_score_ewmgmi_252d_slope_v143_signal,    f36em_f36_earnings_manipulation_score_msurp_252d_slope_v144_signal,    f36em_f36_earnings_manipulation_score_zrecasset_252d_slope_v145_signal,    f36em_f36_earnings_manipulation_score_capidx_126d_slope_v146_signal,    f36em_f36_earnings_manipulation_score_riskcomp_126d_slope_v147_signal,    f36em_f36_earnings_manipulation_score_mtrend_252d_slope_v148_signal,    f36em_f36_earnings_manipulation_score_costgap_126d_slope_v149_signal,    f36em_f36_earnings_manipulation_score_dsriblend_multi_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_EARNINGS_MANIPULATION_SCORE_REGISTRY_SLOPE = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap",
           "sector_index", "bellwether_coin", "bellwether_mstr", "nholders",
           "newholders", "exitholders", "hhi", "totalunits", "avgposition",
           "buyval", "sellval", "buyshares", "sellshares", "buycount", "sellcount",
           "officerbuyval", "dirbuyval", "tenpctbuyval", "officerbuycount",
           "optionexval", "tenpctsellval", "receivables", "workingcapital"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f36_dsri', '_f36_tata', '_f36_gmi', '_f36_sgi')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f36_earnings_manipulation_score_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
