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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (zombie / survivor composite) =====
# Drivers: runway = cashneq / burn; dilution = sharesbas growth;
# leverage = debt / equity (or debt / cashneq); burn = max(opex - ncfo, 0).
def _f35_burn(opex, ncfo):
    # cash burn = operating spend not covered by operating cash flow
    return (opex - ncfo).clip(lower=0.0)


def _f35_runway(cashneq, opex, ncfo):
    # quarters of cash left at current burn rate
    burn = (opex - ncfo).clip(lower=0.0)
    return cashneq / burn.replace(0, np.nan)


def _f35_dilution(sharesbas, w):
    # share-count growth over w days = dilution intensity
    return sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0


def _f35_leverage(debt, equity):
    # debt relative to book equity (negative equity => extreme distress)
    return debt / equity.replace(0, np.nan)


def _f35_netcash(cashneq, debt):
    # net cash position relative to debt (solvency buffer)
    return (cashneq - debt) / (cashneq + debt).replace(0, np.nan)


def _f35_self_fund(ncfo, opex):
    # what fraction of opex is internally funded
    return ncfo / opex.replace(0, np.nan)


def _f35_cash_cov_debt(cashneq, debt):
    return cashneq / debt.replace(0, np.nan)


def _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, w):
    # survivor composite = runway x low-dilution x low-leverage, bounded
    runway = _f35_runway(cashneq, opex, ncfo)
    dil = _f35_dilution(sharesbas, w)
    lev = _f35_leverage(debt, equity)
    run_s = np.tanh(runway / 8.0)
    dil_s = 1.0 / (1.0 + 5.0 * dil.clip(lower=0))
    lev_s = 1.0 / (1.0 + lev.clip(lower=0))
    return run_s * dil_s * lev_s


# ============================================================
# survivor composite: runway x low-dilution x low-leverage, dilution over 1yr
def f35zs_f35_zombie_survivor_score_survivor_252d_base_v001_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    b = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor composite (2yr dilution) expressed as deviation from its 252d median
def f35zs_f35_zombie_survivor_score_survivor_504d_base_v002_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 504)
    med = surv.rolling(252, min_periods=126).median()
    b = surv - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie flag: burning cash AND diluting AND levered (all three on)
def f35zs_f35_zombie_survivor_score_zombieflag_252d_base_v003_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    burn = _f35_burn(opex, ncfo)
    dil = _f35_dilution(sharesbas, 252)
    lev = _f35_leverage(debt, equity)
    is_burn = (burn > 0).astype(float)
    is_dil = (dil > 0.05).astype(float)
    is_lev = (lev > 1.0).astype(float)
    b = is_burn * is_dil * is_lev + 0.001 * np.tanh(burn / opex.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie pressure: weighted sum of three distress drivers (continuous)
def f35zs_f35_zombie_survivor_score_zombiepress_252d_base_v004_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    b = burn_int + 3.0 * dil + lev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# graveyard-risk distance: weakest of the three survival legs (min-leg bottleneck)
def f35zs_f35_zombie_survivor_score_graveyard_252d_base_v005_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil_s = 1.0 / (1.0 + 5.0 * _f35_dilution(sharesbas, 252).clip(lower=0))
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    b = pd.concat([run_s, dil_s, lev_s], axis=1).min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash runway in quarters (level)
def f35zs_f35_zombie_survivor_score_runway_lvl_base_v006_signal(cashneq, opex, ncfo):
    b = _f35_runway(cashneq, opex, ncfo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway dispersion: spread of runway estimates across 21/63/126d burn windows
def f35zs_f35_zombie_survivor_score_runwayself_base_v007_signal(cashneq, opex, ncfo):
    def _run_w(w):
        burn = (_mean(opex, w) - _mean(ncfo, w)).clip(lower=0.0)
        return cashneq / burn.replace(0, np.nan)
    r1 = _run_w(21)
    r2 = _run_w(63)
    r3 = _run_w(126)
    stk = pd.concat([np.tanh(r1 / 8.0), np.tanh(r2 / 8.0), np.tanh(r3 / 8.0)], axis=1)
    b = stk.max(axis=1) - stk.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway trend: change in log runway over a quarter (deteriorating/improving)
def f35zs_f35_zombie_survivor_score_runwaytrend_63d_base_v008_signal(cashneq, opex, ncfo):
    runway = _f35_runway(cashneq, opex, ncfo).clip(lower=0.01)
    lr = np.log(runway)
    b = lr - lr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash solvency buffer (cash minus debt over total)
def f35zs_f35_zombie_survivor_score_netcash_lvl_base_v009_signal(cashneq, debt):
    b = _f35_netcash(cashneq, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage: debt / equity (distress when high or equity negative)
def f35zs_f35_zombie_survivor_score_leverage_lvl_base_v010_signal(debt, equity):
    b = _f35_leverage(debt, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution intensity over a year (share-count growth)
def f35zs_f35_zombie_survivor_score_dilution_252d_base_v011_signal(sharesbas):
    b = _f35_dilution(sharesbas, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted runway: runway-per-share momentum (cash runway diluted away)
def f35zs_f35_zombie_survivor_score_dilrunway_252d_base_v012_signal(cashneq, opex, ncfo, sharesbas):
    runway = _f35_runway(cashneq, opex, ncfo)
    rps = runway / sharesbas.replace(0, np.nan)
    lrps = np.log(rps.clip(lower=1e-12))
    b = lrps - lrps.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-per-share trend net of dilution drag (per-share cash creation/destruction)
def f35zs_f35_zombie_survivor_score_cashpershare_base_v013_signal(cashneq, sharesbas):
    cps = cashneq / sharesbas.replace(0, np.nan)
    lcps = np.log(cps.clip(lower=1e-6))
    b = (lcps - lcps.shift(63)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival score: log(cash coverage of debt) penalized by burn share of opex
def f35zs_f35_zombie_survivor_score_survscore_base_v014_signal(cashneq, debt, opex, ncfo):
    cov = _f35_cash_cov_debt(cashneq, debt).clip(lower=0.01)
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    b = np.log1p(cov) - burn_int
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding ratio (ncfo / opex): >1 sustainable, <0 burning
def f35zs_f35_zombie_survivor_score_selffund_base_v015_signal(ncfo, opex):
    b = _f35_self_fund(ncfo, opex)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distress triad count: how many of {burn, dilute, lever} active, smoothed over a quarter
def f35zs_f35_zombie_survivor_score_triadcount_252d_base_v016_signal(opex, ncfo, sharesbas, debt, equity):
    is_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    is_dil = (_f35_dilution(sharesbas, 252) > 0.05).astype(float)
    is_lev = (_f35_leverage(debt, equity) > 1.0).astype(float)
    cnt = is_burn + is_dil + is_lev
    b = cnt.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-quarter streak: consecutive quarters where opex exceeds ncfo
def f35zs_f35_zombie_survivor_score_burnstreak_base_v017_signal(opex, ncfo):
    burning = (_f35_burn(opex, ncfo) > 0).astype(float)
    grp = (burning == 0).cumsum()
    streak = burning.groupby(grp).cumsum()
    b = streak / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of debt, log-transformed and de-trended vs 252d mean
def f35zs_f35_zombie_survivor_score_cashcovdebt_base_v018_signal(cashneq, debt):
    cov = _f35_cash_cov_debt(cashneq, debt).clip(lower=1e-3)
    lcov = np.log(cov)
    b = lcov - _mean(lcov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity buffer per unit of burn: book equity vs annual burn
def f35zs_f35_zombie_survivor_score_eqburnbuf_base_v019_signal(equity, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    b = equity / (burn * 4.0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite z-score: survivor composite relative to its own 252d history
def f35zs_f35_zombie_survivor_score_survz_252d_base_v020_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    b = _z(surv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway-vs-dilution race: runway growth minus dilution rate
def f35zs_f35_zombie_survivor_score_runwayvsdil_base_v021_signal(cashneq, opex, ncfo, sharesbas):
    runway = _f35_runway(cashneq, opex, ncfo).clip(lower=0.01)
    lr_chg = np.log(runway) - np.log(runway.shift(63))
    dil = _f35_dilution(sharesbas, 63)
    b = lr_chg - 4.0 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# levered-burn interaction: leverage amplifies cash burn intensity
def f35zs_f35_zombie_survivor_score_levburn_base_v022_signal(debt, equity, opex, ncfo):
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    b = lev * burn_int
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-leverage divergence: leverage rank minus dilution rank (which is worse now)
def f35zs_f35_zombie_survivor_score_dillev_base_v023_signal(debt, equity, sharesbas):
    lev = _f35_leverage(debt, equity)
    dil = _f35_dilution(sharesbas, 252)
    b = _rank(lev, 252) - _rank(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival buffer balance: equity cushion vs debt+burn obligations (signed ratio)
def f35zs_f35_zombie_survivor_score_survbuf_base_v024_signal(cashneq, debt, equity, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    assets_side = cashneq + equity.clip(lower=0)
    oblig_side = debt + burn * 4.0
    b = (assets_side - oblig_side) / (assets_side + oblig_side).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-to-zombie momentum: change in (runway,-dil,-lev) distance over a quarter
def f35zs_f35_zombie_survivor_score_distzombie_base_v025_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    dist = (run_s ** 2 + (1.0 - np.tanh(5 * dil)) ** 2 + (1.0 - lev) ** 2) ** 0.5
    b = dist - dist.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn acceleration: change in burn-intensity over a quarter
def f35zs_f35_zombie_survivor_score_burnaccel_63d_base_v026_signal(opex, ncfo):
    burn_int = _f35_burn(opex, ncfo) / opex.replace(0, np.nan)
    b = burn_int - burn_int.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash trend over half a year (solvency improving/eroding)
def f35zs_f35_zombie_survivor_score_netcashtrend_126d_base_v027_signal(cashneq, debt):
    nc = _f35_netcash(cashneq, debt)
    b = nc - nc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash drawdown: cash vs its trailing 252d peak (depletion depth)
def f35zs_f35_zombie_survivor_score_cashdd_252d_base_v028_signal(cashneq):
    peak = _rmax(cashneq, 252)
    b = cashneq / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# years-to-zero cash combined with leverage penalty (graveyard timer)
def f35zs_f35_zombie_survivor_score_yearstozero_base_v029_signal(cashneq, opex, ncfo, debt, equity):
    runway = _f35_runway(cashneq, opex, ncfo)
    years = runway / 4.0
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    b = np.tanh(years / 2.0) * (1.0 - 0.5 * lev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak: fraction of last year with rising share count
def f35zs_f35_zombie_survivor_score_dilstreak_252d_base_v030_signal(sharesbas):
    rising = (sharesbas > sharesbas.shift(21)).astype(float)
    b = rising.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor rank: composite percentile-ranked vs its own 504d history
def f35zs_f35_zombie_survivor_score_survrank_504d_base_v031_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    b = _rank(surv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-funded dilution avoidance: dilution gated by runway (dilute-when-desperate)
def f35zs_f35_zombie_survivor_score_cashvsdil_base_v032_signal(cashneq, opex, ncfo, sharesbas):
    runway = _f35_runway(cashneq, opex, ncfo)
    low_run = (runway < 6.0).astype(float)
    dil = _f35_dilution(sharesbas, 63).clip(lower=0)
    desperate = (dil * 4.0 * low_run).rolling(63, min_periods=21).mean()
    b = _z(desperate, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-adjusted runway divergence: runway rank minus leverage rank
def f35zs_f35_zombie_survivor_score_levrunway_base_v033_signal(cashneq, opex, ncfo, debt, equity):
    runway = _f35_runway(cashneq, opex, ncfo)
    lev = _f35_leverage(debt, equity)
    b = _rank(runway, 252) + _rank(-lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn coverage by net cash, z-scored vs its own 252d history (de-trended)
def f35zs_f35_zombie_survivor_score_burncovnet_base_v034_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    cov = (cashneq - debt) / (burn * 4.0).replace(0, np.nan)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-debt cushion (inverse leverage, survival oriented)
def f35zs_f35_zombie_survivor_score_eqdebt_base_v035_signal(equity, debt):
    b = equity / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite distress momentum: zombie pressure change over a quarter
def f35zs_f35_zombie_survivor_score_pressmom_63d_base_v036_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 63).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    press = burn_int + 3.0 * dil + lev
    b = press - press.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets-proxy erosion: equity vs (cash+debt) capital base, ranked
def f35zs_f35_zombie_survivor_score_negeq_base_v037_signal(equity, debt, cashneq):
    cap = (cashneq + debt).replace(0, np.nan)
    eq_share = equity / cap
    b = _rank(eq_share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash burn rate per share (per-share depletion velocity)
def f35zs_f35_zombie_survivor_score_burnpershare_base_v038_signal(opex, ncfo, sharesbas):
    burn = _f35_burn(opex, ncfo)
    b = burn / sharesbas.replace(0, np.nan)
    bz = _z(b, 252)
    result = bz
    return result.replace([np.inf, -np.inf], np.nan)


# survivor composite using cash/debt instead of debt/equity for leverage leg
def f35zs_f35_zombie_survivor_score_survaltlev_base_v039_signal(cashneq, opex, ncfo, sharesbas, debt):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil_s = 1.0 / (1.0 + 5.0 * _f35_dilution(sharesbas, 252).clip(lower=0))
    cov = _f35_cash_cov_debt(cashneq, debt)
    lev_s = np.tanh(cov / 2.0)
    b = run_s * dil_s * lev_s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# graveyard distance z-scored vs 252d history (regime extremity)
def f35zs_f35_zombie_survivor_score_graveyardz_base_v040_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    nc = _f35_netcash(cashneq, debt)
    g = surv + 0.5 * nc
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-opex months of headroom (independent of ncfo)
def f35zs_f35_zombie_survivor_score_cashopex_base_v041_signal(cashneq, opex):
    b = cashneq / opex.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-funded burn: dilution rate scaled by burn intensity (raising to survive)
def f35zs_f35_zombie_survivor_score_dilfundburn_base_v042_signal(sharesbas, opex, ncfo):
    dil = _f35_dilution(sharesbas, 63).clip(lower=0)
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    b = dil * burn_int * 10.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival half-life: runway smoothed and bounded (sticky survivability)
def f35zs_f35_zombie_survivor_score_survhalflife_base_v043_signal(cashneq, opex, ncfo):
    runway = _f35_runway(cashneq, opex, ncfo)
    b = np.tanh(runway / 8.0).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage trend over a year (deleveraging vs releveraging)
def f35zs_f35_zombie_survivor_score_levtrend_252d_base_v044_signal(debt, equity):
    lev = _f35_leverage(debt, equity)
    b = lev - lev.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-pace disagreement: spread between short (63d) and long (504d) dilution rates
def f35zs_f35_zombie_survivor_score_survdisp_multi_base_v045_signal(sharesbas, cashneq, debt):
    d_short = _f35_dilution(sharesbas, 63) * 4.0
    d_long = _f35_dilution(sharesbas, 504)
    nc = _f35_netcash(cashneq, debt)
    b = (d_short - d_long) * (1.0 - nc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-while-levered intensity: magnitude of burn x leverage averaged over a quarter
def f35zs_f35_zombie_survivor_score_burnlevtime_base_v046_signal(opex, ncfo, debt, equity):
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    prod = burn_int * lev
    b = prod.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-floor breach frequency: fraction of last year cash below two quarters of burn
def f35zs_f35_zombie_survivor_score_cashfloor_base_v047_signal(cashneq, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    breach = (cashneq < 2.0 * burn).astype(float)
    freq = breach.rolling(252, min_periods=126).mean()
    depth = (1.0 - cashneq / (2.0 * burn).replace(0, np.nan)).clip(lower=0)
    b = freq + 0.5 * depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor-vs-zombie rank gap: survivor-leg rank minus zombie-pressure rank
def f35zs_f35_zombie_survivor_score_survminuszom_base_v048_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    zombie = burn_int + 3.0 * dil
    b = _rank(surv, 252) - _rank(zombie, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration: change in dilution rate over half a year
def f35zs_f35_zombie_survivor_score_dilaccel_126d_base_v049_signal(sharesbas):
    dil = _f35_dilution(sharesbas, 63)
    b = dil - dil.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of (debt + annual burn): total obligation coverage
def f35zs_f35_zombie_survivor_score_totobligcov_base_v050_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    b = cashneq / (debt + burn * 4.0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity erosion rate: log change in equity over a year (book destruction)
def f35zs_f35_zombie_survivor_score_eqerosion_252d_base_v051_signal(equity):
    pos = equity.clip(lower=1.0)
    b = np.log(pos) - np.log(pos.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash runway percentile vs own 504d history (debt-adjusted survival rank)
def f35zs_f35_zombie_survivor_score_netcashrun_base_v052_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    ncr = (cashneq - debt) / burn.replace(0, np.nan)
    b = _rank(ncr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor composite displacement: level minus its slow EMA (survival momentum)
def f35zs_f35_zombie_survivor_score_survsm_63d_base_v053_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    b = surv - surv.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn intensity z relative to leverage z (which distress dominates)
def f35zs_f35_zombie_survivor_score_burnvsleg_base_v054_signal(opex, ncfo, debt, equity):
    burn_int = _f35_burn(opex, ncfo) / opex.replace(0, np.nan)
    lev = _f35_leverage(debt, equity)
    b = _z(burn_int, 252) - _z(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding regime persistence: fraction of last year ncfo covered opex
def f35zs_f35_zombie_survivor_score_survselffund_base_v055_signal(ncfo, opex):
    covered = (ncfo >= opex).astype(float)
    frac = covered.rolling(252, min_periods=126).mean()
    depth = (ncfo / opex.replace(0, np.nan)).clip(-1, 1).rolling(63, min_periods=21).mean()
    b = frac + 0.3 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-per-cash divergence: dilution rank vs cash-level rank (raising despite cash?)
def f35zs_f35_zombie_survivor_score_dilpercash_base_v056_signal(sharesbas, cashneq, opex):
    dil = _f35_dilution(sharesbas, 63)
    cash_cov = cashneq / opex.replace(0, np.nan)
    b = _rank(dil, 252) + _rank(cash_cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie onset recency: days since the last quarter with all three flags on
def f35zs_f35_zombie_survivor_score_zombiepersist_base_v057_signal(opex, ncfo, sharesbas, debt, equity):
    is_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    is_dil = (_f35_dilution(sharesbas, 252) > 0.05).astype(float)
    is_lev = (_f35_leverage(debt, equity) > 1.0).astype(float)
    zom = (is_burn * is_dil * is_lev) > 0

    def _recency(a):
        idx = np.where(a > 0.5)[0]
        if len(idx) == 0:
            return float(len(a))
        return float(len(a) - 1 - idx[-1])
    b = zom.astype(float).rolling(252, min_periods=126).apply(_recency, raw=True) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash volatility-adjusted runway (steady vs erratic burn)
def f35zs_f35_zombie_survivor_score_runwaystab_base_v058_signal(cashneq, opex, ncfo):
    runway = _f35_runway(cashneq, opex, ncfo)
    vol = _std(runway, 126)
    b = runway / (1.0 + vol)
    bz = np.tanh(b / 8.0)
    result = bz
    return result.replace([np.inf, -np.inf], np.nan)


# solvency persistence: fraction of last year with positive equity AND net cash
def f35zs_f35_zombie_survivor_score_survsolvent_base_v059_signal(cashneq, debt, equity):
    solvent = ((equity > 0) & (cashneq > debt)).astype(float)
    frac = solvent.rolling(252, min_periods=126).mean()
    buf = np.tanh((cashneq - debt) / equity.clip(lower=1.0))
    b = frac + 0.5 * buf.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-burn z-score: how extreme the debt-vs-burn ratio is vs its own history
def f35zs_f35_zombie_survivor_score_debtburn_base_v060_signal(debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    ratio = debt / (burn * 4.0).replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite survival momentum: log survivor change over half a year
def f35zs_f35_zombie_survivor_score_survmom_126d_base_v061_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252).clip(lower=0.001)
    b = np.log(surv) - np.log(surv.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# graveyard risk: dilution-streak severity gated by short runway (distress only when low cash)
def f35zs_f35_zombie_survivor_score_gravedil_base_v062_signal(cashneq, opex, ncfo, sharesbas):
    rising = (sharesbas > sharesbas.shift(21)).astype(float)
    streak = rising.rolling(252, min_periods=126).mean()
    low_run = 1.0 / (1.0 + _f35_runway(cashneq, opex, ncfo).clip(lower=0))
    b = streak * low_run
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-cover-debt change over a year (solvency trajectory)
def f35zs_f35_zombie_survivor_score_covtrend_252d_base_v063_signal(cashneq, debt):
    cov = _f35_cash_cov_debt(cashneq, debt)
    b = cov - cov.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-funded-by-equity: equity drawdown relative to cumulative burn proxy
def f35zs_f35_zombie_survivor_score_eqfundburn_base_v064_signal(equity, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    cum_burn = burn.rolling(252, min_periods=126).sum()
    b = cum_burn / equity.clip(lower=1.0)
    bz = _z(b, 252)
    result = bz
    return result.replace([np.inf, -np.inf], np.nan)


# survivability worst-case: min survivor composite over the last half year
def f35zs_f35_zombie_survivor_score_survworst_126d_base_v065_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    b = _rmin(surv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-and-leverage joint distress (both rising together)
def f35zs_f35_zombie_survivor_score_dilevjoint_base_v066_signal(sharesbas, debt, equity):
    dil = _f35_dilution(sharesbas, 126).clip(lower=0)
    lev = _f35_leverage(debt, equity)
    lev_rise = (lev - lev.shift(126)).clip(lower=0)
    b = np.tanh(10.0 * dil) * np.tanh(lev_rise)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity vs solvency divergence: runway rank minus cash-cover-debt rank
def f35zs_f35_zombie_survivor_score_liqsolvgap_base_v067_signal(cashneq, opex, ncfo, debt):
    run = _f35_runway(cashneq, opex, ncfo)
    cov = _f35_cash_cov_debt(cashneq, debt)
    b = _rank(run, 252) - _rank(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor composite rank deviation from trailing median (regime shift)
def f35zs_f35_zombie_survivor_score_survreglshift_base_v068_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    med = surv.rolling(252, min_periods=126).median()
    b = surv - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net burn velocity acceleration: change in cash-depletion velocity over a quarter
def f35zs_f35_zombie_survivor_score_netburnvel_base_v069_signal(opex, ncfo, cashneq):
    burn = _f35_burn(opex, ncfo)
    vel = np.tanh((burn * 4.0) / cashneq.replace(0, np.nan))
    b = vel - vel.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash-over-equity momentum: change in solvency-per-book ratio over a quarter
def f35zs_f35_zombie_survivor_score_survovereq_base_v070_signal(cashneq, debt, equity):
    ratio = np.tanh((cashneq - debt) / equity.clip(lower=1.0))
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie-distance velocity: change in graveyard distance over a quarter
def f35zs_f35_zombie_survivor_score_gravevel_63d_base_v071_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    nc = _f35_netcash(cashneq, debt)
    g = surv + 0.5 * nc
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution burden vs equity erosion: dilution rank x equity-decline rank
def f35zs_f35_zombie_survivor_score_dilevburden_base_v072_signal(sharesbas, equity):
    dil = _f35_dilution(sharesbas, 126)
    eq_chg = equity - equity.shift(126)
    b = _rank(dil, 252) * _rank(-eq_chg, 252) * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivability vs prior cycle: composite rank now minus its rank 504d ago
def f35zs_f35_zombie_survivor_score_survcycle_base_v073_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    r = _rank(surv, 252)
    b = r - r.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash adequacy index: net cash + runway both contributing (balanced survival)
def f35zs_f35_zombie_survivor_score_cashadeq_base_v074_signal(cashneq, debt, opex, ncfo):
    nc = _f35_netcash(cashneq, debt)
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    b = 0.5 * nc + 0.5 * run_s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# graveyard flag tally: count of distress conditions met, smoothed over a quarter
def f35zs_f35_zombie_survivor_score_distresscomposite_base_v075_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    f_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    f_dil = (_f35_dilution(sharesbas, 252) > 0.10).astype(float)
    f_lev = (_f35_leverage(debt, equity) > 1.5).astype(float)
    f_run = (_f35_runway(cashneq, opex, ncfo) < 4.0).astype(float)
    f_neg = (equity < 0).astype(float)
    tally = f_burn + f_dil + f_lev + f_run + f_neg
    b = tally.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35zs_f35_zombie_survivor_score_survivor_252d_base_v001_signal,
    f35zs_f35_zombie_survivor_score_survivor_504d_base_v002_signal,
    f35zs_f35_zombie_survivor_score_zombieflag_252d_base_v003_signal,
    f35zs_f35_zombie_survivor_score_zombiepress_252d_base_v004_signal,
    f35zs_f35_zombie_survivor_score_graveyard_252d_base_v005_signal,
    f35zs_f35_zombie_survivor_score_runway_lvl_base_v006_signal,
    f35zs_f35_zombie_survivor_score_runwayself_base_v007_signal,
    f35zs_f35_zombie_survivor_score_runwaytrend_63d_base_v008_signal,
    f35zs_f35_zombie_survivor_score_netcash_lvl_base_v009_signal,
    f35zs_f35_zombie_survivor_score_leverage_lvl_base_v010_signal,
    f35zs_f35_zombie_survivor_score_dilution_252d_base_v011_signal,
    f35zs_f35_zombie_survivor_score_dilrunway_252d_base_v012_signal,
    f35zs_f35_zombie_survivor_score_cashpershare_base_v013_signal,
    f35zs_f35_zombie_survivor_score_survscore_base_v014_signal,
    f35zs_f35_zombie_survivor_score_selffund_base_v015_signal,
    f35zs_f35_zombie_survivor_score_triadcount_252d_base_v016_signal,
    f35zs_f35_zombie_survivor_score_burnstreak_base_v017_signal,
    f35zs_f35_zombie_survivor_score_cashcovdebt_base_v018_signal,
    f35zs_f35_zombie_survivor_score_eqburnbuf_base_v019_signal,
    f35zs_f35_zombie_survivor_score_survz_252d_base_v020_signal,
    f35zs_f35_zombie_survivor_score_runwayvsdil_base_v021_signal,
    f35zs_f35_zombie_survivor_score_levburn_base_v022_signal,
    f35zs_f35_zombie_survivor_score_dillev_base_v023_signal,
    f35zs_f35_zombie_survivor_score_survbuf_base_v024_signal,
    f35zs_f35_zombie_survivor_score_distzombie_base_v025_signal,
    f35zs_f35_zombie_survivor_score_burnaccel_63d_base_v026_signal,
    f35zs_f35_zombie_survivor_score_netcashtrend_126d_base_v027_signal,
    f35zs_f35_zombie_survivor_score_cashdd_252d_base_v028_signal,
    f35zs_f35_zombie_survivor_score_yearstozero_base_v029_signal,
    f35zs_f35_zombie_survivor_score_dilstreak_252d_base_v030_signal,
    f35zs_f35_zombie_survivor_score_survrank_504d_base_v031_signal,
    f35zs_f35_zombie_survivor_score_cashvsdil_base_v032_signal,
    f35zs_f35_zombie_survivor_score_levrunway_base_v033_signal,
    f35zs_f35_zombie_survivor_score_burncovnet_base_v034_signal,
    f35zs_f35_zombie_survivor_score_eqdebt_base_v035_signal,
    f35zs_f35_zombie_survivor_score_pressmom_63d_base_v036_signal,
    f35zs_f35_zombie_survivor_score_negeq_base_v037_signal,
    f35zs_f35_zombie_survivor_score_burnpershare_base_v038_signal,
    f35zs_f35_zombie_survivor_score_survaltlev_base_v039_signal,
    f35zs_f35_zombie_survivor_score_graveyardz_base_v040_signal,
    f35zs_f35_zombie_survivor_score_cashopex_base_v041_signal,
    f35zs_f35_zombie_survivor_score_dilfundburn_base_v042_signal,
    f35zs_f35_zombie_survivor_score_survhalflife_base_v043_signal,
    f35zs_f35_zombie_survivor_score_levtrend_252d_base_v044_signal,
    f35zs_f35_zombie_survivor_score_survdisp_multi_base_v045_signal,
    f35zs_f35_zombie_survivor_score_burnlevtime_base_v046_signal,
    f35zs_f35_zombie_survivor_score_cashfloor_base_v047_signal,
    f35zs_f35_zombie_survivor_score_survminuszom_base_v048_signal,
    f35zs_f35_zombie_survivor_score_dilaccel_126d_base_v049_signal,
    f35zs_f35_zombie_survivor_score_totobligcov_base_v050_signal,
    f35zs_f35_zombie_survivor_score_eqerosion_252d_base_v051_signal,
    f35zs_f35_zombie_survivor_score_netcashrun_base_v052_signal,
    f35zs_f35_zombie_survivor_score_survsm_63d_base_v053_signal,
    f35zs_f35_zombie_survivor_score_burnvsleg_base_v054_signal,
    f35zs_f35_zombie_survivor_score_survselffund_base_v055_signal,
    f35zs_f35_zombie_survivor_score_dilpercash_base_v056_signal,
    f35zs_f35_zombie_survivor_score_zombiepersist_base_v057_signal,
    f35zs_f35_zombie_survivor_score_runwaystab_base_v058_signal,
    f35zs_f35_zombie_survivor_score_survsolvent_base_v059_signal,
    f35zs_f35_zombie_survivor_score_debtburn_base_v060_signal,
    f35zs_f35_zombie_survivor_score_survmom_126d_base_v061_signal,
    f35zs_f35_zombie_survivor_score_gravedil_base_v062_signal,
    f35zs_f35_zombie_survivor_score_covtrend_252d_base_v063_signal,
    f35zs_f35_zombie_survivor_score_eqfundburn_base_v064_signal,
    f35zs_f35_zombie_survivor_score_survworst_126d_base_v065_signal,
    f35zs_f35_zombie_survivor_score_dilevjoint_base_v066_signal,
    f35zs_f35_zombie_survivor_score_liqsolvgap_base_v067_signal,
    f35zs_f35_zombie_survivor_score_survreglshift_base_v068_signal,
    f35zs_f35_zombie_survivor_score_netburnvel_base_v069_signal,
    f35zs_f35_zombie_survivor_score_survovereq_base_v070_signal,
    f35zs_f35_zombie_survivor_score_gravevel_63d_base_v071_signal,
    f35zs_f35_zombie_survivor_score_dilevburden_base_v072_signal,
    f35zs_f35_zombie_survivor_score_survcycle_base_v073_signal,
    f35zs_f35_zombie_survivor_score_cashadeq_base_v074_signal,
    f35zs_f35_zombie_survivor_score_distresscomposite_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_ZOMBIE_SURVIVOR_SCORE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    # cashneq depleting; ncfo swings around opex so burn flips on/off;
    # sharesbas drifting up = dilution; debt builds; equity can go negative.
    cashneq = _fund(3501, base=1.2e8, drift=-0.03, vol=0.11).rename("cashneq")
    ncfo = _fund(3502, base=9e7, drift=-0.01, vol=0.24, allow_neg=True).rename("ncfo")
    sharesbas = _fund(3503, base=5e7, drift=0.03, vol=0.05).rename("sharesbas")
    debt = _fund(3504, base=7e7, drift=0.015, vol=0.13).rename("debt")
    equity = _fund(3505, base=1.5e8, drift=-0.01, vol=0.14, allow_neg=True).rename("equity")
    opex = _fund(3506, base=6e7, drift=0.01, vol=0.08).rename("opex")

    cols = {"cashneq": cashneq, "ncfo": ncfo, "sharesbas": sharesbas,
            "debt": debt, "equity": equity, "opex": opex}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("cashneq", "ncfo", "sharesbas", "debt", "equity", "opex")
                   for c in meta["inputs"]), name
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f35_zombie_survivor_score_base_001_075_claude: %d features pass" % n_features)
