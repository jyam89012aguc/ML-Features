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
# Altman-Z components (miner-adapted, book-value forms)
def _f21_x1(workingcapital, assets):
    # working capital / total assets (liquidity buffer)
    return workingcapital / assets.replace(0, np.nan)


def _f21_x2(retearn, assets):
    # retained earnings / total assets (accumulated-deficit drag)
    return retearn / assets.replace(0, np.nan)


def _f21_x3(ebit, assets):
    # EBIT / total assets (operating return on assets)
    return ebit / assets.replace(0, np.nan)


def _f21_x4(equity, liabilities):
    # book equity / total liabilities (solvency cushion)
    return equity / liabilities.replace(0, np.nan)


def _f21_x5(revenue, assets):
    # sales / total assets (asset turnover)
    return revenue / assets.replace(0, np.nan)


def _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    # Altman Z'' private-firm style composite, miner-adapted (book equity for X4)
    x1 = workingcapital / assets.replace(0, np.nan)
    x2 = retearn / assets.replace(0, np.nan)
    x3 = ebit / assets.replace(0, np.nan)
    x4 = equity / liabilities.replace(0, np.nan)
    x5 = revenue / assets.replace(0, np.nan)
    return 0.717 * x1 + 0.847 * x2 + 3.107 * x3 + 0.420 * x4 + 0.998 * x5


def _f21_zminer(workingcapital, retearn, ebit, equity, liabilities, assets):
    # miner-adapted Z (no-revenue explorers): drop turnover, lean on solvency+deficit
    x1 = workingcapital / assets.replace(0, np.nan)
    x2 = retearn / assets.replace(0, np.nan)
    x3 = ebit / assets.replace(0, np.nan)
    x4 = equity / liabilities.replace(0, np.nan)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def _f21_weak(ratio, w, q):
    # going-concern weakness indicator: ratio sitting in the bottom q-quantile of its
    # own trailing-w history (relative deterioration; absolute-sign-agnostic so it is
    # robust to miners that are chronically loss-making vs episodically distressed)
    thr = ratio.rolling(w, min_periods=max(1, w // 2)).quantile(q)
    return (ratio <= thr).astype(float)


def _f21_below_med(ratio, w):
    # shortfall depth below the ratio's own trailing-w median (>=0)
    med = ratio.rolling(w, min_periods=max(1, w // 2)).median()
    return (med - ratio).clip(lower=0)


# ============================================================
# --- ALTMAN-Z COMPONENTS (levels) ---
# X1: working-capital / assets (liquidity buffer level)
def f21dg_f21_distress_going_concern_x1wc_63d_base_v001_signal(workingcapital, assets):
    b = _f21_x1(workingcapital, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X2: retained-earnings / assets (accumulated-deficit drag level)
def f21dg_f21_distress_going_concern_x2re_63d_base_v002_signal(retearn, assets):
    b = _f21_x2(retearn, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X3: EBIT / assets (operating return on assets level)
def f21dg_f21_distress_going_concern_x3ebit_63d_base_v003_signal(ebit, assets):
    b = _f21_x3(ebit, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X4: book equity / liabilities (solvency cushion level)
def f21dg_f21_distress_going_concern_x4eq_63d_base_v004_signal(equity, liabilities):
    b = _f21_x4(equity, liabilities)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X5: revenue / assets (asset turnover level)
def f21dg_f21_distress_going_concern_x5rev_63d_base_v005_signal(revenue, assets):
    b = _f21_x5(revenue, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ALTMAN Z COMPOSITE (level / smoothed / z / rank) ---
# Altman Z' composite level (overall distress score)
def f21dg_f21_distress_going_concern_altz_63d_base_v006_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    b = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman Z' smoothed over a quarter (persistent distress level)
def f21dg_f21_distress_going_concern_altzsm_63d_base_v007_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = z.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# miner-adapted Z, EBIT/solvency-weighted and z-scored vs 252d (no-revenue explorer distress regime)
def f21dg_f21_distress_going_concern_zminer_63d_base_v008_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    # emphasise operating return and solvency cushion (de-emphasise the wc/assets term that
    # dominates the raw composite) so this is structurally distinct from X1-level features
    x1 = workingcapital / assets.replace(0, np.nan)
    x3 = ebit / assets.replace(0, np.nan)
    x4 = equity / liabilities.replace(0, np.nan)
    x2 = retearn / assets.replace(0, np.nan)
    raw = 1.0 * x1 + 4.0 * x2 + 10.0 * x3 + 3.0 * x4
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman Z' z-scored vs its own 252d history (de-trended distress regime)
def f21dg_f21_distress_going_concern_altzz_252d_base_v009_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _z(z, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman Z' percentile-rank vs its own 504d history (where in distress band)
def f21dg_f21_distress_going_concern_altzrank_504d_base_v010_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _rank(z, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman-Z shortfall below its own 252d rolling 60th-percentile (relative distress-zone depth)
def f21dg_f21_distress_going_concern_altzgap_63d_base_v011_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    thr = z.rolling(252, min_periods=126).quantile(0.60)
    b = (thr - z).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman-Z deterioration acceleration: tanh of the second difference of Z (distress speeding up)
def f21dg_f21_distress_going_concern_altztanh_63d_base_v012_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    accel = z - 2.0 * z.shift(63) + z.shift(126)
    b = np.tanh(3.0 * accel)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- NEGATIVE-EQUITY FLAG / SOLVENCY ---
# weak-solvency-flag prevalence over a quarter blended with equity-erosion depth (count-friendly)
def f21dg_f21_distress_going_concern_negeqflag_63d_base_v013_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    prev = _f21_weak(r, 504, 0.20).rolling(63, min_periods=21).mean()
    b = prev + 3.0 * _f21_below_med(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year solvency sat in its weakest historical quintile (chronic insolvency time)
def f21dg_f21_distress_going_concern_negeqtime_252d_base_v014_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    weak = _f21_weak(r, 504, 0.20)
    b = weak.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity / assets (book solvency ratio, distance to zero equity)
def f21dg_f21_distress_going_concern_eqassets_63d_base_v015_signal(equity, assets):
    b = equity / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities / assets (leverage; >1 = insolvent balance sheet)
def f21dg_f21_distress_going_concern_liabassets_63d_base_v016_signal(liabilities, assets):
    b = liabilities / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets z-scored vs 252d (solvency regime shift)
def f21dg_f21_distress_going_concern_eqassetsz_252d_base_v017_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity drawdown from its trailing 252d peak (book-value erosion depth)
def f21dg_f21_distress_going_concern_eqdd_252d_base_v018_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    peak = _rmax(r, 252)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of equity/assets below its own 252d median (solvency shortfall)
def f21dg_f21_distress_going_concern_eqshortfall_252d_base_v019_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    med = r.rolling(252, min_periods=126).median()
    b = (med - r).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- NEGATIVE RETAINED EARNINGS / ACCUMULATED DEFICIT ---
# accumulated-deficit-flag prevalence over a quarter blended with deficit-erosion depth (count-friendly)
def f21dg_f21_distress_going_concern_negreflag_63d_base_v020_signal(retearn, assets):
    r = retearn / assets.replace(0, np.nan)
    prev = _f21_weak(r, 504, 0.20).rolling(63, min_periods=21).mean()
    b = prev + 2.0 * _f21_below_med(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year retained-earnings sat in its weakest historical quintile (chronic-loss memory)
def f21dg_f21_distress_going_concern_negretime_252d_base_v021_signal(retearn, assets):
    r = retearn / assets.replace(0, np.nan)
    weak = _f21_weak(r, 504, 0.20)
    b = weak.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulated-deficit pressure: mean magnitude of quarterly declines in retained-earnings/assets
def f21dg_f21_distress_going_concern_deficitdepth_63d_base_v022_signal(retearn, assets):
    r = retearn / assets.replace(0, np.nan)
    declines = (r.shift(21) - r).clip(lower=0)
    b = declines.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings/assets drawdown from 252d peak (deficit deepening depth)
def f21dg_f21_distress_going_concern_redd_252d_base_v023_signal(retearn, assets):
    r = retearn / assets.replace(0, np.nan)
    peak = _rmax(r, 252)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deficit burden on capital: retained-earnings erosion (below 252d peak) scaled by equity
def f21dg_f21_distress_going_concern_deficitvseq_63d_base_v024_signal(retearn, equity):
    peak = _rmax(retearn, 252)
    erosion = (peak - retearn).clip(lower=0)
    b = erosion / equity.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings/assets percentile-rank vs 504d (deficit percentile position)
def f21dg_f21_distress_going_concern_rerank_504d_base_v025_signal(retearn, assets):
    r = retearn / assets.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- WORKING-CAPITAL DISTRESS ---
# working-capital-squeeze-flag prevalence over a month blended with squeeze depth (count-friendly)
def f21dg_f21_distress_going_concern_negwcflag_21d_base_v026_signal(workingcapital, assets):
    r = workingcapital / assets.replace(0, np.nan)
    prev = _f21_weak(r, 252, 0.25).rolling(21, min_periods=10).mean()
    b = prev + 4.0 * _f21_below_med(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year working-capital sat in its weakest historical quartile (chronic squeeze)
def f21dg_f21_distress_going_concern_negwctime_252d_base_v027_signal(workingcapital, assets):
    r = workingcapital / assets.replace(0, np.nan)
    weak = _f21_weak(r, 504, 0.25)
    b = weak.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / liabilities (short-term cover of obligations)
def f21dg_f21_distress_going_concern_wcliab_63d_base_v028_signal(workingcapital, liabilities):
    b = workingcapital / liabilities.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X1 (wc/assets) z-scored vs 252d (liquidity-buffer regime shift)
def f21dg_f21_distress_going_concern_x1z_252d_base_v029_signal(workingcapital, assets):
    r = _f21_x1(workingcapital, assets)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets instability: rolling dispersion of the liquidity buffer (erratic liquidity)
def f21dg_f21_distress_going_concern_x1shortfall_252d_base_v030_signal(workingcapital, assets):
    r = _f21_x1(workingcapital, assets)
    b = r.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EBIT / OPERATING DISTRESS ---
# operating-weakness-flag prevalence over a month blended with margin-erosion depth (count-friendly)
def f21dg_f21_distress_going_concern_negebitflag_21d_base_v031_signal(ebit, revenue):
    r = ebit / revenue.replace(0, np.nan)
    prev = _f21_weak(r, 252, 0.25).rolling(21, min_periods=10).mean()
    b = prev + 1.5 * _f21_below_med(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year EBIT/assets sat in its weakest historical quartile (operating-distress time)
def f21dg_f21_distress_going_concern_negebittime_252d_base_v032_signal(ebit, assets):
    r = ebit / assets.replace(0, np.nan)
    weak = _f21_weak(r, 504, 0.25)
    b = weak.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT / liabilities (operating coverage of obligations)
def f21dg_f21_distress_going_concern_ebitliab_63d_base_v033_signal(ebit, liabilities):
    b = ebit / liabilities.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# X3 (ebit/assets) percentile-rank vs 504d (operating-return percentile)
def f21dg_f21_distress_going_concern_x3rank_504d_base_v034_signal(ebit, assets):
    r = _f21_x3(ebit, assets)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-loss depth: EBIT-margin erosion below its 252d peak (deteriorating operations)
def f21dg_f21_distress_going_concern_ebitlossdepth_63d_base_v035_signal(ebit, revenue):
    m = ebit / revenue.replace(0, np.nan)
    peak = _rmax(m, 252)
    b = (peak - m).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GOING-CONCERN DETERIORATION COMPOSITES ---
# going-concern composite: weak-channel count (vs own history) plus small dispersion jitter
def f21dg_f21_distress_going_concern_gccomposite_base_v036_signal(equity, retearn, ebit, workingcapital, liabilities):
    eql = equity / liabilities.replace(0, np.nan)
    rel = retearn / liabilities.replace(0, np.nan)
    ebl = ebit / liabilities.replace(0, np.nan)
    wcl = workingcapital / liabilities.replace(0, np.nan)
    cnt = (_f21_weak(eql, 252, 0.30) + _f21_weak(rel, 252, 0.30)
           + _f21_weak(ebl, 252, 0.30) + _f21_weak(wcl, 252, 0.30))
    jitter = pd.concat([_z(eql, 126), _z(rel, 126), _z(ebl, 126), _z(wcl, 126)], axis=1).std(axis=1)
    b = cnt + jitter
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed going-concern weak-channel tally over a quarter (persistent distress count)
def f21dg_f21_distress_going_concern_gctallysm_63d_base_v037_signal(equity, retearn, ebit, workingcapital, liabilities):
    f1 = _f21_weak(equity / liabilities.replace(0, np.nan), 504, 0.30)
    f2 = _f21_weak(retearn / liabilities.replace(0, np.nan), 504, 0.30)
    f3 = _f21_weak(ebit / liabilities.replace(0, np.nan), 504, 0.30)
    f4 = _f21_weak(workingcapital / liabilities.replace(0, np.nan), 504, 0.30)
    tally = f1 + f2 + f3 + f4
    b = tally.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted distress composite: solvency cushion minus deficit minus loss
def f21dg_f21_distress_going_concern_gcmagcomposite_63d_base_v038_signal(equity, retearn, ebit, assets):
    eqa = equity / assets.replace(0, np.nan)
    rea = retearn / assets.replace(0, np.nan)
    eba = ebit / assets.replace(0, np.nan)
    b = eqa + 0.5 * rea + eba
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# going-concern deterioration: change in the magnitude composite over a year
def f21dg_f21_distress_going_concern_gcdeterior_252d_base_v039_signal(equity, retearn, ebit, assets):
    eqa = equity / assets.replace(0, np.nan)
    rea = retearn / assets.replace(0, np.nan)
    eba = ebit / assets.replace(0, np.nan)
    comp = eqa + 0.5 * rea + eba
    b = comp - comp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-channel weak tally with deficit-erosion weighting (deepening going-concern)
def f21dg_f21_distress_going_concern_gcweighted_63d_base_v040_signal(equity, retearn, ebit, workingcapital, assets):
    flags = (_f21_weak(equity / assets.replace(0, np.nan), 252, 0.20)
             + _f21_weak(ebit / assets.replace(0, np.nan), 252, 0.20)
             + _f21_weak(workingcapital / assets.replace(0, np.nan), 252, 0.20))
    depth = _f21_below_med(retearn / assets.replace(0, np.nan), 252).rolling(63, min_periods=21).mean()
    b = flags + 8.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DISTRESS-QUARTER TALLY (count-friendly) ---
# count of fresh entries into Altman distress zone over last year (distress-onset tally)
def f21dg_f21_distress_going_concern_distressonset_252d_base_v041_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    indistress = (z < 1.1).astype(float)
    entries = ((indistress == 1) & (indistress.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 0.3 * indistress.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year inside the Altman distress zone (chronic-distress time)
def f21dg_f21_distress_going_concern_distresstime_252d_base_v042_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    indistress = (z < 1.1).astype(float)
    b = indistress.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distress-quarter tally with depth: time-in-zone blended with avg sub-threshold depth
def f21dg_f21_distress_going_concern_distressdepth_252d_base_v043_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    indistress = (z < 1.1).astype(float)
    frac = indistress.rolling(252, min_periods=126).mean()
    depth = (1.1 - z.clip(upper=1.1)).rolling(63, min_periods=21).mean()
    b = frac + 0.5 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of distinct weak distress channels currently tripped, smoothed (severity tally)
def f21dg_f21_distress_going_concern_severitytally_126d_base_v044_signal(equity, retearn, ebit, workingcapital, liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    insolvent = _f21_weak(-lev, 504, 0.25)
    negeq = _f21_weak(equity / assets.replace(0, np.nan), 504, 0.25)
    deficit = _f21_weak(retearn / assets.replace(0, np.nan), 504, 0.25)
    oploss = _f21_weak(ebit / assets.replace(0, np.nan), 504, 0.25)
    negwc = _f21_weak(workingcapital / assets.replace(0, np.nan), 504, 0.25)
    tally = insolvent + negeq + deficit + oploss + negwc
    b = tally.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Z-COMPONENT SPREADS / INTERACTIONS ---
# solvency-vs-deficit spread: X4 minus retained-earnings erosion drag (cushion net of deficit)
def f21dg_f21_distress_going_concern_solvdefspr_63d_base_v045_signal(equity, liabilities, retearn, assets):
    x4 = _f21_x4(equity, liabilities)
    defdrag = _f21_below_med(retearn / assets.replace(0, np.nan), 252)
    b = x4 - 12.0 * defdrag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage-of-liabilities deterioration: year-over-year decline in cashneq/liabilities
def f21dg_f21_distress_going_concern_liqlevspr_63d_base_v046_signal(cashneq, liabilities):
    cover = cashneq / liabilities.replace(0, np.nan)
    b = cover.shift(252) - cover
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-vs-deficit interaction: operating-return shortfall x deficit erosion (losing while in deficit)
def f21dg_f21_distress_going_concern_lossXdeficit_63d_base_v047_signal(ebit, retearn, assets):
    loss = _f21_below_med(_f21_x3(ebit, assets), 252)
    deficit = _f21_below_med(retearn / assets.replace(0, np.nan), 252)
    b = 50.0 * loss * deficit
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# insolvency-x-leverage interaction: solvency shortfall scaled by balance-sheet gearing
def f21dg_f21_distress_going_concern_insolXilliq_63d_base_v048_signal(equity, liabilities, assets):
    lowsolv = _f21_below_med(_f21_x4(equity, liabilities), 252)
    lev = liabilities / assets.replace(0, np.nan)
    b = lowsolv * lev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-coverage of liabilities (sales backing of obligations, low = distress)
def f21dg_f21_distress_going_concern_revcover_63d_base_v049_signal(revenue, liabilities):
    b = revenue / liabilities.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash backing of liabilities (cashneq/liabilities; thin cash = distress)
def f21dg_f21_distress_going_concern_cashcover_63d_base_v050_signal(cashneq, liabilities):
    b = cashneq / liabilities.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CASH-BACKED SOLVENCY ---
# cash / assets (treasury share of balance sheet)
def f21dg_f21_distress_going_concern_cashassets_63d_base_v051_signal(cashneq, assets):
    b = cashneq / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash solvency: (cashneq - liabilities) / assets (cash-adjusted solvency)
def f21dg_f21_distress_going_concern_netcashsolv_63d_base_v052_signal(cashneq, liabilities, assets):
    b = (cashneq - liabilities) / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets z-scored vs 252d (treasury-buffer regime)
def f21dg_f21_distress_going_concern_cashassetsz_252d_base_v053_signal(cashneq, assets):
    r = cashneq / assets.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-working-capital-erosion: treasury net of working-capital shortfall (below 252d peak)
def f21dg_f21_distress_going_concern_cashplugwc_63d_base_v054_signal(cashneq, workingcapital, assets):
    peak = _rmax(workingcapital, 252)
    wc_short = (peak - workingcapital).clip(lower=0)
    b = (cashneq - wc_short) / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TREND / DETERIORATION OF Z & COMPONENTS (base-level changes) ---
# Altman Z' trend over a quarter (improving/deteriorating distress)
def f21dg_f21_distress_going_concern_altztrend_63d_base_v055_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = z - z.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman Z' year-over-year change (cyclical distress shift)
def f21dg_f21_distress_going_concern_altzyoy_252d_base_v056_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = z - z.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency (equity/assets) trend over a quarter (capital-erosion velocity, base)
def f21dg_f21_distress_going_concern_eqtrend_63d_base_v057_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulated-deficit growth: year-over-year decline in retained-earnings/assets (deficit accumulation)
def f21dg_f21_distress_going_concern_defgrowth_252d_base_v058_signal(retearn, assets):
    r = retearn / assets.replace(0, np.nan)
    b = (r.shift(252) - r)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage (liabilities/assets) trend over a quarter (balance-sheet stress build, base)
def f21dg_f21_distress_going_concern_levtrend_63d_base_v059_signal(liabilities, assets):
    r = liabilities / assets.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MIN / WORST-CASE Z ---
# worst (min) Altman Z' over last half year (recent distress trough)
def f21dg_f21_distress_going_concern_minz_126d_base_v060_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _rmin(z, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman Z' drawdown from its 252d peak (loss of distress cushion)
def f21dg_f21_distress_going_concern_zdd_252d_base_v061_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    peak = _rmax(z, 252)
    b = z - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# miner-Z drawdown from its 252d peak (solvency-cushion erosion)
def f21dg_f21_distress_going_concern_zminerdd_252d_base_v062_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f21_zminer(workingcapital, retearn, ebit, equity, liabilities, assets)
    peak = _rmax(z, 252)
    b = z - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DISPERSION / VOLATILITY OF DISTRESS ---
# Altman Z' volatility over a year (erratic vs steady distress)
def f21dg_f21_distress_going_concern_zvol_252d_base_v063_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = z.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of equity/assets over a year (solvency instability)
def f21dg_f21_distress_going_concern_eqcv_252d_base_v064_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    m = _mean(r, 252)
    sd = _std(r, 252)
    b = sd / m.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of the five z-normalised Z components (which channel is the outlier driver of distress)
def f21dg_f21_distress_going_concern_zcompdisp_base_v065_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    x1 = _z(_f21_x1(workingcapital, assets), 252)
    x2 = _z(_f21_x2(retearn, assets), 252)
    x3 = _z(_f21_x3(ebit, assets), 252)
    x4 = _z(_f21_x4(equity, liabilities), 252)
    x5 = _z(_f21_x5(revenue, assets), 252)
    b = pd.concat([x1, x2, x3, x4, x5], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TERM-STRUCTURE / SHORT-vs-LONG OF Z ---
# short-vs-long Altman Z' ratio (recent distress vs structural distress)
def f21dg_f21_distress_going_concern_ztermratio_base_v066_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    short = z.rolling(63, min_periods=21).mean()
    long = z.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman Z' displacement: level minus its slow EMA (acute vs chronic distress)
def f21dg_f21_distress_going_concern_zdisp_63d_base_v067_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = z - z.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage term-ratio: short vs long liabilities/assets (deleveraging vs build)
def f21dg_f21_distress_going_concern_levtermratio_base_v068_signal(liabilities, assets):
    r = liabilities / assets.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIGN x MAGNITUDE / COMPRESSED FORMS ---
# net-cash-solvency drawdown from its 252d peak (erosion of cash-adjusted solvency cushion)
def f21dg_f21_distress_going_concern_netcashroot_63d_base_v069_signal(cashneq, liabilities, assets):
    r = (cashneq - liabilities) / assets.replace(0, np.nan)
    peak = _rmax(r, 252)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-equity leverage z-scored vs 252d (gearing-distress regime; distinct from raw X4 level)
def f21dg_f21_distress_going_concern_x4signlog_63d_base_v070_signal(equity, liabilities):
    de = liabilities / equity.abs().replace(0, np.nan)
    b = _z(de, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage run-up from its 252d trough (how far gearing has climbed off its low; distress build)
def f21dg_f21_distress_going_concern_levtanh_63d_base_v071_signal(liabilities, assets):
    lev = liabilities / assets.replace(0, np.nan)
    trough = _rmin(lev, 252)
    b = lev - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTEREST-COVERAGE-LIKE / REVENUE STRESS ---
# EBIT margin (ebit/revenue) as going-concern operating distress
def f21dg_f21_distress_going_concern_ebitmargin_63d_base_v072_signal(ebit, revenue):
    b = ebit / revenue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/assets percentile-rank vs 504d (asset-turnover distress percentile)
def f21dg_f21_distress_going_concern_x5rank_504d_base_v073_signal(revenue, assets):
    r = _f21_x5(revenue, assets)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MULTI-WINDOW DISPERSION / COMPOSITE DISTANCE ---
# Altman Z' disagreement across short/medium/long smoothing (distress disagreement)
def f21dg_f21_distress_going_concern_zwindowdisp_base_v074_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    a = z.rolling(63, min_periods=21).mean()
    b2 = z.rolling(126, min_periods=63).mean()
    c = z.rolling(252, min_periods=126).mean()
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite going-concern distance: distress-zone depth + insolvency rank + deficit drag
def f21dg_f21_distress_going_concern_gcdistance_base_v075_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f21_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    zonedepth = (1.1 - z).clip(lower=0)
    solvrank = 0.5 - _rank(equity / assets.replace(0, np.nan), 252)
    defdrag = _f21_below_med(retearn / assets.replace(0, np.nan), 252).rolling(63, min_periods=21).mean()
    b = zonedepth + solvrank + 8.0 * defdrag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21dg_f21_distress_going_concern_x1wc_63d_base_v001_signal,
    f21dg_f21_distress_going_concern_x2re_63d_base_v002_signal,
    f21dg_f21_distress_going_concern_x3ebit_63d_base_v003_signal,
    f21dg_f21_distress_going_concern_x4eq_63d_base_v004_signal,
    f21dg_f21_distress_going_concern_x5rev_63d_base_v005_signal,
    f21dg_f21_distress_going_concern_altz_63d_base_v006_signal,
    f21dg_f21_distress_going_concern_altzsm_63d_base_v007_signal,
    f21dg_f21_distress_going_concern_zminer_63d_base_v008_signal,
    f21dg_f21_distress_going_concern_altzz_252d_base_v009_signal,
    f21dg_f21_distress_going_concern_altzrank_504d_base_v010_signal,
    f21dg_f21_distress_going_concern_altzgap_63d_base_v011_signal,
    f21dg_f21_distress_going_concern_altztanh_63d_base_v012_signal,
    f21dg_f21_distress_going_concern_negeqflag_63d_base_v013_signal,
    f21dg_f21_distress_going_concern_negeqtime_252d_base_v014_signal,
    f21dg_f21_distress_going_concern_eqassets_63d_base_v015_signal,
    f21dg_f21_distress_going_concern_liabassets_63d_base_v016_signal,
    f21dg_f21_distress_going_concern_eqassetsz_252d_base_v017_signal,
    f21dg_f21_distress_going_concern_eqdd_252d_base_v018_signal,
    f21dg_f21_distress_going_concern_eqshortfall_252d_base_v019_signal,
    f21dg_f21_distress_going_concern_negreflag_63d_base_v020_signal,
    f21dg_f21_distress_going_concern_negretime_252d_base_v021_signal,
    f21dg_f21_distress_going_concern_deficitdepth_63d_base_v022_signal,
    f21dg_f21_distress_going_concern_redd_252d_base_v023_signal,
    f21dg_f21_distress_going_concern_deficitvseq_63d_base_v024_signal,
    f21dg_f21_distress_going_concern_rerank_504d_base_v025_signal,
    f21dg_f21_distress_going_concern_negwcflag_21d_base_v026_signal,
    f21dg_f21_distress_going_concern_negwctime_252d_base_v027_signal,
    f21dg_f21_distress_going_concern_wcliab_63d_base_v028_signal,
    f21dg_f21_distress_going_concern_x1z_252d_base_v029_signal,
    f21dg_f21_distress_going_concern_x1shortfall_252d_base_v030_signal,
    f21dg_f21_distress_going_concern_negebitflag_21d_base_v031_signal,
    f21dg_f21_distress_going_concern_negebittime_252d_base_v032_signal,
    f21dg_f21_distress_going_concern_ebitliab_63d_base_v033_signal,
    f21dg_f21_distress_going_concern_x3rank_504d_base_v034_signal,
    f21dg_f21_distress_going_concern_ebitlossdepth_63d_base_v035_signal,
    f21dg_f21_distress_going_concern_gccomposite_base_v036_signal,
    f21dg_f21_distress_going_concern_gctallysm_63d_base_v037_signal,
    f21dg_f21_distress_going_concern_gcmagcomposite_63d_base_v038_signal,
    f21dg_f21_distress_going_concern_gcdeterior_252d_base_v039_signal,
    f21dg_f21_distress_going_concern_gcweighted_63d_base_v040_signal,
    f21dg_f21_distress_going_concern_distressonset_252d_base_v041_signal,
    f21dg_f21_distress_going_concern_distresstime_252d_base_v042_signal,
    f21dg_f21_distress_going_concern_distressdepth_252d_base_v043_signal,
    f21dg_f21_distress_going_concern_severitytally_126d_base_v044_signal,
    f21dg_f21_distress_going_concern_solvdefspr_63d_base_v045_signal,
    f21dg_f21_distress_going_concern_liqlevspr_63d_base_v046_signal,
    f21dg_f21_distress_going_concern_lossXdeficit_63d_base_v047_signal,
    f21dg_f21_distress_going_concern_insolXilliq_63d_base_v048_signal,
    f21dg_f21_distress_going_concern_revcover_63d_base_v049_signal,
    f21dg_f21_distress_going_concern_cashcover_63d_base_v050_signal,
    f21dg_f21_distress_going_concern_cashassets_63d_base_v051_signal,
    f21dg_f21_distress_going_concern_netcashsolv_63d_base_v052_signal,
    f21dg_f21_distress_going_concern_cashassetsz_252d_base_v053_signal,
    f21dg_f21_distress_going_concern_cashplugwc_63d_base_v054_signal,
    f21dg_f21_distress_going_concern_altztrend_63d_base_v055_signal,
    f21dg_f21_distress_going_concern_altzyoy_252d_base_v056_signal,
    f21dg_f21_distress_going_concern_eqtrend_63d_base_v057_signal,
    f21dg_f21_distress_going_concern_defgrowth_252d_base_v058_signal,
    f21dg_f21_distress_going_concern_levtrend_63d_base_v059_signal,
    f21dg_f21_distress_going_concern_minz_126d_base_v060_signal,
    f21dg_f21_distress_going_concern_zdd_252d_base_v061_signal,
    f21dg_f21_distress_going_concern_zminerdd_252d_base_v062_signal,
    f21dg_f21_distress_going_concern_zvol_252d_base_v063_signal,
    f21dg_f21_distress_going_concern_eqcv_252d_base_v064_signal,
    f21dg_f21_distress_going_concern_zcompdisp_base_v065_signal,
    f21dg_f21_distress_going_concern_ztermratio_base_v066_signal,
    f21dg_f21_distress_going_concern_zdisp_63d_base_v067_signal,
    f21dg_f21_distress_going_concern_levtermratio_base_v068_signal,
    f21dg_f21_distress_going_concern_netcashroot_63d_base_v069_signal,
    f21dg_f21_distress_going_concern_x4signlog_63d_base_v070_signal,
    f21dg_f21_distress_going_concern_levtanh_63d_base_v071_signal,
    f21dg_f21_distress_going_concern_ebitmargin_63d_base_v072_signal,
    f21dg_f21_distress_going_concern_x5rank_504d_base_v073_signal,
    f21dg_f21_distress_going_concern_zwindowdisp_base_v074_signal,
    f21dg_f21_distress_going_concern_gcdistance_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_DISTRESS_GOING_CONCERN_REGISTRY_001_075 = REGISTRY


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

    # distress-prone miner balance sheet: equity/retearn/wc/ebit can swing negative;
    # assets/liabilities/revenue/cashneq strictly positive.
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

    print("OK f21_distress_going_concern_base_001_075_claude: %d features pass" % n_features)
