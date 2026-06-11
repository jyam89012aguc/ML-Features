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


def _ewm(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _med(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ===== folder domain primitives (profitability quality levels) =====
def _f15_gross_margin(revenue, gp):
    return gp / revenue.replace(0, np.nan)


def _f15_op_margin(revenue, opinc):
    return opinc / revenue.replace(0, np.nan)


def _f15_net_margin(revenue, netinc):
    return netinc / revenue.replace(0, np.nan)


def _f15_ebitda_margin(revenue, ebitda):
    return ebitda / revenue.replace(0, np.nan)


def _f15_ebit_margin(revenue, ebit):
    return ebit / revenue.replace(0, np.nan)


def _f15_roe(netinc, equity):
    return netinc / equity.replace(0, np.nan)


def _f15_roa(netinc, assets):
    return netinc / assets.replace(0, np.nan)


def _f15_gp_to_assets(gp, assets):
    return gp / assets.replace(0, np.nan)


def _f15_invcap(equity, assets):
    return (equity + 0.4 * (assets - equity)).replace(0, np.nan)


# ============================================================
# --- gross margin: dispersion/quality variants ---
def f15pq_f15_profitability_quality_gm_iqr_252d_base_v076_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    b = gm.rolling(252, min_periods=126).quantile(0.75) - gm.rolling(252, min_periods=126).quantile(0.25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gm_mom_252d_base_v077_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    sm = _mean(gm, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gm_above_med_504d_base_v078_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    b = (gm - _med(gm, 504)) / _std(gm, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating margin variants ---
def f15pq_f15_profitability_quality_om_iqr_252d_base_v079_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    b = om.rolling(252, min_periods=126).quantile(0.75) - om.rolling(252, min_periods=126).quantile(0.25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_om_mom_252d_base_v080_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    sm = _mean(om, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_om_min_252d_base_v081_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    floor = om.rolling(252, min_periods=126).min()
    b = (om - floor) / (1.0 + om.rolling(252, min_periods=126).std())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net margin variants ---
def f15pq_f15_profitability_quality_nm_mom_252d_base_v082_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    sm = _mean(nm, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nm_downcapture_252d_base_v083_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    med = _med(nm, 252)
    down = (nm - med).clip(upper=0)
    b = down.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nm_kurtproxy_252d_base_v084_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    b = nm.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebitda margin variants ---
def f15pq_f15_profitability_quality_em_mom_252d_base_v085_signal(revenue, ebitda):
    em = _f15_ebitda_margin(revenue, ebitda)
    sm = _mean(em, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_em_rangepos_504d_base_v086_signal(revenue, ebitda):
    em = _f15_ebitda_margin(revenue, ebitda)
    hi = em.rolling(504, min_periods=252).max()
    lo = em.rolling(504, min_periods=252).min()
    b = (em - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebit margin variants ---
def f15pq_f15_profitability_quality_ebm_mom_252d_base_v087_signal(revenue, ebit):
    ebm = _f15_ebit_margin(revenue, ebit)
    sm = _mean(ebm, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebm_stab_252d_base_v088_signal(revenue, ebit):
    ebm = _f15_ebit_margin(revenue, ebit)
    b = _mean(ebm, 252) / _std(ebm, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROE variants ---
def f15pq_f15_profitability_quality_roe_mom_252d_base_v089_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    sm = _mean(roe, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roe_iqr_252d_base_v090_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    b = roe.rolling(252, min_periods=126).quantile(0.8) - roe.rolling(252, min_periods=126).quantile(0.2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roe_sharpe_252d_base_v091_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    chg = roe.diff()
    b = _mean(chg, 252) / _std(chg, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROA variants ---
def f15pq_f15_profitability_quality_roa_mom_252d_base_v092_signal(netinc, assets):
    roa = _f15_roa(netinc, assets)
    sm = _mean(roa, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roa_rank_504d_base_v093_signal(netinc, assets):
    roa = _f15_roa(netinc, assets)
    b = _rank(roa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roa_downvol_252d_base_v094_signal(netinc, assets):
    roa = _f15_roa(netinc, assets)
    med = _med(roa, 252)
    down = (roa - med).clip(upper=0)
    b = np.sqrt((down ** 2).rolling(252, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross profitability (gp/assets) variants ---
def f15pq_f15_profitability_quality_gpa_mom_252d_base_v095_signal(gp, assets):
    gpa = _f15_gp_to_assets(gp, assets)
    sm = _mean(gpa, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpa_stab_252d_base_v096_signal(gp, assets):
    gpa = _f15_gp_to_assets(gp, assets)
    b = _mean(gpa, 252) / _std(gpa, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpa_rangepos_1260d_base_v097_signal(gp, assets):
    gpa = _f15_gp_to_assets(gp, assets)
    hi = gpa.rolling(1260, min_periods=504).max()
    lo = gpa.rolling(1260, min_periods=504).min()
    b = (gpa - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebitda return on assets variant ---
def f15pq_f15_profitability_quality_ebitdaroa_mom_252d_base_v098_signal(ebitda, assets):
    r = ebitda / assets.replace(0, np.nan)
    sm = _mean(r, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitdaroa_rank_504d_base_v099_signal(ebitda, assets):
    r = ebitda / assets.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebit return on assets variant ---
def f15pq_f15_profitability_quality_ebitroa_z_252d_base_v100_signal(ebit, assets):
    r = ebit / assets.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating income return on assets momentum ---
def f15pq_f15_profitability_quality_oproa_mom_252d_base_v101_signal(opinc, assets):
    r = opinc / assets.replace(0, np.nan)
    sm = _mean(r, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin dispersion variants (across types) ---
def f15pq_f15_profitability_quality_mgndisp_z_252d_base_v102_signal(revenue, gp, opinc, netinc):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    nm = _f15_net_margin(revenue, netinc)
    disp = pd.concat([gm, om, nm], axis=1).std(axis=1)
    b = _z(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgndisp5_63d_base_v103_signal(revenue, gp, opinc, ebitda, ebit):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    em = _f15_ebitda_margin(revenue, ebitda)
    ebm = _f15_ebit_margin(revenue, ebit)
    disp = pd.concat([gm, om, em, ebm], axis=1).std(axis=1)
    b = _mean(disp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgnrange_mom_63d_base_v104_signal(revenue, gp, netinc):
    gm = _f15_gross_margin(revenue, gp)
    nm = _f15_net_margin(revenue, netinc)
    spread = gm - nm
    sm = _mean(spread, 63)
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin tier stack-rank coherence ---
def f15pq_f15_profitability_quality_mgnorder_252d_base_v105_signal(revenue, gp, opinc, netinc):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    nm = _f15_net_margin(revenue, netinc)
    ordered = ((gm >= om).astype(float) + (om >= nm).astype(float)) - 1.0
    b = ordered.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross-to-net spread z (cost leakage) ---
def f15pq_f15_profitability_quality_gmnmspr_z_252d_base_v106_signal(revenue, gp, netinc):
    gm = _f15_gross_margin(revenue, gp)
    nm = _f15_net_margin(revenue, netinc)
    b = _z(gm - nm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating leakage share: (gm-om)/gm momentum ---
def f15pq_f15_profitability_quality_opleak_mom_126d_base_v107_signal(revenue, gp, opinc):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    leak = (gm - om) / gm.replace(0, np.nan)
    sm = _mean(leak, 63)
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- below-operating leakage: (om-nm)/om level ---
def f15pq_f15_profitability_quality_belowop_63d_base_v108_signal(revenue, opinc, netinc):
    om = _f15_op_margin(revenue, opinc)
    nm = _f15_net_margin(revenue, netinc)
    leak = (om - nm) / om.replace(0, np.nan)
    b = _mean(leak, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite return rank (roe, roa, ebitda-roa) ---
def f15pq_f15_profitability_quality_retcomp_504d_base_v109_signal(netinc, equity, assets, ebitda):
    roe = _f15_roe(netinc, equity)
    roa = _f15_roa(netinc, assets)
    er = ebitda / assets.replace(0, np.nan)
    b = (_rank(roe, 504) + _rank(roa, 504) + _rank(er, 504)) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin composite minus its own slow mean (margin pulse) ---
def f15pq_f15_profitability_quality_mgnpulse_base_v110_signal(revenue, gp, opinc, netinc, ebitda):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    nm = _f15_net_margin(revenue, netinc)
    em = _f15_ebitda_margin(revenue, ebitda)
    idx = (gm + om + nm + em) / 4.0
    b = _mean(idx, 21) - _mean(idx, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross profit per equity de-trended ---
def f15pq_f15_profitability_quality_gpequ_z_252d_base_v111_signal(gp, equity):
    r = gp / equity.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebit per equity de-trended ---
def f15pq_f15_profitability_quality_ebitequ_z_252d_base_v112_signal(ebit, equity):
    r = ebit / equity.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebitda per equity level ---
def f15pq_f15_profitability_quality_ebitdaequ_63d_base_v113_signal(ebitda, equity):
    r = ebitda / equity.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net margin per unit of margin volatility (information-ratio of profitability) ---
def f15pq_f15_profitability_quality_nm_ir_252d_base_v114_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    b = _mean(nm, 252) / _std(nm, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross margin tanh-bounded level ---
def f15pq_f15_profitability_quality_gmtanh_63d_base_v115_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    b = np.tanh(4.0 * (_mean(gm, 63) - 0.4))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating margin sign x sqrt magnitude (robust) ---
def f15pq_f15_profitability_quality_omsignmag_63d_base_v116_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    sm = np.sign(om) * np.sqrt(om.abs())
    b = _mean(sm, 63) - _mean(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROE convexity (above/below median squared) ---
def f15pq_f15_profitability_quality_roeconvex_252d_base_v117_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    med = _med(roe, 252)
    b = np.sign(roe - med) * (roe - med) ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- profit captures: netinc/ebit (tax+interest drag on operating profit) ---
def f15pq_f15_profitability_quality_niebitcap_63d_base_v118_signal(netinc, ebit):
    cap = netinc / ebit.replace(0, np.nan)
    b = _mean(cap, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- opinc/ebitda: operating-to-cash earnings (D&A consumption of operating cash) ---
def f15pq_f15_profitability_quality_opebitda_63d_base_v119_signal(opinc, ebitda):
    cap = opinc / ebitda.replace(0, np.nan)
    b = _mean(cap, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gp/ebitda: gross-to-cash earnings conversion ---
def f15pq_f15_profitability_quality_gpebitda_z_252d_base_v120_signal(gp, ebitda):
    cap = gp / ebitda.replace(0, np.nan)
    b = _z(cap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROIC (ebit-based) level ---
def f15pq_f15_profitability_quality_ebitroic_63d_base_v121_signal(ebit, equity, assets):
    invcap = _f15_invcap(equity, assets)
    roic = ebit / invcap
    b = _mean(roic, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROIC (ebit-based) momentum ---
def f15pq_f15_profitability_quality_ebitroic_mom_252d_base_v122_signal(ebit, equity, assets):
    invcap = _f15_invcap(equity, assets)
    roic = ebit / invcap
    sm = _mean(roic, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROIC (ebitda-based) level ---
def f15pq_f15_profitability_quality_ebitdaroic_63d_base_v123_signal(ebitda, equity, assets):
    invcap = _f15_invcap(equity, assets)
    roic = ebitda / invcap
    b = _mean(roic, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- asset turnover de-trended (sales productivity, supports profitability) ---
def f15pq_f15_profitability_quality_assetturn_z_252d_base_v124_signal(revenue, assets):
    at = revenue / assets.replace(0, np.nan)
    b = _z(at, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross-margin x asset-turnover (gross profitability decomposition product) ---
def f15pq_f15_profitability_quality_gmxturn_63d_base_v125_signal(revenue, gp, assets):
    gm = _f15_gross_margin(revenue, gp)
    at = revenue / assets.replace(0, np.nan)
    prod = gm * at
    b = _z(prod, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin breadth composite z (how many margins above their own z=0) ---
def f15pq_f15_profitability_quality_mgnstrength_252d_base_v126_signal(revenue, gp, opinc, netinc):
    gm = _z(_f15_gross_margin(revenue, gp), 252)
    om = _z(_f15_op_margin(revenue, opinc), 252)
    nm = _z(_f15_net_margin(revenue, netinc), 252)
    b = (gm + om + nm) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- profitability quality: ROA stability x level ---
def f15pq_f15_profitability_quality_roaqual_252d_base_v127_signal(netinc, assets):
    roa = _f15_roa(netinc, assets)
    lvl = _mean(roa, 252)
    sd = _std(roa, 252)
    b = lvl / (1.0 + sd.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebitda margin quality (level / vol) ---
def f15pq_f15_profitability_quality_emqual_252d_base_v128_signal(revenue, ebitda):
    em = _f15_ebitda_margin(revenue, ebitda)
    lvl = _mean(em, 252)
    sd = _std(em, 252)
    b = lvl / (1.0 + sd.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net margin range position (5y) ---
def f15pq_f15_profitability_quality_nmrangepos_1260d_base_v129_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    hi = nm.rolling(1260, min_periods=504).max()
    lo = nm.rolling(1260, min_periods=504).min()
    b = (nm - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating margin range position (5y) ---
def f15pq_f15_profitability_quality_omrangepos_1260d_base_v130_signal(revenue, opinc):
    om = _f15_op_margin(revenue, opinc)
    hi = om.rolling(1260, min_periods=504).max()
    lo = om.rolling(1260, min_periods=504).min()
    b = (om - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROA percentile in 5y history ---
def f15pq_f15_profitability_quality_roarank_1260d_base_v131_signal(netinc, assets):
    roa = _f15_roa(netinc, assets)
    b = _rank(roa, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross profitability percentile in 5y history ---
def f15pq_f15_profitability_quality_gparank_1260d_base_v132_signal(gp, assets):
    gpa = _f15_gp_to_assets(gp, assets)
    b = _rank(gpa, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin spread (gm-om) range position ---
def f15pq_f15_profitability_quality_gmomspr_rangepos_504d_base_v133_signal(revenue, gp, opinc):
    gm = _f15_gross_margin(revenue, gp)
    om = _f15_op_margin(revenue, opinc)
    spr = gm - om
    hi = spr.rolling(504, min_periods=252).max()
    lo = spr.rolling(504, min_periods=252).min()
    b = (spr - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- pretax-to-aftertax capital-return wedge: roic(ebit) / roa(netinc) de-trended ---
def f15pq_f15_profitability_quality_roicroawedge_252d_base_v134_signal(ebit, netinc, equity, assets):
    invcap = _f15_invcap(equity, assets)
    roic = ebit / invcap
    roa = netinc / assets.replace(0, np.nan)
    wedge = roic / roa.replace(0, np.nan)
    b = _z(wedge, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebitda margin minus net margin (cash vs accrual profitability gap) ---
def f15pq_f15_profitability_quality_emnmspr_63d_base_v135_signal(revenue, ebitda, netinc):
    em = _f15_ebitda_margin(revenue, ebitda)
    nm = _f15_net_margin(revenue, netinc)
    b = (em - nm).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross profit per dollar of revenue x stability (durable gross quality) ---
def f15pq_f15_profitability_quality_gmdurable_504d_base_v136_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    lvl = _rank(gm, 504)
    instab = _std(gm, 252) / _mean(gm, 252).abs().replace(0, np.nan)
    b = lvl - instab
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- profitability acceleration-as-level: net margin minus its lagged half-year mean ---
def f15pq_f15_profitability_quality_nm_vs_lag_126d_base_v137_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    cur = _mean(nm, 63)
    lag = _mean(nm, 126).shift(126)
    b = cur - lag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROE de-trended vs 5y norm ---
def f15pq_f15_profitability_quality_roe_vs_norm_1260d_base_v138_signal(netinc, equity):
    roe = _f15_roe(netinc, equity)
    norm = roe.rolling(1260, min_periods=504).mean()
    b = (roe - norm) / roe.rolling(1260, min_periods=504).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating ROIC stability (inverse CV of opinc/invcap over the year) ---
def f15pq_f15_profitability_quality_oproic_stab_252d_base_v139_signal(opinc, equity, assets):
    invcap = _f15_invcap(equity, assets)
    roic = opinc / invcap
    b = _mean(roic, 252) / _std(roic, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- profit quality composite: rank(gm) + rank(roa) - rank(margin vol) ---
def f15pq_f15_profitability_quality_qualscore_504d_base_v140_signal(revenue, gp, netinc, assets):
    gm = _f15_gross_margin(revenue, gp)
    roa = _f15_roa(netinc, assets)
    nmv = _std(_f15_net_margin(revenue, netinc), 252)
    b = _rank(gm, 504) + _rank(roa, 504) - _rank(nmv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebit margin convexity ---
def f15pq_f15_profitability_quality_ebmconvex_252d_base_v141_signal(revenue, ebit):
    ebm = _f15_ebit_margin(revenue, ebit)
    med = _med(ebm, 252)
    b = np.sign(ebm - med) * (ebm - med) ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross margin vol-of-level (vol of the 63d gm mean over a year) ---
def f15pq_f15_profitability_quality_gmvolofmean_252d_base_v142_signal(revenue, gp):
    gm = _f15_gross_margin(revenue, gp)
    sm = _mean(gm, 63)
    b = _std(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net-margin floor distance (how far above worst recent margin) ---
def f15pq_f15_profitability_quality_nmfloor_252d_base_v143_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    floor = nm.rolling(252, min_periods=126).min()
    b = (nm - floor) / (1.0 + nm.rolling(252, min_periods=126).std())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROIC dispersion across three numerators (opinc/ebit/ebitda on invcap) ---
def f15pq_f15_profitability_quality_roicdisp_63d_base_v144_signal(opinc, ebit, ebitda, equity, assets):
    invcap = _f15_invcap(equity, assets)
    a = opinc / invcap
    b1 = ebit / invcap
    c = ebitda / invcap
    disp = pd.concat([a, b1, c], axis=1).std(axis=1)
    b = _mean(disp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross-to-net retention ratio (netinc/gp) level ---
def f15pq_f15_profitability_quality_nigpret_63d_base_v145_signal(gp, netinc):
    ret = netinc / gp.replace(0, np.nan)
    b = _mean(ret, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- earnings-power per asset breadth (count of return metrics in top half) ---
def f15pq_f15_profitability_quality_retbreadth_504d_base_v146_signal(netinc, equity, assets, opinc):
    roe = _rank(_f15_roe(netinc, equity), 504)
    roa = _rank(_f15_roa(netinc, assets), 504)
    oproa = _rank(opinc / assets.replace(0, np.nan), 504)
    raw = (roe > 0).astype(float) + (roa > 0).astype(float) + (oproa > 0).astype(float) - 1.5
    b = raw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margin compression flag intensity: net margin below 5th pct of its year ---
def f15pq_f15_profitability_quality_nmstress_252d_base_v147_signal(revenue, netinc):
    nm = _f15_net_margin(revenue, netinc)
    p10 = nm.rolling(252, min_periods=126).quantile(0.10)
    stress = (p10 - nm).clip(lower=0)
    b = stress.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROE-to-ROA ratio de-trended (leverage amplification shift) ---
def f15pq_f15_profitability_quality_levampshift_252d_base_v148_signal(netinc, equity, assets):
    roe = _f15_roe(netinc, equity)
    roa = _f15_roa(netinc, assets)
    amp = roe / roa.replace(0, np.nan)
    b = amp - amp.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite cash-profitability: ebitda margin rank + ebitda-roa rank ---
def f15pq_f15_profitability_quality_cashprof_504d_base_v149_signal(revenue, ebitda, assets):
    em = _rank(_f15_ebitda_margin(revenue, ebitda), 504)
    er = _rank(ebitda / assets.replace(0, np.nan), 504)
    b = (em + er) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gross-profitability minus net-margin (asset-quality vs sales-quality divergence) ---
def f15pq_f15_profitability_quality_gpavsnm_504d_base_v150_signal(gp, assets, revenue, netinc):
    gpa = _rank(_f15_gp_to_assets(gp, assets), 504)
    nm = _rank(_f15_net_margin(revenue, netinc), 504)
    b = gpa - nm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15pq_f15_profitability_quality_gm_iqr_252d_base_v076_signal,
    f15pq_f15_profitability_quality_gm_mom_252d_base_v077_signal,
    f15pq_f15_profitability_quality_gm_above_med_504d_base_v078_signal,
    f15pq_f15_profitability_quality_om_iqr_252d_base_v079_signal,
    f15pq_f15_profitability_quality_om_mom_252d_base_v080_signal,
    f15pq_f15_profitability_quality_om_min_252d_base_v081_signal,
    f15pq_f15_profitability_quality_nm_mom_252d_base_v082_signal,
    f15pq_f15_profitability_quality_nm_downcapture_252d_base_v083_signal,
    f15pq_f15_profitability_quality_nm_kurtproxy_252d_base_v084_signal,
    f15pq_f15_profitability_quality_em_mom_252d_base_v085_signal,
    f15pq_f15_profitability_quality_em_rangepos_504d_base_v086_signal,
    f15pq_f15_profitability_quality_ebm_mom_252d_base_v087_signal,
    f15pq_f15_profitability_quality_ebm_stab_252d_base_v088_signal,
    f15pq_f15_profitability_quality_roe_mom_252d_base_v089_signal,
    f15pq_f15_profitability_quality_roe_iqr_252d_base_v090_signal,
    f15pq_f15_profitability_quality_roe_sharpe_252d_base_v091_signal,
    f15pq_f15_profitability_quality_roa_mom_252d_base_v092_signal,
    f15pq_f15_profitability_quality_roa_rank_504d_base_v093_signal,
    f15pq_f15_profitability_quality_roa_downvol_252d_base_v094_signal,
    f15pq_f15_profitability_quality_gpa_mom_252d_base_v095_signal,
    f15pq_f15_profitability_quality_gpa_stab_252d_base_v096_signal,
    f15pq_f15_profitability_quality_gpa_rangepos_1260d_base_v097_signal,
    f15pq_f15_profitability_quality_ebitdaroa_mom_252d_base_v098_signal,
    f15pq_f15_profitability_quality_ebitdaroa_rank_504d_base_v099_signal,
    f15pq_f15_profitability_quality_ebitroa_z_252d_base_v100_signal,
    f15pq_f15_profitability_quality_oproa_mom_252d_base_v101_signal,
    f15pq_f15_profitability_quality_mgndisp_z_252d_base_v102_signal,
    f15pq_f15_profitability_quality_mgndisp5_63d_base_v103_signal,
    f15pq_f15_profitability_quality_mgnrange_mom_63d_base_v104_signal,
    f15pq_f15_profitability_quality_mgnorder_252d_base_v105_signal,
    f15pq_f15_profitability_quality_gmnmspr_z_252d_base_v106_signal,
    f15pq_f15_profitability_quality_opleak_mom_126d_base_v107_signal,
    f15pq_f15_profitability_quality_belowop_63d_base_v108_signal,
    f15pq_f15_profitability_quality_retcomp_504d_base_v109_signal,
    f15pq_f15_profitability_quality_mgnpulse_base_v110_signal,
    f15pq_f15_profitability_quality_gpequ_z_252d_base_v111_signal,
    f15pq_f15_profitability_quality_ebitequ_z_252d_base_v112_signal,
    f15pq_f15_profitability_quality_ebitdaequ_63d_base_v113_signal,
    f15pq_f15_profitability_quality_nm_ir_252d_base_v114_signal,
    f15pq_f15_profitability_quality_gmtanh_63d_base_v115_signal,
    f15pq_f15_profitability_quality_omsignmag_63d_base_v116_signal,
    f15pq_f15_profitability_quality_roeconvex_252d_base_v117_signal,
    f15pq_f15_profitability_quality_niebitcap_63d_base_v118_signal,
    f15pq_f15_profitability_quality_opebitda_63d_base_v119_signal,
    f15pq_f15_profitability_quality_gpebitda_z_252d_base_v120_signal,
    f15pq_f15_profitability_quality_ebitroic_63d_base_v121_signal,
    f15pq_f15_profitability_quality_ebitroic_mom_252d_base_v122_signal,
    f15pq_f15_profitability_quality_ebitdaroic_63d_base_v123_signal,
    f15pq_f15_profitability_quality_assetturn_z_252d_base_v124_signal,
    f15pq_f15_profitability_quality_gmxturn_63d_base_v125_signal,
    f15pq_f15_profitability_quality_mgnstrength_252d_base_v126_signal,
    f15pq_f15_profitability_quality_roaqual_252d_base_v127_signal,
    f15pq_f15_profitability_quality_emqual_252d_base_v128_signal,
    f15pq_f15_profitability_quality_nmrangepos_1260d_base_v129_signal,
    f15pq_f15_profitability_quality_omrangepos_1260d_base_v130_signal,
    f15pq_f15_profitability_quality_roarank_1260d_base_v131_signal,
    f15pq_f15_profitability_quality_gparank_1260d_base_v132_signal,
    f15pq_f15_profitability_quality_gmomspr_rangepos_504d_base_v133_signal,
    f15pq_f15_profitability_quality_roicroawedge_252d_base_v134_signal,
    f15pq_f15_profitability_quality_emnmspr_63d_base_v135_signal,
    f15pq_f15_profitability_quality_gmdurable_504d_base_v136_signal,
    f15pq_f15_profitability_quality_nm_vs_lag_126d_base_v137_signal,
    f15pq_f15_profitability_quality_roe_vs_norm_1260d_base_v138_signal,
    f15pq_f15_profitability_quality_oproic_stab_252d_base_v139_signal,
    f15pq_f15_profitability_quality_qualscore_504d_base_v140_signal,
    f15pq_f15_profitability_quality_ebmconvex_252d_base_v141_signal,
    f15pq_f15_profitability_quality_gmvolofmean_252d_base_v142_signal,
    f15pq_f15_profitability_quality_nmfloor_252d_base_v143_signal,
    f15pq_f15_profitability_quality_roicdisp_63d_base_v144_signal,
    f15pq_f15_profitability_quality_nigpret_63d_base_v145_signal,
    f15pq_f15_profitability_quality_retbreadth_504d_base_v146_signal,
    f15pq_f15_profitability_quality_nmstress_252d_base_v147_signal,
    f15pq_f15_profitability_quality_levampshift_252d_base_v148_signal,
    f15pq_f15_profitability_quality_cashprof_504d_base_v149_signal,
    f15pq_f15_profitability_quality_gpavsnm_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_PROFITABILITY_QUALITY_REGISTRY_076_150 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(1, n, base=1e9, drift=0.02, vol=0.04).rename("revenue")
    gp = _fund(2, n, base=4e8, drift=0.02, vol=0.05).rename("gp")
    opinc = _fund(3, n, base=2e8, drift=0.02, vol=0.06, allow_neg=True).rename("opinc")
    netinc = _fund(4, n, base=1.5e8, drift=0.02, vol=0.07, allow_neg=True).rename("netinc")
    ebitda = _fund(5, n, base=3e8, drift=0.02, vol=0.05).rename("ebitda")
    ebit = _fund(6, n, base=2.2e8, drift=0.02, vol=0.06).rename("ebit")
    equity = _fund(7, n, base=2e9, drift=0.015, vol=0.04).rename("equity")
    assets = _fund(8, n, base=5e9, drift=0.015, vol=0.03).rename("assets")

    cols = {"revenue": revenue, "gp": gp, "opinc": opinc, "netinc": netinc,
            "ebitda": ebitda, "ebit": ebit, "equity": equity, "assets": assets}

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

    print("OK f15_profitability_quality_base_076_150_claude: %d features pass" % n_features)
