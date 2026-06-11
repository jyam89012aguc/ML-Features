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


# ===== folder domain primitives (distress / going concern) =====
def _f21_x1(workingcapital, assets):
    return workingcapital / assets.replace(0, np.nan)


def _f21_x2(retearn, assets):
    return retearn / assets.replace(0, np.nan)


def _f21_x3(ebit, assets):
    return ebit / assets.replace(0, np.nan)


def _f21_x4(equity, liabilities):
    return equity / liabilities.replace(0, np.nan)


def _f21_x5(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    x1 = workingcapital / assets.replace(0, np.nan)
    x2 = retearn / assets.replace(0, np.nan)
    x3 = ebit / assets.replace(0, np.nan)
    x4 = equity / liabilities.replace(0, np.nan)
    x5 = revenue / assets.replace(0, np.nan)
    return 0.717 * x1 + 0.847 * x2 + 3.107 * x3 + 0.420 * x4 + 0.998 * x5


def _f21_zminer(workingcapital, retearn, ebit, equity, liabilities, assets):
    x1 = workingcapital / assets.replace(0, np.nan)
    x2 = retearn / assets.replace(0, np.nan)
    x3 = ebit / assets.replace(0, np.nan)
    x4 = equity / liabilities.replace(0, np.nan)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def _f21_weak(ratio, w, q):
    # going-concern weakness indicator: ratio in the bottom q-quantile of its own w-history
    thr = ratio.rolling(w, min_periods=max(1, w // 2)).quantile(q)
    return (ratio <= thr).astype(float)


def _f21_below_med(ratio, w):
    # shortfall depth below the ratio's own trailing-w median (>=0)
    med = ratio.rolling(w, min_periods=max(1, w // 2)).median()
    return (med - ratio).clip(lower=0)


# ============================================================
# --- ALTMAN-Z COMPONENT SECONDARY FORMS ---
# X1 smoothed level over a quarter (persistent liquidity buffer)
def f21dg_f21_distress_going_concern_x1sm_63d_base_v076_signal(workingcapital, assets):
    r = _f21_x1(workingcapital, assets)
    b = r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X2 (retearn/assets) z-scored vs 252d (accumulated-deficit regime)
def f21dg_f21_distress_going_concern_x2z_252d_base_v077_signal(retearn, assets):
    r = _f21_x2(retearn, assets)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X3 (ebit/assets) smoothed level over a quarter (persistent operating return)
def f21dg_f21_distress_going_concern_x3sm_63d_base_v078_signal(ebit, assets):
    r = _f21_x3(ebit, assets)
    b = r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X4 (equity/liabilities) percentile-rank vs 504d (solvency-cushion percentile)
def f21dg_f21_distress_going_concern_x4rank_504d_base_v079_signal(equity, liabilities):
    r = _f21_x4(equity, liabilities)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X5 (revenue/assets) z-scored vs 252d (asset-turnover distress regime)
def f21dg_f21_distress_going_concern_x5z_252d_base_v080_signal(revenue, assets):
    r = _f21_x5(revenue, assets)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- WEIGHTED-COMPONENT CONTRIBUTIONS TO Z ---
# X3 contribution to Altman Z (3.107*X3; operating-return weight in score)
def f21dg_f21_distress_going_concern_x3contrib_63d_base_v081_signal(ebit, assets):
    b = 3.107 * _f21_x3(ebit, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of Altman Z carried by the solvency term (X4 contribution / |Z|)
def f21dg_f21_distress_going_concern_x4share_63d_base_v082_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    x4c = 0.420 * _f21_x4(equity, liabilities)
    b = x4c / z.abs().replace(0, np.nan)
    b = b.clip(lower=-5.0, upper=5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of Altman Z carried by the deficit term (X2 contribution / |Z|)
def f21dg_f21_distress_going_concern_x2share_63d_base_v083_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    x2c = 0.847 * _f21_x2(retearn, assets)
    b = x2c / z.abs().replace(0, np.nan)
    b = b.clip(lower=-5.0, upper=5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MINER-Z VARIANTS ---
# miner-Z level smoothed over a half year (structural explorer distress)
def f21dg_f21_distress_going_concern_zminersm_126d_base_v084_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f21_zminer(workingcapital, retearn, ebit, equity, liabilities, assets)
    b = z.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# miner-Z percentile-rank vs 504d (explorer-distress percentile band)
def f21dg_f21_distress_going_concern_zminerrank_504d_base_v085_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f21_zminer(workingcapital, retearn, ebit, equity, liabilities, assets)
    b = _rank(z, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread: Altman Z' minus miner-Z (turnover-dependence of the distress score)
def f21dg_f21_distress_going_concern_zspread_63d_base_v086_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    za = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    zm = _f21_zminer(workingcapital, retearn, ebit, equity, liabilities, assets)
    b = _z(za, 252) - _z(zm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# miner-Z trend over a quarter (explorer-distress velocity, base form)
def f21dg_f21_distress_going_concern_zminertrend_63d_base_v087_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f21_zminer(workingcapital, retearn, ebit, equity, liabilities, assets)
    b = z - z.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SOLVENCY / LEVERAGE EXTENSIONS ---
# net debt over assets: (liabilities - cashneq) / assets (cash-adjusted gearing)
def f21dg_f21_distress_going_concern_netdebtassets_63d_base_v088_signal(liabilities, cashneq, assets):
    b = (liabilities - cashneq) / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt over equity: (liabilities - cashneq) / |equity| (cash-adjusted gearing on capital)
def f21dg_f21_distress_going_concern_netdebteq_63d_base_v089_signal(liabilities, cashneq, equity):
    b = (liabilities - cashneq) / equity.abs().replace(0, np.nan)
    b = b.clip(lower=-50.0, upper=50.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt/equity (cash-adjusted book gearing) percentile-rank vs 504d
def f21dg_f21_distress_going_concern_gearrank_504d_base_v090_signal(liabilities, cashneq, equity):
    g = ((liabilities - cashneq) / equity.abs().replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage (liabilities/assets) drawdown above its 252d trough (gearing run-up depth)
def f21dg_f21_distress_going_concern_levrunup_252d_base_v091_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    trough = _rmin(lev, 252)
    b = (lev - trough)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets min over a half year (worst recent solvency point)
def f21dg_f21_distress_going_concern_mineq_126d_base_v092_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    b = _rmin(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DETERIORATION STREAKS / DROPS (base-level) ---
# fraction of last year Altman Z fell quarter-over-quarter (deterioration prevalence)
def f21dg_f21_distress_going_concern_zdropfreq_252d_base_v093_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    drop = (z < z.shift(63)).astype(float)
    b = drop.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean magnitude of Altman Z quarterly declines over a year (chronic deterioration depth)
def f21dg_f21_distress_going_concern_zdeclmag_252d_base_v094_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    decl = (z.shift(63) - z).clip(lower=0)
    b = decl.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year equity/assets fell (solvency-erosion prevalence)
def f21dg_f21_distress_going_concern_eqdropfreq_252d_base_v095_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    drop = (r < r.shift(63)).astype(float)
    b = drop.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year leverage rose (gearing-build prevalence)
def f21dg_f21_distress_going_concern_levrisefreq_252d_base_v096_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    rise = (lev > lev.shift(63)).astype(float)
    b = rise.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GOING-CONCERN COMPOSITE EXTENSIONS ---
# magnitude going-concern score: -X1 -X2 -X3 -X4 -X5 (higher = worse), z-scored
def f21dg_f21_distress_going_concern_gcmagz_252d_base_v097_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = -_z(z, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# going-concern severity weighted by leverage: distress-zone depth x gearing
def f21dg_f21_distress_going_concern_gcXlev_63d_base_v098_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    zonedepth = (1.1 - z).clip(lower=0)
    lev = liabilities / assets.replace(0, np.nan)
    b = zonedepth * lev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite of weak channels measured vs revenue (going-concern severity, sales-scaled)
def f21dg_f21_distress_going_concern_gcrevcomposite_base_v099_signal(equity, retearn, ebit, workingcapital, revenue):
    f1 = _f21_weak(equity / revenue.replace(0, np.nan), 504, 0.25)
    f2 = _f21_weak(retearn / revenue.replace(0, np.nan), 504, 0.25)
    f3 = _f21_weak(ebit / revenue.replace(0, np.nan), 504, 0.25)
    f4 = _f21_weak(workingcapital / revenue.replace(0, np.nan), 504, 0.25)
    jitter = pd.concat([_z(ebit / revenue.replace(0, np.nan), 126),
                        _z(equity / revenue.replace(0, np.nan), 126)], axis=1).std(axis=1)
    b = f1 + f2 + f3 + f4 + jitter
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# going-concern deterioration: rise in weak-channel prevalence over a half year (worsening breadth)
def f21dg_f21_distress_going_concern_gcdetchg_63d_base_v100_signal(equity, retearn, ebit, workingcapital, assets):
    cnt = (_f21_weak(equity / assets.replace(0, np.nan), 504, 0.30)
           + _f21_weak(retearn / assets.replace(0, np.nan), 504, 0.30)
           + _f21_weak(ebit / assets.replace(0, np.nan), 504, 0.30)
           + _f21_weak(workingcapital / assets.replace(0, np.nan), 504, 0.30))
    prev = cnt.rolling(63, min_periods=21).mean()
    b = prev - prev.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DISTRESS-QUARTER TALLIES (count-friendly, alt definitions) ---
# fraction of last year in miner-Z distress zone (explorer chronic-distress time)
def f21dg_f21_distress_going_concern_zminertime_252d_base_v101_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f21_zminer(workingcapital, retearn, ebit, equity, liabilities, assets)
    thr = z.rolling(504, min_periods=252).quantile(0.25)
    indistress = (z <= thr).astype(float)
    frac = indistress.rolling(252, min_periods=126).mean()
    depth = (thr - z).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 0.5 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distress-onset tally on miner-Z (fresh entries into weak zone over last year)
def f21dg_f21_distress_going_concern_zmineronset_252d_base_v102_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f21_zminer(workingcapital, retearn, ebit, equity, liabilities, assets)
    thr = z.rolling(504, min_periods=252).quantile(0.25)
    indistress = (z <= thr).astype(float)
    entries = ((indistress == 1) & (indistress.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 0.3 * indistress.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# severe-distress time: fraction of last year Altman Z below its 10th-percentile (acute distress)
def f21dg_f21_distress_going_concern_severetime_252d_base_v103_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    thr = z.rolling(504, min_periods=252).quantile(0.10)
    severe = (z <= thr).astype(float)
    frac = severe.rolling(252, min_periods=126).mean()
    depth = (thr - z).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 2.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of leverage-spike entries over last year (debt-distress onset tally)
def f21dg_f21_distress_going_concern_levspikeonset_252d_base_v104_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    thr = lev.rolling(504, min_periods=252).quantile(0.80)
    high = (lev >= thr).astype(float)
    entries = ((high == 1) & (high.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 0.3 * high.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SOLVENCY / DEFICIT INTERACTIONS ---
# capital-erosion x leverage: equity-erosion below 252d peak scaled by gearing
def f21dg_f21_distress_going_concern_eqerosXlev_63d_base_v105_signal(equity, assets, liabilities):
    r = equity / assets.replace(0, np.nan)
    erosion = (_rmax(r, 252) - r).clip(lower=0)
    lev = liabilities / assets.replace(0, np.nan)
    b = erosion * lev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deficit-x-illiquidity: retearn-erosion x working-capital-shortfall (compounding distress)
def f21dg_f21_distress_going_concern_defXilliq_63d_base_v106_signal(retearn, workingcapital, assets):
    defero = _f21_below_med(retearn / assets.replace(0, np.nan), 252)
    illiq = _f21_below_med(workingcapital / assets.replace(0, np.nan), 252)
    b = 50.0 * defero * illiq
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-loss x leverage: EBIT-return shortfall scaled by gearing (levered loss-maker)
def f21dg_f21_distress_going_concern_lossXlev_63d_base_v107_signal(ebit, assets, liabilities):
    loss = _f21_below_med(_f21_x3(ebit, assets), 252)
    lev = liabilities / assets.replace(0, np.nan)
    b = loss * lev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- REVENUE / OPERATING DISTRESS ---
# revenue drawdown from its 252d peak (sales collapse, distress for producers)
def f21dg_f21_distress_going_concern_revdd_252d_base_v108_signal(revenue):
    peak = _rmax(revenue, 252)
    b = revenue / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT margin (ebit/revenue) percentile-rank vs 504d (operating-distress percentile)
def f21dg_f21_distress_going_concern_ebitmarginrank_504d_base_v109_signal(ebit, revenue):
    m = ebit / revenue.replace(0, np.nan)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue coverage of liabilities z-scored vs 252d (sales-backed solvency regime)
def f21dg_f21_distress_going_concern_revcoverz_252d_base_v110_signal(revenue, liabilities):
    r = revenue / liabilities.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT margin trend over a year (operating-margin deterioration, base form)
def f21dg_f21_distress_going_concern_ebitmargintrend_252d_base_v111_signal(ebit, revenue):
    m = ebit / revenue.replace(0, np.nan)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CASH-BACKED DISTRESS ---
# cash/liabilities trend over a quarter (cash-cover deterioration, base form)
def f21dg_f21_distress_going_concern_cashcovertrend_63d_base_v112_signal(cashneq, liabilities):
    c = cashneq / liabilities.replace(0, np.nan)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets drawdown from 252d peak (treasury-share erosion)
def f21dg_f21_distress_going_concern_cashassetsdd_252d_base_v113_signal(cashneq, assets):
    r = cashneq / assets.replace(0, np.nan)
    peak = _rmax(r, 252)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash vs current obligations proxy: cashneq / (liabilities - workingcapital), bounded
def f21dg_f21_distress_going_concern_cashvsoblig_63d_base_v114_signal(cashneq, liabilities, workingcapital):
    oblig = (liabilities - workingcapital).clip(lower=1.0)
    b = (cashneq / oblig).clip(upper=20.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash-solvency percentile-rank vs 504d (cash-adjusted solvency percentile)
def f21dg_f21_distress_going_concern_netcashrank_504d_base_v115_signal(cashneq, liabilities, assets):
    r = (cashneq - liabilities) / assets.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Z VOLATILITY / DISPERSION EXTENSIONS ---
# Altman Z coefficient-of-variation over a year (distress-score instability)
def f21dg_f21_distress_going_concern_zcv_252d_base_v116_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    m = _mean(z, 252)
    sd = _std(z, 252)
    b = sd / m.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage volatility over a year (erratic vs steady gearing)
def f21dg_f21_distress_going_concern_levvol_252d_base_v117_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    b = lev.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X3 (ebit/assets) volatility over a year (operating-return instability)
def f21dg_f21_distress_going_concern_x3vol_252d_base_v118_signal(ebit, assets):
    r = _f21_x3(ebit, assets)
    b = r.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TERM STRUCTURE / DISPLACEMENT ---
# Altman Z displacement from its slow EMA over a half year (acute vs chronic distress)
def f21dg_f21_distress_going_concern_zdispema_126d_base_v119_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = z - z.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency (equity/assets) short-vs-long term spread (recent vs structural solvency)
def f21dg_f21_distress_going_concern_eqtermspr_base_v120_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage short-vs-long term spread (recent vs structural gearing)
def f21dg_f21_distress_going_concern_levtermspr_base_v121_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    short = lev.rolling(63, min_periods=21).mean()
    long = lev.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIGN x MAGNITUDE / COMPRESSED ---
# signed-root of EBIT margin (ebit/revenue) (compressed operating-margin distress)
def f21dg_f21_distress_going_concern_x3root_63d_base_v122_signal(ebit, revenue):
    r = ebit / revenue.replace(0, np.nan)
    b = np.sign(r) * (r.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash coverage of liabilities z-scored vs 252d ((cash - liab)/liab solvency regime)
def f21dg_f21_distress_going_concern_netcashsignlog_63d_base_v123_signal(cashneq, liabilities):
    r = (cashneq - liabilities) / liabilities.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed accumulated-deficit pressure (bounded retearn-erosion vs assets)
def f21dg_f21_distress_going_concern_deftanh_63d_base_v124_signal(retearn, assets):
    erosion = _f21_below_med(retearn / assets.replace(0, np.nan), 252)
    b = np.tanh(20.0 * erosion)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DOUBLE-RATIO DISTRESS / EFFICIENCY ---
# EBIT / equity (return on book capital; negative or thin = distress)
def f21dg_f21_distress_going_concern_ebiteq_63d_base_v125_signal(ebit, equity):
    b = (ebit / equity.abs().replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings / equity (deficit share of capital base)
def f21dg_f21_distress_going_concern_reeq_63d_base_v126_signal(retearn, equity):
    b = (retearn / equity.abs().replace(0, np.nan)).clip(lower=-20.0, upper=20.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / current-obligations proxy: wc / (liabilities - workingcapital)
def f21dg_f21_distress_going_concern_wcoblig_63d_base_v127_signal(workingcapital, liabilities):
    oblig = (liabilities - workingcapital).clip(lower=1.0)
    b = (workingcapital / oblig).clip(lower=-5.0, upper=5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / equity (capital productivity; collapse = distress)
def f21dg_f21_distress_going_concern_reveq_63d_base_v128_signal(revenue, equity):
    b = (revenue / equity.abs().replace(0, np.nan)).clip(upper=50.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MIN / WORST-CASE EXTENSIONS ---
# worst Altman Z over last year (deepest distress in the cycle)
def f21dg_f21_distress_going_concern_minz_252d_base_v129_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _rmin(z, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X4 (equity/liabilities) min over a half year (worst recent solvency cushion)
def f21dg_f21_distress_going_concern_minx4_126d_base_v130_signal(equity, liabilities):
    r = _f21_x4(equity, liabilities)
    b = _rmin(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max leverage over last year (peak gearing stress in the cycle)
def f21dg_f21_distress_going_concern_maxlev_252d_base_v131_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    b = _rmax(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- YOY / LONG-HORIZON DISTRESS SHIFTS ---
# equity/assets year-over-year change (annual solvency shift)
def f21dg_f21_distress_going_concern_eqyoy_252d_base_v132_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage year-over-year change (annual gearing shift)
def f21dg_f21_distress_going_concern_levyoy_252d_base_v133_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    b = lev - lev.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/assets year-over-year change (annual operating-return shift)
def f21dg_f21_distress_going_concern_x3yoy_252d_base_v134_signal(ebit, assets):
    r = _f21_x3(ebit, assets)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RANK / Z OF SECONDARY DISTRESS RATIOS ---
# net-debt/assets z-scored vs 252d (cash-adjusted gearing regime)
def f21dg_f21_distress_going_concern_netdebtz_252d_base_v135_signal(liabilities, cashneq, assets):
    r = (liabilities - cashneq) / assets.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/equity percentile-rank vs 504d (return-on-capital distress percentile)
def f21dg_f21_distress_going_concern_ebiteqrank_504d_base_v136_signal(ebit, equity):
    r = (ebit / equity.abs().replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulated-deficit (retearn/equity) percentile-rank vs 504d
def f21dg_f21_distress_going_concern_reeqrank_504d_base_v137_signal(retearn, equity):
    r = (retearn / equity.abs().replace(0, np.nan)).clip(lower=-20.0, upper=20.0)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMPOSITE DISTANCE / SURVIVAL EXTENSIONS ---
# survival buffer: equity/assets + cash/assets - leverage (net balance-sheet strength)
def f21dg_f21_distress_going_concern_survbuffer_63d_base_v138_signal(equity, cashneq, liabilities, assets):
    eqa = equity / assets.replace(0, np.nan)
    casha = cashneq / assets.replace(0, np.nan)
    lev = liabilities / assets.replace(0, np.nan)
    b = (eqa + casha - lev).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distress distance: weak-component count + leverage rank - solvency rank (composite)
def f21dg_f21_distress_going_concern_distdistance_base_v139_signal(equity, retearn, ebit, workingcapital, liabilities, assets):
    cnt = (_f21_weak(equity / assets.replace(0, np.nan), 252, 0.25)
           + _f21_weak(retearn / assets.replace(0, np.nan), 252, 0.25)
           + _f21_weak(ebit / assets.replace(0, np.nan), 252, 0.25)
           + _f21_weak(workingcapital / assets.replace(0, np.nan), 252, 0.25))
    levrank = _rank(liabilities / assets.replace(0, np.nan), 252)
    solvrank = _rank(equity / assets.replace(0, np.nan), 252)
    b = cnt + levrank - solvrank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie-distress score: chronic operating losses + chronic deficit + high gearing (composite)
def f21dg_f21_distress_going_concern_zombiescore_base_v140_signal(ebit, retearn, liabilities, assets):
    oploss_t = _f21_weak(_f21_x3(ebit, assets), 504, 0.30).rolling(252, min_periods=126).mean()
    deficit_t = _f21_weak(_f21_x2(retearn, assets), 504, 0.30).rolling(252, min_periods=126).mean()
    lev = (liabilities / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = oploss_t + deficit_t + lev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ALTMAN-Z RECOVERY / OFF-TROUGH ---
# Altman Z recovery off its 252d trough (distress-score rebound)
def f21dg_f21_distress_going_concern_zrecov_252d_base_v141_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    trough = _rmin(z, 252)
    b = z - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets recovery off its 252d trough (solvency rebound)
def f21dg_f21_distress_going_concern_eqrecov_252d_base_v142_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    trough = _rmin(r, 252)
    b = r - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TIME-IN-ZONE / FILTERED SEVERITY ---
# fraction of last year equity/assets sat below zero-cushion threshold (5th pct) — near-insolvency time
def f21dg_f21_distress_going_concern_nearinsolvtime_252d_base_v143_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    thr = r.rolling(504, min_periods=252).quantile(0.05)
    near = (r <= thr).astype(float)
    frac = near.rolling(252, min_periods=126).mean()
    depth = (thr - r).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 3.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted distress severity: sum of below-median shortfalls across four channels
def f21dg_f21_distress_going_concern_shortfallsum_63d_base_v144_signal(equity, retearn, ebit, workingcapital, assets):
    s = (_f21_below_med(equity / assets.replace(0, np.nan), 252)
         + _f21_below_med(retearn / assets.replace(0, np.nan), 252)
         + _f21_below_med(ebit / assets.replace(0, np.nan), 252)
         + _f21_below_med(workingcapital / assets.replace(0, np.nan), 252))
    b = s.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FINAL DISTRESS FORMS ---
# Altman Z curvature: level minus average of its lead/lag (concavity of distress path, base)
def f21dg_f21_distress_going_concern_zcurv_63d_base_v145_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = z - 0.5 * (z.shift(63) + z.shift(-63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency-cushion (X4) curvature over a quarter (concavity of the cushion path, base)
def f21dg_f21_distress_going_concern_x4curv_63d_base_v146_signal(equity, liabilities):
    r = _f21_x4(equity, liabilities)
    b = r - 0.5 * (r.shift(63) + r.shift(-63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distress-zone width: dispersion of Altman Z across short/medium/long smoothings
def f21dg_f21_distress_going_concern_zwidth_base_v147_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    a = z.rolling(63, min_periods=21).mean()
    b2 = z.rolling(126, min_periods=63).mean()
    c = z.rolling(252, min_periods=126).mean()
    b = pd.concat([a, b2, c], axis=1).max(axis=1) - pd.concat([a, b2, c], axis=1).min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-runway-vs-liabilities distress: cash/assets minus deficit drag (net cash survival)
def f21dg_f21_distress_going_concern_cashsurv_63d_base_v148_signal(cashneq, retearn, assets):
    casha = cashneq / assets.replace(0, np.nan)
    defdrag = _f21_below_med(retearn / assets.replace(0, np.nan), 252)
    b = casha - 5.0 * defdrag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cushion: EBIT/liabilities z-scored vs 252d (operating cover of obligations regime)
def f21dg_f21_distress_going_concern_ebitliabz_252d_base_v149_signal(ebit, liabilities):
    r = ebit / liabilities.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overall going-concern composite: -z(altmanZ) + z(leverage) + deficit-time (multi-facet distress)
def f21dg_f21_distress_going_concern_gcoverall_base_v150_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    lev = liabilities / assets.replace(0, np.nan)
    deftime = _f21_weak(retearn / assets.replace(0, np.nan), 504, 0.30).rolling(126, min_periods=63).mean()
    b = -_z(z, 252) + _z(lev, 252) + deftime
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21dg_f21_distress_going_concern_x1sm_63d_base_v076_signal,
    f21dg_f21_distress_going_concern_x2z_252d_base_v077_signal,
    f21dg_f21_distress_going_concern_x3sm_63d_base_v078_signal,
    f21dg_f21_distress_going_concern_x4rank_504d_base_v079_signal,
    f21dg_f21_distress_going_concern_x5z_252d_base_v080_signal,
    f21dg_f21_distress_going_concern_x3contrib_63d_base_v081_signal,
    f21dg_f21_distress_going_concern_x4share_63d_base_v082_signal,
    f21dg_f21_distress_going_concern_x2share_63d_base_v083_signal,
    f21dg_f21_distress_going_concern_zminersm_126d_base_v084_signal,
    f21dg_f21_distress_going_concern_zminerrank_504d_base_v085_signal,
    f21dg_f21_distress_going_concern_zspread_63d_base_v086_signal,
    f21dg_f21_distress_going_concern_zminertrend_63d_base_v087_signal,
    f21dg_f21_distress_going_concern_netdebtassets_63d_base_v088_signal,
    f21dg_f21_distress_going_concern_netdebteq_63d_base_v089_signal,
    f21dg_f21_distress_going_concern_gearrank_504d_base_v090_signal,
    f21dg_f21_distress_going_concern_levrunup_252d_base_v091_signal,
    f21dg_f21_distress_going_concern_mineq_126d_base_v092_signal,
    f21dg_f21_distress_going_concern_zdropfreq_252d_base_v093_signal,
    f21dg_f21_distress_going_concern_zdeclmag_252d_base_v094_signal,
    f21dg_f21_distress_going_concern_eqdropfreq_252d_base_v095_signal,
    f21dg_f21_distress_going_concern_levrisefreq_252d_base_v096_signal,
    f21dg_f21_distress_going_concern_gcmagz_252d_base_v097_signal,
    f21dg_f21_distress_going_concern_gcXlev_63d_base_v098_signal,
    f21dg_f21_distress_going_concern_gcrevcomposite_base_v099_signal,
    f21dg_f21_distress_going_concern_gcdetchg_63d_base_v100_signal,
    f21dg_f21_distress_going_concern_zminertime_252d_base_v101_signal,
    f21dg_f21_distress_going_concern_zmineronset_252d_base_v102_signal,
    f21dg_f21_distress_going_concern_severetime_252d_base_v103_signal,
    f21dg_f21_distress_going_concern_levspikeonset_252d_base_v104_signal,
    f21dg_f21_distress_going_concern_eqerosXlev_63d_base_v105_signal,
    f21dg_f21_distress_going_concern_defXilliq_63d_base_v106_signal,
    f21dg_f21_distress_going_concern_lossXlev_63d_base_v107_signal,
    f21dg_f21_distress_going_concern_revdd_252d_base_v108_signal,
    f21dg_f21_distress_going_concern_ebitmarginrank_504d_base_v109_signal,
    f21dg_f21_distress_going_concern_revcoverz_252d_base_v110_signal,
    f21dg_f21_distress_going_concern_ebitmargintrend_252d_base_v111_signal,
    f21dg_f21_distress_going_concern_cashcovertrend_63d_base_v112_signal,
    f21dg_f21_distress_going_concern_cashassetsdd_252d_base_v113_signal,
    f21dg_f21_distress_going_concern_cashvsoblig_63d_base_v114_signal,
    f21dg_f21_distress_going_concern_netcashrank_504d_base_v115_signal,
    f21dg_f21_distress_going_concern_zcv_252d_base_v116_signal,
    f21dg_f21_distress_going_concern_levvol_252d_base_v117_signal,
    f21dg_f21_distress_going_concern_x3vol_252d_base_v118_signal,
    f21dg_f21_distress_going_concern_zdispema_126d_base_v119_signal,
    f21dg_f21_distress_going_concern_eqtermspr_base_v120_signal,
    f21dg_f21_distress_going_concern_levtermspr_base_v121_signal,
    f21dg_f21_distress_going_concern_x3root_63d_base_v122_signal,
    f21dg_f21_distress_going_concern_netcashsignlog_63d_base_v123_signal,
    f21dg_f21_distress_going_concern_deftanh_63d_base_v124_signal,
    f21dg_f21_distress_going_concern_ebiteq_63d_base_v125_signal,
    f21dg_f21_distress_going_concern_reeq_63d_base_v126_signal,
    f21dg_f21_distress_going_concern_wcoblig_63d_base_v127_signal,
    f21dg_f21_distress_going_concern_reveq_63d_base_v128_signal,
    f21dg_f21_distress_going_concern_minz_252d_base_v129_signal,
    f21dg_f21_distress_going_concern_minx4_126d_base_v130_signal,
    f21dg_f21_distress_going_concern_maxlev_252d_base_v131_signal,
    f21dg_f21_distress_going_concern_eqyoy_252d_base_v132_signal,
    f21dg_f21_distress_going_concern_levyoy_252d_base_v133_signal,
    f21dg_f21_distress_going_concern_x3yoy_252d_base_v134_signal,
    f21dg_f21_distress_going_concern_netdebtz_252d_base_v135_signal,
    f21dg_f21_distress_going_concern_ebiteqrank_504d_base_v136_signal,
    f21dg_f21_distress_going_concern_reeqrank_504d_base_v137_signal,
    f21dg_f21_distress_going_concern_survbuffer_63d_base_v138_signal,
    f21dg_f21_distress_going_concern_distdistance_base_v139_signal,
    f21dg_f21_distress_going_concern_zombiescore_base_v140_signal,
    f21dg_f21_distress_going_concern_zrecov_252d_base_v141_signal,
    f21dg_f21_distress_going_concern_eqrecov_252d_base_v142_signal,
    f21dg_f21_distress_going_concern_nearinsolvtime_252d_base_v143_signal,
    f21dg_f21_distress_going_concern_shortfallsum_63d_base_v144_signal,
    f21dg_f21_distress_going_concern_zcurv_63d_base_v145_signal,
    f21dg_f21_distress_going_concern_x4curv_63d_base_v146_signal,
    f21dg_f21_distress_going_concern_zwidth_base_v147_signal,
    f21dg_f21_distress_going_concern_cashsurv_63d_base_v148_signal,
    f21dg_f21_distress_going_concern_ebitliabz_252d_base_v149_signal,
    f21dg_f21_distress_going_concern_gcoverall_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_DISTRESS_GOING_CONCERN_REGISTRY_076_150 = REGISTRY


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

    workingcapital = _fund(2101, base=4e7, drift=-0.02, vol=0.18, allow_neg=True).rename("workingcapital")
    retearn = _fund(2102, base=6e7, drift=-0.03, vol=0.16, allow_neg=True).rename("retearn")
    ebit = _fund(2103, base=3e7, drift=-0.01, vol=0.22, allow_neg=True).rename("ebit")
    equity = _fund(2104, base=8e7, drift=-0.015, vol=0.14, allow_neg=True).rename("equity")
    liabilities = _fund(2105, base=9e7, drift=0.02, vol=0.09).rename("liabilities")
    assets = _fund(2106, base=1.8e8, drift=0.0, vol=0.07).rename("assets")
    revenue = _fund(2107, base=7e7, drift=0.01, vol=0.12).rename("revenue")
    cashneq = _fund(2108, base=3e7, drift=-0.02, vol=0.16).rename("cashneq")

    cols = {"workingcapital": workingcapital, "retearn": retearn, "ebit": ebit,
            "equity": equity, "liabilities": liabilities, "assets": assets,
            "revenue": revenue, "cashneq": cashneq}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("workingcapital", "retearn", "ebit", "equity",
                          "liabilities", "assets", "revenue", "cashneq")
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

    print("OK f21_distress_going_concern_base_076_150_claude: %d features pass" % n_features)
