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
def _f074_divyield(dps, close):
    return dps / close.replace(0, np.nan).abs()


# 21d acceleration of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_accel_21d_3d_v001_signal(dps, closeadj):
    base = dps
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_accel_63d_3d_v002_signal(dps, closeadj):
    base = dps
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_accel_126d_3d_v003_signal(dps, closeadj):
    base = dps
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_accel_252d_3d_v004_signal(dps, closeadj):
    base = dps
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_accel_21d_3d_v005_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_accel_63d_3d_v006_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_accel_126d_3d_v007_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_accel_252d_3d_v008_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_accel_21d_3d_v009_signal(divyield, closeadj):
    base = divyield
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_accel_63d_3d_v010_signal(divyield, closeadj):
    base = divyield
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_accel_126d_3d_v011_signal(divyield, closeadj):
    base = divyield
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_accel_252d_3d_v012_signal(divyield, closeadj):
    base = divyield
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_accel_21d_3d_v013_signal(payoutratio, closeadj):
    base = payoutratio
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_accel_63d_3d_v014_signal(payoutratio, closeadj):
    base = payoutratio
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_accel_126d_3d_v015_signal(payoutratio, closeadj):
    base = payoutratio
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_accel_252d_3d_v016_signal(payoutratio, closeadj):
    base = payoutratio
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_accel_21d_3d_v017_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_accel_63d_3d_v018_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_accel_126d_3d_v019_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_accel_252d_3d_v020_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_accel_21d_3d_v021_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_accel_63d_3d_v022_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_accel_126d_3d_v023_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_accel_252d_3d_v024_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_accel_21d_3d_v025_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_accel_63d_3d_v026_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_accel_126d_3d_v027_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_accel_252d_3d_v028_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_slopez_21d_z126_3d_v029_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_slopez_63d_z252_3d_v030_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_slopez_126d_z252_3d_v031_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_slopez_252d_z504_3d_v032_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_slopez_21d_z126_3d_v033_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_slopez_63d_z252_3d_v034_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_slopez_126d_z252_3d_v035_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_slopez_252d_z504_3d_v036_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_slopez_21d_z126_3d_v037_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_slopez_63d_z252_3d_v038_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_slopez_126d_z252_3d_v039_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_slopez_252d_z504_3d_v040_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_slopez_21d_z126_3d_v041_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_slopez_63d_z252_3d_v042_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_slopez_126d_z252_3d_v043_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_slopez_252d_z504_3d_v044_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_slopez_21d_z126_3d_v045_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_slopez_63d_z252_3d_v046_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_slopez_126d_z252_3d_v047_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_slopez_252d_z504_3d_v048_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_slopez_21d_z126_3d_v049_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_slopez_63d_z252_3d_v050_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_slopez_126d_z252_3d_v051_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_slopez_252d_z504_3d_v052_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_slopez_21d_z126_3d_v053_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_slopez_63d_z252_3d_v054_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_slopez_126d_z252_3d_v055_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_slopez_252d_z504_3d_v056_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_jerk_21d_3d_v057_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_jerk_63d_3d_v058_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_jerk_126d_3d_v059_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_jerk_21d_3d_v060_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_jerk_63d_3d_v061_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_jerk_126d_3d_v062_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_jerk_21d_3d_v063_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_jerk_63d_3d_v064_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_jerk_126d_3d_v065_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_jerk_21d_3d_v066_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_jerk_63d_3d_v067_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_jerk_126d_3d_v068_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_jerk_21d_3d_v069_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_jerk_63d_3d_v070_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_jerk_126d_3d_v071_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_jerk_21d_3d_v072_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_jerk_63d_3d_v073_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_jerk_126d_3d_v074_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_jerk_21d_3d_v075_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_jerk_63d_3d_v076_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_jerk_126d_3d_v077_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dps_lvl smoothed over 252d
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_smoothaccel_63d_sm252_3d_v078_signal(dps, closeadj):
    base = dps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dps_lvl smoothed over 504d
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_smoothaccel_252d_sm504_3d_v079_signal(dps, closeadj):
    base = dps
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of divyield_calc smoothed over 252d
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_smoothaccel_63d_sm252_3d_v080_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of divyield_calc smoothed over 504d
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_smoothaccel_252d_sm504_3d_v081_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of divyieldforward_lvl smoothed over 252d
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_smoothaccel_63d_sm252_3d_v082_signal(divyield, closeadj):
    base = divyield
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of divyieldforward_lvl smoothed over 504d
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_smoothaccel_252d_sm504_3d_v083_signal(divyield, closeadj):
    base = divyield
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of payoutratio_lvl smoothed over 252d
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_smoothaccel_63d_sm252_3d_v084_signal(payoutratio, closeadj):
    base = payoutratio
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of payoutratio_lvl smoothed over 504d
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_smoothaccel_252d_sm504_3d_v085_signal(payoutratio, closeadj):
    base = payoutratio
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dps_yoy smoothed over 252d
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_smoothaccel_63d_sm252_3d_v086_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dps_yoy smoothed over 504d
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_smoothaccel_252d_sm504_3d_v087_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of div_payment_to_ni smoothed over 252d
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_smoothaccel_63d_sm252_3d_v088_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of div_payment_to_ni smoothed over 504d
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_smoothaccel_252d_sm504_3d_v089_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ncfdiv_to_fcf smoothed over 252d
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_smoothaccel_63d_sm252_3d_v090_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ncfdiv_to_fcf smoothed over 504d
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_smoothaccel_252d_sm504_3d_v091_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_accelz_21d_z252_3d_v092_signal(dps, closeadj):
    base = dps
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_accelz_63d_z504_3d_v093_signal(dps, closeadj):
    base = dps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_accelz_21d_z252_3d_v094_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_accelz_63d_z504_3d_v095_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_accelz_21d_z252_3d_v096_signal(divyield, closeadj):
    base = divyield
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_accelz_63d_z504_3d_v097_signal(divyield, closeadj):
    base = divyield
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_accelz_21d_z252_3d_v098_signal(payoutratio, closeadj):
    base = payoutratio
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_accelz_63d_z504_3d_v099_signal(payoutratio, closeadj):
    base = payoutratio
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_accelz_21d_z252_3d_v100_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_accelz_63d_z504_3d_v101_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_accelz_21d_z252_3d_v102_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_accelz_63d_z504_3d_v103_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_accelz_21d_z252_3d_v104_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_accelz_63d_z504_3d_v105_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dps_lvl (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_signflip_63d_3d_v106_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dps_lvl (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_signflip_252d_3d_v107_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in divyield_calc (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_signflip_63d_3d_v108_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in divyield_calc (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_signflip_252d_3d_v109_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in divyieldforward_lvl (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_signflip_63d_3d_v110_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in divyieldforward_lvl (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_signflip_252d_3d_v111_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in payoutratio_lvl (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_signflip_63d_3d_v112_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in payoutratio_lvl (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_signflip_252d_3d_v113_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dps_yoy (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_signflip_63d_3d_v114_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dps_yoy (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_signflip_252d_3d_v115_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in div_payment_to_ni (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_signflip_63d_3d_v116_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in div_payment_to_ni (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_signflip_252d_3d_v117_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ncfdiv_to_fcf (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_signflip_63d_3d_v118_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ncfdiv_to_fcf (raw count, no price scaling)
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_signflip_252d_3d_v119_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dps_lvl normalized by 252d range
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_rngaccel_63d_r252_3d_v120_signal(dps, closeadj):
    base = dps
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dps_lvl normalized by 504d range
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_rngaccel_252d_r504_3d_v121_signal(dps, closeadj):
    base = dps
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of divyield_calc normalized by 252d range
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_rngaccel_63d_r252_3d_v122_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of divyield_calc normalized by 504d range
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_rngaccel_252d_r504_3d_v123_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of divyieldforward_lvl normalized by 252d range
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_rngaccel_63d_r252_3d_v124_signal(divyield, closeadj):
    base = divyield
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of divyieldforward_lvl normalized by 504d range
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_rngaccel_252d_r504_3d_v125_signal(divyield, closeadj):
    base = divyield
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of payoutratio_lvl normalized by 252d range
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_rngaccel_63d_r252_3d_v126_signal(payoutratio, closeadj):
    base = payoutratio
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of payoutratio_lvl normalized by 504d range
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_rngaccel_252d_r504_3d_v127_signal(payoutratio, closeadj):
    base = payoutratio
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dps_yoy normalized by 252d range
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_rngaccel_63d_r252_3d_v128_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dps_yoy normalized by 504d range
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_rngaccel_252d_r504_3d_v129_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of div_payment_to_ni normalized by 252d range
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_rngaccel_63d_r252_3d_v130_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of div_payment_to_ni normalized by 504d range
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_rngaccel_252d_r504_3d_v131_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfdiv_to_fcf normalized by 252d range
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_rngaccel_63d_r252_3d_v132_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfdiv_to_fcf normalized by 504d range
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_rngaccel_252d_r504_3d_v133_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_cumslope_21d_3d_v134_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_cumslope_63d_3d_v135_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_cumslope_252d_3d_v136_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_cumslope_21d_3d_v137_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_cumslope_63d_3d_v138_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_cumslope_252d_3d_v139_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_cumslope_21d_3d_v140_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_cumslope_63d_3d_v141_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_cumslope_252d_3d_v142_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_cumslope_21d_3d_v143_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_cumslope_63d_3d_v144_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_cumslope_252d_3d_v145_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_cumslope_21d_3d_v146_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_cumslope_63d_3d_v147_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_cumslope_252d_3d_v148_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_cumslope_21d_3d_v149_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_cumslope_63d_3d_v150_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

