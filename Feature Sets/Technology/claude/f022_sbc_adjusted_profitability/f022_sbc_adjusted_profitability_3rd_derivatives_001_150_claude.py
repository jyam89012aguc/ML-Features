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


# 21d acceleration of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_accel_21d_3d_v001_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_accel_63d_3d_v002_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_accel_126d_3d_v003_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_accel_252d_3d_v004_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_accel_21d_3d_v005_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_accel_63d_3d_v006_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_accel_126d_3d_v007_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_accel_252d_3d_v008_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_accel_21d_3d_v009_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_accel_63d_3d_v010_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_accel_126d_3d_v011_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_accel_252d_3d_v012_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_accel_21d_3d_v013_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_accel_63d_3d_v014_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_accel_126d_3d_v015_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_accel_252d_3d_v016_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_accel_21d_3d_v017_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_accel_63d_3d_v018_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_accel_126d_3d_v019_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_accel_252d_3d_v020_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_accel_21d_3d_v021_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_accel_63d_3d_v022_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_accel_126d_3d_v023_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_accel_252d_3d_v024_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_accel_21d_3d_v025_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_accel_63d_3d_v026_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_accel_126d_3d_v027_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_accel_252d_3d_v028_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_slopez_21d_z126_3d_v029_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_slopez_63d_z252_3d_v030_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_slopez_126d_z252_3d_v031_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_slopez_252d_z504_3d_v032_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_slopez_21d_z126_3d_v033_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_slopez_63d_z252_3d_v034_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_slopez_126d_z252_3d_v035_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_slopez_252d_z504_3d_v036_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_slopez_21d_z126_3d_v037_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_slopez_63d_z252_3d_v038_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_slopez_126d_z252_3d_v039_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_slopez_252d_z504_3d_v040_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_slopez_21d_z126_3d_v041_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_slopez_63d_z252_3d_v042_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_slopez_126d_z252_3d_v043_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_slopez_252d_z504_3d_v044_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_slopez_21d_z126_3d_v045_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_slopez_63d_z252_3d_v046_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_slopez_126d_z252_3d_v047_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_slopez_252d_z504_3d_v048_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_slopez_21d_z126_3d_v049_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_slopez_63d_z252_3d_v050_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_slopez_126d_z252_3d_v051_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_slopez_252d_z504_3d_v052_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_slopez_21d_z126_3d_v053_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_slopez_63d_z252_3d_v054_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_slopez_126d_z252_3d_v055_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_slopez_252d_z504_3d_v056_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_jerk_21d_3d_v057_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_jerk_63d_3d_v058_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_jerk_126d_3d_v059_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_jerk_21d_3d_v060_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_jerk_63d_3d_v061_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_jerk_126d_3d_v062_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_jerk_21d_3d_v063_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_jerk_63d_3d_v064_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_jerk_126d_3d_v065_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_jerk_21d_3d_v066_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_jerk_63d_3d_v067_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_jerk_126d_3d_v068_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_jerk_21d_3d_v069_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_jerk_63d_3d_v070_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_jerk_126d_3d_v071_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_jerk_21d_3d_v072_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_jerk_63d_3d_v073_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_jerk_126d_3d_v074_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_jerk_21d_3d_v075_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_jerk_63d_3d_v076_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_jerk_126d_3d_v077_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of adj_opmargin smoothed over 252d
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_smoothaccel_63d_sm252_3d_v078_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of adj_opmargin smoothed over 504d
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_smoothaccel_252d_sm504_3d_v079_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of adj_fcf_margin smoothed over 252d
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_smoothaccel_63d_sm252_3d_v080_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of adj_fcf_margin smoothed over 504d
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_smoothaccel_252d_sm504_3d_v081_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of adj_netmargin smoothed over 252d
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_smoothaccel_63d_sm252_3d_v082_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of adj_netmargin smoothed over 504d
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_smoothaccel_252d_sm504_3d_v083_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of adj_ebit_margin smoothed over 252d
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_smoothaccel_63d_sm252_3d_v084_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of adj_ebit_margin smoothed over 504d
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_smoothaccel_252d_sm504_3d_v085_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_drag_op smoothed over 252d
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_smoothaccel_63d_sm252_3d_v086_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_drag_op smoothed over 504d
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_smoothaccel_252d_sm504_3d_v087_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_drag_fcf smoothed over 252d
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_smoothaccel_63d_sm252_3d_v088_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_drag_fcf smoothed over 504d
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_smoothaccel_252d_sm504_3d_v089_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of op_to_adjop smoothed over 252d
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_smoothaccel_63d_sm252_3d_v090_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of op_to_adjop smoothed over 504d
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_smoothaccel_252d_sm504_3d_v091_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_accelz_21d_z252_3d_v092_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_accelz_63d_z504_3d_v093_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_accelz_21d_z252_3d_v094_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_accelz_63d_z504_3d_v095_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_accelz_21d_z252_3d_v096_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_accelz_63d_z504_3d_v097_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_accelz_21d_z252_3d_v098_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_accelz_63d_z504_3d_v099_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_accelz_21d_z252_3d_v100_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_accelz_63d_z504_3d_v101_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_accelz_21d_z252_3d_v102_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_accelz_63d_z504_3d_v103_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_accelz_21d_z252_3d_v104_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_accelz_63d_z504_3d_v105_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in adj_opmargin (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_signflip_63d_3d_v106_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in adj_opmargin (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_signflip_252d_3d_v107_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in adj_fcf_margin (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_signflip_63d_3d_v108_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in adj_fcf_margin (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_signflip_252d_3d_v109_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in adj_netmargin (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_signflip_63d_3d_v110_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in adj_netmargin (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_signflip_252d_3d_v111_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in adj_ebit_margin (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_signflip_63d_3d_v112_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in adj_ebit_margin (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_signflip_252d_3d_v113_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_drag_op (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_signflip_63d_3d_v114_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_drag_op (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_signflip_252d_3d_v115_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_drag_fcf (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_signflip_63d_3d_v116_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_drag_fcf (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_signflip_252d_3d_v117_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in op_to_adjop (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_signflip_63d_3d_v118_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in op_to_adjop (raw count, no price scaling)
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_signflip_252d_3d_v119_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_opmargin normalized by 252d range
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_rngaccel_63d_r252_3d_v120_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_opmargin normalized by 504d range
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_rngaccel_252d_r504_3d_v121_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_fcf_margin normalized by 252d range
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_rngaccel_63d_r252_3d_v122_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_fcf_margin normalized by 504d range
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_rngaccel_252d_r504_3d_v123_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_netmargin normalized by 252d range
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_rngaccel_63d_r252_3d_v124_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_netmargin normalized by 504d range
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_rngaccel_252d_r504_3d_v125_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_ebit_margin normalized by 252d range
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_rngaccel_63d_r252_3d_v126_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_ebit_margin normalized by 504d range
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_rngaccel_252d_r504_3d_v127_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_drag_op normalized by 252d range
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_rngaccel_63d_r252_3d_v128_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_drag_op normalized by 504d range
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_rngaccel_252d_r504_3d_v129_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_drag_fcf normalized by 252d range
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_rngaccel_63d_r252_3d_v130_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_drag_fcf normalized by 504d range
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_rngaccel_252d_r504_3d_v131_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of op_to_adjop normalized by 252d range
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_rngaccel_63d_r252_3d_v132_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of op_to_adjop normalized by 504d range
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_rngaccel_252d_r504_3d_v133_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_cumslope_21d_3d_v134_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_cumslope_63d_3d_v135_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_cumslope_252d_3d_v136_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_cumslope_21d_3d_v137_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_cumslope_63d_3d_v138_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_cumslope_252d_3d_v139_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_cumslope_21d_3d_v140_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_cumslope_63d_3d_v141_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_cumslope_252d_3d_v142_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_cumslope_21d_3d_v143_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_cumslope_63d_3d_v144_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_cumslope_252d_3d_v145_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_cumslope_21d_3d_v146_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_cumslope_63d_3d_v147_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_cumslope_252d_3d_v148_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_cumslope_21d_3d_v149_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_cumslope_63d_3d_v150_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

