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


# ===== folder domain primitives =====
def _f29_gp_lift(gp, revenue, w):
    # Gross profit lift: ratio change of gp / revenue over window
    gpm = gp / revenue.replace(0, np.nan)
    return gpm.diff(periods=w)


def _f29_pricing_pass_through(grossmargin, cor, revenue, w):
    # Pricing pass-through: gross margin change vs cor/revenue change
    cor_share = cor / revenue.replace(0, np.nan)
    return grossmargin.diff(periods=w) / (cor_share.diff(periods=w).abs() + 1e-6)


def _f29_margin_recovery(grossmargin, w):
    # Margin recovery: gross margin minus its trailing trough
    trough = grossmargin.rolling(w, min_periods=max(1, w // 2)).min()
    return grossmargin - trough


def f29bmp_building_material_pricing_pricept_xpxchg_63_base_v076_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 63) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xlogrev_252_base_v077_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_diff63_base_v078_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 63).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_sign_base_v079_signal(grossmargin, cor, revenue, closeadj):
    result = (np.sign(_f29_pricing_pass_through(grossmargin, cor, revenue, 63)) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_zema252_base_v080_signal(grossmargin, cor, revenue, closeadj):
    result = (_z(_f29_pricing_pass_through(grossmargin, cor, revenue, 252), 504).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xlogcor_252_base_v081_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * np.log(cor.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xgrossmargin_base_v082_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * grossmargin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_5d_base_v083_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_10d_base_v084_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_21d_base_v085_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_42d_base_v086_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_63d_base_v087_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_126d_base_v088_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_189d_base_v089_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_252d_base_v090_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_378d_base_v091_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_504d_base_v092_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_ma21d_base_v093_signal(grossmargin, closeadj):
    result = (_mean(_f29_margin_recovery(grossmargin, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_ma63d_base_v094_signal(grossmargin, closeadj):
    result = (_mean(_f29_margin_recovery(grossmargin, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_ma252d_base_v095_signal(grossmargin, closeadj):
    result = (_mean(_f29_margin_recovery(grossmargin, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_std63d_base_v096_signal(grossmargin, closeadj):
    result = (_std(_f29_margin_recovery(grossmargin, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_std252d_base_v097_signal(grossmargin, closeadj):
    result = (_std(_f29_margin_recovery(grossmargin, 252), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_z63d_base_v098_signal(grossmargin, closeadj):
    result = (_z(_f29_margin_recovery(grossmargin, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_z252d_base_v099_signal(grossmargin, closeadj):
    result = (_z(_f29_margin_recovery(grossmargin, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_ema21d_base_v100_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 21).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_ema63d_base_v101_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 63).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_ema252d_base_v102_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252).ewm(span=252, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_rank252d_base_v103_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_rank504d_base_v104_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_sq_base_v105_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 63) * _f29_margin_recovery(grossmargin, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_dev252_base_v106_signal(grossmargin, closeadj):
    result = ((_f29_margin_recovery(grossmargin, 252) - _mean(_f29_margin_recovery(grossmargin, 252), 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_var252_base_v107_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_xlogpx_252_base_v108_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_xpxgap_252_base_v109_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_xpxdet_252_base_v110_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_xpkgap_252_base_v111_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_xrange_252_base_v112_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_xvolz_252_base_v113_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252) * _z(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_xpxchg_63_base_v114_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 63) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_diff63_base_v115_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 63).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_diff252_base_v116_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_sign_base_v117_signal(grossmargin, closeadj):
    result = (np.sign(_f29_margin_recovery(grossmargin, 63) - 0.01) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_logema_base_v118_signal(grossmargin, closeadj):
    result = (np.log(_f29_margin_recovery(grossmargin, 63).abs() + 1.0).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_x_pricept_63_base_v119_signal(gp, grossmargin, cor, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63) * _f29_pricing_pass_through(grossmargin, cor, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_x_pricept_252_base_v120_signal(gp, grossmargin, cor, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * _f29_pricing_pass_through(grossmargin, cor, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_x_mrec_252_base_v121_signal(gp, grossmargin, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * _f29_margin_recovery(grossmargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_x_mrec_252_base_v122_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * _f29_margin_recovery(grossmargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_plus_mrec_63_base_v123_signal(gp, grossmargin, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 63) + _f29_margin_recovery(grossmargin, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_minus_mrec_63_base_v124_signal(gp, grossmargin, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 63) - _f29_margin_recovery(grossmargin, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_compo_all_252_base_v125_signal(gp, grossmargin, cor, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 252) + _f29_pricing_pass_through(grossmargin, cor, revenue, 252) + _f29_margin_recovery(grossmargin, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_compow_all_252_base_v126_signal(gp, grossmargin, cor, revenue, closeadj):
    result = ((0.5 * _f29_gp_lift(gp, revenue, 252) + 0.3 * _f29_pricing_pass_through(grossmargin, cor, revenue, 252) + 0.2 * _f29_margin_recovery(grossmargin, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_compo_all_63_base_v127_signal(gp, grossmargin, cor, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 63) + _f29_pricing_pass_through(grossmargin, cor, revenue, 63) + _f29_margin_recovery(grossmargin, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_x_pricept_x_close_base_v128_signal(gp, grossmargin, cor, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63) * _f29_pricing_pass_through(grossmargin, cor, revenue, 63) * closeadj.pct_change(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_x_pricept_x_close_base_v129_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_margin_recovery(grossmargin, 63) * _f29_pricing_pass_through(grossmargin, cor, revenue, 63) * closeadj.pct_change(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_minus_pricept_252_base_v130_signal(gp, grossmargin, cor, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 252) - _f29_pricing_pass_through(grossmargin, cor, revenue, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_minus_pricept_63_base_v131_signal(grossmargin, cor, revenue, closeadj):
    result = ((_f29_margin_recovery(grossmargin, 63) - _f29_pricing_pass_through(grossmargin, cor, revenue, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_compo3w_63_base_v132_signal(gp, grossmargin, cor, revenue, closeadj):
    result = ((0.4 * _f29_gp_lift(gp, revenue, 63) + 0.3 * _f29_pricing_pass_through(grossmargin, cor, revenue, 63) + 0.3 * _f29_margin_recovery(grossmargin, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_x_corshare_252_base_v133_signal(gp, cor, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * (cor / revenue.replace(0, np.nan))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_x_corshare_252_base_v134_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252) * (cor / revenue.replace(0, np.nan))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_x_corshare_252_base_v135_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * (cor / revenue.replace(0, np.nan))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_x_gmdiff_252_base_v136_signal(gp, grossmargin, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * grossmargin.diff(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_x_gmdiff_252_base_v137_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 252) * grossmargin.diff(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_x_mrec_minus_pp_63_base_v138_signal(gp, grossmargin, cor, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 63) + _f29_margin_recovery(grossmargin, 63)) - _f29_pricing_pass_through(grossmargin, cor, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_compo_all_504_base_v139_signal(gp, grossmargin, cor, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 504) + _f29_pricing_pass_through(grossmargin, cor, revenue, 504) + _f29_margin_recovery(grossmargin, 504))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_5d_alt_base_v140_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_504d_alt_base_v141_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_5d_alt_base_v142_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_504d_alt_base_v143_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_5d_alt_base_v144_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_504d_alt_base_v145_signal(grossmargin, closeadj):
    result = (_f29_margin_recovery(grossmargin, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_emadiff_63_base_v146_signal(gp, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 63).ewm(span=21, adjust=False).mean() - _f29_gp_lift(gp, revenue, 63).ewm(span=63, adjust=False).mean())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_emadiff_63_base_v147_signal(grossmargin, cor, revenue, closeadj):
    result = ((_f29_pricing_pass_through(grossmargin, cor, revenue, 63).ewm(span=21, adjust=False).mean() - _f29_pricing_pass_through(grossmargin, cor, revenue, 63).ewm(span=63, adjust=False).mean())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_mrec_emadiff_63_base_v148_signal(grossmargin, closeadj):
    result = ((_f29_margin_recovery(grossmargin, 63).ewm(span=21, adjust=False).mean() - _f29_margin_recovery(grossmargin, 63).ewm(span=63, adjust=False).mean())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_compo_all_minus_504_base_v149_signal(gp, grossmargin, cor, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 504) + _f29_margin_recovery(grossmargin, 504) - _f29_pricing_pass_through(grossmargin, cor, revenue, 504))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_x_pricept_504_base_v150_signal(gp, grossmargin, cor, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 504) * _f29_pricing_pass_through(grossmargin, cor, revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29bmp_building_material_pricing_pricept_xpxchg_63_base_v076_signal,
    f29bmp_building_material_pricing_pricept_xlogrev_252_base_v077_signal,
    f29bmp_building_material_pricing_pricept_diff63_base_v078_signal,
    f29bmp_building_material_pricing_pricept_sign_base_v079_signal,
    f29bmp_building_material_pricing_pricept_zema252_base_v080_signal,
    f29bmp_building_material_pricing_pricept_xlogcor_252_base_v081_signal,
    f29bmp_building_material_pricing_pricept_xgrossmargin_base_v082_signal,
    f29bmp_building_material_pricing_mrec_5d_base_v083_signal,
    f29bmp_building_material_pricing_mrec_10d_base_v084_signal,
    f29bmp_building_material_pricing_mrec_21d_base_v085_signal,
    f29bmp_building_material_pricing_mrec_42d_base_v086_signal,
    f29bmp_building_material_pricing_mrec_63d_base_v087_signal,
    f29bmp_building_material_pricing_mrec_126d_base_v088_signal,
    f29bmp_building_material_pricing_mrec_189d_base_v089_signal,
    f29bmp_building_material_pricing_mrec_252d_base_v090_signal,
    f29bmp_building_material_pricing_mrec_378d_base_v091_signal,
    f29bmp_building_material_pricing_mrec_504d_base_v092_signal,
    f29bmp_building_material_pricing_mrec_ma21d_base_v093_signal,
    f29bmp_building_material_pricing_mrec_ma63d_base_v094_signal,
    f29bmp_building_material_pricing_mrec_ma252d_base_v095_signal,
    f29bmp_building_material_pricing_mrec_std63d_base_v096_signal,
    f29bmp_building_material_pricing_mrec_std252d_base_v097_signal,
    f29bmp_building_material_pricing_mrec_z63d_base_v098_signal,
    f29bmp_building_material_pricing_mrec_z252d_base_v099_signal,
    f29bmp_building_material_pricing_mrec_ema21d_base_v100_signal,
    f29bmp_building_material_pricing_mrec_ema63d_base_v101_signal,
    f29bmp_building_material_pricing_mrec_ema252d_base_v102_signal,
    f29bmp_building_material_pricing_mrec_rank252d_base_v103_signal,
    f29bmp_building_material_pricing_mrec_rank504d_base_v104_signal,
    f29bmp_building_material_pricing_mrec_sq_base_v105_signal,
    f29bmp_building_material_pricing_mrec_dev252_base_v106_signal,
    f29bmp_building_material_pricing_mrec_var252_base_v107_signal,
    f29bmp_building_material_pricing_mrec_xlogpx_252_base_v108_signal,
    f29bmp_building_material_pricing_mrec_xpxgap_252_base_v109_signal,
    f29bmp_building_material_pricing_mrec_xpxdet_252_base_v110_signal,
    f29bmp_building_material_pricing_mrec_xpkgap_252_base_v111_signal,
    f29bmp_building_material_pricing_mrec_xrange_252_base_v112_signal,
    f29bmp_building_material_pricing_mrec_xvolz_252_base_v113_signal,
    f29bmp_building_material_pricing_mrec_xpxchg_63_base_v114_signal,
    f29bmp_building_material_pricing_mrec_diff63_base_v115_signal,
    f29bmp_building_material_pricing_mrec_diff252_base_v116_signal,
    f29bmp_building_material_pricing_mrec_sign_base_v117_signal,
    f29bmp_building_material_pricing_mrec_logema_base_v118_signal,
    f29bmp_building_material_pricing_gplift_x_pricept_63_base_v119_signal,
    f29bmp_building_material_pricing_gplift_x_pricept_252_base_v120_signal,
    f29bmp_building_material_pricing_gplift_x_mrec_252_base_v121_signal,
    f29bmp_building_material_pricing_pricept_x_mrec_252_base_v122_signal,
    f29bmp_building_material_pricing_gplift_plus_mrec_63_base_v123_signal,
    f29bmp_building_material_pricing_gplift_minus_mrec_63_base_v124_signal,
    f29bmp_building_material_pricing_compo_all_252_base_v125_signal,
    f29bmp_building_material_pricing_compow_all_252_base_v126_signal,
    f29bmp_building_material_pricing_compo_all_63_base_v127_signal,
    f29bmp_building_material_pricing_gplift_x_pricept_x_close_base_v128_signal,
    f29bmp_building_material_pricing_mrec_x_pricept_x_close_base_v129_signal,
    f29bmp_building_material_pricing_gplift_minus_pricept_252_base_v130_signal,
    f29bmp_building_material_pricing_mrec_minus_pricept_63_base_v131_signal,
    f29bmp_building_material_pricing_compo3w_63_base_v132_signal,
    f29bmp_building_material_pricing_gplift_x_corshare_252_base_v133_signal,
    f29bmp_building_material_pricing_mrec_x_corshare_252_base_v134_signal,
    f29bmp_building_material_pricing_pricept_x_corshare_252_base_v135_signal,
    f29bmp_building_material_pricing_gplift_x_gmdiff_252_base_v136_signal,
    f29bmp_building_material_pricing_mrec_x_gmdiff_252_base_v137_signal,
    f29bmp_building_material_pricing_gplift_x_mrec_minus_pp_63_base_v138_signal,
    f29bmp_building_material_pricing_compo_all_504_base_v139_signal,
    f29bmp_building_material_pricing_gplift_5d_alt_base_v140_signal,
    f29bmp_building_material_pricing_gplift_504d_alt_base_v141_signal,
    f29bmp_building_material_pricing_pricept_5d_alt_base_v142_signal,
    f29bmp_building_material_pricing_pricept_504d_alt_base_v143_signal,
    f29bmp_building_material_pricing_mrec_5d_alt_base_v144_signal,
    f29bmp_building_material_pricing_mrec_504d_alt_base_v145_signal,
    f29bmp_building_material_pricing_gplift_emadiff_63_base_v146_signal,
    f29bmp_building_material_pricing_pricept_emadiff_63_base_v147_signal,
    f29bmp_building_material_pricing_mrec_emadiff_63_base_v148_signal,
    f29bmp_building_material_pricing_compo_all_minus_504_base_v149_signal,
    f29bmp_building_material_pricing_gplift_x_pricept_504_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_BUILDING_MATERIAL_PRICING_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    gp = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "gp": gp, "cor": cor, "grossmargin": grossmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f29_gp_lift", "_f29_pricing_pass_through", "_f29_margin_recovery")
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
    print(f"OK f29_building_material_pricing_base_076_150_claude: {n_features} features pass")
