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


def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (impairment / writedown risk) =====
def _intang_share(intangibles, assets):
    # intangibles as a share of assets (goodwill-heavy / writedown-prone proxy)
    return intangibles / assets.replace(0, np.nan)


def _ppe_book_stress(ppnenet, equity):
    # PP&E carried vs book equity (impairment would hit equity hardest)
    return ppnenet / equity.replace(0, np.nan)


def _aging(depamor, ppnenet):
    # depreciation/PP&E aging proxy (older base -> writedown-prone)
    return depamor / ppnenet.replace(0, np.nan)


def _tangible_book_share(tangibles, equity):
    # how much of book equity is backed by tangible assets
    return tangibles / equity.replace(0, np.nan)


def _impair_prone_share(intangibles, ppnenet, assets):
    # intangibles + PP&E = the impairment-prone asset block / assets
    return (intangibles + ppnenet) / assets.replace(0, np.nan)


def _tbv(tangibles, intangibles):
    # tangible-book erosion proxy: tangibles net of intangibles
    return (tangibles - intangibles) / (tangibles + intangibles).replace(0, np.nan)


def _growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))




# slope of: intangibles/assets level (goodwill-heavy writedown-prone share)
def f34iw_f34_impairment_writedown_risk_intshare_0d_slope_v001_signal(intangibles, assets):
    base = _intang_share(intangibles, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/assets share z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_intsharez_252d_slope_v002_signal(intangibles, assets):
    base = _z(_intang_share(intangibles, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/assets share z-scored vs its own two years
def f34iw_f34_impairment_writedown_risk_intsharez_504d_slope_v003_signal(intangibles, assets):
    base = _z(_intang_share(intangibles, assets), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/assets share percentile rank (cross-time extremity)
def f34iw_f34_impairment_writedown_risk_intsharerank_504d_slope_v004_signal(intangibles, assets):
    base = _rank(_intang_share(intangibles, assets), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: year-over-year change in intangibles/assets share (goodwill build)
def f34iw_f34_impairment_writedown_risk_intsharegr_252d_slope_v005_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    base = s - s.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of intangibles/assets share
def f34iw_f34_impairment_writedown_risk_intsharemom_63d_slope_v006_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    base = s - s.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/assets term structure (short mean minus long mean)
def f34iw_f34_impairment_writedown_risk_intshareterm_63v504_slope_v007_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    base = _mean(s, 63) - _mean(s, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: dispersion (rolling std) of intangibles/assets share
def f34iw_f34_impairment_writedown_risk_intsharedisp_252d_slope_v008_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    base = _std(s, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles vs its 504d peak (writedown would show as a drop from peak carry)
def f34iw_f34_impairment_writedown_risk_intpeakdist_504d_slope_v009_signal(intangibles):
    pk = _rmax(intangibles, 504)
    base = intangibles / pk.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/equity (book-wipeout exposure if written down)
def f34iw_f34_impairment_writedown_risk_inteq_0d_slope_v010_signal(intangibles, equity):
    base = intangibles / equity.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/equity z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_inteqz_252d_slope_v011_signal(intangibles, equity):
    base = _z(intangibles / equity.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/equity percentile rank (book-wipeout extremity)
def f34iw_f34_impairment_writedown_risk_inteqrank_504d_slope_v012_signal(intangibles, equity):
    base = _rank(intangibles / equity.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy change in intangibles/equity (rising book-wipeout risk)
def f34iw_f34_impairment_writedown_risk_inteqgr_252d_slope_v013_signal(intangibles, equity):
    r = intangibles / equity.replace(0, np.nan)
    base = r - r.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/equity carrying stress (impairment hits equity)
def f34iw_f34_impairment_writedown_risk_ppebook_0d_slope_v014_signal(ppnenet, equity):
    base = _ppe_book_stress(ppnenet, equity)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/equity stress z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_ppebookz_252d_slope_v015_signal(ppnenet, equity):
    base = _z(_ppe_book_stress(ppnenet, equity), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/equity stress percentile rank (carrying-stress extremity)
def f34iw_f34_impairment_writedown_risk_ppebookrank_504d_slope_v016_signal(ppnenet, equity):
    base = _rank(_ppe_book_stress(ppnenet, equity), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of PP&E/equity stress
def f34iw_f34_impairment_writedown_risk_ppebookmom_63d_slope_v017_signal(ppnenet, equity):
    s = _ppe_book_stress(ppnenet, equity)
    base = s - s.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy change in PP&E/equity stress
def f34iw_f34_impairment_writedown_risk_ppebookgr_252d_slope_v018_signal(ppnenet, equity):
    s = _ppe_book_stress(ppnenet, equity)
    base = s - s.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/equity stress term structure (short minus long mean)
def f34iw_f34_impairment_writedown_risk_ppebookterm_63v504_slope_v019_signal(ppnenet, equity):
    s = _ppe_book_stress(ppnenet, equity)
    base = _mean(s, 63) - _mean(s, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/assets fixed-asset intensity (writedown-prone block)
def f34iw_f34_impairment_writedown_risk_ppeasset_0d_slope_v020_signal(ppnenet, assets):
    base = ppnenet / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/assets intensity z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_ppeassetz_252d_slope_v021_signal(ppnenet, assets):
    base = _z(ppnenet / assets.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/assets intensity percentile rank
def f34iw_f34_impairment_writedown_risk_ppeassetrank_504d_slope_v022_signal(ppnenet, assets):
    base = _rank(ppnenet / assets.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: log growth of PP&E balance (capacity build that can be impaired)
def f34iw_f34_impairment_writedown_risk_ppegr_252d_slope_v023_signal(ppnenet):
    base = _growth(ppnenet, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: half-year log growth of PP&E balance
def f34iw_f34_impairment_writedown_risk_ppegr_126d_slope_v024_signal(ppnenet):
    base = _growth(ppnenet, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: depreciation/PP&E aging ratio (older base -> impairment-prone)
def f34iw_f34_impairment_writedown_risk_aging_0d_slope_v025_signal(depamor, ppnenet):
    base = _aging(depamor, ppnenet)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging ratio z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_agingz_252d_slope_v026_signal(depamor, ppnenet):
    base = _z(_aging(depamor, ppnenet), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging ratio percentile rank (aging-extremity)
def f34iw_f34_impairment_writedown_risk_agingrank_504d_slope_v027_signal(depamor, ppnenet):
    base = _rank(_aging(depamor, ppnenet), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of the aging ratio (accelerating depreciation drag)
def f34iw_f34_impairment_writedown_risk_agingmom_63d_slope_v028_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    base = s - s.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy change in aging ratio
def f34iw_f34_impairment_writedown_risk_aginggr_252d_slope_v029_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    base = s - s.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging-ratio term structure (short minus long mean)
def f34iw_f34_impairment_writedown_risk_agingterm_63v504_slope_v030_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    base = _mean(s, 63) - _mean(s, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: depreciation+amortization/assets charge intensity
def f34iw_f34_impairment_writedown_risk_depasset_0d_slope_v031_signal(depamor, assets):
    base = depamor / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: D&A/assets intensity z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_depassetz_252d_slope_v032_signal(depamor, assets):
    base = _z(depamor / assets.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: log growth of D&A charge (accelerating non-cash drag)
def f34iw_f34_impairment_writedown_risk_depgr_252d_slope_v033_signal(depamor):
    base = _growth(depamor, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: D&A/equity (non-cash charge vs book cushion)
def f34iw_f34_impairment_writedown_risk_depeq_0d_slope_v034_signal(depamor, equity):
    base = depamor / equity.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-book share of equity (cushion against writedowns)
def f34iw_f34_impairment_writedown_risk_tbveq_0d_slope_v035_signal(tangibles, equity):
    base = _tangible_book_share(tangibles, equity)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-book/equity z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_tbveqz_252d_slope_v036_signal(tangibles, equity):
    base = _z(_tangible_book_share(tangibles, equity), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy change in tangible-book/equity (tangible-book erosion)
def f34iw_f34_impairment_writedown_risk_tbveqgr_252d_slope_v037_signal(tangibles, equity):
    s = _tangible_book_share(tangibles, equity)
    base = s - s.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of tangible-book/equity
def f34iw_f34_impairment_writedown_risk_tbveqmom_63d_slope_v038_signal(tangibles, equity):
    s = _tangible_book_share(tangibles, equity)
    base = s - s.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-vs-intangible balance (erosion proxy, [-1,1])
def f34iw_f34_impairment_writedown_risk_tbverode_0d_slope_v039_signal(tangibles, intangibles):
    base = _tbv(tangibles, intangibles)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-vs-intangible balance percentile rank
def f34iw_f34_impairment_writedown_risk_tbveroderank_504d_slope_v040_signal(tangibles, intangibles):
    base = _rank(_tbv(tangibles, intangibles), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of tangible-vs-intangible balance
def f34iw_f34_impairment_writedown_risk_tbverodemom_63d_slope_v041_signal(tangibles, intangibles):
    s = _tbv(tangibles, intangibles)
    base = s - s.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-asset share of the balance sheet
def f34iw_f34_impairment_writedown_risk_tangshare_0d_slope_v042_signal(tangibles, assets):
    base = tangibles / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-asset share z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_tangsharez_252d_slope_v043_signal(tangibles, assets):
    base = _z(tangibles / assets.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: impairment-prone asset share (intangibles+PP&E)/assets
def f34iw_f34_impairment_writedown_risk_impshare_0d_slope_v044_signal(intangibles, ppnenet, assets):
    base = _impair_prone_share(intangibles, ppnenet, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: impairment-prone share z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_impsharez_252d_slope_v045_signal(intangibles, ppnenet, assets):
    base = _z(_impair_prone_share(intangibles, ppnenet, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: impairment-prone share percentile rank
def f34iw_f34_impairment_writedown_risk_impsharerank_504d_slope_v046_signal(intangibles, ppnenet, assets):
    base = _rank(_impair_prone_share(intangibles, ppnenet, assets), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of impairment-prone share
def f34iw_f34_impairment_writedown_risk_impsharemom_63d_slope_v047_signal(intangibles, ppnenet, assets):
    s = _impair_prone_share(intangibles, ppnenet, assets)
    base = s - s.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy change in impairment-prone share
def f34iw_f34_impairment_writedown_risk_impsharegr_252d_slope_v048_signal(intangibles, ppnenet, assets):
    s = _impair_prone_share(intangibles, ppnenet, assets)
    base = s - s.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: amortisation rate of the intangible book (D&A relative to intangibles)
def f34iw_f34_impairment_writedown_risk_intamortrate_0d_slope_v049_signal(depamor, intangibles):
    base = depamor / intangibles.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: impairment-prone-block/equity z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_impshareeqz_252d_slope_v050_signal(intangibles, ppnenet, equity):
    base = _z((intangibles + ppnenet) / equity.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: goodwill-heavy proxy: intangibles relative to hard PP&E base
def f34iw_f34_impairment_writedown_risk_gwvsppe_0d_slope_v051_signal(intangibles, ppnenet):
    base = intangibles / ppnenet.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: goodwill-vs-PP&E proxy z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_gwvsppez_252d_slope_v052_signal(intangibles, ppnenet):
    base = _z(intangibles / ppnenet.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: goodwill-vs-PP&E proxy percentile rank
def f34iw_f34_impairment_writedown_risk_gwvspperank_504d_slope_v053_signal(intangibles, ppnenet):
    base = _rank(intangibles / ppnenet.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy change in goodwill-vs-PP&E proxy (goodwill creep vs hard base)
def f34iw_f34_impairment_writedown_risk_gwvsppegr_252d_slope_v054_signal(intangibles, ppnenet):
    r = intangibles / ppnenet.replace(0, np.nan)
    base = r - r.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: equity/assets (thin book amplifies writedown impact)
def f34iw_f34_impairment_writedown_risk_eqasset_0d_slope_v055_signal(equity, assets):
    base = equity / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: equity/assets z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_eqassetz_252d_slope_v056_signal(equity, assets):
    base = _z(equity / assets.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy change in equity/assets (book thinning)
def f34iw_f34_impairment_writedown_risk_eqassetgr_252d_slope_v057_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    base = r - r.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: fraction of last year equity/assets sat below its 504d median (thin-book regime)
def f34iw_f34_impairment_writedown_risk_thinbookcnt_252d_slope_v058_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    med = r.rolling(504, min_periods=126).median()
    thin = (r < med).astype(float)
    base = thin.rolling(252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: book-equity drawdown from its 504d peak (impairment erosion)
def f34iw_f34_impairment_writedown_risk_eqdd_504d_slope_v059_signal(equity):
    pk = _rmax(equity, 504)
    base = equity / pk.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible cover of the impairment-prone block (buffer ratio)
def f34iw_f34_impairment_writedown_risk_tangcover_0d_slope_v060_signal(tangibles, intangibles, ppnenet):
    base = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-cover ratio z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_tangcoverz_252d_slope_v061_signal(tangibles, intangibles, ppnenet):
    base = _z(tangibles / (intangibles + ppnenet).replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy change in net impairment exposure ((prone - tangible cover)/assets)
def f34iw_f34_impairment_writedown_risk_netimpgr_252d_slope_v062_signal(intangibles, ppnenet, tangibles, assets):
    x = (intangibles + ppnenet - tangibles) / assets.replace(0, np.nan)
    base = x - x.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: net impairment exposure percentile rank
def f34iw_f34_impairment_writedown_risk_netimprank_504d_slope_v063_signal(intangibles, ppnenet, tangibles):
    x = (intangibles + ppnenet - tangibles) / (intangibles + ppnenet + tangibles).replace(0, np.nan)
    base = _rank(x, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangible-share x PP&E-book-stress interaction (compounded writedown risk)
def f34iw_f34_impairment_writedown_risk_intsharexstress_0d_slope_v064_signal(intangibles, assets, ppnenet, equity):
    a = _intang_share(intangibles, assets)
    s = _ppe_book_stress(ppnenet, equity)
    base = a * s
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging x intangible-share (old hard base alongside goodwill-heavy mix)
def f34iw_f34_impairment_writedown_risk_agingxintshare_0d_slope_v065_signal(depamor, ppnenet, intangibles, assets):
    ag = _aging(depamor, ppnenet)
    isr = _intang_share(intangibles, assets)
    base = ag * isr
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: uncovered prone block (beyond tangible cover) weighted by aging burden
def f34iw_f34_impairment_writedown_risk_uncoveredxaging_0d_slope_v066_signal(intangibles, ppnenet, tangibles, depamor):
    uncov = (intangibles + ppnenet - tangibles).clip(lower=0.0) / (intangibles + ppnenet).replace(0, np.nan)
    ag = _aging(depamor, ppnenet)
    base = uncov * ag
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: fraction of last year intangible-share rose qoq (goodwill-build regime)
def f34iw_f34_impairment_writedown_risk_intaccelflag_252d_slope_v067_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    up = (s > s.shift(63)).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: fraction of two years the aging ratio rose qoq (sustained aging regime)
def f34iw_f34_impairment_writedown_risk_agingupstreak_504d_slope_v068_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    up = (s > s.shift(63)).astype(float)
    base = up.rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: fraction of two years PP&E/equity stress sat in its upper tercile
def f34iw_f34_impairment_writedown_risk_ppestresshi_504d_slope_v069_signal(ppnenet, equity):
    s = _ppe_book_stress(ppnenet, equity)
    r = _rank(s, 504) + 0.5
    base = (r >= 0.6667).astype(float).rolling(252, min_periods=126).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: signed-sqrt of intangible-share deviation from its year mean
def f34iw_f34_impairment_writedown_risk_intsignmag_252d_slope_v070_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    d = s - _mean(s, 252)
    base = np.sign(d) * (d.abs() ** 0.5)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: fraction of two years the tangible-vs-intangible balance fell qoq (erosion regime)
def f34iw_f34_impairment_writedown_risk_tbverodestreak_504d_slope_v071_signal(tangibles, intangibles):
    s = _tbv(tangibles, intangibles)
    dn = (s < s.shift(63)).astype(float)
    base = dn.rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: drawdown-style: intangibles/equity vs its 504d min (build above floor)
def f34iw_f34_impairment_writedown_risk_inteqdd_504d_slope_v072_signal(intangibles, equity):
    r = intangibles / equity.replace(0, np.nan)
    lo = _rmin(r, 504)
    base = r / lo.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/equity stress relative to its 504d peak (stretch above norm)
def f34iw_f34_impairment_writedown_risk_ppebookpeak_504d_slope_v073_signal(ppnenet, equity):
    s = _ppe_book_stress(ppnenet, equity)
    pk = _rmax(s, 504)
    base = s / pk.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: dispersion of impairment-prone share (instability of asset mix)
def f34iw_f34_impairment_writedown_risk_impsharedisp_252d_slope_v074_signal(intangibles, ppnenet, assets):
    s = _impair_prone_share(intangibles, ppnenet, assets)
    base = _std(s, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging minus D&A/assets (PP&E-specific aging in excess of total charge)
def f34iw_f34_impairment_writedown_risk_agingvsdep_0d_slope_v075_signal(depamor, ppnenet, assets):
    base = _aging(depamor, ppnenet) - depamor / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/assets share z-scored vs its own half-year
def f34iw_f34_impairment_writedown_risk_intsharez_126d_slope_v076_signal(intangibles, assets):
    base = _z(_intang_share(intangibles, assets), 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: EMA-smoothed intangibles/assets share (persistent goodwill load)
def f34iw_f34_impairment_writedown_risk_intshareema_63d_slope_v077_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    base = s.ewm(span=63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/assets share minus its slow EMA (displacement)
def f34iw_f34_impairment_writedown_risk_intsharedisp_ema_252d_slope_v078_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    base = s - s.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: half-year momentum of intangibles/assets share
def f34iw_f34_impairment_writedown_risk_intsharemom_126d_slope_v079_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    base = s - s.shift(126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly log growth of intangibles balance
def f34iw_f34_impairment_writedown_risk_intgr_63d_slope_v080_signal(intangibles):
    base = _growth(intangibles, 63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: percentile rank of yoy intangibles growth
def f34iw_f34_impairment_writedown_risk_intgrrank_504d_slope_v081_signal(intangibles):
    base = _rank(_growth(intangibles, 252), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/equity z-scored vs its own two years
def f34iw_f34_impairment_writedown_risk_inteqz_504d_slope_v082_signal(intangibles, equity):
    base = _z(intangibles / equity.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles/equity term structure (short minus long mean)
def f34iw_f34_impairment_writedown_risk_inteqterm_63v504_slope_v083_signal(intangibles, equity):
    r = intangibles / equity.replace(0, np.nan)
    base = _mean(r, 63) - _mean(r, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: dispersion of intangibles/equity (book-wipeout-risk volatility)
def f34iw_f34_impairment_writedown_risk_inteqdisp_252d_slope_v084_signal(intangibles, equity):
    r = intangibles / equity.replace(0, np.nan)
    base = _std(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: EMA-smoothed intangibles/equity
def f34iw_f34_impairment_writedown_risk_inteqema_63d_slope_v085_signal(intangibles, equity):
    r = intangibles / equity.replace(0, np.nan)
    base = r.ewm(span=63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/equity stress z-scored vs its own half-year
def f34iw_f34_impairment_writedown_risk_ppebookz_126d_slope_v086_signal(ppnenet, equity):
    base = _z(_ppe_book_stress(ppnenet, equity), 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: EMA-smoothed PP&E/equity stress
def f34iw_f34_impairment_writedown_risk_ppebookema_63d_slope_v087_signal(ppnenet, equity):
    s = _ppe_book_stress(ppnenet, equity)
    base = s.ewm(span=63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: half-year momentum of PP&E/equity stress
def f34iw_f34_impairment_writedown_risk_ppebookmom_126d_slope_v088_signal(ppnenet, equity):
    s = _ppe_book_stress(ppnenet, equity)
    base = s - s.shift(126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/equity stress percentile rank vs its five-year history
def f34iw_f34_impairment_writedown_risk_ppebookpct_1260d_slope_v089_signal(ppnenet, equity):
    base = _rank(_ppe_book_stress(ppnenet, equity), 1260)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/assets intensity z-scored vs its own two years
def f34iw_f34_impairment_writedown_risk_ppeassetz_504d_slope_v090_signal(ppnenet, assets):
    base = _z(ppnenet / assets.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of PP&E/assets intensity
def f34iw_f34_impairment_writedown_risk_ppeassetmom_63d_slope_v091_signal(ppnenet, assets):
    r = ppnenet / assets.replace(0, np.nan)
    base = r - r.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: PP&E/assets intensity term structure (short minus long mean)
def f34iw_f34_impairment_writedown_risk_ppeassetterm_63v504_slope_v092_signal(ppnenet, assets):
    r = ppnenet / assets.replace(0, np.nan)
    base = _mean(r, 63) - _mean(r, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly log growth of PP&E balance
def f34iw_f34_impairment_writedown_risk_ppegr_63d_slope_v093_signal(ppnenet):
    base = _growth(ppnenet, 63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: percentile rank of yoy PP&E growth (overbuild flag)
def f34iw_f34_impairment_writedown_risk_ppegrrank_504d_slope_v094_signal(ppnenet):
    base = _rank(_growth(ppnenet, 252), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging ratio z-scored vs its own half-year
def f34iw_f34_impairment_writedown_risk_agingz_126d_slope_v095_signal(depamor, ppnenet):
    base = _z(_aging(depamor, ppnenet), 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: EMA-smoothed aging ratio
def f34iw_f34_impairment_writedown_risk_agingema_63d_slope_v096_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    base = s.ewm(span=63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: half-year momentum of the aging ratio
def f34iw_f34_impairment_writedown_risk_agingmom_126d_slope_v097_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    base = s - s.shift(126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging ratio percentile rank vs five-year history
def f34iw_f34_impairment_writedown_risk_agingpct_1260d_slope_v098_signal(depamor, ppnenet):
    base = _rank(_aging(depamor, ppnenet), 1260)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging-ratio acceleration: qoq momentum minus prior qoq momentum
def f34iw_f34_impairment_writedown_risk_agingaccel_63d_slope_v099_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    m = s - s.shift(63)
    base = m - m.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: D&A/assets intensity z-scored vs its own two years
def f34iw_f34_impairment_writedown_risk_depassetz_504d_slope_v100_signal(depamor, assets):
    base = _z(depamor / assets.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of D&A/assets intensity
def f34iw_f34_impairment_writedown_risk_depassetmom_63d_slope_v101_signal(depamor, assets):
    r = depamor / assets.replace(0, np.nan)
    base = r - r.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: half-year log growth of the D&A charge
def f34iw_f34_impairment_writedown_risk_depgr_126d_slope_v102_signal(depamor):
    base = _growth(depamor, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: D&A/equity z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_depeqz_252d_slope_v103_signal(depamor, equity):
    base = _z(depamor / equity.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: D&A charge burst: smoothed charge vs its 504d typical level (impairment-driven spike)
def f34iw_f34_impairment_writedown_risk_depburst_504d_slope_v104_signal(depamor):
    q = _mean(depamor, 63)
    typ = q.rolling(504, min_periods=252).mean()
    base = q / typ.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-book/equity z-scored vs its own two years
def f34iw_f34_impairment_writedown_risk_tbveqz_504d_slope_v105_signal(tangibles, equity):
    base = _z(_tangible_book_share(tangibles, equity), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-book/equity term structure (short minus long mean)
def f34iw_f34_impairment_writedown_risk_tbveqterm_63v504_slope_v106_signal(tangibles, equity):
    s = _tangible_book_share(tangibles, equity)
    base = _mean(s, 63) - _mean(s, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-book/equity drawdown from its 504d peak (erosion depth)
def f34iw_f34_impairment_writedown_risk_tbveqdd_504d_slope_v107_signal(tangibles, equity):
    s = _tangible_book_share(tangibles, equity)
    pk = _rmax(s, 504)
    base = s / pk.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-vs-intangible balance z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_tbverodez_252d_slope_v108_signal(tangibles, intangibles):
    base = _z(_tbv(tangibles, intangibles), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy change in tangible-vs-intangible balance
def f34iw_f34_impairment_writedown_risk_tbverodegr_252d_slope_v109_signal(tangibles, intangibles):
    s = _tbv(tangibles, intangibles)
    base = s - s.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of tangible-asset share
def f34iw_f34_impairment_writedown_risk_tangsharemom_63d_slope_v110_signal(tangibles, assets):
    r = tangibles / assets.replace(0, np.nan)
    base = r - r.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-asset share z-scored vs its own two years
def f34iw_f34_impairment_writedown_risk_tangsharez_504d_slope_v111_signal(tangibles, assets):
    base = _z(tangibles / assets.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: yoy log growth of tangible assets (negative = tangible erosion)
def f34iw_f34_impairment_writedown_risk_tanggr_252d_slope_v112_signal(tangibles):
    base = _growth(tangibles, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: impairment-prone share z-scored vs its own half-year
def f34iw_f34_impairment_writedown_risk_impsharez_126d_slope_v113_signal(intangibles, ppnenet, assets):
    base = _z(_impair_prone_share(intangibles, ppnenet, assets), 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: EMA-smoothed impairment-prone share
def f34iw_f34_impairment_writedown_risk_impshareema_63d_slope_v114_signal(intangibles, ppnenet, assets):
    s = _impair_prone_share(intangibles, ppnenet, assets)
    base = s.ewm(span=63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: impairment-prone share term structure (short minus long mean)
def f34iw_f34_impairment_writedown_risk_impshareterm_63v504_slope_v115_signal(intangibles, ppnenet, assets):
    s = _impair_prone_share(intangibles, ppnenet, assets)
    base = _mean(s, 63) - _mean(s, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: impairment-prone share vs its 504d min (build above floor)
def f34iw_f34_impairment_writedown_risk_impsharedd_504d_slope_v116_signal(intangibles, ppnenet, assets):
    s = _impair_prone_share(intangibles, ppnenet, assets)
    lo = _rmin(s, 504)
    base = s / lo.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of intangible share within the impairment-prone block
def f34iw_f34_impairment_writedown_risk_intinpronemom_63d_slope_v117_signal(intangibles, ppnenet):
    r = intangibles / (intangibles + ppnenet).replace(0, np.nan)
    base = r - r.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: impairment-cover ratio term structure (prone/tangibles, short minus long mean)
def f34iw_f34_impairment_writedown_risk_impcoverterm_63v504_slope_v118_signal(intangibles, ppnenet, tangibles):
    r = (intangibles + ppnenet) / tangibles.replace(0, np.nan)
    base = _mean(r, 63) - _mean(r, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: goodwill-vs-PP&E proxy z-scored vs its own two years
def f34iw_f34_impairment_writedown_risk_gwvsppez_504d_slope_v119_signal(intangibles, ppnenet):
    base = _z(intangibles / ppnenet.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: goodwill-vs-PP&E proxy term structure (short minus long mean)
def f34iw_f34_impairment_writedown_risk_gwvsppeterm_63v504_slope_v120_signal(intangibles, ppnenet):
    r = intangibles / ppnenet.replace(0, np.nan)
    base = _mean(r, 63) - _mean(r, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: dispersion of the goodwill-vs-PP&E proxy
def f34iw_f34_impairment_writedown_risk_gwvsppedisp_252d_slope_v121_signal(intangibles, ppnenet):
    r = intangibles / ppnenet.replace(0, np.nan)
    base = _std(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: goodwill-vs-PP&E proxy vs its 504d min (accretion above floor)
def f34iw_f34_impairment_writedown_risk_gwvsppedd_504d_slope_v122_signal(intangibles, ppnenet):
    r = intangibles / ppnenet.replace(0, np.nan)
    lo = _rmin(r, 504)
    base = r / lo.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: equity/assets z-scored vs its own two years
def f34iw_f34_impairment_writedown_risk_eqassetz_504d_slope_v123_signal(equity, assets):
    base = _z(equity / assets.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of equity/assets (book-cushion velocity)
def f34iw_f34_impairment_writedown_risk_eqassetmom_63d_slope_v124_signal(equity, assets):
    r = equity / assets.replace(0, np.nan)
    base = r - r.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: equity/assets percentile rank vs five-year history (book-cushion cycle position)
def f34iw_f34_impairment_writedown_risk_eqassetrank_1260d_slope_v125_signal(equity, assets):
    base = _rank(equity / assets.replace(0, np.nan), 1260)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: coefficient-of-variation of book equity (book instability)
def f34iw_f34_impairment_writedown_risk_eqdisp_252d_slope_v126_signal(equity):
    base = _std(equity, 252) / _mean(equity, 252).abs().replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: half-year log growth of book equity
def f34iw_f34_impairment_writedown_risk_eqmom_126d_slope_v127_signal(equity):
    base = _growth(equity.clip(lower=1.0), 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: impairment-absorption buffer: book equity per unit of impairment-prone assets
def f34iw_f34_impairment_writedown_risk_impairabsorb_0d_slope_v128_signal(equity, intangibles, ppnenet):
    base = equity / (intangibles + ppnenet).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-cover ratio z-scored vs its own two years
def f34iw_f34_impairment_writedown_risk_tangcoverz_504d_slope_v129_signal(tangibles, intangibles, ppnenet):
    base = _z(tangibles / (intangibles + ppnenet).replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of the tangible-cover ratio
def f34iw_f34_impairment_writedown_risk_tangcovermom_63d_slope_v130_signal(tangibles, intangibles, ppnenet):
    r = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    base = r - r.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-cover ratio vs its 504d peak (cover erosion)
def f34iw_f34_impairment_writedown_risk_tangcoverdd_504d_slope_v131_signal(tangibles, intangibles, ppnenet):
    r = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    pk = _rmax(r, 504)
    base = r / pk.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: assets-scaled net impairment exposure z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_netimpassetz_252d_slope_v132_signal(intangibles, ppnenet, tangibles, assets):
    x = (intangibles + ppnenet - tangibles) / assets.replace(0, np.nan)
    base = _z(x, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: quarterly momentum of net impairment exposure measured against book equity
def f34iw_f34_impairment_writedown_risk_netimpeqmom_63d_slope_v133_signal(intangibles, ppnenet, tangibles, equity):
    x = (intangibles + ppnenet - tangibles) / equity.replace(0, np.nan)
    base = x - x.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging x intangibles/equity (old base + goodwill-heavy book)
def f34iw_f34_impairment_writedown_risk_agingxinteq_0d_slope_v134_signal(depamor, ppnenet, intangibles, equity):
    ag = _aging(depamor, ppnenet)
    ie = intangibles / equity.replace(0, np.nan)
    base = ag * np.tanh(ie)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: fraction of two years intangibles outgrew assets qoq (goodwill-build regime)
def f34iw_f34_impairment_writedown_risk_gwbuildstreak_504d_slope_v135_signal(intangibles, assets):
    fast = (_growth(intangibles, 63) > _growth(assets, 63)).astype(float)
    base = fast.rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: count of months in last year intangible-share set a new 252d high
def f34iw_f34_impairment_writedown_risk_intsharerise252_252d_slope_v136_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    hi = _rmax(s, 252)
    newhi = (s >= hi * 0.99999).astype(float)
    base = newhi.rolling(252, min_periods=126).sum()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: fraction of two years PP&E/assets intensity rose qoq
def f34iw_f34_impairment_writedown_risk_ppestreak_504d_slope_v137_signal(ppnenet, assets):
    r = ppnenet / assets.replace(0, np.nan)
    up = (r > r.shift(63)).astype(float)
    base = up.rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: count of months in last year the tangible-vs-intangible balance hit a new 504d low
def f34iw_f34_impairment_writedown_risk_tbvnewlo_504d_slope_v138_signal(tangibles, intangibles):
    s = _tbv(tangibles, intangibles)
    lo = _rmin(s, 504)
    newlo = (s <= lo * 1.00001).astype(float)
    base = newlo.rolling(252, min_periods=126).sum()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: signed-sqrt of PP&E/equity stress deviation from its year mean
def f34iw_f34_impairment_writedown_risk_ppebooksignmag_252d_slope_v139_signal(ppnenet, equity):
    s = _ppe_book_stress(ppnenet, equity)
    d = s - _mean(s, 252)
    base = np.sign(d) * (d.abs() ** 0.5)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging-ratio displacement: ratio minus its slow EMA (regime detachment)
def f34iw_f34_impairment_writedown_risk_agingdisp_ema_252d_slope_v140_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    base = s - s.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: convex (squared, signed) impairment-prone-share deviation from year mean
def f34iw_f34_impairment_writedown_risk_impconvex_252d_slope_v141_signal(intangibles, ppnenet, assets):
    s = _impair_prone_share(intangibles, ppnenet, assets)
    d = s - _mean(s, 252)
    base = np.sign(d) * (d ** 2) * 10.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: dual stress: intangibles/equity plus PP&E/equity, gated by thin book
def f34iw_f34_impairment_writedown_risk_dualstress_0d_slope_v142_signal(intangibles, ppnenet, equity, assets):
    ie = intangibles / equity.replace(0, np.nan)
    pe = ppnenet / equity.replace(0, np.nan)
    thin = (1.0 - (equity / assets.replace(0, np.nan)).clip(0, 1))
    base = (ie + pe) * thin
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: tangible-book erosion index: tangible cover of equity minus its 504d mean
def f34iw_f34_impairment_writedown_risk_erosionidx_504d_slope_v143_signal(tangibles, intangibles, equity):
    tc = (tangibles - intangibles) / equity.replace(0, np.nan)
    base = tc - _mean(tc, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging gap: depamor/ppnenet minus depamor/tangibles (PP&E-specific aging burden)
def f34iw_f34_impairment_writedown_risk_depcovergap_0d_slope_v144_signal(depamor, ppnenet, tangibles):
    base = depamor / ppnenet.replace(0, np.nan) - depamor / tangibles.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: intangibles growth minus PP&E growth (goodwill outpacing hard assets)
def f34iw_f34_impairment_writedown_risk_intvsppegr_252d_slope_v145_signal(intangibles, ppnenet):
    base = _growth(intangibles, 252) - _growth(ppnenet, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: hard-vs-soft asset spread: PP&E share minus intangible share of assets
def f34iw_f34_impairment_writedown_risk_hardvssoftspread_0d_slope_v146_signal(ppnenet, tangibles, intangibles, assets):
    base = (ppnenet - intangibles) / assets.replace(0, np.nan) + 0.25 * (ppnenet / tangibles.replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: worst-case impairment book hit: prone block net of tangible cover, /equity
def f34iw_f34_impairment_writedown_risk_impairhitratio_0d_slope_v147_signal(intangibles, ppnenet, equity, tangibles):
    base = (intangibles + ppnenet - tangibles).clip(lower=0.0) / equity.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: aging gated by thin book (old base in a thinly-capitalised company)
def f34iw_f34_impairment_writedown_risk_agingxbookthin_0d_slope_v148_signal(depamor, ppnenet, equity, assets):
    ag = _aging(depamor, ppnenet)
    thin = (1.0 - (equity / assets.replace(0, np.nan)).clip(0, 1))
    base = ag * thin
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: vol-of-level: 252d std of intangibles/assets share, normalised by its mean
def f34iw_f34_impairment_writedown_risk_intsharevol_504d_slope_v149_signal(intangibles, assets):
    s = _intang_share(intangibles, assets)
    base = _std(s, 252) / _mean(s, 504).abs().replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of: curvature of PP&E/equity stress: short mean minus midpoint of short/long
def f34iw_f34_impairment_writedown_risk_ppebookcurv_252d_slope_v150_signal(ppnenet, equity):
    s = _ppe_book_stress(ppnenet, equity)
    base = _mean(s, 63) - 0.5 * (_mean(s, 21) + _mean(s, 252))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34iw_f34_impairment_writedown_risk_intshare_0d_slope_v001_signal,
    f34iw_f34_impairment_writedown_risk_intsharez_252d_slope_v002_signal,
    f34iw_f34_impairment_writedown_risk_intsharez_504d_slope_v003_signal,
    f34iw_f34_impairment_writedown_risk_intsharerank_504d_slope_v004_signal,
    f34iw_f34_impairment_writedown_risk_intsharegr_252d_slope_v005_signal,
    f34iw_f34_impairment_writedown_risk_intsharemom_63d_slope_v006_signal,
    f34iw_f34_impairment_writedown_risk_intshareterm_63v504_slope_v007_signal,
    f34iw_f34_impairment_writedown_risk_intsharedisp_252d_slope_v008_signal,
    f34iw_f34_impairment_writedown_risk_intpeakdist_504d_slope_v009_signal,
    f34iw_f34_impairment_writedown_risk_inteq_0d_slope_v010_signal,
    f34iw_f34_impairment_writedown_risk_inteqz_252d_slope_v011_signal,
    f34iw_f34_impairment_writedown_risk_inteqrank_504d_slope_v012_signal,
    f34iw_f34_impairment_writedown_risk_inteqgr_252d_slope_v013_signal,
    f34iw_f34_impairment_writedown_risk_ppebook_0d_slope_v014_signal,
    f34iw_f34_impairment_writedown_risk_ppebookz_252d_slope_v015_signal,
    f34iw_f34_impairment_writedown_risk_ppebookrank_504d_slope_v016_signal,
    f34iw_f34_impairment_writedown_risk_ppebookmom_63d_slope_v017_signal,
    f34iw_f34_impairment_writedown_risk_ppebookgr_252d_slope_v018_signal,
    f34iw_f34_impairment_writedown_risk_ppebookterm_63v504_slope_v019_signal,
    f34iw_f34_impairment_writedown_risk_ppeasset_0d_slope_v020_signal,
    f34iw_f34_impairment_writedown_risk_ppeassetz_252d_slope_v021_signal,
    f34iw_f34_impairment_writedown_risk_ppeassetrank_504d_slope_v022_signal,
    f34iw_f34_impairment_writedown_risk_ppegr_252d_slope_v023_signal,
    f34iw_f34_impairment_writedown_risk_ppegr_126d_slope_v024_signal,
    f34iw_f34_impairment_writedown_risk_aging_0d_slope_v025_signal,
    f34iw_f34_impairment_writedown_risk_agingz_252d_slope_v026_signal,
    f34iw_f34_impairment_writedown_risk_agingrank_504d_slope_v027_signal,
    f34iw_f34_impairment_writedown_risk_agingmom_63d_slope_v028_signal,
    f34iw_f34_impairment_writedown_risk_aginggr_252d_slope_v029_signal,
    f34iw_f34_impairment_writedown_risk_agingterm_63v504_slope_v030_signal,
    f34iw_f34_impairment_writedown_risk_depasset_0d_slope_v031_signal,
    f34iw_f34_impairment_writedown_risk_depassetz_252d_slope_v032_signal,
    f34iw_f34_impairment_writedown_risk_depgr_252d_slope_v033_signal,
    f34iw_f34_impairment_writedown_risk_depeq_0d_slope_v034_signal,
    f34iw_f34_impairment_writedown_risk_tbveq_0d_slope_v035_signal,
    f34iw_f34_impairment_writedown_risk_tbveqz_252d_slope_v036_signal,
    f34iw_f34_impairment_writedown_risk_tbveqgr_252d_slope_v037_signal,
    f34iw_f34_impairment_writedown_risk_tbveqmom_63d_slope_v038_signal,
    f34iw_f34_impairment_writedown_risk_tbverode_0d_slope_v039_signal,
    f34iw_f34_impairment_writedown_risk_tbveroderank_504d_slope_v040_signal,
    f34iw_f34_impairment_writedown_risk_tbverodemom_63d_slope_v041_signal,
    f34iw_f34_impairment_writedown_risk_tangshare_0d_slope_v042_signal,
    f34iw_f34_impairment_writedown_risk_tangsharez_252d_slope_v043_signal,
    f34iw_f34_impairment_writedown_risk_impshare_0d_slope_v044_signal,
    f34iw_f34_impairment_writedown_risk_impsharez_252d_slope_v045_signal,
    f34iw_f34_impairment_writedown_risk_impsharerank_504d_slope_v046_signal,
    f34iw_f34_impairment_writedown_risk_impsharemom_63d_slope_v047_signal,
    f34iw_f34_impairment_writedown_risk_impsharegr_252d_slope_v048_signal,
    f34iw_f34_impairment_writedown_risk_intamortrate_0d_slope_v049_signal,
    f34iw_f34_impairment_writedown_risk_impshareeqz_252d_slope_v050_signal,
    f34iw_f34_impairment_writedown_risk_gwvsppe_0d_slope_v051_signal,
    f34iw_f34_impairment_writedown_risk_gwvsppez_252d_slope_v052_signal,
    f34iw_f34_impairment_writedown_risk_gwvspperank_504d_slope_v053_signal,
    f34iw_f34_impairment_writedown_risk_gwvsppegr_252d_slope_v054_signal,
    f34iw_f34_impairment_writedown_risk_eqasset_0d_slope_v055_signal,
    f34iw_f34_impairment_writedown_risk_eqassetz_252d_slope_v056_signal,
    f34iw_f34_impairment_writedown_risk_eqassetgr_252d_slope_v057_signal,
    f34iw_f34_impairment_writedown_risk_thinbookcnt_252d_slope_v058_signal,
    f34iw_f34_impairment_writedown_risk_eqdd_504d_slope_v059_signal,
    f34iw_f34_impairment_writedown_risk_tangcover_0d_slope_v060_signal,
    f34iw_f34_impairment_writedown_risk_tangcoverz_252d_slope_v061_signal,
    f34iw_f34_impairment_writedown_risk_netimpgr_252d_slope_v062_signal,
    f34iw_f34_impairment_writedown_risk_netimprank_504d_slope_v063_signal,
    f34iw_f34_impairment_writedown_risk_intsharexstress_0d_slope_v064_signal,
    f34iw_f34_impairment_writedown_risk_agingxintshare_0d_slope_v065_signal,
    f34iw_f34_impairment_writedown_risk_uncoveredxaging_0d_slope_v066_signal,
    f34iw_f34_impairment_writedown_risk_intaccelflag_252d_slope_v067_signal,
    f34iw_f34_impairment_writedown_risk_agingupstreak_504d_slope_v068_signal,
    f34iw_f34_impairment_writedown_risk_ppestresshi_504d_slope_v069_signal,
    f34iw_f34_impairment_writedown_risk_intsignmag_252d_slope_v070_signal,
    f34iw_f34_impairment_writedown_risk_tbverodestreak_504d_slope_v071_signal,
    f34iw_f34_impairment_writedown_risk_inteqdd_504d_slope_v072_signal,
    f34iw_f34_impairment_writedown_risk_ppebookpeak_504d_slope_v073_signal,
    f34iw_f34_impairment_writedown_risk_impsharedisp_252d_slope_v074_signal,
    f34iw_f34_impairment_writedown_risk_agingvsdep_0d_slope_v075_signal,
    f34iw_f34_impairment_writedown_risk_intsharez_126d_slope_v076_signal,
    f34iw_f34_impairment_writedown_risk_intshareema_63d_slope_v077_signal,
    f34iw_f34_impairment_writedown_risk_intsharedisp_ema_252d_slope_v078_signal,
    f34iw_f34_impairment_writedown_risk_intsharemom_126d_slope_v079_signal,
    f34iw_f34_impairment_writedown_risk_intgr_63d_slope_v080_signal,
    f34iw_f34_impairment_writedown_risk_intgrrank_504d_slope_v081_signal,
    f34iw_f34_impairment_writedown_risk_inteqz_504d_slope_v082_signal,
    f34iw_f34_impairment_writedown_risk_inteqterm_63v504_slope_v083_signal,
    f34iw_f34_impairment_writedown_risk_inteqdisp_252d_slope_v084_signal,
    f34iw_f34_impairment_writedown_risk_inteqema_63d_slope_v085_signal,
    f34iw_f34_impairment_writedown_risk_ppebookz_126d_slope_v086_signal,
    f34iw_f34_impairment_writedown_risk_ppebookema_63d_slope_v087_signal,
    f34iw_f34_impairment_writedown_risk_ppebookmom_126d_slope_v088_signal,
    f34iw_f34_impairment_writedown_risk_ppebookpct_1260d_slope_v089_signal,
    f34iw_f34_impairment_writedown_risk_ppeassetz_504d_slope_v090_signal,
    f34iw_f34_impairment_writedown_risk_ppeassetmom_63d_slope_v091_signal,
    f34iw_f34_impairment_writedown_risk_ppeassetterm_63v504_slope_v092_signal,
    f34iw_f34_impairment_writedown_risk_ppegr_63d_slope_v093_signal,
    f34iw_f34_impairment_writedown_risk_ppegrrank_504d_slope_v094_signal,
    f34iw_f34_impairment_writedown_risk_agingz_126d_slope_v095_signal,
    f34iw_f34_impairment_writedown_risk_agingema_63d_slope_v096_signal,
    f34iw_f34_impairment_writedown_risk_agingmom_126d_slope_v097_signal,
    f34iw_f34_impairment_writedown_risk_agingpct_1260d_slope_v098_signal,
    f34iw_f34_impairment_writedown_risk_agingaccel_63d_slope_v099_signal,
    f34iw_f34_impairment_writedown_risk_depassetz_504d_slope_v100_signal,
    f34iw_f34_impairment_writedown_risk_depassetmom_63d_slope_v101_signal,
    f34iw_f34_impairment_writedown_risk_depgr_126d_slope_v102_signal,
    f34iw_f34_impairment_writedown_risk_depeqz_252d_slope_v103_signal,
    f34iw_f34_impairment_writedown_risk_depburst_504d_slope_v104_signal,
    f34iw_f34_impairment_writedown_risk_tbveqz_504d_slope_v105_signal,
    f34iw_f34_impairment_writedown_risk_tbveqterm_63v504_slope_v106_signal,
    f34iw_f34_impairment_writedown_risk_tbveqdd_504d_slope_v107_signal,
    f34iw_f34_impairment_writedown_risk_tbverodez_252d_slope_v108_signal,
    f34iw_f34_impairment_writedown_risk_tbverodegr_252d_slope_v109_signal,
    f34iw_f34_impairment_writedown_risk_tangsharemom_63d_slope_v110_signal,
    f34iw_f34_impairment_writedown_risk_tangsharez_504d_slope_v111_signal,
    f34iw_f34_impairment_writedown_risk_tanggr_252d_slope_v112_signal,
    f34iw_f34_impairment_writedown_risk_impsharez_126d_slope_v113_signal,
    f34iw_f34_impairment_writedown_risk_impshareema_63d_slope_v114_signal,
    f34iw_f34_impairment_writedown_risk_impshareterm_63v504_slope_v115_signal,
    f34iw_f34_impairment_writedown_risk_impsharedd_504d_slope_v116_signal,
    f34iw_f34_impairment_writedown_risk_intinpronemom_63d_slope_v117_signal,
    f34iw_f34_impairment_writedown_risk_impcoverterm_63v504_slope_v118_signal,
    f34iw_f34_impairment_writedown_risk_gwvsppez_504d_slope_v119_signal,
    f34iw_f34_impairment_writedown_risk_gwvsppeterm_63v504_slope_v120_signal,
    f34iw_f34_impairment_writedown_risk_gwvsppedisp_252d_slope_v121_signal,
    f34iw_f34_impairment_writedown_risk_gwvsppedd_504d_slope_v122_signal,
    f34iw_f34_impairment_writedown_risk_eqassetz_504d_slope_v123_signal,
    f34iw_f34_impairment_writedown_risk_eqassetmom_63d_slope_v124_signal,
    f34iw_f34_impairment_writedown_risk_eqassetrank_1260d_slope_v125_signal,
    f34iw_f34_impairment_writedown_risk_eqdisp_252d_slope_v126_signal,
    f34iw_f34_impairment_writedown_risk_eqmom_126d_slope_v127_signal,
    f34iw_f34_impairment_writedown_risk_impairabsorb_0d_slope_v128_signal,
    f34iw_f34_impairment_writedown_risk_tangcoverz_504d_slope_v129_signal,
    f34iw_f34_impairment_writedown_risk_tangcovermom_63d_slope_v130_signal,
    f34iw_f34_impairment_writedown_risk_tangcoverdd_504d_slope_v131_signal,
    f34iw_f34_impairment_writedown_risk_netimpassetz_252d_slope_v132_signal,
    f34iw_f34_impairment_writedown_risk_netimpeqmom_63d_slope_v133_signal,
    f34iw_f34_impairment_writedown_risk_agingxinteq_0d_slope_v134_signal,
    f34iw_f34_impairment_writedown_risk_gwbuildstreak_504d_slope_v135_signal,
    f34iw_f34_impairment_writedown_risk_intsharerise252_252d_slope_v136_signal,
    f34iw_f34_impairment_writedown_risk_ppestreak_504d_slope_v137_signal,
    f34iw_f34_impairment_writedown_risk_tbvnewlo_504d_slope_v138_signal,
    f34iw_f34_impairment_writedown_risk_ppebooksignmag_252d_slope_v139_signal,
    f34iw_f34_impairment_writedown_risk_agingdisp_ema_252d_slope_v140_signal,
    f34iw_f34_impairment_writedown_risk_impconvex_252d_slope_v141_signal,
    f34iw_f34_impairment_writedown_risk_dualstress_0d_slope_v142_signal,
    f34iw_f34_impairment_writedown_risk_erosionidx_504d_slope_v143_signal,
    f34iw_f34_impairment_writedown_risk_depcovergap_0d_slope_v144_signal,
    f34iw_f34_impairment_writedown_risk_intvsppegr_252d_slope_v145_signal,
    f34iw_f34_impairment_writedown_risk_hardvssoftspread_0d_slope_v146_signal,
    f34iw_f34_impairment_writedown_risk_impairhitratio_0d_slope_v147_signal,
    f34iw_f34_impairment_writedown_risk_agingxbookthin_0d_slope_v148_signal,
    f34iw_f34_impairment_writedown_risk_intsharevol_504d_slope_v149_signal,
    f34iw_f34_impairment_writedown_risk_ppebookcurv_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_IMPAIRMENT_WRITEDOWN_RISK_REGISTRY_2ND_001_150 = REGISTRY


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

    # impairment / writedown-risk fundamentals.
    # assets is the largest aggregate; tangibles + intangibles are subsets of assets;
    # ppnenet is a subset of tangibles; equity allows negative (post-writedown distress).
    assets = _fund(3401, base=1.4e9, drift=0.010, vol=0.06).rename("assets")
    _tang_raw = _fund(3402, base=8.0e8, drift=0.006, vol=0.08)
    tangibles = pd.Series(np.minimum(_tang_raw.values, 0.95 * assets.values),
                          name="tangibles")
    _ppe_raw = _fund(3403, base=5.0e8, drift=0.012, vol=0.11)
    ppnenet = pd.Series(np.minimum(_ppe_raw.values, 0.97 * tangibles.values),
                        name="ppnenet")
    _intang_raw = _fund(3404, base=3.0e8, drift=0.020, vol=0.14)
    intangibles = pd.Series(np.minimum(_intang_raw.values, 0.9 * (assets.values - tangibles.values + 1.0)),
                            name="intangibles")
    equity = _fund(3405, base=6.0e8, drift=0.004, vol=0.12, allow_neg=True).rename("equity")
    depamor = _fund(3406, base=6.0e7, drift=0.010, vol=0.16).rename("depamor")

    cols = {"intangibles": intangibles, "ppnenet": ppnenet, "assets": assets,
            "equity": equity, "tangibles": tangibles, "depamor": depamor}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("intangibles", "ppnenet", "assets", "equity", "tangibles", "depamor") for c in meta["inputs"]), name
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

    print("OK f34_impairment_writedown_risk_2nd_derivatives_001_150_claude: %d features pass" % n_features)
