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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s vs time over window w (per-step), scaled by 1/level handled by caller
    idx = np.arange(w, dtype=float)
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        ym = a.mean()
        return float(((idx - xm) * (a - ym)).sum() / xden)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (reinvestment dynamics) =====
def _f27_capex_rev(capex, revenue):
    # capex intensity: how much of sales is plowed into fixed assets
    return capex / revenue.replace(0, np.nan)


def _f27_rnd_rev(rnd, revenue):
    # R&D intensity
    return rnd / revenue.replace(0, np.nan)


def _f27_sbc_rev(sbcomp, revenue):
    # stock-based-comp intensity
    return sbcomp / revenue.replace(0, np.nan)


def _f27_reinv_rate(capex, rnd, revenue):
    # reinvestment rate vs an OCF-proxy (revenue scaled) — total growth spend / sales
    return (capex + rnd) / revenue.replace(0, np.nan)


def _f27_growth_capex(capex, ppnenet):
    # capex relative to installed net PP&E (growth vs maintenance capex)
    return capex / ppnenet.replace(0, np.nan)


def _f27_rnd_assets(rnd, assets):
    # R&D relative to the asset base
    return rnd / assets.replace(0, np.nan)


def _f27_capex_assets(capex, assets):
    # capital intensity relative to assets
    return capex / assets.replace(0, np.nan)


def _f27_growth(s, w):
    # log growth of a (positive) fundamental over window w
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


# ============================================================
# capex/revenue level (52w smoothed intensity)
def f27ri_f27_reinvestment_dynamics_capexrev_252d_base_v001_signal(capex, revenue):
    b = _mean(_f27_capex_rev(capex, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue z-scored vs its own 504d history (de-trended intensity)
def f27ri_f27_reinvestment_dynamics_capexrevz_504d_base_v002_signal(capex, revenue):
    b = _z(_f27_capex_rev(capex, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue percentile-ranked vs its own 252d history
def f27ri_f27_reinvestment_dynamics_capexrevrank_252d_base_v003_signal(capex, revenue):
    b = _rank(_f27_capex_rev(capex, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity level (smoothed)
def f27ri_f27_reinvestment_dynamics_rndrev_252d_base_v004_signal(rnd, revenue):
    b = _mean(_f27_rnd_rev(rnd, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity z-scored vs own 504d history
def f27ri_f27_reinvestment_dynamics_rndrevz_504d_base_v005_signal(rnd, revenue):
    b = _z(_f27_rnd_rev(rnd, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity percentile-ranked vs own 252d history
def f27ri_f27_reinvestment_dynamics_rndrevrank_252d_base_v006_signal(rnd, revenue):
    b = _rank(_f27_rnd_rev(rnd, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC intensity level (smoothed)
def f27ri_f27_reinvestment_dynamics_sbcrev_252d_base_v007_signal(sbcomp, revenue):
    b = _mean(_f27_sbc_rev(sbcomp, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC intensity z-scored vs own 504d history
def f27ri_f27_reinvestment_dynamics_sbcrevz_504d_base_v008_signal(sbcomp, revenue):
    b = _z(_f27_sbc_rev(sbcomp, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate (capex+rnd)/revenue level (smoothed)
def f27ri_f27_reinvestment_dynamics_reinvrate_252d_base_v009_signal(capex, rnd, revenue):
    b = _mean(_f27_reinv_rate(capex, rnd, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate z-scored vs own 504d history
def f27ri_f27_reinvestment_dynamics_reinvratez_504d_base_v010_signal(capex, rnd, revenue):
    b = _z(_f27_reinv_rate(capex, rnd, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex (capex/ppnenet) level (smoothed)
def f27ri_f27_reinvestment_dynamics_growthcapex_252d_base_v011_signal(capex, ppnenet):
    b = _mean(_f27_growth_capex(capex, ppnenet), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex z-scored vs own 504d history
def f27ri_f27_reinvestment_dynamics_growthcapexz_504d_base_v012_signal(capex, ppnenet):
    b = _z(_f27_growth_capex(capex, ppnenet), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex percentile-ranked vs own 252d history
def f27ri_f27_reinvestment_dynamics_growthcapexrank_252d_base_v013_signal(capex, ppnenet):
    b = _rank(_f27_growth_capex(capex, ppnenet), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/assets level (smoothed)
def f27ri_f27_reinvestment_dynamics_rndassets_252d_base_v014_signal(rnd, assets):
    b = _mean(_f27_rnd_assets(rnd, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets level (smoothed)
def f27ri_f27_reinvestment_dynamics_capexassets_252d_base_v015_signal(capex, assets):
    b = _mean(_f27_capex_assets(capex, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth (252d log growth of rnd)
def f27ri_f27_reinvestment_dynamics_rndgrow_252d_base_v016_signal(rnd):
    b = _f27_growth(rnd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth over 126d
def f27ri_f27_reinvestment_dynamics_rndgrow_126d_base_v017_signal(rnd):
    b = _f27_growth(rnd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth (252d log growth)
def f27ri_f27_reinvestment_dynamics_capexgrow_252d_base_v018_signal(capex):
    b = _f27_growth(capex, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth minus revenue growth (reinvestment outpacing sales)
def f27ri_f27_reinvestment_dynamics_capexvsrevgrow_252d_base_v019_signal(capex, revenue):
    b = _f27_growth(capex, 252) - _f27_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth minus revenue growth (research outpacing sales)
def f27ri_f27_reinvestment_dynamics_rndvsrevgrow_252d_base_v020_signal(rnd, revenue):
    b = _f27_growth(rnd, 252) - _f27_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC growth minus revenue growth (comp dilution outpacing sales)
def f27ri_f27_reinvestment_dynamics_sbcvsrevgrow_252d_base_v021_signal(sbcomp, revenue):
    b = _f27_growth(sbcomp, 252) - _f27_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-mix: R&D share of total reinvestment (rnd/(capex+rnd))
def f27ri_f27_reinvestment_dynamics_rndmix_252d_base_v022_signal(capex, rnd):
    mix = rnd / (capex + rnd).replace(0, np.nan)
    b = _mean(mix, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-mix z-scored (shift between physical vs research spend)
def f27ri_f27_reinvestment_dynamics_rndmixz_504d_base_v023_signal(capex, rnd):
    mix = rnd / (capex + rnd).replace(0, np.nan)
    b = _z(mix, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-to-R&D ratio momentum (shift in asset-heavy vs research-heavy posture)
def f27ri_f27_reinvestment_dynamics_capexrnd_252d_base_v024_signal(capex, rnd):
    ratio = np.log(capex.replace(0, np.nan) / rnd.replace(0, np.nan))
    b = ratio - ratio.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total reinvestment intensity incl SBC: (capex+rnd+sbcomp)/revenue
def f27ri_f27_reinvestment_dynamics_totinv_252d_base_v025_signal(capex, rnd, sbcomp, revenue):
    tot = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = _mean(tot, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total reinvestment intensity z-scored vs own history
def f27ri_f27_reinvestment_dynamics_totinvz_504d_base_v026_signal(capex, rnd, sbcomp, revenue):
    tot = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    b = _z(tot, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment trend: 126d OLS slope of capex/revenue, scaled by its level
def f27ri_f27_reinvestment_dynamics_capexrevtrend_126d_base_v027_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    sl = _slope(ci, 126)
    b = sl / _mean(ci, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-intensity trend: 126d OLS slope of rnd/revenue scaled by level
def f27ri_f27_reinvestment_dynamics_rndrevtrend_126d_base_v028_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    sl = _slope(ri, 126)
    b = sl / _mean(ri, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex trend: 126d slope of capex/ppnenet scaled by level
def f27ri_f27_reinvestment_dynamics_growthcapextrend_126d_base_v029_signal(capex, ppnenet):
    gc = _f27_growth_capex(capex, ppnenet)
    sl = _slope(gc, 126)
    b = sl / _mean(gc, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate trend: 252d slope of (capex+rnd)/revenue scaled by level
def f27ri_f27_reinvestment_dynamics_reinvratetrend_252d_base_v030_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    sl = _slope(rr, 252)
    b = sl / _mean(rr, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue dispersion (instability of investment intensity over 252d)
def f27ri_f27_reinvestment_dynamics_capexrevdisp_252d_base_v031_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    b = _std(ci, 252) / _mean(ci, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity dispersion (research-spend stability)
def f27ri_f27_reinvestment_dynamics_rndrevdisp_252d_base_v032_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    b = _std(ri, 252) / _mean(ri, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate dispersion (capex+rnd)/revenue volatility
def f27ri_f27_reinvestment_dynamics_reinvratedisp_252d_base_v033_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    b = _std(rr, 252) / _mean(rr, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC intensity dispersion
def f27ri_f27_reinvestment_dynamics_sbcrevdisp_252d_base_v034_signal(sbcomp, revenue):
    si = _f27_sbc_rev(sbcomp, revenue)
    b = _std(si, 252) / _mean(si, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity acceleration: 63d change of capex/revenue relative to its dispersion
def f27ri_f27_reinvestment_dynamics_capexrevmom_252d_base_v035_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    chg = ci - ci.shift(63)
    b = chg / _std(ci, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-intensity acceleration: 63d change of rnd/revenue relative to its dispersion
def f27ri_f27_reinvestment_dynamics_rndrevmom_252d_base_v036_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    chg = ri - ri.shift(63)
    b = chg / _std(ri, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex momentum: capex/ppnenet change over a year
def f27ri_f27_reinvestment_dynamics_growthcapexmom_252d_base_v037_signal(capex, ppnenet):
    gc = _f27_growth_capex(capex, ppnenet)
    b = gc - gc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment efficiency: revenue growth per unit of reinvestment intensity
def f27ri_f27_reinvestment_dynamics_reinveff_252d_base_v038_signal(capex, rnd, revenue):
    rr = _mean(_f27_reinv_rate(capex, rnd, revenue), 252)
    g = _f27_growth(revenue, 252)
    b = g / rr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex efficiency rank: percentile of revenue-growth-per-capex/rev vs own 504d history
def f27ri_f27_reinvestment_dynamics_capexeff_252d_base_v039_signal(capex, revenue):
    ci = _mean(_f27_capex_rev(capex, revenue), 252)
    g = _f27_growth(revenue, 252)
    eff = g / ci.replace(0, np.nan)
    b = _rank(eff, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D efficiency level minus capex efficiency level (which dollar reinvests harder)
def f27ri_f27_reinvestment_dynamics_rndeff_252d_base_v040_signal(rnd, revenue, capex):
    ri = _mean(_f27_rnd_rev(rnd, revenue), 252)
    ci = _mean(_f27_capex_rev(capex, revenue), 252)
    g = _f27_growth(revenue, 252)
    b = g / ri.replace(0, np.nan) - g / ci.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex level log-growth (raw investment scaling, 126d)
def f27ri_f27_reinvestment_dynamics_capexgrow_126d_base_v041_signal(capex):
    b = _f27_growth(capex, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC growth (252d log growth, dilution trajectory)
def f27ri_f27_reinvestment_dynamics_sbcgrow_252d_base_v042_signal(sbcomp):
    b = _f27_growth(sbcomp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet growth (asset-base expansion from cumulative reinvestment)
def f27ri_f27_reinvestment_dynamics_ppnegrow_252d_base_v043_signal(ppnenet):
    b = _f27_growth(ppnenet, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net capex over ppnenet minus its own 252d depreciation proxy slope (capex above replacement)
def f27ri_f27_reinvestment_dynamics_netgrowthcapex_252d_base_v044_signal(capex, ppnenet):
    gc = _f27_growth_capex(capex, ppnenet)
    b = gc - gc.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity vs assets: (capex+rnd)/assets level
def f27ri_f27_reinvestment_dynamics_reinvassets_252d_base_v045_signal(capex, rnd, assets):
    ra = (capex + rnd) / assets.replace(0, np.nan)
    b = _mean(ra, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity vs assets z-scored
def f27ri_f27_reinvestment_dynamics_reinvassetsz_504d_base_v046_signal(capex, rnd, assets):
    ra = (capex + rnd) / assets.replace(0, np.nan)
    b = _z(ra, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC/assets year-over-year change (equity-comp dilution drift vs asset base)
def f27ri_f27_reinvestment_dynamics_sbcassets_252d_base_v047_signal(sbcomp, assets):
    sa = sbcomp / assets.replace(0, np.nan)
    b = sa - sa.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue minus R&D/revenue (tilt toward physical vs intangible reinvestment)
def f27ri_f27_reinvestment_dynamics_invtilt_252d_base_v048_signal(capex, rnd, revenue):
    tilt = _f27_capex_rev(capex, revenue) - _f27_rnd_rev(rnd, revenue)
    b = _mean(tilt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investment-tilt z-scored (regime shift in reinvestment composition)
def f27ri_f27_reinvestment_dynamics_invtiltz_504d_base_v049_signal(capex, rnd, revenue):
    tilt = _f27_capex_rev(capex, revenue) - _f27_rnd_rev(rnd, revenue)
    b = _z(tilt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment acceleration: reinvestment rate now vs a year ago, signed-sqrt squashed
def f27ri_f27_reinvestment_dynamics_reinvaccel_252d_base_v050_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    chg = rr - rr.shift(252)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-intensity hit-rate: fraction of last year R&D/rev rose, minus capex/rev hit-rate
def f27ri_f27_reinvestment_dynamics_rndhit_252d_base_v051_signal(rnd, revenue, capex):
    ri = _f27_rnd_rev(rnd, revenue)
    ci = _f27_capex_rev(capex, revenue)
    up_r = (ri > ri.shift(21)).astype(float).rolling(252, min_periods=126).mean()
    up_c = (ci > ci.shift(21)).astype(float).rolling(252, min_periods=126).mean()
    b = up_r - up_c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity hit-rate: fraction of last year capex/rev rose vs prior month
def f27ri_f27_reinvestment_dynamics_capexhit_252d_base_v052_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    up = (ci > ci.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex EMA (persistent expansion posture)
def f27ri_f27_reinvestment_dynamics_growthcapexema_252d_base_v053_signal(capex, ppnenet):
    gc = _f27_growth_capex(capex, ppnenet)
    b = gc.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue displacement: level minus its slow EMA (acceleration above trend)
def f27ri_f27_reinvestment_dynamics_capexrevdisp_ema_base_v054_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    b = ci - ci.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity displacement vs slow EMA
def f27ri_f27_reinvestment_dynamics_rndrevdisp_ema_base_v055_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    b = ri - ri.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth: sign-of-growth times reinvestment-rate rank (durable funding)
def f27ri_f27_reinvestment_dynamics_reinvfunded_252d_base_v056_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    rr_rank = _rank(rr, 252)
    g = _f27_growth(revenue, 126)
    b = np.sign(g) * (rr_rank + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet vs capex/revenue spread, z-scored vs own 504d history (intensity-base gap)
def f27ri_f27_reinvestment_dynamics_capexbasespr_252d_base_v057_signal(capex, ppnenet, revenue):
    spr = _f27_growth_capex(capex, ppnenet) - _f27_capex_rev(capex, revenue)
    b = _z(spr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D growth acceleration: R&D 126d growth minus prior 126d growth
def f27ri_f27_reinvestment_dynamics_rndgrowaccel_126d_base_v058_signal(rnd):
    g = _f27_growth(rnd, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth acceleration
def f27ri_f27_reinvestment_dynamics_capexgrowaccel_126d_base_v059_signal(capex):
    g = _f27_growth(capex, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate quarterly-change rank vs own 504d history (momentum percentile)
def f27ri_f27_reinvestment_dynamics_reinvraterank_504d_base_v060_signal(capex, rnd, revenue):
    rr = _f27_reinv_rate(capex, rnd, revenue)
    chg = rr - rr.shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC intensity rank vs own 252d history
def f27ri_f27_reinvestment_dynamics_sbcrevrank_252d_base_v061_signal(sbcomp, revenue):
    b = _rank(_f27_sbc_rev(sbcomp, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/assets z-scored vs own history
def f27ri_f27_reinvestment_dynamics_rndassetsz_504d_base_v062_signal(rnd, assets):
    b = _z(_f27_rnd_assets(rnd, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets dispersion (capital-spend volatility vs asset base)
def f27ri_f27_reinvestment_dynamics_capexassetsdisp_252d_base_v063_signal(capex, assets):
    ca = _f27_capex_assets(capex, assets)
    b = _std(ca, 252) / _mean(ca, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment efficiency trend: 126d slope of (rev growth / reinvest rate)
def f27ri_f27_reinvestment_dynamics_reinvefftrend_126d_base_v064_signal(capex, rnd, revenue):
    rr = _mean(_f27_reinv_rate(capex, rnd, revenue), 126)
    g = _f27_growth(revenue, 126)
    eff = g / rr.replace(0, np.nan)
    b = _slope(eff, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total reinvestment (capex+rnd+sbc)/assets trend: 126d slope scaled by level
def f27ri_f27_reinvestment_dynamics_totinvassets_252d_base_v065_signal(capex, rnd, sbcomp, assets):
    tot = (capex + rnd + sbcomp) / assets.replace(0, np.nan)
    sl = _slope(tot, 126)
    b = sl / _mean(tot, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC vs capex spread trend: 126d slope of (sbc/rev - capex/rev) posture
def f27ri_f27_reinvestment_dynamics_sbccapexspr_252d_base_v066_signal(sbcomp, capex, revenue):
    spr = _f27_sbc_rev(sbcomp, revenue) - _f27_capex_rev(capex, revenue)
    b = _slope(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex per unit of reinvestment dispersion (smooth aggressive expansion)
def f27ri_f27_reinvestment_dynamics_growthcapexstab_252d_base_v067_signal(capex, ppnenet):
    gc = _f27_growth_capex(capex, ppnenet)
    lvl = _mean(gc, 252)
    disp = _std(gc, 252).replace(0, np.nan)
    b = lvl / disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D intensity per unit of its dispersion (steady research commitment)
def f27ri_f27_reinvestment_dynamics_rndstab_252d_base_v068_signal(rnd, revenue):
    ri = _f27_rnd_rev(rnd, revenue)
    lvl = _mean(ri, 252)
    disp = _std(ri, 252).replace(0, np.nan)
    b = lvl / disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity year-over-year second difference (changing direction of capex/rev)
def f27ri_f27_reinvestment_dynamics_capexrevyoy2_252d_base_v069_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    d1 = ci - ci.shift(252)
    b = d1 - d1.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment mix trend: 126d slope of rnd/(capex+rnd)
def f27ri_f27_reinvestment_dynamics_rndmixtrend_126d_base_v070_signal(capex, rnd):
    mix = rnd / (capex + rnd).replace(0, np.nan)
    b = _slope(mix, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment vs revenue interaction: reinvest rate x revenue rank (scale-weighted intensity)
def f27ri_f27_reinvestment_dynamics_reinvscale_252d_base_v071_signal(capex, rnd, revenue):
    rr = _mean(_f27_reinv_rate(capex, rnd, revenue), 252)
    rev_rank = _rank(revenue, 504)
    b = rr * (rev_rank + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage proxy: revenue per unit of capex (asset-light scaling)
def f27ri_f27_reinvestment_dynamics_capexcover_252d_base_v072_signal(capex, revenue):
    cover = revenue / capex.replace(0, np.nan)
    b = _z(cover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-burden momentum: 252d change of (capex+rnd+sbc)/revenue, ranked
def f27ri_f27_reinvestment_dynamics_totinvrank_504d_base_v073_signal(capex, rnd, sbcomp, revenue):
    tot = (capex + rnd + sbcomp) / revenue.replace(0, np.nan)
    chg = tot - tot.shift(252)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity convexity: distance of capex/rev from its 252d range midpoint
def f27ri_f27_reinvestment_dynamics_capexrevmid_252d_base_v074_signal(capex, revenue):
    ci = _f27_capex_rev(capex, revenue)
    hi = ci.rolling(252, min_periods=126).max()
    lo = ci.rolling(252, min_periods=126).min()
    mid = (hi + lo) / 2.0
    b = (ci - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-to-installed-base growth: capex/ppnenet interacted with ppnenet growth
def f27ri_f27_reinvestment_dynamics_basemom_252d_base_v075_signal(capex, ppnenet):
    gc = _mean(_f27_growth_capex(capex, ppnenet), 252)
    pg = _f27_growth(ppnenet, 252)
    b = gc * (1.0 + pg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27ri_f27_reinvestment_dynamics_capexrev_252d_base_v001_signal,
    f27ri_f27_reinvestment_dynamics_capexrevz_504d_base_v002_signal,
    f27ri_f27_reinvestment_dynamics_capexrevrank_252d_base_v003_signal,
    f27ri_f27_reinvestment_dynamics_rndrev_252d_base_v004_signal,
    f27ri_f27_reinvestment_dynamics_rndrevz_504d_base_v005_signal,
    f27ri_f27_reinvestment_dynamics_rndrevrank_252d_base_v006_signal,
    f27ri_f27_reinvestment_dynamics_sbcrev_252d_base_v007_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevz_504d_base_v008_signal,
    f27ri_f27_reinvestment_dynamics_reinvrate_252d_base_v009_signal,
    f27ri_f27_reinvestment_dynamics_reinvratez_504d_base_v010_signal,
    f27ri_f27_reinvestment_dynamics_growthcapex_252d_base_v011_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexz_504d_base_v012_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexrank_252d_base_v013_signal,
    f27ri_f27_reinvestment_dynamics_rndassets_252d_base_v014_signal,
    f27ri_f27_reinvestment_dynamics_capexassets_252d_base_v015_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow_252d_base_v016_signal,
    f27ri_f27_reinvestment_dynamics_rndgrow_126d_base_v017_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow_252d_base_v018_signal,
    f27ri_f27_reinvestment_dynamics_capexvsrevgrow_252d_base_v019_signal,
    f27ri_f27_reinvestment_dynamics_rndvsrevgrow_252d_base_v020_signal,
    f27ri_f27_reinvestment_dynamics_sbcvsrevgrow_252d_base_v021_signal,
    f27ri_f27_reinvestment_dynamics_rndmix_252d_base_v022_signal,
    f27ri_f27_reinvestment_dynamics_rndmixz_504d_base_v023_signal,
    f27ri_f27_reinvestment_dynamics_capexrnd_252d_base_v024_signal,
    f27ri_f27_reinvestment_dynamics_totinv_252d_base_v025_signal,
    f27ri_f27_reinvestment_dynamics_totinvz_504d_base_v026_signal,
    f27ri_f27_reinvestment_dynamics_capexrevtrend_126d_base_v027_signal,
    f27ri_f27_reinvestment_dynamics_rndrevtrend_126d_base_v028_signal,
    f27ri_f27_reinvestment_dynamics_growthcapextrend_126d_base_v029_signal,
    f27ri_f27_reinvestment_dynamics_reinvratetrend_252d_base_v030_signal,
    f27ri_f27_reinvestment_dynamics_capexrevdisp_252d_base_v031_signal,
    f27ri_f27_reinvestment_dynamics_rndrevdisp_252d_base_v032_signal,
    f27ri_f27_reinvestment_dynamics_reinvratedisp_252d_base_v033_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevdisp_252d_base_v034_signal,
    f27ri_f27_reinvestment_dynamics_capexrevmom_252d_base_v035_signal,
    f27ri_f27_reinvestment_dynamics_rndrevmom_252d_base_v036_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexmom_252d_base_v037_signal,
    f27ri_f27_reinvestment_dynamics_reinveff_252d_base_v038_signal,
    f27ri_f27_reinvestment_dynamics_capexeff_252d_base_v039_signal,
    f27ri_f27_reinvestment_dynamics_rndeff_252d_base_v040_signal,
    f27ri_f27_reinvestment_dynamics_capexgrow_126d_base_v041_signal,
    f27ri_f27_reinvestment_dynamics_sbcgrow_252d_base_v042_signal,
    f27ri_f27_reinvestment_dynamics_ppnegrow_252d_base_v043_signal,
    f27ri_f27_reinvestment_dynamics_netgrowthcapex_252d_base_v044_signal,
    f27ri_f27_reinvestment_dynamics_reinvassets_252d_base_v045_signal,
    f27ri_f27_reinvestment_dynamics_reinvassetsz_504d_base_v046_signal,
    f27ri_f27_reinvestment_dynamics_sbcassets_252d_base_v047_signal,
    f27ri_f27_reinvestment_dynamics_invtilt_252d_base_v048_signal,
    f27ri_f27_reinvestment_dynamics_invtiltz_504d_base_v049_signal,
    f27ri_f27_reinvestment_dynamics_reinvaccel_252d_base_v050_signal,
    f27ri_f27_reinvestment_dynamics_rndhit_252d_base_v051_signal,
    f27ri_f27_reinvestment_dynamics_capexhit_252d_base_v052_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexema_252d_base_v053_signal,
    f27ri_f27_reinvestment_dynamics_capexrevdisp_ema_base_v054_signal,
    f27ri_f27_reinvestment_dynamics_rndrevdisp_ema_base_v055_signal,
    f27ri_f27_reinvestment_dynamics_reinvfunded_252d_base_v056_signal,
    f27ri_f27_reinvestment_dynamics_capexbasespr_252d_base_v057_signal,
    f27ri_f27_reinvestment_dynamics_rndgrowaccel_126d_base_v058_signal,
    f27ri_f27_reinvestment_dynamics_capexgrowaccel_126d_base_v059_signal,
    f27ri_f27_reinvestment_dynamics_reinvraterank_504d_base_v060_signal,
    f27ri_f27_reinvestment_dynamics_sbcrevrank_252d_base_v061_signal,
    f27ri_f27_reinvestment_dynamics_rndassetsz_504d_base_v062_signal,
    f27ri_f27_reinvestment_dynamics_capexassetsdisp_252d_base_v063_signal,
    f27ri_f27_reinvestment_dynamics_reinvefftrend_126d_base_v064_signal,
    f27ri_f27_reinvestment_dynamics_totinvassets_252d_base_v065_signal,
    f27ri_f27_reinvestment_dynamics_sbccapexspr_252d_base_v066_signal,
    f27ri_f27_reinvestment_dynamics_growthcapexstab_252d_base_v067_signal,
    f27ri_f27_reinvestment_dynamics_rndstab_252d_base_v068_signal,
    f27ri_f27_reinvestment_dynamics_capexrevyoy2_252d_base_v069_signal,
    f27ri_f27_reinvestment_dynamics_rndmixtrend_126d_base_v070_signal,
    f27ri_f27_reinvestment_dynamics_reinvscale_252d_base_v071_signal,
    f27ri_f27_reinvestment_dynamics_capexcover_252d_base_v072_signal,
    f27ri_f27_reinvestment_dynamics_totinvrank_504d_base_v073_signal,
    f27ri_f27_reinvestment_dynamics_capexrevmid_252d_base_v074_signal,
    f27ri_f27_reinvestment_dynamics_basemom_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_REINVESTMENT_DYNAMICS_REGISTRY_001_075 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(101, base=1e9, drift=0.03, vol=0.04).rename("revenue")
    capex = _fund(102, base=8e7, drift=0.025, vol=0.06).rename("capex")
    rnd = _fund(103, base=6e7, drift=0.035, vol=0.07).rename("rnd")
    sbcomp = _fund(104, base=3e7, drift=0.04, vol=0.08).rename("sbcomp")
    assets = _fund(105, base=2e9, drift=0.02, vol=0.03).rename("assets")
    ppnenet = _fund(106, base=5e8, drift=0.02, vol=0.05).rename("ppnenet")

    cols = {"revenue": revenue, "capex": capex, "rnd": rnd,
            "sbcomp": sbcomp, "assets": assets, "ppnenet": ppnenet}

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

    print("OK f27_reinvestment_dynamics_base_001_075_claude: %d features pass" % n_features)
