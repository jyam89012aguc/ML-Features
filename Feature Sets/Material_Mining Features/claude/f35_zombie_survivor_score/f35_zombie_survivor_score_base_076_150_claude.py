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
# survivor composite ranked vs own 252d history (cross-time survivability percentile)
def f35zs_f35_zombie_survivor_score_survpctile_252d_base_v076_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    b = _rank(surv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie pressure smoothed over a half year (persistent distress level)
def f35zs_f35_zombie_survivor_score_presssm_126d_base_v077_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    press = burn_int + 3.0 * dil + lev
    b = press.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# graveyard-distance percentile (how far into the safe zone, ranked)
def f35zs_f35_zombie_survivor_score_gravepctile_base_v078_signal(cashneq, opex, ncfo, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    nc = _f35_netcash(cashneq, debt)
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    g = run_s + nc + lev_s
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway in years, log-compressed (survival horizon)
def f35zs_f35_zombie_survivor_score_runwayyears_base_v079_signal(cashneq, opex, ncfo):
    years = _f35_runway(cashneq, opex, ncfo) / 4.0
    b = np.log1p(years.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-rate volatility: instability of the cash-burn signal (erratic vs steady)
def f35zs_f35_zombie_survivor_score_burnvol_126d_base_v080_signal(opex, ncfo, cashneq):
    burn = _f35_burn(opex, ncfo)
    burn_norm = burn / cashneq.replace(0, np.nan)
    b = _std(burn_norm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash position level (cash minus debt over total) z-scored
def f35zs_f35_zombie_survivor_score_netcashz_base_v081_signal(cashneq, debt):
    nc = _f35_netcash(cashneq, debt)
    b = _z(nc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage percentile vs own history (where in the debt cycle)
def f35zs_f35_zombie_survivor_score_levpctile_base_v082_signal(debt, equity):
    lev = _f35_leverage(debt, equity)
    b = _rank(lev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution over a 2yr cycle (long-horizon share creep)
def f35zs_f35_zombie_survivor_score_cumdil_504d_base_v083_signal(sharesbas):
    b = _f35_dilution(sharesbas, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-vs-cash interaction: dilution scaled by short runway (forced raise proxy)
def f35zs_f35_zombie_survivor_score_forcedraise_base_v084_signal(sharesbas, cashneq, opex, ncfo):
    dil = _f35_dilution(sharesbas, 63).clip(lower=0)
    short_run = (_f35_runway(cashneq, opex, ncfo) < 8.0).astype(float)
    raw = dil * short_run * 10.0
    b = raw.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival score: log net-cash coverage minus burn drag, ranked
def f35zs_f35_zombie_survivor_score_survscorerank_base_v085_signal(cashneq, debt, opex, ncfo):
    cov = _f35_cash_cov_debt(cashneq, debt).clip(lower=0.01)
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    raw = np.log1p(cov) - burn_int
    b = _rank(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie streak: consecutive quarters all-three flags active (graveyard tenure)
def f35zs_f35_zombie_survivor_score_zombietenure_base_v086_signal(opex, ncfo, sharesbas, debt, equity):
    f_burn = (_f35_burn(opex, ncfo) > 0)
    f_dil = (_f35_dilution(sharesbas, 252) > 0.05)
    f_lev = (_f35_leverage(debt, equity) > 1.0)
    zom = (f_burn & f_dil & f_lev).astype(float)
    grp = (zom == 0).cumsum()
    streak = zom.groupby(grp).cumsum()
    b = streak / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival buffer trend: net-cash-runway change over a half year
def f35zs_f35_zombie_survivor_score_bufftrend_126d_base_v087_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    ncr = (cashneq - debt) / burn.replace(0, np.nan)
    sncr = np.tanh(ncr / 8.0)
    b = sncr - sncr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity cushion vs dilution: book equity per share trend (per-share book erosion)
def f35zs_f35_zombie_survivor_score_bvps_trend_base_v088_signal(equity, sharesbas):
    bvps = equity / sharesbas.replace(0, np.nan)
    b = np.sign(bvps) * np.log1p(bvps.abs()) - np.sign(bvps.shift(126)) * np.log1p(bvps.shift(126).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap: opex not covered by ncfo, per unit cash (depletion pressure)
def f35zs_f35_zombie_survivor_score_selffundgap_base_v089_signal(opex, ncfo, cashneq):
    gap = (opex - ncfo) / cashneq.replace(0, np.nan)
    b = np.tanh(gap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triad flag tally smoothed at half-year (slow distress regime)
def f35zs_f35_zombie_survivor_score_triadsm_126d_base_v090_signal(opex, ncfo, sharesbas, debt, equity):
    is_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    is_dil = (_f35_dilution(sharesbas, 252) > 0.05).astype(float)
    is_lev = (_f35_leverage(debt, equity) > 1.0).astype(float)
    cnt = is_burn + is_dil + is_lev
    b = cnt.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage-of-debt momentum (solvency improving/eroding over a quarter)
def f35zs_f35_zombie_survivor_score_covmom_63d_base_v091_signal(cashneq, debt):
    cov = _f35_cash_cov_debt(cashneq, debt)
    lcov = np.log(cov.clip(lower=1e-3))
    b = lcov - lcov.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# levered-dilution joint percentile (both distress legs ranked together)
def f35zs_f35_zombie_survivor_score_levdilrank_base_v092_signal(debt, equity, sharesbas):
    lev = _f35_leverage(debt, equity)
    dil = _f35_dilution(sharesbas, 252)
    b = (_rank(lev, 252) + 0.5) * (_rank(dil, 252) + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway worst-case over a year (minimum survival horizon)
def f35zs_f35_zombie_survivor_score_runwaymin_252d_base_v093_signal(cashneq, opex, ncfo):
    runway = _f35_runway(cashneq, opex, ncfo)
    b = np.tanh(_rmin(runway, 252) / 8.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-burn drain rate: annual burn as a fraction of net cash (debt-adjusted drain)
def f35zs_f35_zombie_survivor_score_netdrain_base_v094_signal(opex, ncfo, cashneq, debt):
    burn = _f35_burn(opex, ncfo)
    nc = (cashneq - debt).clip(lower=1.0)
    drain = (burn * 4.0) / nc
    b = _z(np.log1p(drain), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-definition disagreement: d/e-based vs cash/debt-based leverage rank gap
def f35zs_f35_zombie_survivor_score_survlevdisp_base_v095_signal(cashneq, debt, equity):
    lev_a = _f35_leverage(debt, equity)
    lev_b = 1.0 / _f35_cash_cov_debt(cashneq, debt).clip(lower=0.01)
    b = _rank(lev_a, 252) - _rank(lev_b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulated burn over a year relative to cash (cumulative depletion ratio)
def f35zs_f35_zombie_survivor_score_cumburn_252d_base_v096_signal(opex, ncfo, cashneq):
    burn = _f35_burn(opex, ncfo)
    cum = burn.rolling(252, min_periods=126).sum()
    ratio = cum / cashneq.replace(0, np.nan)
    b = _z(np.log1p(ratio.clip(lower=0)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration sign x magnitude (worsening vs easing dilution)
def f35zs_f35_zombie_survivor_score_dilaccelsm_base_v097_signal(sharesbas):
    dil = _f35_dilution(sharesbas, 63)
    acc = dil - dil.shift(63)
    b = np.sign(acc) * (acc.abs() ** 0.5) * 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival index: weighted blend of runway, net-cash, low-leverage (positive=safe)
def f35zs_f35_zombie_survivor_score_survindex_base_v098_signal(cashneq, opex, ncfo, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    nc = _f35_netcash(cashneq, debt)
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    b = 0.4 * run_s + 0.3 * nc + 0.3 * (2.0 * lev_s - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn intensity z (how extreme current burn is vs own history)
def f35zs_f35_zombie_survivor_score_burnintz_base_v099_signal(opex, ncfo):
    burn_int = _f35_burn(opex, ncfo) / opex.replace(0, np.nan)
    b = _z(burn_int, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-vs-cash regime: months of cash that debt would consume, ranked
def f35zs_f35_zombie_survivor_score_debtcashrank_base_v100_signal(debt, cashneq):
    ratio = debt / cashneq.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor composite acceleration: change in survivor momentum over a quarter
def f35zs_f35_zombie_survivor_score_survaccel_base_v101_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    mom = surv - surv.shift(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-debt percentile (inverse leverage rank, survival oriented)
def f35zs_f35_zombie_survivor_score_eqdebtrank_base_v102_signal(equity, debt):
    ratio = equity / debt.replace(0, np.nan)
    b = _rank(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-funded-survival: dilution rate times runway extension proxy
def f35zs_f35_zombie_survivor_score_dilsurv_base_v103_signal(sharesbas, cashneq, opex, ncfo):
    dil = _f35_dilution(sharesbas, 126).clip(lower=0)
    run = _f35_runway(cashneq, opex, ncfo)
    b = np.tanh(dil * 5.0) * np.tanh(run / 8.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn coverage stability: net-cash-runway divided by its volatility (steady survival)
def f35zs_f35_zombie_survivor_score_survstability_base_v104_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    ncr = (cashneq - debt) / burn.replace(0, np.nan)
    sncr = np.tanh(ncr / 8.0)
    vol = _std(sncr, 126)
    b = sncr / (0.05 + vol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie pressure z (distress extremity vs own history)
def f35zs_f35_zombie_survivor_score_pressz_base_v105_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    press = burn_int + 3.0 * dil + lev
    b = _z(press, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash adequacy minus dilution drag (net survival after share creep)
def f35zs_f35_zombie_survivor_score_cashadeqdil_base_v106_signal(cashneq, opex, ncfo, sharesbas):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil = _f35_dilution(sharesbas, 252)
    b = run_s - np.tanh(8.0 * dil.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage build vs equity erosion divergence (which side worsens faster)
def f35zs_f35_zombie_survivor_score_levequdiv_base_v107_signal(debt, equity):
    dchg = (debt - debt.shift(126)) / debt.shift(126).replace(0, np.nan)
    echg = (equity - equity.shift(126)) / equity.shift(126).abs().replace(0, np.nan)
    b = dchg - echg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor composite drawdown: surv vs its trailing 252d peak (survivability erosion)
def f35zs_f35_zombie_survivor_score_survdd_252d_base_v108_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    peak = _rmax(surv, 252)
    b = surv / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-per-share level z (per-share liquidity backing)
def f35zs_f35_zombie_survivor_score_cpsz_base_v109_signal(cashneq, sharesbas):
    cps = cashneq / sharesbas.replace(0, np.nan)
    b = _z(cps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# graveyard timer: years-to-zero capped, penalized by leverage percentile
def f35zs_f35_zombie_survivor_score_gravetimer_base_v110_signal(cashneq, opex, ncfo, debt, equity):
    years = (_f35_runway(cashneq, opex, ncfo) / 4.0).clip(upper=10.0)
    levp = _rank(_f35_leverage(debt, equity), 252) + 0.5
    b = np.tanh(years / 2.0) * (1.0 - 0.6 * levp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding streak: fraction of last 2yr ncfo positive (operating viability)
def f35zs_f35_zombie_survivor_score_ncfopostime_base_v111_signal(ncfo, opex):
    pos = (ncfo > 0).astype(float)
    frac = pos.rolling(504, min_periods=252).mean()
    depth = _f35_self_fund(ncfo, opex).clip(-1, 1).rolling(126, min_periods=63).mean()
    b = frac + 0.2 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash floor breach frequency: fraction of last year net cash below annual burn
def f35zs_f35_zombie_survivor_score_netcashfloor_base_v112_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    floor = burn * 4.0
    nc = cashneq - debt
    breach = (nc < floor).astype(float)
    freq = breach.rolling(252, min_periods=126).mean()
    depth = (floor - nc).clip(lower=0) / (nc.abs() + floor + 1.0)
    b = freq + 0.5 * depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution x leverage compound distress, change over a half year (worsening squeeze)
def f35zs_f35_zombie_survivor_score_dilevcompound_base_v113_signal(sharesbas, debt, equity):
    dil = np.tanh(8.0 * _f35_dilution(sharesbas, 252).clip(lower=0))
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    comp = dil * lev
    b = comp - comp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor composite vs its half-year median (survivability regime shift)
def f35zs_f35_zombie_survivor_score_survregime_base_v114_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    med = surv.rolling(126, min_periods=63).median()
    b = (surv - med) / (surv.abs() + med.abs() + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-funded-by-debt: debt growth covering operating burn (debt-financed zombie)
def f35zs_f35_zombie_survivor_score_debtfundburn_base_v115_signal(debt, opex, ncfo):
    dchg = (debt - debt.shift(63)).clip(lower=0)
    burn = _f35_burn(opex, ncfo)
    b = np.tanh(dchg / (burn + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival score weighted by self-funding momentum (improving operations)
def f35zs_f35_zombie_survivor_score_survopmom_base_v116_signal(cashneq, debt, ncfo, opex):
    cov = np.tanh(_f35_cash_cov_debt(cashneq, debt) / 2.0)
    sf = _f35_self_fund(ncfo, opex)
    sf_mom = (sf - sf.shift(126)).clip(-1, 1)
    b = cov + sf_mom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie distance: full safe-state distance combining all six columns, ranked
def f35zs_f35_zombie_survivor_score_fulldist_base_v117_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil_s = 1.0 - np.tanh(5.0 * _f35_dilution(sharesbas, 252).clip(lower=0))
    lev_s = 1.0 - np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    eq_s = (equity > 0).astype(float)
    dist = (run_s ** 2 + dil_s ** 2 + lev_s ** 2 + eq_s ** 2) ** 0.5
    b = _rank(dist, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash depletion velocity: log cash change over a quarter (runway burn-down)
def f35zs_f35_zombie_survivor_score_cashvel_base_v118_signal(cashneq):
    lc = np.log(cashneq.clip(lower=1.0))
    b = lc - lc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-adjusted burn coverage: net cash over (debt + burn), ranked
def f35zs_f35_zombie_survivor_score_levburncov_base_v119_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    cov = cashneq / (debt + burn * 4.0).replace(0, np.nan)
    b = _rank(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor minus distress count (continuous survival net of flag tally)
def f35zs_f35_zombie_survivor_score_survnetflags_base_v120_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    f_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    f_dil = (_f35_dilution(sharesbas, 252) > 0.05).astype(float)
    f_lev = (_f35_leverage(debt, equity) > 1.0).astype(float)
    tally = (f_burn + f_dil + f_lev).rolling(63, min_periods=21).mean()
    b = surv - 0.2 * tally
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution velocity z (how fast shares are growing vs own history)
def f35zs_f35_zombie_survivor_score_dilvelz_base_v121_signal(sharesbas):
    vel = _f35_dilution(sharesbas, 21)
    b = _z(vel, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivability convexity: tophug of survivor range position (near safe vs near zombie)
def f35zs_f35_zombie_survivor_score_survconvex_base_v122_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    hi = _rmax(surv, 252)
    lo = _rmin(surv, 252)
    pos = (surv - lo) / (hi - lo).replace(0, np.nan)
    b = np.sign(pos - 0.5) * (pos - 0.5) ** 2 * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-to-equity drain: annual burn vs book equity (years of equity left)
def f35zs_f35_zombie_survivor_score_burneqdrain_base_v123_signal(opex, ncfo, equity):
    burn = _f35_burn(opex, ncfo)
    b = np.tanh((burn * 4.0) / equity.clip(lower=1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite survival rank slope (survivability percentile trend over a quarter)
def f35zs_f35_zombie_survivor_score_survrankslope_base_v124_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    r = _rank(surv, 252)
    b = (r - r.shift(63)) / 63.0 * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-cycle position: debt vs its 504d range (build vs paydown phase)
def f35zs_f35_zombie_survivor_score_debtcyclepos_base_v125_signal(debt, cashneq):
    hi = _rmax(debt, 504)
    lo = _rmin(debt, 504)
    pos = (debt - lo) / (hi - lo).replace(0, np.nan)
    cash_w = np.tanh(cashneq / debt.replace(0, np.nan) / 2.0)
    b = pos * (1.0 - 0.5 * cash_w)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvent-survivability momentum: change in equity-gated survivor over a quarter
def f35zs_f35_zombie_survivor_score_solventsurvrank_base_v126_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    eq_w = np.tanh(equity / cashneq.replace(0, np.nan))
    raw = surv * (0.5 + 0.5 * (eq_w + 1.0) / 2.0)
    b = raw - raw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-vs-solvency rank divergence: runway rank minus leverage rank
def f35zs_f35_zombie_survivor_score_runminuslev_base_v127_signal(cashneq, opex, ncfo, debt, equity):
    run = _f35_runway(cashneq, opex, ncfo)
    lev = _f35_leverage(debt, equity)
    b = _rank(run, 252) - _rank(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak entries: count of dilution-onset events over a year (raise frequency)
def f35zs_f35_zombie_survivor_score_dilonsets_base_v128_signal(sharesbas):
    fast = _f35_dilution(sharesbas, 21)
    diluting = (fast > 0.02).astype(float)
    onsets = ((diluting == 1) & (diluting.shift(1) == 0)).astype(float)
    rate = onsets.rolling(252, min_periods=126).sum()
    depth = fast.clip(lower=0).rolling(63, min_periods=21).mean() * 20.0
    b = rate + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival index momentum over half a year (survivability trajectory)
def f35zs_f35_zombie_survivor_score_survindexmom_base_v129_signal(cashneq, opex, ncfo, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    nc = _f35_netcash(cashneq, debt)
    lev_s = 1.0 / (1.0 + _f35_leverage(debt, equity).clip(lower=0))
    idx = 0.4 * run_s + 0.3 * nc + 0.3 * (2.0 * lev_s - 1.0)
    b = idx - idx.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-vs-financing gap proxy: burn relative to cash (internal-funding shortfall), z
def f35zs_f35_zombie_survivor_score_burnshortfall_base_v130_signal(opex, ncfo, cashneq):
    short = (opex - ncfo) / cashneq.replace(0, np.nan)
    b = _z(short, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash-to-opex coverage (debt-adjusted months of opex headroom)
def f35zs_f35_zombie_survivor_score_netcashopex_base_v131_signal(cashneq, debt, opex):
    b = np.tanh((cashneq - debt) / opex.replace(0, np.nan) / 4.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor composite cross-window agreement (126d vs 504d survivor, signed)
def f35zs_f35_zombie_survivor_score_survagree_base_v132_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    s_short = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 126)
    s_long = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 504)
    b = (s_short - s_long) / (s_short + s_long).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage volatility (debt-cycle instability through the commodity cycle)
def f35zs_f35_zombie_survivor_score_levvol_base_v133_signal(debt, equity):
    lev = _f35_leverage(debt, equity)
    b = _std(lev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-burn-quarter tally over 2yr (count of operating-burn quarters)
def f35zs_f35_zombie_survivor_score_burnqtrtally_base_v134_signal(opex, ncfo):
    burning = (_f35_burn(opex, ncfo) > 0).astype(float)
    b = burning.rolling(504, min_periods=252).mean()
    depth = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = (b + 0.3 * depth).replace([np.inf, -np.inf], np.nan)
    return result


# survivor composite tanh-momentum (bounded change in survivability)
def f35zs_f35_zombie_survivor_score_survtanhmom_base_v135_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    chg = surv - surv.shift(21)
    b = np.tanh(15.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-erosion-funded-by-debt: leverage rising while equity falling (squeeze), ranked
def f35zs_f35_zombie_survivor_score_squeezerank_base_v136_signal(debt, equity, cashneq):
    lev_rise = (_f35_leverage(debt, equity) - _f35_leverage(debt, equity).shift(126))
    eq_fall = -(equity - equity.shift(126)) / equity.shift(126).abs().replace(0, np.nan)
    raw = lev_rise.clip(lower=0) * eq_fall.clip(lower=0)
    b = _rank(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway resilience: fraction of last year runway stayed above one year of cash
def f35zs_f35_zombie_survivor_score_runwayresil_base_v137_signal(cashneq, opex, ncfo):
    runway = _f35_runway(cashneq, opex, ncfo)
    safe = (runway > 4.0).astype(float)
    frac = safe.rolling(252, min_periods=126).mean()
    cushion = np.tanh((runway - 4.0) / 8.0).rolling(63, min_periods=21).mean()
    b = frac + 0.3 * cushion
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie pressure year-over-year change (distress vs prior year)
def f35zs_f35_zombie_survivor_score_pressyoy_base_v138_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    burn_int = (_f35_burn(opex, ncfo) / opex.replace(0, np.nan)).clip(0, 2)
    dil = _f35_dilution(sharesbas, 252).clip(lower=0)
    lev = np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    press = burn_int + 3.0 * dil + lev
    b = press - press.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage-of-total-obligations rank (cash vs debt+annual burn percentile)
def f35zs_f35_zombie_survivor_score_obligcovrank_base_v139_signal(cashneq, debt, opex, ncfo):
    burn = _f35_burn(opex, ncfo)
    cov = cashneq / (debt + burn * 4.0).replace(0, np.nan)
    b = _rank(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivor composite EMA crossover (fast vs slow survivability)
def f35zs_f35_zombie_survivor_score_survcross_base_v140_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    fast = surv.ewm(span=42, min_periods=21).mean()
    slow = surv.ewm(span=126, min_periods=42).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown-vs-dilution: are they deleveraging by diluting? (financing mix proxy)
def f35zs_f35_zombie_survivor_score_delevbydil_base_v141_signal(debt, sharesbas):
    dlev = -(debt - debt.shift(126)) / debt.shift(126).replace(0, np.nan)
    dil = _f35_dilution(sharesbas, 126)
    b = np.tanh(dlev.clip(lower=0) * 5.0) * np.tanh(dil.clip(lower=0) * 8.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash drawup from trough: recovery in cash off its 504d low (refinancing recovery)
def f35zs_f35_zombie_survivor_score_cashrecov_base_v142_signal(cashneq):
    lo = _rmin(cashneq, 504)
    b = np.tanh(cashneq / lo.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie-flag tally slope (rate of distress accumulation, count-friendly)
def f35zs_f35_zombie_survivor_score_flagslope_base_v143_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    f_burn = (_f35_burn(opex, ncfo) > 0).astype(float)
    f_dil = (_f35_dilution(sharesbas, 252) > 0.10).astype(float)
    f_lev = (_f35_leverage(debt, equity) > 1.5).astype(float)
    f_run = (_f35_runway(cashneq, opex, ncfo) < 4.0).astype(float)
    tally = (f_burn + f_dil + f_lev + f_run).rolling(63, min_periods=21).mean()
    b = tally - tally.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival buffer per share (net cash plus equity cushion per diluted share), z
def f35zs_f35_zombie_survivor_score_bufpershare_base_v144_signal(cashneq, debt, equity, sharesbas):
    cushion = cashneq - debt + equity.clip(lower=0)
    cps = cushion / sharesbas.replace(0, np.nan)
    b = _z(cps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net burn vs financing-need proxy: burn relative to net cash, year-over-year shift
def f35zs_f35_zombie_survivor_score_burnneedyoy_base_v145_signal(opex, ncfo, cashneq, debt):
    burn = _f35_burn(opex, ncfo)
    need = np.log1p((burn * 4.0) / (cashneq - debt).clip(lower=1.0))
    b = need - need.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite distress vs survivor cross-sectional balance over a year (count-friendly)
def f35zs_f35_zombie_survivor_score_distresstime_base_v146_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    zombie = (surv < surv.rolling(252, min_periods=126).median()).astype(float)
    grp = (zombie == 0).cumsum()
    streak = zombie.groupby(grp).cumsum()
    b = streak / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway-weighted dilution penalty (dilution hurts more when runway short), ranked
def f35zs_f35_zombie_survivor_score_dilrunpen_base_v147_signal(sharesbas, cashneq, opex, ncfo):
    dil = _f35_dilution(sharesbas, 126).clip(lower=0)
    inv_run = 1.0 / (1.0 + _f35_runway(cashneq, opex, ncfo).clip(lower=0))
    raw = dil * inv_run
    b = _rank(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency-adjusted survivor momentum (signed sqrt of net-cash-gated survivor change)
def f35zs_f35_zombie_survivor_score_solvsurv_base_v148_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    surv = _f35_survivor(cashneq, opex, ncfo, sharesbas, debt, equity, 252)
    nc = _f35_netcash(cashneq, debt)
    adj = surv * (1.0 + nc) / 2.0
    chg = adj - adj.shift(126)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn acceleration z (how fast burn intensity is changing, vs own history)
def f35zs_f35_zombie_survivor_score_burnaccelz_base_v149_signal(opex, ncfo):
    burn_int = _f35_burn(opex, ncfo) / opex.replace(0, np.nan)
    acc = burn_int - burn_int.shift(63)
    b = _z(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# master survival score: blended runway, dilution, leverage, solvency composite, ranked
def f35zs_f35_zombie_survivor_score_masterscore_base_v150_signal(cashneq, opex, ncfo, sharesbas, debt, equity):
    run_s = np.tanh(_f35_runway(cashneq, opex, ncfo) / 8.0)
    dil_s = 1.0 - np.tanh(6.0 * _f35_dilution(sharesbas, 252).clip(lower=0))
    lev_s = 1.0 - np.tanh(_f35_leverage(debt, equity).clip(lower=0))
    nc = (_f35_netcash(cashneq, debt) + 1.0) / 2.0
    score = 0.3 * run_s + 0.25 * dil_s + 0.25 * lev_s + 0.2 * nc
    b = _rank(score, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35zs_f35_zombie_survivor_score_survpctile_252d_base_v076_signal,
    f35zs_f35_zombie_survivor_score_presssm_126d_base_v077_signal,
    f35zs_f35_zombie_survivor_score_gravepctile_base_v078_signal,
    f35zs_f35_zombie_survivor_score_runwayyears_base_v079_signal,
    f35zs_f35_zombie_survivor_score_burnvol_126d_base_v080_signal,
    f35zs_f35_zombie_survivor_score_netcashz_base_v081_signal,
    f35zs_f35_zombie_survivor_score_levpctile_base_v082_signal,
    f35zs_f35_zombie_survivor_score_cumdil_504d_base_v083_signal,
    f35zs_f35_zombie_survivor_score_forcedraise_base_v084_signal,
    f35zs_f35_zombie_survivor_score_survscorerank_base_v085_signal,
    f35zs_f35_zombie_survivor_score_zombietenure_base_v086_signal,
    f35zs_f35_zombie_survivor_score_bufftrend_126d_base_v087_signal,
    f35zs_f35_zombie_survivor_score_bvps_trend_base_v088_signal,
    f35zs_f35_zombie_survivor_score_selffundgap_base_v089_signal,
    f35zs_f35_zombie_survivor_score_triadsm_126d_base_v090_signal,
    f35zs_f35_zombie_survivor_score_covmom_63d_base_v091_signal,
    f35zs_f35_zombie_survivor_score_levdilrank_base_v092_signal,
    f35zs_f35_zombie_survivor_score_runwaymin_252d_base_v093_signal,
    f35zs_f35_zombie_survivor_score_netdrain_base_v094_signal,
    f35zs_f35_zombie_survivor_score_survlevdisp_base_v095_signal,
    f35zs_f35_zombie_survivor_score_cumburn_252d_base_v096_signal,
    f35zs_f35_zombie_survivor_score_dilaccelsm_base_v097_signal,
    f35zs_f35_zombie_survivor_score_survindex_base_v098_signal,
    f35zs_f35_zombie_survivor_score_burnintz_base_v099_signal,
    f35zs_f35_zombie_survivor_score_debtcashrank_base_v100_signal,
    f35zs_f35_zombie_survivor_score_survaccel_base_v101_signal,
    f35zs_f35_zombie_survivor_score_eqdebtrank_base_v102_signal,
    f35zs_f35_zombie_survivor_score_dilsurv_base_v103_signal,
    f35zs_f35_zombie_survivor_score_survstability_base_v104_signal,
    f35zs_f35_zombie_survivor_score_pressz_base_v105_signal,
    f35zs_f35_zombie_survivor_score_cashadeqdil_base_v106_signal,
    f35zs_f35_zombie_survivor_score_levequdiv_base_v107_signal,
    f35zs_f35_zombie_survivor_score_survdd_252d_base_v108_signal,
    f35zs_f35_zombie_survivor_score_cpsz_base_v109_signal,
    f35zs_f35_zombie_survivor_score_gravetimer_base_v110_signal,
    f35zs_f35_zombie_survivor_score_ncfopostime_base_v111_signal,
    f35zs_f35_zombie_survivor_score_netcashfloor_base_v112_signal,
    f35zs_f35_zombie_survivor_score_dilevcompound_base_v113_signal,
    f35zs_f35_zombie_survivor_score_survregime_base_v114_signal,
    f35zs_f35_zombie_survivor_score_debtfundburn_base_v115_signal,
    f35zs_f35_zombie_survivor_score_survopmom_base_v116_signal,
    f35zs_f35_zombie_survivor_score_fulldist_base_v117_signal,
    f35zs_f35_zombie_survivor_score_cashvel_base_v118_signal,
    f35zs_f35_zombie_survivor_score_levburncov_base_v119_signal,
    f35zs_f35_zombie_survivor_score_survnetflags_base_v120_signal,
    f35zs_f35_zombie_survivor_score_dilvelz_base_v121_signal,
    f35zs_f35_zombie_survivor_score_survconvex_base_v122_signal,
    f35zs_f35_zombie_survivor_score_burneqdrain_base_v123_signal,
    f35zs_f35_zombie_survivor_score_survrankslope_base_v124_signal,
    f35zs_f35_zombie_survivor_score_debtcyclepos_base_v125_signal,
    f35zs_f35_zombie_survivor_score_solventsurvrank_base_v126_signal,
    f35zs_f35_zombie_survivor_score_runminuslev_base_v127_signal,
    f35zs_f35_zombie_survivor_score_dilonsets_base_v128_signal,
    f35zs_f35_zombie_survivor_score_survindexmom_base_v129_signal,
    f35zs_f35_zombie_survivor_score_burnshortfall_base_v130_signal,
    f35zs_f35_zombie_survivor_score_netcashopex_base_v131_signal,
    f35zs_f35_zombie_survivor_score_survagree_base_v132_signal,
    f35zs_f35_zombie_survivor_score_levvol_base_v133_signal,
    f35zs_f35_zombie_survivor_score_burnqtrtally_base_v134_signal,
    f35zs_f35_zombie_survivor_score_survtanhmom_base_v135_signal,
    f35zs_f35_zombie_survivor_score_squeezerank_base_v136_signal,
    f35zs_f35_zombie_survivor_score_runwayresil_base_v137_signal,
    f35zs_f35_zombie_survivor_score_pressyoy_base_v138_signal,
    f35zs_f35_zombie_survivor_score_obligcovrank_base_v139_signal,
    f35zs_f35_zombie_survivor_score_survcross_base_v140_signal,
    f35zs_f35_zombie_survivor_score_delevbydil_base_v141_signal,
    f35zs_f35_zombie_survivor_score_cashrecov_base_v142_signal,
    f35zs_f35_zombie_survivor_score_flagslope_base_v143_signal,
    f35zs_f35_zombie_survivor_score_bufpershare_base_v144_signal,
    f35zs_f35_zombie_survivor_score_burnneedyoy_base_v145_signal,
    f35zs_f35_zombie_survivor_score_distresstime_base_v146_signal,
    f35zs_f35_zombie_survivor_score_dilrunpen_base_v147_signal,
    f35zs_f35_zombie_survivor_score_solvsurv_base_v148_signal,
    f35zs_f35_zombie_survivor_score_burnaccelz_base_v149_signal,
    f35zs_f35_zombie_survivor_score_masterscore_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_ZOMBIE_SURVIVOR_SCORE_REGISTRY_076_150 = REGISTRY


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

    print("OK f35_zombie_survivor_score_base_076_150_claude: %d features pass" % n_features)
