import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    # ordinary-least-squares slope over a rolling window (per-step)
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        idx = idx - idx.mean()
        denom = (idx ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(idx, a) / denom)

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _chg(s, w):
    return s - s.shift(w)


def _logratio(a, b):
    return np.log(a.replace(0, np.nan).abs().clip(lower=1e-9)) - \
        np.log(b.replace(0, np.nan).abs().clip(lower=1e-9))


# ===== folder domain primitives (Beneish manipulation indices) =====
# Each index compares a current ratio to its level one year (252d) earlier.
def _f36_dsri(receivables, revenue, w=TRADING_DAYS_YEAR):
    # Days-Sales-in-Receivables Index = (rec_t/rev_t) / (rec_{t-1}/rev_{t-1})
    cur = receivables / revenue.replace(0, np.nan)
    return cur / cur.shift(w).replace(0, np.nan)


def _f36_gmi(gp, revenue, w=TRADING_DAYS_YEAR):
    # Gross-Margin Index = gm_{t-1} / gm_t  (deterioration > 1)
    gm = gp / revenue.replace(0, np.nan)
    return gm.shift(w) / gm.replace(0, np.nan)


def _f36_aqi(assets, ppnenet, w=TRADING_DAYS_YEAR):
    # Asset-Quality Index = nonPPE-noncurrent share ratio proxy = (1-ppne/assets)_t / prior
    q = 1.0 - ppnenet / assets.replace(0, np.nan)
    return q / q.shift(w).replace(0, np.nan)


def _f36_sgi(revenue, w=TRADING_DAYS_YEAR):
    # Sales-Growth Index = rev_t / rev_{t-1}
    return revenue / revenue.shift(w).replace(0, np.nan)


def _f36_depi(depamor, ppnenet, w=TRADING_DAYS_YEAR):
    # Depreciation Index = deprate_{t-1} / deprate_t
    rate = depamor / (depamor + ppnenet).replace(0, np.nan)
    return rate.shift(w) / rate.replace(0, np.nan)


def _f36_sgai(sgna, revenue, w=TRADING_DAYS_YEAR):
    # SG&A Index = (sga/rev)_t / (sga/rev)_{t-1}
    r = sgna / revenue.replace(0, np.nan)
    return r / r.shift(w).replace(0, np.nan)


def _f36_lvgi(debt, assets, w=TRADING_DAYS_YEAR):
    # Leverage Index = (debt/assets)_t / (debt/assets)_{t-1}
    r = debt / assets.replace(0, np.nan)
    return r / r.shift(w).replace(0, np.nan)


def _f36_tata(netinc, ncfo, assets):
    # Total Accruals To Total Assets = (netinc - ncfo) / assets
    return (netinc - ncfo) / assets.replace(0, np.nan)


def _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt,
                netinc, ncfo, w=TRADING_DAYS_YEAR):
    # Beneish 8-variable composite M-score
    dsri = _f36_dsri(receivables, revenue, w)
    gmi = _f36_gmi(gp, revenue, w)
    aqi = _f36_aqi(assets, ppnenet, w)
    sgi = _f36_sgi(revenue, w)
    depi = _f36_depi(depamor, ppnenet, w)
    sgai = _f36_sgai(sgna, revenue, w)
    lvgi = _f36_lvgi(debt, assets, w)
    tata = _f36_tata(netinc, ncfo, assets)
    return (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
            + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)


# ============================================================
# ---- DSRI: days-sales-in-receivables index ----
def f36mb_f36_manipulation_beneish_dsri_252d_base_v001_signal(receivables, revenue):
    b = _f36_dsri(receivables, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsriz_252d_base_v002_signal(receivables, revenue):
    d = _f36_dsri(receivables, revenue, 252)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrirank_504d_base_v003_signal(receivables, revenue):
    d = _f36_dsri(receivables, revenue, 252)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrislp_126d_base_v004_signal(receivables, revenue):
    d = _f36_dsri(receivables, revenue, 252)
    b = _slope(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsriexc_252d_base_v005_signal(receivables, revenue):
    # excess over the neutral level of 1.0 (no manipulation pressure baseline)
    d = _f36_dsri(receivables, revenue, 252)
    b = (d - 1.0) * np.sign(d - 1.0) * np.abs(d - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintensz_126d_base_v006_signal(receivables, revenue):
    # raw receivables intensity z-score (level, not index)
    r = receivables / revenue.replace(0, np.nan)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvgrowth_252d_base_v007_signal(receivables, revenue):
    # receivables-intensity acceleration: change in the (rec/rev) momentum (2nd order)
    r = receivables / revenue.replace(0, np.nan)
    mom = r - r.shift(126)
    b = mom - mom.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrishort_126d_base_v008_signal(receivables, revenue):
    # half-year DSRI variant (semiannual comparison window)
    b = _f36_dsri(receivables, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- GMI: gross-margin index ----
def f36mb_f36_manipulation_beneish_gmi_252d_base_v009_signal(gp, revenue):
    b = _f36_gmi(gp, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmiz_252d_base_v010_signal(gp, revenue):
    g = _f36_gmi(gp, revenue, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmirank_504d_base_v011_signal(gp, revenue):
    g = _f36_gmi(gp, revenue, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmislp_126d_base_v012_signal(gp, revenue):
    g = _f36_gmi(gp, revenue, 252)
    b = _slope(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargz_126d_base_v013_signal(gp, revenue):
    # gross-margin level z-score (deteriorating-fundamentals motive)
    gm = gp / revenue.replace(0, np.nan)
    b = _z(gm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargvol_126d_base_v014_signal(gp, revenue):
    # gross-margin instability: rolling dispersion of the margin level
    gm = gp / revenue.replace(0, np.nan)
    b = _std(gm, 126) / _mean(gm, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_margtrendrank_504d_base_v015_signal(gp, revenue):
    # gross-margin trend (quarterly slope) percentile-ranked across history
    gm = gp / revenue.replace(0, np.nan)
    slp = _slope(gm, 63)
    b = _rank(slp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- AQI: asset-quality index ----
def f36mb_f36_manipulation_beneish_aqi_252d_base_v016_signal(assets, ppnenet):
    b = _f36_aqi(assets, ppnenet, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqiz_252d_base_v017_signal(assets, ppnenet):
    a = _f36_aqi(assets, ppnenet, 252)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqirank_504d_base_v018_signal(assets, ppnenet):
    a = _f36_aqi(assets, ppnenet, 252)
    b = _rank(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqislp_126d_base_v019_signal(assets, ppnenet):
    a = _f36_aqi(assets, ppnenet, 252)
    b = _slope(a, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetz_126d_base_v020_signal(assets, ppnenet):
    # soft-asset share level (non-PPE share) z-score
    soft = 1.0 - ppnenet / assets.replace(0, np.nan)
    b = _z(soft, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetvol_126d_base_v021_signal(assets, ppnenet):
    # soft-asset share instability (rolling dispersion of the non-PPE share)
    soft = 1.0 - ppnenet / assets.replace(0, np.nan)
    b = _std(soft, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ppneshareslp_252d_base_v022_signal(ppnenet, assets):
    # capital-intensity (PPE share) slope over a year
    share = ppnenet / assets.replace(0, np.nan)
    b = _slope(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- SGI: sales-growth index ----
def f36mb_f36_manipulation_beneish_sgi_252d_base_v023_signal(revenue):
    b = _f36_sgi(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgiz_252d_base_v024_signal(revenue):
    s = _f36_sgi(revenue, 252)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgirank_504d_base_v025_signal(revenue):
    s = _f36_sgi(revenue, 252)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgislp_126d_base_v026_signal(revenue):
    s = _f36_sgi(revenue, 252)
    b = _slope(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_salesaccel_252d_base_v027_signal(revenue):
    # growth acceleration: SGI now vs SGI a quarter ago
    s = _f36_sgi(revenue, 252)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_salesgrowthgap_252d_base_v028_signal(revenue):
    # sales-growth gap: current yoy growth minus its trailing 252d average (regime shift)
    g = _logratio(revenue, revenue.shift(252))
    b = g - _mean(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgivol_126d_base_v029_signal(revenue):
    # instability of growth: rolling std of short-window sales growth
    g = _logratio(revenue, revenue.shift(63))
    b = _std(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- DEPI: depreciation index ----
def f36mb_f36_manipulation_beneish_depi_252d_base_v030_signal(depamor, ppnenet):
    b = _f36_depi(depamor, ppnenet, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depiz_252d_base_v031_signal(depamor, ppnenet):
    d = _f36_depi(depamor, ppnenet, 252)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depirank_504d_base_v032_signal(depamor, ppnenet):
    d = _f36_depi(depamor, ppnenet, 252)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depislp_126d_base_v033_signal(depamor, ppnenet):
    d = _f36_depi(depamor, ppnenet, 252)
    b = _slope(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depratez_126d_base_v034_signal(depamor, ppnenet):
    # depreciation rate level z-score
    rate = depamor / (depamor + ppnenet).replace(0, np.nan)
    b = _z(rate, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depratevol_126d_base_v035_signal(depamor, ppnenet):
    # depreciation-rate instability (rolling coefficient of variation)
    rate = depamor / (depamor + ppnenet).replace(0, np.nan)
    b = _std(rate, 126) / _mean(rate, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depamorrev_252d_base_v036_signal(depamor, revenue):
    # depreciation burden vs revenue (slowing-amortization proxy), z-scored
    burden = depamor / revenue.replace(0, np.nan)
    b = _z(burden, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- SGAI: SG&A index ----
def f36mb_f36_manipulation_beneish_sgai_252d_base_v037_signal(sgna, revenue):
    b = _f36_sgai(sgna, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaiz_252d_base_v038_signal(sgna, revenue):
    s = _f36_sgai(sgna, revenue, 252)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgairank_504d_base_v039_signal(sgna, revenue):
    s = _f36_sgai(sgna, revenue, 252)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaislp_126d_base_v040_signal(sgna, revenue):
    s = _f36_sgai(sgna, revenue, 252)
    b = _slope(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaintensz_126d_base_v041_signal(sgna, revenue):
    # SG&A intensity level z-score
    r = sgna / revenue.replace(0, np.nan)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaitrendrank_504d_base_v042_signal(sgna, revenue):
    # SG&A-intensity trend (quarterly slope) percentile-ranked across history
    r = sgna / revenue.replace(0, np.nan)
    slp = _slope(r, 63)
    b = _rank(slp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- LVGI: leverage index ----
def f36mb_f36_manipulation_beneish_lvgi_252d_base_v043_signal(debt, assets):
    b = _f36_lvgi(debt, assets, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgiz_252d_base_v044_signal(debt, assets):
    l = _f36_lvgi(debt, assets, 252)
    b = _z(l, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgirank_504d_base_v045_signal(debt, assets):
    l = _f36_lvgi(debt, assets, 252)
    b = _rank(l, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgislp_126d_base_v046_signal(debt, assets):
    l = _f36_lvgi(debt, assets, 252)
    b = _slope(l, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_leveragez_126d_base_v047_signal(debt, assets):
    # leverage level z-score
    lev = debt / assets.replace(0, np.nan)
    b = _z(lev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_levtrendrank_504d_base_v048_signal(debt, assets):
    # leverage trend (quarterly slope of debt/assets) percentile-ranked across history
    lev = debt / assets.replace(0, np.nan)
    slp = _slope(lev, 63)
    b = _rank(slp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- TATA: total accruals to total assets ----
def f36mb_f36_manipulation_beneish_tata_base_v049_signal(netinc, ncfo, assets):
    b = _f36_tata(netinc, ncfo, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tataz_252d_base_v050_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatarank_504d_base_v051_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    b = _rank(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tataslp_126d_base_v052_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    b = _slope(t, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatachg_252d_base_v053_signal(netinc, ncfo, assets):
    t = _f36_tata(netinc, ncfo, assets)
    b = _chg(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_accrincome_126d_base_v054_signal(netinc, ncfo):
    # accruals as a fraction of net income (earnings-quality gap)
    accr = (netinc - ncfo) / netinc.replace(0, np.nan).abs().clip(lower=1e-6)
    b = _z(accr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_accrualvol_126d_base_v055_signal(netinc, ncfo, assets):
    # accrual instability: rolling dispersion of TATA (earnings-quality noise)
    tata = (netinc - ncfo) / assets.replace(0, np.nan)
    b = _std(tata, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- M-score composite and component blends ----
def f36mb_f36_manipulation_beneish_mscore_252d_base_v056_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    b = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorez_252d_base_v057_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    m = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 252)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorerank_504d_base_v058_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    m = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 252)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscoreslp_126d_base_v059_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    m = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 252)
    b = _slope(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorechg_252d_base_v060_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    m = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 252)
    b = _chg(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorezblend_252d_base_v061_signal(
        receivables, revenue, gp, assets, ppnenet, debt, netinc, ncfo):
    # standardized composite: equal-weight z-scores of the key indices (robust M-score)
    dsri = _z(_f36_dsri(receivables, revenue, 252), 252)
    gmi = _z(_f36_gmi(gp, revenue, 252), 252)
    aqi = _z(_f36_aqi(assets, ppnenet, 252), 252)
    lvgi = _z(_f36_lvgi(debt, assets, 252), 252)
    tata = _z(_f36_tata(netinc, ncfo, assets), 252)
    b = (dsri + gmi + aqi - lvgi + tata) / 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_indexbreadth_252d_base_v062_signal(
        receivables, revenue, gp, assets, ppnenet, sgna):
    # breadth of revenue/cost red flags: count-like blend of how many indices exceed 1
    dsri = np.tanh(5.0 * (_f36_dsri(receivables, revenue, 252) - 1.0))
    gmi = np.tanh(5.0 * (_f36_gmi(gp, revenue, 252) - 1.0))
    aqi = np.tanh(5.0 * (_f36_aqi(assets, ppnenet, 252) - 1.0))
    sgi = np.tanh(5.0 * (_f36_sgi(revenue, 252) - 1.0))
    sgai = np.tanh(5.0 * (_f36_sgai(sgna, revenue, 252) - 1.0))
    b = (dsri + gmi + aqi + sgi + sgai) / 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_revenueside_252d_base_v063_signal(
        receivables, revenue, gp):
    # revenue-recognition sub-score: DSRI x GMI x SGI (top-line manipulation cluster)
    dsri = _f36_dsri(receivables, revenue, 252)
    gmi = _f36_gmi(gp, revenue, 252)
    sgi = _f36_sgi(revenue, 252)
    b = 0.92 * dsri + 0.528 * gmi + 0.892 * sgi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_costside_252d_base_v064_signal(
        assets, ppnenet, depamor, sgna, revenue, debt):
    # cost-/capitalization-side sub-score: AQI + DEPI + SGAI + LVGI
    aqi = _f36_aqi(assets, ppnenet, 252)
    depi = _f36_depi(depamor, ppnenet, 252)
    sgai = _f36_sgai(sgna, revenue, 252)
    lvgi = _f36_lvgi(debt, assets, 252)
    b = 0.404 * aqi + 0.115 * depi - 0.172 * sgai - 0.327 * lvgi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_accrualmomrank_504d_base_v065_signal(
        netinc, ncfo, assets):
    # accrual-momentum: quarterly slope of TATA, percentile-ranked across history
    tata = _f36_tata(netinc, ncfo, assets)
    slp = _slope(tata, 63)
    b = _rank(slp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_redflagcount_252d_base_v066_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt):
    # continuous severity: sum of positive exceedances over per-index thresholds
    dsri = (_f36_dsri(receivables, revenue, 252) - 1.031).clip(lower=0)
    gmi = (_f36_gmi(gp, revenue, 252) - 1.014).clip(lower=0)
    aqi = (_f36_aqi(assets, ppnenet, 252) - 1.04).clip(lower=0)
    sgi = (_f36_sgi(revenue, 252) - 1.134).clip(lower=0)
    depi = (_f36_depi(depamor, ppnenet, 252) - 1.0).clip(lower=0)
    sgai = (_f36_sgai(sgna, revenue, 252) - 1.054).clip(lower=0)
    b = dsri + gmi + aqi + sgi + depi + sgai
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrigmi_252d_base_v067_signal(receivables, revenue, gp):
    # interaction: receivables-bloat AND margin-deterioration jointly
    dsri = _f36_dsri(receivables, revenue, 252)
    gmi = _f36_gmi(gp, revenue, 252)
    b = (dsri - 1.0) * (gmi - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgitata_252d_base_v068_signal(revenue, netinc, ncfo, assets):
    # high growth funded by accruals (aggressive-growth-with-accruals interaction)
    sgi = _f36_sgi(revenue, 252) - 1.0
    tata = _f36_tata(netinc, ncfo, assets)
    b = sgi * tata
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqidepi_252d_base_v069_signal(assets, ppnenet, depamor):
    # capitalization aggressiveness: soft assets up AND depreciation slowing
    aqi = _f36_aqi(assets, ppnenet, 252)
    depi = _f36_depi(depamor, ppnenet, 252)
    b = (aqi - 1.0) + (depi - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscoredisp_252d_base_v070_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt):
    # dispersion across the 6 index components (broad vs concentrated red flags)
    dsri = _f36_dsri(receivables, revenue, 252)
    gmi = _f36_gmi(gp, revenue, 252)
    aqi = _f36_aqi(assets, ppnenet, 252)
    sgi = _f36_sgi(revenue, 252)
    depi = _f36_depi(depamor, ppnenet, 252)
    sgai = _f36_sgai(sgna, revenue, 252)
    stacked = pd.concat([dsri, gmi, aqi, sgi, depi, sgai], axis=1)
    b = stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscoremax_252d_base_v071_signal(
        receivables, revenue, gp, assets, ppnenet, sgna):
    # worst single red flag (max index across components)
    dsri = _f36_dsri(receivables, revenue, 252)
    gmi = _f36_gmi(gp, revenue, 252)
    aqi = _f36_aqi(assets, ppnenet, 252)
    sgi = _f36_sgi(revenue, 252)
    sgai = _f36_sgai(sgna, revenue, 252)
    stacked = pd.concat([dsri, gmi, aqi, sgi, sgai], axis=1)
    b = stacked.max(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_accrualrev_252d_base_v072_signal(
        netinc, ncfo, assets):
    # accrual reversal: sign-flip of TATA vs one year ago (reversal red flag)
    t = _f36_tata(netinc, ncfo, assets)
    b = np.sign(t) - np.sign(t.shift(252))
    result = b * t.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsritata_252d_base_v073_signal(
        receivables, revenue, netinc, ncfo, assets):
    # receivables bloat reinforced by positive accruals
    dsri = _f36_dsri(receivables, revenue, 252) - 1.0
    tata = _f36_tata(netinc, ncfo, assets)
    b = dsri + 3.0 * tata
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscoreaccel_252d_base_v074_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    # M-score acceleration: quarter-over-quarter change of the yearly composite change
    m = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 252)
    chg = m - m.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorevol_126d_base_v075_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    # instability of the manipulation score (its rolling std)
    m = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 252)
    b = _std(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36mb_f36_manipulation_beneish_dsri_252d_base_v001_signal,
    f36mb_f36_manipulation_beneish_dsriz_252d_base_v002_signal,
    f36mb_f36_manipulation_beneish_dsrirank_504d_base_v003_signal,
    f36mb_f36_manipulation_beneish_dsrislp_126d_base_v004_signal,
    f36mb_f36_manipulation_beneish_dsriexc_252d_base_v005_signal,
    f36mb_f36_manipulation_beneish_recvintensz_126d_base_v006_signal,
    f36mb_f36_manipulation_beneish_recvgrowth_252d_base_v007_signal,
    f36mb_f36_manipulation_beneish_dsrishort_126d_base_v008_signal,
    f36mb_f36_manipulation_beneish_gmi_252d_base_v009_signal,
    f36mb_f36_manipulation_beneish_gmiz_252d_base_v010_signal,
    f36mb_f36_manipulation_beneish_gmirank_504d_base_v011_signal,
    f36mb_f36_manipulation_beneish_gmislp_126d_base_v012_signal,
    f36mb_f36_manipulation_beneish_grossmargz_126d_base_v013_signal,
    f36mb_f36_manipulation_beneish_grossmargvol_126d_base_v014_signal,
    f36mb_f36_manipulation_beneish_margtrendrank_504d_base_v015_signal,
    f36mb_f36_manipulation_beneish_aqi_252d_base_v016_signal,
    f36mb_f36_manipulation_beneish_aqiz_252d_base_v017_signal,
    f36mb_f36_manipulation_beneish_aqirank_504d_base_v018_signal,
    f36mb_f36_manipulation_beneish_aqislp_126d_base_v019_signal,
    f36mb_f36_manipulation_beneish_softassetz_126d_base_v020_signal,
    f36mb_f36_manipulation_beneish_softassetvol_126d_base_v021_signal,
    f36mb_f36_manipulation_beneish_ppneshareslp_252d_base_v022_signal,
    f36mb_f36_manipulation_beneish_sgi_252d_base_v023_signal,
    f36mb_f36_manipulation_beneish_sgiz_252d_base_v024_signal,
    f36mb_f36_manipulation_beneish_sgirank_504d_base_v025_signal,
    f36mb_f36_manipulation_beneish_sgislp_126d_base_v026_signal,
    f36mb_f36_manipulation_beneish_salesaccel_252d_base_v027_signal,
    f36mb_f36_manipulation_beneish_salesgrowthgap_252d_base_v028_signal,
    f36mb_f36_manipulation_beneish_sgivol_126d_base_v029_signal,
    f36mb_f36_manipulation_beneish_depi_252d_base_v030_signal,
    f36mb_f36_manipulation_beneish_depiz_252d_base_v031_signal,
    f36mb_f36_manipulation_beneish_depirank_504d_base_v032_signal,
    f36mb_f36_manipulation_beneish_depislp_126d_base_v033_signal,
    f36mb_f36_manipulation_beneish_depratez_126d_base_v034_signal,
    f36mb_f36_manipulation_beneish_depratevol_126d_base_v035_signal,
    f36mb_f36_manipulation_beneish_depamorrev_252d_base_v036_signal,
    f36mb_f36_manipulation_beneish_sgai_252d_base_v037_signal,
    f36mb_f36_manipulation_beneish_sgaiz_252d_base_v038_signal,
    f36mb_f36_manipulation_beneish_sgairank_504d_base_v039_signal,
    f36mb_f36_manipulation_beneish_sgaislp_126d_base_v040_signal,
    f36mb_f36_manipulation_beneish_sgaintensz_126d_base_v041_signal,
    f36mb_f36_manipulation_beneish_sgaitrendrank_504d_base_v042_signal,
    f36mb_f36_manipulation_beneish_lvgi_252d_base_v043_signal,
    f36mb_f36_manipulation_beneish_lvgiz_252d_base_v044_signal,
    f36mb_f36_manipulation_beneish_lvgirank_504d_base_v045_signal,
    f36mb_f36_manipulation_beneish_lvgislp_126d_base_v046_signal,
    f36mb_f36_manipulation_beneish_leveragez_126d_base_v047_signal,
    f36mb_f36_manipulation_beneish_levtrendrank_504d_base_v048_signal,
    f36mb_f36_manipulation_beneish_tata_base_v049_signal,
    f36mb_f36_manipulation_beneish_tataz_252d_base_v050_signal,
    f36mb_f36_manipulation_beneish_tatarank_504d_base_v051_signal,
    f36mb_f36_manipulation_beneish_tataslp_126d_base_v052_signal,
    f36mb_f36_manipulation_beneish_tatachg_252d_base_v053_signal,
    f36mb_f36_manipulation_beneish_accrincome_126d_base_v054_signal,
    f36mb_f36_manipulation_beneish_accrualvol_126d_base_v055_signal,
    f36mb_f36_manipulation_beneish_mscore_252d_base_v056_signal,
    f36mb_f36_manipulation_beneish_mscorez_252d_base_v057_signal,
    f36mb_f36_manipulation_beneish_mscorerank_504d_base_v058_signal,
    f36mb_f36_manipulation_beneish_mscoreslp_126d_base_v059_signal,
    f36mb_f36_manipulation_beneish_mscorechg_252d_base_v060_signal,
    f36mb_f36_manipulation_beneish_mscorezblend_252d_base_v061_signal,
    f36mb_f36_manipulation_beneish_indexbreadth_252d_base_v062_signal,
    f36mb_f36_manipulation_beneish_revenueside_252d_base_v063_signal,
    f36mb_f36_manipulation_beneish_costside_252d_base_v064_signal,
    f36mb_f36_manipulation_beneish_accrualmomrank_504d_base_v065_signal,
    f36mb_f36_manipulation_beneish_redflagcount_252d_base_v066_signal,
    f36mb_f36_manipulation_beneish_dsrigmi_252d_base_v067_signal,
    f36mb_f36_manipulation_beneish_sgitata_252d_base_v068_signal,
    f36mb_f36_manipulation_beneish_aqidepi_252d_base_v069_signal,
    f36mb_f36_manipulation_beneish_mscoredisp_252d_base_v070_signal,
    f36mb_f36_manipulation_beneish_mscoremax_252d_base_v071_signal,
    f36mb_f36_manipulation_beneish_accrualrev_252d_base_v072_signal,
    f36mb_f36_manipulation_beneish_dsritata_252d_base_v073_signal,
    f36mb_f36_manipulation_beneish_mscoreaccel_252d_base_v074_signal,
    f36mb_f36_manipulation_beneish_mscorevol_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_MANIPULATION_BENEISH_REGISTRY_001_075 = REGISTRY


def _build_synth():
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    revenue = _fund(1, base=1e9, drift=0.03, vol=0.06).rename("revenue")
    gp = (_fund(2, base=4e8, drift=0.025, vol=0.06)).rename("gp")
    receivables = _fund(3, base=2e8, drift=0.03, vol=0.07).rename("receivables")
    assets = _fund(4, base=2e9, drift=0.02, vol=0.04).rename("assets")
    ppnenet = _fund(5, base=6e8, drift=0.02, vol=0.05).rename("ppnenet")
    depamor = _fund(6, base=8e7, drift=0.02, vol=0.05).rename("depamor")
    sgna = _fund(7, base=2.5e8, drift=0.025, vol=0.06).rename("sgna")
    debt = _fund(8, base=7e8, drift=0.02, vol=0.06).rename("debt")
    netinc = _fund(9, base=1.5e8, drift=0.02, vol=0.08, allow_neg=True).rename("netinc")
    ncfo = _fund(10, base=2e8, drift=0.02, vol=0.07, allow_neg=True).rename("ncfo")

    return {
        "revenue": revenue, "gp": gp, "receivables": receivables, "assets": assets,
        "ppnenet": ppnenet, "depamor": depamor, "sgna": sgna, "debt": debt,
        "netinc": netinc, "ncfo": ncfo,
    }


if __name__ == "__main__":
    cols = _build_synth()

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f36_manipulation_beneish_base_001_075_claude: %d features pass" % n_features)
