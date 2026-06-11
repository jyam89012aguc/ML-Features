import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives: SBC dilution / overhang =====
def _sb_dilrate(sbcomp, marketcap):
    # SBC dilution rate: annual paper comp as a fraction of market value
    return _safe_div(sbcomp, marketcap)


def _sb_promote_opex(sbcomp, opex):
    # promote intensity vs operating cost base
    return _safe_div(sbcomp, opex)


def _sb_promote_rev(sbcomp, revenue):
    # promote intensity vs revenue (comp burden per dollar of sales)
    return _safe_div(sbcomp, revenue)


def _sb_burn_subsidy(sbcomp, ncfo):
    # SBC as cash-burn subsidy: how much of operating cash drain SBC papers over
    return _safe_div(sbcomp, ncfo.abs())


def _sb_overhang(shareswadil, shareswa):
    # diluted-vs-basic overhang: latent share creation from options/RSUs
    return _safe_div(shareswadil, shareswa) - 1.0


def _sb_paper_vs_cash(sbcomp, ncfcommon):
    # paper comp vs cash returned to / raised from common holders
    return _safe_div(sbcomp, ncfcommon.abs())


# ============================================================
# --- SBC dilution rate (sbcomp/marketcap) facets, v001-v012 ---

# SBC dilution rate level (annual paper comp / market value)
def f28sb_f28_sbc_dilution_overhang_dilrate_lvl_63d_base_v001_signal(sbcomp, marketcap):
    b = _sb_dilrate(sbcomp, marketcap)
    result = _mean(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution rate, z-scored vs own year (de-trended overhang intensity)
def f28sb_f28_sbc_dilution_overhang_dilrate_z_252d_base_v002_signal(sbcomp, marketcap):
    b = _z(_sb_dilrate(sbcomp, marketcap), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution rate, year-over-year change (overhang acceleration as level)
def f28sb_f28_sbc_dilution_overhang_dilrate_yoy_252d_base_v003_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution-rate quarterly-change percentile rank vs own 504d (rank of intensification)
def f28sb_f28_sbc_dilution_overhang_dilrate_chgrank_504d_base_v004_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    chg = d - d.shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution rate quarterly growth (intensifying dilution)
def f28sb_f28_sbc_dilution_overhang_dilrate_roc_63d_base_v005_signal(sbcomp, marketcap):
    b = _roc(_sb_dilrate(sbcomp, marketcap), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution rate dispersion (stability of paper-comp intensity)
def f28sb_f28_sbc_dilution_overhang_dilrate_disp_126d_base_v006_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    b = _std(d, 126) / _mean(d, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution rate curvature: quarterly acceleration (2nd difference of the level)
def f28sb_f28_sbc_dilution_overhang_dilrate_accel_63d_base_v007_signal(sbcomp, marketcap):
    d = _mean(_sb_dilrate(sbcomp, marketcap), 21)
    b = (d - d.shift(63)) - (d.shift(63) - d.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC dilution rate fast-minus-slow EMA spread, scaled (MACD-style intensity momentum)
def f28sb_f28_sbc_dilution_overhang_dilrate_macd_189d_base_v008_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    fast = d.ewm(span=42, min_periods=21).mean()
    slow = d.ewm(span=189, min_periods=63).mean()
    b = _safe_div(fast - slow, slow.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long SBC dilution rate ratio (recent paper-comp acceleration)
def f28sb_f28_sbc_dilution_overhang_dilrate_sl_252d_base_v009_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    b = _safe_div(_mean(d, 63), _mean(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate momentum sign x sqrt magnitude (signed, dampened half-year change)
def f28sb_f28_sbc_dilution_overhang_dilrate_signmag_126d_base_v010_signal(sbcomp, marketcap):
    d = _mean(_sb_dilrate(sbcomp, marketcap), 21)
    chg = d - d.shift(126)
    b = np.sign(chg) * np.sqrt(chg.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the year SBC dilution rate sat above its own 504d median (heavy-dilution time)
def f28sb_f28_sbc_dilution_overhang_dilrate_heavytime_252d_base_v011_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    med = d.rolling(504, min_periods=126).median()
    heavy = (d >= med).astype(float)
    b = heavy.rolling(189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate above-median persistence streak, tanh-bounded (regime stickiness)
def f28sb_f28_sbc_dilution_overhang_dilrate_streak_126d_base_v012_signal(sbcomp, marketcap):
    d = _sb_dilrate(sbcomp, marketcap)
    med = d.rolling(252, min_periods=63).median()
    sign = np.sign(d - med)
    streak = sign.rolling(126, min_periods=42).sum() / 126.0
    b = np.tanh(3.0 * streak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- promote intensity vs opex (sbcomp/opex) facets, v013-v024 ---

# SBC as a share of operating expense (promote intensity vs cost base)
def f28sb_f28_sbc_dilution_overhang_promopex_lvl_63d_base_v013_signal(sbcomp, opex):
    b = _mean(_sb_promote_opex(sbcomp, opex), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex z-scored vs own year
def f28sb_f28_sbc_dilution_overhang_promopex_z_252d_base_v014_signal(sbcomp, opex):
    b = _z(_sb_promote_opex(sbcomp, opex), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex quarterly growth (rising comp embedded in cost base)
def f28sb_f28_sbc_dilution_overhang_promopex_roc_63d_base_v015_signal(sbcomp, opex):
    b = _roc(_sb_promote_opex(sbcomp, opex), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex year-over-year change
def f28sb_f28_sbc_dilution_overhang_promopex_yoy_252d_base_v016_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    b = p - p.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex quarterly-change percentile rank vs own 504d (rank of intensification)
def f28sb_f28_sbc_dilution_overhang_promopex_chgrank_504d_base_v017_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    chg = p - p.shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex short/long ratio (recent comp-intensity acceleration)
def f28sb_f28_sbc_dilution_overhang_promopex_sl_252d_base_v018_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    b = _safe_div(_mean(p, 63), _mean(p, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex dispersion (volatility of comp embedment)
def f28sb_f28_sbc_dilution_overhang_promopex_disp_126d_base_v019_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    b = _std(p, 126) / _mean(p, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex fast-minus-slow EMA spread, scaled (MACD-style momentum)
def f28sb_f28_sbc_dilution_overhang_promopex_macd_189d_base_v020_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    fast = p.ewm(span=42, min_periods=21).mean()
    slow = p.ewm(span=189, min_periods=63).mean()
    b = _safe_div(fast - slow, slow.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC growth minus opex growth (paper comp outpacing its own cost base)
def f28sb_f28_sbc_dilution_overhang_promopex_growthspr_126d_base_v021_signal(sbcomp, opex):
    b = _roc(sbcomp, 126) - _roc(opex, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex momentum sign x sqrt magnitude (dampened half-year change)
def f28sb_f28_sbc_dilution_overhang_promopex_signmag_126d_base_v022_signal(sbcomp, opex):
    p = _mean(_sb_promote_opex(sbcomp, opex), 21)
    chg = p - p.shift(126)
    b = np.sign(chg) * np.sqrt(chg.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-opex above-median persistence streak, tanh-bounded (regime stickiness)
def f28sb_f28_sbc_dilution_overhang_promopex_streak_126d_base_v023_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    med = p.rolling(252, min_periods=63).median()
    sign = np.sign(p - med)
    streak = sign.rolling(126, min_periods=42).sum() / 126.0
    b = np.tanh(3.0 * streak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year promote-vs-opex above its own 504d median (heavy embedment time)
def f28sb_f28_sbc_dilution_overhang_promopex_heavytime_252d_base_v024_signal(sbcomp, opex):
    p = _sb_promote_opex(sbcomp, opex)
    med = p.rolling(504, min_periods=126).median()
    heavy = (p >= med).astype(float)
    b = heavy.rolling(189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- promote intensity vs revenue (sbcomp/revenue) facets, v025-v036 ---

# SBC as a share of revenue (comp burden per sales dollar)
def f28sb_f28_sbc_dilution_overhang_promrev_lvl_63d_base_v025_signal(sbcomp, revenue):
    b = _mean(_sb_promote_rev(sbcomp, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue z-scored vs own year
def f28sb_f28_sbc_dilution_overhang_promrev_z_252d_base_v026_signal(sbcomp, revenue):
    b = _z(_sb_promote_rev(sbcomp, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue quarterly growth
def f28sb_f28_sbc_dilution_overhang_promrev_roc_63d_base_v027_signal(sbcomp, revenue):
    b = _roc(_sb_promote_rev(sbcomp, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue year-over-year change
def f28sb_f28_sbc_dilution_overhang_promrev_yoy_252d_base_v028_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    b = p - p.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue quarterly-change percentile rank vs own 504d (rank of intensification)
def f28sb_f28_sbc_dilution_overhang_promrev_chgrank_504d_base_v029_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    chg = p - p.shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue short/long ratio
def f28sb_f28_sbc_dilution_overhang_promrev_sl_252d_base_v030_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    b = _safe_div(_mean(p, 63), _mean(p, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue dispersion
def f28sb_f28_sbc_dilution_overhang_promrev_disp_126d_base_v031_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    b = _std(p, 126) / _mean(p, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue half-year slope (linear trend of comp burden)
def f28sb_f28_sbc_dilution_overhang_promrev_trend_126d_base_v032_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    b = (p - p.shift(126)) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue curvature: quarterly acceleration of comp burden
def f28sb_f28_sbc_dilution_overhang_promrev_accel_63d_base_v033_signal(sbcomp, revenue):
    p = _mean(_sb_promote_rev(sbcomp, revenue), 21)
    b = (p - p.shift(63)) - (p.shift(63) - p.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue momentum sign x sqrt magnitude (dampened half-year change)
def f28sb_f28_sbc_dilution_overhang_promrev_signmag_126d_base_v034_signal(sbcomp, revenue):
    p = _mean(_sb_promote_rev(sbcomp, revenue), 21)
    chg = p - p.shift(126)
    b = np.sign(chg) * np.sqrt(chg.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# promote-vs-revenue above-median persistence streak, tanh-bounded (regime stickiness)
def f28sb_f28_sbc_dilution_overhang_promrev_streak_126d_base_v035_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    med = p.rolling(252, min_periods=63).median()
    sign = np.sign(p - med)
    streak = sign.rolling(126, min_periods=42).sum() / 126.0
    b = np.tanh(3.0 * streak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year promote-vs-revenue above its own 504d median (heavy burden time)
def f28sb_f28_sbc_dilution_overhang_promrev_heavytime_252d_base_v036_signal(sbcomp, revenue):
    p = _sb_promote_rev(sbcomp, revenue)
    med = p.rolling(504, min_periods=126).median()
    heavy = (p >= med).astype(float)
    b = heavy.rolling(189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SBC as cash-burn subsidy (sbcomp/|ncfo|) facets, v037-v048 ---

# SBC as cash-burn subsidy level (paper comp / |operating cash flow|)
def f28sb_f28_sbc_dilution_overhang_burnsub_lvl_63d_base_v037_signal(sbcomp, ncfo):
    b = _mean(_sb_burn_subsidy(sbcomp, ncfo), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy z-scored vs own year
def f28sb_f28_sbc_dilution_overhang_burnsub_z_252d_base_v038_signal(sbcomp, ncfo):
    b = _z(_sb_burn_subsidy(sbcomp, ncfo), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy quarterly growth
def f28sb_f28_sbc_dilution_overhang_burnsub_roc_63d_base_v039_signal(sbcomp, ncfo):
    b = _roc(_sb_burn_subsidy(sbcomp, ncfo), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy quarterly-change percentile rank vs own 504d (rank of subsidy intensification)
def f28sb_f28_sbc_dilution_overhang_burnsub_chgrank_504d_base_v040_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    chg = s - s.shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SBC growth minus operating-cash growth (paper comp outpacing cash generation)
def f28sb_f28_sbc_dilution_overhang_burnsub_growthspr_126d_base_v041_signal(sbcomp, ncfo):
    b = _roc(sbcomp, 126) - _roc(ncfo.abs(), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash flow stripped of the SBC add-back, scaled by SBC (true burn cover)
def f28sb_f28_sbc_dilution_overhang_burnsub_strip_63d_base_v042_signal(sbcomp, ncfo):
    cash_ocf = ncfo - sbcomp
    b = _mean(_safe_div(cash_ocf, sbcomp.abs()), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy short/long ratio (intensifying reliance on paper comp)
def f28sb_f28_sbc_dilution_overhang_burnsub_sl_252d_base_v043_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    b = _safe_div(_mean(s, 63), _mean(s, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy curvature sign x sqrt magnitude (dampened quarterly acceleration)
def f28sb_f28_sbc_dilution_overhang_burnsub_signmag_63d_base_v044_signal(sbcomp, ncfo):
    s = _mean(_sb_burn_subsidy(sbcomp, ncfo), 21)
    accel = (s - s.shift(63)) - (s.shift(63) - s.shift(126))
    b = np.sign(accel) * np.sqrt(accel.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy above-median persistence streak, tanh-bounded (regime stickiness)
def f28sb_f28_sbc_dilution_overhang_burnsub_streak_126d_base_v045_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    med = s.rolling(252, min_periods=63).median()
    sign = np.sign(s - med)
    streak = sign.rolling(126, min_periods=42).sum() / 126.0
    b = np.tanh(3.0 * streak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weak-cash regime (ncfo below own 252d median) weighted by SBC subsidy intensity
def f28sb_f28_sbc_dilution_overhang_burnsub_regime_63d_base_v046_signal(sbcomp, ncfo):
    weak = (ncfo < ncfo.rolling(252, min_periods=63).median()).astype(float)
    sub = _sb_burn_subsidy(sbcomp, ncfo)
    b = _mean(weak * sub, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year SBC subsidy sat above its own 504d median (heavy-subsidy time)
def f28sb_f28_sbc_dilution_overhang_burnsub_fullcover_252d_base_v047_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    med = s.rolling(504, min_periods=126).median()
    full = (s >= med).astype(float)
    b = full.rolling(189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-subsidy fast-minus-slow EMA spread, scaled (MACD-style momentum)
def f28sb_f28_sbc_dilution_overhang_burnsub_macd_189d_base_v048_signal(sbcomp, ncfo):
    s = _sb_burn_subsidy(sbcomp, ncfo)
    fast = s.ewm(span=42, min_periods=21).mean()
    slow = s.ewm(span=189, min_periods=63).mean()
    b = _safe_div(fast - slow, slow.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- diluted-vs-basic overhang (shareswadil/shareswa-1) facets, v049-v062 ---

# diluted-vs-basic share overhang level (latent dilution from options/RSUs)
def f28sb_f28_sbc_dilution_overhang_overhang_lvl_63d_base_v049_signal(shareswadil, shareswa):
    b = _mean(_sb_overhang(shareswadil, shareswa), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang z-scored vs own year
def f28sb_f28_sbc_dilution_overhang_overhang_z_252d_base_v050_signal(shareswadil, shareswa):
    b = _z(_sb_overhang(shareswadil, shareswa), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang trend: change over a year (overhang building or unwinding)
def f28sb_f28_sbc_dilution_overhang_overhang_yoy_252d_base_v051_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    b = o - o.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang quarterly growth (rate of latent-share build)
def f28sb_f28_sbc_dilution_overhang_overhang_roc_63d_base_v052_signal(shareswadil, shareswa):
    b = _roc(_sb_overhang(shareswadil, shareswa), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang quarterly-change percentile rank vs own 504d (rank of overhang momentum)
def f28sb_f28_sbc_dilution_overhang_overhang_chgrank_504d_base_v053_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    chg = o - o.shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang half-year linear slope (overhang trajectory)
def f28sb_f28_sbc_dilution_overhang_overhang_trend_126d_base_v054_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    b = (o - o.shift(126)) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang dispersion (stability of latent dilution)
def f28sb_f28_sbc_dilution_overhang_overhang_disp_126d_base_v055_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    b = _std(o, 126) / _mean(o, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang short/long ratio (recent overhang acceleration)
def f28sb_f28_sbc_dilution_overhang_overhang_sl_252d_base_v056_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    b = _safe_div(_mean(o, 63), _mean(o, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang curvature: quarterly acceleration of latent-share creep
def f28sb_f28_sbc_dilution_overhang_overhang_accel_63d_base_v057_signal(shareswadil, shareswa):
    o = _mean(_sb_overhang(shareswadil, shareswa), 21)
    b = (o - o.shift(63)) - (o.shift(63) - o.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang sign x sqrt magnitude
def f28sb_f28_sbc_dilution_overhang_overhang_signmag_126d_base_v058_signal(shareswadil, shareswa):
    o = _mean(_sb_overhang(shareswadil, shareswa), 126)
    b = np.sign(o) * np.sqrt(o.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang tanh-squashed quarterly change
def f28sb_f28_sbc_dilution_overhang_overhang_tanh_63d_base_v059_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    chg = o - o.shift(63)
    b = np.tanh(50.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year overhang above its own 504d median (heavy-creep time)
def f28sb_f28_sbc_dilution_overhang_overhang_heavytime_252d_base_v060_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    med = o.rolling(504, min_periods=126).median()
    heavy = (o >= med).astype(float)
    b = heavy.rolling(189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang fast-minus-slow EMA spread, scaled (MACD-style momentum)
def f28sb_f28_sbc_dilution_overhang_overhang_macd_189d_base_v061_signal(shareswadil, shareswa):
    o = _sb_overhang(shareswadil, shareswa)
    fast = o.ewm(span=42, min_periods=21).mean()
    slow = o.ewm(span=189, min_periods=63).mean()
    b = _safe_div(fast - slow, slow.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# latent overhang per dollar of paper comp: overhang scaled by SBC/revenue burden
def f28sb_f28_sbc_dilution_overhang_overhang_persbc_63d_base_v062_signal(shareswadil, shareswa, sbcomp, revenue):
    o = _sb_overhang(shareswadil, shareswa)
    burden = _sb_promote_rev(sbcomp, revenue)
    b = _mean(_safe_div(o, burden), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- paper-vs-cash comp (sbcomp vs ncfcommon) facets, v063-v075 ---

# paper-vs-cash comp level (SBC / |net common cash flow|)
def f28sb_f28_sbc_dilution_overhang_papercash_lvl_63d_base_v063_signal(sbcomp, ncfcommon):
    b = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash comp z-scored vs own year
def f28sb_f28_sbc_dilution_overhang_papercash_z_252d_base_v064_signal(sbcomp, ncfcommon):
    b = _z(_sb_paper_vs_cash(sbcomp, ncfcommon), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net paper-minus-cash flow to common (SBC issuance net of cash returned)
def f28sb_f28_sbc_dilution_overhang_papercash_net_63d_base_v065_signal(sbcomp, ncfcommon):
    # ncfcommon negative = cash raised from common (issuance); positive = buyback/return
    net = sbcomp + ncfcommon
    b = _mean(_safe_div(net, sbcomp.abs()), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash quarterly growth
def f28sb_f28_sbc_dilution_overhang_papercash_roc_63d_base_v066_signal(sbcomp, ncfcommon):
    b = _roc(_sb_paper_vs_cash(sbcomp, ncfcommon), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash quarterly-change percentile rank vs own 504d (rank of mix shift)
def f28sb_f28_sbc_dilution_overhang_papercash_chgrank_504d_base_v067_signal(sbcomp, ncfcommon):
    p = _sb_paper_vs_cash(sbcomp, ncfcommon)
    chg = p - p.shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-offset: how far common cash flow runs below its own 252d median, vs SBC issued
def f28sb_f28_sbc_dilution_overhang_papercash_offset_63d_base_v068_signal(sbcomp, ncfcommon):
    med = ncfcommon.rolling(252, min_periods=63).median()
    buyback = (med - ncfcommon).clip(lower=0)
    b = _mean(_safe_div(buyback, sbcomp.abs()), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash short/long ratio
def f28sb_f28_sbc_dilution_overhang_papercash_sl_252d_base_v069_signal(sbcomp, ncfcommon):
    p = _sb_paper_vs_cash(sbcomp, ncfcommon)
    b = _safe_div(_mean(p, 63), _mean(p, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash curvature sign x sqrt magnitude (dampened quarterly acceleration)
def f28sb_f28_sbc_dilution_overhang_papercash_signmag_63d_base_v070_signal(sbcomp, ncfcommon):
    p = _mean(_sb_paper_vs_cash(sbcomp, ncfcommon), 21)
    accel = (p - p.shift(63)) - (p.shift(63) - p.shift(126))
    b = np.sign(accel) * np.sqrt(accel.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash above-median persistence streak, tanh-bounded (regime stickiness)
def f28sb_f28_sbc_dilution_overhang_papercash_streak_126d_base_v071_signal(sbcomp, ncfcommon):
    p = _sb_paper_vs_cash(sbcomp, ncfcommon)
    med = p.rolling(252, min_periods=63).median()
    sign = np.sign(p - med)
    streak = sign.rolling(126, min_periods=42).sum() / 126.0
    b = np.tanh(3.0 * streak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year paper-vs-cash mix sat above its own 504d median (paper-dominant time)
def f28sb_f28_sbc_dilution_overhang_papercash_dominate_252d_base_v072_signal(sbcomp, ncfcommon):
    p = _sb_paper_vs_cash(sbcomp, ncfcommon)
    med = p.rolling(504, min_periods=126).median()
    dom = (p >= med).astype(float)
    b = dom.rolling(189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash year-over-year change
def f28sb_f28_sbc_dilution_overhang_papercash_yoy_252d_base_v073_signal(sbcomp, ncfcommon):
    p = _sb_paper_vs_cash(sbcomp, ncfcommon)
    b = p - p.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash dispersion (stability of paper-vs-cash mix)
def f28sb_f28_sbc_dilution_overhang_papercash_disp_126d_base_v074_signal(sbcomp, ncfcommon):
    p = _sb_paper_vs_cash(sbcomp, ncfcommon)
    b = _std(p, 126) / _mean(p, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite dilution pressure: z(SBC dilution rate) + z(diluted overhang) (two normalized channels)
def f28sb_f28_sbc_dilution_overhang_combo_pressure_252d_base_v075_signal(sbcomp, marketcap, shareswadil, shareswa):
    zd = _z(_sb_dilrate(sbcomp, marketcap), 252)
    zo = _z(_sb_overhang(shareswadil, shareswa), 252)
    b = zd + zo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28sb_f28_sbc_dilution_overhang_dilrate_lvl_63d_base_v001_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_z_252d_base_v002_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_yoy_252d_base_v003_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_chgrank_504d_base_v004_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_roc_63d_base_v005_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_disp_126d_base_v006_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_accel_63d_base_v007_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_macd_189d_base_v008_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_sl_252d_base_v009_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_signmag_126d_base_v010_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_heavytime_252d_base_v011_signal,
    f28sb_f28_sbc_dilution_overhang_dilrate_streak_126d_base_v012_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_lvl_63d_base_v013_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_z_252d_base_v014_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_roc_63d_base_v015_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_yoy_252d_base_v016_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_chgrank_504d_base_v017_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_sl_252d_base_v018_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_disp_126d_base_v019_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_macd_189d_base_v020_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_growthspr_126d_base_v021_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_signmag_126d_base_v022_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_streak_126d_base_v023_signal,
    f28sb_f28_sbc_dilution_overhang_promopex_heavytime_252d_base_v024_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_lvl_63d_base_v025_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_z_252d_base_v026_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_roc_63d_base_v027_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_yoy_252d_base_v028_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_chgrank_504d_base_v029_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_sl_252d_base_v030_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_disp_126d_base_v031_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_trend_126d_base_v032_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_accel_63d_base_v033_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_signmag_126d_base_v034_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_streak_126d_base_v035_signal,
    f28sb_f28_sbc_dilution_overhang_promrev_heavytime_252d_base_v036_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_lvl_63d_base_v037_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_z_252d_base_v038_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_roc_63d_base_v039_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_chgrank_504d_base_v040_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_growthspr_126d_base_v041_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_strip_63d_base_v042_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_sl_252d_base_v043_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_signmag_63d_base_v044_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_streak_126d_base_v045_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_regime_63d_base_v046_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_fullcover_252d_base_v047_signal,
    f28sb_f28_sbc_dilution_overhang_burnsub_macd_189d_base_v048_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_lvl_63d_base_v049_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_z_252d_base_v050_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_yoy_252d_base_v051_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_roc_63d_base_v052_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_chgrank_504d_base_v053_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_trend_126d_base_v054_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_disp_126d_base_v055_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_sl_252d_base_v056_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_accel_63d_base_v057_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_signmag_126d_base_v058_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_tanh_63d_base_v059_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_heavytime_252d_base_v060_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_macd_189d_base_v061_signal,
    f28sb_f28_sbc_dilution_overhang_overhang_persbc_63d_base_v062_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_lvl_63d_base_v063_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_z_252d_base_v064_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_net_63d_base_v065_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_roc_63d_base_v066_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_chgrank_504d_base_v067_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_offset_63d_base_v068_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_sl_252d_base_v069_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_signmag_63d_base_v070_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_streak_126d_base_v071_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_dominate_252d_base_v072_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_yoy_252d_base_v073_signal,
    f28sb_f28_sbc_dilution_overhang_papercash_disp_126d_base_v074_signal,
    f28sb_f28_sbc_dilution_overhang_combo_pressure_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_SBC_DILUTION_OVERHANG_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    sbcomp = _fund(101, base=4e7, drift=0.03, vol=0.08).rename("sbcomp")
    opex = _fund(102, base=3e8, drift=0.025, vol=0.05).rename("opex")
    revenue = _fund(103, base=5e8, drift=0.03, vol=0.05).rename("revenue")
    marketcap = _fund(104, base=2e9, drift=0.02, vol=0.09).rename("marketcap")
    ncfcommon = _fund(105, base=3e7, drift=0.0, vol=0.10, allow_neg=True).rename("ncfcommon")
    shareswa = _fund(106, base=2e8, drift=0.01, vol=0.02).rename("shareswa")
    _dilfac = pd.Series(np.abs(np.random.default_rng(107).normal(0.05, 0.03, n)), name=None)
    shareswadil = (shareswa * (1.0 + _dilfac)).rename("shareswadil")
    ncfo = _fund(108, base=6e7, drift=0.02, vol=0.10, allow_neg=True).rename("ncfo")

    cols = {
        "sbcomp": sbcomp, "opex": opex, "revenue": revenue, "marketcap": marketcap,
        "ncfcommon": ncfcommon, "shareswa": shareswa, "shareswadil": shareswadil,
        "ncfo": ncfo, "closeadj": closeadj,
    }

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
        "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
        "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
        "investments", "inventory", "receivables", "payables", "equity", "retearn",
        "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
        "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
        "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
        "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
        "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
        "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not subset of allowlist" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
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

    print("OK f28_sbc_dilution_overhang_base_001_075_claude: %d features pass" % n_features)
