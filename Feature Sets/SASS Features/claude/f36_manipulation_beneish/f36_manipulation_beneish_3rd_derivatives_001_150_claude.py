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
def f36mb_f36_manipulation_beneish_dsrijerk_21d_jerk_v001_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 252)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsri504jerkz_21d_jerk_v002_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 504)
    d = _accel(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintjerkrank_10d_jerk_v003_signal(receivables, revenue):
    base = receivables / revenue.replace(0, np.nan)
    d = _accel(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassetjerkdev_10d_jerk_v004_signal(receivables, assets):
    base = receivables / assets.replace(0, np.nan)
    d = _accel(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrizjerksq_21d_jerk_v005_signal(receivables, revenue):
    base = _z(_f36_dsri(receivables, revenue, 252), 252)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmijerk_21d_jerk_v006_signal(gp, revenue):
    base = _f36_gmi(gp, revenue, 252)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargjerkz_10d_jerk_v007_signal(gp, revenue):
    base = gp / revenue.replace(0, np.nan)
    d = _accel(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsintjerkrank_10d_jerk_v008_signal(gp, revenue):
    base = (revenue - gp) / revenue.replace(0, np.nan)
    d = _accel(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmizjerkdev_21d_jerk_v009_signal(gp, revenue):
    base = _z(_f36_gmi(gp, revenue, 252), 252)
    d = _accel(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqijerksq_21d_jerk_v010_signal(assets, ppnenet):
    base = _f36_aqi(assets, ppnenet, 252)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetjerk_10d_jerk_v011_signal(assets, ppnenet):
    base = 1.0 - ppnenet / assets.replace(0, np.nan)
    d = _accel(base, 10)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_capintensjerkz_10d_jerk_v012_signal(ppnenet, depamor):
    base = ppnenet / (ppnenet + depamor).replace(0, np.nan)
    d = _accel(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqizjerkrank_21d_jerk_v013_signal(assets, ppnenet):
    base = _z(_f36_aqi(assets, ppnenet, 252), 252)
    d = _accel(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgijerkdev_21d_jerk_v014_signal(revenue):
    base = _f36_sgi(revenue, 252)
    d = _accel(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgi126jerksq_10d_jerk_v015_signal(revenue):
    base = _f36_sgi(revenue, 126)
    d = _accel(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgizjerk_21d_jerk_v016_signal(revenue):
    base = _z(_f36_sgi(revenue, 252), 252)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depijerkz_21d_jerk_v017_signal(depamor, ppnenet):
    base = _f36_depi(depamor, ppnenet, 252)
    d = _accel(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depratejerkrank_10d_jerk_v018_signal(depamor, ppnenet):
    base = depamor / (depamor + ppnenet).replace(0, np.nan)
    d = _accel(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depburdenjerkdev_10d_jerk_v019_signal(depamor, revenue):
    base = depamor / revenue.replace(0, np.nan)
    d = _accel(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaijerksq_21d_jerk_v020_signal(sgna, revenue):
    base = _f36_sgai(sgna, revenue, 252)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaintjerk_10d_jerk_v021_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    d = _accel(base, 10)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaiprofitjerkz_10d_jerk_v022_signal(sgna, gp):
    base = sgna / gp.replace(0, np.nan)
    d = _accel(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgijerkrank_21d_jerk_v023_signal(debt, assets):
    base = _f36_lvgi(debt, assets, 252)
    d = _accel(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_leveragejerkdev_10d_jerk_v024_signal(debt, assets):
    base = debt / assets.replace(0, np.nan)
    d = _accel(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtrevjerksq_10d_jerk_v025_signal(debt, revenue):
    base = debt / revenue.replace(0, np.nan)
    d = _accel(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatajerk_10d_jerk_v026_signal(netinc, ncfo, assets):
    base = _f36_tata(netinc, ncfo, assets)
    d = _accel(base, 10)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatarevjerkz_10d_jerk_v027_signal(netinc, revenue):
    base = netinc / revenue.replace(0, np.nan)
    d = _accel(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cashconvjerkrank_10d_jerk_v028_signal(netinc, ncfo):
    base = ncfo / netinc.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _accel(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_roajerkdev_10d_jerk_v029_signal(netinc, assets):
    base = netinc / assets.replace(0, np.nan)
    d = _accel(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cfomarginjerksq_10d_jerk_v030_signal(ncfo, revenue):
    base = ncfo / revenue.replace(0, np.nan)
    d = _accel(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorejerk_21d_jerk_v031_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 252)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscore504jerkz_21d_jerk_v032_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 504)
    d = _accel(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_revsidejerkrank_21d_jerk_v033_signal(receivables, revenue, gp):
    base = (0.92 * _f36_dsri(receivables, revenue, 252) + 0.528 * _f36_gmi(gp, revenue, 252) + 0.892 * _f36_sgi(revenue, 252))
    d = _accel(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_costsidejerkdev_21d_jerk_v034_signal(assets, ppnenet, depamor, sgna, revenue, debt):
    base = (0.404 * _f36_aqi(assets, ppnenet, 252) + 0.115 * _f36_depi(depamor, ppnenet, 252) - 0.172 * _f36_sgai(sgna, revenue, 252) - 0.327 * _f36_lvgi(debt, assets, 252))
    d = _accel(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrigmijerksq_21d_jerk_v035_signal(receivables, revenue, gp):
    base = (_f36_dsri(receivables, revenue, 252) - 1.0) * (_f36_gmi(gp, revenue, 252) - 1.0)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgitatajerk_21d_jerk_v036_signal(revenue, netinc, ncfo, assets):
    base = (_f36_sgi(revenue, 252) - 1.0) * _f36_tata(netinc, ncfo, assets)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqidepijerkz_21d_jerk_v037_signal(assets, ppnenet, depamor):
    base = (_f36_aqi(assets, ppnenet, 252) - 1.0) + (_f36_depi(depamor, ppnenet, 252) - 1.0)
    d = _accel(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvncfojerkrank_10d_jerk_v038_signal(receivables, ncfo):
    base = receivables / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _accel(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetturnjerkdev_10d_jerk_v039_signal(revenue, assets):
    base = revenue / assets.replace(0, np.nan)
    d = _accel(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossassetjerksq_10d_jerk_v040_signal(gp, assets):
    base = gp / assets.replace(0, np.nan)
    d = _accel(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ncfomarginjerk_10d_jerk_v041_signal(ncfo, assets):
    base = ncfo / assets.replace(0, np.nan)
    d = _accel(base, 10)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ppnedebtjerkz_10d_jerk_v042_signal(ppnenet, debt):
    base = ppnenet / debt.replace(0, np.nan)
    d = _accel(base, 10)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtcfjerkrank_10d_jerk_v043_signal(debt, ncfo):
    base = debt / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _accel(base, 10)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_marginspreadjerkdev_10d_jerk_v044_signal(gp, revenue, sgna):
    base = (gp - sgna) / revenue.replace(0, np.nan)
    d = _accel(base, 10)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depdebtjerksq_10d_jerk_v045_signal(depamor, debt):
    base = depamor / debt.replace(0, np.nan)
    d = _accel(base, 10)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrijerkrank_42d_jerk_v046_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 252)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsri504jerkdev_42d_jerk_v047_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 504)
    d = _accel(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintjerksq_21d_jerk_v048_signal(receivables, revenue):
    base = receivables / revenue.replace(0, np.nan)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassetjerk_21d_jerk_v049_signal(receivables, assets):
    base = receivables / assets.replace(0, np.nan)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrizjerkz_42d_jerk_v050_signal(receivables, revenue):
    base = _z(_f36_dsri(receivables, revenue, 252), 252)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmijerkrank_42d_jerk_v051_signal(gp, revenue):
    base = _f36_gmi(gp, revenue, 252)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargjerkdev_21d_jerk_v052_signal(gp, revenue):
    base = gp / revenue.replace(0, np.nan)
    d = _accel(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsintjerksq_21d_jerk_v053_signal(gp, revenue):
    base = (revenue - gp) / revenue.replace(0, np.nan)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmizjerk_42d_jerk_v054_signal(gp, revenue):
    base = _z(_f36_gmi(gp, revenue, 252), 252)
    d = _accel(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqijerkz_42d_jerk_v055_signal(assets, ppnenet):
    base = _f36_aqi(assets, ppnenet, 252)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetjerkrank_21d_jerk_v056_signal(assets, ppnenet):
    base = 1.0 - ppnenet / assets.replace(0, np.nan)
    d = _accel(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_capintensjerkdev_21d_jerk_v057_signal(ppnenet, depamor):
    base = ppnenet / (ppnenet + depamor).replace(0, np.nan)
    d = _accel(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqizjerksq_42d_jerk_v058_signal(assets, ppnenet):
    base = _z(_f36_aqi(assets, ppnenet, 252), 252)
    d = _accel(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgijerk_42d_jerk_v059_signal(revenue):
    base = _f36_sgi(revenue, 252)
    d = _accel(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgi126jerkz_21d_jerk_v060_signal(revenue):
    base = _f36_sgi(revenue, 126)
    d = _accel(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgizjerkrank_42d_jerk_v061_signal(revenue):
    base = _z(_f36_sgi(revenue, 252), 252)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depijerkdev_42d_jerk_v062_signal(depamor, ppnenet):
    base = _f36_depi(depamor, ppnenet, 252)
    d = _accel(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depratejerksq_21d_jerk_v063_signal(depamor, ppnenet):
    base = depamor / (depamor + ppnenet).replace(0, np.nan)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depburdenjerk_21d_jerk_v064_signal(depamor, revenue):
    base = depamor / revenue.replace(0, np.nan)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaijerkz_42d_jerk_v065_signal(sgna, revenue):
    base = _f36_sgai(sgna, revenue, 252)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaintjerkrank_21d_jerk_v066_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    d = _accel(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaiprofitjerkdev_21d_jerk_v067_signal(sgna, gp):
    base = sgna / gp.replace(0, np.nan)
    d = _accel(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgijerksq_42d_jerk_v068_signal(debt, assets):
    base = _f36_lvgi(debt, assets, 252)
    d = _accel(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_leveragejerk_21d_jerk_v069_signal(debt, assets):
    base = debt / assets.replace(0, np.nan)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtrevjerkz_21d_jerk_v070_signal(debt, revenue):
    base = debt / revenue.replace(0, np.nan)
    d = _accel(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatajerkrank_21d_jerk_v071_signal(netinc, ncfo, assets):
    base = _f36_tata(netinc, ncfo, assets)
    d = _accel(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatarevjerkdev_21d_jerk_v072_signal(netinc, revenue):
    base = netinc / revenue.replace(0, np.nan)
    d = _accel(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cashconvjerksq_21d_jerk_v073_signal(netinc, ncfo):
    base = ncfo / netinc.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_roajerk_21d_jerk_v074_signal(netinc, assets):
    base = netinc / assets.replace(0, np.nan)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cfomarginjerkz_21d_jerk_v075_signal(ncfo, revenue):
    base = ncfo / revenue.replace(0, np.nan)
    d = _accel(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorejerkrank_42d_jerk_v076_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 252)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscore504jerkdev_42d_jerk_v077_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 504)
    d = _accel(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_revsidejerksq_42d_jerk_v078_signal(receivables, revenue, gp):
    base = (0.92 * _f36_dsri(receivables, revenue, 252) + 0.528 * _f36_gmi(gp, revenue, 252) + 0.892 * _f36_sgi(revenue, 252))
    d = _accel(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_costsidejerk_42d_jerk_v079_signal(assets, ppnenet, depamor, sgna, revenue, debt):
    base = (0.404 * _f36_aqi(assets, ppnenet, 252) + 0.115 * _f36_depi(depamor, ppnenet, 252) - 0.172 * _f36_sgai(sgna, revenue, 252) - 0.327 * _f36_lvgi(debt, assets, 252))
    d = _accel(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrigmijerkz_42d_jerk_v080_signal(receivables, revenue, gp):
    base = (_f36_dsri(receivables, revenue, 252) - 1.0) * (_f36_gmi(gp, revenue, 252) - 1.0)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgitatajerkrank_42d_jerk_v081_signal(revenue, netinc, ncfo, assets):
    base = (_f36_sgi(revenue, 252) - 1.0) * _f36_tata(netinc, ncfo, assets)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqidepijerkdev_42d_jerk_v082_signal(assets, ppnenet, depamor):
    base = (_f36_aqi(assets, ppnenet, 252) - 1.0) + (_f36_depi(depamor, ppnenet, 252) - 1.0)
    d = _accel(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvncfojerksq_21d_jerk_v083_signal(receivables, ncfo):
    base = receivables / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetturnjerk_21d_jerk_v084_signal(revenue, assets):
    base = revenue / assets.replace(0, np.nan)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossassetjerkz_21d_jerk_v085_signal(gp, assets):
    base = gp / assets.replace(0, np.nan)
    d = _accel(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ncfomarginjerkrank_21d_jerk_v086_signal(ncfo, assets):
    base = ncfo / assets.replace(0, np.nan)
    d = _accel(base, 21)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ppnedebtjerkdev_21d_jerk_v087_signal(ppnenet, debt):
    base = ppnenet / debt.replace(0, np.nan)
    d = _accel(base, 21)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtcfjerksq_21d_jerk_v088_signal(debt, ncfo):
    base = debt / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _accel(base, 21)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_marginspreadjerk_21d_jerk_v089_signal(gp, revenue, sgna):
    base = (gp - sgna) / revenue.replace(0, np.nan)
    d = _accel(base, 21)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depdebtjerkz_21d_jerk_v090_signal(depamor, debt):
    base = depamor / debt.replace(0, np.nan)
    d = _accel(base, 21)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrijerksq_63d_jerk_v091_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 252)
    d = _accel(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsri504jerk_63d_jerk_v092_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 504)
    d = _accel(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintjerkz_42d_jerk_v093_signal(receivables, revenue):
    base = receivables / revenue.replace(0, np.nan)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassetjerkrank_42d_jerk_v094_signal(receivables, assets):
    base = receivables / assets.replace(0, np.nan)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrizjerkdev_63d_jerk_v095_signal(receivables, revenue):
    base = _z(_f36_dsri(receivables, revenue, 252), 252)
    d = _accel(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmijerksq_63d_jerk_v096_signal(gp, revenue):
    base = _f36_gmi(gp, revenue, 252)
    d = _accel(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargjerk_42d_jerk_v097_signal(gp, revenue):
    base = gp / revenue.replace(0, np.nan)
    d = _accel(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsintjerkz_42d_jerk_v098_signal(gp, revenue):
    base = (revenue - gp) / revenue.replace(0, np.nan)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmizjerkrank_63d_jerk_v099_signal(gp, revenue):
    base = _z(_f36_gmi(gp, revenue, 252), 252)
    d = _accel(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqijerkdev_63d_jerk_v100_signal(assets, ppnenet):
    base = _f36_aqi(assets, ppnenet, 252)
    d = _accel(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetjerksq_42d_jerk_v101_signal(assets, ppnenet):
    base = 1.0 - ppnenet / assets.replace(0, np.nan)
    d = _accel(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_capintensjerk_42d_jerk_v102_signal(ppnenet, depamor):
    base = ppnenet / (ppnenet + depamor).replace(0, np.nan)
    d = _accel(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqizjerkz_63d_jerk_v103_signal(assets, ppnenet):
    base = _z(_f36_aqi(assets, ppnenet, 252), 252)
    d = _accel(base, 63)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgijerkrank_63d_jerk_v104_signal(revenue):
    base = _f36_sgi(revenue, 252)
    d = _accel(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgi126jerkdev_42d_jerk_v105_signal(revenue):
    base = _f36_sgi(revenue, 126)
    d = _accel(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgizjerksq_63d_jerk_v106_signal(revenue):
    base = _z(_f36_sgi(revenue, 252), 252)
    d = _accel(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depijerk_63d_jerk_v107_signal(depamor, ppnenet):
    base = _f36_depi(depamor, ppnenet, 252)
    d = _accel(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depratejerkz_42d_jerk_v108_signal(depamor, ppnenet):
    base = depamor / (depamor + ppnenet).replace(0, np.nan)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depburdenjerkrank_42d_jerk_v109_signal(depamor, revenue):
    base = depamor / revenue.replace(0, np.nan)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaijerkdev_63d_jerk_v110_signal(sgna, revenue):
    base = _f36_sgai(sgna, revenue, 252)
    d = _accel(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaintjerksq_42d_jerk_v111_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    d = _accel(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgaiprofitjerk_42d_jerk_v112_signal(sgna, gp):
    base = sgna / gp.replace(0, np.nan)
    d = _accel(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_lvgijerkz_63d_jerk_v113_signal(debt, assets):
    base = _f36_lvgi(debt, assets, 252)
    d = _accel(base, 63)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_leveragejerkrank_42d_jerk_v114_signal(debt, assets):
    base = debt / assets.replace(0, np.nan)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtrevjerkdev_42d_jerk_v115_signal(debt, revenue):
    base = debt / revenue.replace(0, np.nan)
    d = _accel(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatajerksq_42d_jerk_v116_signal(netinc, ncfo, assets):
    base = _f36_tata(netinc, ncfo, assets)
    d = _accel(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_tatarevjerk_42d_jerk_v117_signal(netinc, revenue):
    base = netinc / revenue.replace(0, np.nan)
    d = _accel(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cashconvjerkz_42d_jerk_v118_signal(netinc, ncfo):
    base = ncfo / netinc.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_roajerkrank_42d_jerk_v119_signal(netinc, assets):
    base = netinc / assets.replace(0, np.nan)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cfomarginjerkdev_42d_jerk_v120_signal(ncfo, revenue):
    base = ncfo / revenue.replace(0, np.nan)
    d = _accel(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscorejerksq_63d_jerk_v121_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 252)
    d = _accel(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_mscore504jerk_63d_jerk_v122_signal(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo):
    base = _f36_mscore(receivables, revenue, gp, assets, ppnenet, depamor, sgna, debt, netinc, ncfo, 504)
    d = _accel(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_revsidejerkz_63d_jerk_v123_signal(receivables, revenue, gp):
    base = (0.92 * _f36_dsri(receivables, revenue, 252) + 0.528 * _f36_gmi(gp, revenue, 252) + 0.892 * _f36_sgi(revenue, 252))
    d = _accel(base, 63)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_costsidejerkrank_63d_jerk_v124_signal(assets, ppnenet, depamor, sgna, revenue, debt):
    base = (0.404 * _f36_aqi(assets, ppnenet, 252) + 0.115 * _f36_depi(depamor, ppnenet, 252) - 0.172 * _f36_sgai(sgna, revenue, 252) - 0.327 * _f36_lvgi(debt, assets, 252))
    d = _accel(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrigmijerkdev_63d_jerk_v125_signal(receivables, revenue, gp):
    base = (_f36_dsri(receivables, revenue, 252) - 1.0) * (_f36_gmi(gp, revenue, 252) - 1.0)
    d = _accel(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgitatajerksq_63d_jerk_v126_signal(revenue, netinc, ncfo, assets):
    base = (_f36_sgi(revenue, 252) - 1.0) * _f36_tata(netinc, ncfo, assets)
    d = _accel(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqidepijerk_63d_jerk_v127_signal(assets, ppnenet, depamor):
    base = (_f36_aqi(assets, ppnenet, 252) - 1.0) + (_f36_depi(depamor, ppnenet, 252) - 1.0)
    d = _accel(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvncfojerkz_42d_jerk_v128_signal(receivables, ncfo):
    base = receivables / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_assetturnjerkrank_42d_jerk_v129_signal(revenue, assets):
    base = revenue / assets.replace(0, np.nan)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossassetjerkdev_42d_jerk_v130_signal(gp, assets):
    base = gp / assets.replace(0, np.nan)
    d = _accel(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ncfomarginjerksq_42d_jerk_v131_signal(ncfo, assets):
    base = ncfo / assets.replace(0, np.nan)
    d = _accel(base, 42)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_ppnedebtjerk_42d_jerk_v132_signal(ppnenet, debt):
    base = ppnenet / debt.replace(0, np.nan)
    d = _accel(base, 42)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_debtcfjerkz_42d_jerk_v133_signal(debt, ncfo):
    base = debt / ncfo.replace(0, np.nan).abs().clip(lower=1e-6)
    d = _accel(base, 42)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_marginspreadjerkrank_42d_jerk_v134_signal(gp, revenue, sgna):
    base = (gp - sgna) / revenue.replace(0, np.nan)
    d = _accel(base, 42)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_depdebtjerkdev_42d_jerk_v135_signal(depamor, debt):
    base = depamor / debt.replace(0, np.nan)
    d = _accel(base, 42)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrijerkz_126d_jerk_v136_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 252)
    d = _accel(base, 126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsri504jerkrank_126d_jerk_v137_signal(receivables, revenue):
    base = _f36_dsri(receivables, revenue, 504)
    d = _accel(base, 126)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvintjerkdev_63d_jerk_v138_signal(receivables, revenue):
    base = receivables / revenue.replace(0, np.nan)
    d = _accel(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_recvassetjerksq_63d_jerk_v139_signal(receivables, assets):
    base = receivables / assets.replace(0, np.nan)
    d = _accel(base, 63)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_dsrizjerk_126d_jerk_v140_signal(receivables, revenue):
    base = _z(_f36_dsri(receivables, revenue, 252), 252)
    d = _accel(base, 126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmijerkz_126d_jerk_v141_signal(gp, revenue):
    base = _f36_gmi(gp, revenue, 252)
    d = _accel(base, 126)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_grossmargjerkrank_63d_jerk_v142_signal(gp, revenue):
    base = gp / revenue.replace(0, np.nan)
    d = _accel(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_cogsintjerkdev_63d_jerk_v143_signal(gp, revenue):
    base = (revenue - gp) / revenue.replace(0, np.nan)
    d = _accel(base, 63)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_gmizjerksq_126d_jerk_v144_signal(gp, revenue):
    base = _z(_f36_gmi(gp, revenue, 252), 252)
    d = _accel(base, 126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqijerk_126d_jerk_v145_signal(assets, ppnenet):
    base = _f36_aqi(assets, ppnenet, 252)
    d = _accel(base, 126)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_softassetjerkz_63d_jerk_v146_signal(assets, ppnenet):
    base = 1.0 - ppnenet / assets.replace(0, np.nan)
    d = _accel(base, 63)
    out = _z(d, 252)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_capintensjerkrank_63d_jerk_v147_signal(ppnenet, depamor):
    base = ppnenet / (ppnenet + depamor).replace(0, np.nan)
    d = _accel(base, 63)
    out = _rank(d, 504)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_aqizjerkdev_126d_jerk_v148_signal(assets, ppnenet):
    base = _z(_f36_aqi(assets, ppnenet, 252), 252)
    d = _accel(base, 126)
    out = d - _mean(d, 126)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgijerksq_126d_jerk_v149_signal(revenue):
    base = _f36_sgi(revenue, 252)
    d = _accel(base, 126)
    out = np.sign(d) * (d.abs() ** 0.5)
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


def f36mb_f36_manipulation_beneish_sgi126jerk_63d_jerk_v150_signal(revenue):
    base = _f36_sgi(revenue, 126)
    d = _accel(base, 63)
    out = d
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36mb_f36_manipulation_beneish_dsrijerk_21d_jerk_v001_signal,
    f36mb_f36_manipulation_beneish_dsri504jerkz_21d_jerk_v002_signal,
    f36mb_f36_manipulation_beneish_recvintjerkrank_10d_jerk_v003_signal,
    f36mb_f36_manipulation_beneish_recvassetjerkdev_10d_jerk_v004_signal,
    f36mb_f36_manipulation_beneish_dsrizjerksq_21d_jerk_v005_signal,
    f36mb_f36_manipulation_beneish_gmijerk_21d_jerk_v006_signal,
    f36mb_f36_manipulation_beneish_grossmargjerkz_10d_jerk_v007_signal,
    f36mb_f36_manipulation_beneish_cogsintjerkrank_10d_jerk_v008_signal,
    f36mb_f36_manipulation_beneish_gmizjerkdev_21d_jerk_v009_signal,
    f36mb_f36_manipulation_beneish_aqijerksq_21d_jerk_v010_signal,
    f36mb_f36_manipulation_beneish_softassetjerk_10d_jerk_v011_signal,
    f36mb_f36_manipulation_beneish_capintensjerkz_10d_jerk_v012_signal,
    f36mb_f36_manipulation_beneish_aqizjerkrank_21d_jerk_v013_signal,
    f36mb_f36_manipulation_beneish_sgijerkdev_21d_jerk_v014_signal,
    f36mb_f36_manipulation_beneish_sgi126jerksq_10d_jerk_v015_signal,
    f36mb_f36_manipulation_beneish_sgizjerk_21d_jerk_v016_signal,
    f36mb_f36_manipulation_beneish_depijerkz_21d_jerk_v017_signal,
    f36mb_f36_manipulation_beneish_depratejerkrank_10d_jerk_v018_signal,
    f36mb_f36_manipulation_beneish_depburdenjerkdev_10d_jerk_v019_signal,
    f36mb_f36_manipulation_beneish_sgaijerksq_21d_jerk_v020_signal,
    f36mb_f36_manipulation_beneish_sgaintjerk_10d_jerk_v021_signal,
    f36mb_f36_manipulation_beneish_sgaiprofitjerkz_10d_jerk_v022_signal,
    f36mb_f36_manipulation_beneish_lvgijerkrank_21d_jerk_v023_signal,
    f36mb_f36_manipulation_beneish_leveragejerkdev_10d_jerk_v024_signal,
    f36mb_f36_manipulation_beneish_debtrevjerksq_10d_jerk_v025_signal,
    f36mb_f36_manipulation_beneish_tatajerk_10d_jerk_v026_signal,
    f36mb_f36_manipulation_beneish_tatarevjerkz_10d_jerk_v027_signal,
    f36mb_f36_manipulation_beneish_cashconvjerkrank_10d_jerk_v028_signal,
    f36mb_f36_manipulation_beneish_roajerkdev_10d_jerk_v029_signal,
    f36mb_f36_manipulation_beneish_cfomarginjerksq_10d_jerk_v030_signal,
    f36mb_f36_manipulation_beneish_mscorejerk_21d_jerk_v031_signal,
    f36mb_f36_manipulation_beneish_mscore504jerkz_21d_jerk_v032_signal,
    f36mb_f36_manipulation_beneish_revsidejerkrank_21d_jerk_v033_signal,
    f36mb_f36_manipulation_beneish_costsidejerkdev_21d_jerk_v034_signal,
    f36mb_f36_manipulation_beneish_dsrigmijerksq_21d_jerk_v035_signal,
    f36mb_f36_manipulation_beneish_sgitatajerk_21d_jerk_v036_signal,
    f36mb_f36_manipulation_beneish_aqidepijerkz_21d_jerk_v037_signal,
    f36mb_f36_manipulation_beneish_recvncfojerkrank_10d_jerk_v038_signal,
    f36mb_f36_manipulation_beneish_assetturnjerkdev_10d_jerk_v039_signal,
    f36mb_f36_manipulation_beneish_grossassetjerksq_10d_jerk_v040_signal,
    f36mb_f36_manipulation_beneish_ncfomarginjerk_10d_jerk_v041_signal,
    f36mb_f36_manipulation_beneish_ppnedebtjerkz_10d_jerk_v042_signal,
    f36mb_f36_manipulation_beneish_debtcfjerkrank_10d_jerk_v043_signal,
    f36mb_f36_manipulation_beneish_marginspreadjerkdev_10d_jerk_v044_signal,
    f36mb_f36_manipulation_beneish_depdebtjerksq_10d_jerk_v045_signal,
    f36mb_f36_manipulation_beneish_dsrijerkrank_42d_jerk_v046_signal,
    f36mb_f36_manipulation_beneish_dsri504jerkdev_42d_jerk_v047_signal,
    f36mb_f36_manipulation_beneish_recvintjerksq_21d_jerk_v048_signal,
    f36mb_f36_manipulation_beneish_recvassetjerk_21d_jerk_v049_signal,
    f36mb_f36_manipulation_beneish_dsrizjerkz_42d_jerk_v050_signal,
    f36mb_f36_manipulation_beneish_gmijerkrank_42d_jerk_v051_signal,
    f36mb_f36_manipulation_beneish_grossmargjerkdev_21d_jerk_v052_signal,
    f36mb_f36_manipulation_beneish_cogsintjerksq_21d_jerk_v053_signal,
    f36mb_f36_manipulation_beneish_gmizjerk_42d_jerk_v054_signal,
    f36mb_f36_manipulation_beneish_aqijerkz_42d_jerk_v055_signal,
    f36mb_f36_manipulation_beneish_softassetjerkrank_21d_jerk_v056_signal,
    f36mb_f36_manipulation_beneish_capintensjerkdev_21d_jerk_v057_signal,
    f36mb_f36_manipulation_beneish_aqizjerksq_42d_jerk_v058_signal,
    f36mb_f36_manipulation_beneish_sgijerk_42d_jerk_v059_signal,
    f36mb_f36_manipulation_beneish_sgi126jerkz_21d_jerk_v060_signal,
    f36mb_f36_manipulation_beneish_sgizjerkrank_42d_jerk_v061_signal,
    f36mb_f36_manipulation_beneish_depijerkdev_42d_jerk_v062_signal,
    f36mb_f36_manipulation_beneish_depratejerksq_21d_jerk_v063_signal,
    f36mb_f36_manipulation_beneish_depburdenjerk_21d_jerk_v064_signal,
    f36mb_f36_manipulation_beneish_sgaijerkz_42d_jerk_v065_signal,
    f36mb_f36_manipulation_beneish_sgaintjerkrank_21d_jerk_v066_signal,
    f36mb_f36_manipulation_beneish_sgaiprofitjerkdev_21d_jerk_v067_signal,
    f36mb_f36_manipulation_beneish_lvgijerksq_42d_jerk_v068_signal,
    f36mb_f36_manipulation_beneish_leveragejerk_21d_jerk_v069_signal,
    f36mb_f36_manipulation_beneish_debtrevjerkz_21d_jerk_v070_signal,
    f36mb_f36_manipulation_beneish_tatajerkrank_21d_jerk_v071_signal,
    f36mb_f36_manipulation_beneish_tatarevjerkdev_21d_jerk_v072_signal,
    f36mb_f36_manipulation_beneish_cashconvjerksq_21d_jerk_v073_signal,
    f36mb_f36_manipulation_beneish_roajerk_21d_jerk_v074_signal,
    f36mb_f36_manipulation_beneish_cfomarginjerkz_21d_jerk_v075_signal,
    f36mb_f36_manipulation_beneish_mscorejerkrank_42d_jerk_v076_signal,
    f36mb_f36_manipulation_beneish_mscore504jerkdev_42d_jerk_v077_signal,
    f36mb_f36_manipulation_beneish_revsidejerksq_42d_jerk_v078_signal,
    f36mb_f36_manipulation_beneish_costsidejerk_42d_jerk_v079_signal,
    f36mb_f36_manipulation_beneish_dsrigmijerkz_42d_jerk_v080_signal,
    f36mb_f36_manipulation_beneish_sgitatajerkrank_42d_jerk_v081_signal,
    f36mb_f36_manipulation_beneish_aqidepijerkdev_42d_jerk_v082_signal,
    f36mb_f36_manipulation_beneish_recvncfojerksq_21d_jerk_v083_signal,
    f36mb_f36_manipulation_beneish_assetturnjerk_21d_jerk_v084_signal,
    f36mb_f36_manipulation_beneish_grossassetjerkz_21d_jerk_v085_signal,
    f36mb_f36_manipulation_beneish_ncfomarginjerkrank_21d_jerk_v086_signal,
    f36mb_f36_manipulation_beneish_ppnedebtjerkdev_21d_jerk_v087_signal,
    f36mb_f36_manipulation_beneish_debtcfjerksq_21d_jerk_v088_signal,
    f36mb_f36_manipulation_beneish_marginspreadjerk_21d_jerk_v089_signal,
    f36mb_f36_manipulation_beneish_depdebtjerkz_21d_jerk_v090_signal,
    f36mb_f36_manipulation_beneish_dsrijerksq_63d_jerk_v091_signal,
    f36mb_f36_manipulation_beneish_dsri504jerk_63d_jerk_v092_signal,
    f36mb_f36_manipulation_beneish_recvintjerkz_42d_jerk_v093_signal,
    f36mb_f36_manipulation_beneish_recvassetjerkrank_42d_jerk_v094_signal,
    f36mb_f36_manipulation_beneish_dsrizjerkdev_63d_jerk_v095_signal,
    f36mb_f36_manipulation_beneish_gmijerksq_63d_jerk_v096_signal,
    f36mb_f36_manipulation_beneish_grossmargjerk_42d_jerk_v097_signal,
    f36mb_f36_manipulation_beneish_cogsintjerkz_42d_jerk_v098_signal,
    f36mb_f36_manipulation_beneish_gmizjerkrank_63d_jerk_v099_signal,
    f36mb_f36_manipulation_beneish_aqijerkdev_63d_jerk_v100_signal,
    f36mb_f36_manipulation_beneish_softassetjerksq_42d_jerk_v101_signal,
    f36mb_f36_manipulation_beneish_capintensjerk_42d_jerk_v102_signal,
    f36mb_f36_manipulation_beneish_aqizjerkz_63d_jerk_v103_signal,
    f36mb_f36_manipulation_beneish_sgijerkrank_63d_jerk_v104_signal,
    f36mb_f36_manipulation_beneish_sgi126jerkdev_42d_jerk_v105_signal,
    f36mb_f36_manipulation_beneish_sgizjerksq_63d_jerk_v106_signal,
    f36mb_f36_manipulation_beneish_depijerk_63d_jerk_v107_signal,
    f36mb_f36_manipulation_beneish_depratejerkz_42d_jerk_v108_signal,
    f36mb_f36_manipulation_beneish_depburdenjerkrank_42d_jerk_v109_signal,
    f36mb_f36_manipulation_beneish_sgaijerkdev_63d_jerk_v110_signal,
    f36mb_f36_manipulation_beneish_sgaintjerksq_42d_jerk_v111_signal,
    f36mb_f36_manipulation_beneish_sgaiprofitjerk_42d_jerk_v112_signal,
    f36mb_f36_manipulation_beneish_lvgijerkz_63d_jerk_v113_signal,
    f36mb_f36_manipulation_beneish_leveragejerkrank_42d_jerk_v114_signal,
    f36mb_f36_manipulation_beneish_debtrevjerkdev_42d_jerk_v115_signal,
    f36mb_f36_manipulation_beneish_tatajerksq_42d_jerk_v116_signal,
    f36mb_f36_manipulation_beneish_tatarevjerk_42d_jerk_v117_signal,
    f36mb_f36_manipulation_beneish_cashconvjerkz_42d_jerk_v118_signal,
    f36mb_f36_manipulation_beneish_roajerkrank_42d_jerk_v119_signal,
    f36mb_f36_manipulation_beneish_cfomarginjerkdev_42d_jerk_v120_signal,
    f36mb_f36_manipulation_beneish_mscorejerksq_63d_jerk_v121_signal,
    f36mb_f36_manipulation_beneish_mscore504jerk_63d_jerk_v122_signal,
    f36mb_f36_manipulation_beneish_revsidejerkz_63d_jerk_v123_signal,
    f36mb_f36_manipulation_beneish_costsidejerkrank_63d_jerk_v124_signal,
    f36mb_f36_manipulation_beneish_dsrigmijerkdev_63d_jerk_v125_signal,
    f36mb_f36_manipulation_beneish_sgitatajerksq_63d_jerk_v126_signal,
    f36mb_f36_manipulation_beneish_aqidepijerk_63d_jerk_v127_signal,
    f36mb_f36_manipulation_beneish_recvncfojerkz_42d_jerk_v128_signal,
    f36mb_f36_manipulation_beneish_assetturnjerkrank_42d_jerk_v129_signal,
    f36mb_f36_manipulation_beneish_grossassetjerkdev_42d_jerk_v130_signal,
    f36mb_f36_manipulation_beneish_ncfomarginjerksq_42d_jerk_v131_signal,
    f36mb_f36_manipulation_beneish_ppnedebtjerk_42d_jerk_v132_signal,
    f36mb_f36_manipulation_beneish_debtcfjerkz_42d_jerk_v133_signal,
    f36mb_f36_manipulation_beneish_marginspreadjerkrank_42d_jerk_v134_signal,
    f36mb_f36_manipulation_beneish_depdebtjerkdev_42d_jerk_v135_signal,
    f36mb_f36_manipulation_beneish_dsrijerkz_126d_jerk_v136_signal,
    f36mb_f36_manipulation_beneish_dsri504jerkrank_126d_jerk_v137_signal,
    f36mb_f36_manipulation_beneish_recvintjerkdev_63d_jerk_v138_signal,
    f36mb_f36_manipulation_beneish_recvassetjerksq_63d_jerk_v139_signal,
    f36mb_f36_manipulation_beneish_dsrizjerk_126d_jerk_v140_signal,
    f36mb_f36_manipulation_beneish_gmijerkz_126d_jerk_v141_signal,
    f36mb_f36_manipulation_beneish_grossmargjerkrank_63d_jerk_v142_signal,
    f36mb_f36_manipulation_beneish_cogsintjerkdev_63d_jerk_v143_signal,
    f36mb_f36_manipulation_beneish_gmizjerksq_126d_jerk_v144_signal,
    f36mb_f36_manipulation_beneish_aqijerk_126d_jerk_v145_signal,
    f36mb_f36_manipulation_beneish_softassetjerkz_63d_jerk_v146_signal,
    f36mb_f36_manipulation_beneish_capintensjerkrank_63d_jerk_v147_signal,
    f36mb_f36_manipulation_beneish_aqizjerkdev_126d_jerk_v148_signal,
    f36mb_f36_manipulation_beneish_sgijerksq_126d_jerk_v149_signal,
    f36mb_f36_manipulation_beneish_sgi126jerk_63d_jerk_v150_signal,
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

    print("OK f36_manipulation_beneish_3rd_derivatives_001_150_claude: %d features pass" % n_features)
