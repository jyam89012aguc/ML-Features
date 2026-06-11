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
def _f36_dsri(receivables, revenue, w=TRADING_DAYS_YEAR):
    cur = receivables / revenue.replace(0, np.nan)
    return cur / cur.shift(w).replace(0, np.nan)


def _f36_gmi(gp, revenue, w=TRADING_DAYS_YEAR):
    gm = gp / revenue.replace(0, np.nan)
    return gm.shift(w) / gm.replace(0, np.nan)


def _f36_aqi(assets, ppnenet, w=TRADING_DAYS_YEAR):
    q = 1.0 - ppnenet / assets.replace(0, np.nan)
    return q / q.shift(w).replace(0, np.nan)


def _f36_sgi(revenue, w=TRADING_DAYS_YEAR):
    return revenue / revenue.shift(w).replace(0, np.nan)


def _f36_depi(depamor, ppnenet, w=TRADING_DAYS_YEAR):
    rate = depamor / (depamor + ppnenet).replace(0, np.nan)
    return rate.shift(w) / rate.replace(0, np.nan)


def _f36_sgai(sgna, revenue, w=TRADING_DAYS_YEAR):
    r = sgna / revenue.replace(0, np.nan)
    return r / r.shift(w).replace(0, np.nan)


def _f36_lvgi(debt, assets, w=TRADING_DAYS_YEAR):
    r = debt / assets.replace(0, np.nan)
    return r / r.shift(w).replace(0, np.nan)


def _f36_tata(netinc, ncfo, assets):
    return (netinc - ncfo) / assets.replace(0, np.nan)


def _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt,
                netinc, ncfo, w=TRADING_DAYS_YEAR):
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
# ---- DSRI variants on alternate windows / cross-fundamental forms ----
def f36mb_f36_manipulation_beneish_dsri504_504d_base_v076_signal(receivables, revenue):
    # two-year DSRI (longer comparison base captures slow receivables bloat)
    b = _f36_dsri(receivables, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsri504z_252d_base_v077_signal(receivables, revenue):
    d = _f36_dsri(receivables, revenue, 504)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassets_252d_base_v078_signal(receivables, assets):
    # receivables as a share of total assets, year-over-year index
    r = receivables / assets.replace(0, np.nan)
    b = r / r.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassetsz_126d_base_v079_signal(receivables, assets):
    r = receivables / assets.replace(0, np.nan)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvncfo_252d_base_v080_signal(receivables, ncfo):
    # receivables vs operating cash flow (uncollected-sales pressure)
    r = receivables / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintensslp_252d_base_v081_signal(receivables, revenue):
    # trend of receivables intensity over a year (collections deterioration)
    r = receivables / revenue.replace(0, np.nan)
    b = _slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- GMI variants ----
def f36mb_f36_manipulation_beneish_gmi504_504d_base_v082_signal(gp, revenue):
    b = _f36_gmi(gp, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsintens_252d_base_v083_signal(gp, revenue):
    # COGS intensity index ((rev-gp)/rev) year-over-year (mirror of margin)
    cogs = (revenue - gp) / revenue.replace(0, np.nan)
    b = cogs / cogs.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gpgrowthrank_504d_base_v084_signal(gp, revenue):
    # gross-profit growth relative to its own history, ranked
    g = _logratio(gp, gp.shift(252))
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_marginspread_126d_base_v085_signal(gp, revenue, sgna):
    # gross margin minus SG&A intensity (operating cushion proxy), z-scored
    spread = (gp - sgna) / revenue.replace(0, np.nan)
    b = _z(spread, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gpaccrint_252d_base_v086_signal(gp, netinc, ncfo):
    # gross-profit vs accrual quality: GP growth gated by cash backing
    gpg = _logratio(gp, gp.shift(252))
    cashback = ncfo / netinc.replace(0, np.nan).abs().clip(lower=1e-6)
    b = gpg * np.tanh(cashback)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- AQI variants ----
def f36mb_f36_manipulation_beneish_aqi504_504d_base_v087_signal(assets, ppnenet):
    b = _f36_aqi(assets, ppnenet, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetgrowth_252d_base_v088_signal(assets, revenue):
    # asset growth minus revenue growth (asset-bloat / overinvestment flag)
    ag = _logratio(assets, assets.shift(252))
    rg = _logratio(revenue, revenue.shift(252))
    b = ag - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_capintensrank_504d_base_v089_signal(ppnenet, assets):
    # capital intensity (PPE/assets) percentile-ranked across history
    ci = ppnenet / assets.replace(0, np.nan)
    b = _rank(ci, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetslp_252d_base_v090_signal(assets, ppnenet):
    soft = 1.0 - ppnenet / assets.replace(0, np.nan)
    b = _slope(soft, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ppnedebt_252d_base_v091_signal(ppnenet, debt):
    # fixed-asset backing of debt (collateral cushion), year-over-year change
    cover = ppnenet / debt.replace(0, np.nan)
    b = _chg(cover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- SGI variants ----
def f36mb_f36_manipulation_beneish_sgi504_504d_base_v092_signal(revenue):
    b = _f36_sgi(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgi126_126d_base_v093_signal(revenue):
    # semiannual sales-growth index (faster top-line cadence)
    b = _f36_sgi(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgistability_252d_base_v094_signal(revenue):
    # growth quality: mean growth divided by its dispersion (smooth-growth suspicion)
    g = _logratio(revenue, revenue.shift(63))
    b = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetturnz_126d_base_v095_signal(revenue, assets):
    # asset-turnover level (revenue/assets) z-scored vs its own history
    t = revenue / assets.replace(0, np.nan)
    b = _z(t, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_revcashdiv_252d_base_v096_signal(revenue, ncfo):
    # revenue growth not matched by operating-cash growth (paper-sales divergence)
    rg = _logratio(revenue, revenue.shift(252))
    cg = _logratio(ncfo, ncfo.shift(252))
    b = rg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- DEPI variants ----
def f36mb_f36_manipulation_beneish_depi504_504d_base_v097_signal(depamor, ppnenet):
    b = _f36_depi(depamor, ppnenet, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_deprateslp_252d_base_v098_signal(depamor, ppnenet):
    rate = depamor / (depamor + ppnenet).replace(0, np.nan)
    b = _slope(rate, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depamorintensz_126d_base_v099_signal(depamor, ppnenet):
    # depreciation expense per unit of gross PPE base, z-scored (write-off aggressiveness)
    intens = depamor / (depamor + ppnenet).replace(0, np.nan)
    b = -_z(intens, 126) + np.tanh(_slope(intens, 63) * 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depburdenrank_504d_base_v100_signal(depamor, revenue):
    burden = depamor / revenue.replace(0, np.nan)
    b = _rank(burden, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- SGAI variants ----
def f36mb_f36_manipulation_beneish_sgai504_504d_base_v101_signal(sgna, revenue):
    b = _f36_sgai(sgna, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaiprofit_252d_base_v102_signal(sgna, gp):
    # SG&A relative to gross profit (overhead absorption), year-over-year index
    r = sgna / gp.replace(0, np.nan)
    b = r / r.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaintensslp_252d_base_v103_signal(sgna, revenue):
    r = sgna / revenue.replace(0, np.nan)
    b = _slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaivol_126d_base_v104_signal(sgna, revenue):
    r = sgna / revenue.replace(0, np.nan)
    b = _std(r, 126) / _mean(r, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- LVGI variants ----
def f36mb_f36_manipulation_beneish_lvgi504_504d_base_v105_signal(debt, assets):
    b = _f36_lvgi(debt, assets, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtrev_252d_base_v106_signal(debt, revenue):
    # debt-to-sales index (leverage vs revenue base)
    r = debt / revenue.replace(0, np.nan)
    b = r / r.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtcfcover_252d_base_v107_signal(debt, ncfo):
    # debt vs operating-cash coverage, z-scored (refinancing-pressure proxy)
    cover = debt / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    b = _z(cover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_levslp_252d_base_v108_signal(debt, assets):
    lev = debt / assets.replace(0, np.nan)
    b = _slope(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- TATA / accrual variants ----
def f36mb_f36_manipulation_beneish_tatarev_252d_base_v109_signal(netinc, ncfo, revenue):
    # accruals scaled by sales rather than assets, z-scored
    accr = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = _z(accr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatasign_252d_base_v110_signal(netinc, ncfo, assets):
    # sign-magnitude transform of TATA (asymmetric accrual emphasis)
    t = _f36_tata(netinc, ncfo, assets)
    b = np.sign(t) * np.sqrt(t.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tata504slp_252d_base_v111_signal(netinc, ncfo, assets):
    # year-long slope of TATA (accrual build-up trajectory)
    t = _f36_tata(netinc, ncfo, assets)
    b = _slope(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_accrualpersist_126d_base_v112_signal(netinc, ncfo, assets):
    # accrual persistence: rolling autocorrelation of TATA (sticky vs reversing accruals)
    t = _f36_tata(netinc, ncfo, assets)
    b = t.rolling(126, min_periods=63).corr(t.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_earnpersist_126d_base_v113_signal(netinc, assets):
    # earnings level relative to assets (ROA), instability-adjusted
    roa = netinc / assets.replace(0, np.nan)
    b = _z(roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cfoquality_126d_base_v114_signal(ncfo, revenue):
    # operating-cash margin level (cash-backed sales), z-scored
    m = ncfo / revenue.replace(0, np.nan)
    b = _z(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- composites on alternate windows & blends ----
def f36mb_f36_manipulation_beneish_mscore504_504d_base_v115_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    # two-year-comparison M-score (slower manipulation accumulation)
    b = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscore504z_252d_base_v116_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    m = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 504)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorehorizgap_base_v117_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    # divergence between short-horizon and long-horizon M-scores (manipulation cadence)
    m1 = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                     debt, netinc, ncfo, 252)
    m2 = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                     debt, netinc, ncfo, 504)
    b = m1 - m2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_revcostbal_252d_base_v118_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna):
    # balance between revenue-side and cost-side red flags (manipulation style)
    revside = 0.92 * _f36_dsri(receivables, revenue, 252) + 0.892 * _f36_sgi(revenue, 252)
    costside = (0.404 * _f36_aqi(assets, ppnenet, 252)
                + 0.115 * _f36_depi(depamor, ppnenet, 252)
                - 0.172 * _f36_sgai(sgna, revenue, 252))
    b = (revside - costside) / (revside.abs() + costside.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grosssgicross_252d_base_v119_signal(gp, revenue):
    # margin deterioration AND sales acceleration together (classic fraud pattern)
    gmi = _f36_gmi(gp, revenue, 252) - 1.0
    sgi = _f36_sgi(revenue, 252) - 1.0
    b = gmi * sgi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsridepicross_252d_base_v120_signal(
        receivables, revenue, depamor, ppnenet):
    # receivables bloat AND depreciation slowdown (dual-lever earnings inflation)
    dsri = _f36_dsri(receivables, revenue, 252) - 1.0
    depi = _f36_depi(depamor, ppnenet, 252) - 1.0
    b = dsri + depi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqilvgicross_252d_base_v121_signal(
        assets, ppnenet, debt):
    # softening assets while levering up (aggressive capitalization + debt)
    aqi = _f36_aqi(assets, ppnenet, 252) - 1.0
    lvgi = _f36_lvgi(debt, assets, 252) - 1.0
    b = aqi * lvgi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_indexspread126_252_base_v122_signal(
        receivables, revenue):
    # DSRI horizon spread: semiannual minus annual receivables-index (acceleration)
    short = _f36_dsri(receivables, revenue, 126)
    long = _f36_dsri(receivables, revenue, 252)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgihorizgap_base_v123_signal(revenue):
    # sales-growth horizon gap: annualized semiannual SGI minus annual SGI
    short = _f36_sgi(revenue, 126) ** 2
    long = _f36_sgi(revenue, 252)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorepersist_252d_base_v124_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    # persistence of elevated M-score: smoothed composite (sticky manipulation regime)
    m = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 252)
    b = m.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscoredisp126_base_v125_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna):
    # dispersion of the six indices on the semiannual horizon (broad short-term flags)
    dsri = _f36_dsri(receivables, revenue, 126)
    gmi = _f36_gmi(gp, revenue, 126)
    aqi = _f36_aqi(assets, ppnenet, 126)
    sgi = _f36_sgi(revenue, 126)
    depi = _f36_depi(depamor, ppnenet, 126)
    sgai = _f36_sgai(sgna, revenue, 126)
    b = pd.concat([dsri, gmi, aqi, sgi, depi, sgai], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_accrualgmicross_252d_base_v126_signal(
        gp, revenue, netinc, ncfo, assets):
    # margin deterioration funded by accruals (low-quality earnings support)
    gmi = _f36_gmi(gp, revenue, 252) - 1.0
    tata = _f36_tata(netinc, ncfo, assets)
    b = gmi + 4.0 * tata
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvdeprcross_252d_base_v127_signal(
        receivables, revenue, depamor, ppnenet):
    # joint revenue-recognition & expense-deferral aggressiveness, ranked
    dsri = _f36_dsri(receivables, revenue, 252)
    depi = _f36_depi(depamor, ppnenet, 252)
    raw = (dsri - 1.0) + (depi - 1.0)
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetqualtrend_252d_base_v128_signal(assets, ppnenet):
    # asset-quality trajectory: AQI year-over-year change (deterioration speed)
    aqi = _f36_aqi(assets, ppnenet, 252)
    b = _chg(aqi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_salesqualcross_252d_base_v129_signal(
        revenue, receivables, ncfo):
    # high sales growth with weak cash conversion and rising receivables (red cluster)
    sgi = _f36_sgi(revenue, 252) - 1.0
    cash_lag = _logratio(ncfo, ncfo.shift(252))
    recv = _logratio(receivables, receivables.shift(252))
    b = sgi * (recv - cash_lag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscoreabswt_252d_base_v130_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    # absolute aggregate red-flag energy (magnitude of index deviations from neutral)
    parts = [
        (_f36_dsri(receivables, revenue, 252) - 1.0).abs(),
        (_f36_gmi(gp, revenue, 252) - 1.0).abs(),
        (_f36_aqi(assets, ppnenet, 252) - 1.0).abs(),
        (_f36_sgi(revenue, 252) - 1.0).abs(),
        (_f36_depi(depamor, ppnenet, 252) - 1.0).abs(),
        (_f36_sgai(sgna, revenue, 252) - 1.0).abs(),
        (_f36_lvgi(debt, assets, 252) - 1.0).abs(),
    ]
    b = sum(parts)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrirankslow_756d_base_v131_signal(receivables, revenue):
    # DSRI percentile over a very long memory (3y) — structural receivables drift
    d = _f36_dsri(receivables, revenue, 252)
    b = _rank(d, 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmislpfast_63d_base_v132_signal(gp, revenue):
    # fast (quarterly) slope of the GMI series (margin-index momentum)
    g = _f36_gmi(gp, revenue, 252)
    b = _slope(g, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaislpfast_63d_base_v133_signal(sgna, revenue):
    s = _f36_sgai(sgna, revenue, 252)
    b = _slope(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgislpfast_63d_base_v134_signal(debt, assets):
    l = _f36_lvgi(debt, assets, 252)
    b = _slope(l, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tataema_63d_base_v135_signal(netinc, ncfo, assets):
    # smoothed accrual intensity (persistent earnings-quality gap)
    t = _f36_tata(netinc, ncfo, assets)
    b = t.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossassetint_252d_base_v136_signal(gp, assets):
    # gross profit per asset (productivity), year-over-year index
    g = gp / assets.replace(0, np.nan)
    b = g / g.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvgpcross_252d_base_v137_signal(receivables, gp):
    # receivables growing faster than gross profit (low-quality revenue mix)
    rg = _logratio(receivables, receivables.shift(252))
    gg = _logratio(gp, gp.shift(252))
    b = rg - gg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depvsdebt_252d_base_v138_signal(depamor, debt):
    # depreciation relative to debt service capacity, z-scored
    r = depamor / debt.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_netincncfospread_126d_base_v139_signal(netinc, ncfo):
    # net income vs operating cash flow spread, normalized by their scale
    spread = (netinc - ncfo)
    scale = (netinc.abs() + ncfo.abs()).replace(0, np.nan)
    b = _z(spread / scale, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgiaccelrank_504d_base_v140_signal(revenue):
    # sales-growth acceleration percentile (suspicious step-ups in growth)
    sgi = _f36_sgi(revenue, 252)
    accel = sgi - sgi.shift(63)
    b = _rank(accel, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqitata_252d_base_v141_signal(
        assets, ppnenet, netinc, ncfo):
    # soft-asset growth reinforced by positive accruals (capitalization + accrual)
    aqi = _f36_aqi(assets, ppnenet, 252) - 1.0
    tata = _f36_tata(netinc, ncfo, assets)
    b = aqi + 3.0 * tata
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvrevcorr_252d_base_v142_signal(receivables, revenue):
    # rolling correlation of receivables vs revenue levels (decoupling = quality flaw)
    b = receivables.rolling(252, min_periods=126).corr(revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscoremin_252d_base_v143_signal(
        receivables, revenue, gp, assets, ppnenet, sgna, debt):
    # weakest (most negative) index deviation — concentration of cleanliness
    dsri = _f36_dsri(receivables, revenue, 252) - 1.0
    gmi = _f36_gmi(gp, revenue, 252) - 1.0
    aqi = _f36_aqi(assets, ppnenet, 252) - 1.0
    sgi = _f36_sgi(revenue, 252) - 1.0
    sgai = _f36_sgai(sgna, revenue, 252) - 1.0
    lvgi = _f36_lvgi(debt, assets, 252) - 1.0
    b = pd.concat([dsri, gmi, aqi, sgi, sgai, lvgi], axis=1).min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsslp_252d_base_v144_signal(gp, revenue):
    # COGS-intensity trend (margin compression speed)
    cogs = (revenue - gp) / revenue.replace(0, np.nan)
    b = _slope(cogs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetturnslp_252d_base_v145_signal(revenue, assets):
    t = revenue / assets.replace(0, np.nan)
    b = _slope(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvncforatio_252d_base_v146_signal(receivables, ncfo):
    # receivables vs operating cash flow, year-over-year index (cash-light receivables)
    r = receivables / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    b = r / r.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorezfast_126d_base_v147_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    # M-score z-scored over a shorter (semiannual) window (fast anomaly detection)
    m = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna,
                    debt, netinc, ncfo, 252)
    b = _z(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmiaqiblend_252d_base_v148_signal(
        gp, revenue, assets, ppnenet):
    # margin-deterioration plus asset-softening composite, ranked
    gmi = _f36_gmi(gp, revenue, 252)
    aqi = _f36_aqi(assets, ppnenet, 252)
    raw = 0.6 * gmi + 0.4 * aqi
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtaccrualcross_252d_base_v149_signal(
        debt, assets, netinc, ncfo):
    # leverage build-up combined with accrual build-up (covenant-driven manipulation)
    lvgi = _f36_lvgi(debt, assets, 252) - 1.0
    tata = _f36_tata(netinc, ncfo, assets)
    b = lvgi * np.sign(tata) * tata.abs() ** 0.5 * 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_fullindexenergy_252d_base_v150_signal(
        receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    # standardized aggregate of all eight Beneish levers (broad manipulation pressure)
    parts = [
        _z(_f36_dsri(receivables, revenue, 252), 252),
        _z(_f36_gmi(gp, revenue, 252), 252),
        _z(_f36_aqi(assets, ppnenet, 252), 252),
        _z(_f36_sgi(revenue, 252), 252),
        _z(_f36_depi(depamor, ppnenet, 252), 252),
        -_z(_f36_sgai(sgna, revenue, 252), 252),
        -_z(_f36_lvgi(debt, assets, 252), 252),
        _z(_f36_tata(netinc, ncfo, assets), 252),
    ]
    b = sum(parts) / 8.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36mb_f36_manipulation_beneish_dsri504_504d_base_v076_signal,
    f36mb_f36_manipulation_beneish_dsri504z_252d_base_v077_signal,
    f36mb_f36_manipulation_beneish_recvassets_252d_base_v078_signal,
    f36mb_f36_manipulation_beneish_recvassetsz_126d_base_v079_signal,
    f36mb_f36_manipulation_beneish_recvncfo_252d_base_v080_signal,
    f36mb_f36_manipulation_beneish_recvintensslp_252d_base_v081_signal,
    f36mb_f36_manipulation_beneish_gmi504_504d_base_v082_signal,
    f36mb_f36_manipulation_beneish_cogsintens_252d_base_v083_signal,
    f36mb_f36_manipulation_beneish_gpgrowthrank_504d_base_v084_signal,
    f36mb_f36_manipulation_beneish_marginspread_126d_base_v085_signal,
    f36mb_f36_manipulation_beneish_gpaccrint_252d_base_v086_signal,
    f36mb_f36_manipulation_beneish_aqi504_504d_base_v087_signal,
    f36mb_f36_manipulation_beneish_assetgrowth_252d_base_v088_signal,
    f36mb_f36_manipulation_beneish_capintensrank_504d_base_v089_signal,
    f36mb_f36_manipulation_beneish_softassetslp_252d_base_v090_signal,
    f36mb_f36_manipulation_beneish_ppnedebt_252d_base_v091_signal,
    f36mb_f36_manipulation_beneish_sgi504_504d_base_v092_signal,
    f36mb_f36_manipulation_beneish_sgi126_126d_base_v093_signal,
    f36mb_f36_manipulation_beneish_sgistability_252d_base_v094_signal,
    f36mb_f36_manipulation_beneish_assetturnz_126d_base_v095_signal,
    f36mb_f36_manipulation_beneish_revcashdiv_252d_base_v096_signal,
    f36mb_f36_manipulation_beneish_depi504_504d_base_v097_signal,
    f36mb_f36_manipulation_beneish_deprateslp_252d_base_v098_signal,
    f36mb_f36_manipulation_beneish_depamorintensz_126d_base_v099_signal,
    f36mb_f36_manipulation_beneish_depburdenrank_504d_base_v100_signal,
    f36mb_f36_manipulation_beneish_sgai504_504d_base_v101_signal,
    f36mb_f36_manipulation_beneish_sgaiprofit_252d_base_v102_signal,
    f36mb_f36_manipulation_beneish_sgaintensslp_252d_base_v103_signal,
    f36mb_f36_manipulation_beneish_sgaivol_126d_base_v104_signal,
    f36mb_f36_manipulation_beneish_lvgi504_504d_base_v105_signal,
    f36mb_f36_manipulation_beneish_debtrev_252d_base_v106_signal,
    f36mb_f36_manipulation_beneish_debtcfcover_252d_base_v107_signal,
    f36mb_f36_manipulation_beneish_levslp_252d_base_v108_signal,
    f36mb_f36_manipulation_beneish_tatarev_252d_base_v109_signal,
    f36mb_f36_manipulation_beneish_tatasign_252d_base_v110_signal,
    f36mb_f36_manipulation_beneish_tata504slp_252d_base_v111_signal,
    f36mb_f36_manipulation_beneish_accrualpersist_126d_base_v112_signal,
    f36mb_f36_manipulation_beneish_earnpersist_126d_base_v113_signal,
    f36mb_f36_manipulation_beneish_cfoquality_126d_base_v114_signal,
    f36mb_f36_manipulation_beneish_mscore504_504d_base_v115_signal,
    f36mb_f36_manipulation_beneish_mscore504z_252d_base_v116_signal,
    f36mb_f36_manipulation_beneish_mscorehorizgap_base_v117_signal,
    f36mb_f36_manipulation_beneish_revcostbal_252d_base_v118_signal,
    f36mb_f36_manipulation_beneish_grosssgicross_252d_base_v119_signal,
    f36mb_f36_manipulation_beneish_dsridepicross_252d_base_v120_signal,
    f36mb_f36_manipulation_beneish_aqilvgicross_252d_base_v121_signal,
    f36mb_f36_manipulation_beneish_indexspread126_252_base_v122_signal,
    f36mb_f36_manipulation_beneish_sgihorizgap_base_v123_signal,
    f36mb_f36_manipulation_beneish_mscorepersist_252d_base_v124_signal,
    f36mb_f36_manipulation_beneish_mscoredisp126_base_v125_signal,
    f36mb_f36_manipulation_beneish_accrualgmicross_252d_base_v126_signal,
    f36mb_f36_manipulation_beneish_recvdeprcross_252d_base_v127_signal,
    f36mb_f36_manipulation_beneish_assetqualtrend_252d_base_v128_signal,
    f36mb_f36_manipulation_beneish_salesqualcross_252d_base_v129_signal,
    f36mb_f36_manipulation_beneish_mscoreabswt_252d_base_v130_signal,
    f36mb_f36_manipulation_beneish_dsrirankslow_756d_base_v131_signal,
    f36mb_f36_manipulation_beneish_gmislpfast_63d_base_v132_signal,
    f36mb_f36_manipulation_beneish_sgaislpfast_63d_base_v133_signal,
    f36mb_f36_manipulation_beneish_lvgislpfast_63d_base_v134_signal,
    f36mb_f36_manipulation_beneish_tataema_63d_base_v135_signal,
    f36mb_f36_manipulation_beneish_grossassetint_252d_base_v136_signal,
    f36mb_f36_manipulation_beneish_recvgpcross_252d_base_v137_signal,
    f36mb_f36_manipulation_beneish_depvsdebt_252d_base_v138_signal,
    f36mb_f36_manipulation_beneish_netincncfospread_126d_base_v139_signal,
    f36mb_f36_manipulation_beneish_sgiaccelrank_504d_base_v140_signal,
    f36mb_f36_manipulation_beneish_aqitata_252d_base_v141_signal,
    f36mb_f36_manipulation_beneish_recvrevcorr_252d_base_v142_signal,
    f36mb_f36_manipulation_beneish_mscoremin_252d_base_v143_signal,
    f36mb_f36_manipulation_beneish_cogsslp_252d_base_v144_signal,
    f36mb_f36_manipulation_beneish_assetturnslp_252d_base_v145_signal,
    f36mb_f36_manipulation_beneish_recvncforatio_252d_base_v146_signal,
    f36mb_f36_manipulation_beneish_mscorezfast_126d_base_v147_signal,
    f36mb_f36_manipulation_beneish_gmiaqiblend_252d_base_v148_signal,
    f36mb_f36_manipulation_beneish_debtaccrualcross_252d_base_v149_signal,
    f36mb_f36_manipulation_beneish_fullindexenergy_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_MANIPULATION_BENEISH_REGISTRY_076_150 = REGISTRY


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

    print("OK f36_manipulation_beneish_base_076_150_claude: %d features pass" % n_features)
