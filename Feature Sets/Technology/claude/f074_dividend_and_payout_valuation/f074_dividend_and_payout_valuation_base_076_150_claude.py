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
def _f074_divyield(dps, close):
    return dps / close.replace(0, np.nan).abs()


# 63d z-score of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_z_63d_base_v076_signal(dps, closeadj):
    base = dps
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_z_126d_base_v077_signal(dps, closeadj):
    base = dps
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_z_252d_base_v078_signal(dps, closeadj):
    base = dps
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_z_504d_base_v079_signal(dps, closeadj):
    base = dps
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_z_63d_base_v080_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_z_126d_base_v081_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_z_252d_base_v082_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_z_504d_base_v083_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_z_63d_base_v084_signal(divyield, closeadj):
    base = divyield
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_z_126d_base_v085_signal(divyield, closeadj):
    base = divyield
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_z_252d_base_v086_signal(divyield, closeadj):
    base = divyield
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_z_504d_base_v087_signal(divyield, closeadj):
    base = divyield
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_z_63d_base_v088_signal(payoutratio, closeadj):
    base = payoutratio
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_z_126d_base_v089_signal(payoutratio, closeadj):
    base = payoutratio
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_z_252d_base_v090_signal(payoutratio, closeadj):
    base = payoutratio
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_z_504d_base_v091_signal(payoutratio, closeadj):
    base = payoutratio
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_z_63d_base_v092_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_z_126d_base_v093_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_z_252d_base_v094_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_z_504d_base_v095_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_z_63d_base_v096_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_z_126d_base_v097_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_z_252d_base_v098_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_z_504d_base_v099_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_z_63d_base_v100_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_z_126d_base_v101_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_z_252d_base_v102_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_z_504d_base_v103_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_distmax_252d_base_v104_signal(dps, closeadj):
    base = dps
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_distmax_504d_base_v105_signal(dps, closeadj):
    base = dps
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_distmax_252d_base_v106_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_distmax_504d_base_v107_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_distmax_252d_base_v108_signal(divyield, closeadj):
    base = divyield
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_distmax_504d_base_v109_signal(divyield, closeadj):
    base = divyield
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_distmax_252d_base_v110_signal(payoutratio, closeadj):
    base = payoutratio
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_distmax_504d_base_v111_signal(payoutratio, closeadj):
    base = payoutratio
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_distmax_252d_base_v112_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_distmax_504d_base_v113_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_distmax_252d_base_v114_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_distmax_504d_base_v115_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_distmax_252d_base_v116_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_distmax_504d_base_v117_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_distmed_126d_base_v118_signal(dps, closeadj):
    base = dps
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_distmed_252d_base_v119_signal(dps, closeadj):
    base = dps
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_distmed_504d_base_v120_signal(dps, closeadj):
    base = dps
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_distmed_126d_base_v121_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_distmed_252d_base_v122_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_distmed_504d_base_v123_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_distmed_126d_base_v124_signal(divyield, closeadj):
    base = divyield
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_distmed_252d_base_v125_signal(divyield, closeadj):
    base = divyield
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_distmed_504d_base_v126_signal(divyield, closeadj):
    base = divyield
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_distmed_126d_base_v127_signal(payoutratio, closeadj):
    base = payoutratio
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_distmed_252d_base_v128_signal(payoutratio, closeadj):
    base = payoutratio
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_distmed_504d_base_v129_signal(payoutratio, closeadj):
    base = payoutratio
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_distmed_126d_base_v130_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_distmed_252d_base_v131_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_distmed_504d_base_v132_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_distmed_126d_base_v133_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_distmed_252d_base_v134_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_distmed_504d_base_v135_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_distmed_126d_base_v136_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_distmed_252d_base_v137_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_distmed_504d_base_v138_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_chg_63d_base_v139_signal(dps, closeadj):
    base = dps
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_chg_252d_base_v140_signal(dps, closeadj):
    base = dps
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_chg_63d_base_v141_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_chg_252d_base_v142_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_chg_63d_base_v143_signal(divyield, closeadj):
    base = divyield
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_chg_252d_base_v144_signal(divyield, closeadj):
    base = divyield
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_chg_63d_base_v145_signal(payoutratio, closeadj):
    base = payoutratio
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_chg_252d_base_v146_signal(payoutratio, closeadj):
    base = payoutratio
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_chg_63d_base_v147_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_chg_252d_base_v148_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_chg_63d_base_v149_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_chg_252d_base_v150_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

