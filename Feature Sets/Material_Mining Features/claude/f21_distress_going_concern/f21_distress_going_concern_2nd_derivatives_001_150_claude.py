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


def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (distress / going concern) =====
def _x1(workingcapital, assets):
    return workingcapital / assets.replace(0, np.nan)


def _x2(retearn, assets):
    return retearn / assets.replace(0, np.nan)


def _x3(ebit, assets):
    return ebit / assets.replace(0, np.nan)


def _x4(equity, liabilities):
    return equity / liabilities.replace(0, np.nan)


def _x5(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    x1 = workingcapital / assets.replace(0, np.nan)
    x2 = retearn / assets.replace(0, np.nan)
    x3 = ebit / assets.replace(0, np.nan)
    x4 = equity / liabilities.replace(0, np.nan)
    x5 = revenue / assets.replace(0, np.nan)
    return 0.717 * x1 + 0.847 * x2 + 3.107 * x3 + 0.420 * x4 + 0.998 * x5


def _zminer(workingcapital, retearn, ebit, equity, liabilities, assets):
    x1 = workingcapital / assets.replace(0, np.nan)
    x2 = retearn / assets.replace(0, np.nan)
    x3 = ebit / assets.replace(0, np.nan)
    x4 = equity / liabilities.replace(0, np.nan)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def _below_med(ratio, w):
    med = ratio.rolling(w, min_periods=max(1, w // 2)).median()
    return (med - ratio).clip(lower=0)


# ============================================================
# Each feature: build a distress / going-concern base series inline, then take its
# 1st math derivative (slope) over a window matched to the base window.

# slope of Altman Z' (distress-score velocity), 21d
def f21dg_f21_distress_going_concern_altz_21d_slope_v001_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    base = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Altman Z', 63d (slower distress velocity)
def f21dg_f21_distress_going_concern_altz_63d_slope_v002_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    base = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/solvency-weighted miner-Z (operating+solvency emphasis), 21d
def f21dg_f21_distress_going_concern_zminer_21d_slope_v003_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    base = (1.0 * _x1(workingcapital, assets) + 4.0 * _x2(retearn, assets)
            + 10.0 * _x3(ebit, assets) + 3.0 * _x4(equity, liabilities))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/solvency-weighted miner-Z, 63d
def f21dg_f21_distress_going_concern_zminer_63d_slope_v004_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    base = (1.0 * _x1(workingcapital, assets) + 4.0 * _x2(retearn, assets)
            + 10.0 * _x3(ebit, assets) + 3.0 * _x4(equity, liabilities))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X1 (wc/assets), 21d (liquidity-buffer velocity)
def f21dg_f21_distress_going_concern_x1_21d_slope_v005_signal(workingcapital, assets):
    base = _x1(workingcapital, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X2 (retearn/assets), 21d (deficit-drag velocity)
def f21dg_f21_distress_going_concern_x2_21d_slope_v006_signal(retearn, assets):
    base = _x2(retearn, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X3 (ebit/assets), 21d (operating-return velocity)
def f21dg_f21_distress_going_concern_x3_21d_slope_v007_signal(ebit, assets):
    base = _x3(ebit, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X4 (equity/liabilities) short-vs-long term spread, 21d (solvency term-structure velocity)
def f21dg_f21_distress_going_concern_x4_21d_slope_v008_signal(equity, liabilities):
    r = _x4(equity, liabilities)
    base = r.rolling(63, min_periods=21).mean() - r.rolling(252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X5 (revenue/assets), 21d (asset-turnover velocity)
def f21dg_f21_distress_going_concern_x5_21d_slope_v009_signal(revenue, assets):
    base = _x5(revenue, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets solvency, 21d (capital-erosion velocity)
def f21dg_f21_distress_going_concern_eqassets_21d_slope_v010_signal(equity, assets):
    base = equity / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets, 63d
def f21dg_f21_distress_going_concern_eqassets_63d_slope_v011_signal(equity, assets):
    base = equity / assets.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage (liabilities/assets), 21d (gearing-build velocity)
def f21dg_f21_distress_going_concern_lev_21d_slope_v012_signal(liabilities, assets):
    base = liabilities / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage, 63d
def f21dg_f21_distress_going_concern_lev_63d_slope_v013_signal(liabilities, assets):
    base = liabilities / assets.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-debt/assets, 21d (cash-adjusted gearing velocity)
def f21dg_f21_distress_going_concern_netdebt_21d_slope_v014_signal(liabilities, cashneq, assets):
    base = (liabilities - cashneq) / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-cash-solvency z-scored vs 252d, 21d (cash-adjusted solvency regime velocity)
def f21dg_f21_distress_going_concern_netcashsolv_21d_slope_v015_signal(cashneq, liabilities, assets):
    base = _z((cashneq - liabilities) / assets.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/assets, 21d (treasury-share velocity)
def f21dg_f21_distress_going_concern_cashassets_21d_slope_v016_signal(cashneq, assets):
    base = cashneq / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/liabilities coverage, 21d
def f21dg_f21_distress_going_concern_cashcover_21d_slope_v017_signal(cashneq, liabilities):
    base = cashneq / liabilities.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue coverage of liabilities, 21d
def f21dg_f21_distress_going_concern_revcover_21d_slope_v018_signal(revenue, liabilities):
    base = revenue / liabilities.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT margin (ebit/revenue), 21d (operating-margin velocity)
def f21dg_f21_distress_going_concern_ebitmargin_21d_slope_v019_signal(ebit, revenue):
    base = ebit / revenue.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/liabilities, 21d (operating cover velocity)
def f21dg_f21_distress_going_concern_ebitliab_21d_slope_v020_signal(ebit, liabilities):
    base = ebit / liabilities.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/equity (return on capital), 21d
def f21dg_f21_distress_going_concern_ebiteq_21d_slope_v021_signal(ebit, equity):
    base = (ebit / equity.abs().replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retained-earnings/equity (deficit share of capital), 21d
def f21dg_f21_distress_going_concern_reeq_21d_slope_v022_signal(retearn, equity):
    base = (retearn / equity.abs().replace(0, np.nan)).clip(lower=-20.0, upper=20.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-debt/equity gearing, 21d
def f21dg_f21_distress_going_concern_netdebteq_21d_slope_v023_signal(liabilities, cashneq, equity):
    base = ((liabilities - cashneq) / equity.abs().replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity-capitalization drawdown from its 252d peak, 21d (capital-share erosion velocity)
def f21dg_f21_distress_going_concern_eqcap_21d_slope_v024_signal(equity, liabilities):
    cap = equity / (equity + liabilities).replace(0, np.nan)
    base = cap - _rmax(cap, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Altman Z z-score (de-trended distress regime velocity), 21d
def f21dg_f21_distress_going_concern_altzz_21d_slope_v025_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = _z(z, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Altman Z percentile-rank, 21d
def f21dg_f21_distress_going_concern_altzrank_21d_slope_v026_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = _rank(z, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets z-score, 21d
def f21dg_f21_distress_going_concern_eqassetsz_21d_slope_v027_signal(equity, assets):
    base = _z(equity / assets.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage z-score, 21d
def f21dg_f21_distress_going_concern_levz_21d_slope_v028_signal(liabilities, assets):
    base = _z(liabilities / assets.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/assets percentile-rank, 21d
def f21dg_f21_distress_going_concern_x3rank_21d_slope_v029_signal(ebit, assets):
    base = _rank(_x3(ebit, assets), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X4 percentile-rank, 21d
def f21dg_f21_distress_going_concern_x4rank_21d_slope_v030_signal(equity, liabilities):
    base = _rank(_x4(equity, liabilities), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of distress-zone shortfall (1.1 - Z clipped), 21d
def f21dg_f21_distress_going_concern_zonegap_21d_slope_v031_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = (1.1 - z).clip(lower=0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accumulated-deficit erosion (below 252d median retearn/assets), 21d
def f21dg_f21_distress_going_concern_deficit_21d_slope_v032_signal(retearn, assets):
    base = _below_med(_x2(retearn, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of working-capital shortfall (below 252d median X1), 21d
def f21dg_f21_distress_going_concern_wcshort_21d_slope_v033_signal(workingcapital, assets):
    base = _below_med(_x1(workingcapital, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of solvency shortfall (below 252d median X4), 21d
def f21dg_f21_distress_going_concern_solvshort_21d_slope_v034_signal(equity, liabilities):
    base = _below_med(_x4(equity, liabilities), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-cash-solvency, 63d
def f21dg_f21_distress_going_concern_netcashsolv_63d_slope_v035_signal(cashneq, liabilities, assets):
    base = (cashneq - liabilities) / assets.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of survival buffer (eqa + casha - lev), 21d
def f21dg_f21_distress_going_concern_survbuffer_21d_slope_v036_signal(equity, cashneq, liabilities, assets):
    eqa = equity / assets.replace(0, np.nan)
    casha = cashneq / assets.replace(0, np.nan)
    lev = liabilities / assets.replace(0, np.nan)
    base = eqa + casha - lev
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of magnitude going-concern composite (eqa + 0.5 rea + eba), 21d
def f21dg_f21_distress_going_concern_gcmag_21d_slope_v037_signal(equity, retearn, ebit, assets):
    base = (equity / assets.replace(0, np.nan)
            + 0.5 * retearn / assets.replace(0, np.nan)
            + ebit / assets.replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT-to-(equity+liabilities) capital yield, 21d (return on invested capital velocity)
def f21dg_f21_distress_going_concern_x3contrib_21d_slope_v038_signal(ebit, equity, liabilities):
    base = (ebit / (equity + liabilities).replace(0, np.nan)).clip(lower=-5.0, upper=5.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-debt/equity z-score, 21d
def f21dg_f21_distress_going_concern_netdebtz_21d_slope_v039_signal(liabilities, cashneq, equity):
    r = ((liabilities - cashneq) / equity.abs().replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    base = _z(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue/equity (capital productivity), 21d
def f21dg_f21_distress_going_concern_reveq_21d_slope_v040_signal(revenue, equity):
    base = (revenue / equity.abs().replace(0, np.nan)).clip(upper=50.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of working-capital/liabilities, 21d
def f21dg_f21_distress_going_concern_wcliab_21d_slope_v041_signal(workingcapital, liabilities):
    base = workingcapital / liabilities.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash vs current obligations proxy, 21d
def f21dg_f21_distress_going_concern_cashoblig_21d_slope_v042_signal(cashneq, liabilities, workingcapital):
    oblig = (liabilities - workingcapital).clip(lower=1.0)
    base = (cashneq / oblig).clip(upper=20.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT margin z-score, 21d
def f21dg_f21_distress_going_concern_ebitmarginz_21d_slope_v043_signal(ebit, revenue):
    base = _z(ebit / revenue.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retained-earnings/assets z-score, 21d
def f21dg_f21_distress_going_concern_x2z_21d_slope_v044_signal(retearn, assets):
    base = _z(_x2(retearn, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue/assets z-score, 21d
def f21dg_f21_distress_going_concern_x5z_21d_slope_v045_signal(revenue, assets):
    base = _z(_x5(revenue, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-coverage drawdown from its 252d peak, 21d (cash-cushion erosion velocity)
def f21dg_f21_distress_going_concern_netcashcov_21d_slope_v046_signal(cashneq, liabilities):
    c = cashneq / liabilities.replace(0, np.nan)
    base = c - _rmax(c, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of solvency-minus-leverage spread (X4 - liab/assets), 21d (net balance-sheet strength velocity)
def f21dg_f21_distress_going_concern_solvdefspr_21d_slope_v047_signal(equity, liabilities, assets):
    base = _x4(equity, liabilities) - liabilities / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-liquidity-vs-leverage spread percentile-rank vs 504d, 21d
def f21dg_f21_distress_going_concern_liqlevspr_21d_slope_v048_signal(cashneq, liabilities, assets):
    spread = cashneq / assets.replace(0, np.nan) - liabilities / assets.replace(0, np.nan)
    base = _rank(spread, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/assets z-score, 21d
def f21dg_f21_distress_going_concern_x3z_21d_slope_v049_signal(ebit, assets):
    base = _z(_x3(ebit, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X4 z-score, 21d
def f21dg_f21_distress_going_concern_x4z_21d_slope_v050_signal(equity, liabilities):
    base = _z(_x4(equity, liabilities), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 5d (fast) slopes ---
# slope of Altman Z', 5d (acute distress-score velocity)
def f21dg_f21_distress_going_concern_altz_5d_slope_v051_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    base = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets, 5d
def f21dg_f21_distress_going_concern_eqassets_5d_slope_v052_signal(equity, assets):
    base = equity / assets.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage, 5d
def f21dg_f21_distress_going_concern_lev_5d_slope_v053_signal(liabilities, assets):
    base = liabilities / assets.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/assets, 5d
def f21dg_f21_distress_going_concern_x3_5d_slope_v054_signal(ebit, assets):
    base = _x3(ebit, assets)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/assets, 5d
def f21dg_f21_distress_going_concern_cashassets_5d_slope_v055_signal(cashneq, assets):
    base = cashneq / assets.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 63d slopes of secondary distress series ---
# slope of net-debt run-up off its 252d trough, 21d (gearing-build velocity off low)
def f21dg_f21_distress_going_concern_netdebt_63d_slope_v056_signal(liabilities, cashneq, assets):
    nd = (liabilities - cashneq) / assets.replace(0, np.nan)
    base = nd - _rmin(nd, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/liabilities coverage, 63d
def f21dg_f21_distress_going_concern_cashcover_63d_slope_v057_signal(cashneq, liabilities):
    base = cashneq / liabilities.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT margin, 63d
def f21dg_f21_distress_going_concern_ebitmargin_63d_slope_v058_signal(ebit, revenue):
    base = ebit / revenue.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue coverage of liabilities, 63d
def f21dg_f21_distress_going_concern_revcover_63d_slope_v059_signal(revenue, liabilities):
    base = revenue / liabilities.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X1 (wc/assets), 63d
def f21dg_f21_distress_going_concern_x1_63d_slope_v060_signal(workingcapital, assets):
    base = _x1(workingcapital, assets)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X2 (retearn/assets), 63d
def f21dg_f21_distress_going_concern_x2_63d_slope_v061_signal(retearn, assets):
    base = _x2(retearn, assets)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X4 (equity/liabilities) percentile-rank vs 504d, 63d (solvency-percentile drift)
def f21dg_f21_distress_going_concern_x4_63d_slope_v062_signal(equity, liabilities):
    base = _rank(_x4(equity, liabilities), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X5 (revenue/assets), 63d
def f21dg_f21_distress_going_concern_x5_63d_slope_v063_signal(revenue, assets):
    base = _x5(revenue, assets)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-cash-solvency, 5d
def f21dg_f21_distress_going_concern_netcashsolv_5d_slope_v064_signal(cashneq, liabilities, assets):
    base = (cashneq - liabilities) / assets.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/equity, 63d
def f21dg_f21_distress_going_concern_ebiteq_63d_slope_v065_signal(ebit, equity):
    base = (ebit / equity.abs().replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retearn/equity, 63d
def f21dg_f21_distress_going_concern_reeq_63d_slope_v066_signal(retearn, equity):
    base = (retearn / equity.abs().replace(0, np.nan)).clip(lower=-20.0, upper=20.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of survival buffer, 63d
def f21dg_f21_distress_going_concern_survbuffer_63d_slope_v067_signal(equity, cashneq, liabilities, assets):
    eqa = equity / assets.replace(0, np.nan)
    casha = cashneq / assets.replace(0, np.nan)
    lev = liabilities / assets.replace(0, np.nan)
    base = eqa + casha - lev
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of miner-Z z-score, 21d
def f21dg_f21_distress_going_concern_zminerz_21d_slope_v068_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    base = _z(_zminer(workingcapital, retearn, ebit, equity, liabilities, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Z-component dispersion (z-normalised), 21d
def f21dg_f21_distress_going_concern_zcompdisp_21d_slope_v069_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    x1 = _z(_x1(workingcapital, assets), 252)
    x2 = _z(_x2(retearn, assets), 252)
    x3 = _z(_x3(ebit, assets), 252)
    x4 = _z(_x4(equity, liabilities), 252)
    x5 = _z(_x5(revenue, assets), 252)
    base = pd.concat([x1, x2, x3, x4, x5], axis=1).std(axis=1)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Altman Z percentile-rank smoothed (63d mean), 21d (distress-percentile drift velocity)
def f21dg_f21_distress_going_concern_altzsm_21d_slope_v070_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = _rank(z, 504).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage smoothed (63d mean), 21d
def f21dg_f21_distress_going_concern_levsm_21d_slope_v071_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    base = lev.rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/liabilities percentile-rank vs 504d, 21d (cash-cover percentile velocity)
def f21dg_f21_distress_going_concern_cashcoversm_21d_slope_v072_signal(cashneq, liabilities):
    base = _rank(cashneq / liabilities.replace(0, np.nan), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of distress-zone shortfall (1.1 - Z), 63d
def f21dg_f21_distress_going_concern_zonegap_63d_slope_v073_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = (1.1 - z).clip(lower=0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accumulated-deficit erosion, 63d
def f21dg_f21_distress_going_concern_deficit_63d_slope_v074_signal(retearn, assets):
    base = _below_med(_x2(retearn, assets), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of solvency shortfall, 63d
def f21dg_f21_distress_going_concern_solvshort_63d_slope_v075_signal(equity, liabilities):
    base = _below_med(_x4(equity, liabilities), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 126d (slow) and 42d (intermediate) slopes ---
# slope of Altman Z', 126d (structural distress drift)
def f21dg_f21_distress_going_concern_altz_126d_slope_v076_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    base = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets, 126d
def f21dg_f21_distress_going_concern_eqassets_126d_slope_v077_signal(equity, assets):
    base = equity / assets.replace(0, np.nan)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage, 126d
def f21dg_f21_distress_going_concern_lev_126d_slope_v078_signal(liabilities, assets):
    base = liabilities / assets.replace(0, np.nan)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/assets, 126d
def f21dg_f21_distress_going_concern_x3_126d_slope_v079_signal(ebit, assets):
    base = _x3(ebit, assets)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X4, 126d
def f21dg_f21_distress_going_concern_x4_126d_slope_v080_signal(equity, liabilities):
    base = _x4(equity, liabilities)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Altman Z', 42d
def f21dg_f21_distress_going_concern_altz_42d_slope_v081_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    base = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets, 42d
def f21dg_f21_distress_going_concern_eqassets_42d_slope_v082_signal(equity, assets):
    base = equity / assets.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage, 42d
def f21dg_f21_distress_going_concern_lev_42d_slope_v083_signal(liabilities, assets):
    base = liabilities / assets.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/assets, 42d
def f21dg_f21_distress_going_concern_cashassets_42d_slope_v084_signal(cashneq, assets):
    base = cashneq / assets.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/liabilities, 42d
def f21dg_f21_distress_going_concern_ebitliab_42d_slope_v085_signal(ebit, liabilities):
    base = ebit / liabilities.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X1, 42d
def f21dg_f21_distress_going_concern_x1_42d_slope_v086_signal(workingcapital, assets):
    base = _x1(workingcapital, assets)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X2, 42d
def f21dg_f21_distress_going_concern_x2_42d_slope_v087_signal(retearn, assets):
    base = _x2(retearn, assets)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-debt/assets, 42d
def f21dg_f21_distress_going_concern_netdebt_42d_slope_v088_signal(liabilities, cashneq, assets):
    base = (liabilities - cashneq) / assets.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT margin, 42d
def f21dg_f21_distress_going_concern_ebitmargin_42d_slope_v089_signal(ebit, revenue):
    base = ebit / revenue.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue coverage, 42d
def f21dg_f21_distress_going_concern_revcover_42d_slope_v090_signal(revenue, liabilities):
    base = revenue / liabilities.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- slopes of trend / drawdown / recovery distress bases ---
# slope of Altman Z drawdown from 252d peak, 21d
def f21dg_f21_distress_going_concern_zdd_21d_slope_v091_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = z - _rmax(z, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets drawdown from 252d peak, 21d
def f21dg_f21_distress_going_concern_eqdd_21d_slope_v092_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    base = r - _rmax(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Altman Z recovery off 252d trough, 21d
def f21dg_f21_distress_going_concern_zrecov_21d_slope_v093_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = z - _rmin(z, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage run-up off 252d trough, 21d
def f21dg_f21_distress_going_concern_levrunup_21d_slope_v094_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    base = lev - _rmin(lev, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of min Altman Z (126d), 63d
def f21dg_f21_distress_going_concern_minz_63d_slope_v095_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = _rmin(z, 126)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of max leverage (126d), 63d
def f21dg_f21_distress_going_concern_maxlev_63d_slope_v096_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    base = _rmax(lev, 126)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue drawdown from 252d peak, 21d
def f21dg_f21_distress_going_concern_revdd_21d_slope_v097_signal(revenue):
    peak = _rmax(revenue, 252)
    base = revenue / peak.replace(0, np.nan) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/assets drawdown from 252d peak, 21d
def f21dg_f21_distress_going_concern_cashdd_21d_slope_v098_signal(cashneq, assets):
    r = cashneq / assets.replace(0, np.nan)
    base = r - _rmax(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-cash-solvency volatility (126d std), 63d (cash-solvency instability velocity)
def f21dg_f21_distress_going_concern_netcashdd_21d_slope_v099_signal(cashneq, liabilities, assets):
    r = (cashneq - liabilities) / assets.replace(0, np.nan)
    base = r.rolling(126, min_periods=63).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of going-concern severity weighted by leverage (zone-depth x lev), 21d
def f21dg_f21_distress_going_concern_gcXlev_21d_slope_v100_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    zonedepth = (1.1 - z).clip(lower=0)
    lev = liabilities / assets.replace(0, np.nan)
    base = zonedepth * lev
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- slopes of term-spread / displacement bases ---
# slope of Altman Z term spread (short-long), 21d
def f21dg_f21_distress_going_concern_ztermspr_21d_slope_v101_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = z.rolling(63, min_periods=21).mean() - z.rolling(252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage term spread (short-long), 21d
def f21dg_f21_distress_going_concern_levtermspr_21d_slope_v102_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    base = lev.rolling(63, min_periods=21).mean() - lev.rolling(252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Altman Z displacement from slow EMA, 21d
def f21dg_f21_distress_going_concern_zdisp_21d_slope_v103_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = z - z.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets displacement from slow EMA, 21d
def f21dg_f21_distress_going_concern_eqdisp_21d_slope_v104_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    base = r - r.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/liabilities displacement from slow EMA, 21d
def f21dg_f21_distress_going_concern_cashcoverdisp_21d_slope_v105_signal(cashneq, liabilities):
    r = cashneq / liabilities.replace(0, np.nan)
    base = r - r.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- slopes of volatility / dispersion bases ---
# slope of Altman Z volatility (126d std), 63d
def f21dg_f21_distress_going_concern_zvol_63d_slope_v106_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    base = z.rolling(126, min_periods=63).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage volatility (126d std), 63d
def f21dg_f21_distress_going_concern_levvol_63d_slope_v107_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    base = lev.rolling(126, min_periods=63).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/assets volatility (126d std), 63d
def f21dg_f21_distress_going_concern_x3vol_63d_slope_v108_signal(ebit, assets):
    r = _x3(ebit, assets)
    base = r.rolling(126, min_periods=63).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets coefficient-of-variation (252d), 63d
def f21dg_f21_distress_going_concern_eqcv_63d_slope_v109_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    base = _std(r, 252) / _mean(r, 252).abs().replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-debt/equity, 63d
def f21dg_f21_distress_going_concern_netdebteq_63d_slope_v110_signal(liabilities, cashneq, equity):
    base = ((liabilities - cashneq) / equity.abs().replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- slopes of tally / time-in-zone bases ---
# slope of distress-time fraction (Altman Z weak), 21d
def f21dg_f21_distress_going_concern_distresstime_21d_slope_v111_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    thr = z.rolling(504, min_periods=252).quantile(0.25)
    indist = (z <= thr).astype(float)
    base = indist.rolling(126, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of weak-channel count smoothed (going-concern breadth), 21d
def f21dg_f21_distress_going_concern_gcbreadth_21d_slope_v112_signal(equity, retearn, ebit, workingcapital, assets):
    def wk(r):
        thr = r.rolling(504, min_periods=252).quantile(0.30)
        return (r <= thr).astype(float)
    cnt = (wk(equity / assets.replace(0, np.nan)) + wk(retearn / assets.replace(0, np.nan))
           + wk(ebit / assets.replace(0, np.nan)) + wk(workingcapital / assets.replace(0, np.nan)))
    base = cnt.rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of leverage-spike time fraction, 21d
def f21dg_f21_distress_going_concern_levspiketime_21d_slope_v113_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    thr = lev.rolling(504, min_periods=252).quantile(0.80)
    high = (lev >= thr).astype(float)
    base = high.rolling(126, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of shortfall-sum across four channels, 21d
def f21dg_f21_distress_going_concern_shortfallsum_21d_slope_v114_signal(equity, retearn, ebit, workingcapital, assets):
    s = (_below_med(equity / assets.replace(0, np.nan), 252)
         + _below_med(retearn / assets.replace(0, np.nan), 252)
         + _below_med(ebit / assets.replace(0, np.nan), 252)
         + _below_med(workingcapital / assets.replace(0, np.nan), 252))
    base = s.rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of zombie-distress score (loss-time + deficit-time + lev), 21d
def f21dg_f21_distress_going_concern_zombie_21d_slope_v115_signal(ebit, retearn, liabilities, assets):
    def wk(r):
        thr = r.rolling(504, min_periods=252).quantile(0.30)
        return (r <= thr).astype(float)
    loss_t = wk(_x3(ebit, assets)).rolling(126, min_periods=63).mean()
    def_t = wk(_x2(retearn, assets)).rolling(126, min_periods=63).mean()
    lev = (liabilities / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    base = loss_t + def_t + lev
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- slopes of interaction / composite bases ---
# slope of equity-erosion (below 252d peak) x net-debt/equity interaction, 21d (levered capital-bleed)
def f21dg_f21_distress_going_concern_eqerosXlev_21d_slope_v116_signal(equity, assets, liabilities, cashneq):
    r = equity / assets.replace(0, np.nan)
    erosion = (_rmax(r, 252) - r).clip(lower=0)
    gear = ((liabilities - cashneq) / equity.abs().replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    base = erosion * gear
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of operating-loss x leverage interaction, 21d
def f21dg_f21_distress_going_concern_lossXlev_21d_slope_v117_signal(ebit, assets, liabilities):
    loss = _below_med(_x3(ebit, assets), 252)
    lev = liabilities / assets.replace(0, np.nan)
    base = loss * lev
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/assets percentile-rank vs 504d, 21d (treasury-share percentile velocity)
def f21dg_f21_distress_going_concern_cashsurv_21d_slope_v118_signal(cashneq, assets):
    base = _rank(cashneq / assets.replace(0, np.nan), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of overall going-concern composite (-zZ + zLev + deftime), 21d
def f21dg_f21_distress_going_concern_gcoverall_21d_slope_v119_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    lev = liabilities / assets.replace(0, np.nan)
    thr = (_x2(retearn, assets)).rolling(504, min_periods=252).quantile(0.30)
    deftime = ((_x2(retearn, assets)) <= thr).astype(float).rolling(126, min_periods=63).mean()
    base = -_z(z, 252) + _z(lev, 252) + deftime
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of operating-margin-erosion x leverage interaction, 21d (levered margin-collapse velocity)
def f21dg_f21_distress_going_concern_insolXlev_21d_slope_v120_signal(ebit, revenue, liabilities, assets):
    m = ebit / revenue.replace(0, np.nan)
    erosion = (_rmax(m, 252) - m).clip(lower=0)
    lev = liabilities / assets.replace(0, np.nan)
    base = erosion * lev
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional component / ratio slopes at varied windows ---
# slope of X1 (wc/assets) smoothed, 63d
def f21dg_f21_distress_going_concern_x1sm_63d_slope_v121_signal(workingcapital, assets):
    base = _x1(workingcapital, assets).rolling(63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of X3 (ebit/assets) displacement from slow EMA, 21d (acute operating-return shift)
def f21dg_f21_distress_going_concern_x3sm_63d_slope_v122_signal(ebit, assets):
    r = _x3(ebit, assets)
    base = r - r.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/equity percentile-rank, 63d
def f21dg_f21_distress_going_concern_ebiteqrank_63d_slope_v123_signal(ebit, equity):
    r = (ebit / equity.abs().replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    base = _rank(r, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retearn/equity percentile-rank, 63d
def f21dg_f21_distress_going_concern_reeqrank_63d_slope_v124_signal(retearn, equity):
    r = (retearn / equity.abs().replace(0, np.nan)).clip(lower=-20.0, upper=20.0)
    base = _rank(r, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-debt/assets z-score, 63d
def f21dg_f21_distress_going_concern_netdebtz_63d_slope_v125_signal(liabilities, cashneq, assets):
    r = (liabilities - cashneq) / assets.replace(0, np.nan)
    base = _z(r, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue/assets percentile-rank vs 504d, 21d (turnover-percentile velocity)
def f21dg_f21_distress_going_concern_x5lvl_21d_slope_v126_signal(revenue, assets):
    base = _rank(_x5(revenue, assets), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of working-capital/liabilities, 63d
def f21dg_f21_distress_going_concern_wcliab_63d_slope_v127_signal(workingcapital, liabilities):
    base = workingcapital / liabilities.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity-capitalization displacement from its slow EMA, 63d (acute capital-share shift)
def f21dg_f21_distress_going_concern_eqcap_63d_slope_v128_signal(equity, liabilities):
    cap = equity / (equity + liabilities).replace(0, np.nan)
    base = cap - cap.ewm(span=252, min_periods=84).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT margin percentile-rank, 63d
def f21dg_f21_distress_going_concern_ebitmarginrank_63d_slope_v129_signal(ebit, revenue):
    base = _rank(ebit / revenue.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of miner-Z percentile-rank, 63d
def f21dg_f21_distress_going_concern_zminerrank_63d_slope_v130_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    base = _rank(_zminer(workingcapital, retearn, ebit, equity, liabilities, assets), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Altman-Z minus miner-Z spread (z forms), 21d
def f21dg_f21_distress_going_concern_zspread_21d_slope_v131_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    za = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    zm = _zminer(workingcapital, retearn, ebit, equity, liabilities, assets)
    base = _z(za, 252) - _z(zm, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-vs-current-obligations proxy, 63d
def f21dg_f21_distress_going_concern_cashoblig_63d_slope_v132_signal(cashneq, liabilities, workingcapital):
    oblig = (liabilities - workingcapital).clip(lower=1.0)
    base = (cashneq / oblig).clip(upper=20.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of working-capital/current-obligations proxy, 21d
def f21dg_f21_distress_going_concern_wcoblig_21d_slope_v133_signal(workingcapital, liabilities):
    oblig = (liabilities - workingcapital).clip(lower=1.0)
    base = (workingcapital / oblig).clip(lower=-5.0, upper=5.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-cash coverage of liabilities z-score, 21d
def f21dg_f21_distress_going_concern_netcashcovz_21d_slope_v134_signal(cashneq, liabilities):
    r = (cashneq - liabilities) / liabilities.replace(0, np.nan)
    base = _z(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue coverage z-score, 21d
def f21dg_f21_distress_going_concern_revcoverz_21d_slope_v135_signal(revenue, liabilities):
    base = _z(revenue / liabilities.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT/liabilities z-score, 21d
def f21dg_f21_distress_going_concern_ebitliabz_21d_slope_v136_signal(ebit, liabilities):
    base = _z(ebit / liabilities.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accumulated-deficit pressure (mean quarterly declines), 63d
def f21dg_f21_distress_going_concern_defpress_63d_slope_v137_signal(retearn, assets):
    r = retearn / assets.replace(0, np.nan)
    decl = (r.shift(21) - r).clip(lower=0)
    base = decl.rolling(126, min_periods=63).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT-margin erosion below 252d peak, 21d
def f21dg_f21_distress_going_concern_ebiteros_21d_slope_v138_signal(ebit, revenue):
    m = ebit / revenue.replace(0, np.nan)
    base = (_rmax(m, 252) - m).clip(lower=0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retearn-erosion below 252d peak (deficit accumulation), 21d
def f21dg_f21_distress_going_concern_reeros_21d_slope_v139_signal(retearn, assets):
    r = retearn / assets.replace(0, np.nan)
    base = (_rmax(r, 252) - r).clip(lower=0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets recovery off 126d trough scaled by recovery magnitude, 21d
def f21dg_f21_distress_going_concern_eqrecov_21d_slope_v140_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    trough = _rmin(r, 126)
    base = (r - trough) * np.sign(r)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of distress distance composite (cnt + levrank - solvrank), 21d
def f21dg_f21_distress_going_concern_distdistance_21d_slope_v141_signal(equity, retearn, ebit, workingcapital, liabilities, assets):
    def wk(r):
        thr = r.rolling(252, min_periods=126).quantile(0.25)
        return (r <= thr).astype(float)
    cnt = (wk(equity / assets.replace(0, np.nan)) + wk(retearn / assets.replace(0, np.nan))
           + wk(ebit / assets.replace(0, np.nan)) + wk(workingcapital / assets.replace(0, np.nan)))
    base = cnt + _rank(liabilities / assets.replace(0, np.nan), 252) - _rank(equity / assets.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-debt/equity percentile-rank, 63d
def f21dg_f21_distress_going_concern_netdebteqrank_63d_slope_v142_signal(liabilities, cashneq, equity):
    g = ((liabilities - cashneq) / equity.abs().replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    base = _rank(g, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue/equity, 63d
def f21dg_f21_distress_going_concern_reveq_63d_slope_v143_signal(revenue, equity):
    base = (revenue / equity.abs().replace(0, np.nan)).clip(upper=50.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash/assets z-score, 21d
def f21dg_f21_distress_going_concern_cashassetsz_21d_slope_v144_signal(cashneq, assets):
    base = _z(cashneq / assets.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT-margin displacement from slow EMA, 21d (acute margin shift velocity)
def f21dg_f21_distress_going_concern_ebitmarginsm_21d_slope_v145_signal(ebit, revenue):
    m = ebit / revenue.replace(0, np.nan)
    base = m - m.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-debt/assets smoothed (63d), 21d
def f21dg_f21_distress_going_concern_netdebtsm_21d_slope_v146_signal(liabilities, cashneq, assets):
    base = ((liabilities - cashneq) / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of solvency-minus-leverage spread (X4 - liab/assets), 63d (net strength drift)
def f21dg_f21_distress_going_concern_solvdefspr_63d_slope_v147_signal(equity, liabilities, assets):
    base = _x4(equity, liabilities) - liabilities / assets.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of going-concern severity weighted by leverage, 63d
def f21dg_f21_distress_going_concern_gcXlev_63d_slope_v148_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    zonedepth = (1.1 - z).clip(lower=0)
    lev = liabilities / assets.replace(0, np.nan)
    base = zonedepth * lev
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-cash coverage of liabilities ((cash-liab)/liab), 42d (cash-solvency velocity)
def f21dg_f21_distress_going_concern_netcashsolv_42d_slope_v149_signal(cashneq, liabilities):
    base = (cashneq - liabilities) / liabilities.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of overall going-concern composite, 63d
def f21dg_f21_distress_going_concern_gcoverall_63d_slope_v150_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    lev = liabilities / assets.replace(0, np.nan)
    thr = (_x2(retearn, assets)).rolling(504, min_periods=252).quantile(0.30)
    deftime = ((_x2(retearn, assets)) <= thr).astype(float).rolling(126, min_periods=63).mean()
    base = -_z(z, 252) + _z(lev, 252) + deftime
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21dg_f21_distress_going_concern_altz_21d_slope_v001_signal,
    f21dg_f21_distress_going_concern_altz_63d_slope_v002_signal,
    f21dg_f21_distress_going_concern_zminer_21d_slope_v003_signal,
    f21dg_f21_distress_going_concern_zminer_63d_slope_v004_signal,
    f21dg_f21_distress_going_concern_x1_21d_slope_v005_signal,
    f21dg_f21_distress_going_concern_x2_21d_slope_v006_signal,
    f21dg_f21_distress_going_concern_x3_21d_slope_v007_signal,
    f21dg_f21_distress_going_concern_x4_21d_slope_v008_signal,
    f21dg_f21_distress_going_concern_x5_21d_slope_v009_signal,
    f21dg_f21_distress_going_concern_eqassets_21d_slope_v010_signal,
    f21dg_f21_distress_going_concern_eqassets_63d_slope_v011_signal,
    f21dg_f21_distress_going_concern_lev_21d_slope_v012_signal,
    f21dg_f21_distress_going_concern_lev_63d_slope_v013_signal,
    f21dg_f21_distress_going_concern_netdebt_21d_slope_v014_signal,
    f21dg_f21_distress_going_concern_netcashsolv_21d_slope_v015_signal,
    f21dg_f21_distress_going_concern_cashassets_21d_slope_v016_signal,
    f21dg_f21_distress_going_concern_cashcover_21d_slope_v017_signal,
    f21dg_f21_distress_going_concern_revcover_21d_slope_v018_signal,
    f21dg_f21_distress_going_concern_ebitmargin_21d_slope_v019_signal,
    f21dg_f21_distress_going_concern_ebitliab_21d_slope_v020_signal,
    f21dg_f21_distress_going_concern_ebiteq_21d_slope_v021_signal,
    f21dg_f21_distress_going_concern_reeq_21d_slope_v022_signal,
    f21dg_f21_distress_going_concern_netdebteq_21d_slope_v023_signal,
    f21dg_f21_distress_going_concern_eqcap_21d_slope_v024_signal,
    f21dg_f21_distress_going_concern_altzz_21d_slope_v025_signal,
    f21dg_f21_distress_going_concern_altzrank_21d_slope_v026_signal,
    f21dg_f21_distress_going_concern_eqassetsz_21d_slope_v027_signal,
    f21dg_f21_distress_going_concern_levz_21d_slope_v028_signal,
    f21dg_f21_distress_going_concern_x3rank_21d_slope_v029_signal,
    f21dg_f21_distress_going_concern_x4rank_21d_slope_v030_signal,
    f21dg_f21_distress_going_concern_zonegap_21d_slope_v031_signal,
    f21dg_f21_distress_going_concern_deficit_21d_slope_v032_signal,
    f21dg_f21_distress_going_concern_wcshort_21d_slope_v033_signal,
    f21dg_f21_distress_going_concern_solvshort_21d_slope_v034_signal,
    f21dg_f21_distress_going_concern_netcashsolv_63d_slope_v035_signal,
    f21dg_f21_distress_going_concern_survbuffer_21d_slope_v036_signal,
    f21dg_f21_distress_going_concern_gcmag_21d_slope_v037_signal,
    f21dg_f21_distress_going_concern_x3contrib_21d_slope_v038_signal,
    f21dg_f21_distress_going_concern_netdebtz_21d_slope_v039_signal,
    f21dg_f21_distress_going_concern_reveq_21d_slope_v040_signal,
    f21dg_f21_distress_going_concern_wcliab_21d_slope_v041_signal,
    f21dg_f21_distress_going_concern_cashoblig_21d_slope_v042_signal,
    f21dg_f21_distress_going_concern_ebitmarginz_21d_slope_v043_signal,
    f21dg_f21_distress_going_concern_x2z_21d_slope_v044_signal,
    f21dg_f21_distress_going_concern_x5z_21d_slope_v045_signal,
    f21dg_f21_distress_going_concern_netcashcov_21d_slope_v046_signal,
    f21dg_f21_distress_going_concern_solvdefspr_21d_slope_v047_signal,
    f21dg_f21_distress_going_concern_liqlevspr_21d_slope_v048_signal,
    f21dg_f21_distress_going_concern_x3z_21d_slope_v049_signal,
    f21dg_f21_distress_going_concern_x4z_21d_slope_v050_signal,
    f21dg_f21_distress_going_concern_altz_5d_slope_v051_signal,
    f21dg_f21_distress_going_concern_eqassets_5d_slope_v052_signal,
    f21dg_f21_distress_going_concern_lev_5d_slope_v053_signal,
    f21dg_f21_distress_going_concern_x3_5d_slope_v054_signal,
    f21dg_f21_distress_going_concern_cashassets_5d_slope_v055_signal,
    f21dg_f21_distress_going_concern_netdebt_63d_slope_v056_signal,
    f21dg_f21_distress_going_concern_cashcover_63d_slope_v057_signal,
    f21dg_f21_distress_going_concern_ebitmargin_63d_slope_v058_signal,
    f21dg_f21_distress_going_concern_revcover_63d_slope_v059_signal,
    f21dg_f21_distress_going_concern_x1_63d_slope_v060_signal,
    f21dg_f21_distress_going_concern_x2_63d_slope_v061_signal,
    f21dg_f21_distress_going_concern_x4_63d_slope_v062_signal,
    f21dg_f21_distress_going_concern_x5_63d_slope_v063_signal,
    f21dg_f21_distress_going_concern_netcashsolv_5d_slope_v064_signal,
    f21dg_f21_distress_going_concern_ebiteq_63d_slope_v065_signal,
    f21dg_f21_distress_going_concern_reeq_63d_slope_v066_signal,
    f21dg_f21_distress_going_concern_survbuffer_63d_slope_v067_signal,
    f21dg_f21_distress_going_concern_zminerz_21d_slope_v068_signal,
    f21dg_f21_distress_going_concern_zcompdisp_21d_slope_v069_signal,
    f21dg_f21_distress_going_concern_altzsm_21d_slope_v070_signal,
    f21dg_f21_distress_going_concern_levsm_21d_slope_v071_signal,
    f21dg_f21_distress_going_concern_cashcoversm_21d_slope_v072_signal,
    f21dg_f21_distress_going_concern_zonegap_63d_slope_v073_signal,
    f21dg_f21_distress_going_concern_deficit_63d_slope_v074_signal,
    f21dg_f21_distress_going_concern_solvshort_63d_slope_v075_signal,
    f21dg_f21_distress_going_concern_altz_126d_slope_v076_signal,
    f21dg_f21_distress_going_concern_eqassets_126d_slope_v077_signal,
    f21dg_f21_distress_going_concern_lev_126d_slope_v078_signal,
    f21dg_f21_distress_going_concern_x3_126d_slope_v079_signal,
    f21dg_f21_distress_going_concern_x4_126d_slope_v080_signal,
    f21dg_f21_distress_going_concern_altz_42d_slope_v081_signal,
    f21dg_f21_distress_going_concern_eqassets_42d_slope_v082_signal,
    f21dg_f21_distress_going_concern_lev_42d_slope_v083_signal,
    f21dg_f21_distress_going_concern_cashassets_42d_slope_v084_signal,
    f21dg_f21_distress_going_concern_ebitliab_42d_slope_v085_signal,
    f21dg_f21_distress_going_concern_x1_42d_slope_v086_signal,
    f21dg_f21_distress_going_concern_x2_42d_slope_v087_signal,
    f21dg_f21_distress_going_concern_netdebt_42d_slope_v088_signal,
    f21dg_f21_distress_going_concern_ebitmargin_42d_slope_v089_signal,
    f21dg_f21_distress_going_concern_revcover_42d_slope_v090_signal,
    f21dg_f21_distress_going_concern_zdd_21d_slope_v091_signal,
    f21dg_f21_distress_going_concern_eqdd_21d_slope_v092_signal,
    f21dg_f21_distress_going_concern_zrecov_21d_slope_v093_signal,
    f21dg_f21_distress_going_concern_levrunup_21d_slope_v094_signal,
    f21dg_f21_distress_going_concern_minz_63d_slope_v095_signal,
    f21dg_f21_distress_going_concern_maxlev_63d_slope_v096_signal,
    f21dg_f21_distress_going_concern_revdd_21d_slope_v097_signal,
    f21dg_f21_distress_going_concern_cashdd_21d_slope_v098_signal,
    f21dg_f21_distress_going_concern_netcashdd_21d_slope_v099_signal,
    f21dg_f21_distress_going_concern_gcXlev_21d_slope_v100_signal,
    f21dg_f21_distress_going_concern_ztermspr_21d_slope_v101_signal,
    f21dg_f21_distress_going_concern_levtermspr_21d_slope_v102_signal,
    f21dg_f21_distress_going_concern_zdisp_21d_slope_v103_signal,
    f21dg_f21_distress_going_concern_eqdisp_21d_slope_v104_signal,
    f21dg_f21_distress_going_concern_cashcoverdisp_21d_slope_v105_signal,
    f21dg_f21_distress_going_concern_zvol_63d_slope_v106_signal,
    f21dg_f21_distress_going_concern_levvol_63d_slope_v107_signal,
    f21dg_f21_distress_going_concern_x3vol_63d_slope_v108_signal,
    f21dg_f21_distress_going_concern_eqcv_63d_slope_v109_signal,
    f21dg_f21_distress_going_concern_netdebteq_63d_slope_v110_signal,
    f21dg_f21_distress_going_concern_distresstime_21d_slope_v111_signal,
    f21dg_f21_distress_going_concern_gcbreadth_21d_slope_v112_signal,
    f21dg_f21_distress_going_concern_levspiketime_21d_slope_v113_signal,
    f21dg_f21_distress_going_concern_shortfallsum_21d_slope_v114_signal,
    f21dg_f21_distress_going_concern_zombie_21d_slope_v115_signal,
    f21dg_f21_distress_going_concern_eqerosXlev_21d_slope_v116_signal,
    f21dg_f21_distress_going_concern_lossXlev_21d_slope_v117_signal,
    f21dg_f21_distress_going_concern_cashsurv_21d_slope_v118_signal,
    f21dg_f21_distress_going_concern_gcoverall_21d_slope_v119_signal,
    f21dg_f21_distress_going_concern_insolXlev_21d_slope_v120_signal,
    f21dg_f21_distress_going_concern_x1sm_63d_slope_v121_signal,
    f21dg_f21_distress_going_concern_x3sm_63d_slope_v122_signal,
    f21dg_f21_distress_going_concern_ebiteqrank_63d_slope_v123_signal,
    f21dg_f21_distress_going_concern_reeqrank_63d_slope_v124_signal,
    f21dg_f21_distress_going_concern_netdebtz_63d_slope_v125_signal,
    f21dg_f21_distress_going_concern_x5lvl_21d_slope_v126_signal,
    f21dg_f21_distress_going_concern_wcliab_63d_slope_v127_signal,
    f21dg_f21_distress_going_concern_eqcap_63d_slope_v128_signal,
    f21dg_f21_distress_going_concern_ebitmarginrank_63d_slope_v129_signal,
    f21dg_f21_distress_going_concern_zminerrank_63d_slope_v130_signal,
    f21dg_f21_distress_going_concern_zspread_21d_slope_v131_signal,
    f21dg_f21_distress_going_concern_cashoblig_63d_slope_v132_signal,
    f21dg_f21_distress_going_concern_wcoblig_21d_slope_v133_signal,
    f21dg_f21_distress_going_concern_netcashcovz_21d_slope_v134_signal,
    f21dg_f21_distress_going_concern_revcoverz_21d_slope_v135_signal,
    f21dg_f21_distress_going_concern_ebitliabz_21d_slope_v136_signal,
    f21dg_f21_distress_going_concern_defpress_63d_slope_v137_signal,
    f21dg_f21_distress_going_concern_ebiteros_21d_slope_v138_signal,
    f21dg_f21_distress_going_concern_reeros_21d_slope_v139_signal,
    f21dg_f21_distress_going_concern_eqrecov_21d_slope_v140_signal,
    f21dg_f21_distress_going_concern_distdistance_21d_slope_v141_signal,
    f21dg_f21_distress_going_concern_netdebteqrank_63d_slope_v142_signal,
    f21dg_f21_distress_going_concern_reveq_63d_slope_v143_signal,
    f21dg_f21_distress_going_concern_cashassetsz_21d_slope_v144_signal,
    f21dg_f21_distress_going_concern_ebitmarginsm_21d_slope_v145_signal,
    f21dg_f21_distress_going_concern_netdebtsm_21d_slope_v146_signal,
    f21dg_f21_distress_going_concern_solvdefspr_63d_slope_v147_signal,
    f21dg_f21_distress_going_concern_gcXlev_63d_slope_v148_signal,
    f21dg_f21_distress_going_concern_netcashsolv_42d_slope_v149_signal,
    f21dg_f21_distress_going_concern_gcoverall_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_DISTRESS_GOING_CONCERN_REGISTRY_SLOPE_001_150 = REGISTRY


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

    print("OK f21_distress_going_concern_2nd_derivatives_001_150_claude: %d features pass" % n_features)
