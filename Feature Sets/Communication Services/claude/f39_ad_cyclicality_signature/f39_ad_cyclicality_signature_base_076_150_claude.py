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
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    mid = (hi + lo) / 2.0
    return (hi - lo) / mid.replace(0, np.nan)


def _f39_cyc_phase(s, w):
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _f39_detrend(s, w):
    return s - s.rolling(w, min_periods=max(1, w // 2)).mean()


def _f39_op_margin(opinc, revenue):
    return opinc / revenue.replace(0, np.nan)


def _f39_gross_margin(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f39_sales_intensity(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f39_swing(s, w):
    d = s - s.rolling(w, min_periods=max(1, w // 2)).mean()
    return d.rolling(w, min_periods=max(1, w // 2)).std()


def _f39_beta(y, x, w):
    cov = (y * x).rolling(w, min_periods=max(1, w // 2)).mean() \
        - y.rolling(w, min_periods=max(1, w // 2)).mean() * x.rolling(w, min_periods=max(1, w // 2)).mean()
    var = x.rolling(w, min_periods=max(1, w // 2)).var()
    return cov / var.replace(0, np.nan)


# ============================================================
# revenue cyclic amplitude over 126d (short ad-cycle swing)
def f39ac_f39_ad_cyclicality_signature_revamp_126d_base_v076_signal(revenue):
    b = _f39_cyc_amp(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclic phase over 504d (long ad-cycle position)
def f39ac_f39_ad_cyclicality_signature_revphase_504d_base_v077_signal(revenue):
    b = _f39_cyc_phase(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin cyclic amplitude over 504d (long-cycle operating swing)
def f39ac_f39_ad_cyclicality_signature_opmamp_504d_base_v078_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    b = _f39_cyc_amp(om, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity level z-scored vs own 504d history (ad-sales intensity regime)
def f39ac_f39_ad_cyclicality_signature_salesint_504d_base_v079_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _z(si, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin compression over 504d (long-cycle downturn depth)
def f39ac_f39_ad_cyclicality_signature_gmcompress_504d_base_v080_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    peak = gm.rolling(504, min_periods=252).max()
    b = gm / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue beta to gross-profit changes (top-line cyclical co-move)
def f39ac_f39_ad_cyclicality_signature_revgpbeta_126d_base_v081_signal(revenue, gp):
    dr = _roc(revenue, 21)
    dg = _roc(gp, 21)
    b = _f39_beta(dg, dr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cyclic phase over 126d (short margin-cycle position)
def f39ac_f39_ad_cyclicality_signature_ebmphase_126d_base_v082_signal(ebitdamargin):
    b = _f39_cyc_phase(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue detrended cyclical component over 504d normalized by trend
def f39ac_f39_ad_cyclicality_signature_revcyc_504d_base_v083_signal(revenue):
    trend = _mean(revenue, 504)
    b = _f39_detrend(revenue, 504) / trend.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit cyclic amplitude over 126d
def f39ac_f39_ad_cyclicality_signature_gpamp_126d_base_v084_signal(gp):
    b = _f39_cyc_amp(gp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin phase over 504d (long operating-cycle position)
def f39ac_f39_ad_cyclicality_signature_opmphase_504d_base_v085_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    b = _f39_cyc_phase(om, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity swing over 504d (long ad-spend oscillation)
def f39ac_f39_ad_cyclicality_signature_salesswing_504d_base_v086_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _f39_swing(si, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin swing over 126d (short margin oscillation)
def f39ac_f39_ad_cyclicality_signature_gmswing_126d_base_v087_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    b = _f39_swing(gm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue phase momentum over 504d cycle (long-cycle direction)
def f39ac_f39_ad_cyclicality_signature_revphasemom_504d_base_v088_signal(revenue):
    ph = _f39_cyc_phase(revenue, 504)
    b = ph - ph.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin compression over 504d from long peak
def f39ac_f39_ad_cyclicality_signature_opmcompress_504d_base_v089_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    peak = om.rolling(504, min_periods=252).max()
    b = om - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ad-sales intensity cyclic amplitude over 126d (short ad-spend swing)
def f39ac_f39_ad_cyclicality_signature_salesamp_126d_base_v090_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _f39_cyc_amp(si, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin detrended over 504d (long margin cyclical component)
def f39ac_f39_ad_cyclicality_signature_ebmcyc_504d_base_v091_signal(ebitdamargin):
    b = _f39_detrend(ebitdamargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-margin cyclic co-movement over 252d (sales-leverage correlation)
def f39ac_f39_ad_cyclicality_signature_revmargco_504d_base_v092_signal(revenue, opinc):
    rz = _z(revenue, 504)
    om = _f39_op_margin(opinc, revenue)
    mz = _z(om, 504)
    b = (rz * mz).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin phase over 504d (long compression/expansion regime)
def f39ac_f39_ad_cyclicality_signature_gmphase_504d_base_v093_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    b = _f39_cyc_phase(gm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-revenue cyclical beta over 252d (operating leverage sensitivity)
def f39ac_f39_ad_cyclicality_signature_opbeta_252d_base_v094_signal(opinc, revenue):
    dr = revenue.diff()
    do = opinc.diff()
    b = _f39_beta(do, dr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclic-amplitude ratio short vs long (126 vs 504 cycle tightening)
def f39ac_f39_ad_cyclicality_signature_ampratio_126v504_base_v095_signal(revenue):
    s = _f39_cyc_amp(revenue, 126)
    l = _f39_cyc_amp(revenue, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin compression rank over 252d window (downturn percentile, long ref)
def f39ac_f39_ad_cyclicality_signature_gmcomprank_504d_base_v096_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    peak = gm.rolling(504, min_periods=252).max()
    comp = gm / peak.replace(0, np.nan) - 1.0
    b = _rank(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin to revenue-phase divergence (margin lag vs revenue cycle)
def f39ac_f39_ad_cyclicality_signature_opmrevlag_252d_base_v097_signal(opinc, revenue):
    pom = _f39_cyc_phase(_f39_op_margin(opinc, revenue), 252)
    prev = _f39_cyc_phase(revenue, 252)
    b = pom - prev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ad-sales intensity detrended over 504d
def f39ac_f39_ad_cyclicality_signature_salescyc_504d_base_v098_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _f39_detrend(si, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin phase momentum over 504d cycle
def f39ac_f39_ad_cyclicality_signature_ebmphasemom_504d_base_v099_signal(ebitdamargin):
    ph = _f39_cyc_phase(ebitdamargin, 504)
    b = ph - ph.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue recovery off 252d trough (ad-revenue upturn strength)
def f39ac_f39_ad_cyclicality_signature_revrecov_252d_base_v100_signal(revenue):
    trough = revenue.rolling(252, min_periods=126).min()
    b = revenue / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit phase position over 504d, z-scored vs 252d
def f39ac_f39_ad_cyclicality_signature_gpphasez_504d_base_v101_signal(gp):
    ph = _f39_cyc_phase(gp, 504)
    b = _z(ph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity vs gross-margin spread over 504d (ad-spend efficiency long cycle)
def f39ac_f39_ad_cyclicality_signature_salesgmspr_504d_base_v102_signal(sgna, revenue, gp):
    si = _f39_sales_intensity(sgna, revenue)
    gm = _f39_gross_margin(gp, revenue)
    b = _z(si, 504) - _z(gm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin cyclic amplitude over 126d (short operating swing)
def f39ac_f39_ad_cyclicality_signature_opmamp_126d_base_v103_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    b = _f39_cyc_amp(om, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical sensitivity weighted by long-trend slope sign
def f39ac_f39_ad_cyclicality_signature_revsensdir_504d_base_v104_signal(revenue):
    amp = _f39_cyc_amp(revenue, 504)
    slope = _roc(_mean(revenue, 126), 126)
    b = amp * np.sign(slope)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin recovery off 504d trough (long expansion strength)
def f39ac_f39_ad_cyclicality_signature_gmrecov_504d_base_v105_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    trough = gm.rolling(504, min_periods=252).min()
    b = gm / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity phase over 126d (short ad-spend ramp position)
def f39ac_f39_ad_cyclicality_signature_salesphase_126d_base_v106_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = _f39_cyc_phase(si, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cyclic amplitude trend over 504d (long margin-cycle widening)
def f39ac_f39_ad_cyclicality_signature_ebmcompress_504d_base_v107_signal(ebitdamargin):
    amp = _f39_cyc_amp(ebitdamargin, 504)
    b = amp - amp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue fast-vs-slow trend gap over 126/504 (mid-cycle deviation)
def f39ac_f39_ad_cyclicality_signature_revcycgap_504d_base_v108_signal(revenue):
    fast = revenue / _mean(revenue, 126).replace(0, np.nan) - 1.0
    slow = revenue / _mean(revenue, 504).replace(0, np.nan) - 1.0
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin vs gross-margin cyclical divergence over 504d
def f39ac_f39_ad_cyclicality_signature_opgmdiv_504d_base_v109_signal(opinc, revenue, gp):
    om = _f39_op_margin(opinc, revenue)
    gm = _f39_gross_margin(gp, revenue)
    b = _f39_detrend(om, 504) - _f39_detrend(gm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue amplitude per unit sales-intensity over 504d (long cycle reach)
def f39ac_f39_ad_cyclicality_signature_ampperint_504d_base_v110_signal(revenue, sgna):
    amp = _f39_cyc_amp(revenue, 504)
    si = sgna / revenue.replace(0, np.nan)
    b = amp / _mean(si, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin cyclic amplitude over 504d
def f39ac_f39_ad_cyclicality_signature_gmamp_504d_base_v111_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    b = _f39_cyc_amp(gm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion over 126d (short-cycle lumpiness)
def f39ac_f39_ad_cyclicality_signature_revgdisp_126d_base_v112_signal(revenue):
    g = _roc(revenue, 21)
    b = _std(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity rising-streak fraction over 126d (short ad-spend ramp)
def f39ac_f39_ad_cyclicality_signature_salesstreak_126d_base_v113_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    up = (si.diff() > 0).astype(float)
    b = up.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin trough distance over 504d (long cycle low cushion)
def f39ac_f39_ad_cyclicality_signature_opmtrough_504d_base_v114_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    trough = om.rolling(504, min_periods=252).min()
    b = om - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cyclic amplitude over 126d (short margin swing)
def f39ac_f39_ad_cyclicality_signature_ebmamp_126d_base_v115_signal(ebitdamargin):
    b = _f39_cyc_amp(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit vs revenue amplitude ratio over 504d (margin reach long cycle)
def f39ac_f39_ad_cyclicality_signature_gprevsens_504d_base_v116_signal(gp, revenue):
    ga = _f39_cyc_amp(gp, 504)
    ra = _f39_cyc_amp(revenue, 504)
    b = ga / ra.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# counter-cyclical ad-spend tell over 504d (intensity z minus long revenue phase)
def f39ac_f39_ad_cyclicality_signature_countercyc_504d_base_v117_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    ph = _f39_cyc_phase(revenue, 504)
    b = _z(si, 504) - (ph - 0.5) * 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin downturn duration over 504d window
def f39ac_f39_ad_cyclicality_signature_gmdowndur_504d_base_v118_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    below = (gm < _mean(gm, 504)).astype(float)
    b = below.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical exposure over 504d (phase-velocity x amplitude)
def f39ac_f39_ad_cyclicality_signature_cycexpos_504d_base_v119_signal(revenue):
    ph = _f39_cyc_phase(revenue, 504)
    amp = _f39_cyc_amp(revenue, 504)
    b = (ph - ph.shift(42)) * amp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin vs ebitda-margin phase gap over 504d
def f39ac_f39_ad_cyclicality_signature_opebmgap_504d_base_v120_signal(opinc, revenue, ebitdamargin):
    pom = _f39_cyc_phase(_f39_op_margin(opinc, revenue), 504)
    peb = _f39_cyc_phase(ebitdamargin, 504)
    b = pom - peb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration dispersion over 126d (short-cycle accel lumpiness)
def f39ac_f39_ad_cyclicality_signature_revacccyc_126d_base_v121_signal(revenue):
    acc = _roc(revenue, 21) - _roc(revenue.shift(21), 21)
    b = _std(acc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin level z over 252d (cyclical margin regime, short ref)
def f39ac_f39_ad_cyclicality_signature_gmcyclz_252d_base_v122_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    b = _z(gm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity pro-cyclicality over 504d (ad-spend amplitude vs revenue amplitude)
def f39ac_f39_ad_cyclicality_signature_salesprocyc_504d_base_v123_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    sa = _f39_cyc_amp(si, 504)
    ra = _f39_cyc_amp(revenue, 504)
    b = sa / ra.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin below-trend duration over 504d
def f39ac_f39_ad_cyclicality_signature_ebmdowndur_504d_base_v124_signal(ebitdamargin):
    below = (ebitdamargin < _mean(ebitdamargin, 504)).astype(float)
    b = below.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue downturn count weighted by depth over 504d (long ad-recession tally)
def f39ac_f39_ad_cyclicality_signature_revdowncount_504d_base_v125_signal(revenue):
    trend = _mean(revenue, 504)
    below = (revenue < trend).astype(float)
    entries = ((below == 1) & (below.shift(1) == 0)).astype(float)
    count = entries.rolling(504, min_periods=252).sum()
    depth = (trend - revenue).clip(lower=0) / trend.replace(0, np.nan)
    b = count + 8.0 * depth.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin phase momentum over 504d cycle
def f39ac_f39_ad_cyclicality_signature_opmphasemom_504d_base_v126_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    ph = _f39_cyc_phase(om, 504)
    b = ph - ph.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# joint stress over 504d (gm compression x revenue downturn, long cycle)
def f39ac_f39_ad_cyclicality_signature_jointstress_504d_base_v127_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    gmcomp = (_mean(gm, 504) - gm).clip(lower=0)
    revdd = (_mean(revenue, 504) - revenue).clip(lower=0) / _mean(revenue, 504).replace(0, np.nan)
    b = gmcomp * revdd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity + op-margin detrended sum over 504d (spend-profit tradeoff)
def f39ac_f39_ad_cyclicality_signature_salesopspr_504d_base_v128_signal(sgna, revenue, opinc):
    si = _f39_sales_intensity(sgna, revenue)
    om = _f39_op_margin(opinc, revenue)
    b = _f39_detrend(si, 504) + _f39_detrend(om, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclic amplitude trend over 504d (long cycle widening/narrowing)
def f39ac_f39_ad_cyclicality_signature_amptrend_504d_base_v129_signal(revenue):
    amp = _f39_cyc_amp(revenue, 504)
    b = amp - amp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit detrended over 504d normalized by trend
def f39ac_f39_ad_cyclicality_signature_gpcyc_504d_base_v130_signal(gp):
    trend = _mean(gp, 504)
    b = _f39_detrend(gp, 504) / trend.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin growth dispersion over 252d (short margin-cycle lumpiness)
def f39ac_f39_ad_cyclicality_signature_ebmrecov_252d_base_v131_signal(ebitdamargin):
    g = ebitdamargin.diff()
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical ad-response beta over 252d (revenue change vs sgna change)
def f39ac_f39_ad_cyclicality_signature_adresponse_252d_base_v132_signal(revenue, sgna):
    dr = _roc(revenue, 21)
    dsg = _roc(sgna, 21)
    b = _f39_beta(dr, dsg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin compression rank over 252d (cyclical profit-trough percentile, long ref)
def f39ac_f39_ad_cyclicality_signature_opmcomprank_504d_base_v133_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    peak = om.rolling(504, min_periods=252).max()
    comp = om - peak
    b = _rank(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin phase momentum over 504d cycle
def f39ac_f39_ad_cyclicality_signature_gmphasemom_504d_base_v134_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    ph = _f39_cyc_phase(gm, 504)
    b = ph - ph.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level vs long trend ratio smoothed (persistent long cyclical tilt)
def f39ac_f39_ad_cyclicality_signature_revtilt_504d_base_v135_signal(revenue):
    ratio = revenue / _mean(revenue, 504).replace(0, np.nan)
    b = ratio.ewm(span=84, min_periods=42).mean() - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity vs 504d trough (long ad-spend cut depth)
def f39ac_f39_ad_cyclicality_signature_salescut_504d_base_v136_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    trough = si.rolling(504, min_periods=252).min()
    b = si / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cyclical momentum over 504d (margin oscillation velocity)
def f39ac_f39_ad_cyclicality_signature_ebmcycmom_504d_base_v137_signal(ebitdamargin):
    d = _f39_detrend(ebitdamargin, 504)
    b = d - d.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-margin joint cyclic amplitude over 504d
def f39ac_f39_ad_cyclicality_signature_jointamp_504d_base_v138_signal(revenue, opinc):
    ra = _f39_cyc_amp(revenue, 504)
    oa = _f39_cyc_amp(_f39_op_margin(opinc, revenue), 504)
    b = (ra + oa) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit vs revenue phase synchronization over 504d
def f39ac_f39_ad_cyclicality_signature_phasesync_504d_base_v139_signal(gp, revenue):
    pg = _f39_cyc_phase(gp, 504)
    pr = _f39_cyc_phase(revenue, 504)
    b = (pg - 0.5) * (pr - 0.5) * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin pass-through from gross-margin over 252d (downturn margin transmission)
def f39ac_f39_ad_cyclicality_signature_marginpass_252d_base_v140_signal(opinc, revenue, gp):
    om = _f39_op_margin(opinc, revenue)
    gm = _f39_gross_margin(gp, revenue)
    b = _f39_beta(om.diff(), gm.diff(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue upturn strength over 504d (above-long-trend persistence)
def f39ac_f39_ad_cyclicality_signature_revupturn_504d_base_v141_signal(revenue):
    above = (revenue > _mean(revenue, 504)).astype(float)
    excess = (revenue / _mean(revenue, 504).replace(0, np.nan) - 1.0).clip(lower=0)
    b = above.rolling(504, min_periods=252).mean() * 0.5 + excess.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity displacement vs slow EMA over 504d span
def f39ac_f39_ad_cyclicality_signature_salesdisp_504d_base_v142_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    b = si - si.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin amplification per gross-profit swing over 252d
def f39ac_f39_ad_cyclicality_signature_ebmamplify_252d_base_v143_signal(ebitdamargin, gp):
    ebsw = _f39_swing(ebitdamargin, 252)
    gpsw = _f39_swing(_roc(gp, 21), 252)
    b = ebsw / gpsw.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclic amplitude z over 504d (long cycle-intensity extremity)
def f39ac_f39_ad_cyclicality_signature_revampz_504d_base_v144_signal(revenue):
    amp = _f39_cyc_amp(revenue, 504)
    b = _z(amp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross vs op cyclical-swing ratio over 504d (cost-line amplification, long cycle)
def f39ac_f39_ad_cyclicality_signature_compspr_504d_base_v145_signal(gp, revenue, opinc):
    gm = _f39_gross_margin(gp, revenue)
    om = _f39_op_margin(opinc, revenue)
    gmsw = _f39_swing(gm, 504)
    omsw = _f39_swing(om, 504)
    b = omsw / gmsw.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue distance past peak over 504d, scaled by time since that peak (cycle decay rate)
def f39ac_f39_ad_cyclicality_signature_peakdist_504d_base_v146_signal(revenue):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    hi = _rmax(revenue, 504)
    gap = np.log(revenue.replace(0, np.nan) / hi.replace(0, np.nan))
    dsh = revenue.rolling(504, min_periods=252).apply(_dsh, raw=True)
    b = gap * (1.0 - dsh)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spend-discipline cycle over 504d (sales-intensity x op-margin co-move)
def f39ac_f39_ad_cyclicality_signature_spenddisc_504d_base_v147_signal(sgna, revenue, opinc):
    si = _f39_sales_intensity(sgna, revenue)
    om = _f39_op_margin(opinc, revenue)
    b = (_z(si, 504) * _z(om, 504)).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin cyclical phase relative to revenue phase over 504d (margin-lag tell)
def f39ac_f39_ad_cyclicality_signature_marginlag_504d_base_v148_signal(gp, revenue):
    pg = _f39_cyc_phase(_f39_gross_margin(gp, revenue), 504)
    pr = _f39_cyc_phase(revenue, 504)
    b = pg - pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cyclical composite over 504d (amplitude x growth dispersion, long)
def f39ac_f39_ad_cyclicality_signature_cyccomp_504d_base_v149_signal(revenue):
    amp = _f39_cyc_amp(revenue, 504)
    disp = _std(_roc(revenue, 21), 504)
    b = amp * disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-intensity-weighted ebitda-margin cyclicality (ad-spend funded margin swing)
def f39ac_f39_ad_cyclicality_signature_adfundedmarg_252d_base_v150_signal(sgna, revenue, ebitdamargin):
    si = _f39_sales_intensity(sgna, revenue)
    ebcyc = _f39_detrend(ebitdamargin, 252)
    b = ebcyc * _z(si, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39ac_f39_ad_cyclicality_signature_revamp_126d_base_v076_signal,
    f39ac_f39_ad_cyclicality_signature_revphase_504d_base_v077_signal,
    f39ac_f39_ad_cyclicality_signature_opmamp_504d_base_v078_signal,
    f39ac_f39_ad_cyclicality_signature_salesint_504d_base_v079_signal,
    f39ac_f39_ad_cyclicality_signature_gmcompress_504d_base_v080_signal,
    f39ac_f39_ad_cyclicality_signature_revgpbeta_126d_base_v081_signal,
    f39ac_f39_ad_cyclicality_signature_ebmphase_126d_base_v082_signal,
    f39ac_f39_ad_cyclicality_signature_revcyc_504d_base_v083_signal,
    f39ac_f39_ad_cyclicality_signature_gpamp_126d_base_v084_signal,
    f39ac_f39_ad_cyclicality_signature_opmphase_504d_base_v085_signal,
    f39ac_f39_ad_cyclicality_signature_salesswing_504d_base_v086_signal,
    f39ac_f39_ad_cyclicality_signature_gmswing_126d_base_v087_signal,
    f39ac_f39_ad_cyclicality_signature_revphasemom_504d_base_v088_signal,
    f39ac_f39_ad_cyclicality_signature_opmcompress_504d_base_v089_signal,
    f39ac_f39_ad_cyclicality_signature_salesamp_126d_base_v090_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcyc_504d_base_v091_signal,
    f39ac_f39_ad_cyclicality_signature_revmargco_504d_base_v092_signal,
    f39ac_f39_ad_cyclicality_signature_gmphase_504d_base_v093_signal,
    f39ac_f39_ad_cyclicality_signature_opbeta_252d_base_v094_signal,
    f39ac_f39_ad_cyclicality_signature_ampratio_126v504_base_v095_signal,
    f39ac_f39_ad_cyclicality_signature_gmcomprank_504d_base_v096_signal,
    f39ac_f39_ad_cyclicality_signature_opmrevlag_252d_base_v097_signal,
    f39ac_f39_ad_cyclicality_signature_salescyc_504d_base_v098_signal,
    f39ac_f39_ad_cyclicality_signature_ebmphasemom_504d_base_v099_signal,
    f39ac_f39_ad_cyclicality_signature_revrecov_252d_base_v100_signal,
    f39ac_f39_ad_cyclicality_signature_gpphasez_504d_base_v101_signal,
    f39ac_f39_ad_cyclicality_signature_salesgmspr_504d_base_v102_signal,
    f39ac_f39_ad_cyclicality_signature_opmamp_126d_base_v103_signal,
    f39ac_f39_ad_cyclicality_signature_revsensdir_504d_base_v104_signal,
    f39ac_f39_ad_cyclicality_signature_gmrecov_504d_base_v105_signal,
    f39ac_f39_ad_cyclicality_signature_salesphase_126d_base_v106_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcompress_504d_base_v107_signal,
    f39ac_f39_ad_cyclicality_signature_revcycgap_504d_base_v108_signal,
    f39ac_f39_ad_cyclicality_signature_opgmdiv_504d_base_v109_signal,
    f39ac_f39_ad_cyclicality_signature_ampperint_504d_base_v110_signal,
    f39ac_f39_ad_cyclicality_signature_gmamp_504d_base_v111_signal,
    f39ac_f39_ad_cyclicality_signature_revgdisp_126d_base_v112_signal,
    f39ac_f39_ad_cyclicality_signature_salesstreak_126d_base_v113_signal,
    f39ac_f39_ad_cyclicality_signature_opmtrough_504d_base_v114_signal,
    f39ac_f39_ad_cyclicality_signature_ebmamp_126d_base_v115_signal,
    f39ac_f39_ad_cyclicality_signature_gprevsens_504d_base_v116_signal,
    f39ac_f39_ad_cyclicality_signature_countercyc_504d_base_v117_signal,
    f39ac_f39_ad_cyclicality_signature_gmdowndur_504d_base_v118_signal,
    f39ac_f39_ad_cyclicality_signature_cycexpos_504d_base_v119_signal,
    f39ac_f39_ad_cyclicality_signature_opebmgap_504d_base_v120_signal,
    f39ac_f39_ad_cyclicality_signature_revacccyc_126d_base_v121_signal,
    f39ac_f39_ad_cyclicality_signature_gmcyclz_252d_base_v122_signal,
    f39ac_f39_ad_cyclicality_signature_salesprocyc_504d_base_v123_signal,
    f39ac_f39_ad_cyclicality_signature_ebmdowndur_504d_base_v124_signal,
    f39ac_f39_ad_cyclicality_signature_revdowncount_504d_base_v125_signal,
    f39ac_f39_ad_cyclicality_signature_opmphasemom_504d_base_v126_signal,
    f39ac_f39_ad_cyclicality_signature_jointstress_504d_base_v127_signal,
    f39ac_f39_ad_cyclicality_signature_salesopspr_504d_base_v128_signal,
    f39ac_f39_ad_cyclicality_signature_amptrend_504d_base_v129_signal,
    f39ac_f39_ad_cyclicality_signature_gpcyc_504d_base_v130_signal,
    f39ac_f39_ad_cyclicality_signature_ebmrecov_252d_base_v131_signal,
    f39ac_f39_ad_cyclicality_signature_adresponse_252d_base_v132_signal,
    f39ac_f39_ad_cyclicality_signature_opmcomprank_504d_base_v133_signal,
    f39ac_f39_ad_cyclicality_signature_gmphasemom_504d_base_v134_signal,
    f39ac_f39_ad_cyclicality_signature_revtilt_504d_base_v135_signal,
    f39ac_f39_ad_cyclicality_signature_salescut_504d_base_v136_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcycmom_504d_base_v137_signal,
    f39ac_f39_ad_cyclicality_signature_jointamp_504d_base_v138_signal,
    f39ac_f39_ad_cyclicality_signature_phasesync_504d_base_v139_signal,
    f39ac_f39_ad_cyclicality_signature_marginpass_252d_base_v140_signal,
    f39ac_f39_ad_cyclicality_signature_revupturn_504d_base_v141_signal,
    f39ac_f39_ad_cyclicality_signature_salesdisp_504d_base_v142_signal,
    f39ac_f39_ad_cyclicality_signature_ebmamplify_252d_base_v143_signal,
    f39ac_f39_ad_cyclicality_signature_revampz_504d_base_v144_signal,
    f39ac_f39_ad_cyclicality_signature_compspr_504d_base_v145_signal,
    f39ac_f39_ad_cyclicality_signature_peakdist_504d_base_v146_signal,
    f39ac_f39_ad_cyclicality_signature_spenddisc_504d_base_v147_signal,
    f39ac_f39_ad_cyclicality_signature_marginlag_504d_base_v148_signal,
    f39ac_f39_ad_cyclicality_signature_cyccomp_504d_base_v149_signal,
    f39ac_f39_ad_cyclicality_signature_adfundedmarg_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_AD_CYCLICALITY_SIGNATURE_REGISTRY_076_150 = REGISTRY


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

    print("OK f39_ad_cyclicality_signature_base_076_150_claude: %d features pass" % n_features)
