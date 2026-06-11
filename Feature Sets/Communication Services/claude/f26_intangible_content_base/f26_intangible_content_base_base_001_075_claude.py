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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (intangible / content base & amortization) =====
def _f26_intang_share(intangibles, assets):
    # content/IP heaviness: intangibles as a share of the asset base
    return intangibles / assets.replace(0, np.nan)


def _f26_tang_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _f26_amort_pace(depamor, intangibles):
    # content-amortization pace: how fast the content/IP stock is being expensed
    return depamor / intangibles.replace(0, np.nan)


def _f26_amort_ppne(depamor, ppnenet):
    return depamor / ppnenet.replace(0, np.nan)


def _f26_intang_to_tang(intangibles, tangibles):
    return intangibles / tangibles.replace(0, np.nan)


def _f26_content_base(intangibles, ppnenet):
    # combined productive content/platform base
    return intangibles + ppnenet


def _f26_amort_aging(depamor, intangibles, ppnenet):
    # amortization relative to the whole content + platform base (aging proxy)
    return depamor / (intangibles + ppnenet).replace(0, np.nan)


# ============================================================
# intangibles / assets : raw content-library heaviness
def f26ic_f26_intangible_content_base_intangshare_0d_base_v001_signal(intangibles, assets):
    b = _f26_intang_share(intangibles, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles / assets, z-scored vs its own 252d history (de-trended heaviness)
def f26ic_f26_intangible_content_base_intangsharez_252d_base_v002_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles / assets, percentile-ranked vs its own 504d history
def f26ic_f26_intangible_content_base_intangsharerank_504d_base_v003_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# physical-to-content base ratio: tangibles / (intangibles+ppnenet) — physical vs productive content
def f26ic_f26_intangible_content_base_tangshare_0d_base_v004_signal(tangibles, intangibles, ppnenet):
    b = tangibles / _f26_content_base(intangibles, ppnenet).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles share of physical assets tangibles/(tangibles+ppnenet), z-scored (physical-mix anomaly)
def f26ic_f26_intangible_content_base_tangsharez_252d_base_v005_signal(tangibles, ppnenet):
    s = tangibles / (tangibles + ppnenet).replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-vs-tangible balance momentum: fast minus slow EWM of (intang-tang)/(intang+tang)
def f26ic_f26_intangible_content_base_mixspread_0d_base_v006_signal(intangibles, tangibles, assets):
    raw = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    b = raw.ewm(span=21, min_periods=10).mean() - raw.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles / tangibles : content-vs-physical mix ratio (log)
def f26ic_f26_intangible_content_base_intang2tang_0d_base_v007_signal(intangibles, tangibles):
    r = _f26_intang_to_tang(intangibles, tangibles)
    b = np.log(r.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles / tangibles ratio z-scored vs its own 126d history (mix anomaly)
def f26ic_f26_intangible_content_base_intang2tangz_126d_base_v008_signal(intangibles, tangibles):
    r = _f26_intang_to_tang(intangibles, tangibles)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depamor / intangibles : content-amortization pace
def f26ic_f26_intangible_content_base_amortpace_0d_base_v009_signal(depamor, intangibles):
    b = _f26_amort_pace(depamor, intangibles)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depamor / intangibles, z-scored vs its 252d history (amortization-pace anomaly)
def f26ic_f26_intangible_content_base_amortpacez_252d_base_v010_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depamor / ppnenet : platform/PP&E amortization pace
def f26ic_f26_intangible_content_base_amortppne_0d_base_v011_signal(depamor, ppnenet):
    b = _f26_amort_ppne(depamor, ppnenet)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depamor / ppnenet, percentile-ranked vs its 504d history
def f26ic_f26_intangible_content_base_amortppnerank_504d_base_v012_signal(depamor, ppnenet):
    s = _f26_amort_ppne(depamor, ppnenet)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible weight in the amortizing base: intangibles/(intang+ppne) — where amortization is anchored
def f26ic_f26_intangible_content_base_amortaging_0d_base_v013_signal(depamor, intangibles, ppnenet):
    weight = intangibles / _f26_content_base(intangibles, ppnenet).replace(0, np.nan)
    pace = _f26_amort_aging(depamor, intangibles, ppnenet)
    b = weight * np.log(pace.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible content-base growth (log) over a year
def f26ic_f26_intangible_content_base_intanggrow_252d_base_v014_signal(intangibles):
    b = _logroc(intangibles, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible content-base growth (log) over a half-year
def f26ic_f26_intangible_content_base_intanggrow_126d_base_v015_signal(intangibles):
    b = _logroc(intangibles, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible content-base sequential growth (log) over a quarter
def f26ic_f26_intangible_content_base_intanggrow_63d_base_v016_signal(intangibles):
    b = _logroc(intangibles, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined content+platform base growth over a year
def f26ic_f26_intangible_content_base_contentbasegrow_252d_base_v017_signal(intangibles, ppnenet):
    cb = _f26_content_base(intangibles, ppnenet)
    b = _logroc(cb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet growth (platform/physical base build) over a year
def f26ic_f26_intangible_content_base_ppnegrow_252d_base_v018_signal(ppnenet):
    b = _logroc(ppnenet, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-growth minus asset-growth (content out-investment vs whole BS)
def f26ic_f26_intangible_content_base_intangvsasset_252d_base_v019_signal(intangibles, assets):
    b = _logroc(intangibles, 252) - _logroc(assets, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-growth vs combined physical-base growth (content out-build vs tang+ppne), z-scored
def f26ic_f26_intangible_content_base_intangvstang_252d_base_v020_signal(intangibles, tangibles, ppnenet):
    phys = (tangibles + ppnenet)
    raw = _logroc(intangibles, 252) - _logroc(phys, 252)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depamor growth (amortization expense build) over a year
def f26ic_f26_intangible_content_base_amortgrow_252d_base_v021_signal(depamor):
    b = _logroc(depamor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net content self-funding: yearly intangible dollar adds relative to yearly amortization expensed
def f26ic_f26_intangible_content_base_netcontent_252d_base_v022_signal(intangibles, depamor):
    adds = intangibles - intangibles.shift(252)
    expensed = depamor.rolling(252, min_periods=126).mean() * 252.0 / 252.0
    b = adds / (adds.abs() + expensed.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-heaviness change z-scored vs its own history (significant tilt shift)
def f26ic_f26_intangible_content_base_heavychgz_252d_base_v023_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    chg = s - s.shift(126)
    b = _z(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible heaviness quarter-change, risk-adjusted by its own 252d level-volatility (regime move)
def f26ic_f26_intangible_content_base_heavychg_63d_base_v024_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    chg = s - s.shift(63)
    sd = _std(s, 252).replace(0, np.nan)
    b = np.tanh(chg / sd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization pace change over a year (Δ depamor/intangibles)
def f26ic_f26_intangible_content_base_pacechg_252d_base_v025_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content base / assets : how much of the BS is productive content + platform
def f26ic_f26_intangible_content_base_contentintensity_0d_base_v026_signal(intangibles, ppnenet, assets):
    cb = _f26_content_base(intangibles, ppnenet)
    b = cb / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content base / assets, z-scored vs its 252d history
def f26ic_f26_intangible_content_base_contentintensityz_252d_base_v027_signal(intangibles, ppnenet, assets):
    cb = _f26_content_base(intangibles, ppnenet)
    s = cb / assets.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization expense relative to total assets (asset-wide amortization burden)
def f26ic_f26_intangible_content_base_amortburden_0d_base_v028_signal(depamor, assets):
    b = depamor / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization burden change over a year
def f26ic_f26_intangible_content_base_amortburdenchg_252d_base_v029_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles vs ppnenet mix (content library vs physical platform)
def f26ic_f26_intangible_content_base_intang2ppne_0d_base_v030_signal(intangibles, ppnenet):
    b = np.log(intangibles.replace(0, np.nan) / ppnenet.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles vs ppnenet mix change over a year (capitalize-content vs build-platform)
def f26ic_f26_intangible_content_base_intang2ppneroc_252d_base_v031_signal(intangibles, ppnenet):
    r = intangibles / ppnenet.replace(0, np.nan)
    b = _roc(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization coverage: depamor relative to intangible-base growth (replenish vs expense)
def f26ic_f26_intangible_content_base_amortcoverage_252d_base_v032_signal(depamor, intangibles):
    add = (intangibles - intangibles.shift(252)).clip(lower=0)
    b = depamor / add.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied content-library life = intangibles / depamor (years of amortization runway)
def f26ic_f26_intangible_content_base_contentlife_0d_base_v033_signal(intangibles, depamor):
    b = intangibles / depamor.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied content-library life, z-scored vs its 252d history (aging anomaly)
def f26ic_f26_intangible_content_base_contentlifez_252d_base_v034_signal(intangibles, depamor):
    s = intangibles / depamor.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied platform life = ppnenet / depamor
def f26ic_f26_intangible_content_base_platformlife_0d_base_v035_signal(ppnenet, depamor):
    b = ppnenet / depamor.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible share dispersion (rolling std of intangibles/assets over a year)
def f26ic_f26_intangible_content_base_sharedisp_252d_base_v036_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    b = _std(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-pace dispersion (rolling std of depamor/intangibles)
def f26ic_f26_intangible_content_base_pacedisp_252d_base_v037_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    b = _std(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-share distance from its own 504d median (regime distance)
def f26ic_f26_intangible_content_base_sharedist_504d_base_v038_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    med = s.rolling(504, min_periods=126).median()
    b = s - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-heavy regime streak: fraction of last year above the 504d median share
def f26ic_f26_intangible_content_base_heavystreak_252d_base_v039_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    med = s.rolling(504, min_periods=126).median()
    above = (s > med).astype(float)
    b = above.rolling(252, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-acceleration regime: depamor/intangibles above its 504d median streak
def f26ic_f26_intangible_content_base_pacestreak_252d_base_v040_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    med = s.rolling(504, min_periods=126).median()
    above = (s > med).astype(float)
    b = above.rolling(252, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base growth minus amortization-burden growth (net build vs expense growth)
def f26ic_f26_intangible_content_base_buildvsexpense_252d_base_v041_signal(intangibles, ppnenet, depamor):
    cb = _f26_content_base(intangibles, ppnenet)
    b = _logroc(cb, 252) - _logroc(depamor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles vs ppnenet share gap relative to assets (which dominates the base)
def f26ic_f26_intangible_content_base_basedominance_0d_base_v042_signal(intangibles, ppnenet, assets):
    b = (intangibles - ppnenet) / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible heaviness vs its slow EMA (content-tilt displacement)
def f26ic_f26_intangible_content_base_heavydisp_base_v043_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    b = s - s.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-heaviness EMA gap: fast vs slow smoothing of the share (persistent-tilt momentum)
def f26ic_f26_intangible_content_base_heavyema_base_v044_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    fast = s.ewm(span=21, min_periods=10).mean()
    slow = s.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization pace vs its slow EMA (pace displacement)
def f26ic_f26_intangible_content_base_pacedisp_ema_base_v045_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    b = s - s.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset growth over a year (physical capacity build)
def f26ic_f26_intangible_content_base_tanggrow_252d_base_v046_signal(tangibles):
    b = _logroc(tangibles, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-base growth over a year (whole-BS expansion baseline)
def f26ic_f26_intangible_content_base_assetgrow_252d_base_v047_signal(assets):
    b = _logroc(assets, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-out-investment intensity: intangible-growth z minus asset-growth z (mix-neutral push)
def f26ic_f26_intangible_content_base_contentpush_252d_base_v048_signal(intangibles, assets):
    gi = _logroc(intangibles, 126)
    ga = _logroc(assets, 126)
    b = _z(gi, 252) - _z(ga, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-pace x heaviness interaction de-trended: pace*heavy minus its own 252d mean
def f26ic_f26_intangible_content_base_paceheavy_0d_base_v049_signal(depamor, intangibles, assets):
    pace = _f26_amort_pace(depamor, intangibles)
    heavy = _f26_intang_share(intangibles, assets)
    raw = pace * heavy
    b = (raw - raw.rolling(252, min_periods=63).mean()) / raw.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-to-content-base share regime: fraction of last year above its 504d median (composition regime)
def f26ic_f26_intangible_content_base_intangofbasez_252d_base_v050_signal(intangibles, ppnenet):
    cb = _f26_content_base(intangibles, ppnenet)
    s = intangibles / cb.replace(0, np.nan)
    med = s.rolling(504, min_periods=126).median()
    above = (s > med).astype(float)
    b = above.rolling(252, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-of-base change over a year (mix drift within productive base)
def f26ic_f26_intangible_content_base_intangofbasechg_252d_base_v051_signal(intangibles, ppnenet):
    cb = _f26_content_base(intangibles, ppnenet)
    s = intangibles / cb.replace(0, np.nan)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization pace measured against ppnenet, z-scored
def f26ic_f26_intangible_content_base_amortppnez_252d_base_v052_signal(depamor, ppnenet):
    s = _f26_amort_ppne(depamor, ppnenet)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization aging, z-scored vs its 504d history (content-stock age anomaly)
def f26ic_f26_intangible_content_base_agingz_504d_base_v053_signal(depamor, intangibles, ppnenet):
    s = _f26_amort_aging(depamor, intangibles, ppnenet)
    b = _z(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base expansion vs its own 1260d trough (multi-year build off the low)
def f26ic_f26_intangible_content_base_baseexpand_1260d_base_v054_signal(intangibles, ppnenet):
    cb = _f26_content_base(intangibles, ppnenet)
    lo = _rmin(cb, 1260)
    b = np.log(cb.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# platform-amortization-pace position in its own 1260d range (PP&E expensing cycle)
def f26ic_f26_intangible_content_base_ppnepacerangepos_1260d_base_v055_signal(depamor, ppnenet):
    s = _f26_amort_ppne(depamor, ppnenet)
    hi = _rmax(s, 1260)
    lo = _rmin(s, 1260)
    b = (s - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mix momentum: 63d change in log(intang/tang) scaled by its own 252d volatility
def f26ic_f26_intangible_content_base_mixmom_63d_base_v056_signal(intangibles, tangibles):
    lr = np.log(_f26_intang_to_tang(intangibles, tangibles).replace(0, np.nan))
    chg = lr - lr.shift(63)
    vol = lr.diff().rolling(252, min_periods=63).std()
    b = chg / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of intangible content-base growth (Δ of yearly growth over a quarter)
def f26ic_f26_intangible_content_base_growaccel_252d_base_v057_signal(intangibles):
    g = _logroc(intangibles, 252)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-pace acceleration, sign-magnitude compressed and ranked (bounded pace-bend regime)
def f26ic_f26_intangible_content_base_paceaccel_252d_base_v058_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    accel = s - 2.0 * s.shift(63) + s.shift(126)
    sm = np.sign(accel) * np.sqrt(accel.abs())
    b = _rank(sm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base intensity minus tangible share (net intangible tilt incl. platform)
def f26ic_f26_intangible_content_base_nettilt_0d_base_v059_signal(intangibles, ppnenet, tangibles, assets):
    cb = _f26_content_base(intangibles, ppnenet)
    b = cb / assets.replace(0, np.nan) - _f26_tang_share(tangibles, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization burden relative to content base (depamor / (intangibles+ppnenet)) ranked
def f26ic_f26_intangible_content_base_agingrank_504d_base_v060_signal(depamor, intangibles, ppnenet):
    s = _f26_amort_aging(depamor, intangibles, ppnenet)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-heaviness curvature, EWM-smoothed and ranked (persistent tilt-bend regime, non-affine)
def f26ic_f26_intangible_content_base_heavycurv_252d_base_v061_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    curv = (s - 2.0 * s.shift(63) + s.shift(126)).ewm(span=63, min_periods=21).mean()
    b = _rank(curv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied content life change over a year (content stock aging up or being refreshed)
def f26ic_f26_intangible_content_base_lifechg_252d_base_v062_signal(intangibles, depamor):
    s = intangibles / depamor.replace(0, np.nan)
    b = _roc(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-life acceleration: change in implied content life over a quarter, de-trended
def f26ic_f26_intangible_content_base_lifeaccel_0d_base_v063_signal(intangibles, depamor):
    cl = intangibles / depamor.replace(0, np.nan)
    chg = cl - cl.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# physical-vs-content reinvestment divergence: tangible growth minus ppnenet growth
def f26ic_f26_intangible_content_base_physdiverge_252d_base_v064_signal(tangibles, ppnenet):
    b = _logroc(tangibles, 252) - _logroc(ppnenet, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base out-investment streak: fraction of last year content-base outgrows assets (regime)
def f26ic_f26_intangible_content_base_basevsasset_252d_base_v065_signal(intangibles, ppnenet, assets):
    cb = _f26_content_base(intangibles, ppnenet)
    gap = _logroc(cb, 63) - _logroc(assets, 63)
    out = (gap > 0).astype(float)
    b = out.rolling(252, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-pace mean-reversion: pace minus its 252d mean, scaled by 252d std (extremity)
def f26ic_f26_intangible_content_base_pacestretch_252d_base_v066_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    b = (s - _mean(s, 252)) / _std(s, 252).replace(0, np.nan)
    result = b.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-heaviness convexity vs price-path: signed-sqrt of tilt accel, rank-stabilized (tilt bend)
def f26ic_f26_intangible_content_base_heavyaccel_base_v067_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    accel = s - 2.0 * s.shift(126) + s.shift(252)
    b = (np.sign(accel) * np.sqrt(accel.abs())).rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles share of non-tangible assets (intangibles / (assets - tangibles))
def f26ic_f26_intangible_content_base_intangofnontang_0d_base_v068_signal(intangibles, tangibles, assets):
    denom = (assets - tangibles).replace(0, np.nan)
    b = intangibles / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depamor growth minus intangible growth (amortization outpacing content build)
def f26ic_f26_intangible_content_base_amortoutpace_252d_base_v069_signal(depamor, intangibles):
    b = _logroc(depamor, 252) - _logroc(intangibles, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content base / ppnenet leverage, 126d momentum (content out-leveraging platform, speed)
def f26ic_f26_intangible_content_base_baseoverplatformmom_126d_base_v070_signal(intangibles, ppnenet):
    cb = _f26_content_base(intangibles, ppnenet)
    s = np.log((cb / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible content-base growth, smoothed (persistent content-investment trend)
def f26ic_f26_intangible_content_base_growsm_252d_base_v071_signal(intangibles):
    g = _logroc(intangibles, 252)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-life dispersion: rolling std of implied content life (aging stability), de-leveled
def f26ic_f26_intangible_content_base_lifedisp_252d_base_v072_signal(intangibles, depamor):
    life = np.log((intangibles / depamor.replace(0, np.nan)).replace(0, np.nan))
    b = _std(life, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible share vs tangible share ratio (log) — pure mix indicator on the BS
def f26ic_f26_intangible_content_base_shareratio_0d_base_v073_signal(intangibles, tangibles):
    b = np.log(intangibles.replace(0, np.nan)) - np.log(tangibles.replace(0, np.nan))
    result = b - b.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# amortization burden percentile vs 1260d history (multi-year expense regime)
def f26ic_f26_intangible_content_base_burdenrank_1260d_base_v074_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    b = _rank(s, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable content-tilt composite: sign of content out-investment x amortization-light regime
def f26ic_f26_intangible_content_base_durabletilt_base_v075_signal(intangibles, ppnenet, depamor, assets):
    heavy = _f26_intang_share(intangibles, assets)
    cb = _f26_content_base(intangibles, ppnenet)
    grow = _logroc(cb, 252)
    aging = _f26_amort_aging(depamor, intangibles, ppnenet)
    light = -_z(aging, 252)
    b = np.tanh(8.0 * grow) * np.tanh(3.0 * (heavy - heavy.rolling(504, min_periods=126).median())) + 0.3 * light
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26ic_f26_intangible_content_base_intangshare_0d_base_v001_signal,
    f26ic_f26_intangible_content_base_intangsharez_252d_base_v002_signal,
    f26ic_f26_intangible_content_base_intangsharerank_504d_base_v003_signal,
    f26ic_f26_intangible_content_base_tangshare_0d_base_v004_signal,
    f26ic_f26_intangible_content_base_tangsharez_252d_base_v005_signal,
    f26ic_f26_intangible_content_base_mixspread_0d_base_v006_signal,
    f26ic_f26_intangible_content_base_intang2tang_0d_base_v007_signal,
    f26ic_f26_intangible_content_base_intang2tangz_126d_base_v008_signal,
    f26ic_f26_intangible_content_base_amortpace_0d_base_v009_signal,
    f26ic_f26_intangible_content_base_amortpacez_252d_base_v010_signal,
    f26ic_f26_intangible_content_base_amortppne_0d_base_v011_signal,
    f26ic_f26_intangible_content_base_amortppnerank_504d_base_v012_signal,
    f26ic_f26_intangible_content_base_amortaging_0d_base_v013_signal,
    f26ic_f26_intangible_content_base_intanggrow_252d_base_v014_signal,
    f26ic_f26_intangible_content_base_intanggrow_126d_base_v015_signal,
    f26ic_f26_intangible_content_base_intanggrow_63d_base_v016_signal,
    f26ic_f26_intangible_content_base_contentbasegrow_252d_base_v017_signal,
    f26ic_f26_intangible_content_base_ppnegrow_252d_base_v018_signal,
    f26ic_f26_intangible_content_base_intangvsasset_252d_base_v019_signal,
    f26ic_f26_intangible_content_base_intangvstang_252d_base_v020_signal,
    f26ic_f26_intangible_content_base_amortgrow_252d_base_v021_signal,
    f26ic_f26_intangible_content_base_netcontent_252d_base_v022_signal,
    f26ic_f26_intangible_content_base_heavychgz_252d_base_v023_signal,
    f26ic_f26_intangible_content_base_heavychg_63d_base_v024_signal,
    f26ic_f26_intangible_content_base_pacechg_252d_base_v025_signal,
    f26ic_f26_intangible_content_base_contentintensity_0d_base_v026_signal,
    f26ic_f26_intangible_content_base_contentintensityz_252d_base_v027_signal,
    f26ic_f26_intangible_content_base_amortburden_0d_base_v028_signal,
    f26ic_f26_intangible_content_base_amortburdenchg_252d_base_v029_signal,
    f26ic_f26_intangible_content_base_intang2ppne_0d_base_v030_signal,
    f26ic_f26_intangible_content_base_intang2ppneroc_252d_base_v031_signal,
    f26ic_f26_intangible_content_base_amortcoverage_252d_base_v032_signal,
    f26ic_f26_intangible_content_base_contentlife_0d_base_v033_signal,
    f26ic_f26_intangible_content_base_contentlifez_252d_base_v034_signal,
    f26ic_f26_intangible_content_base_platformlife_0d_base_v035_signal,
    f26ic_f26_intangible_content_base_sharedisp_252d_base_v036_signal,
    f26ic_f26_intangible_content_base_pacedisp_252d_base_v037_signal,
    f26ic_f26_intangible_content_base_sharedist_504d_base_v038_signal,
    f26ic_f26_intangible_content_base_heavystreak_252d_base_v039_signal,
    f26ic_f26_intangible_content_base_pacestreak_252d_base_v040_signal,
    f26ic_f26_intangible_content_base_buildvsexpense_252d_base_v041_signal,
    f26ic_f26_intangible_content_base_basedominance_0d_base_v042_signal,
    f26ic_f26_intangible_content_base_heavydisp_base_v043_signal,
    f26ic_f26_intangible_content_base_heavyema_base_v044_signal,
    f26ic_f26_intangible_content_base_pacedisp_ema_base_v045_signal,
    f26ic_f26_intangible_content_base_tanggrow_252d_base_v046_signal,
    f26ic_f26_intangible_content_base_assetgrow_252d_base_v047_signal,
    f26ic_f26_intangible_content_base_contentpush_252d_base_v048_signal,
    f26ic_f26_intangible_content_base_paceheavy_0d_base_v049_signal,
    f26ic_f26_intangible_content_base_intangofbasez_252d_base_v050_signal,
    f26ic_f26_intangible_content_base_intangofbasechg_252d_base_v051_signal,
    f26ic_f26_intangible_content_base_amortppnez_252d_base_v052_signal,
    f26ic_f26_intangible_content_base_agingz_504d_base_v053_signal,
    f26ic_f26_intangible_content_base_baseexpand_1260d_base_v054_signal,
    f26ic_f26_intangible_content_base_ppnepacerangepos_1260d_base_v055_signal,
    f26ic_f26_intangible_content_base_mixmom_63d_base_v056_signal,
    f26ic_f26_intangible_content_base_growaccel_252d_base_v057_signal,
    f26ic_f26_intangible_content_base_paceaccel_252d_base_v058_signal,
    f26ic_f26_intangible_content_base_nettilt_0d_base_v059_signal,
    f26ic_f26_intangible_content_base_agingrank_504d_base_v060_signal,
    f26ic_f26_intangible_content_base_heavycurv_252d_base_v061_signal,
    f26ic_f26_intangible_content_base_lifechg_252d_base_v062_signal,
    f26ic_f26_intangible_content_base_lifeaccel_0d_base_v063_signal,
    f26ic_f26_intangible_content_base_physdiverge_252d_base_v064_signal,
    f26ic_f26_intangible_content_base_basevsasset_252d_base_v065_signal,
    f26ic_f26_intangible_content_base_pacestretch_252d_base_v066_signal,
    f26ic_f26_intangible_content_base_heavyaccel_base_v067_signal,
    f26ic_f26_intangible_content_base_intangofnontang_0d_base_v068_signal,
    f26ic_f26_intangible_content_base_amortoutpace_252d_base_v069_signal,
    f26ic_f26_intangible_content_base_baseoverplatformmom_126d_base_v070_signal,
    f26ic_f26_intangible_content_base_growsm_252d_base_v071_signal,
    f26ic_f26_intangible_content_base_lifedisp_252d_base_v072_signal,
    f26ic_f26_intangible_content_base_shareratio_0d_base_v073_signal,
    f26ic_f26_intangible_content_base_burdenrank_1260d_base_v074_signal,
    f26ic_f26_intangible_content_base_durabletilt_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_INTANGIBLE_CONTENT_BASE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc",
        "opex", "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin",
        "netinc", "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps",
        "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex",
        "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory",
        "receivables", "payables", "equity", "retearn", "workingcapital", "debt",
        "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio",
        "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp",
        "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield", "payoutratio",
        "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    def _wig(seed, amp):
        # idiosyncratic positive multiplicative wiggle (quarterly-reset random walk on
        # top of the smooth _fund path) so structurally distinct formulas decorrelate.
        g = np.random.default_rng(seed)
        w = np.cumsum(g.normal(0.0, amp, n))
        w = w - pd.Series(w).rolling(126, min_periods=1).mean().values
        return np.exp(w)

    # assets is the whole balance sheet; intangibles + tangibles are subsets of assets.
    # Build positive fraction series so intangibles, tangibles each < assets and
    # intangibles + tangibles <= assets at all times.
    assets = _fund(2601, base=1.0e9, drift=0.030, vol=0.06).rename("assets")
    assets = (assets * _wig(3601, 0.022)).rename("assets")
    # intangible share wanders ~0.16-0.36 (content/IP heavy comm-services)
    ishare = _fund(2602, base=0.30, drift=0.010, vol=0.05)
    ishare = (0.16 + 0.20 * (ishare / ishare.iloc[0]).clip(0.6, 1.4) / 1.4) * _wig(3602, 0.030)
    intangibles = (assets * ishare).rename("intangibles")
    # tangible share wanders ~0.18-0.34, kept so that ishare+tshare < ~0.80
    tshare = _fund(2603, base=0.28, drift=0.008, vol=0.045)
    tshare = (0.18 + 0.16 * (tshare / tshare.iloc[0]).clip(0.6, 1.4) / 1.4) * _wig(3603, 0.026)
    tangibles = (assets * tshare).rename("tangibles")
    # ppnenet is the physical platform (subset of tangibles in spirit), distinct path
    ppshare = _fund(2604, base=0.16, drift=0.012, vol=0.06)
    ppshare = (0.09 + 0.11 * (ppshare / ppshare.iloc[0]).clip(0.6, 1.4) / 1.4) * _wig(3604, 0.034)
    ppnenet = (assets * ppshare).rename("ppnenet")
    # depamor: amortization/depreciation expense, ~5-12% of the content+platform base, own path
    dpace = _fund(2605, base=0.08, drift=0.006, vol=0.10)
    dpace = (0.05 + 0.09 * (dpace / dpace.iloc[0]).clip(0.5, 1.6) / 1.6) * _wig(3605, 0.050)
    depamor = ((intangibles + ppnenet) * dpace).rename("depamor")

    # sanity: subsets of assets, all positive
    assert (intangibles > 0).all() and (tangibles > 0).all()
    assert (ppnenet > 0).all() and (depamor > 0).all() and (assets > 0).all()
    assert (intangibles < assets).all() and (tangibles < assets).all()
    assert ((intangibles + tangibles) <= assets).all()

    cols = {
        "intangibles": intangibles,
        "assets": assets,
        "depamor": depamor,
        "ppnenet": ppnenet,
        "tangibles": tangibles,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f26_intangible_content_base_base_001_075_claude: %d features pass" % n_features)
