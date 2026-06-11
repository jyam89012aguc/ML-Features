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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        idx = idx - idx.mean()
        denom = (idx ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(idx, a) / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _roc(s, w):
    # math 1st derivative: per-step rate of change over window w
    return (s - s.shift(w)) / float(w)


def _accel(s, w):
    # math 2nd derivative: rate of change of the rate of change
    d = (s - s.shift(w)) / float(w)
    return (d - d.shift(w)) / float(w)


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
def f36mb_f36_manipulation_beneish_dsriroc_21d_slope_v001_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 252)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsri504rocz_21d_slope_v002_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 504)
    d = _roc(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintrocrank_10d_slope_v003_signal(receivables, revenue):
    base = receivables / revenue.replace(0, np.nan)
    d = _roc(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassetrocdev_10d_slope_v004_signal(receivables, assets):
    base = receivables / assets.replace(0, np.nan)
    d = _roc(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrizrocsq_21d_slope_v005_signal(receivables, revenue):
    base = _z(_f36_dsri(receivables, revenue, 252), 252)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmiroc_21d_slope_v006_signal(gp, revenue):
    base = _f36_gmi(gp, revenue, 252)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargrocz_10d_slope_v007_signal(gp, revenue):
    base = gp / revenue.replace(0, np.nan)
    d = _roc(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsintrocrank_10d_slope_v008_signal(gp, revenue):
    base = (revenue - gp) / revenue.replace(0, np.nan)
    d = _roc(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmizrocdev_21d_slope_v009_signal(gp, revenue):
    base = _z(_f36_gmi(gp, revenue, 252), 252)
    d = _roc(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqirocsq_21d_slope_v010_signal(assets, ppnenet):
    base = _f36_aqi(assets, ppnenet, 252)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetroc_10d_slope_v011_signal(assets, ppnenet):
    base = 1.0 - ppnenet / assets.replace(0, np.nan)
    d = _roc(base, 10)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_capintensrocz_10d_slope_v012_signal(ppnenet, depamor):
    base = ppnenet / (ppnenet + depamor).replace(0, np.nan)
    d = _roc(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqizrocrank_21d_slope_v013_signal(assets, ppnenet):
    base = _z(_f36_aqi(assets, ppnenet, 252), 252)
    d = _roc(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgirocdev_21d_slope_v014_signal(revenue):
    base = _f36_sgi(revenue, 252)
    d = _roc(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgi126rocsq_10d_slope_v015_signal(revenue):
    base = _f36_sgi(revenue, 126)
    d = _roc(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgizroc_21d_slope_v016_signal(revenue):
    base = _z(_f36_sgi(revenue, 252), 252)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depirocz_21d_slope_v017_signal(depamor, ppnenet):
    base = _f36_depi(depamor, ppnenet, 252)
    d = _roc(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depraterocrank_10d_slope_v018_signal(depamor, ppnenet):
    base = depamor / (depamor + ppnenet).replace(0, np.nan)
    d = _roc(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depburdenrocdev_10d_slope_v019_signal(depamor, revenue):
    base = depamor / revenue.replace(0, np.nan)
    d = _roc(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgairocsq_21d_slope_v020_signal(sgna, revenue):
    base = _f36_sgai(sgna, revenue, 252)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaintroc_10d_slope_v021_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    d = _roc(base, 10)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaiprofitrocz_10d_slope_v022_signal(sgna, gp):
    base = sgna / gp.replace(0, np.nan)
    d = _roc(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgirocrank_21d_slope_v023_signal(debt, assets):
    base = _f36_lvgi(debt, assets, 252)
    d = _roc(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_leveragerocdev_10d_slope_v024_signal(debt, assets):
    base = debt / assets.replace(0, np.nan)
    d = _roc(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtrevrocsq_10d_slope_v025_signal(debt, revenue):
    base = debt / revenue.replace(0, np.nan)
    d = _roc(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tataroc_10d_slope_v026_signal(netinc, ncfo, assets):
    base = _f36_tata(netinc, ncfo, assets)
    d = _roc(base, 10)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatarevrocz_10d_slope_v027_signal(netinc, revenue):
    base = netinc / revenue.replace(0, np.nan)
    d = _roc(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cashconvrocrank_10d_slope_v028_signal(netinc, ncfo):
    base = ncfo / netinc.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _roc(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_roarocdev_10d_slope_v029_signal(netinc, assets):
    base = netinc / assets.replace(0, np.nan)
    d = _roc(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cfomarginrocsq_10d_slope_v030_signal(ncfo, revenue):
    base = ncfo / revenue.replace(0, np.nan)
    d = _roc(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscoreroc_21d_slope_v031_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 252)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscore504rocz_21d_slope_v032_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 504)
    d = _roc(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_revsiderocrank_21d_slope_v033_signal(receivables, revenue, gp):
    base = (0.92 * _f36_dsri(receivables, revenue, 252) + 0.528 * _f36_gmi(gp, revenue, 252) + 0.892 * _f36_sgi(revenue, 252))
    d = _roc(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_costsiderocdev_21d_slope_v034_signal(assets, ppnenet, depamor, sgna, revenue, debt):
    base = (0.404 * _f36_aqi(assets, ppnenet, 252) + 0.115 * _f36_depi(depamor, ppnenet, 252) - 0.172 * _f36_sgai(sgna, revenue, 252) - 0.327 * _f36_lvgi(debt, assets, 252))
    d = _roc(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrigmirocsq_21d_slope_v035_signal(receivables, revenue, gp):
    base = (_f36_dsri(receivables, revenue, 252) - 1.0) * (_f36_gmi(gp, revenue, 252) - 1.0)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgitataroc_21d_slope_v036_signal(revenue, netinc, ncfo, assets):
    base = (_f36_sgi(revenue, 252) - 1.0) * _f36_tata(netinc, ncfo, assets)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqidepirocz_21d_slope_v037_signal(assets, ppnenet, depamor):
    base = (_f36_aqi(assets, ppnenet, 252) - 1.0) + (_f36_depi(depamor, ppnenet, 252) - 1.0)
    d = _roc(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvncforocrank_10d_slope_v038_signal(receivables, ncfo):
    base = receivables / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _roc(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetturnrocdev_10d_slope_v039_signal(revenue, assets):
    base = revenue / assets.replace(0, np.nan)
    d = _roc(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossassetrocsq_10d_slope_v040_signal(gp, assets):
    base = gp / assets.replace(0, np.nan)
    d = _roc(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ncfomarginroc_10d_slope_v041_signal(ncfo, assets):
    base = ncfo / assets.replace(0, np.nan)
    d = _roc(base, 10)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ppnedebtrocz_10d_slope_v042_signal(ppnenet, debt):
    base = ppnenet / debt.replace(0, np.nan)
    d = _roc(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtcfrocrank_10d_slope_v043_signal(debt, ncfo):
    base = debt / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _roc(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_marginspreadrocdev_10d_slope_v044_signal(gp, revenue, sgna):
    base = (gp - sgna) / revenue.replace(0, np.nan)
    d = _roc(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depdebtrocsq_10d_slope_v045_signal(depamor, debt):
    base = depamor / debt.replace(0, np.nan)
    d = _roc(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrirocrank_42d_slope_v046_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 252)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsri504rocdev_42d_slope_v047_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 504)
    d = _roc(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintrocsq_21d_slope_v048_signal(receivables, revenue):
    base = receivables / revenue.replace(0, np.nan)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassetroc_21d_slope_v049_signal(receivables, assets):
    base = receivables / assets.replace(0, np.nan)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrizrocz_42d_slope_v050_signal(receivables, revenue):
    base = _z(_f36_dsri(receivables, revenue, 252), 252)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmirocrank_42d_slope_v051_signal(gp, revenue):
    base = _f36_gmi(gp, revenue, 252)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargrocdev_21d_slope_v052_signal(gp, revenue):
    base = gp / revenue.replace(0, np.nan)
    d = _roc(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsintrocsq_21d_slope_v053_signal(gp, revenue):
    base = (revenue - gp) / revenue.replace(0, np.nan)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmizroc_42d_slope_v054_signal(gp, revenue):
    base = _z(_f36_gmi(gp, revenue, 252), 252)
    d = _roc(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqirocz_42d_slope_v055_signal(assets, ppnenet):
    base = _f36_aqi(assets, ppnenet, 252)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetrocrank_21d_slope_v056_signal(assets, ppnenet):
    base = 1.0 - ppnenet / assets.replace(0, np.nan)
    d = _roc(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_capintensrocdev_21d_slope_v057_signal(ppnenet, depamor):
    base = ppnenet / (ppnenet + depamor).replace(0, np.nan)
    d = _roc(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqizrocsq_42d_slope_v058_signal(assets, ppnenet):
    base = _z(_f36_aqi(assets, ppnenet, 252), 252)
    d = _roc(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgiroc_42d_slope_v059_signal(revenue):
    base = _f36_sgi(revenue, 252)
    d = _roc(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgi126rocz_21d_slope_v060_signal(revenue):
    base = _f36_sgi(revenue, 126)
    d = _roc(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgizrocrank_42d_slope_v061_signal(revenue):
    base = _z(_f36_sgi(revenue, 252), 252)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depirocdev_42d_slope_v062_signal(depamor, ppnenet):
    base = _f36_depi(depamor, ppnenet, 252)
    d = _roc(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depraterocsq_21d_slope_v063_signal(depamor, ppnenet):
    base = depamor / (depamor + ppnenet).replace(0, np.nan)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depburdenroc_21d_slope_v064_signal(depamor, revenue):
    base = depamor / revenue.replace(0, np.nan)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgairocz_42d_slope_v065_signal(sgna, revenue):
    base = _f36_sgai(sgna, revenue, 252)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaintrocrank_21d_slope_v066_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    d = _roc(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaiprofitrocdev_21d_slope_v067_signal(sgna, gp):
    base = sgna / gp.replace(0, np.nan)
    d = _roc(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgirocsq_42d_slope_v068_signal(debt, assets):
    base = _f36_lvgi(debt, assets, 252)
    d = _roc(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_leverageroc_21d_slope_v069_signal(debt, assets):
    base = debt / assets.replace(0, np.nan)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtrevrocz_21d_slope_v070_signal(debt, revenue):
    base = debt / revenue.replace(0, np.nan)
    d = _roc(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatarocrank_21d_slope_v071_signal(netinc, ncfo, assets):
    base = _f36_tata(netinc, ncfo, assets)
    d = _roc(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatarevrocdev_21d_slope_v072_signal(netinc, revenue):
    base = netinc / revenue.replace(0, np.nan)
    d = _roc(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cashconvrocsq_21d_slope_v073_signal(netinc, ncfo):
    base = ncfo / netinc.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_roaroc_21d_slope_v074_signal(netinc, assets):
    base = netinc / assets.replace(0, np.nan)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cfomarginrocz_21d_slope_v075_signal(ncfo, revenue):
    base = ncfo / revenue.replace(0, np.nan)
    d = _roc(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorerocrank_42d_slope_v076_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 252)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscore504rocdev_42d_slope_v077_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 504)
    d = _roc(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_revsiderocsq_42d_slope_v078_signal(receivables, revenue, gp):
    base = (0.92 * _f36_dsri(receivables, revenue, 252) + 0.528 * _f36_gmi(gp, revenue, 252) + 0.892 * _f36_sgi(revenue, 252))
    d = _roc(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_costsideroc_42d_slope_v079_signal(assets, ppnenet, depamor, sgna, revenue, debt):
    base = (0.404 * _f36_aqi(assets, ppnenet, 252) + 0.115 * _f36_depi(depamor, ppnenet, 252) - 0.172 * _f36_sgai(sgna, revenue, 252) - 0.327 * _f36_lvgi(debt, assets, 252))
    d = _roc(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrigmirocz_42d_slope_v080_signal(receivables, revenue, gp):
    base = (_f36_dsri(receivables, revenue, 252) - 1.0) * (_f36_gmi(gp, revenue, 252) - 1.0)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgitatarocrank_42d_slope_v081_signal(revenue, netinc, ncfo, assets):
    base = (_f36_sgi(revenue, 252) - 1.0) * _f36_tata(netinc, ncfo, assets)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqidepirocdev_42d_slope_v082_signal(assets, ppnenet, depamor):
    base = (_f36_aqi(assets, ppnenet, 252) - 1.0) + (_f36_depi(depamor, ppnenet, 252) - 1.0)
    d = _roc(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvncforocsq_21d_slope_v083_signal(receivables, ncfo):
    base = receivables / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetturnroc_21d_slope_v084_signal(revenue, assets):
    base = revenue / assets.replace(0, np.nan)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossassetrocz_21d_slope_v085_signal(gp, assets):
    base = gp / assets.replace(0, np.nan)
    d = _roc(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ncfomarginrocrank_21d_slope_v086_signal(ncfo, assets):
    base = ncfo / assets.replace(0, np.nan)
    d = _roc(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ppnedebtrocdev_21d_slope_v087_signal(ppnenet, debt):
    base = ppnenet / debt.replace(0, np.nan)
    d = _roc(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtcfrocsq_21d_slope_v088_signal(debt, ncfo):
    base = debt / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _roc(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_marginspreadroc_21d_slope_v089_signal(gp, revenue, sgna):
    base = (gp - sgna) / revenue.replace(0, np.nan)
    d = _roc(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depdebtrocz_21d_slope_v090_signal(depamor, debt):
    base = depamor / debt.replace(0, np.nan)
    d = _roc(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrirocsq_63d_slope_v091_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 252)
    d = _roc(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsri504roc_63d_slope_v092_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 504)
    d = _roc(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintrocz_42d_slope_v093_signal(receivables, revenue):
    base = receivables / revenue.replace(0, np.nan)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassetrocrank_42d_slope_v094_signal(receivables, assets):
    base = receivables / assets.replace(0, np.nan)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrizrocdev_63d_slope_v095_signal(receivables, revenue):
    base = _z(_f36_dsri(receivables, revenue, 252), 252)
    d = _roc(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmirocsq_63d_slope_v096_signal(gp, revenue):
    base = _f36_gmi(gp, revenue, 252)
    d = _roc(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargroc_42d_slope_v097_signal(gp, revenue):
    base = gp / revenue.replace(0, np.nan)
    d = _roc(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsintrocz_42d_slope_v098_signal(gp, revenue):
    base = (revenue - gp) / revenue.replace(0, np.nan)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmizrocrank_63d_slope_v099_signal(gp, revenue):
    base = _z(_f36_gmi(gp, revenue, 252), 252)
    d = _roc(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqirocdev_63d_slope_v100_signal(assets, ppnenet):
    base = _f36_aqi(assets, ppnenet, 252)
    d = _roc(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetrocsq_42d_slope_v101_signal(assets, ppnenet):
    base = 1.0 - ppnenet / assets.replace(0, np.nan)
    d = _roc(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_capintensroc_42d_slope_v102_signal(ppnenet, depamor):
    base = ppnenet / (ppnenet + depamor).replace(0, np.nan)
    d = _roc(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqizrocz_63d_slope_v103_signal(assets, ppnenet):
    base = _z(_f36_aqi(assets, ppnenet, 252), 252)
    d = _roc(base, 63)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgirocrank_63d_slope_v104_signal(revenue):
    base = _f36_sgi(revenue, 252)
    d = _roc(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgi126rocdev_42d_slope_v105_signal(revenue):
    base = _f36_sgi(revenue, 126)
    d = _roc(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgizrocsq_63d_slope_v106_signal(revenue):
    base = _z(_f36_sgi(revenue, 252), 252)
    d = _roc(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depiroc_63d_slope_v107_signal(depamor, ppnenet):
    base = _f36_depi(depamor, ppnenet, 252)
    d = _roc(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depraterocz_42d_slope_v108_signal(depamor, ppnenet):
    base = depamor / (depamor + ppnenet).replace(0, np.nan)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depburdenrocrank_42d_slope_v109_signal(depamor, revenue):
    base = depamor / revenue.replace(0, np.nan)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgairocdev_63d_slope_v110_signal(sgna, revenue):
    base = _f36_sgai(sgna, revenue, 252)
    d = _roc(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaintrocsq_42d_slope_v111_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    d = _roc(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaiprofitroc_42d_slope_v112_signal(sgna, gp):
    base = sgna / gp.replace(0, np.nan)
    d = _roc(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgirocz_63d_slope_v113_signal(debt, assets):
    base = _f36_lvgi(debt, assets, 252)
    d = _roc(base, 63)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_leveragerocrank_42d_slope_v114_signal(debt, assets):
    base = debt / assets.replace(0, np.nan)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtrevrocdev_42d_slope_v115_signal(debt, revenue):
    base = debt / revenue.replace(0, np.nan)
    d = _roc(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatarocsq_42d_slope_v116_signal(netinc, ncfo, assets):
    base = _f36_tata(netinc, ncfo, assets)
    d = _roc(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatarevroc_42d_slope_v117_signal(netinc, revenue):
    base = netinc / revenue.replace(0, np.nan)
    d = _roc(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cashconvrocz_42d_slope_v118_signal(netinc, ncfo):
    base = ncfo / netinc.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_roarocrank_42d_slope_v119_signal(netinc, assets):
    base = netinc / assets.replace(0, np.nan)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cfomarginrocdev_42d_slope_v120_signal(ncfo, revenue):
    base = ncfo / revenue.replace(0, np.nan)
    d = _roc(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorerocsq_63d_slope_v121_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 252)
    d = _roc(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscore504roc_63d_slope_v122_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 504)
    d = _roc(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_revsiderocz_63d_slope_v123_signal(receivables, revenue, gp):
    base = (0.92 * _f36_dsri(receivables, revenue, 252) + 0.528 * _f36_gmi(gp, revenue, 252) + 0.892 * _f36_sgi(revenue, 252))
    d = _roc(base, 63)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_costsiderocrank_63d_slope_v124_signal(assets, ppnenet, depamor, sgna, revenue, debt):
    base = (0.404 * _f36_aqi(assets, ppnenet, 252) + 0.115 * _f36_depi(depamor, ppnenet, 252) - 0.172 * _f36_sgai(sgna, revenue, 252) - 0.327 * _f36_lvgi(debt, assets, 252))
    d = _roc(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrigmirocdev_63d_slope_v125_signal(receivables, revenue, gp):
    base = (_f36_dsri(receivables, revenue, 252) - 1.0) * (_f36_gmi(gp, revenue, 252) - 1.0)
    d = _roc(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgitatarocsq_63d_slope_v126_signal(revenue, netinc, ncfo, assets):
    base = (_f36_sgi(revenue, 252) - 1.0) * _f36_tata(netinc, ncfo, assets)
    d = _roc(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqidepiroc_63d_slope_v127_signal(assets, ppnenet, depamor):
    base = (_f36_aqi(assets, ppnenet, 252) - 1.0) + (_f36_depi(depamor, ppnenet, 252) - 1.0)
    d = _roc(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvncforocz_42d_slope_v128_signal(receivables, ncfo):
    base = receivables / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetturnrocrank_42d_slope_v129_signal(revenue, assets):
    base = revenue / assets.replace(0, np.nan)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossassetrocdev_42d_slope_v130_signal(gp, assets):
    base = gp / assets.replace(0, np.nan)
    d = _roc(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ncfomarginrocsq_42d_slope_v131_signal(ncfo, assets):
    base = ncfo / assets.replace(0, np.nan)
    d = _roc(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ppnedebtroc_42d_slope_v132_signal(ppnenet, debt):
    base = ppnenet / debt.replace(0, np.nan)
    d = _roc(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtcfrocz_42d_slope_v133_signal(debt, ncfo):
    base = debt / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _roc(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_marginspreadrocrank_42d_slope_v134_signal(gp, revenue, sgna):
    base = (gp - sgna) / revenue.replace(0, np.nan)
    d = _roc(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depdebtrocdev_42d_slope_v135_signal(depamor, debt):
    base = depamor / debt.replace(0, np.nan)
    d = _roc(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrirocz_126d_slope_v136_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 252)
    d = _roc(base, 126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsri504rocrank_126d_slope_v137_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 504)
    d = _roc(base, 126)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintrocdev_63d_slope_v138_signal(receivables, revenue):
    base = receivables / revenue.replace(0, np.nan)
    d = _roc(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassetrocsq_63d_slope_v139_signal(receivables, assets):
    base = receivables / assets.replace(0, np.nan)
    d = _roc(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrizroc_126d_slope_v140_signal(receivables, revenue):
    base = _z(_f36_dsri(receivables, revenue, 252), 252)
    d = _roc(base, 126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmirocz_126d_slope_v141_signal(gp, revenue):
    base = _f36_gmi(gp, revenue, 252)
    d = _roc(base, 126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargrocrank_63d_slope_v142_signal(gp, revenue):
    base = gp / revenue.replace(0, np.nan)
    d = _roc(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsintrocdev_63d_slope_v143_signal(gp, revenue):
    base = (revenue - gp) / revenue.replace(0, np.nan)
    d = _roc(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmizrocsq_126d_slope_v144_signal(gp, revenue):
    base = _z(_f36_gmi(gp, revenue, 252), 252)
    d = _roc(base, 126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqiroc_126d_slope_v145_signal(assets, ppnenet):
    base = _f36_aqi(assets, ppnenet, 252)
    d = _roc(base, 126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetrocz_63d_slope_v146_signal(assets, ppnenet):
    base = 1.0 - ppnenet / assets.replace(0, np.nan)
    d = _roc(base, 63)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_capintensrocrank_63d_slope_v147_signal(ppnenet, depamor):
    base = ppnenet / (ppnenet + depamor).replace(0, np.nan)
    d = _roc(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqizrocdev_126d_slope_v148_signal(assets, ppnenet):
    base = _z(_f36_aqi(assets, ppnenet, 252), 252)
    d = _roc(base, 126)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgirocsq_126d_slope_v149_signal(revenue):
    base = _f36_sgi(revenue, 252)
    d = _roc(base, 126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgi126roc_63d_slope_v150_signal(revenue):
    base = _f36_sgi(revenue, 126)
    d = _roc(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36mb_f36_manipulation_beneish_dsriroc_21d_slope_v001_signal,
    f36mb_f36_manipulation_beneish_dsri504rocz_21d_slope_v002_signal,
    f36mb_f36_manipulation_beneish_recvintrocrank_10d_slope_v003_signal,
    f36mb_f36_manipulation_beneish_recvassetrocdev_10d_slope_v004_signal,
    f36mb_f36_manipulation_beneish_dsrizrocsq_21d_slope_v005_signal,
    f36mb_f36_manipulation_beneish_gmiroc_21d_slope_v006_signal,
    f36mb_f36_manipulation_beneish_grossmargrocz_10d_slope_v007_signal,
    f36mb_f36_manipulation_beneish_cogsintrocrank_10d_slope_v008_signal,
    f36mb_f36_manipulation_beneish_gmizrocdev_21d_slope_v009_signal,
    f36mb_f36_manipulation_beneish_aqirocsq_21d_slope_v010_signal,
    f36mb_f36_manipulation_beneish_softassetroc_10d_slope_v011_signal,
    f36mb_f36_manipulation_beneish_capintensrocz_10d_slope_v012_signal,
    f36mb_f36_manipulation_beneish_aqizrocrank_21d_slope_v013_signal,
    f36mb_f36_manipulation_beneish_sgirocdev_21d_slope_v014_signal,
    f36mb_f36_manipulation_beneish_sgi126rocsq_10d_slope_v015_signal,
    f36mb_f36_manipulation_beneish_sgizroc_21d_slope_v016_signal,
    f36mb_f36_manipulation_beneish_depirocz_21d_slope_v017_signal,
    f36mb_f36_manipulation_beneish_depraterocrank_10d_slope_v018_signal,
    f36mb_f36_manipulation_beneish_depburdenrocdev_10d_slope_v019_signal,
    f36mb_f36_manipulation_beneish_sgairocsq_21d_slope_v020_signal,
    f36mb_f36_manipulation_beneish_sgaintroc_10d_slope_v021_signal,
    f36mb_f36_manipulation_beneish_sgaiprofitrocz_10d_slope_v022_signal,
    f36mb_f36_manipulation_beneish_lvgirocrank_21d_slope_v023_signal,
    f36mb_f36_manipulation_beneish_leveragerocdev_10d_slope_v024_signal,
    f36mb_f36_manipulation_beneish_debtrevrocsq_10d_slope_v025_signal,
    f36mb_f36_manipulation_beneish_tataroc_10d_slope_v026_signal,
    f36mb_f36_manipulation_beneish_tatarevrocz_10d_slope_v027_signal,
    f36mb_f36_manipulation_beneish_cashconvrocrank_10d_slope_v028_signal,
    f36mb_f36_manipulation_beneish_roarocdev_10d_slope_v029_signal,
    f36mb_f36_manipulation_beneish_cfomarginrocsq_10d_slope_v030_signal,
    f36mb_f36_manipulation_beneish_mscoreroc_21d_slope_v031_signal,
    f36mb_f36_manipulation_beneish_mscore504rocz_21d_slope_v032_signal,
    f36mb_f36_manipulation_beneish_revsiderocrank_21d_slope_v033_signal,
    f36mb_f36_manipulation_beneish_costsiderocdev_21d_slope_v034_signal,
    f36mb_f36_manipulation_beneish_dsrigmirocsq_21d_slope_v035_signal,
    f36mb_f36_manipulation_beneish_sgitataroc_21d_slope_v036_signal,
    f36mb_f36_manipulation_beneish_aqidepirocz_21d_slope_v037_signal,
    f36mb_f36_manipulation_beneish_recvncforocrank_10d_slope_v038_signal,
    f36mb_f36_manipulation_beneish_assetturnrocdev_10d_slope_v039_signal,
    f36mb_f36_manipulation_beneish_grossassetrocsq_10d_slope_v040_signal,
    f36mb_f36_manipulation_beneish_ncfomarginroc_10d_slope_v041_signal,
    f36mb_f36_manipulation_beneish_ppnedebtrocz_10d_slope_v042_signal,
    f36mb_f36_manipulation_beneish_debtcfrocrank_10d_slope_v043_signal,
    f36mb_f36_manipulation_beneish_marginspreadrocdev_10d_slope_v044_signal,
    f36mb_f36_manipulation_beneish_depdebtrocsq_10d_slope_v045_signal,
    f36mb_f36_manipulation_beneish_dsrirocrank_42d_slope_v046_signal,
    f36mb_f36_manipulation_beneish_dsri504rocdev_42d_slope_v047_signal,
    f36mb_f36_manipulation_beneish_recvintrocsq_21d_slope_v048_signal,
    f36mb_f36_manipulation_beneish_recvassetroc_21d_slope_v049_signal,
    f36mb_f36_manipulation_beneish_dsrizrocz_42d_slope_v050_signal,
    f36mb_f36_manipulation_beneish_gmirocrank_42d_slope_v051_signal,
    f36mb_f36_manipulation_beneish_grossmargrocdev_21d_slope_v052_signal,
    f36mb_f36_manipulation_beneish_cogsintrocsq_21d_slope_v053_signal,
    f36mb_f36_manipulation_beneish_gmizroc_42d_slope_v054_signal,
    f36mb_f36_manipulation_beneish_aqirocz_42d_slope_v055_signal,
    f36mb_f36_manipulation_beneish_softassetrocrank_21d_slope_v056_signal,
    f36mb_f36_manipulation_beneish_capintensrocdev_21d_slope_v057_signal,
    f36mb_f36_manipulation_beneish_aqizrocsq_42d_slope_v058_signal,
    f36mb_f36_manipulation_beneish_sgiroc_42d_slope_v059_signal,
    f36mb_f36_manipulation_beneish_sgi126rocz_21d_slope_v060_signal,
    f36mb_f36_manipulation_beneish_sgizrocrank_42d_slope_v061_signal,
    f36mb_f36_manipulation_beneish_depirocdev_42d_slope_v062_signal,
    f36mb_f36_manipulation_beneish_depraterocsq_21d_slope_v063_signal,
    f36mb_f36_manipulation_beneish_depburdenroc_21d_slope_v064_signal,
    f36mb_f36_manipulation_beneish_sgairocz_42d_slope_v065_signal,
    f36mb_f36_manipulation_beneish_sgaintrocrank_21d_slope_v066_signal,
    f36mb_f36_manipulation_beneish_sgaiprofitrocdev_21d_slope_v067_signal,
    f36mb_f36_manipulation_beneish_lvgirocsq_42d_slope_v068_signal,
    f36mb_f36_manipulation_beneish_leverageroc_21d_slope_v069_signal,
    f36mb_f36_manipulation_beneish_debtrevrocz_21d_slope_v070_signal,
    f36mb_f36_manipulation_beneish_tatarocrank_21d_slope_v071_signal,
    f36mb_f36_manipulation_beneish_tatarevrocdev_21d_slope_v072_signal,
    f36mb_f36_manipulation_beneish_cashconvrocsq_21d_slope_v073_signal,
    f36mb_f36_manipulation_beneish_roaroc_21d_slope_v074_signal,
    f36mb_f36_manipulation_beneish_cfomarginrocz_21d_slope_v075_signal,
    f36mb_f36_manipulation_beneish_mscorerocrank_42d_slope_v076_signal,
    f36mb_f36_manipulation_beneish_mscore504rocdev_42d_slope_v077_signal,
    f36mb_f36_manipulation_beneish_revsiderocsq_42d_slope_v078_signal,
    f36mb_f36_manipulation_beneish_costsideroc_42d_slope_v079_signal,
    f36mb_f36_manipulation_beneish_dsrigmirocz_42d_slope_v080_signal,
    f36mb_f36_manipulation_beneish_sgitatarocrank_42d_slope_v081_signal,
    f36mb_f36_manipulation_beneish_aqidepirocdev_42d_slope_v082_signal,
    f36mb_f36_manipulation_beneish_recvncforocsq_21d_slope_v083_signal,
    f36mb_f36_manipulation_beneish_assetturnroc_21d_slope_v084_signal,
    f36mb_f36_manipulation_beneish_grossassetrocz_21d_slope_v085_signal,
    f36mb_f36_manipulation_beneish_ncfomarginrocrank_21d_slope_v086_signal,
    f36mb_f36_manipulation_beneish_ppnedebtrocdev_21d_slope_v087_signal,
    f36mb_f36_manipulation_beneish_debtcfrocsq_21d_slope_v088_signal,
    f36mb_f36_manipulation_beneish_marginspreadroc_21d_slope_v089_signal,
    f36mb_f36_manipulation_beneish_depdebtrocz_21d_slope_v090_signal,
    f36mb_f36_manipulation_beneish_dsrirocsq_63d_slope_v091_signal,
    f36mb_f36_manipulation_beneish_dsri504roc_63d_slope_v092_signal,
    f36mb_f36_manipulation_beneish_recvintrocz_42d_slope_v093_signal,
    f36mb_f36_manipulation_beneish_recvassetrocrank_42d_slope_v094_signal,
    f36mb_f36_manipulation_beneish_dsrizrocdev_63d_slope_v095_signal,
    f36mb_f36_manipulation_beneish_gmirocsq_63d_slope_v096_signal,
    f36mb_f36_manipulation_beneish_grossmargroc_42d_slope_v097_signal,
    f36mb_f36_manipulation_beneish_cogsintrocz_42d_slope_v098_signal,
    f36mb_f36_manipulation_beneish_gmizrocrank_63d_slope_v099_signal,
    f36mb_f36_manipulation_beneish_aqirocdev_63d_slope_v100_signal,
    f36mb_f36_manipulation_beneish_softassetrocsq_42d_slope_v101_signal,
    f36mb_f36_manipulation_beneish_capintensroc_42d_slope_v102_signal,
    f36mb_f36_manipulation_beneish_aqizrocz_63d_slope_v103_signal,
    f36mb_f36_manipulation_beneish_sgirocrank_63d_slope_v104_signal,
    f36mb_f36_manipulation_beneish_sgi126rocdev_42d_slope_v105_signal,
    f36mb_f36_manipulation_beneish_sgizrocsq_63d_slope_v106_signal,
    f36mb_f36_manipulation_beneish_depiroc_63d_slope_v107_signal,
    f36mb_f36_manipulation_beneish_depraterocz_42d_slope_v108_signal,
    f36mb_f36_manipulation_beneish_depburdenrocrank_42d_slope_v109_signal,
    f36mb_f36_manipulation_beneish_sgairocdev_63d_slope_v110_signal,
    f36mb_f36_manipulation_beneish_sgaintrocsq_42d_slope_v111_signal,
    f36mb_f36_manipulation_beneish_sgaiprofitroc_42d_slope_v112_signal,
    f36mb_f36_manipulation_beneish_lvgirocz_63d_slope_v113_signal,
    f36mb_f36_manipulation_beneish_leveragerocrank_42d_slope_v114_signal,
    f36mb_f36_manipulation_beneish_debtrevrocdev_42d_slope_v115_signal,
    f36mb_f36_manipulation_beneish_tatarocsq_42d_slope_v116_signal,
    f36mb_f36_manipulation_beneish_tatarevroc_42d_slope_v117_signal,
    f36mb_f36_manipulation_beneish_cashconvrocz_42d_slope_v118_signal,
    f36mb_f36_manipulation_beneish_roarocrank_42d_slope_v119_signal,
    f36mb_f36_manipulation_beneish_cfomarginrocdev_42d_slope_v120_signal,
    f36mb_f36_manipulation_beneish_mscorerocsq_63d_slope_v121_signal,
    f36mb_f36_manipulation_beneish_mscore504roc_63d_slope_v122_signal,
    f36mb_f36_manipulation_beneish_revsiderocz_63d_slope_v123_signal,
    f36mb_f36_manipulation_beneish_costsiderocrank_63d_slope_v124_signal,
    f36mb_f36_manipulation_beneish_dsrigmirocdev_63d_slope_v125_signal,
    f36mb_f36_manipulation_beneish_sgitatarocsq_63d_slope_v126_signal,
    f36mb_f36_manipulation_beneish_aqidepiroc_63d_slope_v127_signal,
    f36mb_f36_manipulation_beneish_recvncforocz_42d_slope_v128_signal,
    f36mb_f36_manipulation_beneish_assetturnrocrank_42d_slope_v129_signal,
    f36mb_f36_manipulation_beneish_grossassetrocdev_42d_slope_v130_signal,
    f36mb_f36_manipulation_beneish_ncfomarginrocsq_42d_slope_v131_signal,
    f36mb_f36_manipulation_beneish_ppnedebtroc_42d_slope_v132_signal,
    f36mb_f36_manipulation_beneish_debtcfrocz_42d_slope_v133_signal,
    f36mb_f36_manipulation_beneish_marginspreadrocrank_42d_slope_v134_signal,
    f36mb_f36_manipulation_beneish_depdebtrocdev_42d_slope_v135_signal,
    f36mb_f36_manipulation_beneish_dsrirocz_126d_slope_v136_signal,
    f36mb_f36_manipulation_beneish_dsri504rocrank_126d_slope_v137_signal,
    f36mb_f36_manipulation_beneish_recvintrocdev_63d_slope_v138_signal,
    f36mb_f36_manipulation_beneish_recvassetrocsq_63d_slope_v139_signal,
    f36mb_f36_manipulation_beneish_dsrizroc_126d_slope_v140_signal,
    f36mb_f36_manipulation_beneish_gmirocz_126d_slope_v141_signal,
    f36mb_f36_manipulation_beneish_grossmargrocrank_63d_slope_v142_signal,
    f36mb_f36_manipulation_beneish_cogsintrocdev_63d_slope_v143_signal,
    f36mb_f36_manipulation_beneish_gmizrocsq_126d_slope_v144_signal,
    f36mb_f36_manipulation_beneish_aqiroc_126d_slope_v145_signal,
    f36mb_f36_manipulation_beneish_softassetrocz_63d_slope_v146_signal,
    f36mb_f36_manipulation_beneish_capintensrocrank_63d_slope_v147_signal,
    f36mb_f36_manipulation_beneish_aqizrocdev_126d_slope_v148_signal,
    f36mb_f36_manipulation_beneish_sgirocsq_126d_slope_v149_signal,
    f36mb_f36_manipulation_beneish_sgi126roc_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_MANIPULATION_BENEISH_REGISTRY_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f36_manipulation_beneish_2nd_derivatives_001_150_claude: %d features pass" % n_features)
