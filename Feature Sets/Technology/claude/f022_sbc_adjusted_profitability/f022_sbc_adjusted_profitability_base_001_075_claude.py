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


# 21d mean of adj_opmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_mean_21d_base_v001_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of adj_opmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_mean_63d_base_v002_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of adj_opmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_mean_126d_base_v003_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of adj_opmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_mean_252d_base_v004_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of adj_opmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_mean_504d_base_v005_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of adj_fcf_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_mean_21d_base_v006_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of adj_fcf_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_mean_63d_base_v007_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of adj_fcf_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_mean_126d_base_v008_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of adj_fcf_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_mean_252d_base_v009_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of adj_fcf_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_mean_504d_base_v010_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of adj_netmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_mean_21d_base_v011_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of adj_netmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_mean_63d_base_v012_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of adj_netmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_mean_126d_base_v013_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of adj_netmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_mean_252d_base_v014_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of adj_netmargin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_mean_504d_base_v015_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of adj_ebit_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_mean_21d_base_v016_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of adj_ebit_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_mean_63d_base_v017_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of adj_ebit_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_mean_126d_base_v018_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of adj_ebit_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_mean_252d_base_v019_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of adj_ebit_margin scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_mean_504d_base_v020_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_drag_op scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_mean_21d_base_v021_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_drag_op scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_mean_63d_base_v022_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_drag_op scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_mean_126d_base_v023_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_drag_op scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_mean_252d_base_v024_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_drag_op scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_mean_504d_base_v025_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_drag_fcf scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_mean_21d_base_v026_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_drag_fcf scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_mean_63d_base_v027_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_drag_fcf scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_mean_126d_base_v028_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_drag_fcf scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_mean_252d_base_v029_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_drag_fcf scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_mean_504d_base_v030_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of op_to_adjop scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_mean_21d_base_v031_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of op_to_adjop scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_mean_63d_base_v032_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of op_to_adjop scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_mean_126d_base_v033_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of op_to_adjop scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_mean_252d_base_v034_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of op_to_adjop scaled by closeadj
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_mean_504d_base_v035_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_median_63d_base_v036_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_median_252d_base_v037_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_median_504d_base_v038_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_median_63d_base_v039_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_median_252d_base_v040_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_median_504d_base_v041_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_median_63d_base_v042_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_median_252d_base_v043_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_median_504d_base_v044_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_median_63d_base_v045_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_median_252d_base_v046_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_median_504d_base_v047_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_median_63d_base_v048_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_median_252d_base_v049_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_median_504d_base_v050_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_median_63d_base_v051_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_median_252d_base_v052_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_median_504d_base_v053_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_median_63d_base_v054_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_median_252d_base_v055_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_median_504d_base_v056_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_rmax_252d_base_v057_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_rmax_504d_base_v058_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_rmax_252d_base_v059_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_rmax_504d_base_v060_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_rmax_252d_base_v061_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_rmax_504d_base_v062_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_rmax_252d_base_v063_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of adj_ebit_margin
def f022sap_f022_sbc_adjusted_profitability_adj_ebit_margin_rmax_504d_base_v064_signal(ebit, sbcomp, revenue, closeadj):
    base = (ebit - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_rmax_252d_base_v065_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sbc_drag_op
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_op_rmax_504d_base_v066_signal(sbcomp, opinc, closeadj):
    base = sbcomp / opinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_rmax_252d_base_v067_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sbc_drag_fcf
def f022sap_f022_sbc_adjusted_profitability_sbc_drag_fcf_rmax_504d_base_v068_signal(sbcomp, fcf, closeadj):
    base = sbcomp / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_rmax_252d_base_v069_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of op_to_adjop
def f022sap_f022_sbc_adjusted_profitability_op_to_adjop_rmax_504d_base_v070_signal(opinc, sbcomp, closeadj):
    base = opinc / (opinc - sbcomp.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_rmin_252d_base_v071_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of adj_opmargin
def f022sap_f022_sbc_adjusted_profitability_adj_opmargin_rmin_504d_base_v072_signal(opinc, sbcomp, revenue, closeadj):
    base = _f022_adj_opmargin(opinc, sbcomp, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_rmin_252d_base_v073_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of adj_fcf_margin
def f022sap_f022_sbc_adjusted_profitability_adj_fcf_margin_rmin_504d_base_v074_signal(fcf, sbcomp, revenue, closeadj):
    base = _f022_adj_fcf_margin(fcf, sbcomp, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of adj_netmargin
def f022sap_f022_sbc_adjusted_profitability_adj_netmargin_rmin_252d_base_v075_signal(netinc, sbcomp, revenue, closeadj):
    base = (netinc - sbcomp.fillna(0)) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

