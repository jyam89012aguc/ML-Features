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
# This family is OVERHANG / EXISTENCE & derivative-value MAGNITUDE. It does NOT compute the
# put-vs-call skew putvalue/(putvalue+cllvalue), nor holder-type fund/und/prf composition
# (f51_ownership_mix_concentration), nor the institutional shrvalue/holder accumulation trend (f45).
def _f46_intensity(value, marketcap):
    return value / marketcap.replace(0, np.nan)


def _f46_share(part, whole):
    return part / whole.replace(0, np.nan)


def _f46_per_holder(value, holders):
    return value / holders.replace(0, np.nan)


def _f46_accum(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f46_presence(s, w):
    return (s > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# ---- warrant overhang, alternate windows / facets ----
# warrant overhang vs total ownership value, z-scored vs year (dilution-mix regime)
def f46ow_f46_options_warrant_positioning_wntsharez_252d_base_v076_signal(wntvalue, totalvalue):
    sh = _f46_share(wntvalue, totalvalue)
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang half-year momentum (slow latent-dilution build)
def f46ow_f46_options_warrant_positioning_wntovermom_126d_base_v077_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang ranked vs 504d (latent-dilution percentile regime)
def f46ow_f46_options_warrant_positioning_wntoverrank_504d_base_v078_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang accumulation acceleration (half-year build minus prior half-year build)
def f46ow_f46_options_warrant_positioning_wntaccel_126d_base_v079_signal(wntvalue):
    roc = _f46_accum(wntvalue, 126)
    b = roc - roc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant value coefficient-of-variation over 252d (dilution-value instability, long window)
def f46ow_f46_options_warrant_positioning_wntcv_252d_base_v080_signal(wntvalue):
    b = _std(wntvalue, 252) / _mean(wntvalue, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant per-holder accumulation over half-year (overhang concentration build)
def f46ow_f46_options_warrant_positioning_wntperhldaccum_126d_base_v081_signal(wntvalue, wntholders):
    wp = _f46_per_holder(wntvalue, wntholders)
    b = _f46_accum(wp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang vs its long EMA, z-scored (dilution displacement regime)
def f46ow_f46_options_warrant_positioning_wntoverdispz_252d_base_v082_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    disp = r - r.ewm(span=126, min_periods=42).mean()
    b = _z(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant-holder breadth ranked vs 504d (dilution-holder existence breadth percentile)
def f46ow_f46_options_warrant_positioning_wnthldrank_504d_base_v083_signal(wntholders):
    b = _rank(wntholders, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- convert / debt overhang, alternate facets ----
# convert overhang vs total ownership value, z-scored vs year (leverage-mix regime)
def f46ow_f46_options_warrant_positioning_dbtsharez_252d_base_v084_signal(dbtvalue, totalvalue):
    sh = _f46_share(dbtvalue, totalvalue)
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang half-year momentum (slow leverage-claim build)
def f46ow_f46_options_warrant_positioning_dbtovermom_126d_base_v085_signal(dbtvalue, marketcap):
    r = _f46_intensity(dbtvalue, marketcap)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang ranked vs 504d (leverage percentile regime)
def f46ow_f46_options_warrant_positioning_dbtoverrank_504d_base_v086_signal(dbtvalue, marketcap):
    r = _f46_intensity(dbtvalue, marketcap)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang accumulation acceleration (leverage build curvature)
def f46ow_f46_options_warrant_positioning_dbtaccel_63d_base_v087_signal(dbtvalue):
    roc = _f46_accum(dbtvalue, 63)
    b = roc - roc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert value-vs-holder divergence over a quarter, pct-growth form (leverage overhang concentrating)
def f46ow_f46_options_warrant_positioning_dbtconcdiv_63d_base_v088_signal(dbtvalue, dbtholders):
    vg = _roc(dbtvalue, 63)
    hg = _roc(dbtholders, 63)
    b = vg - hg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert per-holder accumulation over half-year (convert concentration build)
def f46ow_f46_options_warrant_positioning_dbtperhldaccum_126d_base_v089_signal(dbtvalue, dbtholders):
    dp = _f46_per_holder(dbtvalue, dbtholders)
    b = _f46_accum(dp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert-holder breadth ranked vs 504d (leverage-holder existence breadth percentile)
def f46ow_f46_options_warrant_positioning_dbthldrank_504d_base_v090_signal(dbtholders):
    b = _rank(dbtholders, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- put VALUE magnitude facets (positioning intensity, NOT skew) ----
# put intensity half-year momentum (slow downside-positioning build)
def f46ow_f46_options_warrant_positioning_putintensmom_126d_base_v091_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity YoY change (slow positioning-regime shift)
def f46ow_f46_options_warrant_positioning_putintensyoy_252d_base_v092_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity sign-magnitude vs typical over half-year (compression-adjusted positioning extremity)
def f46ow_f46_options_warrant_positioning_putsignmag_126d_base_v093_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    dev = r - _mean(r, 126)
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity position within its 504d range (0=trough, 1=peak; positioning range-position)
def f46ow_f46_options_warrant_positioning_putintensrngpos_504d_base_v094_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    b = (r - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put per-holder claim accumulation over a quarter (positioning conviction build)
def f46ow_f46_options_warrant_positioning_putperhldaccum_63d_base_v095_signal(putvalue, putholders):
    pp = _f46_per_holder(putvalue, putholders)
    b = _f46_accum(pp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put value coefficient-of-variation over half-year (positioning-value instability)
def f46ow_f46_options_warrant_positioning_putcv_126d_base_v096_signal(putvalue):
    b = _std(putvalue, 126) / _mean(putvalue, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- call VALUE magnitude facets ----
# call intensity half-year momentum (slow upside-positioning build)
def f46ow_f46_options_warrant_positioning_cllintensmom_126d_base_v097_signal(cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity sign-magnitude vs typical over half-year (compression-adjusted positioning extremity)
def f46ow_f46_options_warrant_positioning_cllsignmag_126d_base_v098_signal(cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    dev = r - _mean(r, 126)
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity recovery off its 252d trough (upside-positioning re-arming)
def f46ow_f46_options_warrant_positioning_cllintensrecov_252d_base_v099_signal(cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    b = r / _rmin(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call per-holder claim accumulation over a quarter (positioning conviction build)
def f46ow_f46_options_warrant_positioning_cllperhldaccum_63d_base_v100_signal(cllvalue, cllholders):
    cp = _f46_per_holder(cllvalue, cllholders)
    b = _f46_accum(cp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call value coefficient-of-variation over half-year (positioning-value instability)
def f46ow_f46_options_warrant_positioning_cllcv_126d_base_v101_signal(cllvalue):
    b = _std(cllvalue, 126) / _mean(cllvalue, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity vs its long EMA (upside-positioning displacement from trend)
def f46ow_f46_options_warrant_positioning_cllintensdisp_base_v102_signal(cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    b = r / r.ewm(span=126, min_periods=42).mean().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- total options-value magnitude facets ----
# total options value (put+call) vs total ownership value, z-scored vs year
def f46ow_f46_options_warrant_positioning_optsharez_252d_base_v103_signal(putvalue, cllvalue, totalvalue):
    r = (putvalue + cllvalue) / totalvalue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options value vs total ownership value, ranked vs 504d (options-footprint percentile)
def f46ow_f46_options_warrant_positioning_optsharerank_504d_base_v104_signal(putvalue, cllvalue, totalvalue):
    r = (putvalue + cllvalue) / totalvalue.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options value intensity half-year momentum (gross options-value build)
def f46ow_f46_options_warrant_positioning_optintensmom_126d_base_v105_signal(putvalue, cllvalue, marketcap):
    r = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options value intensity stretch vs 252d max (gross options-value vs peak)
def f46ow_f46_options_warrant_positioning_optintensstretch_252d_base_v106_signal(putvalue, cllvalue, marketcap):
    r = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    b = r / _rmax(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options value intensity dispersion over half-year (gross options-value instability)
def f46ow_f46_options_warrant_positioning_optintensvol_126d_base_v107_signal(putvalue, cllvalue, marketcap):
    r = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- derivative-value share of total ownership, alternate facets ----
# total derivative value share ranked vs 504d (non-equity-claim percentile)
def f46ow_f46_options_warrant_positioning_derivvalsharerank_504d_base_v108_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    deriv = putvalue + cllvalue + wntvalue + dbtvalue
    sh = deriv / totalvalue.replace(0, np.nan)
    b = _rank(sh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total derivative value share momentum over a quarter (non-equity-claim build)
def f46ow_f46_options_warrant_positioning_derivvalsharemom_63d_base_v109_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    deriv = putvalue + cllvalue + wntvalue + dbtvalue
    sh = deriv / totalvalue.replace(0, np.nan)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total derivative value share EMA-smoothed (persistent non-equity-claim weight)
def f46ow_f46_options_warrant_positioning_derivvalshareema_base_v110_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    deriv = putvalue + cllvalue + wntvalue + dbtvalue
    sh = deriv / totalvalue.replace(0, np.nan)
    b = sh.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- structural-vs-tradable overhang balance facets ----
# structural-overhang (wnt+dbt) vs options-value ratio, momentum over a quarter (supply-vs-positioning build)
def f46ow_f46_options_warrant_positioning_structvsoptmom_63d_base_v111_signal(wntvalue, dbtvalue, putvalue, cllvalue):
    struct = wntvalue + dbtvalue
    opt = (putvalue + cllvalue).replace(0, np.nan)
    r = struct / opt
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structural-overhang weight of full derivative value, z-scored vs year (structural-supply regime)
def f46ow_f46_options_warrant_positioning_structweightz_252d_base_v112_signal(wntvalue, dbtvalue, putvalue, cllvalue):
    struct = wntvalue + dbtvalue
    full = (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)
    b = _z(struct / full, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- overhang vs equity-value facets (latent claim vs long base) ----
# warrant overhang vs equity value, z-scored vs year (dilution-to-equity regime)
def f46ow_f46_options_warrant_positioning_wntvsequityz_252d_base_v113_signal(wntvalue, shrvalue):
    r = _f46_share(wntvalue, shrvalue)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put value vs equity value, ranked vs 504d (positioning-to-equity percentile)
def f46ow_f46_options_warrant_positioning_putvsequityrank_504d_base_v114_signal(putvalue, shrvalue):
    r = _f46_share(putvalue, shrvalue)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call value vs equity value, momentum over a quarter (positioning-to-equity build)
def f46ow_f46_options_warrant_positioning_cllvsequitymom_63d_base_v115_signal(cllvalue, shrvalue):
    r = _f46_share(cllvalue, shrvalue)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- per-holder concentration facets ----
# warrant per-holder claim, ranked vs 504d (overhang-concentration percentile)
def f46ow_f46_options_warrant_positioning_wntperhldrank_504d_base_v116_signal(wntvalue, wntholders):
    pp = _f46_per_holder(wntvalue, wntholders)
    b = _rank(pp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put per-holder claim, ranked vs 504d (positioning-concentration percentile)
def f46ow_f46_options_warrant_positioning_putperhldrank_504d_base_v117_signal(putvalue, putholders):
    pp = _f46_per_holder(putvalue, putholders)
    b = _rank(pp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call per-holder claim, ranked vs 504d (positioning-concentration percentile)
def f46ow_f46_options_warrant_positioning_cllperhldrank_504d_base_v118_signal(cllvalue, cllholders):
    cp = _f46_per_holder(cllvalue, cllholders)
    b = _rank(cp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- holder-breadth accumulation facets (existence breadth flow) ----
# warrant-holder breadth accumulation over half-year (dilution-holder existence build)
def f46ow_f46_options_warrant_positioning_wnthldaccum_126d_base_v119_signal(wntholders):
    b = _f46_accum(wntholders, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder breadth accumulation over a quarter (downside-positioning breadth build)
def f46ow_f46_options_warrant_positioning_puthldaccum_63d_base_v120_signal(putholders):
    b = _f46_accum(putholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-holder breadth accumulation over a quarter (upside-positioning breadth build)
def f46ow_f46_options_warrant_positioning_cllhldaccum_63d_base_v121_signal(cllholders):
    b = _f46_accum(cllholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert-holder breadth accumulation over half-year (leverage-holder existence build)
def f46ow_f46_options_warrant_positioning_dbthldaccum_126d_base_v122_signal(dbtholders):
    b = _f46_accum(dbtholders, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- combined claim-footprint facets ----
# full claim (put+call+wnt+dbt) value vs marketcap, ranked vs 504d (total footprint percentile)
def f46ow_f46_options_warrant_positioning_claimfootrank_504d_base_v123_signal(putvalue, cllvalue, wntvalue, dbtvalue, marketcap):
    claim = putvalue + cllvalue + wntvalue + dbtvalue
    r = claim / marketcap.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full claim value vs marketcap, half-year momentum (total footprint build)
def f46ow_f46_options_warrant_positioning_claimfootmom_126d_base_v124_signal(putvalue, cllvalue, wntvalue, dbtvalue, marketcap):
    claim = putvalue + cllvalue + wntvalue + dbtvalue
    r = claim / marketcap.replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options value (put+call) accumulation over half-year (options-value flow magnitude, slow)
def f46ow_f46_options_warrant_positioning_optaccum_126d_base_v125_signal(putvalue, cllvalue):
    b = _f46_accum(putvalue + cllvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- coverage-weighted overhang interactions ----
# convert overhang gated by ownership coverage (coverage-weighted leverage risk)
def f46ow_f46_options_warrant_positioning_covdbtrisk_lvl_base_v126_signal(percentoftotal, dbtvalue, marketcap):
    over = _f46_intensity(dbtvalue, marketcap)
    b = over * percentoftotal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options intensity gated by ownership coverage (coverage-weighted positioning footprint)
def f46ow_f46_options_warrant_positioning_covoptpos_lvl_base_v127_signal(percentoftotal, putvalue, cllvalue, marketcap):
    r = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    b = r * percentoftotal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity gated by ownership coverage (coverage-weighted upside positioning)
def f46ow_f46_options_warrant_positioning_covcllpos_lvl_base_v128_signal(percentoftotal, cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    b = r * percentoftotal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- overhang acceleration / curvature facets ----
# convert overhang acceleration (quarter momentum minus prior-quarter momentum; leverage curvature)
def f46ow_f46_options_warrant_positioning_dbtoveraccel_63d_base_v129_signal(dbtvalue, marketcap):
    r = _f46_intensity(dbtvalue, marketcap)
    b = (r - r.shift(63)) - (r.shift(63) - r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity acceleration (upside-positioning curvature)
def f46ow_f46_options_warrant_positioning_cllintensaccel_63d_base_v130_signal(cllvalue, marketcap):
    r = _f46_intensity(cllvalue, marketcap)
    b = (r - r.shift(63)) - (r.shift(63) - r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- overhang regime distance / drawdown facets ----
# warrant overhang drawdown from its 252d peak (latent-dilution cooling depth)
def f46ow_f46_options_warrant_positioning_wntoverdd_252d_base_v131_signal(wntvalue, marketcap):
    r = _f46_intensity(wntvalue, marketcap)
    b = r / _rmax(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity drawdown from its 252d peak (downside-positioning cooling depth)
def f46ow_f46_options_warrant_positioning_putintensdd_252d_base_v132_signal(putvalue, marketcap):
    r = _f46_intensity(putvalue, marketcap)
    b = r / _rmax(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang recovery off its 252d trough (leverage-claim re-building)
def f46ow_f46_options_warrant_positioning_dbtoverrecov_252d_base_v133_signal(dbtvalue, marketcap):
    r = _f46_intensity(dbtvalue, marketcap)
    b = r / _rmin(r, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- value-vs-equity accumulation spreads (overhang flow net of long-base flow) ----
# warrant value accumulation vs equity value accumulation spread (dilution flow net of long flow)
def f46ow_f46_options_warrant_positioning_wntvsequityflow_126d_base_v134_signal(wntvalue, shrvalue):
    wg = _f46_accum(wntvalue, 126)
    sg = _f46_accum(shrvalue, 126)
    b = wg - sg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put value accumulation vs equity value accumulation spread (positioning flow net of long flow)
def f46ow_f46_options_warrant_positioning_putvsequityflow_126d_base_v135_signal(putvalue, shrvalue):
    pg = _f46_accum(putvalue, 126)
    sg = _f46_accum(shrvalue, 126)
    b = pg - sg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert value accumulation vs equity value accumulation spread (leverage flow net of long flow)
def f46ow_f46_options_warrant_positioning_dbtvsequityflow_126d_base_v136_signal(dbtvalue, shrvalue):
    dg = _f46_accum(dbtvalue, 126)
    sg = _f46_accum(shrvalue, 126)
    b = dg - sg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- presence-duration / persistence facets ----
# warrant-presence persistence: fraction of trailing 504d with any warrant value (long-window existence)
def f46ow_f46_options_warrant_positioning_wntpresence_504d_base_v137_signal(wntvalue):
    b = _f46_presence(wntvalue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert-presence persistence over 504d (long-window leverage-claim existence)
def f46ow_f46_options_warrant_positioning_dbtpresence_504d_base_v138_signal(dbtvalue):
    b = _f46_presence(dbtvalue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- overhang vs options magnitude interactions ----
# warrant overhang net of put-positioning intensity (latent supply minus realized downside demand), de-trended
def f46ow_f46_options_warrant_positioning_dilnetput_252d_base_v139_signal(wntvalue, putvalue, marketcap):
    wr = _f46_intensity(wntvalue, marketcap)
    pr = _f46_intensity(putvalue, marketcap)
    b = _z(wr - pr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convert overhang net of call-positioning intensity (latent leverage minus realized upside demand), de-trended
def f46ow_f46_options_warrant_positioning_dilnetcll_252d_base_v140_signal(dbtvalue, cllvalue, marketcap):
    dr = _f46_intensity(dbtvalue, marketcap)
    cr = _f46_intensity(cllvalue, marketcap)
    b = _z(dr - cr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- combined structural overhang accumulation flow ----
# combined structural overhang (wnt+dbt) accumulation over a quarter (structural-supply flow)
def f46ow_f46_options_warrant_positioning_structaccum_63d_base_v141_signal(wntvalue, dbtvalue):
    b = _f46_accum(wntvalue + dbtvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined structural overhang vs marketcap, dispersion over half-year (structural-supply instability)
def f46ow_f46_options_warrant_positioning_structovervol_126d_base_v142_signal(wntvalue, dbtvalue, marketcap):
    r = (wntvalue + dbtvalue) / marketcap.replace(0, np.nan)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- options-value per total-value density (existence intensity) ----
# put-holder density: put holders per total ownership value, de-trended (downside breadth density)
def f46ow_f46_options_warrant_positioning_puthlddens_252d_base_v143_signal(putholders, totalvalue):
    r = putholders / totalvalue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant-holder density: warrant holders per total ownership value, de-trended (dilution breadth density)
def f46ow_f46_options_warrant_positioning_wnthlddens_252d_base_v144_signal(wntholders, totalvalue):
    r = wntholders / totalvalue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- per-holder claim dispersion / instability facets ----
# put per-holder claim stretch vs 252d max (positioning-size relative to peak)
def f46ow_f46_options_warrant_positioning_putperhldstretch_252d_base_v145_signal(putvalue, putholders):
    pp = _f46_per_holder(putvalue, putholders)
    b = pp / _rmax(pp, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant per-holder claim stretch vs 252d max (overhang-size relative to peak)
def f46ow_f46_options_warrant_positioning_wntperhldstretch_252d_base_v146_signal(wntvalue, wntholders):
    wp = _f46_per_holder(wntvalue, wntholders)
    b = wp / _rmax(wp, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- overhang YoY / long-horizon facets ----
# convert overhang YoY change (slow leverage-regime shift)
def f46ow_f46_options_warrant_positioning_dbtoveryoy_252d_base_v147_signal(dbtvalue, marketcap):
    r = _f46_intensity(dbtvalue, marketcap)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total options intensity YoY change (slow gross options-value regime shift)
def f46ow_f46_options_warrant_positioning_optintensyoy_252d_base_v148_signal(putvalue, cllvalue, marketcap):
    r = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- derivative-breadth growth facets ----
# total derivative-holder breadth accumulation over a quarter (overall positioning-breadth flow)
def f46ow_f46_options_warrant_positioning_derivbreadthgr_63d_base_v149_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = putholders + cllholders + wntholders + dbtholders
    b = _f46_accum(deriv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total derivative-holder breadth z-scored, slow EMA (persistent positioning-breadth regime)
def f46ow_f46_options_warrant_positioning_derivbreadthema_base_v150_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = putholders + cllholders + wntholders + dbtholders
    b = _z(deriv, 252).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46ow_f46_options_warrant_positioning_wntsharez_252d_base_v076_signal,
    f46ow_f46_options_warrant_positioning_wntovermom_126d_base_v077_signal,
    f46ow_f46_options_warrant_positioning_wntoverrank_504d_base_v078_signal,
    f46ow_f46_options_warrant_positioning_wntaccel_126d_base_v079_signal,
    f46ow_f46_options_warrant_positioning_wntcv_252d_base_v080_signal,
    f46ow_f46_options_warrant_positioning_wntperhldaccum_126d_base_v081_signal,
    f46ow_f46_options_warrant_positioning_wntoverdispz_252d_base_v082_signal,
    f46ow_f46_options_warrant_positioning_wnthldrank_504d_base_v083_signal,
    f46ow_f46_options_warrant_positioning_dbtsharez_252d_base_v084_signal,
    f46ow_f46_options_warrant_positioning_dbtovermom_126d_base_v085_signal,
    f46ow_f46_options_warrant_positioning_dbtoverrank_504d_base_v086_signal,
    f46ow_f46_options_warrant_positioning_dbtaccel_63d_base_v087_signal,
    f46ow_f46_options_warrant_positioning_dbtconcdiv_63d_base_v088_signal,
    f46ow_f46_options_warrant_positioning_dbtperhldaccum_126d_base_v089_signal,
    f46ow_f46_options_warrant_positioning_dbthldrank_504d_base_v090_signal,
    f46ow_f46_options_warrant_positioning_putintensmom_126d_base_v091_signal,
    f46ow_f46_options_warrant_positioning_putintensyoy_252d_base_v092_signal,
    f46ow_f46_options_warrant_positioning_putsignmag_126d_base_v093_signal,
    f46ow_f46_options_warrant_positioning_putintensrngpos_504d_base_v094_signal,
    f46ow_f46_options_warrant_positioning_putperhldaccum_63d_base_v095_signal,
    f46ow_f46_options_warrant_positioning_putcv_126d_base_v096_signal,
    f46ow_f46_options_warrant_positioning_cllintensmom_126d_base_v097_signal,
    f46ow_f46_options_warrant_positioning_cllsignmag_126d_base_v098_signal,
    f46ow_f46_options_warrant_positioning_cllintensrecov_252d_base_v099_signal,
    f46ow_f46_options_warrant_positioning_cllperhldaccum_63d_base_v100_signal,
    f46ow_f46_options_warrant_positioning_cllcv_126d_base_v101_signal,
    f46ow_f46_options_warrant_positioning_cllintensdisp_base_v102_signal,
    f46ow_f46_options_warrant_positioning_optsharez_252d_base_v103_signal,
    f46ow_f46_options_warrant_positioning_optsharerank_504d_base_v104_signal,
    f46ow_f46_options_warrant_positioning_optintensmom_126d_base_v105_signal,
    f46ow_f46_options_warrant_positioning_optintensstretch_252d_base_v106_signal,
    f46ow_f46_options_warrant_positioning_optintensvol_126d_base_v107_signal,
    f46ow_f46_options_warrant_positioning_derivvalsharerank_504d_base_v108_signal,
    f46ow_f46_options_warrant_positioning_derivvalsharemom_63d_base_v109_signal,
    f46ow_f46_options_warrant_positioning_derivvalshareema_base_v110_signal,
    f46ow_f46_options_warrant_positioning_structvsoptmom_63d_base_v111_signal,
    f46ow_f46_options_warrant_positioning_structweightz_252d_base_v112_signal,
    f46ow_f46_options_warrant_positioning_wntvsequityz_252d_base_v113_signal,
    f46ow_f46_options_warrant_positioning_putvsequityrank_504d_base_v114_signal,
    f46ow_f46_options_warrant_positioning_cllvsequitymom_63d_base_v115_signal,
    f46ow_f46_options_warrant_positioning_wntperhldrank_504d_base_v116_signal,
    f46ow_f46_options_warrant_positioning_putperhldrank_504d_base_v117_signal,
    f46ow_f46_options_warrant_positioning_cllperhldrank_504d_base_v118_signal,
    f46ow_f46_options_warrant_positioning_wnthldaccum_126d_base_v119_signal,
    f46ow_f46_options_warrant_positioning_puthldaccum_63d_base_v120_signal,
    f46ow_f46_options_warrant_positioning_cllhldaccum_63d_base_v121_signal,
    f46ow_f46_options_warrant_positioning_dbthldaccum_126d_base_v122_signal,
    f46ow_f46_options_warrant_positioning_claimfootrank_504d_base_v123_signal,
    f46ow_f46_options_warrant_positioning_claimfootmom_126d_base_v124_signal,
    f46ow_f46_options_warrant_positioning_optaccum_126d_base_v125_signal,
    f46ow_f46_options_warrant_positioning_covdbtrisk_lvl_base_v126_signal,
    f46ow_f46_options_warrant_positioning_covoptpos_lvl_base_v127_signal,
    f46ow_f46_options_warrant_positioning_covcllpos_lvl_base_v128_signal,
    f46ow_f46_options_warrant_positioning_dbtoveraccel_63d_base_v129_signal,
    f46ow_f46_options_warrant_positioning_cllintensaccel_63d_base_v130_signal,
    f46ow_f46_options_warrant_positioning_wntoverdd_252d_base_v131_signal,
    f46ow_f46_options_warrant_positioning_putintensdd_252d_base_v132_signal,
    f46ow_f46_options_warrant_positioning_dbtoverrecov_252d_base_v133_signal,
    f46ow_f46_options_warrant_positioning_wntvsequityflow_126d_base_v134_signal,
    f46ow_f46_options_warrant_positioning_putvsequityflow_126d_base_v135_signal,
    f46ow_f46_options_warrant_positioning_dbtvsequityflow_126d_base_v136_signal,
    f46ow_f46_options_warrant_positioning_wntpresence_504d_base_v137_signal,
    f46ow_f46_options_warrant_positioning_dbtpresence_504d_base_v138_signal,
    f46ow_f46_options_warrant_positioning_dilnetput_252d_base_v139_signal,
    f46ow_f46_options_warrant_positioning_dilnetcll_252d_base_v140_signal,
    f46ow_f46_options_warrant_positioning_structaccum_63d_base_v141_signal,
    f46ow_f46_options_warrant_positioning_structovervol_126d_base_v142_signal,
    f46ow_f46_options_warrant_positioning_puthlddens_252d_base_v143_signal,
    f46ow_f46_options_warrant_positioning_wnthlddens_252d_base_v144_signal,
    f46ow_f46_options_warrant_positioning_putperhldstretch_252d_base_v145_signal,
    f46ow_f46_options_warrant_positioning_wntperhldstretch_252d_base_v146_signal,
    f46ow_f46_options_warrant_positioning_dbtoveryoy_252d_base_v147_signal,
    f46ow_f46_options_warrant_positioning_optintensyoy_252d_base_v148_signal,
    f46ow_f46_options_warrant_positioning_derivbreadthgr_63d_base_v149_signal,
    f46ow_f46_options_warrant_positioning_derivbreadthema_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_OPTIONS_WARRANT_POSITIONING_REGISTRY_076_150 = REGISTRY


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

    print("OK f46_options_warrant_positioning_base_076_150_claude: %d features pass" % n_features)
