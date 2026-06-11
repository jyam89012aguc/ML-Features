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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (warrant / options OVERHANG & derivative-value magnitude) =====
# NOTE: this family is OVERHANG / EXISTENCE & derivative-value MAGNITUDE.
# It deliberately does NOT compute the put-vs-call skew putvalue/(putvalue+cllvalue)
# nor holder-type fund/und/prf composition (those belong to f51_ownership_mix_concentration),
# and does NOT compute the institutional shrvalue/holder accumulation trend (f45).
def _f46_intensity(value, marketcap):
    # overhang / positioning intensity vs market cap
    return value / marketcap.replace(0, np.nan)


def _f46_share(part, whole):
    # derivative-value share of a whole (e.g. value/totalvalue)
    return part / whole.replace(0, np.nan)


def _f46_per_holder(value, holders):
    # average claim size per derivative holder (overhang concentration proxy)
    return value / holders.replace(0, np.nan)


def _f46_accum(s, w):
    # overhang accumulation momentum: log change over window
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f46_presence(s, w):
    # fraction of the trailing window in which a claim type is present (>0)
    return (s > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# ---- warrant overhang = wntvalue/marketcap (latent dilution) ----
# warrant overhang level (latent-dilution intensity vs market cap)
def f46ow_f46_options_warrant_positioning_wntoverhang_lvl_base_v001_signal(wntvalue, marketcap):
    b = _f46_intensity(wntvalue, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang vs total ownership value (latent dilution share of sf3a base)
def f46ow_f46_options_warrant_positioning_wntshare_lvl_base_v002_signal(wntvalue, totalvalue):
    b = _f46_share(wntvalue, totalvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang z-scored vs its own year (dilution-overhang regime shift)
def f46ow_f46_options_warrant_positioning_wntoverz_252d_base_v003_signal(wntvalue, marketcap):
    raw = _f46_intensity(wntvalue, marketcap)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang accumulation (half-year log build of latent dilution)
def f46ow_f46_options_warrant_positioning_wntaccum_126d_base_v004_signal(wntvalue):
    b = _f46_accum(wntvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang dispersion (rolling std of wnt/marketcap; dilution instability)
def f46ow_f46_options_warrant_positioning_wntovervol_126d_base_v005_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant-value coefficient-of-variation (dilution-value instability normalized by level)
def f46ow_f46_options_warrant_positioning_wntcv_126d_base_v006_signal(wntvalue):
    b = _std(wntvalue, 126) / _mean(wntvalue, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant per-holder claim size (overhang concentration), de-trended
def f46ow_f46_options_warrant_positioning_wntperhld_252d_base_v007_signal(wntvalue, wntholders):
    pp = _f46_per_holder(wntvalue, wntholders)
    b = _z(pp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant-presence regime: fraction of trailing year with any warrant value (existence)
def f46ow_f46_options_warrant_positioning_wntpresence_252d_base_v008_signal(wntvalue):
    b = _f46_presence(wntvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- debt / convert overhang = dbtvalue/totalvalue & dbtvalue/marketcap ----
# convert/debt overhang vs market cap (latent leverage claim intensity)
def f46ow_f46_options_warrant_positioning_dbtoverhang_lvl_base_v009_signal(dbtvalue, marketcap):
    b = _f46_intensity(dbtvalue, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert/debt overhang as share of total ownership value (leverage mix)
def f46ow_f46_options_warrant_positioning_dbtshare_lvl_base_v010_signal(dbtvalue, totalvalue):
    b = _f46_share(dbtvalue, totalvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang z-scored vs its own year (leverage-overhang regime)
def f46ow_f46_options_warrant_positioning_dbtoverz_252d_base_v011_signal(dbtvalue, marketcap):
    raw = _f46_intensity(dbtvalue, marketcap)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang accumulation (half-year log build of leverage claim)
def f46ow_f46_options_warrant_positioning_dbtaccum_126d_base_v012_signal(dbtvalue):
    b = _f46_accum(dbtvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang dispersion (rolling std of dbt/marketcap; leverage instability)
def f46ow_f46_options_warrant_positioning_dbtovervol_126d_base_v013_signal(dbtvalue, marketcap):
    r = _f46_intensity(dbtvalue, marketcap)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert per-holder claim size, de-trended (convert concentration)
def f46ow_f46_options_warrant_positioning_dbtperhld_252d_base_v014_signal(dbtvalue, dbtholders):
    pp = _f46_per_holder(dbtvalue, dbtholders)
    b = _z(pp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert-presence regime: fraction of trailing year with any convert value
def f46ow_f46_options_warrant_positioning_dbtpresence_252d_base_v015_signal(dbtvalue):
    b = _f46_presence(dbtvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- put VALUE magnitude vs marketcap (positioning intensity, NOT skew) ----
# put-value positioning intensity vs market cap (downside-positioning magnitude)
def f46ow_f46_options_warrant_positioning_putintens_lvl_base_v016_signal(putvalue, marketcap):
    b = _f46_intensity(putvalue, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value intensity z-scored vs its own year (de-trended positioning surge)
def f46ow_f46_options_warrant_positioning_putintensz_252d_base_v017_signal(putvalue, marketcap):
    raw = _f46_intensity(putvalue, marketcap)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value intensity ranked vs 504d (positioning-crowding percentile)
def f46ow_f46_options_warrant_positioning_putintensrank_504d_base_v018_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value intensity dispersion (rolling std of put/marketcap; positioning instability)
def f46ow_f46_options_warrant_positioning_putintensvol_126d_base_v019_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- call VALUE magnitude vs marketcap (positioning intensity, NOT skew) ----
# call-value positioning intensity vs market cap (upside-positioning magnitude)
def f46ow_f46_options_warrant_positioning_cllintens_lvl_base_v020_signal(cllvalue, marketcap):
    b = _f46_intensity(cllvalue, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-value intensity z-scored vs its own year (de-trended positioning surge)
def f46ow_f46_options_warrant_positioning_cllintensz_252d_base_v021_signal(cllvalue, marketcap):
    raw = _f46_intensity(cllvalue, marketcap)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-value intensity ranked vs 504d (positioning-crowding percentile)
def f46ow_f46_options_warrant_positioning_cllintensrank_504d_base_v022_signal(cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-value intensity dispersion (rolling std of call/marketcap)
def f46ow_f46_options_warrant_positioning_cllintensvol_126d_base_v023_signal(cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- TOTAL options value magnitude (put+call) vs marketcap ----
# total options value (put+call) intensity vs market cap (gross derivative-value footprint)
def f46ow_f46_options_warrant_positioning_optintens_lvl_base_v024_signal(putvalue, cllvalue, marketcap):
    b = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options value intensity z-scored vs year (gross options-value regime)
def f46ow_f46_options_warrant_positioning_optintensz_252d_base_v025_signal(putvalue, cllvalue, marketcap):
    r = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options value accumulation over a quarter (options-value flow magnitude)
def f46ow_f46_options_warrant_positioning_optaccum_63d_base_v026_signal(putvalue, cllvalue):
    b = _f46_accum(putvalue + cllvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- derivative-value SHARE of total ownership (magnitude mix, NOT composition) ----
# total derivative value (put+call+wnt+dbt) as share of total ownership value
def f46ow_f46_options_warrant_positioning_derivvalshare_lvl_base_v027_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    deriv = putvalue + cllvalue + wntvalue + dbtvalue
    b = deriv / totalvalue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total derivative value share, z-scored vs year (non-equity-claim regime)
def f46ow_f46_options_warrant_positioning_derivvalsharez_252d_base_v028_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    deriv = putvalue + cllvalue + wntvalue + dbtvalue
    sh = deriv / totalvalue.replace(0, np.nan)
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant dominance within structural claims: smoothed wnt / (wnt + dbt) (which channel leads)
# distinct from any dbt-over-X feature because it isolates the warrant fraction of structural overhang.
def f46ow_f46_options_warrant_positioning_wntdominance_lvl_base_v029_signal(wntvalue, dbtvalue):
    raw = wntvalue / (wntvalue + dbtvalue).replace(0, np.nan)
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tradable-options value (put+call) as share of total ownership value
def f46ow_f46_options_warrant_positioning_optshare_lvl_base_v030_signal(putvalue, cllvalue, totalvalue):
    b = (putvalue + cllvalue) / totalvalue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- structural-dilution (warrant/convert) vs tradable-options balance ----
# structural-claim (wnt+dbt) overhang RELATIVE to tradable-options value (supply-vs-positioning ratio)
# distinct from raw dbt-overhang even when warrants are absent, because the denominator is options value.
def f46ow_f46_options_warrant_positioning_structvsopt_lvl_base_v031_signal(wntvalue, dbtvalue, putvalue, cllvalue):
    struct = wntvalue + dbtvalue
    opt = (putvalue + cllvalue).replace(0, np.nan)
    b = struct / opt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structural-overhang-to-options ratio ranked vs 504d (supply-vs-positioning percentile regime)
def f46ow_f46_options_warrant_positioning_structvsoptrank_504d_base_v032_signal(wntvalue, dbtvalue, putvalue, cllvalue):
    struct = wntvalue + dbtvalue
    opt = (putvalue + cllvalue).replace(0, np.nan)
    b = _rank(struct / opt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structural-overhang weight of full derivative value, accumulation over a quarter
# (is the structural-supply share of total derivative value building or fading?)
def f46ow_f46_options_warrant_positioning_structweightmom_63d_base_v033_signal(wntvalue, dbtvalue, putvalue, cllvalue):
    struct = wntvalue + dbtvalue
    full = (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)
    sh = struct / full
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- overhang vs equity value (latent claim relative to existing long base) ----
# warrant overhang relative to existing equity ownership value (dilution-to-equity)
def f46ow_f46_options_warrant_positioning_wntvsequity_lvl_base_v034_signal(wntvalue, shrvalue):
    b = _f46_share(wntvalue, shrvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang relative to existing equity ownership value, half-year momentum (leverage-to-equity build)
def f46ow_f46_options_warrant_positioning_dbtvsequitymom_126d_base_v035_signal(dbtvalue, shrvalue):
    r = _f46_share(dbtvalue, shrvalue)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value magnitude relative to existing equity ownership value (positioning-to-equity)
def f46ow_f46_options_warrant_positioning_putvsequity_lvl_base_v036_signal(putvalue, shrvalue):
    b = _f46_share(putvalue, shrvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-value magnitude relative to existing equity ownership value
def f46ow_f46_options_warrant_positioning_cllvsequity_lvl_base_v037_signal(cllvalue, shrvalue):
    b = _f46_share(cllvalue, shrvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- holder-breadth of derivative existence (count-based, OVERHANG breadth) ----
# warrant-holder breadth z-scored vs year (dilution-holder existence breadth)
def f46ow_f46_options_warrant_positioning_wnthldbreadth_252d_base_v038_signal(wntholders):
    b = _z(wntholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert-holder breadth z-scored vs year (leverage-holder existence breadth)
def f46ow_f46_options_warrant_positioning_dbthldbreadth_252d_base_v039_signal(dbtholders):
    b = _z(dbtholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder breadth ranked vs 504d (downside-positioning breadth percentile)
def f46ow_f46_options_warrant_positioning_puthldrank_504d_base_v040_signal(putholders):
    b = _rank(putholders, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-holder breadth ranked vs 504d (upside-positioning breadth percentile)
def f46ow_f46_options_warrant_positioning_cllhldrank_504d_base_v041_signal(cllholders):
    b = _rank(cllholders, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total derivative-holder breadth (put+call+wnt+dbt) z-scored vs year
def f46ow_f46_options_warrant_positioning_derivbreadth_252d_base_v042_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = putholders + cllholders + wntholders + dbtholders
    b = _z(deriv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- per-holder concentration of positioning (value/holder magnitude) ----
# put per-holder claim size, de-trended (positioning concentration)
def f46ow_f46_options_warrant_positioning_putperhld_252d_base_v043_signal(putvalue, putholders):
    pp = _f46_per_holder(putvalue, putholders)
    b = _z(pp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call per-holder claim size, de-trended (positioning concentration)
def f46ow_f46_options_warrant_positioning_cllperhld_252d_base_v044_signal(cllvalue, cllholders):
    cp = _f46_per_holder(cllvalue, cllholders)
    b = _z(cp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- momentum facets of overhang / intensity ----
# warrant overhang momentum (quarterly change in wnt/marketcap; dilution build rate)
def f46ow_f46_options_warrant_positioning_wntovermom_63d_base_v045_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang momentum (quarterly change in dbt/marketcap)
def f46ow_f46_options_warrant_positioning_dbtovermom_63d_base_v046_signal(dbtvalue, marketcap):
    r = _f46_intensity(dbtvalue, marketcap)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity momentum (quarterly change in put/marketcap; positioning build rate)
def f46ow_f46_options_warrant_positioning_putintensmom_63d_base_v047_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity momentum (quarterly change in call/marketcap)
def f46ow_f46_options_warrant_positioning_cllintensmom_63d_base_v048_signal(cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- stretch / drawdown vs own peak (overhang extremity, distinct nonlinearity) ----
# warrant overhang stretch vs its 252d max (overhang relative to historical peak)
def f46ow_f46_options_warrant_positioning_wntoverstretch_252d_base_v049_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = r / _rmax(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity stretch vs its 252d max (positioning relative to peak)
def f46ow_f46_options_warrant_positioning_putintensstretch_252d_base_v050_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = r / _rmax(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity drawdown from its 252d peak (positioning cooling-off depth)
def f46ow_f46_options_warrant_positioning_cllintensdd_252d_base_v051_signal(cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    b = r / _rmax(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang stretch vs 504d max (leverage-claim supply vs 2yr peak)
def f46ow_f46_options_warrant_positioning_dbtoverstretch_504d_base_v052_signal(dbtvalue, marketcap):
    r = _f46_intensity(dbtvalue, marketcap)
    b = r / _rmax(r, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- sign x magnitude compression facets ----
# put intensity sign-magnitude vs typical level (compression-adjusted positioning extremity)
def f46ow_f46_options_warrant_positioning_putsignmag_252d_base_v053_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    dev = r - _mean(r, 252)
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang sign-magnitude vs typical (compression-adjusted dilution extremity)
def f46ow_f46_options_warrant_positioning_wntsignmag_252d_base_v054_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    dev = r - _mean(r, 252)
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- displacement from own slow EMA (overhang trend deviation) ----
# warrant overhang vs its long EMA (dilution displacement from trend)
def f46ow_f46_options_warrant_positioning_wntoverdisp_base_v055_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = r / r.ewm(span=126, min_periods=42).mean().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity vs its long EMA (positioning displacement from trend)
def f46ow_f46_options_warrant_positioning_putintensdisp_base_v056_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = r / r.ewm(span=126, min_periods=42).mean().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- value-vs-holder concentration divergence (value grows faster than breadth) ----
# warrant value-vs-holder divergence over half-year, pct-growth form (overhang concentrating)
def f46ow_f46_options_warrant_positioning_wntconcdiv_126d_base_v057_signal(wntvalue, wntholders):
    vg = _roc(wntvalue, 126)
    hg = _roc(wntholders, 126)
    b = vg - hg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put value-vs-holder divergence over a quarter, pct-growth form (positioning concentrating)
def f46ow_f46_options_warrant_positioning_putconcdiv_63d_base_v058_signal(putvalue, putholders):
    vg = _roc(putvalue, 63)
    hg = _roc(putholders, 63)
    b = vg - hg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call value-vs-holder divergence over a quarter, pct-growth form
def f46ow_f46_options_warrant_positioning_cllconcdiv_63d_base_v059_signal(cllvalue, cllholders):
    vg = _roc(cllvalue, 63)
    hg = _roc(cllholders, 63)
    b = vg - hg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- overhang per-marketcap interaction with coverage (existence x footprint) ----
# warrant overhang gated by ownership coverage (coverage-weighted dilution risk)
def f46ow_f46_options_warrant_positioning_covdilrisk_lvl_base_v060_signal(percentoftotal, wntvalue, marketcap):
    over = _f46_intensity(wntvalue, marketcap)
    b = over * percentoftotal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put positioning intensity gated by ownership coverage (coverage-weighted positioning)
def f46ow_f46_options_warrant_positioning_covputpos_lvl_base_v061_signal(percentoftotal, putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = r * percentoftotal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- combined claim overhang vs marketcap (full derivative footprint magnitude) ----
# full claim (put+call+wnt+dbt) value vs marketcap, z-scored (total derivative footprint regime)
def f46ow_f46_options_warrant_positioning_claimfootprint_252d_base_v062_signal(putvalue, cllvalue, wntvalue, dbtvalue, marketcap):
    claim = putvalue + cllvalue + wntvalue + dbtvalue
    b = _z(claim / marketcap.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full claim (put+call+wnt+dbt) value per total derivative holder (avg claim size across all derivative holders)
def f46ow_f46_options_warrant_positioning_claimperhld_252d_base_v063_signal(putvalue, cllvalue, wntvalue, dbtvalue, putholders, cllholders, wntholders, dbtholders):
    claim = putvalue + cllvalue + wntvalue + dbtvalue
    hld = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    b = _z(claim / hld, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- overhang acceleration (curvature of intensity) ----
# warrant overhang acceleration: quarter momentum minus prior-quarter momentum (dilution curvature)
def f46ow_f46_options_warrant_positioning_wntoveraccel_63d_base_v064_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = (r - r.shift(63)) - (r.shift(63) - r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity acceleration (positioning curvature)
def f46ow_f46_options_warrant_positioning_putintensaccel_63d_base_v065_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = (r - r.shift(63)) - (r.shift(63) - r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options-intensity acceleration (gross options-value curvature)
def f46ow_f46_options_warrant_positioning_optintensaccel_63d_base_v066_signal(putvalue, cllvalue, marketcap):
    r = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    b = (r - r.shift(63)) - (r.shift(63) - r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- year-over-year overhang regime shifts ----
# warrant overhang YoY change (slow dilution-regime shift)
def f46ow_f46_options_warrant_positioning_wntoveryoy_252d_base_v067_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity YoY change (slow positioning-regime shift)
def f46ow_f46_options_warrant_positioning_putintensyoy_252d_base_v068_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- derivative-value share momentum / smoothing (magnitude mix dynamics) ----
# warrant share-of-total momentum (latent-dilution mix build over a quarter)
def f46ow_f46_options_warrant_positioning_wntsharemom_63d_base_v069_signal(wntvalue, totalvalue):
    sh = _f46_share(wntvalue, totalvalue)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert share-of-total momentum (leverage mix build over a quarter)
def f46ow_f46_options_warrant_positioning_dbtsharemom_63d_base_v070_signal(dbtvalue, totalvalue):
    sh = _f46_share(dbtvalue, totalvalue)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put value share-of-total EMA-smoothed (persistent positioning weight)
def f46ow_f46_options_warrant_positioning_putshareema_base_v071_signal(putvalue, totalvalue):
    sh = _f46_share(putvalue, totalvalue)
    b = sh.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- overhang recovery off trough (re-arming of latent supply) ----
# warrant overhang recovery off its 252d trough (dilution overhang re-building)
def f46ow_f46_options_warrant_positioning_wntoverrecov_252d_base_v072_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = r / _rmin(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity recovery off its 252d trough (positioning re-arming)
def f46ow_f46_options_warrant_positioning_putintensrecov_252d_base_v073_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = r / _rmin(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- presence regimes for options (existence breadth, count-based) ----
# put-presence regime: fraction of trailing year with any put value (downside-positioning existence)
def f46ow_f46_options_warrant_positioning_putpresence_252d_base_v074_signal(putvalue):
    b = _f46_presence(putvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# derivative-breadth regime: fraction of trailing year total derivative holder count sits above
# its own 252d median (a high-positioning-breadth existence regime, distinct from value presence)
def f46ow_f46_options_warrant_positioning_derivbreadthreg_252d_base_v075_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = putholders + cllholders + wntholders + dbtholders
    med = deriv.rolling(252, min_periods=126).median()
    above = (deriv > med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46ow_f46_options_warrant_positioning_wntoverhang_lvl_base_v001_signal,
    f46ow_f46_options_warrant_positioning_wntshare_lvl_base_v002_signal,
    f46ow_f46_options_warrant_positioning_wntoverz_252d_base_v003_signal,
    f46ow_f46_options_warrant_positioning_wntaccum_126d_base_v004_signal,
    f46ow_f46_options_warrant_positioning_wntovervol_126d_base_v005_signal,
    f46ow_f46_options_warrant_positioning_wntcv_126d_base_v006_signal,
    f46ow_f46_options_warrant_positioning_wntperhld_252d_base_v007_signal,
    f46ow_f46_options_warrant_positioning_wntpresence_252d_base_v008_signal,
    f46ow_f46_options_warrant_positioning_dbtoverhang_lvl_base_v009_signal,
    f46ow_f46_options_warrant_positioning_dbtshare_lvl_base_v010_signal,
    f46ow_f46_options_warrant_positioning_dbtoverz_252d_base_v011_signal,
    f46ow_f46_options_warrant_positioning_dbtaccum_126d_base_v012_signal,
    f46ow_f46_options_warrant_positioning_dbtovervol_126d_base_v013_signal,
    f46ow_f46_options_warrant_positioning_dbtperhld_252d_base_v014_signal,
    f46ow_f46_options_warrant_positioning_dbtpresence_252d_base_v015_signal,
    f46ow_f46_options_warrant_positioning_putintens_lvl_base_v016_signal,
    f46ow_f46_options_warrant_positioning_putintensz_252d_base_v017_signal,
    f46ow_f46_options_warrant_positioning_putintensrank_504d_base_v018_signal,
    f46ow_f46_options_warrant_positioning_putintensvol_126d_base_v019_signal,
    f46ow_f46_options_warrant_positioning_cllintens_lvl_base_v020_signal,
    f46ow_f46_options_warrant_positioning_cllintensz_252d_base_v021_signal,
    f46ow_f46_options_warrant_positioning_cllintensrank_504d_base_v022_signal,
    f46ow_f46_options_warrant_positioning_cllintensvol_126d_base_v023_signal,
    f46ow_f46_options_warrant_positioning_optintens_lvl_base_v024_signal,
    f46ow_f46_options_warrant_positioning_optintensz_252d_base_v025_signal,
    f46ow_f46_options_warrant_positioning_optaccum_63d_base_v026_signal,
    f46ow_f46_options_warrant_positioning_derivvalshare_lvl_base_v027_signal,
    f46ow_f46_options_warrant_positioning_derivvalsharez_252d_base_v028_signal,
    f46ow_f46_options_warrant_positioning_wntdominance_lvl_base_v029_signal,
    f46ow_f46_options_warrant_positioning_optshare_lvl_base_v030_signal,
    f46ow_f46_options_warrant_positioning_structvsopt_lvl_base_v031_signal,
    f46ow_f46_options_warrant_positioning_structvsoptrank_504d_base_v032_signal,
    f46ow_f46_options_warrant_positioning_structweightmom_63d_base_v033_signal,
    f46ow_f46_options_warrant_positioning_wntvsequity_lvl_base_v034_signal,
    f46ow_f46_options_warrant_positioning_dbtvsequitymom_126d_base_v035_signal,
    f46ow_f46_options_warrant_positioning_putvsequity_lvl_base_v036_signal,
    f46ow_f46_options_warrant_positioning_cllvsequity_lvl_base_v037_signal,
    f46ow_f46_options_warrant_positioning_wnthldbreadth_252d_base_v038_signal,
    f46ow_f46_options_warrant_positioning_dbthldbreadth_252d_base_v039_signal,
    f46ow_f46_options_warrant_positioning_puthldrank_504d_base_v040_signal,
    f46ow_f46_options_warrant_positioning_cllhldrank_504d_base_v041_signal,
    f46ow_f46_options_warrant_positioning_derivbreadth_252d_base_v042_signal,
    f46ow_f46_options_warrant_positioning_putperhld_252d_base_v043_signal,
    f46ow_f46_options_warrant_positioning_cllperhld_252d_base_v044_signal,
    f46ow_f46_options_warrant_positioning_wntovermom_63d_base_v045_signal,
    f46ow_f46_options_warrant_positioning_dbtovermom_63d_base_v046_signal,
    f46ow_f46_options_warrant_positioning_putintensmom_63d_base_v047_signal,
    f46ow_f46_options_warrant_positioning_cllintensmom_63d_base_v048_signal,
    f46ow_f46_options_warrant_positioning_wntoverstretch_252d_base_v049_signal,
    f46ow_f46_options_warrant_positioning_putintensstretch_252d_base_v050_signal,
    f46ow_f46_options_warrant_positioning_cllintensdd_252d_base_v051_signal,
    f46ow_f46_options_warrant_positioning_dbtoverstretch_504d_base_v052_signal,
    f46ow_f46_options_warrant_positioning_putsignmag_252d_base_v053_signal,
    f46ow_f46_options_warrant_positioning_wntsignmag_252d_base_v054_signal,
    f46ow_f46_options_warrant_positioning_wntoverdisp_base_v055_signal,
    f46ow_f46_options_warrant_positioning_putintensdisp_base_v056_signal,
    f46ow_f46_options_warrant_positioning_wntconcdiv_126d_base_v057_signal,
    f46ow_f46_options_warrant_positioning_putconcdiv_63d_base_v058_signal,
    f46ow_f46_options_warrant_positioning_cllconcdiv_63d_base_v059_signal,
    f46ow_f46_options_warrant_positioning_covdilrisk_lvl_base_v060_signal,
    f46ow_f46_options_warrant_positioning_covputpos_lvl_base_v061_signal,
    f46ow_f46_options_warrant_positioning_claimfootprint_252d_base_v062_signal,
    f46ow_f46_options_warrant_positioning_claimperhld_252d_base_v063_signal,
    f46ow_f46_options_warrant_positioning_wntoveraccel_63d_base_v064_signal,
    f46ow_f46_options_warrant_positioning_putintensaccel_63d_base_v065_signal,
    f46ow_f46_options_warrant_positioning_optintensaccel_63d_base_v066_signal,
    f46ow_f46_options_warrant_positioning_wntoveryoy_252d_base_v067_signal,
    f46ow_f46_options_warrant_positioning_putintensyoy_252d_base_v068_signal,
    f46ow_f46_options_warrant_positioning_wntsharemom_63d_base_v069_signal,
    f46ow_f46_options_warrant_positioning_dbtsharemom_63d_base_v070_signal,
    f46ow_f46_options_warrant_positioning_putshareema_base_v071_signal,
    f46ow_f46_options_warrant_positioning_wntoverrecov_252d_base_v072_signal,
    f46ow_f46_options_warrant_positioning_putintensrecov_252d_base_v073_signal,
    f46ow_f46_options_warrant_positioning_putpresence_252d_base_v074_signal,
    f46ow_f46_options_warrant_positioning_derivbreadthreg_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_OPTIONS_WARRANT_POSITIONING_REGISTRY_001_075 = REGISTRY


ALLOW = {
    "putholders", "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue",
    "dbtholders", "dbtvalue", "totalvalue", "shrvalue", "percentoftotal", "marketcap",
}


def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.6
    return pd.Series(s, name=None)


def _intermittent(s, seed, p_zero=0.35):
    # zero out random contiguous quarters so presence/existence varies (warrant/convert
    # claims are intermittent in real sf3a data); keeps a positive regime for ratios.
    # add idiosyncratic daily jitter so derived ratios/accum are not locally linear.
    g = np.random.default_rng(seed)
    n = len(s)
    mask = np.ones(n)
    for q in range(0, n, 63):
        if g.random() < p_zero:
            mask[q:q + 63] = 0.0
    jitter = np.exp(g.normal(0.0, 0.06, n))
    return pd.Series(s.values * mask * jitter, name=s.name)


def _jit(s, seed, sd=0.05):
    g = np.random.default_rng(seed)
    return pd.Series(s.values * np.exp(g.normal(0.0, sd, len(s))), name=s.name)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    putholders = _jit(_fund(101, base=120.0, drift=0.02, vol=0.06), 301).rename("putholders")
    putvalue = _intermittent(_fund(102, base=4.0e7, drift=0.025, vol=0.09), 202, p_zero=0.18).rename("putvalue")
    cllholders = _jit(_fund(103, base=140.0, drift=0.02, vol=0.06), 303).rename("cllholders")
    cllvalue = _intermittent(_fund(104, base=5.0e7, drift=0.03, vol=0.09), 204, p_zero=0.15).rename("cllvalue")
    wntholders = _intermittent(_fund(105, base=40.0, drift=0.015, vol=0.07), 205, p_zero=0.30).rename("wntholders")
    wntvalue = _intermittent(_fund(106, base=2.0e7, drift=0.02, vol=0.10), 206, p_zero=0.30).rename("wntvalue")
    dbtholders = _intermittent(_fund(107, base=55.0, drift=0.04, vol=0.13), 217, p_zero=0.25).rename("dbtholders")
    dbtvalue = _intermittent(_fund(108, base=3.0e7, drift=0.05, vol=0.15), 218, p_zero=0.25).rename("dbtvalue")
    totalvalue = _fund(109, base=6.0e8, drift=0.02, vol=0.08).rename("totalvalue")
    shrvalue = _fund(110, base=4.5e8, drift=0.035, vol=0.10).rename("shrvalue")
    marketcap = _fund(111, base=1.0e9, drift=0.01, vol=0.12).rename("marketcap")
    percentoftotal = (_fund(112, base=0.4, drift=0.0, vol=0.16).clip(0.01, 0.99)).rename("percentoftotal")

    cols = {
        "putholders": putholders, "putvalue": putvalue, "cllholders": cllholders,
        "cllvalue": cllvalue, "wntholders": wntholders, "wntvalue": wntvalue,
        "dbtholders": dbtholders, "dbtvalue": dbtvalue, "totalvalue": totalvalue,
        "shrvalue": shrvalue, "percentoftotal": percentoftotal, "marketcap": marketcap,
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

    print("OK f46_options_warrant_positioning_base_001_075_claude: %d features pass" % n_features)
