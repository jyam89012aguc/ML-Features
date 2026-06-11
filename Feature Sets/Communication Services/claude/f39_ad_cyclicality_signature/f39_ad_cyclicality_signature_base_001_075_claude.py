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
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (ad-cyclicality signature) =====
def _f39_cyc_amp(s, w):
    # cyclic amplitude = rolling peak-to-trough range normalized by level
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    mid = (hi + lo) / 2.0
    return (hi - lo) / mid.replace(0, np.nan)


def _f39_cyc_phase(s, w):
    # phase = where in the peak-trough cycle the current level sits (0=trough,1=peak)
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _f39_detrend(s, w):
    # cyclical component = level minus its own trend (rolling mean)
    return s - s.rolling(w, min_periods=max(1, w // 2)).mean()


def _f39_op_margin(opinc, revenue):
    return opinc / revenue.replace(0, np.nan)


def _f39_gross_margin(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f39_sales_intensity(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f39_swing(s, w):
    # swing = rolling std of the detrended cyclical component (amplitude of oscillation)
    d = s - s.rolling(w, min_periods=max(1, w // 2)).mean()
    return d.rolling(w, min_periods=max(1, w // 2)).std()


# ============================================================
# revenue cyclic amplitude over 252d (ad-revenue peak-to-trough swing)
def f39ac_f39_ad_cyclicality_signature_revamp_252d_base_v001_signal(revenue):
    b = _f39_cyc_amp(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclic amplitude over 504d (multi-year ad cycle amplitude)
def f39ac_f39_ad_cyclicality_signature_revamp_504d_base_v002_signal(revenue):
    b = _f39_cyc_amp(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ad-cycle phase position of revenue (trough=low, peak=high) over 252d
def f39ac_f39_ad_cyclicality_signature_revphase_252d_base_v003_signal(revenue):
    b = _f39_cyc_phase(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin swing tied to ad cycle (252d std of detrended op-margin)
def f39ac_f39_ad_cyclicality_signature_opmswing_252d_base_v004_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    b = _f39_swing(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sg&a (sales) / revenue ad-sales intensity level, z-scored vs own 252d history
def f39ac_f39_ad_cyclicality_signature_salesint_252d_base_v005_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _z(si, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin compression in downturns: gm minus its 252d peak (negative=compressed)
def f39ac_f39_ad_cyclicality_signature_gmcompress_252d_base_v006_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    peak = gm.rolling(252, min_periods=126).max()
    b = gm / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cyclical revenue sensitivity: revenue growth amplitude scaled by op-margin growth
def f39ac_f39_ad_cyclicality_signature_revsens_252d_base_v007_signal(revenue, opinc):
    rg = _roc(revenue, 63)
    og = _roc(opinc, 63)
    b = og.rolling(252, min_periods=126).std() / rg.rolling(252, min_periods=126).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cyclic amplitude (ad-cycle margin swing)
def f39ac_f39_ad_cyclicality_signature_ebmamp_252d_base_v008_signal(ebitdamargin):
    b = _f39_cyc_amp(ebitdamargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# detrended revenue cyclical component, normalized by its trend
def f39ac_f39_ad_cyclicality_signature_revcyc_252d_base_v009_signal(revenue):
    trend = _mean(revenue, 252)
    b = _f39_detrend(revenue, 252) / trend.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit cyclic amplitude over 252d
def f39ac_f39_ad_cyclicality_signature_gpamp_252d_base_v010_signal(gp):
    b = _f39_cyc_amp(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin phase in the ad cycle (252d)
def f39ac_f39_ad_cyclicality_signature_opmphase_252d_base_v011_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    b = _f39_cyc_phase(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity swing (ad-sales spend oscillation amplitude) 252d
def f39ac_f39_ad_cyclicality_signature_salesswing_252d_base_v012_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _f39_swing(si, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin swing tied to ad cycle (504d std of detrended gm)
def f39ac_f39_ad_cyclicality_signature_gmswing_504d_base_v013_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    b = _f39_swing(gm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical phase momentum: change in phase over a quarter
def f39ac_f39_ad_cyclicality_signature_revphasemom_252d_base_v014_signal(revenue):
    ph = _f39_cyc_phase(revenue, 252)
    b = ph - ph.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin compression from peak (cyclical downturn depth)
def f39ac_f39_ad_cyclicality_signature_opmcompress_252d_base_v015_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    peak = om.rolling(252, min_periods=126).max()
    b = om - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ad-sales intensity cyclic amplitude (sgna/revenue peak-to-trough) 504d
def f39ac_f39_ad_cyclicality_signature_salesamp_504d_base_v016_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _f39_cyc_amp(si, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin detrended cyclical level (margin vs its own trend)
def f39ac_f39_ad_cyclicality_signature_ebmcyc_252d_base_v017_signal(ebitdamargin):
    b = _f39_detrend(ebitdamargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-to-margin cyclic co-movement: corr proxy via product of detrended z-scores
def f39ac_f39_ad_cyclicality_signature_revmargco_252d_base_v018_signal(revenue, opinc):
    rz = _z(revenue, 252)
    om = _f39_op_margin(opinc, revenue)
    mz = _z(om, 252)
    b = (rz * mz).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin phase in ad cycle (compression vs expansion regime) 252d
def f39ac_f39_ad_cyclicality_signature_gmphase_252d_base_v019_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    b = _f39_cyc_phase(gm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cyclical revenue sensitivity beta: regression-free slope of opinc vs revenue change
def f39ac_f39_ad_cyclicality_signature_opbeta_126d_base_v020_signal(opinc, revenue):
    dr = revenue.diff()
    do = opinc.diff()
    cov = (dr * do).rolling(126, min_periods=63).mean() - dr.rolling(126, min_periods=63).mean() * do.rolling(126, min_periods=63).mean()
    var = dr.rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclic amplitude ratio: short cycle vs long cycle (cycle-tightening)
def f39ac_f39_ad_cyclicality_signature_ampratio_252v504_base_v021_signal(revenue):
    s = _f39_cyc_amp(revenue, 252)
    l = _f39_cyc_amp(revenue, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin compression rank vs own history (downturn extremity percentile)
def f39ac_f39_ad_cyclicality_signature_gmcomprank_252d_base_v022_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    peak = gm.rolling(252, min_periods=126).max()
    comp = gm / peak.replace(0, np.nan) - 1.0
    b = _rank(comp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage cyclicality: correlation of op-margin change with revenue change
def f39ac_f39_ad_cyclicality_signature_oplevcyc_252d_base_v023_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    dom = om.diff()
    dr = _roc(revenue, 21)
    mo = dom.rolling(252, min_periods=126).mean()
    mr = dr.rolling(252, min_periods=126).mean()
    cov = (dom * dr).rolling(252, min_periods=126).mean() - mo * mr
    so = dom.rolling(252, min_periods=126).std()
    sr = dr.rolling(252, min_periods=126).std()
    b = cov / (so * sr).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ad-sales intensity detrended cyclical component
def f39ac_f39_ad_cyclicality_signature_salescyc_252d_base_v024_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _f39_detrend(si, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin phase momentum: change in margin-cycle phase over a quarter
def f39ac_f39_ad_cyclicality_signature_ebmphasemom_252d_base_v025_signal(ebitdamargin):
    ph = _f39_cyc_phase(ebitdamargin, 252)
    b = ph - ph.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical drawdown from peak, scaled by elapsed time since that peak (decay rate)
def f39ac_f39_ad_cyclicality_signature_revdd_252d_base_v026_signal(revenue):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    peak = revenue.rolling(252, min_periods=126).max()
    dd = revenue / peak.replace(0, np.nan) - 1.0
    dsh = revenue.rolling(252, min_periods=126).apply(_dsh, raw=True)
    b = dd * (1.0 - dsh)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit phase position in cycle, z-scored vs own 126d history
def f39ac_f39_ad_cyclicality_signature_gpphasez_252d_base_v027_signal(gp):
    ph = _f39_cyc_phase(gp, 252)
    b = _z(ph, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity vs gross-margin spread (ad-spend efficiency in cycle)
def f39ac_f39_ad_cyclicality_signature_salesgmspr_252d_base_v028_signal(sgna, revenue, gp):
    si = _f39_sales_intensity(sgna, revenue)
    gm = _f39_gross_margin(gp, revenue)
    b = _z(si, 252) - _z(gm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin cyclic amplitude (operating leverage swing through ad cycle)
def f39ac_f39_ad_cyclicality_signature_opmamp_252d_base_v029_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    b = _f39_cyc_amp(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical sensitivity: amplitude weighted by trend slope sign
def f39ac_f39_ad_cyclicality_signature_revsensdir_252d_base_v030_signal(revenue):
    amp = _f39_cyc_amp(revenue, 252)
    slope = _roc(_mean(revenue, 63), 63)
    b = amp * np.sign(slope)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin recovery off trough (expansion phase strength)
def f39ac_f39_ad_cyclicality_signature_gmrecov_252d_base_v031_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    trough = gm.rolling(252, min_periods=126).min()
    b = gm / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity phase in cycle (ad-spend ramp position) 504d
def f39ac_f39_ad_cyclicality_signature_salesphase_504d_base_v032_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _f39_cyc_phase(si, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin compression from peak (cyclical margin downturn)
def f39ac_f39_ad_cyclicality_signature_ebmcompress_252d_base_v033_signal(ebitdamargin):
    peak = ebitdamargin.rolling(252, min_periods=126).max()
    b = ebitdamargin - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue short-vs-long trend gap (fast cycle deviation minus slow cycle deviation)
def f39ac_f39_ad_cyclicality_signature_revcycz_252d_base_v034_signal(revenue):
    fast = revenue / _mean(revenue, 63).replace(0, np.nan) - 1.0
    slow = revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin to gross-margin cyclical divergence (cost-leverage in downturn)
def f39ac_f39_ad_cyclicality_signature_opgmdiv_252d_base_v035_signal(opinc, revenue, gp):
    om = _f39_op_margin(opinc, revenue)
    gm = _f39_gross_margin(gp, revenue)
    b = _f39_detrend(om, 252) - _f39_detrend(gm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue amplitude per unit sales intensity (cycle reach of ad spend)
def f39ac_f39_ad_cyclicality_signature_ampperint_252d_base_v036_signal(revenue, sgna):
    amp = _f39_cyc_amp(revenue, 252)
    si = sgna / revenue.replace(0, np.nan)
    b = amp / _mean(si, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin cyclic amplitude 252d
def f39ac_f39_ad_cyclicality_signature_gmamp_252d_base_v037_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    b = _f39_cyc_amp(gm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion (cyclical lumpiness of ad revenue)
def f39ac_f39_ad_cyclicality_signature_revgdisp_252d_base_v038_signal(revenue):
    g = _roc(revenue, 21)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity rising-streak fraction (ad-spend ramp persistence)
def f39ac_f39_ad_cyclicality_signature_salesstreak_252d_base_v039_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    up = (si.diff() > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin cyclical trough distance (how far above the cycle low)
def f39ac_f39_ad_cyclicality_signature_opmtrough_252d_base_v040_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    trough = om.rolling(252, min_periods=126).min()
    b = om - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cyclic amplitude long cycle 504d
def f39ac_f39_ad_cyclicality_signature_ebmamp_504d_base_v041_signal(ebitdamargin):
    b = _f39_cyc_amp(ebitdamargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical sensitivity to gross-profit (gp amplitude vs revenue amplitude)
def f39ac_f39_ad_cyclicality_signature_gprevsens_252d_base_v042_signal(gp, revenue):
    ga = _f39_cyc_amp(gp, 252)
    ra = _f39_cyc_amp(revenue, 252)
    b = ga / ra.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity z minus revenue-phase (counter-cyclical ad spend tell)
def f39ac_f39_ad_cyclicality_signature_countercyc_252d_base_v043_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    ph = _f39_cyc_phase(revenue, 252)
    b = _z(si, 252) - (ph - 0.5) * 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin downturn duration: fraction of last year below the 252d gm mean
def f39ac_f39_ad_cyclicality_signature_gmdowndur_252d_base_v044_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    below = (gm < _mean(gm, 252)).astype(float)
    b = below.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical exposure: phase-velocity x amplitude (where the cycle is moving fastest)
def f39ac_f39_ad_cyclicality_signature_cycexpos_252d_base_v045_signal(revenue):
    ph = _f39_cyc_phase(revenue, 252)
    amp = _f39_cyc_amp(revenue, 252)
    b = (ph - ph.shift(21)) * amp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin vs ebitda-margin cyclical-phase gap (below-the-line cyclicality lead/lag)
def f39ac_f39_ad_cyclicality_signature_opebmswing_252d_base_v046_signal(opinc, revenue, ebitdamargin):
    pom = _f39_cyc_phase(_f39_op_margin(opinc, revenue), 252)
    peb = _f39_cyc_phase(ebitdamargin, 252)
    b = pom - peb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration cyclicality (2nd-diff dispersion of revenue) as level
def f39ac_f39_ad_cyclicality_signature_revacccyc_252d_base_v047_signal(revenue):
    acc = _roc(revenue, 21) - _roc(revenue.shift(21), 21)
    b = _std(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin cyclical z relative to long trend
def f39ac_f39_ad_cyclicality_signature_gmcyclz_504d_base_v048_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    b = _z(gm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity amplitude per revenue amplitude (ad-spend pro-cyclicality)
def f39ac_f39_ad_cyclicality_signature_salesprocyc_252d_base_v049_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    sa = _f39_cyc_amp(si, 252)
    ra = _f39_cyc_amp(revenue, 252)
    b = sa / ra.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cyclic-amplitude trend (margin-cycle widening/narrowing)
def f39ac_f39_ad_cyclicality_signature_ebmphaserank_252d_base_v050_signal(ebitdamargin):
    amp = _f39_cyc_amp(ebitdamargin, 252)
    b = amp - amp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue downturn count weighted by below-trend depth (ad-recession tally + severity)
def f39ac_f39_ad_cyclicality_signature_revdowncount_252d_base_v051_signal(revenue):
    trend = _mean(revenue, 252)
    below = (revenue < trend).astype(float)
    entries = ((below == 1) & (below.shift(1) == 0)).astype(float)
    count = entries.rolling(252, min_periods=126).sum()
    depth = (trend - revenue).clip(lower=0) / trend.replace(0, np.nan)
    b = count + 8.0 * depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin cyclical phase momentum (margin-cycle direction)
def f39ac_f39_ad_cyclicality_signature_opmphasemom_252d_base_v052_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    ph = _f39_cyc_phase(om, 252)
    b = ph - ph.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin compression depth weighted by revenue downturn (joint stress)
def f39ac_f39_ad_cyclicality_signature_jointstress_252d_base_v053_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    gmcomp = (_mean(gm, 252) - gm).clip(lower=0)
    revdd = (_mean(revenue, 252) - revenue).clip(lower=0) / _mean(revenue, 252).replace(0, np.nan)
    b = gmcomp * revdd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity vs op-margin spread cyclicality (ad-spend vs profit tradeoff)
def f39ac_f39_ad_cyclicality_signature_salesopspr_252d_base_v054_signal(sgna, revenue, opinc):
    si = _f39_sales_intensity(sgna, revenue)
    om = _f39_op_margin(opinc, revenue)
    b = _f39_detrend(si, 252) + _f39_detrend(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclic amplitude trend (cycle widening/narrowing over a year)
def f39ac_f39_ad_cyclicality_signature_amptrend_252d_base_v055_signal(revenue):
    amp = _f39_cyc_amp(revenue, 252)
    b = amp - amp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit detrended cyclical component normalized by trend
def f39ac_f39_ad_cyclicality_signature_gpcyc_252d_base_v056_signal(gp):
    trend = _mean(gp, 252)
    b = _f39_detrend(gp, 252) / trend.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin below-trend duration (fraction of year in margin-cycle downturn)
def f39ac_f39_ad_cyclicality_signature_ebmdd_252d_base_v057_signal(ebitdamargin):
    below = (ebitdamargin < _mean(ebitdamargin, 252)).astype(float)
    b = below.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical sensitivity vs sales intensity change (ad-spend response)
def f39ac_f39_ad_cyclicality_signature_adresponse_126d_base_v058_signal(revenue, sgna):
    dr = _roc(revenue, 21)
    dsg = _roc(sgna, 21)
    cov = (dr * dsg).rolling(126, min_periods=63).mean() - dr.rolling(126, min_periods=63).mean() * dsg.rolling(126, min_periods=63).mean()
    var = dsg.rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin compression rank (cyclical profit-trough percentile)
def f39ac_f39_ad_cyclicality_signature_opmcomprank_252d_base_v059_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    peak = om.rolling(252, min_periods=126).max()
    comp = om - peak
    b = _rank(comp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin phase momentum (margin-cycle expansion/contraction speed)
def f39ac_f39_ad_cyclicality_signature_gmphasemom_252d_base_v060_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    ph = _f39_cyc_phase(gm, 252)
    b = ph - ph.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level vs trend ratio, smoothed (persistent cyclical tilt)
def f39ac_f39_ad_cyclicality_signature_revtilt_252d_base_v061_signal(revenue):
    ratio = revenue / _mean(revenue, 252).replace(0, np.nan)
    b = ratio.ewm(span=42, min_periods=21).mean() - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity compression: intensity vs its 252d trough (ad-spend cut)
def f39ac_f39_ad_cyclicality_signature_salescut_252d_base_v062_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    trough = si.rolling(252, min_periods=126).min()
    b = si / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cyclical momentum (margin oscillation velocity over a month)
def f39ac_f39_ad_cyclicality_signature_ebmcycz_252d_base_v063_signal(ebitdamargin):
    d = _f39_detrend(ebitdamargin, 252)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-margin joint cyclic amplitude (combined ad-cycle stress)
def f39ac_f39_ad_cyclicality_signature_jointamp_252d_base_v064_signal(revenue, opinc):
    ra = _f39_cyc_amp(revenue, 252)
    oa = _f39_cyc_amp(_f39_op_margin(opinc, revenue), 252)
    b = (ra + oa) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit cyclical phase x revenue phase (synchronized ad cycle)
def f39ac_f39_ad_cyclicality_signature_phasesync_252d_base_v065_signal(gp, revenue):
    pg = _f39_cyc_phase(gp, 252)
    pr = _f39_cyc_phase(revenue, 252)
    b = (pg - 0.5) * (pr - 0.5) * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin sensitivity to gross-margin (downturn margin pass-through)
def f39ac_f39_ad_cyclicality_signature_marginpass_126d_base_v066_signal(opinc, revenue, gp):
    om = _f39_op_margin(opinc, revenue)
    gm = _f39_gross_margin(gp, revenue)
    dom = om.diff()
    dgm = gm.diff()
    cov = (dom * dgm).rolling(126, min_periods=63).mean() - dom.rolling(126, min_periods=63).mean() * dgm.rolling(126, min_periods=63).mean()
    var = dgm.rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical upturn strength (above-trend persistence)
def f39ac_f39_ad_cyclicality_signature_revupturn_252d_base_v067_signal(revenue):
    above = (revenue > _mean(revenue, 252)).astype(float)
    excess = (revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0).clip(lower=0)
    b = above.rolling(252, min_periods=126).mean() * 0.5 + excess.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity smoothed trend deviation (ad-budget cycle displacement)
def f39ac_f39_ad_cyclicality_signature_salesdisp_252d_base_v068_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = si - si.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin swing per revenue swing (operating amplification through cycle)
def f39ac_f39_ad_cyclicality_signature_ebmamplify_252d_base_v069_signal(ebitdamargin, revenue):
    ebsw = _f39_swing(ebitdamargin, 252)
    rvsw = _f39_swing(_roc(revenue, 21), 252)
    b = ebsw / rvsw.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclic amplitude z-scored (cycle-intensity extremity)
def f39ac_f39_ad_cyclicality_signature_revampz_252d_base_v070_signal(revenue):
    amp = _f39_cyc_amp(revenue, 252)
    b = _z(amp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin compression vs op-margin compression spread (cost-line stress)
def f39ac_f39_ad_cyclicality_signature_compspr_252d_base_v071_signal(gp, revenue, opinc):
    gm = _f39_gross_margin(gp, revenue)
    om = _f39_op_margin(opinc, revenue)
    gmc = gm / gm.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    omc = om - om.rolling(252, min_periods=126).max()
    b = gmc - omc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue phase distance from peak (how far past the ad-cycle top)
def f39ac_f39_ad_cyclicality_signature_peakdist_252d_base_v072_signal(revenue):
    hi = _rmax(revenue, 252)
    b = np.log(revenue.replace(0, np.nan) / hi.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity cyclical co-movement with op-margin (spend-discipline cycle)
def f39ac_f39_ad_cyclicality_signature_spenddisc_252d_base_v073_signal(sgna, revenue, opinc):
    si = _f39_sales_intensity(sgna, revenue)
    om = _f39_op_margin(opinc, revenue)
    b = (_z(si, 252) * _z(om, 252)).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cyclical phase relative to revenue phase (margin-lag tell)
def f39ac_f39_ad_cyclicality_signature_marginlag_252d_base_v074_signal(ebitdamargin, revenue):
    pe = _f39_cyc_phase(ebitdamargin, 252)
    pr = _f39_cyc_phase(revenue, 252)
    b = pe - pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical sensitivity composite: amplitude x growth dispersion
def f39ac_f39_ad_cyclicality_signature_cyccomp_252d_base_v075_signal(revenue):
    amp = _f39_cyc_amp(revenue, 252)
    disp = _std(_roc(revenue, 21), 252)
    b = amp * disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39ac_f39_ad_cyclicality_signature_revamp_252d_base_v001_signal,
    f39ac_f39_ad_cyclicality_signature_revamp_504d_base_v002_signal,
    f39ac_f39_ad_cyclicality_signature_revphase_252d_base_v003_signal,
    f39ac_f39_ad_cyclicality_signature_opmswing_252d_base_v004_signal,
    f39ac_f39_ad_cyclicality_signature_salesint_252d_base_v005_signal,
    f39ac_f39_ad_cyclicality_signature_gmcompress_252d_base_v006_signal,
    f39ac_f39_ad_cyclicality_signature_revsens_252d_base_v007_signal,
    f39ac_f39_ad_cyclicality_signature_ebmamp_252d_base_v008_signal,
    f39ac_f39_ad_cyclicality_signature_revcyc_252d_base_v009_signal,
    f39ac_f39_ad_cyclicality_signature_gpamp_252d_base_v010_signal,
    f39ac_f39_ad_cyclicality_signature_opmphase_252d_base_v011_signal,
    f39ac_f39_ad_cyclicality_signature_salesswing_252d_base_v012_signal,
    f39ac_f39_ad_cyclicality_signature_gmswing_504d_base_v013_signal,
    f39ac_f39_ad_cyclicality_signature_revphasemom_252d_base_v014_signal,
    f39ac_f39_ad_cyclicality_signature_opmcompress_252d_base_v015_signal,
    f39ac_f39_ad_cyclicality_signature_salesamp_504d_base_v016_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcyc_252d_base_v017_signal,
    f39ac_f39_ad_cyclicality_signature_revmargco_252d_base_v018_signal,
    f39ac_f39_ad_cyclicality_signature_gmphase_252d_base_v019_signal,
    f39ac_f39_ad_cyclicality_signature_opbeta_126d_base_v020_signal,
    f39ac_f39_ad_cyclicality_signature_ampratio_252v504_base_v021_signal,
    f39ac_f39_ad_cyclicality_signature_gmcomprank_252d_base_v022_signal,
    f39ac_f39_ad_cyclicality_signature_oplevcyc_252d_base_v023_signal,
    f39ac_f39_ad_cyclicality_signature_salescyc_252d_base_v024_signal,
    f39ac_f39_ad_cyclicality_signature_ebmphasemom_252d_base_v025_signal,
    f39ac_f39_ad_cyclicality_signature_revdd_252d_base_v026_signal,
    f39ac_f39_ad_cyclicality_signature_gpphasez_252d_base_v027_signal,
    f39ac_f39_ad_cyclicality_signature_salesgmspr_252d_base_v028_signal,
    f39ac_f39_ad_cyclicality_signature_opmamp_252d_base_v029_signal,
    f39ac_f39_ad_cyclicality_signature_revsensdir_252d_base_v030_signal,
    f39ac_f39_ad_cyclicality_signature_gmrecov_252d_base_v031_signal,
    f39ac_f39_ad_cyclicality_signature_salesphase_504d_base_v032_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcompress_252d_base_v033_signal,
    f39ac_f39_ad_cyclicality_signature_revcycz_252d_base_v034_signal,
    f39ac_f39_ad_cyclicality_signature_opgmdiv_252d_base_v035_signal,
    f39ac_f39_ad_cyclicality_signature_ampperint_252d_base_v036_signal,
    f39ac_f39_ad_cyclicality_signature_gmamp_252d_base_v037_signal,
    f39ac_f39_ad_cyclicality_signature_revgdisp_252d_base_v038_signal,
    f39ac_f39_ad_cyclicality_signature_salesstreak_252d_base_v039_signal,
    f39ac_f39_ad_cyclicality_signature_opmtrough_252d_base_v040_signal,
    f39ac_f39_ad_cyclicality_signature_ebmamp_504d_base_v041_signal,
    f39ac_f39_ad_cyclicality_signature_gprevsens_252d_base_v042_signal,
    f39ac_f39_ad_cyclicality_signature_countercyc_252d_base_v043_signal,
    f39ac_f39_ad_cyclicality_signature_gmdowndur_252d_base_v044_signal,
    f39ac_f39_ad_cyclicality_signature_cycexpos_252d_base_v045_signal,
    f39ac_f39_ad_cyclicality_signature_opebmswing_252d_base_v046_signal,
    f39ac_f39_ad_cyclicality_signature_revacccyc_252d_base_v047_signal,
    f39ac_f39_ad_cyclicality_signature_gmcyclz_504d_base_v048_signal,
    f39ac_f39_ad_cyclicality_signature_salesprocyc_252d_base_v049_signal,
    f39ac_f39_ad_cyclicality_signature_ebmphaserank_252d_base_v050_signal,
    f39ac_f39_ad_cyclicality_signature_revdowncount_252d_base_v051_signal,
    f39ac_f39_ad_cyclicality_signature_opmphasemom_252d_base_v052_signal,
    f39ac_f39_ad_cyclicality_signature_jointstress_252d_base_v053_signal,
    f39ac_f39_ad_cyclicality_signature_salesopspr_252d_base_v054_signal,
    f39ac_f39_ad_cyclicality_signature_amptrend_252d_base_v055_signal,
    f39ac_f39_ad_cyclicality_signature_gpcyc_252d_base_v056_signal,
    f39ac_f39_ad_cyclicality_signature_ebmdd_252d_base_v057_signal,
    f39ac_f39_ad_cyclicality_signature_adresponse_126d_base_v058_signal,
    f39ac_f39_ad_cyclicality_signature_opmcomprank_252d_base_v059_signal,
    f39ac_f39_ad_cyclicality_signature_gmphasemom_252d_base_v060_signal,
    f39ac_f39_ad_cyclicality_signature_revtilt_252d_base_v061_signal,
    f39ac_f39_ad_cyclicality_signature_salescut_252d_base_v062_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcycz_252d_base_v063_signal,
    f39ac_f39_ad_cyclicality_signature_jointamp_252d_base_v064_signal,
    f39ac_f39_ad_cyclicality_signature_phasesync_252d_base_v065_signal,
    f39ac_f39_ad_cyclicality_signature_marginpass_126d_base_v066_signal,
    f39ac_f39_ad_cyclicality_signature_revupturn_252d_base_v067_signal,
    f39ac_f39_ad_cyclicality_signature_salesdisp_252d_base_v068_signal,
    f39ac_f39_ad_cyclicality_signature_ebmamplify_252d_base_v069_signal,
    f39ac_f39_ad_cyclicality_signature_revampz_252d_base_v070_signal,
    f39ac_f39_ad_cyclicality_signature_compspr_252d_base_v071_signal,
    f39ac_f39_ad_cyclicality_signature_peakdist_252d_base_v072_signal,
    f39ac_f39_ad_cyclicality_signature_spenddisc_252d_base_v073_signal,
    f39ac_f39_ad_cyclicality_signature_marginlag_252d_base_v074_signal,
    f39ac_f39_ad_cyclicality_signature_cyccomp_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_AD_CYCLICALITY_SIGNATURE_REGISTRY_001_075 = REGISTRY


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

    # ad-cyclical component: revenue/gp/sgna positive with a cyclical oscillation
    cyc = pd.Series(np.sin(np.arange(n) * 2.0 * np.pi / 252.0)
                    + 0.4 * np.sin(np.arange(n) * 2.0 * np.pi / 110.0), name=None)
    revenue = (_fund(101, base=1.2e8, drift=0.025, vol=0.06)
               * (1.0 + 0.22 * cyc)).rename("revenue")
    gp = (_fund(102, base=6.0e7, drift=0.024, vol=0.06)
          * (1.0 + 0.18 * cyc)).rename("gp")
    sgna = (_fund(103, base=3.5e7, drift=0.02, vol=0.05)
            * (1.0 + 0.15 * cyc.shift(20).fillna(0.0))).rename("sgna")
    opinc = (_fund(104, base=1.5e7, drift=0.02, vol=0.10, allow_neg=True)
             * (1.0 + 0.30 * cyc)).rename("opinc")
    ebitdamargin = (0.12 + 0.05 * cyc
                    + pd.Series(np.random.normal(0, 0.01, n))).clip(0.01, 0.6).rename("ebitdamargin")

    cols = {
        "revenue": revenue, "gp": gp, "sgna": sgna,
        "opinc": opinc, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (name, meta["inputs"])
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

    print("OK f39_ad_cyclicality_signature_base_001_075_claude: %d features pass" % n_features)
