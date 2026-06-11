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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _jerk(s, w):
    # 2nd math derivative: change of the slope (acceleration/jerk) over w trading days
    slope = (s - s.shift(w)) / float(w)
    return (slope - slope.shift(w)) / float(w)


# ===== folder domain primitives (zombie / survivor composite) =====
def _f35_burn(opex, ncfo):
    return (opex - ncfo).clip(lower=0.0)


def _f35_runway(cashneq, opex, ncfo):
    burn = (opex - ncfo).clip(lower=0.0)
    return cashneq / burn.replace(0, np.nan)


def _f35_dilution(sharesbas, w):
    return sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0


def _f35_leverage(debt, equity):
    return debt / equity.replace(0, np.nan)


def _f35_netcash(cashneq, debt):
    return (cashneq - debt) / (cashneq + debt).replace(0, np.nan)


def _f35_self_fund(ncfo, opex):
    return ncfo / opex.replace(0, np.nan)


def _f35_cash_cov_debt(cashneq, debt):
    return cashneq / debt.replace(0, np.nan)


def _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, w):
    runway = _f35_runway(cashneq, opex, ncfo)
    dil = _f35_dilution(sharesbas, w)
    lev = _f35_leverage(debt, equity)
    run_s = np.tanh(runway / 8.0)
    dil_s = 1.0 / (1.0 + 5.0 * dil.clip(lower=0))
    lev_s = 1.0 / (1.0 + lev.clip(lower=0))
    return run_s * dil_s * lev_s


# ============================================================
# jerk of survivor composite (252d dilution), 63d ROC
def f35zs_f35_zombie_survivor_score_survivor_63d_jerk_v001_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    base = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of zombie pressure, 63d ROC
def f35zs_f35_zombie_survivor_score_zombiepress_63d_jerk_v002_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    base = burn_int + 3.0 * dil + lev
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash runway (tanh-compressed), 63d ROC
def f35zs_f35_zombie_survivor_score_runway_63d_jerk_v003_signal(cashneq, opex, ncfo):
    base = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash position, 63d ROC
def f35zs_f35_zombie_survivor_score_netcash_63d_jerk_v004_signal(cashneq, debt):
    base = _f35_netcash(cashneq, debt)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage (tanh), 63d ROC
def f35zs_f35_zombie_survivor_score_leverage_63d_jerk_v005_signal(debt, equity):
    base = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution rate, 63d ROC
def f35zs_f35_zombie_survivor_score_dilution_63d_jerk_v006_signal(sharesbas):
    base = _f35_dilution(sharesbas, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funding ratio, 63d ROC
def f35zs_f35_zombie_survivor_score_selffund_63d_jerk_v007_signal(ncfo, opex):
    base = _f35_self_fund(ncfo, opex)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-coverage-of-debt rank, 63d ROC
def f35zs_f35_zombie_survivor_score_cashcovdebt_63d_jerk_v008_signal(cashneq, debt):
    base = _rank(_f35_cash_cov_debt(cashneq, debt), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of graveyard distance (min-leg), 63d ROC
def f35zs_f35_zombie_survivor_score_graveyard_63d_jerk_v009_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil_s = 1.0 / (1.0 + 5.0 * _f35_dilution(sharesbas, 252).clip(lower=0))
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    base = pd.concat([run_s, dil_s, lev_s], axis=1).min(axis=1)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survival score rank (cov-rank minus burn-rank), 63d ROC
def f35zs_f35_zombie_survivor_score_survscore_63d_jerk_v010_signal(cashneq, debt, opex, ncfo):
    cov = _f35_cash_cov_debt(cashneq, debt)
    burn_int = _f35_burn(opex, ncfo) / opex.replace(0, np.nan)
    base = _rank(cov, 252) - _rank(burn_int, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of triad-count (smoothed), 21d ROC
def f35zs_f35_zombie_survivor_score_triadcount_21d_jerk_v011_signal(opex, ncfo, sharesbas, debt, equity):
    is_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    is_dil = (_f35_dilution(sharesbas, 252) > 0.05).astype(float)
    is_lev = (_f35_leverage(debt, equity) > 1.0).astype(float)
    base = (is_burn + is_dil + is_lev).rolling(63, min_periods=21).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of equity-to-debt cushion, 63d ROC
def f35zs_f35_zombie_survivor_score_eqdebt_63d_jerk_v012_signal(equity, debt):
    base = np.tanh(equity / debt.replace(0, np.nan))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-per-share (log), 63d ROC
def f35zs_f35_zombie_survivor_score_cps_63d_jerk_v013_signal(cashneq, sharesbas):
    base = np.log((cashneq / sharesbas.replace(0, np.nan)).clip(lower=1e-9))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor composite (504d dilution), 63d ROC
def f35zs_f35_zombie_survivor_score_survivorlong_63d_jerk_v014_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    base = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash runway (tanh), 63d ROC
def f35zs_f35_zombie_survivor_score_netcashrun_63d_jerk_v015_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    base = np.tanh(((cashneq - debt) / burn.replace(0, np.nan)) / 8.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of burn-vs-equity drain (burn relative to book equity), 21d ROC
def f35zs_f35_zombie_survivor_score_burnint_21d_jerk_v016_signal(opex, ncfo, equity):
    base = np.tanh(_f35_burn(opex, ncfo) / equity.clip(lower=1.0))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor z-score, 63d ROC
def f35zs_f35_zombie_survivor_score_survz_63d_jerk_v017_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    base = _z(surv, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-over-opex coverage, 63d ROC
def f35zs_f35_zombie_survivor_score_cashopex_63d_jerk_v018_signal(cashneq, opex):
    base = np.log((cashneq / opex.replace(0, np.nan)).clip(lower=1e-6))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of runway-rank minus dilution-rank (dilution-adjusted survival rank), 63d ROC
def f35zs_f35_zombie_survivor_score_dilrunway_63d_jerk_v019_signal(cashneq, opex, ncfo, sharesbas):
    runway = _f35_runway(cashneq, opex, ncfo)
    dil = _f35_dilution(sharesbas, 252)
    base = _rank(runway, 252) - _rank(dil, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of equity-buffer-per-burn (tanh), 63d ROC
def f35zs_f35_zombie_survivor_score_eqburnbuf_63d_jerk_v020_signal(equity, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    base = np.tanh(equity / (burn * 4.0).replace(0, np.nan))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor rank, 63d ROC
def f35zs_f35_zombie_survivor_score_survrank_63d_jerk_v021_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    base = _rank(surv, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of levered-burn interaction, 21d ROC
def f35zs_f35_zombie_survivor_score_levburn_21d_jerk_v022_signal(debt, equity, opex, ncfo):
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    base = lev * burn_int
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash z, 63d ROC
def f35zs_f35_zombie_survivor_score_netcashz_63d_jerk_v023_signal(cashneq, debt):
    base = _z(_f35_netcash(cashneq, debt), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash drawdown vs 252d peak, 63d ROC
def f35zs_f35_zombie_survivor_score_cashdd_63d_jerk_v024_signal(cashneq):
    peak = _rmax(cashneq, 252)
    base = cashneq / peak.replace(0, np.nan) - 1.0
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of years-to-zero (gated), 63d ROC
def f35zs_f35_zombie_survivor_score_yearstozero_63d_jerk_v025_signal(cashneq, opex, ncfo, debt, equity):
    years = _f35_runway(cashneq, opex, ncfo) / 4.0
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    base = np.tanh(years / 2.0) * (1.0 - 0.5 * lev)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution streak fraction, 21d ROC
def f35zs_f35_zombie_survivor_score_dilstreak_21d_jerk_v026_signal(sharesbas):
    rising = (sharesbas > sharesbas.shift(21)).astype(float)
    base = rising.rolling(252, min_periods=126).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survival buffer balance, 63d ROC
def f35zs_f35_zombie_survivor_score_survbuf_63d_jerk_v027_signal(cashneq, debt, equity, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    a = cashneq + equity.clip(lower=0)
    o = debt + burn * 4.0
    base = (a - o) / (a + o).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage-adjusted runway rank, 63d ROC
def f35zs_f35_zombie_survivor_score_levrunway_63d_jerk_v028_signal(cashneq, opex, ncfo, debt, equity):
    run = _f35_runway(cashneq, opex, ncfo)
    lev = _f35_leverage(debt, equity)
    base = _rank(run, 252) + _rank(-lev, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of total-obligation coverage rank, 63d ROC
def f35zs_f35_zombie_survivor_score_totobligcov_63d_jerk_v029_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    base = _rank(cashneq / (debt + burn * 4.0).replace(0, np.nan), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funding gap (tanh), 21d ROC
def f35zs_f35_zombie_survivor_score_selffundgap_21d_jerk_v030_signal(opex, ncfo, cashneq):
    base = np.tanh((opex - ncfo) / cashneq.replace(0, np.nan))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survival index, 63d ROC
def f35zs_f35_zombie_survivor_score_survindex_63d_jerk_v031_signal(cashneq, opex, ncfo, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    nc = _f35_netcash(cashneq, debt)
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    base = 0.4 * run_s + 0.3 * nc + 0.3 * (2.0 * lev_s - 1.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of debt-burden vs equity-cushion balance, 63d ROC
def f35zs_f35_zombie_survivor_score_debtburn_63d_jerk_v032_signal(debt, equity, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    obligation = debt + burn * 4.0
    cushion = equity.clip(lower=0) + 1.0
    base = (obligation - cushion) / (obligation + cushion).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of smoothed self-funding depth, 21d ROC
def f35zs_f35_zombie_survivor_score_ncfopostime_21d_jerk_v033_signal(ncfo, opex):
    base = _f35_self_fund(ncfo, opex).rolling(63, min_periods=21).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-coverage momentum, 21d ROC
def f35zs_f35_zombie_survivor_score_covmom_21d_jerk_v034_signal(cashneq, debt):
    lcov = np.log(_f35_cash_cov_debt(cashneq, debt).clip(lower=1e-3))
    base = lcov - lcov.shift(63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution-vs-leverage rank gap, 63d ROC
def f35zs_f35_zombie_survivor_score_dillevgap_63d_jerk_v035_signal(debt, equity, sharesbas):
    lev = _f35_leverage(debt, equity)
    dil = _f35_dilution(sharesbas, 252)
    base = _rank(lev, 252) - _rank(dil, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of runway minimum over a year, 63d ROC
def f35zs_f35_zombie_survivor_score_runwaymin_63d_jerk_v036_signal(cashneq, opex, ncfo):
    runway = _f35_runway(cashneq, opex, ncfo)
    base = np.tanh(_rmin(runway, 252) / 8.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of burn-vs-equity drain rank (equity-cushion depletion), 63d ROC
def f35zs_f35_zombie_survivor_score_netdrain_63d_jerk_v037_signal(opex, ncfo, equity):
    burn = _f35_burn(opex, ncfo)
    base = _rank((burn * 4.0) / equity.clip(lower=1.0), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cumulative-burn ratio z, 63d ROC
def f35zs_f35_zombie_survivor_score_cumburn_63d_jerk_v038_signal(opex, ncfo, cashneq):
    burn = _f35_burn(opex, ncfo)
    cum = burn.rolling(252, min_periods=126).sum()
    base = _z(np.log1p((cum / cashneq.replace(0, np.nan)).clip(lower=0)), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survival-score rank, 63d ROC
def f35zs_f35_zombie_survivor_score_survscorerank_63d_jerk_v039_signal(cashneq, debt, opex, ncfo):
    cov = _f35_cash_cov_debt(cashneq, debt).clip(lower=0.01)
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    base = _rank(np.log1p(cov) - burn_int, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-per-share z, 63d ROC
def f35zs_f35_zombie_survivor_score_cpsz_63d_jerk_v040_signal(cashneq, sharesbas):
    cps = cashneq / sharesbas.replace(0, np.nan)
    base = _z(cps, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage percentile, 63d ROC
def f35zs_f35_zombie_survivor_score_levpctile_63d_jerk_v041_signal(debt, equity):
    base = _rank(_f35_leverage(debt, equity), 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cumulative dilution (504d), 63d ROC
def f35zs_f35_zombie_survivor_score_cumdil_63d_jerk_v042_signal(sharesbas):
    base = _f35_dilution(sharesbas, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of burn-vs-leverage z spread, 63d ROC
def f35zs_f35_zombie_survivor_score_burnvslev_63d_jerk_v043_signal(opex, ncfo, debt, equity):
    burn_int = _f35_burn(opex, ncfo) / opex.replace(0, np.nan)
    lev = _f35_leverage(debt, equity)
    base = _z(burn_int, 252) - _z(lev, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash-to-opex coverage, 63d ROC
def f35zs_f35_zombie_survivor_score_netcashopex_63d_jerk_v044_signal(cashneq, debt, opex):
    base = np.tanh((cashneq - debt) / opex.replace(0, np.nan) / 4.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor cross-window agreement, 63d ROC
def f35zs_f35_zombie_survivor_score_survagree_63d_jerk_v045_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    s1 = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 126)
    s2 = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 504)
    base = (s1 - s2) / (s1 + s2).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of equity-share-of-capital z, 63d ROC
def f35zs_f35_zombie_survivor_score_eqassetrank_63d_jerk_v046_signal(equity, debt, cashneq):
    cap = (cashneq + debt + equity.clip(lower=0)).replace(0, np.nan)
    base = _z(equity / cap, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage trend, 21d ROC
def f35zs_f35_zombie_survivor_score_levtrend_21d_jerk_v047_signal(debt, equity):
    lev = _f35_leverage(debt, equity)
    base = lev - lev.shift(252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor half-life (smoothed), 63d ROC
def f35zs_f35_zombie_survivor_score_survhalflife_63d_jerk_v048_signal(cashneq, opex, ncfo):
    runway = _f35_runway(cashneq, opex, ncfo)
    base = np.tanh(runway / 8.0).ewm(span=63, min_periods=21).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of burn-quarter tally, 21d ROC
def f35zs_f35_zombie_survivor_score_burnqtrtally_21d_jerk_v049_signal(opex, ncfo):
    burning = (_f35_burn(opex, ncfo) > 0).astype(float)
    base = burning.rolling(504, min_periods=252).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of master survival score rank, 63d ROC
def f35zs_f35_zombie_survivor_score_masterscore_63d_jerk_v050_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil_s = 1.0 - np.tanh(6.0 * _f35_dilution(sharesbas, 252).clip(lower=0))
    lev_s = 1.0 - np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    nc = (_f35_netcash(cashneq, debt) + 1.0) / 2.0
    base = _rank(0.3 * run_s + 0.25 * dil_s + 0.25 * lev_s + 0.2 * nc, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor composite, faster 21d ROC
def f35zs_f35_zombie_survivor_score_survivor_21d_jerk_v051_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    base = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of runway (tanh), faster 21d ROC
def f35zs_f35_zombie_survivor_score_runway_21d_jerk_v052_signal(cashneq, opex, ncfo):
    base = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash, faster 21d ROC
def f35zs_f35_zombie_survivor_score_netcash_21d_jerk_v053_signal(cashneq, debt):
    base = _f35_netcash(cashneq, debt)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage (tanh), faster 21d ROC
def f35zs_f35_zombie_survivor_score_leverage_21d_jerk_v054_signal(debt, equity):
    base = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution rate, faster 21d ROC
def f35zs_f35_zombie_survivor_score_dilution_21d_jerk_v055_signal(sharesbas):
    base = _f35_dilution(sharesbas, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-coverage-of-debt rank, faster 21d ROC
def f35zs_f35_zombie_survivor_score_cashcovdebt_21d_jerk_v056_signal(cashneq, debt):
    base = _rank(_f35_cash_cov_debt(cashneq, debt), 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of zombie pressure, faster 21d ROC
def f35zs_f35_zombie_survivor_score_zombiepress_21d_jerk_v057_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 126).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    base = burn_int + 3.0 * dil + lev
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funding ratio, faster 21d ROC
def f35zs_f35_zombie_survivor_score_selffund_21d_jerk_v058_signal(ncfo, opex):
    base = _f35_self_fund(ncfo, opex)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survival index (runway/net-cash weighted), faster 21d ROC
def f35zs_f35_zombie_survivor_score_survindex_21d_jerk_v059_signal(cashneq, opex, ncfo, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    nc = _f35_netcash(cashneq, debt)
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    base = 0.55 * run_s + 0.35 * nc + 0.1 * (2.0 * lev_s - 1.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash runway (tanh), faster 21d ROC
def f35zs_f35_zombie_survivor_score_netcashrun_21d_jerk_v060_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    base = np.tanh(((cashneq - debt) / burn.replace(0, np.nan)) / 8.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor composite, longer 126d ROC
def f35zs_f35_zombie_survivor_score_survivor_126d_jerk_v061_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    base = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of runway (tanh), longer 126d ROC
def f35zs_f35_zombie_survivor_score_runway_126d_jerk_v062_signal(cashneq, opex, ncfo):
    base = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash, longer 126d ROC
def f35zs_f35_zombie_survivor_score_netcash_126d_jerk_v063_signal(cashneq, debt):
    base = _f35_netcash(cashneq, debt)
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage (tanh), longer 126d ROC
def f35zs_f35_zombie_survivor_score_leverage_126d_jerk_v064_signal(debt, equity):
    base = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution rate, longer 126d ROC
def f35zs_f35_zombie_survivor_score_dilution_126d_jerk_v065_signal(sharesbas):
    base = _f35_dilution(sharesbas, 252)
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-coverage-of-debt rank, longer 126d ROC
def f35zs_f35_zombie_survivor_score_cashcovdebt_126d_jerk_v066_signal(cashneq, debt):
    base = _rank(_f35_cash_cov_debt(cashneq, debt), 504)
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survival index, longer 126d ROC
def f35zs_f35_zombie_survivor_score_survindex_126d_jerk_v067_signal(cashneq, opex, ncfo, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    nc = _f35_netcash(cashneq, debt)
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    base = 0.4 * run_s + 0.3 * nc + 0.3 * (2.0 * lev_s - 1.0)
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-per-share (log), longer 126d ROC
def f35zs_f35_zombie_survivor_score_cps_126d_jerk_v068_signal(cashneq, sharesbas):
    base = np.log((cashneq / sharesbas.replace(0, np.nan)).clip(lower=1e-9))
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of equity-to-debt cushion, longer 126d ROC
def f35zs_f35_zombie_survivor_score_eqdebt_126d_jerk_v069_signal(equity, debt):
    base = np.tanh(equity / debt.replace(0, np.nan))
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of zombie pressure, longer 126d ROC
def f35zs_f35_zombie_survivor_score_zombiepress_126d_jerk_v070_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    base = burn_int + 3.0 * dil + lev
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-over-opex coverage, longer 126d ROC
def f35zs_f35_zombie_survivor_score_cashopex_126d_jerk_v071_signal(cashneq, opex):
    base = np.log((cashneq / opex.replace(0, np.nan)).clip(lower=1e-6))
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash runway (tanh), longer 126d ROC
def f35zs_f35_zombie_survivor_score_netcashrun_126d_jerk_v072_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    base = np.tanh(((cashneq - debt) / burn.replace(0, np.nan)) / 8.0)
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funding gap rank, 63d ROC
def f35zs_f35_zombie_survivor_score_selffundgap_63d_jerk_v073_signal(opex, ncfo, cashneq):
    base = _rank((opex - ncfo) / cashneq.replace(0, np.nan), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of graveyard percentile, 63d ROC
def f35zs_f35_zombie_survivor_score_gravepctile_63d_jerk_v074_signal(cashneq, opex, ncfo, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    nc = _f35_netcash(cashneq, debt)
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    base = _rank(run_s + nc + lev_s, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution-funded-survival, 63d ROC
def f35zs_f35_zombie_survivor_score_dilsurv_63d_jerk_v075_signal(sharesbas, cashneq, opex, ncfo):
    dil = _f35_dilution(sharesbas, 126).clip(lower=0)
    run = _f35_runway(cashneq, opex, ncfo)
    base = np.tanh(dil * 5.0) * np.tanh(run / 8.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of equity erosion rate, 63d ROC
def f35zs_f35_zombie_survivor_score_eqerosion_63d_jerk_v076_signal(equity):
    pos = equity.clip(lower=1.0)
    base = np.log(pos) - np.log(pos.shift(252))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of burn-acceleration, 21d ROC
def f35zs_f35_zombie_survivor_score_burnaccel_21d_jerk_v077_signal(opex, ncfo):
    burn_int = _f35_burn(opex, ncfo) / opex.replace(0, np.nan)
    base = burn_int - burn_int.shift(63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of debt-vs-cash rank, 63d ROC
def f35zs_f35_zombie_survivor_score_debtcashrank_63d_jerk_v078_signal(debt, cashneq):
    base = _rank(debt / cashneq.replace(0, np.nan), 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution-vs-cash divergence rank, 63d ROC
def f35zs_f35_zombie_survivor_score_dilpercash_63d_jerk_v079_signal(sharesbas, cashneq, opex):
    dil = _f35_dilution(sharesbas, 63)
    cash_cov = cashneq / opex.replace(0, np.nan)
    base = _rank(dil, 252) + _rank(cash_cov, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor displacement vs slow EMA, 21d ROC
def f35zs_f35_zombie_survivor_score_survdisp_21d_jerk_v080_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    base = surv - surv.ewm(span=126, min_periods=42).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash adequacy index (net-cash weighted), 126d ROC
def f35zs_f35_zombie_survivor_score_cashadeq_63d_jerk_v081_signal(cashneq, debt, opex, ncfo):
    nc = _f35_netcash(cashneq, debt)
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    base = 0.75 * nc + 0.25 * run_s
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-burn velocity rank, 21d ROC
def f35zs_f35_zombie_survivor_score_netburnvel_21d_jerk_v082_signal(opex, ncfo, cashneq):
    burn = _f35_burn(opex, ncfo)
    base = _rank((burn * 4.0) / cashneq.replace(0, np.nan), 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survival-over-equity (tanh), 63d ROC
def f35zs_f35_zombie_survivor_score_survovereq_63d_jerk_v083_signal(cashneq, debt, equity):
    base = np.tanh((cashneq - debt) / equity.clip(lower=1.0))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of liquidity-vs-solvency rank gap, 63d ROC
def f35zs_f35_zombie_survivor_score_liqsolv_63d_jerk_v084_signal(cashneq, opex, ncfo, debt):
    run = _f35_runway(cashneq, opex, ncfo)
    cov = _f35_cash_cov_debt(cashneq, debt)
    base = _rank(run, 252) - _rank(cov, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of equity-buffer-per-share z, 63d ROC
def f35zs_f35_zombie_survivor_score_bufpershare_63d_jerk_v085_signal(cashneq, debt, equity, sharesbas):
    cushion = cashneq - debt + equity.clip(lower=0)
    base = _z(cushion / sharesbas.replace(0, np.nan), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of smoothed dilution velocity, 21d ROC
def f35zs_f35_zombie_survivor_score_dilonsets_21d_jerk_v086_signal(sharesbas):
    base = _f35_dilution(sharesbas, 21).rolling(42, min_periods=21).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of burn-to-equity drain (tanh), 63d ROC
def f35zs_f35_zombie_survivor_score_burneqdrain_63d_jerk_v087_signal(opex, ncfo, equity):
    burn = _f35_burn(opex, ncfo)
    base = np.tanh((burn * 4.0) / equity.clip(lower=1.0))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of debt-cycle position, 63d ROC
def f35zs_f35_zombie_survivor_score_debtcyclepos_63d_jerk_v088_signal(debt, cashneq):
    hi = _rmax(debt, 504)
    lo = _rmin(debt, 504)
    pos = (debt - lo) / (hi - lo).replace(0, np.nan)
    cash_w = np.tanh(cashneq / debt.replace(0, np.nan) / 2.0)
    base = pos * (1.0 - 0.5 * cash_w)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage volatility, 63d ROC
def f35zs_f35_zombie_survivor_score_levvol_63d_jerk_v089_signal(debt, equity):
    base = _std(_f35_leverage(debt, equity), 126)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funding gap rank, 21d ROC
def f35zs_f35_zombie_survivor_score_selffundpersist_21d_jerk_v090_signal(ncfo, opex):
    base = _rank((opex - ncfo) / opex.replace(0, np.nan), 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of burn-volatility, 63d ROC
def f35zs_f35_zombie_survivor_score_burnvol_63d_jerk_v091_signal(opex, ncfo, cashneq):
    burn = _f35_burn(opex, ncfo)
    base = _std(burn / cashneq.replace(0, np.nan), 126)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution-velocity z, 21d ROC
def f35zs_f35_zombie_survivor_score_dilvelz_21d_jerk_v092_signal(sharesbas):
    base = _z(_f35_dilution(sharesbas, 21), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of burn-intensity z-score, 63d ROC
def f35zs_f35_zombie_survivor_score_burnint63_63d_jerk_v093_signal(opex, ncfo):
    base = _z(_f35_burn(opex, ncfo) / opex.replace(0, np.nan), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of equity-to-debt percentile, 63d ROC
def f35zs_f35_zombie_survivor_score_eqdebtrank_63d_jerk_v094_signal(equity, debt):
    base = _rank(equity / debt.replace(0, np.nan), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of runway resilience fraction, 21d ROC
def f35zs_f35_zombie_survivor_score_runwayresil_21d_jerk_v095_signal(cashneq, opex, ncfo):
    runway = _f35_runway(cashneq, opex, ncfo)
    base = (runway > 4.0).astype(float).rolling(252, min_periods=126).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash-to-opex (tanh), longer 126d ROC
def f35zs_f35_zombie_survivor_score_netcashopex_126d_jerk_v096_signal(cashneq, debt, opex):
    base = np.tanh((cashneq - debt) / opex.replace(0, np.nan) / 4.0)
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor-vs-zombie rank gap, 63d ROC
def f35zs_f35_zombie_survivor_score_survminuszom_63d_jerk_v097_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    base = _rank(surv, 252) - _rank(burn_int + 3.0 * dil, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash depletion velocity, 21d ROC
def f35zs_f35_zombie_survivor_score_cashvel_21d_jerk_v098_signal(cashneq):
    lc = np.log(cashneq.clip(lower=1.0))
    base = lc - lc.shift(63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage-adjusted burn coverage (log level), 63d ROC
def f35zs_f35_zombie_survivor_score_levburncov_63d_jerk_v099_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    cov = cashneq / (debt + burn * 4.0).replace(0, np.nan)
    base = np.log(cov.clip(lower=1e-6))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor worst-case (126d min), 63d ROC
def f35zs_f35_zombie_survivor_score_survworst_63d_jerk_v100_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    base = _rmin(surv, 126)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of triad smoothed (half-year), 63d ROC
def f35zs_f35_zombie_survivor_score_triadsm_63d_jerk_v101_signal(opex, ncfo, sharesbas, debt, equity):
    is_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    is_dil = (_f35_dilution(sharesbas, 252) > 0.05).astype(float)
    is_lev = (_f35_leverage(debt, equity) > 1.0).astype(float)
    base = (is_burn + is_dil + is_lev).ewm(span=126, min_periods=42).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash recovery from trough (tanh), 63d ROC
def f35zs_f35_zombie_survivor_score_cashrecov_63d_jerk_v102_signal(cashneq):
    lo = _rmin(cashneq, 504)
    base = np.tanh(cashneq / lo.replace(0, np.nan) - 1.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survival stability, 63d ROC
def f35zs_f35_zombie_survivor_score_survstab_63d_jerk_v103_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    ncr = (cashneq - debt) / burn.replace(0, np.nan)
    sncr = np.tanh(ncr / 8.0)
    base = sncr / (0.05 + _std(sncr, 126))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of debt-funded-burn (tanh), 21d ROC
def f35zs_f35_zombie_survivor_score_debtfundburn_21d_jerk_v104_signal(debt, opex, ncfo):
    dchg = (debt - debt.shift(63)).clip(lower=0)
    burn = _f35_burn(opex, ncfo)
    base = np.tanh(dchg / (burn + 1.0))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of solvency persistence, 21d ROC
def f35zs_f35_zombie_survivor_score_solventpersist_21d_jerk_v105_signal(cashneq, debt, equity):
    solvent = ((equity > 0) & (cashneq > debt)).astype(float)
    base = solvent.rolling(252, min_periods=126).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor cross EMA (fast-slow), 21d ROC
def f35zs_f35_zombie_survivor_score_survcross_21d_jerk_v106_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    base = surv.ewm(span=42, min_periods=21).mean() - surv.ewm(span=126, min_periods=42).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of forced-raise proxy, 21d ROC
def f35zs_f35_zombie_survivor_score_forcedraise_21d_jerk_v107_signal(sharesbas, cashneq, opex, ncfo):
    dil = _f35_dilution(sharesbas, 63).clip(lower=0)
    short = (_f35_runway(cashneq, opex, ncfo) < 8.0).astype(float)
    base = (dil * short * 10.0).rolling(21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of book-value-per-share rank, 126d ROC
def f35zs_f35_zombie_survivor_score_bvps_63d_jerk_v108_signal(equity, sharesbas):
    bvps = equity / sharesbas.replace(0, np.nan)
    base = _rank(bvps, 252)
    b = _jerk(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of obligation coverage rank, 63d ROC
def f35zs_f35_zombie_survivor_score_obligcovrank_63d_jerk_v109_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    cov = cashneq / (debt + burn * 4.0).replace(0, np.nan)
    base = _rank(cov, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage-vs-equity divergence, 63d ROC
def f35zs_f35_zombie_survivor_score_levequdiv_63d_jerk_v110_signal(debt, equity):
    dchg = (debt - debt.shift(126)) / debt.shift(126).replace(0, np.nan)
    echg = (equity - equity.shift(126)) / equity.shift(126).abs().replace(0, np.nan)
    base = dchg - echg
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor drawdown, 63d ROC
def f35zs_f35_zombie_survivor_score_survdd_63d_jerk_v111_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    base = surv / _rmax(surv, 252).replace(0, np.nan) - 1.0
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution acceleration sign-mag, 63d ROC
def f35zs_f35_zombie_survivor_score_dilaccel_63d_jerk_v112_signal(sharesbas):
    dil = _f35_dilution(sharesbas, 63)
    acc = dil - dil.shift(63)
    base = np.sign(acc) * (acc.abs() ** 0.5) * 5.0
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-adequacy minus dilution, 63d ROC
def f35zs_f35_zombie_survivor_score_cashadeqdil_63d_jerk_v113_signal(cashneq, opex, ncfo, sharesbas):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil = _f35_dilution(sharesbas, 252)
    base = run_s - np.tanh(8.0 * dil.clip(lower=0))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash-over-floor rank, 21d ROC
def f35zs_f35_zombie_survivor_score_netcashfloor_21d_jerk_v114_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    floor = (burn * 4.0).clip(lower=1.0)
    nc = (cashneq - debt).clip(lower=1.0)
    base = _rank(nc / floor, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of squeeze rank (lev up, eq down), 63d ROC
def f35zs_f35_zombie_survivor_score_squeeze_63d_jerk_v115_signal(debt, equity):
    lev_rise = (_f35_leverage(debt, equity) - _f35_leverage(debt, equity).shift(126)).clip(lower=0)
    eq_fall = (-(equity - equity.shift(126)) / equity.shift(126).abs().replace(0, np.nan)).clip(lower=0)
    base = _rank(lev_rise * eq_fall, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor regime deviation, 21d ROC
def f35zs_f35_zombie_survivor_score_survregime_21d_jerk_v116_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    med = surv.rolling(126, min_periods=63).median()
    base = (surv - med) / (surv.abs() + med.abs() + 1e-9)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of compound dil+lev distress rank, 63d ROC
def f35zs_f35_zombie_survivor_score_dilevcomp_63d_jerk_v117_signal(sharesbas, debt, equity):
    dil = _f35_dilution(sharesbas, 252)
    lev = _f35_leverage(debt, equity)
    base = _rank(dil, 252) + _rank(lev, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash-over-equity ratio, 21d ROC
def f35zs_f35_zombie_survivor_score_ncoeq_21d_jerk_v118_signal(cashneq, debt, equity):
    base = np.tanh((cashneq - debt) / equity.clip(lower=1.0))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of operating-funded survival momentum, 63d ROC
def f35zs_f35_zombie_survivor_score_survopmom_63d_jerk_v119_signal(cashneq, debt, ncfo, opex):
    cov = np.tanh(_f35_cash_cov_debt(cashneq, debt) / 2.0)
    sf = _f35_self_fund(ncfo, opex)
    base = cov + (sf - sf.shift(126)).clip(-1, 1)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of runway-weighted dilution penalty rank, 63d ROC
def f35zs_f35_zombie_survivor_score_dilrunpen_63d_jerk_v120_signal(sharesbas, cashneq, opex, ncfo):
    dil = _f35_dilution(sharesbas, 126).clip(lower=0)
    inv_run = 1.0 / (1.0 + _f35_runway(cashneq, opex, ncfo).clip(lower=0))
    base = _rank(dil * inv_run, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of leverage-definition disagreement rank, 63d ROC
def f35zs_f35_zombie_survivor_score_levdisp_63d_jerk_v121_signal(cashneq, debt, equity):
    lev_a = _f35_leverage(debt, equity)
    lev_b = 1.0 / _f35_cash_cov_debt(cashneq, debt).clip(lower=0.01)
    base = _rank(lev_a, 252) - _rank(lev_b, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor tanh-momentum, 21d ROC
def f35zs_f35_zombie_survivor_score_survtanhmom_21d_jerk_v122_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    base = np.tanh(15.0 * (surv - surv.shift(21)))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of debt-paydown-by-dilution, 63d ROC
def f35zs_f35_zombie_survivor_score_delevbydil_63d_jerk_v123_signal(debt, sharesbas):
    dlev = -(debt - debt.shift(126)) / debt.shift(126).replace(0, np.nan)
    dil = _f35_dilution(sharesbas, 126)
    base = np.tanh(dlev.clip(lower=0) * 5.0) * np.tanh(dil.clip(lower=0) * 8.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-floor breach frequency, 21d ROC
def f35zs_f35_zombie_survivor_score_cashfloor_21d_jerk_v124_signal(cashneq, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    base = (cashneq < 2.0 * burn).astype(float).rolling(252, min_periods=126).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor-net-flags, 63d ROC
def f35zs_f35_zombie_survivor_score_survnetflags_63d_jerk_v125_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    f_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    f_dil = (_f35_dilution(sharesbas, 252) > 0.05).astype(float)
    f_lev = (_f35_leverage(debt, equity) > 1.0).astype(float)
    tally = (f_burn + f_dil + f_lev).rolling(63, min_periods=21).mean()
    base = surv - 0.2 * tally
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of distance-to-zombie, 63d ROC
def f35zs_f35_zombie_survivor_score_distzombie_21d_jerk_v126_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    base = (run_s ** 2 + (1.0 - np.tanh(5 * dil)) ** 2 + (1.0 - lev) ** 2) ** 0.5
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution-burden vs equity erosion rank product, 63d ROC
def f35zs_f35_zombie_survivor_score_dilevburden_63d_jerk_v127_signal(sharesbas, equity):
    dil = _f35_dilution(sharesbas, 126)
    eq_chg = equity - equity.shift(126)
    base = _rank(dil, 252) * _rank(-eq_chg, 252) * 4.0
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of graveyard flag tally, 21d ROC
def f35zs_f35_zombie_survivor_score_gravetally_21d_jerk_v128_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    f_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    f_dil = (_f35_dilution(sharesbas, 252) > 0.10).astype(float)
    f_lev = (_f35_leverage(debt, equity) > 1.5).astype(float)
    f_run = (_f35_runway(cashneq, opex, ncfo) < 4.0).astype(float)
    f_neg = (equity < 0).astype(float)
    base = (f_burn + f_dil + f_lev + f_run + f_neg).rolling(63, min_periods=21).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor cycle rank change, 63d ROC
def f35zs_f35_zombie_survivor_score_survcycle_63d_jerk_v129_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    r = _rank(surv, 252)
    base = r - r.shift(504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-burn shortfall z, 21d ROC
def f35zs_f35_zombie_survivor_score_burnshortfall_21d_jerk_v130_signal(opex, ncfo, cashneq):
    base = _z((opex - ncfo) / cashneq.replace(0, np.nan), 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor convexity, 63d ROC
def f35zs_f35_zombie_survivor_score_survconvex_63d_jerk_v131_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    hi = _rmax(surv, 252)
    lo = _rmin(surv, 252)
    pos = (surv - lo) / (hi - lo).replace(0, np.nan)
    base = np.sign(pos - 0.5) * (pos - 0.5) ** 2 * 4.0
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of high-leverage regime fraction over a half year, 21d ROC
def f35zs_f35_zombie_survivor_score_zombietenure_21d_jerk_v132_signal(debt, equity):
    f_lev = (_f35_leverage(debt, equity) > 1.0).astype(float)
    base = f_lev.rolling(126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution-vs-cash desperate raise z, 21d ROC
def f35zs_f35_zombie_survivor_score_cashvsdil_21d_jerk_v133_signal(cashneq, opex, ncfo, sharesbas):
    runway = _f35_runway(cashneq, opex, ncfo)
    low_run = (runway < 6.0).astype(float)
    dil = _f35_dilution(sharesbas, 63).clip(lower=0)
    base = _z((dil * 4.0 * low_run).rolling(63, min_periods=21).mean(), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash trend, 63d ROC
def f35zs_f35_zombie_survivor_score_netcashtrend_63d_jerk_v134_signal(cashneq, debt):
    nc = _f35_netcash(cashneq, debt)
    base = nc - nc.shift(126)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of survivor displacement (level minus EMA), 63d ROC
def f35zs_f35_zombie_survivor_score_survdisp_63d_jerk_v135_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    base = surv - surv.ewm(span=63, min_periods=21).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of equity-funded-burn z, 63d ROC
def f35zs_f35_zombie_survivor_score_eqfundburn_63d_jerk_v136_signal(equity, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    cum = burn.rolling(252, min_periods=126).sum()
    base = _z(cum / equity.clip(lower=1.0), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cov-trend, 63d ROC
def f35zs_f35_zombie_survivor_score_covtrend_63d_jerk_v137_signal(cashneq, debt):
    cov = _f35_cash_cov_debt(cashneq, debt)
    base = cov - cov.shift(252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of levered-dilution joint distress rank, 63d ROC
def f35zs_f35_zombie_survivor_score_levdiljoint_63d_jerk_v138_signal(debt, equity, sharesbas):
    lev = _f35_leverage(debt, equity)
    dil = _f35_dilution(sharesbas, 252)
    base = (_rank(lev, 252) + 0.5) * (_rank(dil, 252) + 0.5)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of runway-rank minus dilution-rank (per-share survival), 21d ROC
def f35zs_f35_zombie_survivor_score_runwayps_21d_jerk_v139_signal(cashneq, opex, ncfo, sharesbas):
    runway = _f35_runway(cashneq, opex, ncfo)
    dil = _f35_dilution(sharesbas, 63)
    base = _rank(runway, 126) - _rank(dil, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of debt-financed-burn coverage (debt growth vs burn), 63d ROC
def f35zs_f35_zombie_survivor_score_debtburncash_63d_jerk_v140_signal(debt, cashneq, opex, ncfo):
    dchg = (debt - debt.shift(63)).clip(lower=0)
    burn = _f35_burn(opex, ncfo)
    base = np.tanh(dchg / (burn + cashneq * 0.01 + 1.0))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cumulative-burn-quarter tally with depth, 21d ROC
def f35zs_f35_zombie_survivor_score_burntally_21d_jerk_v141_signal(opex, ncfo):
    burning = (_f35_burn(opex, ncfo) > 0).astype(float)
    frac = burning.rolling(504, min_periods=252).mean()
    depth = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    base = frac + 0.3 * depth
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution-window survivor spread (short vs long dilution leg only), 63d ROC
def f35zs_f35_zombie_survivor_score_survprior_63d_jerk_v142_signal(sharesbas, cashneq, opex, ncfo, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    dil_short = 1.0 / (1.0 + 5.0 * _f35_dilution(sharesbas, 63).clip(lower=0))
    dil_long = 1.0 / (1.0 + 5.0 * _f35_dilution(sharesbas, 504).clip(lower=0))
    base = run_s * lev_s * (dil_short - dil_long)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funding rank, 63d ROC
def f35zs_f35_zombie_survivor_score_selffunddepth_63d_jerk_v143_signal(ncfo, opex):
    base = _rank(_f35_self_fund(ncfo, opex), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution-pace disagreement, 63d ROC
def f35zs_f35_zombie_survivor_score_dilpace_63d_jerk_v144_signal(sharesbas, cashneq, debt):
    d_short = _f35_dilution(sharesbas, 63) * 4.0
    d_long = _f35_dilution(sharesbas, 504)
    nc = _f35_netcash(cashneq, debt)
    base = (d_short - d_long) * (1.0 - nc)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of equity-solvency gate weight (equity vs cash), 21d ROC
def f35zs_f35_zombie_survivor_score_solventsurv_21d_jerk_v145_signal(cashneq, equity, debt):
    eq_w = np.tanh(equity / cashneq.replace(0, np.nan))
    nc = _f35_netcash(cashneq, debt)
    base = 0.5 * eq_w + 0.5 * nc
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash-over-floor z, 63d ROC
def f35zs_f35_zombie_survivor_score_netcashfloorlog_63d_jerk_v146_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    floor = (burn * 4.0).clip(lower=1.0)
    nc = (cashneq - debt).clip(lower=1.0)
    base = _z(np.log(nc / floor), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of distress-time streak (below median survivor), 21d ROC
def f35zs_f35_zombie_survivor_score_distresstime_21d_jerk_v147_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    zombie = (surv < surv.rolling(252, min_periods=126).median()).astype(float)
    grp = (zombie == 0).cumsum()
    base = zombie.groupby(grp).cumsum() / 252.0
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of burn-acceleration z, 63d ROC
def f35zs_f35_zombie_survivor_score_burnaccelz_63d_jerk_v148_signal(opex, ncfo):
    burn_int = _f35_burn(opex, ncfo) / opex.replace(0, np.nan)
    acc = burn_int - burn_int.shift(63)
    base = _z(acc, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-cash-to-opex coverage, 21d ROC
def f35zs_f35_zombie_survivor_score_netcashopex_21d_jerk_v149_signal(cashneq, debt, opex):
    base = (cashneq - debt) / opex.replace(0, np.nan)
    base = _z(base, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of master score weighted blend (non-ranked), 63d ROC
def f35zs_f35_zombie_survivor_score_masterblend_63d_jerk_v150_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil_s = 1.0 - np.tanh(6.0 * _f35_dilution(sharesbas, 252).clip(lower=0))
    lev_s = 1.0 - np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    nc = (_f35_netcash(cashneq, debt) + 1.0) / 2.0
    base = 0.3 * run_s + 0.25 * dil_s + 0.25 * lev_s + 0.2 * nc
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35zs_f35_zombie_survivor_score_survivor_63d_jerk_v001_signal,
    f35zs_f35_zombie_survivor_score_zombiepress_63d_jerk_v002_signal,
    f35zs_f35_zombie_survivor_score_runway_63d_jerk_v003_signal,
    f35zs_f35_zombie_survivor_score_netcash_63d_jerk_v004_signal,
    f35zs_f35_zombie_survivor_score_leverage_63d_jerk_v005_signal,
    f35zs_f35_zombie_survivor_score_dilution_63d_jerk_v006_signal,
    f35zs_f35_zombie_survivor_score_selffund_63d_jerk_v007_signal,
    f35zs_f35_zombie_survivor_score_cashcovdebt_63d_jerk_v008_signal,
    f35zs_f35_zombie_survivor_score_graveyard_63d_jerk_v009_signal,
    f35zs_f35_zombie_survivor_score_survscore_63d_jerk_v010_signal,
    f35zs_f35_zombie_survivor_score_triadcount_21d_jerk_v011_signal,
    f35zs_f35_zombie_survivor_score_eqdebt_63d_jerk_v012_signal,
    f35zs_f35_zombie_survivor_score_cps_63d_jerk_v013_signal,
    f35zs_f35_zombie_survivor_score_survivorlong_63d_jerk_v014_signal,
    f35zs_f35_zombie_survivor_score_netcashrun_63d_jerk_v015_signal,
    f35zs_f35_zombie_survivor_score_burnint_21d_jerk_v016_signal,
    f35zs_f35_zombie_survivor_score_survz_63d_jerk_v017_signal,
    f35zs_f35_zombie_survivor_score_cashopex_63d_jerk_v018_signal,
    f35zs_f35_zombie_survivor_score_dilrunway_63d_jerk_v019_signal,
    f35zs_f35_zombie_survivor_score_eqburnbuf_63d_jerk_v020_signal,
    f35zs_f35_zombie_survivor_score_survrank_63d_jerk_v021_signal,
    f35zs_f35_zombie_survivor_score_levburn_21d_jerk_v022_signal,
    f35zs_f35_zombie_survivor_score_netcashz_63d_jerk_v023_signal,
    f35zs_f35_zombie_survivor_score_cashdd_63d_jerk_v024_signal,
    f35zs_f35_zombie_survivor_score_yearstozero_63d_jerk_v025_signal,
    f35zs_f35_zombie_survivor_score_dilstreak_21d_jerk_v026_signal,
    f35zs_f35_zombie_survivor_score_survbuf_63d_jerk_v027_signal,
    f35zs_f35_zombie_survivor_score_levrunway_63d_jerk_v028_signal,
    f35zs_f35_zombie_survivor_score_totobligcov_63d_jerk_v029_signal,
    f35zs_f35_zombie_survivor_score_selffundgap_21d_jerk_v030_signal,
    f35zs_f35_zombie_survivor_score_survindex_63d_jerk_v031_signal,
    f35zs_f35_zombie_survivor_score_debtburn_63d_jerk_v032_signal,
    f35zs_f35_zombie_survivor_score_ncfopostime_21d_jerk_v033_signal,
    f35zs_f35_zombie_survivor_score_covmom_21d_jerk_v034_signal,
    f35zs_f35_zombie_survivor_score_dillevgap_63d_jerk_v035_signal,
    f35zs_f35_zombie_survivor_score_runwaymin_63d_jerk_v036_signal,
    f35zs_f35_zombie_survivor_score_netdrain_63d_jerk_v037_signal,
    f35zs_f35_zombie_survivor_score_cumburn_63d_jerk_v038_signal,
    f35zs_f35_zombie_survivor_score_survscorerank_63d_jerk_v039_signal,
    f35zs_f35_zombie_survivor_score_cpsz_63d_jerk_v040_signal,
    f35zs_f35_zombie_survivor_score_levpctile_63d_jerk_v041_signal,
    f35zs_f35_zombie_survivor_score_cumdil_63d_jerk_v042_signal,
    f35zs_f35_zombie_survivor_score_burnvslev_63d_jerk_v043_signal,
    f35zs_f35_zombie_survivor_score_netcashopex_63d_jerk_v044_signal,
    f35zs_f35_zombie_survivor_score_survagree_63d_jerk_v045_signal,
    f35zs_f35_zombie_survivor_score_eqassetrank_63d_jerk_v046_signal,
    f35zs_f35_zombie_survivor_score_levtrend_21d_jerk_v047_signal,
    f35zs_f35_zombie_survivor_score_survhalflife_63d_jerk_v048_signal,
    f35zs_f35_zombie_survivor_score_burnqtrtally_21d_jerk_v049_signal,
    f35zs_f35_zombie_survivor_score_masterscore_63d_jerk_v050_signal,
    f35zs_f35_zombie_survivor_score_survivor_21d_jerk_v051_signal,
    f35zs_f35_zombie_survivor_score_runway_21d_jerk_v052_signal,
    f35zs_f35_zombie_survivor_score_netcash_21d_jerk_v053_signal,
    f35zs_f35_zombie_survivor_score_leverage_21d_jerk_v054_signal,
    f35zs_f35_zombie_survivor_score_dilution_21d_jerk_v055_signal,
    f35zs_f35_zombie_survivor_score_cashcovdebt_21d_jerk_v056_signal,
    f35zs_f35_zombie_survivor_score_zombiepress_21d_jerk_v057_signal,
    f35zs_f35_zombie_survivor_score_selffund_21d_jerk_v058_signal,
    f35zs_f35_zombie_survivor_score_survindex_21d_jerk_v059_signal,
    f35zs_f35_zombie_survivor_score_netcashrun_21d_jerk_v060_signal,
    f35zs_f35_zombie_survivor_score_survivor_126d_jerk_v061_signal,
    f35zs_f35_zombie_survivor_score_runway_126d_jerk_v062_signal,
    f35zs_f35_zombie_survivor_score_netcash_126d_jerk_v063_signal,
    f35zs_f35_zombie_survivor_score_leverage_126d_jerk_v064_signal,
    f35zs_f35_zombie_survivor_score_dilution_126d_jerk_v065_signal,
    f35zs_f35_zombie_survivor_score_cashcovdebt_126d_jerk_v066_signal,
    f35zs_f35_zombie_survivor_score_survindex_126d_jerk_v067_signal,
    f35zs_f35_zombie_survivor_score_cps_126d_jerk_v068_signal,
    f35zs_f35_zombie_survivor_score_eqdebt_126d_jerk_v069_signal,
    f35zs_f35_zombie_survivor_score_zombiepress_126d_jerk_v070_signal,
    f35zs_f35_zombie_survivor_score_cashopex_126d_jerk_v071_signal,
    f35zs_f35_zombie_survivor_score_netcashrun_126d_jerk_v072_signal,
    f35zs_f35_zombie_survivor_score_selffundgap_63d_jerk_v073_signal,
    f35zs_f35_zombie_survivor_score_gravepctile_63d_jerk_v074_signal,
    f35zs_f35_zombie_survivor_score_dilsurv_63d_jerk_v075_signal,
    f35zs_f35_zombie_survivor_score_eqerosion_63d_jerk_v076_signal,
    f35zs_f35_zombie_survivor_score_burnaccel_21d_jerk_v077_signal,
    f35zs_f35_zombie_survivor_score_debtcashrank_63d_jerk_v078_signal,
    f35zs_f35_zombie_survivor_score_dilpercash_63d_jerk_v079_signal,
    f35zs_f35_zombie_survivor_score_survdisp_21d_jerk_v080_signal,
    f35zs_f35_zombie_survivor_score_cashadeq_63d_jerk_v081_signal,
    f35zs_f35_zombie_survivor_score_netburnvel_21d_jerk_v082_signal,
    f35zs_f35_zombie_survivor_score_survovereq_63d_jerk_v083_signal,
    f35zs_f35_zombie_survivor_score_liqsolv_63d_jerk_v084_signal,
    f35zs_f35_zombie_survivor_score_bufpershare_63d_jerk_v085_signal,
    f35zs_f35_zombie_survivor_score_dilonsets_21d_jerk_v086_signal,
    f35zs_f35_zombie_survivor_score_burneqdrain_63d_jerk_v087_signal,
    f35zs_f35_zombie_survivor_score_debtcyclepos_63d_jerk_v088_signal,
    f35zs_f35_zombie_survivor_score_levvol_63d_jerk_v089_signal,
    f35zs_f35_zombie_survivor_score_selffundpersist_21d_jerk_v090_signal,
    f35zs_f35_zombie_survivor_score_burnvol_63d_jerk_v091_signal,
    f35zs_f35_zombie_survivor_score_dilvelz_21d_jerk_v092_signal,
    f35zs_f35_zombie_survivor_score_burnint63_63d_jerk_v093_signal,
    f35zs_f35_zombie_survivor_score_eqdebtrank_63d_jerk_v094_signal,
    f35zs_f35_zombie_survivor_score_runwayresil_21d_jerk_v095_signal,
    f35zs_f35_zombie_survivor_score_netcashopex_126d_jerk_v096_signal,
    f35zs_f35_zombie_survivor_score_survminuszom_63d_jerk_v097_signal,
    f35zs_f35_zombie_survivor_score_cashvel_21d_jerk_v098_signal,
    f35zs_f35_zombie_survivor_score_levburncov_63d_jerk_v099_signal,
    f35zs_f35_zombie_survivor_score_survworst_63d_jerk_v100_signal,
    f35zs_f35_zombie_survivor_score_triadsm_63d_jerk_v101_signal,
    f35zs_f35_zombie_survivor_score_cashrecov_63d_jerk_v102_signal,
    f35zs_f35_zombie_survivor_score_survstab_63d_jerk_v103_signal,
    f35zs_f35_zombie_survivor_score_debtfundburn_21d_jerk_v104_signal,
    f35zs_f35_zombie_survivor_score_solventpersist_21d_jerk_v105_signal,
    f35zs_f35_zombie_survivor_score_survcross_21d_jerk_v106_signal,
    f35zs_f35_zombie_survivor_score_forcedraise_21d_jerk_v107_signal,
    f35zs_f35_zombie_survivor_score_bvps_63d_jerk_v108_signal,
    f35zs_f35_zombie_survivor_score_obligcovrank_63d_jerk_v109_signal,
    f35zs_f35_zombie_survivor_score_levequdiv_63d_jerk_v110_signal,
    f35zs_f35_zombie_survivor_score_survdd_63d_jerk_v111_signal,
    f35zs_f35_zombie_survivor_score_dilaccel_63d_jerk_v112_signal,
    f35zs_f35_zombie_survivor_score_cashadeqdil_63d_jerk_v113_signal,
    f35zs_f35_zombie_survivor_score_netcashfloor_21d_jerk_v114_signal,
    f35zs_f35_zombie_survivor_score_squeeze_63d_jerk_v115_signal,
    f35zs_f35_zombie_survivor_score_survregime_21d_jerk_v116_signal,
    f35zs_f35_zombie_survivor_score_dilevcomp_63d_jerk_v117_signal,
    f35zs_f35_zombie_survivor_score_ncoeq_21d_jerk_v118_signal,
    f35zs_f35_zombie_survivor_score_survopmom_63d_jerk_v119_signal,
    f35zs_f35_zombie_survivor_score_dilrunpen_63d_jerk_v120_signal,
    f35zs_f35_zombie_survivor_score_levdisp_63d_jerk_v121_signal,
    f35zs_f35_zombie_survivor_score_survtanhmom_21d_jerk_v122_signal,
    f35zs_f35_zombie_survivor_score_delevbydil_63d_jerk_v123_signal,
    f35zs_f35_zombie_survivor_score_cashfloor_21d_jerk_v124_signal,
    f35zs_f35_zombie_survivor_score_survnetflags_63d_jerk_v125_signal,
    f35zs_f35_zombie_survivor_score_distzombie_21d_jerk_v126_signal,
    f35zs_f35_zombie_survivor_score_dilevburden_63d_jerk_v127_signal,
    f35zs_f35_zombie_survivor_score_gravetally_21d_jerk_v128_signal,
    f35zs_f35_zombie_survivor_score_survcycle_63d_jerk_v129_signal,
    f35zs_f35_zombie_survivor_score_burnshortfall_21d_jerk_v130_signal,
    f35zs_f35_zombie_survivor_score_survconvex_63d_jerk_v131_signal,
    f35zs_f35_zombie_survivor_score_zombietenure_21d_jerk_v132_signal,
    f35zs_f35_zombie_survivor_score_cashvsdil_21d_jerk_v133_signal,
    f35zs_f35_zombie_survivor_score_netcashtrend_63d_jerk_v134_signal,
    f35zs_f35_zombie_survivor_score_survdisp_63d_jerk_v135_signal,
    f35zs_f35_zombie_survivor_score_eqfundburn_63d_jerk_v136_signal,
    f35zs_f35_zombie_survivor_score_covtrend_63d_jerk_v137_signal,
    f35zs_f35_zombie_survivor_score_levdiljoint_63d_jerk_v138_signal,
    f35zs_f35_zombie_survivor_score_runwayps_21d_jerk_v139_signal,
    f35zs_f35_zombie_survivor_score_debtburncash_63d_jerk_v140_signal,
    f35zs_f35_zombie_survivor_score_burntally_21d_jerk_v141_signal,
    f35zs_f35_zombie_survivor_score_survprior_63d_jerk_v142_signal,
    f35zs_f35_zombie_survivor_score_selffunddepth_63d_jerk_v143_signal,
    f35zs_f35_zombie_survivor_score_dilpace_63d_jerk_v144_signal,
    f35zs_f35_zombie_survivor_score_solventsurv_21d_jerk_v145_signal,
    f35zs_f35_zombie_survivor_score_netcashfloorlog_63d_jerk_v146_signal,
    f35zs_f35_zombie_survivor_score_distresstime_21d_jerk_v147_signal,
    f35zs_f35_zombie_survivor_score_burnaccelz_63d_jerk_v148_signal,
    f35zs_f35_zombie_survivor_score_netcashopex_21d_jerk_v149_signal,
    f35zs_f35_zombie_survivor_score_masterblend_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_ZOMBIE_SURVIVOR_SCORE_REGISTRY_JERK_001_150 = REGISTRY


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

    print("OK f35_zombie_survivor_score_3rd_derivatives_001_150_claude: %d features pass" % n_features)
