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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== family ownership primitives (institutional accumulation, sf3a) =====
def _f45_growth(s, w):
    # log growth of an ownership level over w days
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f45_roc(s, w):
    # simple rate-of-change of an ownership level
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f45_slope(s, w):
    # normalized trailing slope (per-day) of an ownership level, scaled by level
    def _f(a):
        x = np.arange(len(a), dtype=float)
        xc = x - x.mean()
        denom = (xc * xc).sum()
        if denom == 0:
            return np.nan
        return float((xc * (a - a.mean())).sum() / denom)

    raw = s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)
    return raw / _mean(s, w).replace(0, np.nan)


def _f45_share(s, w):
    # current level relative to trailing-mean level (accumulation share)
    return s / _mean(s, w).replace(0, np.nan)


def _f45_avgsize(value, units):
    # average position value per holder/unit (smart-money concentration)
    return value / units.replace(0, np.nan)


# ============================================================
# inst-holder-count trend: 63d log growth of holder count
def f45ia_f45_institutional_accumulation_holdgrow_63d_base_v001_signal(shrholders):
    b = _f45_growth(shrholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-holder-count trend: 126d log growth of holder count
def f45ia_f45_institutional_accumulation_holdgrow_126d_base_v002_signal(shrholders):
    b = _f45_growth(shrholders, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-holder-count trend: 252d log growth of holder count
def f45ia_f45_institutional_accumulation_holdgrow_252d_base_v003_signal(shrholders):
    b = _f45_growth(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-value trend: 63d log growth of total institutional value
def f45ia_f45_institutional_accumulation_valgrow_63d_base_v004_signal(shrvalue):
    b = _f45_growth(shrvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-value trend: 126d log growth of institutional value
def f45ia_f45_institutional_accumulation_valgrow_126d_base_v005_signal(shrvalue):
    b = _f45_growth(shrvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-value trend: 252d log growth of institutional value
def f45ia_f45_institutional_accumulation_valgrow_252d_base_v006_signal(shrvalue):
    b = _f45_growth(shrvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-value growth: 63d growth of aggregate totalvalue
def f45ia_f45_institutional_accumulation_totvalgrow_63d_base_v007_signal(totalvalue):
    b = _f45_growth(totalvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-value growth: 126d growth of aggregate totalvalue
def f45ia_f45_institutional_accumulation_totvalgrow_126d_base_v008_signal(totalvalue):
    b = _f45_growth(totalvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-units trend: 63d growth of shares held (units accumulation)
def f45ia_f45_institutional_accumulation_unitgrow_63d_base_v009_signal(shrunits):
    b = _f45_growth(shrunits, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-units trend: 126d growth of shares held
def f45ia_f45_institutional_accumulation_unitgrow_126d_base_v010_signal(shrunits):
    b = _f45_growth(shrunits, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-units trend: 252d growth of shares held
def f45ia_f45_institutional_accumulation_unitgrow_252d_base_v011_signal(shrunits):
    b = _f45_growth(shrunits, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst ownership %: shrvalue relative to marketcap (institutional ownership fraction)
def f45ia_f45_institutional_accumulation_ownpct_base_v012_signal(shrvalue, marketcap):
    b = shrvalue / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# broad ownership coverage intensity: totalvalue/marketcap vs its own 252d baseline
def f45ia_f45_institutional_accumulation_totownpct_base_v013_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own / _mean(own, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst ownership % momentum: change in shrvalue/marketcap over a quarter
def f45ia_f45_institutional_accumulation_ownpctmom_63d_base_v014_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = own - own.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst ownership % momentum: change in shrvalue/marketcap over half year
def f45ia_f45_institutional_accumulation_ownpctmom_126d_base_v015_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = own - own.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation momentum: holder-count ROC over a month
def f45ia_f45_institutional_accumulation_holdroc_21d_base_v016_signal(shrholders):
    b = _f45_roc(shrholders, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation momentum: units ROC over a month
def f45ia_f45_institutional_accumulation_unitroc_21d_base_v017_signal(shrunits):
    b = _f45_roc(shrunits, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money inflow: average position value per holder (concentration level)
def f45ia_f45_institutional_accumulation_avgpos_base_v018_signal(shrvalue, shrholders):
    b = _f45_avgsize(shrvalue, shrholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money inflow: growth of average position value per holder
def f45ia_f45_institutional_accumulation_avgposgrow_63d_base_v019_signal(shrvalue, shrholders):
    avg = shrvalue / shrholders.replace(0, np.nan)
    b = _f45_growth(avg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money inflow: average value per share-unit (price-implied position quality)
def f45ia_f45_institutional_accumulation_valperunit_base_v020_signal(shrvalue, shrunits):
    b = _f45_avgsize(shrvalue, shrunits)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count share: holders vs trailing 252d mean (breadth surge)
def f45ia_f45_institutional_accumulation_holdshare_252d_base_v021_signal(shrholders):
    b = _f45_share(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value share: shrvalue vs trailing 252d mean (value surge)
def f45ia_f45_institutional_accumulation_valshare_252d_base_v022_signal(shrvalue):
    b = _f45_share(shrvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units share: shrunits vs trailing 126d mean (position surge)
def f45ia_f45_institutional_accumulation_unitshare_126d_base_v023_signal(shrunits):
    b = _f45_share(shrunits, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count z-score vs its 252d history (de-trended breadth extremity)
def f45ia_f45_institutional_accumulation_holdz_252d_base_v024_signal(shrholders):
    b = _z(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value z-score vs its 252d history (de-trended value extremity)
def f45ia_f45_institutional_accumulation_valz_252d_base_v025_signal(shrvalue):
    b = _z(shrvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units z-score vs its 126d history
def f45ia_f45_institutional_accumulation_unitz_126d_base_v026_signal(shrunits):
    b = _z(shrunits, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count accumulation efficiency: net change / total path traveled over 126d
def f45ia_f45_institutional_accumulation_holdeff_126d_base_v027_signal(shrholders):
    net = (shrholders - shrholders.shift(126)).abs()
    path = shrholders.diff().abs().rolling(126, min_periods=42).sum()
    b = np.sign(shrholders - shrholders.shift(126)) * net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trailing slope of institutional value (normalized value trend)
def f45ia_f45_institutional_accumulation_valslope_126d_base_v028_signal(shrvalue):
    b = _f45_slope(shrvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trailing slope of share-units (normalized position trend)
def f45ia_f45_institutional_accumulation_unitslope_126d_base_v029_signal(shrunits):
    b = _f45_slope(shrunits, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth-vs-position: holder growth minus unit growth (more holders vs bigger blocks)
def f45ia_f45_institutional_accumulation_breadthspr_63d_base_v030_signal(shrholders, shrunits):
    b = _f45_growth(shrholders, 63) - _f45_growth(shrunits, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-vs-value divergence: unit growth minus value growth (price-effect stripped flow)
def f45ia_f45_institutional_accumulation_unitvaldiv_63d_base_v031_signal(shrunits, shrvalue):
    b = _f45_growth(shrunits, 63) - _f45_growth(shrvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value vs marketcap growth: are institutions outpacing the cap (relative accumulation)
def f45ia_f45_institutional_accumulation_valvscap_63d_base_v032_signal(shrvalue, marketcap):
    b = _f45_growth(shrvalue, 63) - _f45_growth(marketcap, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units vs marketcap growth: real share accumulation net of cap moves
def f45ia_f45_institutional_accumulation_unitvscap_126d_base_v033_signal(shrunits, marketcap):
    b = _f45_growth(shrunits, 126) - _f45_growth(marketcap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation acceleration proxy: holder growth now vs a quarter ago
def f45ia_f45_institutional_accumulation_holdgrowmom_base_v034_signal(shrholders):
    g = _f45_growth(shrholders, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value growth momentum: value growth now vs a quarter ago
def f45ia_f45_institutional_accumulation_valgrowmom_base_v035_signal(shrvalue):
    g = _f45_growth(shrvalue, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst ownership % z-scored vs its own 252d history (ownership extremity)
def f45ia_f45_institutional_accumulation_ownpctz_252d_base_v036_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = _z(own, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count percentile-ranked vs own 504d history (breadth rank)
def f45ia_f45_institutional_accumulation_holdrank_504d_base_v037_signal(shrholders):
    b = shrholders.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value percentile-ranked vs own 504d history (value rank)
def f45ia_f45_institutional_accumulation_valrank_504d_base_v038_signal(shrvalue):
    b = shrvalue.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units percentile-ranked vs own 504d history (position rank)
def f45ia_f45_institutional_accumulation_unitrank_504d_base_v039_signal(shrunits):
    b = shrunits.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money block concentration: avg holder stake as fraction of company cap
def f45ia_f45_institutional_accumulation_blockconc_base_v040_signal(shrvalue, shrholders, marketcap):
    per_holder = shrvalue / shrholders.replace(0, np.nan)
    b = per_holder / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average shares per holder (position-size in units, conviction proxy)
def f45ia_f45_institutional_accumulation_unitsperhold_base_v041_signal(shrunits, shrholders):
    b = shrunits / shrholders.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth of average shares per holder (conviction building)
def f45ia_f45_institutional_accumulation_unitsperholdgrow_126d_base_v042_signal(shrunits, shrholders):
    uph = shrunits / shrholders.replace(0, np.nan)
    b = _f45_growth(uph, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money inflow: dollar inflow rate = change in shrvalue scaled by its own level
def f45ia_f45_institutional_accumulation_inflow_21d_base_v043_signal(shrvalue):
    b = (shrvalue - shrvalue.shift(21)) / _mean(shrvalue, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unit accumulation breadth: fraction of last half-year with positive 21d unit growth
def f45ia_f45_institutional_accumulation_unitaccfrac_base_v044_signal(shrunits):
    pos = (_f45_growth(shrunits, 21) > 0).astype(float)
    b = pos.rolling(126, min_periods=42).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage gap: shrvalue vs totalvalue (active-inst share of all reported value)
def f45ia_f45_institutional_accumulation_coverage_base_v045_signal(shrvalue, totalvalue):
    b = shrvalue / totalvalue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend: change in shrvalue/totalvalue over a quarter
def f45ia_f45_institutional_accumulation_coveragemom_63d_base_v046_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = cov - cov.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation persistence: fraction of last quarter holder count rose day-over-day
def f45ia_f45_institutional_accumulation_holdupfrac_63d_base_v047_signal(shrholders):
    up = (shrholders.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation persistence: fraction of last quarter units rose day-over-day
def f45ia_f45_institutional_accumulation_unitupfrac_63d_base_v048_signal(shrunits):
    up = (shrunits.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-build persistence: fraction of last half-year ownership%-of-cap rose vs 21d ago
def f45ia_f45_institutional_accumulation_ownbuild_base_v049_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    up = (own > own.shift(21)).astype(float)
    b = up.rolling(126, min_periods=42).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long value-growth spread (accumulation acceleration via windows)
def f45ia_f45_institutional_accumulation_valgrowspr_base_v050_signal(shrvalue):
    b = _f45_roc(shrvalue, 63) - _f45_roc(shrvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long holder-growth spread (breadth acceleration via windows)
def f45ia_f45_institutional_accumulation_holdgrowspr_base_v051_signal(shrholders):
    b = _f45_roc(shrholders, 63) - _f45_roc(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long unit-growth spread (position acceleration via windows)
def f45ia_f45_institutional_accumulation_unitgrowspr_base_v052_signal(shrunits):
    b = _f45_roc(shrunits, 63) - _f45_roc(shrunits, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# broad ownership percentile: totalvalue/marketcap ranked vs own 504d history
def f45ia_f45_institutional_accumulation_ownrank_504d_base_v053_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count vs units divergence ranked (crowd-vs-conviction regime)
def f45ia_f45_institutional_accumulation_crowdconv_base_v054_signal(shrholders, shrunits):
    spr = _f45_growth(shrholders, 126) - _f45_growth(shrunits, 126)
    b = spr.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed value-per-holder re-rating (bounded smart-money position-quality flow)
def f45ia_f45_institutional_accumulation_vphtanh_base_v055_signal(shrvalue, shrholders):
    avg = shrvalue / shrholders.replace(0, np.nan)
    chg = _f45_growth(avg, 21)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of holder-growth (asymmetric breadth signal)
def f45ia_f45_institutional_accumulation_holdsignmag_base_v056_signal(shrholders):
    g = _f45_growth(shrholders, 63)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value accumulation streak: count of last 126d with positive 21d value growth
def f45ia_f45_institutional_accumulation_valstreak_base_v057_signal(shrvalue):
    pos = (_f45_growth(shrvalue, 21) > 0).astype(float)
    b = pos.rolling(126, min_periods=42).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder z-score (block conviction extremity)
def f45ia_f45_institutional_accumulation_uphz_252d_base_v058_signal(shrunits, shrholders):
    uph = shrunits / shrholders.replace(0, np.nan)
    b = _z(uph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership %-of-cap acceleration: 63d ownership momentum now vs one quarter ago
def f45ia_f45_institutional_accumulation_ownaccel_base_v059_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    mom = own - own.shift(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit growth (implied per-share value re-rating by inst)
def f45ia_f45_institutional_accumulation_vpugrow_126d_base_v060_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    b = _f45_growth(vpu, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth-quality: holder slope x value slope sign agreement
def f45ia_f45_institutional_accumulation_accqual_base_v061_signal(shrholders, shrvalue):
    hs = _f45_slope(shrholders, 126)
    vs = _f45_slope(shrvalue, 126)
    b = np.sign(hs) * np.sign(vs) * (hs.abs() + vs.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-value vs shrvalue gap growth (passive/other ownership build)
def f45ia_f45_institutional_accumulation_othervalgrow_126d_base_v062_signal(totalvalue, shrvalue):
    other = (totalvalue - shrvalue).clip(lower=0)
    b = _f45_growth(other + 1.0, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count drawup: holders vs trailing 252d max (distance below breadth peak)
def f45ia_f45_institutional_accumulation_holddrawup_base_v063_signal(shrholders):
    peak = _rmax(shrholders, 252)
    b = shrholders / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value distance above trailing 252d min (recovery in inst value)
def f45ia_f45_institutional_accumulation_valrecov_base_v064_signal(shrvalue):
    trough = _rmin(shrvalue, 252)
    b = shrvalue / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units new-high frequency: fraction of last quarter shrunits made a 252d high
def f45ia_f45_institutional_accumulation_unitnewhi_base_v065_signal(shrunits):
    hi = _rmax(shrunits, 252)
    is_hi = (shrunits >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inflow risk-adjusted: 63d value growth per unit of its own volatility
def f45ia_f45_institutional_accumulation_riskadjflow_base_v066_signal(shrvalue):
    g = _f45_growth(shrvalue, 63)
    vol = _f45_growth(shrvalue, 21).rolling(126, min_periods=42).std()
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep+broad accumulation: ownership%-momentum interacted with holder-breadth growth
def f45ia_f45_institutional_accumulation_deepbroad_base_v067_signal(shrvalue, marketcap, shrholders):
    own = shrvalue / marketcap.replace(0, np.nan)
    own_mom = own - own.shift(63)
    breadth_g = _f45_growth(shrholders, 63)
    b = own_mom * breadth_g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-growth dispersion across 63/126/252 windows (consistency of accumulation)
def f45ia_f45_institutional_accumulation_growdisp_base_v068_signal(shrvalue):
    g1 = _f45_roc(shrvalue, 63)
    g2 = _f45_roc(shrvalue, 126)
    g3 = _f45_roc(shrvalue, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue/marketcap momentum over half-year (broad ownership build vs price)
def f45ia_f45_institutional_accumulation_totownmom_126d_base_v069_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own - own.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count year-over-year change in growth (annual breadth shift)
def f45ia_f45_institutional_accumulation_holdyoy_base_v070_signal(shrholders):
    g = _f45_growth(shrholders, 21)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value flow stability: coefficient of variation of 21d value-growth over 126d (steadiness)
def f45ia_f45_institutional_accumulation_valstability_base_v071_signal(shrvalue):
    g = _f45_growth(shrvalue, 21)
    mu = g.rolling(126, min_periods=42).mean()
    sd = g.rolling(126, min_periods=42).std()
    b = mu / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# avg-position-value rank vs own 504d history (smart-money sizing percentile)
def f45ia_f45_institutional_accumulation_avgposrank_base_v072_signal(shrvalue, shrholders):
    avg = shrvalue / shrholders.replace(0, np.nan)
    b = avg.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net accumulation composite: unit-growth x ownership%-level (real + deep buying)
def f45ia_f45_institutional_accumulation_netacc_base_v073_signal(shrunits, shrvalue, marketcap):
    ug = _f45_growth(shrunits, 63)
    own = shrvalue / marketcap.replace(0, np.nan)
    b = ug * own
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage (shrvalue/totalvalue) z-scored vs 252d history (active-share extremity)
def f45ia_f45_institutional_accumulation_coveragez_base_v074_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation balance: normalized balance of unit inflow vs holder inflow over a quarter
def f45ia_f45_institutional_accumulation_accbalance_base_v075_signal(shrunits, shrholders):
    ug = _f45_growth(shrunits, 63).clip(lower=-1.0, upper=1.0)
    hg = _f45_growth(shrholders, 63).clip(lower=-1.0, upper=1.0)
    b = (ug - hg) / (ug.abs() + hg.abs() + 1e-6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45ia_f45_institutional_accumulation_holdgrow_63d_base_v001_signal,
    f45ia_f45_institutional_accumulation_holdgrow_126d_base_v002_signal,
    f45ia_f45_institutional_accumulation_holdgrow_252d_base_v003_signal,
    f45ia_f45_institutional_accumulation_valgrow_63d_base_v004_signal,
    f45ia_f45_institutional_accumulation_valgrow_126d_base_v005_signal,
    f45ia_f45_institutional_accumulation_valgrow_252d_base_v006_signal,
    f45ia_f45_institutional_accumulation_totvalgrow_63d_base_v007_signal,
    f45ia_f45_institutional_accumulation_totvalgrow_126d_base_v008_signal,
    f45ia_f45_institutional_accumulation_unitgrow_63d_base_v009_signal,
    f45ia_f45_institutional_accumulation_unitgrow_126d_base_v010_signal,
    f45ia_f45_institutional_accumulation_unitgrow_252d_base_v011_signal,
    f45ia_f45_institutional_accumulation_ownpct_base_v012_signal,
    f45ia_f45_institutional_accumulation_totownpct_base_v013_signal,
    f45ia_f45_institutional_accumulation_ownpctmom_63d_base_v014_signal,
    f45ia_f45_institutional_accumulation_ownpctmom_126d_base_v015_signal,
    f45ia_f45_institutional_accumulation_holdroc_21d_base_v016_signal,
    f45ia_f45_institutional_accumulation_unitroc_21d_base_v017_signal,
    f45ia_f45_institutional_accumulation_avgpos_base_v018_signal,
    f45ia_f45_institutional_accumulation_avgposgrow_63d_base_v019_signal,
    f45ia_f45_institutional_accumulation_valperunit_base_v020_signal,
    f45ia_f45_institutional_accumulation_holdshare_252d_base_v021_signal,
    f45ia_f45_institutional_accumulation_valshare_252d_base_v022_signal,
    f45ia_f45_institutional_accumulation_unitshare_126d_base_v023_signal,
    f45ia_f45_institutional_accumulation_holdz_252d_base_v024_signal,
    f45ia_f45_institutional_accumulation_valz_252d_base_v025_signal,
    f45ia_f45_institutional_accumulation_unitz_126d_base_v026_signal,
    f45ia_f45_institutional_accumulation_holdeff_126d_base_v027_signal,
    f45ia_f45_institutional_accumulation_valslope_126d_base_v028_signal,
    f45ia_f45_institutional_accumulation_unitslope_126d_base_v029_signal,
    f45ia_f45_institutional_accumulation_breadthspr_63d_base_v030_signal,
    f45ia_f45_institutional_accumulation_unitvaldiv_63d_base_v031_signal,
    f45ia_f45_institutional_accumulation_valvscap_63d_base_v032_signal,
    f45ia_f45_institutional_accumulation_unitvscap_126d_base_v033_signal,
    f45ia_f45_institutional_accumulation_holdgrowmom_base_v034_signal,
    f45ia_f45_institutional_accumulation_valgrowmom_base_v035_signal,
    f45ia_f45_institutional_accumulation_ownpctz_252d_base_v036_signal,
    f45ia_f45_institutional_accumulation_holdrank_504d_base_v037_signal,
    f45ia_f45_institutional_accumulation_valrank_504d_base_v038_signal,
    f45ia_f45_institutional_accumulation_unitrank_504d_base_v039_signal,
    f45ia_f45_institutional_accumulation_blockconc_base_v040_signal,
    f45ia_f45_institutional_accumulation_unitsperhold_base_v041_signal,
    f45ia_f45_institutional_accumulation_unitsperholdgrow_126d_base_v042_signal,
    f45ia_f45_institutional_accumulation_inflow_21d_base_v043_signal,
    f45ia_f45_institutional_accumulation_unitaccfrac_base_v044_signal,
    f45ia_f45_institutional_accumulation_coverage_base_v045_signal,
    f45ia_f45_institutional_accumulation_coveragemom_63d_base_v046_signal,
    f45ia_f45_institutional_accumulation_holdupfrac_63d_base_v047_signal,
    f45ia_f45_institutional_accumulation_unitupfrac_63d_base_v048_signal,
    f45ia_f45_institutional_accumulation_ownbuild_base_v049_signal,
    f45ia_f45_institutional_accumulation_valgrowspr_base_v050_signal,
    f45ia_f45_institutional_accumulation_holdgrowspr_base_v051_signal,
    f45ia_f45_institutional_accumulation_unitgrowspr_base_v052_signal,
    f45ia_f45_institutional_accumulation_ownrank_504d_base_v053_signal,
    f45ia_f45_institutional_accumulation_crowdconv_base_v054_signal,
    f45ia_f45_institutional_accumulation_vphtanh_base_v055_signal,
    f45ia_f45_institutional_accumulation_holdsignmag_base_v056_signal,
    f45ia_f45_institutional_accumulation_valstreak_base_v057_signal,
    f45ia_f45_institutional_accumulation_uphz_252d_base_v058_signal,
    f45ia_f45_institutional_accumulation_ownaccel_base_v059_signal,
    f45ia_f45_institutional_accumulation_vpugrow_126d_base_v060_signal,
    f45ia_f45_institutional_accumulation_accqual_base_v061_signal,
    f45ia_f45_institutional_accumulation_othervalgrow_126d_base_v062_signal,
    f45ia_f45_institutional_accumulation_holddrawup_base_v063_signal,
    f45ia_f45_institutional_accumulation_valrecov_base_v064_signal,
    f45ia_f45_institutional_accumulation_unitnewhi_base_v065_signal,
    f45ia_f45_institutional_accumulation_riskadjflow_base_v066_signal,
    f45ia_f45_institutional_accumulation_deepbroad_base_v067_signal,
    f45ia_f45_institutional_accumulation_growdisp_base_v068_signal,
    f45ia_f45_institutional_accumulation_totownmom_126d_base_v069_signal,
    f45ia_f45_institutional_accumulation_holdyoy_base_v070_signal,
    f45ia_f45_institutional_accumulation_valstability_base_v071_signal,
    f45ia_f45_institutional_accumulation_avgposrank_base_v072_signal,
    f45ia_f45_institutional_accumulation_netacc_base_v073_signal,
    f45ia_f45_institutional_accumulation_coveragez_base_v074_signal,
    f45ia_f45_institutional_accumulation_accbalance_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_INSTITUTIONAL_ACCUMULATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
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

    # ownership columns: all positive with upward trend so accumulation features vary
    shrholders = _fund(101, base=350.0, drift=0.05, vol=0.10).rename("shrholders")
    shrunits = _fund(102, base=4.0e7, drift=0.06, vol=0.12).rename("shrunits")
    shrvalue = _fund(103, base=6.0e8, drift=0.05, vol=0.11).rename("shrvalue")
    totalvalue = _fund(104, base=9.0e8, drift=0.045, vol=0.10).rename("totalvalue")
    marketcap = _fund(105, base=1.5e9, drift=0.035, vol=0.13).rename("marketcap")

    cols = {
        "shrholders": shrholders, "shrunits": shrunits, "shrvalue": shrvalue,
        "totalvalue": totalvalue, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
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

    print("OK f45_institutional_accumulation_base_001_075_claude: %d features pass" % n_features)
