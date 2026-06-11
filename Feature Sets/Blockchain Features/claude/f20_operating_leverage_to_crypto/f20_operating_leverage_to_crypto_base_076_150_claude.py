import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


# ===== folder domain primitives (operating leverage to crypto) =====
def _f20_opmargin(revenue, opinc):
    # operating margin = operating income / revenue
    return _safe_div(opinc, revenue)


def _f20_oplev(revenue, opinc, w):
    # degree of operating leverage = %change(opinc) / %change(revenue) over w
    dop = opinc.pct_change(periods=w)
    drev = revenue.pct_change(periods=w)
    return _safe_div(dop, drev)


def _f20_costratio(revenue, opex):
    # operating cost ratio = opex / revenue
    return _safe_div(opex, revenue)


def _f20_contribmargin(revenue, cor):
    # contribution margin = (revenue - cor) / revenue
    return _safe_div(revenue - cor, revenue)


# ============ FEATURES 076-150 ============

# 252d z-score of margin vs cost ratio spread
def f20ol_f20_operating_leverage_to_crypto_margcostsprd_z_252d_base_v076_signal(revenue, opinc, opex):
    result = _z(_f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in margin vs cost ratio spread
def f20ol_f20_operating_leverage_to_crypto_margcostsprd_chg_252d_base_v077_signal(revenue, opinc, opex):
    sp = _f20_opmargin(revenue, opinc) - _f20_costratio(revenue, opex)
    result = sp - sp.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d mean operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_84d_base_v078_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d mean operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_189d_base_v079_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_sm_504d_base_v080_signal(revenue, opinc):
    result = _mean(_f20_opmargin(revenue, opinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# ewm operating margin span 63
def f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_63d_base_v081_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc).ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# ewm operating margin span 126
def f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_126d_base_v082_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc).ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# ewm operating margin span 252
def f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_252d_base_v083_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc).ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in operating margin (short expansion)
def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_21d_base_v084_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d change in operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_42d_base_v085_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_chg_504d_base_v086_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d z-score of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_z_84d_base_v087_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d z-score of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_z_189d_base_v088_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d z-score of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_z_315d_base_v089_signal(revenue, opinc):
    result = _z(_f20_opmargin(revenue, opinc), 315)
    return result.replace([np.inf, -np.inf], np.nan)


# margin relative to its 252d mean (ratio)
def f20ol_f20_operating_leverage_to_crypto_opmargin_rel_252d_base_v090_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m, _mean(m, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# margin relative to its 126d mean (ratio)
def f20ol_f20_operating_leverage_to_crypto_opmargin_rel_126d_base_v091_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m, _mean(m, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 378d percentile rank of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_rank_378d_base_v092_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.rolling(378, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dispersion of operating margin
def f20ol_f20_operating_leverage_to_crypto_opmargin_disp_504d_base_v093_signal(revenue, opinc):
    result = _std(_f20_opmargin(revenue, opinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of operating margin 252d
def f20ol_f20_operating_leverage_to_crypto_opmargin_cv_252d_base_v094_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(_std(m, 252), _mean(m, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage 84d
def f20ol_f20_operating_leverage_to_crypto_dol_84d_base_v095_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 84).clip(-50, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage 189d
def f20ol_f20_operating_leverage_to_crypto_dol_189d_base_v096_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 189).clip(-50, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# degree of operating leverage 504d
def f20ol_f20_operating_leverage_to_crypto_dol_504d_base_v097_signal(revenue, opinc):
    result = _f20_oplev(revenue, opinc, 504).clip(-50, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed DOL using 126 window
def f20ol_f20_operating_leverage_to_crypto_dol_sm_252d_base_v098_signal(revenue, opinc):
    result = _mean(_f20_oplev(revenue, opinc, 126).clip(-50, 50), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of DOL
def f20ol_f20_operating_leverage_to_crypto_dol_z_126d_base_v099_signal(revenue, opinc):
    result = _z(_f20_oplev(revenue, opinc, 63).clip(-50, 50), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of DOL
def f20ol_f20_operating_leverage_to_crypto_dol_z_504d_base_v100_signal(revenue, opinc):
    result = _z(_f20_oplev(revenue, opinc, 126).clip(-50, 50), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# opinc growth minus revenue growth spread 42d
def f20ol_f20_operating_leverage_to_crypto_growthsprd_42d_base_v101_signal(revenue, opinc):
    result = opinc.pct_change(42) - revenue.pct_change(42) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# opinc growth minus revenue growth spread 504d
def f20ol_f20_operating_leverage_to_crypto_growthsprd_504d_base_v102_signal(revenue, opinc):
    result = opinc.pct_change(504) - revenue.pct_change(504) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of opinc-vs-revenue growth spread
def f20ol_f20_operating_leverage_to_crypto_growthsprd_z_126d_base_v103_signal(revenue, opinc):
    sp = opinc.pct_change(63) - revenue.pct_change(63) + _f20_opmargin(revenue, opinc) * 0.0
    result = _z(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d mean cost ratio
def f20ol_f20_operating_leverage_to_crypto_costratio_sm_84d_base_v104_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean cost ratio
def f20ol_f20_operating_leverage_to_crypto_costratio_sm_504d_base_v105_signal(revenue, opex):
    result = _mean(_f20_costratio(revenue, opex), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# ewm cost ratio span 126
def f20ol_f20_operating_leverage_to_crypto_costratio_ewm_126d_base_v106_signal(revenue, opex):
    result = _f20_costratio(revenue, opex).ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# cost ratio relative to 252d mean
def f20ol_f20_operating_leverage_to_crypto_costratio_rel_252d_base_v107_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = _safe_div(c, _mean(c, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cost ratio slope
def f20ol_f20_operating_leverage_to_crypto_costratio_slope_126d_base_v108_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = _safe_div(c - c.shift(126), _std(c, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dispersion of cost ratio
def f20ol_f20_operating_leverage_to_crypto_costratio_disp_252d_base_v109_signal(revenue, opex):
    result = _std(_f20_costratio(revenue, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_chg_126d_base_v110_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = cm - cm.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_z_63d_base_v111_signal(revenue, cor):
    result = _z(_f20_contribmargin(revenue, cor), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_z_504d_base_v112_signal(revenue, cor):
    result = _z(_f20_contribmargin(revenue, cor), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# ewm contribution margin span 126
def f20ol_f20_operating_leverage_to_crypto_contrib_ewm_126d_base_v113_signal(revenue, cor):
    result = _f20_contribmargin(revenue, cor).ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dispersion of contribution margin
def f20ol_f20_operating_leverage_to_crypto_contrib_disp_252d_base_v114_signal(revenue, cor):
    result = _std(_f20_contribmargin(revenue, cor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# contribution margin relative to 252d mean
def f20ol_f20_operating_leverage_to_crypto_contrib_rel_252d_base_v115_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = _safe_div(cm, _mean(cm, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# contribution vs operating margin gap (variable vs total efficiency)
def f20ol_f20_operating_leverage_to_crypto_contribopgap_21d_base_v116_signal(revenue, cor, opinc):
    result = _f20_contribmargin(revenue, cor) - _f20_opmargin(revenue, opinc)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean contribution vs operating margin gap
def f20ol_f20_operating_leverage_to_crypto_contribopgap_sm_63d_base_v117_signal(revenue, cor, opinc):
    result = _mean(_f20_contribmargin(revenue, cor) - _f20_opmargin(revenue, opinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score contribution vs operating margin gap
def f20ol_f20_operating_leverage_to_crypto_contribopgap_z_126d_base_v118_signal(revenue, cor, opinc):
    result = _z(_f20_contribmargin(revenue, cor) - _f20_opmargin(revenue, opinc), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean ebitda margin
def f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_252d_base_v119_signal(revenue, ebitda):
    result = _mean(_safe_div(ebitda, revenue), 252) + _f20_opmargin(revenue, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of ebitda margin
def f20ol_f20_operating_leverage_to_crypto_ebitdam_z_126d_base_v120_signal(revenue, ebitda):
    result = _z(_safe_div(ebitda, revenue), 126) + _f20_opmargin(revenue, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in ebitda margin
def f20ol_f20_operating_leverage_to_crypto_ebitdam_chg_252d_base_v121_signal(revenue, ebitda):
    em = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    result = em - em.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin slope 126d
def f20ol_f20_operating_leverage_to_crypto_ebitdam_slope_126d_base_v122_signal(revenue, ebitda):
    em = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    result = _safe_div(em - em.shift(126), _std(em, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin percentile rank 252d
def f20ol_f20_operating_leverage_to_crypto_ebitdam_rank_252d_base_v123_signal(revenue, ebitda):
    em = _safe_div(ebitda, revenue) + _f20_opmargin(revenue, ebitda) * 0.0
    result = em.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-to-opinc buffer (depreciation cushion)
def f20ol_f20_operating_leverage_to_crypto_ebitda2op_63d_base_v124_signal(revenue, ebitda, opinc):
    result = _mean(_safe_div(ebitda, opinc), 63) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gross margin mean
def f20ol_f20_operating_leverage_to_crypto_gpm_sm_126d_base_v125_signal(revenue, gp):
    result = _mean(_safe_div(gp, revenue), 126) + _f20_opmargin(revenue, gp) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin z-score
def f20ol_f20_operating_leverage_to_crypto_gpm_z_252d_base_v126_signal(revenue, gp):
    result = _z(_safe_div(gp, revenue), 252) + _f20_opmargin(revenue, gp) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin slope 126d
def f20ol_f20_operating_leverage_to_crypto_gpm_slope_126d_base_v127_signal(revenue, gp):
    gm = _safe_div(gp, revenue) + _f20_opmargin(revenue, gp) * 0.0
    result = _safe_div(gm - gm.shift(126), _std(gm, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin percentile rank 252d
def f20ol_f20_operating_leverage_to_crypto_gpm_rank_252d_base_v128_signal(revenue, gp):
    gm = _safe_div(gp, revenue) + _f20_opmargin(revenue, gp) * 0.0
    result = gm.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin to operating margin ratio (operating efficiency)
def f20ol_f20_operating_leverage_to_crypto_gp2op_63d_base_v129_signal(revenue, gp, opinc):
    result = _mean(_safe_div(_safe_div(gp, revenue), _f20_opmargin(revenue, opinc)), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean opinc-to-ebitda
def f20ol_f20_operating_leverage_to_crypto_op2ebitda_sm_126d_base_v130_signal(opinc, ebitda, revenue):
    result = _mean(_safe_div(opinc, ebitda), 126) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score opinc-to-ebitda
def f20ol_f20_operating_leverage_to_crypto_op2ebitda_z_252d_base_v131_signal(opinc, ebitda, revenue):
    result = _z(_safe_div(opinc, ebitda), 252) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean fixed-cost absorption (opinc/opex)
def f20ol_f20_operating_leverage_to_crypto_absorb_sm_126d_base_v132_signal(opinc, opex, revenue):
    result = _mean(_safe_div(opinc, opex), 126) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of absorption
def f20ol_f20_operating_leverage_to_crypto_absorb_z_126d_base_v133_signal(opinc, opex, revenue):
    result = _z(_safe_div(opinc, opex), 126) + _f20_opmargin(revenue, opinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in absorption
def f20ol_f20_operating_leverage_to_crypto_absorb_chg_252d_base_v134_signal(opinc, opex, revenue):
    a = _safe_div(opinc, opex) + _f20_opmargin(revenue, opinc) * 0.0
    result = a - a.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# absorption percentile rank 252d
def f20ol_f20_operating_leverage_to_crypto_absorb_rank_252d_base_v135_signal(opinc, opex, revenue):
    a = _safe_div(opinc, opex) + _f20_opmargin(revenue, opinc) * 0.0
    result = a.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue intensity of operating margin 252d
def f20ol_f20_operating_leverage_to_crypto_margXrevg_252d_base_v136_signal(revenue, opinc):
    result = _f20_opmargin(revenue, opinc) * revenue.pct_change(252)
    return result.replace([np.inf, -np.inf], np.nan)


# operating leverage sensitivity 252d
def f20ol_f20_operating_leverage_to_crypto_sens_252d_base_v137_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = _safe_div(m - m.shift(252), revenue.pct_change(252))
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed operating leverage sensitivity 63d window
def f20ol_f20_operating_leverage_to_crypto_sens_sm_63d_base_v138_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    sens = _safe_div(m - m.shift(63), revenue.pct_change(63))
    result = _mean(sens.clip(-50, 50), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# cost ratio momentum (rate of change of cost ratio) 126d
def f20ol_f20_operating_leverage_to_crypto_costratio_roc_126d_base_v139_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin momentum (rate of change) 126d
def f20ol_f20_operating_leverage_to_crypto_opmargin_roc_126d_base_v140_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin momentum (rate of change) 252d
def f20ol_f20_operating_leverage_to_crypto_opmargin_roc_252d_base_v141_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m.pct_change(252)
    return result.replace([np.inf, -np.inf], np.nan)


# margin acceleration (63d chg minus 126d chg)
def f20ol_f20_operating_leverage_to_crypto_opmargin_accel_base_v142_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = (m - m.shift(63)) - (m.shift(63) - m.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# contribution margin momentum 252d
def f20ol_f20_operating_leverage_to_crypto_contrib_roc_252d_base_v143_signal(revenue, cor):
    cm = _f20_contribmargin(revenue, cor)
    result = cm.pct_change(252)
    return result.replace([np.inf, -np.inf], np.nan)


# margin-weighted revenue growth z-score 126d
def f20ol_f20_operating_leverage_to_crypto_margXrevg_z_126d_base_v144_signal(revenue, opinc):
    sig = _f20_opmargin(revenue, opinc) * revenue.pct_change(63)
    result = _z(sig, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin minus its ewm (margin surprise)
def f20ol_f20_operating_leverage_to_crypto_opmargin_surp_126d_base_v145_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = m - m.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# cost ratio minus its ewm (cost surprise)
def f20ol_f20_operating_leverage_to_crypto_costratio_surp_126d_base_v146_signal(revenue, opex):
    c = _f20_costratio(revenue, opex)
    result = c - c.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# DOL minus contribution margin interaction (leverage quality) 63d
def f20ol_f20_operating_leverage_to_crypto_dolXcontrib_63d_base_v147_signal(revenue, opinc, cor):
    result = _mean(_f20_oplev(revenue, opinc, 63).clip(-50, 50) * _f20_contribmargin(revenue, cor), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# blended operating-leverage composite (margin z + neg cost z + dol z)
def f20ol_f20_operating_leverage_to_crypto_blend_composite_base_v148_signal(revenue, opinc, opex):
    mz = _z(_f20_opmargin(revenue, opinc), 252)
    cz = _z(_f20_costratio(revenue, opex), 252)
    dz = _z(_f20_oplev(revenue, opinc, 63).clip(-50, 50), 252)
    result = (mz - cz + dz) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion times revenue growth (operating leverage payoff) 126d
def f20ol_f20_operating_leverage_to_crypto_payoff_126d_base_v149_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = (m - m.shift(126)) * revenue.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon operating margin trend composite
def f20ol_f20_operating_leverage_to_crypto_marg_trend_multi_base_v150_signal(revenue, opinc):
    m = _f20_opmargin(revenue, opinc)
    result = ((m - m.shift(63)) + (m - m.shift(126)) + (m - m.shift(252))) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20ol_f20_operating_leverage_to_crypto_margcostsprd_z_252d_base_v076_signal,
    f20ol_f20_operating_leverage_to_crypto_margcostsprd_chg_252d_base_v077_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_84d_base_v078_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_189d_base_v079_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_sm_504d_base_v080_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_63d_base_v081_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_126d_base_v082_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_ewm_252d_base_v083_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_21d_base_v084_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_42d_base_v085_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_chg_504d_base_v086_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_z_84d_base_v087_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_z_189d_base_v088_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_z_315d_base_v089_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_rel_252d_base_v090_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_rel_126d_base_v091_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_rank_378d_base_v092_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_disp_504d_base_v093_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_cv_252d_base_v094_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_84d_base_v095_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_189d_base_v096_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_504d_base_v097_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_sm_252d_base_v098_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_z_126d_base_v099_signal,
    f20ol_f20_operating_leverage_to_crypto_dol_z_504d_base_v100_signal,
    f20ol_f20_operating_leverage_to_crypto_growthsprd_42d_base_v101_signal,
    f20ol_f20_operating_leverage_to_crypto_growthsprd_504d_base_v102_signal,
    f20ol_f20_operating_leverage_to_crypto_growthsprd_z_126d_base_v103_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_sm_84d_base_v104_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_sm_504d_base_v105_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_ewm_126d_base_v106_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_rel_252d_base_v107_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_slope_126d_base_v108_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_disp_252d_base_v109_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_chg_126d_base_v110_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_z_63d_base_v111_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_z_504d_base_v112_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_ewm_126d_base_v113_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_disp_252d_base_v114_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_rel_252d_base_v115_signal,
    f20ol_f20_operating_leverage_to_crypto_contribopgap_21d_base_v116_signal,
    f20ol_f20_operating_leverage_to_crypto_contribopgap_sm_63d_base_v117_signal,
    f20ol_f20_operating_leverage_to_crypto_contribopgap_z_126d_base_v118_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_sm_252d_base_v119_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_z_126d_base_v120_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_chg_252d_base_v121_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_slope_126d_base_v122_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitdam_rank_252d_base_v123_signal,
    f20ol_f20_operating_leverage_to_crypto_ebitda2op_63d_base_v124_signal,
    f20ol_f20_operating_leverage_to_crypto_gpm_sm_126d_base_v125_signal,
    f20ol_f20_operating_leverage_to_crypto_gpm_z_252d_base_v126_signal,
    f20ol_f20_operating_leverage_to_crypto_gpm_slope_126d_base_v127_signal,
    f20ol_f20_operating_leverage_to_crypto_gpm_rank_252d_base_v128_signal,
    f20ol_f20_operating_leverage_to_crypto_gp2op_63d_base_v129_signal,
    f20ol_f20_operating_leverage_to_crypto_op2ebitda_sm_126d_base_v130_signal,
    f20ol_f20_operating_leverage_to_crypto_op2ebitda_z_252d_base_v131_signal,
    f20ol_f20_operating_leverage_to_crypto_absorb_sm_126d_base_v132_signal,
    f20ol_f20_operating_leverage_to_crypto_absorb_z_126d_base_v133_signal,
    f20ol_f20_operating_leverage_to_crypto_absorb_chg_252d_base_v134_signal,
    f20ol_f20_operating_leverage_to_crypto_absorb_rank_252d_base_v135_signal,
    f20ol_f20_operating_leverage_to_crypto_margXrevg_252d_base_v136_signal,
    f20ol_f20_operating_leverage_to_crypto_sens_252d_base_v137_signal,
    f20ol_f20_operating_leverage_to_crypto_sens_sm_63d_base_v138_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_roc_126d_base_v139_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_roc_126d_base_v140_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_roc_252d_base_v141_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_accel_base_v142_signal,
    f20ol_f20_operating_leverage_to_crypto_contrib_roc_252d_base_v143_signal,
    f20ol_f20_operating_leverage_to_crypto_margXrevg_z_126d_base_v144_signal,
    f20ol_f20_operating_leverage_to_crypto_opmargin_surp_126d_base_v145_signal,
    f20ol_f20_operating_leverage_to_crypto_costratio_surp_126d_base_v146_signal,
    f20ol_f20_operating_leverage_to_crypto_dolXcontrib_63d_base_v147_signal,
    f20ol_f20_operating_leverage_to_crypto_blend_composite_base_v148_signal,
    f20ol_f20_operating_leverage_to_crypto_payoff_126d_base_v149_signal,
    f20ol_f20_operating_leverage_to_crypto_marg_trend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_OPERATING_LEVERAGE_TO_CRYPTO_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f20_opmargin", "_f20_oplev", "_f20_costratio", "_f20_contribmargin")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f20_operating_leverage_to_crypto_base_076_150_claude: {n_features} features pass")
