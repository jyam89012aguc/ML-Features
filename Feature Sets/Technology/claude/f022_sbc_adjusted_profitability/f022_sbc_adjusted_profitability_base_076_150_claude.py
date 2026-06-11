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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f022_adj_opmargin(opinc, sbcomp, revenue):
    return (opinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)


def _f022_adj_fcf_margin(fcf, sbcomp, revenue):
    return (fcf - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)


# 63d z-score of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_z_63d_base_v076_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_z_126d_base_v077_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_z_252d_base_v078_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_z_504d_base_v079_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_z_63d_base_v080_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_z_126d_base_v081_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_z_252d_base_v082_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_z_504d_base_v083_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_z_63d_base_v084_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_z_126d_base_v085_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_z_252d_base_v086_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_z_504d_base_v087_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_z_63d_base_v088_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_z_126d_base_v089_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_z_252d_base_v090_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_z_504d_base_v091_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_z_63d_base_v092_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_z_126d_base_v093_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_z_252d_base_v094_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_z_504d_base_v095_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_z_63d_base_v096_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_z_126d_base_v097_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_z_252d_base_v098_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_z_504d_base_v099_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_z_63d_base_v100_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_z_126d_base_v101_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_z_252d_base_v102_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_z_504d_base_v103_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_distmax_252d_base_v104_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_distmax_504d_base_v105_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_distmax_252d_base_v106_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_distmax_504d_base_v107_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_distmax_252d_base_v108_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_distmax_504d_base_v109_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_distmax_252d_base_v110_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_distmax_504d_base_v111_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_distmax_252d_base_v112_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_distmax_504d_base_v113_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_distmax_252d_base_v114_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_distmax_504d_base_v115_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_distmax_252d_base_v116_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_distmax_504d_base_v117_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_distmed_126d_base_v118_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_distmed_252d_base_v119_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_distmed_504d_base_v120_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_distmed_126d_base_v121_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_distmed_252d_base_v122_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_distmed_504d_base_v123_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_distmed_126d_base_v124_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_distmed_252d_base_v125_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_distmed_504d_base_v126_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_distmed_126d_base_v127_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_distmed_252d_base_v128_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_distmed_504d_base_v129_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_distmed_126d_base_v130_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_distmed_252d_base_v131_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_distmed_504d_base_v132_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_distmed_126d_base_v133_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_distmed_252d_base_v134_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_distmed_504d_base_v135_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_distmed_126d_base_v136_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_distmed_252d_base_v137_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_distmed_504d_base_v138_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_chg_63d_base_v139_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_chg_252d_base_v140_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_chg_63d_base_v141_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_chg_252d_base_v142_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_chg_63d_base_v143_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_chg_252d_base_v144_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_chg_63d_base_v145_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_chg_252d_base_v146_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_chg_63d_base_v147_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_chg_252d_base_v148_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_chg_63d_base_v149_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_chg_252d_base_v150_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

