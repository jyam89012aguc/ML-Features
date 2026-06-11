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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f40_cor_to_revenue(cor, revenue):
    # Cost of revenue as fraction of revenue (input intensity)
    return cor / revenue.replace(0, np.nan)


def _f40_margin_input_sensitivity(grossmargin, cor, w):
    # Change in margin per change in cor (negative-correlation proxy)
    gm_chg = grossmargin.diff(w)
    cor_chg = cor.pct_change(w)
    return gm_chg / cor_chg.replace(0, np.nan).abs()


def _f40_pass_through_score(grossmargin, cor, revenue, w):
    # Pass-through: positive if revenue rises with cor while margin holds
    rev_g = revenue.pct_change(w)
    cor_g = cor.pct_change(w)
    gm_chg = grossmargin.diff(w)
    return (rev_g - cor_g) + gm_chg


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_5d_base_v076_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 5) * cor.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_10d_base_v077_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 10) * cor.pct_change(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_21d_base_v078_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 21) * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_42d_base_v079_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 42) * cor.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_63d_base_v080_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 63) * cor.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_126d_base_v081_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 126) * cor.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_189d_base_v082_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 189) * cor.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_252d_base_v083_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 252) * cor.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_378d_base_v084_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 378) * cor.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_504d_base_v085_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 504) * cor.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_5d_base_v086_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 5)
    result = d * cor.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_10d_base_v087_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 10)
    result = d * cor.pct_change(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_21d_base_v088_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 21)
    result = d * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_42d_base_v089_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 42)
    result = d * cor.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_63d_base_v090_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d * cor.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_126d_base_v091_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 126)
    result = d * cor.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_189d_base_v092_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 189)
    result = d * cor.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_252d_base_v093_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = d * cor.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_378d_base_v094_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 378)
    result = d * cor.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_504d_base_v095_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 504)
    result = d * cor.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_5d_base_v096_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 5)
    result = d * cor.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_10d_base_v097_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 10)
    result = d * cor.pct_change(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_21d_base_v098_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 21)
    result = d * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_42d_base_v099_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 42)
    result = d * cor.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_63d_base_v100_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d * cor.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_126d_base_v101_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 126)
    result = d * cor.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_189d_base_v102_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 189)
    result = d * cor.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_252d_base_v103_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = d * cor.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_378d_base_v104_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 378)
    result = d * cor.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_504d_base_v105_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 504)
    result = d * cor.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_21d_base_v106_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 21) * revenue.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_42d_base_v107_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 42) * revenue.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_63d_base_v108_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 63) * revenue.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_126d_base_v109_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 126) * revenue.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_189d_base_v110_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 189) * revenue.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_252d_base_v111_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 252) * revenue.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_504d_base_v112_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 504) * revenue.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_21d_base_v113_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 21)
    result = d * revenue.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_42d_base_v114_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 42)
    result = d * revenue.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_63d_base_v115_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d * revenue.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_126d_base_v116_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 126)
    result = d * revenue.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_189d_base_v117_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 189)
    result = d * revenue.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_252d_base_v118_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = d * revenue.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_504d_base_v119_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 504)
    result = d * revenue.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrusq_21d_base_v120_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 21)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrusq_42d_base_v121_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 42)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrusq_63d_base_v122_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrusq_126d_base_v123_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 126)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrusq_189d_base_v124_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 189)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrusq_252d_base_v125_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrusq_504d_base_v126_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 504)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvdev_21d_base_v127_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = (d - _mean(d, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvdev_42d_base_v128_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = (d - _mean(d, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvdev_63d_base_v129_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = (d - _mean(d, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvdev_126d_base_v130_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = (d - _mean(d, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvdev_189d_base_v131_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = (d - _mean(d, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvdev_252d_base_v132_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = (d - _mean(d, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvdev_504d_base_v133_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = (d - _mean(d, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_21d_base_v134_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_42d_base_v135_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_63d_base_v136_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_126d_base_v137_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_189d_base_v138_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_252d_base_v139_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_378d_base_v140_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrudif_21d_base_v141_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrudif_42d_base_v142_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrudif_63d_base_v143_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrudif_126d_base_v144_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrudif_189d_base_v145_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrudif_252d_base_v146_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrudif_378d_base_v147_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgmd_252d_base_v148_signal(cor, revenue, grossmargin, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 252) * grossmargin.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxgmd_252d_base_v149_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d * grossmargin.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxgmd_252d_base_v150_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d * grossmargin.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_5d_base_v076_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_10d_base_v077_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_21d_base_v078_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_42d_base_v079_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_63d_base_v080_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_126d_base_v081_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_189d_base_v082_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_252d_base_v083_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_378d_base_v084_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxcorg_504d_base_v085_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_5d_base_v086_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_10d_base_v087_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_21d_base_v088_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_42d_base_v089_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_63d_base_v090_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_126d_base_v091_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_189d_base_v092_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_252d_base_v093_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_378d_base_v094_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxcorg_504d_base_v095_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_5d_base_v096_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_10d_base_v097_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_21d_base_v098_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_42d_base_v099_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_63d_base_v100_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_126d_base_v101_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_189d_base_v102_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_252d_base_v103_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_378d_base_v104_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxcorg_504d_base_v105_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_21d_base_v106_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_42d_base_v107_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_63d_base_v108_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_126d_base_v109_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_189d_base_v110_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_252d_base_v111_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxrevg_504d_base_v112_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_21d_base_v113_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_42d_base_v114_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_63d_base_v115_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_126d_base_v116_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_189d_base_v117_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_252d_base_v118_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxrevg_504d_base_v119_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrusq_21d_base_v120_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrusq_42d_base_v121_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrusq_63d_base_v122_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrusq_126d_base_v123_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrusq_189d_base_v124_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrusq_252d_base_v125_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrusq_504d_base_v126_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvdev_21d_base_v127_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvdev_42d_base_v128_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvdev_63d_base_v129_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvdev_126d_base_v130_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvdev_189d_base_v131_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvdev_252d_base_v132_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvdev_504d_base_v133_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_21d_base_v134_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_42d_base_v135_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_63d_base_v136_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_126d_base_v137_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_189d_base_v138_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_252d_base_v139_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensdiff_378d_base_v140_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrudif_21d_base_v141_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrudif_42d_base_v142_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrudif_63d_base_v143_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrudif_126d_base_v144_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrudif_189d_base_v145_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrudif_252d_base_v146_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrudif_378d_base_v147_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgmd_252d_base_v148_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxgmd_252d_base_v149_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxgmd_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_TEXTILE_INPUT_COST_SENSITIVITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f40_cor_to_revenue", "_f40_margin_input_sensitivity", "_f40_pass_through_score",)
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
    print(f"OK f40_textile_input_cost_sensitivity_076_150_claude: {n_features} features pass")
