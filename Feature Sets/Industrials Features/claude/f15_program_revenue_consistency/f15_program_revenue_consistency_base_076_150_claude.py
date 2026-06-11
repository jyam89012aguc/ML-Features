import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (f15 program_revenue_consistency) =====
def _f15_revenue_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan).abs()


def _f15_program_smoothness(revenue, w):
    diff = revenue.diff().abs()
    return diff.rolling(w, min_periods=max(1, w // 2)).mean() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan).abs()


def _f15_revenue_predictability(revenue, w):
    rg = revenue.pct_change(periods=max(1, w // 4))
    sd = rg.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (1.0 + sd.replace(0, np.nan))


def prc_f15_program_revenue_consistency_revcv_21d_dshift_v076_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 21)
    result = (base - base.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_absprod_v077_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 21)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_stdw_v078_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_meanw_v079_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 63)
    result = _mean(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_xvol_v080_signal(closeadj, revenue, volume):
    base = _f15_program_smoothness(revenue, 63)
    result = base * _mean(volume, 15) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_xdv_v081_signal(closeadj, revenue, volume):
    base = _f15_revenue_predictability(revenue, 63)
    result = base * _mean(closeadj * volume, 15) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_xebitda_v082_signal(closeadj, ebitda, revenue):
    base = _f15_revenue_cv(revenue, 126)
    result = base * closeadj * _mean(ebitda, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_xnetinc_v083_signal(closeadj, netinc, revenue):
    base = _f15_program_smoothness(revenue, 126)
    result = base * closeadj * _mean(netinc, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_xcapex_v084_signal(capex, closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 126)
    result = base * closeadj * _mean(capex, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_xdrev_v085_signal(closeadj, deferredrev, revenue):
    base = _f15_revenue_cv(revenue, 252)
    result = base * closeadj * _mean(deferredrev, 126) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_xnm_v086_signal(closeadj, netmargin, revenue):
    base = _f15_program_smoothness(revenue, 252)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_252d_xebm_v087_signal(closeadj, ebitdamargin, revenue):
    base = _f15_revenue_predictability(revenue, 252)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_504d_logc_v088_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 504)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_504d_sqrtc_v089_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 504)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_504d_dshift_v090_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 504)
    result = (base - base.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_absprod_v091_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 21)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_stdw_v092_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_meanw_v093_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_xvol_v094_signal(closeadj, revenue, volume):
    base = _f15_revenue_cv(revenue, 63)
    result = base * _mean(volume, 15) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_xdv_v095_signal(closeadj, revenue, volume):
    base = _f15_program_smoothness(revenue, 63)
    result = base * _mean(closeadj * volume, 15) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_xebitda_v096_signal(closeadj, ebitda, revenue):
    base = _f15_revenue_predictability(revenue, 63)
    result = base * closeadj * _mean(ebitda, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_xnetinc_v097_signal(closeadj, netinc, revenue):
    base = _f15_revenue_cv(revenue, 126)
    result = base * closeadj * _mean(netinc, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_xcapex_v098_signal(capex, closeadj, revenue):
    base = _f15_program_smoothness(revenue, 126)
    result = base * closeadj * _mean(capex, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_xdrev_v099_signal(closeadj, deferredrev, revenue):
    base = _f15_revenue_predictability(revenue, 126)
    result = base * closeadj * _mean(deferredrev, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_xnm_v100_signal(closeadj, netmargin, revenue):
    base = _f15_revenue_cv(revenue, 252)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_xebm_v101_signal(closeadj, ebitdamargin, revenue):
    base = _f15_program_smoothness(revenue, 252)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_252d_logc_v102_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_504d_sqrtc_v103_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 504)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_504d_dshift_v104_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 504)
    result = (base - base.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_504d_absprod_v105_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 504)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_stdw_v106_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_meanw_v107_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_xvol_v108_signal(closeadj, revenue, volume):
    base = _f15_revenue_predictability(revenue, 21)
    result = base * _mean(volume, 5) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_xdv_v109_signal(closeadj, revenue, volume):
    base = _f15_revenue_cv(revenue, 63)
    result = base * _mean(closeadj * volume, 15) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_xebitda_v110_signal(closeadj, ebitda, revenue):
    base = _f15_program_smoothness(revenue, 63)
    result = base * closeadj * _mean(ebitda, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_xnetinc_v111_signal(closeadj, netinc, revenue):
    base = _f15_revenue_predictability(revenue, 63)
    result = base * closeadj * _mean(netinc, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_xcapex_v112_signal(capex, closeadj, revenue):
    base = _f15_revenue_cv(revenue, 126)
    result = base * closeadj * _mean(capex, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_xdrev_v113_signal(closeadj, deferredrev, revenue):
    base = _f15_program_smoothness(revenue, 126)
    result = base * closeadj * _mean(deferredrev, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_xnm_v114_signal(closeadj, netmargin, revenue):
    base = _f15_revenue_predictability(revenue, 126)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_xebm_v115_signal(closeadj, ebitdamargin, revenue):
    base = _f15_revenue_cv(revenue, 252)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_logc_v116_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_252d_sqrtc_v117_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 252)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_504d_dshift_v118_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 504)
    result = (base - base.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_504d_absprod_v119_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 504)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_504d_stdw_v120_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 504)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_meanw_v121_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_xvol_v122_signal(closeadj, revenue, volume):
    base = _f15_program_smoothness(revenue, 21)
    result = base * _mean(volume, 5) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_xdv_v123_signal(closeadj, revenue, volume):
    base = _f15_revenue_predictability(revenue, 21)
    result = base * _mean(closeadj * volume, 5) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_xebitda_v124_signal(closeadj, ebitda, revenue):
    base = _f15_revenue_cv(revenue, 63)
    result = base * closeadj * _mean(ebitda, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_xnetinc_v125_signal(closeadj, netinc, revenue):
    base = _f15_program_smoothness(revenue, 63)
    result = base * closeadj * _mean(netinc, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_xcapex_v126_signal(capex, closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 63)
    result = base * closeadj * _mean(capex, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_xdrev_v127_signal(closeadj, deferredrev, revenue):
    base = _f15_revenue_cv(revenue, 126)
    result = base * closeadj * _mean(deferredrev, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_xnm_v128_signal(closeadj, netmargin, revenue):
    base = _f15_program_smoothness(revenue, 126)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_xebm_v129_signal(closeadj, ebitdamargin, revenue):
    base = _f15_revenue_predictability(revenue, 126)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_logc_v130_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_sqrtc_v131_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 252)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_252d_dshift_v132_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_504d_absprod_v133_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 504)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_504d_stdw_v134_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 504)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_504d_meanw_v135_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_xvol_v136_signal(closeadj, revenue, volume):
    base = _f15_revenue_cv(revenue, 21)
    result = base * _mean(volume, 5) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_xdv_v137_signal(closeadj, revenue, volume):
    base = _f15_program_smoothness(revenue, 21)
    result = base * _mean(closeadj * volume, 5) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_xebitda_v138_signal(closeadj, ebitda, revenue):
    base = _f15_revenue_predictability(revenue, 21)
    result = base * closeadj * _mean(ebitda, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_xnetinc_v139_signal(closeadj, netinc, revenue):
    base = _f15_revenue_cv(revenue, 63)
    result = base * closeadj * _mean(netinc, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_xcapex_v140_signal(capex, closeadj, revenue):
    base = _f15_program_smoothness(revenue, 63)
    result = base * closeadj * _mean(capex, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_xdrev_v141_signal(closeadj, deferredrev, revenue):
    base = _f15_revenue_predictability(revenue, 63)
    result = base * closeadj * _mean(deferredrev, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_xnm_v142_signal(closeadj, netmargin, revenue):
    base = _f15_revenue_cv(revenue, 126)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_xebm_v143_signal(closeadj, ebitdamargin, revenue):
    base = _f15_program_smoothness(revenue, 126)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_logc_v144_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 126)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_sqrtc_v145_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 252)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_dshift_v146_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_252d_absprod_v147_signal(closeadj, revenue):
    base = _f15_revenue_predictability(revenue, 252)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_504d_stdw_v148_signal(closeadj, revenue):
    base = _f15_revenue_cv(revenue, 504)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_504d_meanw_v149_signal(closeadj, revenue):
    base = _f15_program_smoothness(revenue, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_504d_xvol_v150_signal(closeadj, revenue, volume):
    base = _f15_revenue_predictability(revenue, 504)
    result = base * _mean(volume, 126) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    prc_f15_program_revenue_consistency_revcv_21d_dshift_v076_signal,
    prc_f15_program_revenue_consistency_smooth_21d_absprod_v077_signal,
    prc_f15_program_revenue_consistency_revpred_21d_stdw_v078_signal,
    prc_f15_program_revenue_consistency_revcv_63d_meanw_v079_signal,
    prc_f15_program_revenue_consistency_smooth_63d_xvol_v080_signal,
    prc_f15_program_revenue_consistency_revpred_63d_xdv_v081_signal,
    prc_f15_program_revenue_consistency_revcv_126d_xebitda_v082_signal,
    prc_f15_program_revenue_consistency_smooth_126d_xnetinc_v083_signal,
    prc_f15_program_revenue_consistency_revpred_126d_xcapex_v084_signal,
    prc_f15_program_revenue_consistency_revcv_252d_xdrev_v085_signal,
    prc_f15_program_revenue_consistency_smooth_252d_xnm_v086_signal,
    prc_f15_program_revenue_consistency_revpred_252d_xebm_v087_signal,
    prc_f15_program_revenue_consistency_revcv_504d_logc_v088_signal,
    prc_f15_program_revenue_consistency_smooth_504d_sqrtc_v089_signal,
    prc_f15_program_revenue_consistency_revpred_504d_dshift_v090_signal,
    prc_f15_program_revenue_consistency_revcv_21d_absprod_v091_signal,
    prc_f15_program_revenue_consistency_smooth_21d_stdw_v092_signal,
    prc_f15_program_revenue_consistency_revpred_21d_meanw_v093_signal,
    prc_f15_program_revenue_consistency_revcv_63d_xvol_v094_signal,
    prc_f15_program_revenue_consistency_smooth_63d_xdv_v095_signal,
    prc_f15_program_revenue_consistency_revpred_63d_xebitda_v096_signal,
    prc_f15_program_revenue_consistency_revcv_126d_xnetinc_v097_signal,
    prc_f15_program_revenue_consistency_smooth_126d_xcapex_v098_signal,
    prc_f15_program_revenue_consistency_revpred_126d_xdrev_v099_signal,
    prc_f15_program_revenue_consistency_revcv_252d_xnm_v100_signal,
    prc_f15_program_revenue_consistency_smooth_252d_xebm_v101_signal,
    prc_f15_program_revenue_consistency_revpred_252d_logc_v102_signal,
    prc_f15_program_revenue_consistency_revcv_504d_sqrtc_v103_signal,
    prc_f15_program_revenue_consistency_smooth_504d_dshift_v104_signal,
    prc_f15_program_revenue_consistency_revpred_504d_absprod_v105_signal,
    prc_f15_program_revenue_consistency_revcv_21d_stdw_v106_signal,
    prc_f15_program_revenue_consistency_smooth_21d_meanw_v107_signal,
    prc_f15_program_revenue_consistency_revpred_21d_xvol_v108_signal,
    prc_f15_program_revenue_consistency_revcv_63d_xdv_v109_signal,
    prc_f15_program_revenue_consistency_smooth_63d_xebitda_v110_signal,
    prc_f15_program_revenue_consistency_revpred_63d_xnetinc_v111_signal,
    prc_f15_program_revenue_consistency_revcv_126d_xcapex_v112_signal,
    prc_f15_program_revenue_consistency_smooth_126d_xdrev_v113_signal,
    prc_f15_program_revenue_consistency_revpred_126d_xnm_v114_signal,
    prc_f15_program_revenue_consistency_revcv_252d_xebm_v115_signal,
    prc_f15_program_revenue_consistency_smooth_252d_logc_v116_signal,
    prc_f15_program_revenue_consistency_revpred_252d_sqrtc_v117_signal,
    prc_f15_program_revenue_consistency_revcv_504d_dshift_v118_signal,
    prc_f15_program_revenue_consistency_smooth_504d_absprod_v119_signal,
    prc_f15_program_revenue_consistency_revpred_504d_stdw_v120_signal,
    prc_f15_program_revenue_consistency_revcv_21d_meanw_v121_signal,
    prc_f15_program_revenue_consistency_smooth_21d_xvol_v122_signal,
    prc_f15_program_revenue_consistency_revpred_21d_xdv_v123_signal,
    prc_f15_program_revenue_consistency_revcv_63d_xebitda_v124_signal,
    prc_f15_program_revenue_consistency_smooth_63d_xnetinc_v125_signal,
    prc_f15_program_revenue_consistency_revpred_63d_xcapex_v126_signal,
    prc_f15_program_revenue_consistency_revcv_126d_xdrev_v127_signal,
    prc_f15_program_revenue_consistency_smooth_126d_xnm_v128_signal,
    prc_f15_program_revenue_consistency_revpred_126d_xebm_v129_signal,
    prc_f15_program_revenue_consistency_revcv_252d_logc_v130_signal,
    prc_f15_program_revenue_consistency_smooth_252d_sqrtc_v131_signal,
    prc_f15_program_revenue_consistency_revpred_252d_dshift_v132_signal,
    prc_f15_program_revenue_consistency_revcv_504d_absprod_v133_signal,
    prc_f15_program_revenue_consistency_smooth_504d_stdw_v134_signal,
    prc_f15_program_revenue_consistency_revpred_504d_meanw_v135_signal,
    prc_f15_program_revenue_consistency_revcv_21d_xvol_v136_signal,
    prc_f15_program_revenue_consistency_smooth_21d_xdv_v137_signal,
    prc_f15_program_revenue_consistency_revpred_21d_xebitda_v138_signal,
    prc_f15_program_revenue_consistency_revcv_63d_xnetinc_v139_signal,
    prc_f15_program_revenue_consistency_smooth_63d_xcapex_v140_signal,
    prc_f15_program_revenue_consistency_revpred_63d_xdrev_v141_signal,
    prc_f15_program_revenue_consistency_revcv_126d_xnm_v142_signal,
    prc_f15_program_revenue_consistency_smooth_126d_xebm_v143_signal,
    prc_f15_program_revenue_consistency_revpred_126d_logc_v144_signal,
    prc_f15_program_revenue_consistency_revcv_252d_sqrtc_v145_signal,
    prc_f15_program_revenue_consistency_smooth_252d_dshift_v146_signal,
    prc_f15_program_revenue_consistency_revpred_252d_absprod_v147_signal,
    prc_f15_program_revenue_consistency_revcv_504d_stdw_v148_signal,
    prc_f15_program_revenue_consistency_smooth_504d_meanw_v149_signal,
    prc_f15_program_revenue_consistency_revpred_504d_xvol_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_PROGRAM_REVENUE_CONSISTENCY_REGISTRY_076_150 = REGISTRY
F15_PROGRAM_REVENUE_CONSISTENCY_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f15_revenue_cv", "_f15_program_smoothness", "_f15_revenue_predictability",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f15_program_revenue_consistency_base_076_150_claude: {n_features} features pass")
