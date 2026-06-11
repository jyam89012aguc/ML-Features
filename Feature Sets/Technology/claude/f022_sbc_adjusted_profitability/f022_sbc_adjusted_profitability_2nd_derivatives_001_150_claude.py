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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f022_adj_opmargin(opinc, sbcomp, revenue):
    return (opinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)


def _f022_adj_fcf_margin(fcf, sbcomp, revenue):
    return (fcf - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)


# 21d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_slope_21d_2d_v001_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_slope_63d_2d_v002_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_slope_126d_2d_v003_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_slope_252d_2d_v004_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_slope_504d_2d_v005_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_slope_21d_2d_v006_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_slope_63d_2d_v007_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_slope_126d_2d_v008_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_slope_252d_2d_v009_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_slope_504d_2d_v010_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_slope_21d_2d_v011_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_slope_63d_2d_v012_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_slope_126d_2d_v013_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_slope_252d_2d_v014_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_slope_504d_2d_v015_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_slope_21d_2d_v016_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_slope_63d_2d_v017_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_slope_126d_2d_v018_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_slope_252d_2d_v019_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_slope_504d_2d_v020_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_slope_21d_2d_v021_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_slope_63d_2d_v022_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_slope_126d_2d_v023_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_slope_252d_2d_v024_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_slope_504d_2d_v025_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_slope_21d_2d_v026_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_slope_63d_2d_v027_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_slope_126d_2d_v028_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_slope_252d_2d_v029_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_slope_504d_2d_v030_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_slope_21d_2d_v031_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_slope_63d_2d_v032_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_slope_126d_2d_v033_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_slope_252d_2d_v034_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_slope_504d_2d_v035_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_sm21_sl21_2d_v036_signal(opinc, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_opmargin(opinc, sbcomp, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_sm63_sl21_2d_v037_signal(opinc, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_opmargin(opinc, sbcomp, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_sm63_sl63_2d_v038_signal(opinc, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_opmargin(opinc, sbcomp, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_sm252_sl63_2d_v039_signal(opinc, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_opmargin(opinc, sbcomp, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_sm252_sl126_2d_v040_signal(opinc, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_opmargin(opinc, sbcomp, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_sm21_sl21_2d_v041_signal(fcf, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_fcf_margin(fcf, sbcomp, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_sm63_sl21_2d_v042_signal(fcf, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_fcf_margin(fcf, sbcomp, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_sm63_sl63_2d_v043_signal(fcf, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_fcf_margin(fcf, sbcomp, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_sm252_sl63_2d_v044_signal(fcf, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_fcf_margin(fcf, sbcomp, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_sm252_sl126_2d_v045_signal(fcf, sbcomp, revenue, closeadj):
    base = _mean(_f022_adj_fcf_margin(fcf, sbcomp, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_sm21_sl21_2d_v046_signal(netinc, sbcomp, revenue, closeadj):
    base = _mean((netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_sm63_sl21_2d_v047_signal(netinc, sbcomp, revenue, closeadj):
    base = _mean((netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_sm63_sl63_2d_v048_signal(netinc, sbcomp, revenue, closeadj):
    base = _mean((netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_sm252_sl63_2d_v049_signal(netinc, sbcomp, revenue, closeadj):
    base = _mean((netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_sm252_sl126_2d_v050_signal(netinc, sbcomp, revenue, closeadj):
    base = _mean((netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_sm21_sl21_2d_v051_signal(ebit, sbcomp, revenue, closeadj):
    base = _mean((ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_sm63_sl21_2d_v052_signal(ebit, sbcomp, revenue, closeadj):
    base = _mean((ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_sm63_sl63_2d_v053_signal(ebit, sbcomp, revenue, closeadj):
    base = _mean((ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_sm252_sl63_2d_v054_signal(ebit, sbcomp, revenue, closeadj):
    base = _mean((ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_sm252_sl126_2d_v055_signal(ebit, sbcomp, revenue, closeadj):
    base = _mean((ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_sm21_sl21_2d_v056_signal(sbcomp, opinc, closeadj):
    base = _mean(sbcomp / opinc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_sm63_sl21_2d_v057_signal(sbcomp, opinc, closeadj):
    base = _mean(sbcomp / opinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_sm63_sl63_2d_v058_signal(sbcomp, opinc, closeadj):
    base = _mean(sbcomp / opinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_sm252_sl63_2d_v059_signal(sbcomp, opinc, closeadj):
    base = _mean(sbcomp / opinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_sm252_sl126_2d_v060_signal(sbcomp, opinc, closeadj):
    base = _mean(sbcomp / opinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_sm21_sl21_2d_v061_signal(sbcomp, fcf, closeadj):
    base = _mean(sbcomp / fcf.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_sm63_sl21_2d_v062_signal(sbcomp, fcf, closeadj):
    base = _mean(sbcomp / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_sm63_sl63_2d_v063_signal(sbcomp, fcf, closeadj):
    base = _mean(sbcomp / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_sm252_sl63_2d_v064_signal(sbcomp, fcf, closeadj):
    base = _mean(sbcomp / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_sm252_sl126_2d_v065_signal(sbcomp, fcf, closeadj):
    base = _mean(sbcomp / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_sm21_sl21_2d_v066_signal(opinc, sbcomp, closeadj):
    base = _mean(opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_sm63_sl21_2d_v067_signal(opinc, sbcomp, closeadj):
    base = _mean(opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_sm63_sl63_2d_v068_signal(opinc, sbcomp, closeadj):
    base = _mean(opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_sm252_sl63_2d_v069_signal(opinc, sbcomp, closeadj):
    base = _mean(opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_sm252_sl126_2d_v070_signal(opinc, sbcomp, closeadj):
    base = _mean(opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_pctslope_21d_2d_v071_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_pctslope_63d_2d_v072_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_pctslope_252d_2d_v073_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_pctslope_21d_2d_v074_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_pctslope_63d_2d_v075_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_pctslope_252d_2d_v076_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_pctslope_21d_2d_v077_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_pctslope_63d_2d_v078_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_pctslope_252d_2d_v079_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_pctslope_21d_2d_v080_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_pctslope_63d_2d_v081_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_pctslope_252d_2d_v082_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_pctslope_21d_2d_v083_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_pctslope_63d_2d_v084_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_pctslope_252d_2d_v085_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_pctslope_21d_2d_v086_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_pctslope_63d_2d_v087_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_pctslope_252d_2d_v088_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_pctslope_21d_2d_v089_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_pctslope_63d_2d_v090_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_pctslope_252d_2d_v091_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_sgnslope_21d_2d_v092_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_sgnslope_63d_2d_v093_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_sgnslope_252d_2d_v094_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_sgnslope_21d_2d_v095_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_sgnslope_63d_2d_v096_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_sgnslope_252d_2d_v097_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_sgnslope_21d_2d_v098_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_sgnslope_63d_2d_v099_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_sgnslope_252d_2d_v100_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_sgnslope_21d_2d_v101_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_sgnslope_63d_2d_v102_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_sgnslope_252d_2d_v103_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_sgnslope_21d_2d_v104_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_sgnslope_63d_2d_v105_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_sgnslope_252d_2d_v106_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_sgnslope_21d_2d_v107_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_sgnslope_63d_2d_v108_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_sgnslope_252d_2d_v109_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_sgnslope_21d_2d_v110_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_sgnslope_63d_2d_v111_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_sgnslope_252d_2d_v112_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_logmagslope_21d_2d_v113_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_logmagslope_63d_2d_v114_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_logmagslope_252d_2d_v115_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_logmagslope_21d_2d_v116_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_logmagslope_63d_2d_v117_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_logmagslope_252d_2d_v118_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_logmagslope_21d_2d_v119_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_logmagslope_63d_2d_v120_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_logmagslope_252d_2d_v121_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_logmagslope_21d_2d_v122_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_logmagslope_63d_2d_v123_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_logmagslope_252d_2d_v124_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_logmagslope_21d_2d_v125_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_logmagslope_63d_2d_v126_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_logmagslope_252d_2d_v127_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_logmagslope_21d_2d_v128_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_logmagslope_63d_2d_v129_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_logmagslope_252d_2d_v130_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_logmagslope_21d_2d_v131_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_logmagslope_63d_2d_v132_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_logmagslope_252d_2d_v133_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|adj_opmargin|
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_logslope_63d_2d_v134_signal(opinc, sbcomp, revenue, closeadj):
    base = np.log((_f022_adj_opmargin(opinc, sbcomp, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|adj_opmargin|
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_logslope_252d_2d_v135_signal(opinc, sbcomp, revenue, closeadj):
    base = np.log((_f022_adj_opmargin(opinc, sbcomp, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|adj_fcf_margin|
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_logslope_63d_2d_v136_signal(fcf, sbcomp, revenue, closeadj):
    base = np.log((_f022_adj_fcf_margin(fcf, sbcomp, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|adj_fcf_margin|
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_logslope_252d_2d_v137_signal(fcf, sbcomp, revenue, closeadj):
    base = np.log((_f022_adj_fcf_margin(fcf, sbcomp, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|adj_netmargin|
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_logslope_63d_2d_v138_signal(netinc, sbcomp, revenue, closeadj):
    base = np.log(((netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|adj_netmargin|
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_logslope_252d_2d_v139_signal(netinc, sbcomp, revenue, closeadj):
    base = np.log(((netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|adj_ebit_margin|
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_logslope_63d_2d_v140_signal(ebit, sbcomp, revenue, closeadj):
    base = np.log(((ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|adj_ebit_margin|
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_logslope_252d_2d_v141_signal(ebit, sbcomp, revenue, closeadj):
    base = np.log(((ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_drag_op|
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_logslope_63d_2d_v142_signal(sbcomp, opinc, closeadj):
    base = np.log((sbcomp / opinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_drag_op|
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_logslope_252d_2d_v143_signal(sbcomp, opinc, closeadj):
    base = np.log((sbcomp / opinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_drag_fcf|
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_logslope_63d_2d_v144_signal(sbcomp, fcf, closeadj):
    base = np.log((sbcomp / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_drag_fcf|
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_logslope_252d_2d_v145_signal(sbcomp, fcf, closeadj):
    base = np.log((sbcomp / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|op_to_adjop|
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_logslope_63d_2d_v146_signal(opinc, sbcomp, closeadj):
    base = np.log((opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|op_to_adjop|
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_logslope_252d_2d_v147_signal(opinc, sbcomp, closeadj):
    base = np.log((opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

