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


# 21d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_slope_21d_2d_v001_signal(dps, closeadj):
    base = dps
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_slope_63d_2d_v002_signal(dps, closeadj):
    base = dps
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_slope_126d_2d_v003_signal(dps, closeadj):
    base = dps
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_slope_252d_2d_v004_signal(dps, closeadj):
    base = dps
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_slope_504d_2d_v005_signal(dps, closeadj):
    base = dps
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_slope_21d_2d_v006_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_slope_63d_2d_v007_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_slope_126d_2d_v008_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_slope_252d_2d_v009_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_slope_504d_2d_v010_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_slope_21d_2d_v011_signal(divyield, closeadj):
    base = divyield
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_slope_63d_2d_v012_signal(divyield, closeadj):
    base = divyield
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_slope_126d_2d_v013_signal(divyield, closeadj):
    base = divyield
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_slope_252d_2d_v014_signal(divyield, closeadj):
    base = divyield
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_slope_504d_2d_v015_signal(divyield, closeadj):
    base = divyield
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_slope_21d_2d_v016_signal(payoutratio, closeadj):
    base = payoutratio
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_slope_63d_2d_v017_signal(payoutratio, closeadj):
    base = payoutratio
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_slope_126d_2d_v018_signal(payoutratio, closeadj):
    base = payoutratio
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_slope_252d_2d_v019_signal(payoutratio, closeadj):
    base = payoutratio
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_slope_504d_2d_v020_signal(payoutratio, closeadj):
    base = payoutratio
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_slope_21d_2d_v021_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_slope_63d_2d_v022_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_slope_126d_2d_v023_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_slope_252d_2d_v024_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_slope_504d_2d_v025_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_slope_21d_2d_v026_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_slope_63d_2d_v027_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_slope_126d_2d_v028_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_slope_252d_2d_v029_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_slope_504d_2d_v030_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_slope_21d_2d_v031_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_slope_63d_2d_v032_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_slope_126d_2d_v033_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_slope_252d_2d_v034_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_slope_504d_2d_v035_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_sm21_sl21_2d_v036_signal(dps, closeadj):
    base = _mean(dps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_sm63_sl21_2d_v037_signal(dps, closeadj):
    base = _mean(dps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_sm63_sl63_2d_v038_signal(dps, closeadj):
    base = _mean(dps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_sm252_sl63_2d_v039_signal(dps, closeadj):
    base = _mean(dps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_sm252_sl126_2d_v040_signal(dps, closeadj):
    base = _mean(dps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_sm21_sl21_2d_v041_signal(dps, close, closeadj):
    base = _mean(_f074_divyield(dps, close), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_sm63_sl21_2d_v042_signal(dps, close, closeadj):
    base = _mean(_f074_divyield(dps, close), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_sm63_sl63_2d_v043_signal(dps, close, closeadj):
    base = _mean(_f074_divyield(dps, close), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_sm252_sl63_2d_v044_signal(dps, close, closeadj):
    base = _mean(_f074_divyield(dps, close), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_sm252_sl126_2d_v045_signal(dps, close, closeadj):
    base = _mean(_f074_divyield(dps, close), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_sm21_sl21_2d_v046_signal(divyield, closeadj):
    base = _mean(divyield, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_sm63_sl21_2d_v047_signal(divyield, closeadj):
    base = _mean(divyield, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_sm63_sl63_2d_v048_signal(divyield, closeadj):
    base = _mean(divyield, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_sm252_sl63_2d_v049_signal(divyield, closeadj):
    base = _mean(divyield, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_sm252_sl126_2d_v050_signal(divyield, closeadj):
    base = _mean(divyield, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_sm21_sl21_2d_v051_signal(payoutratio, closeadj):
    base = _mean(payoutratio, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_sm63_sl21_2d_v052_signal(payoutratio, closeadj):
    base = _mean(payoutratio, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_sm63_sl63_2d_v053_signal(payoutratio, closeadj):
    base = _mean(payoutratio, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_sm252_sl63_2d_v054_signal(payoutratio, closeadj):
    base = _mean(payoutratio, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_sm252_sl126_2d_v055_signal(payoutratio, closeadj):
    base = _mean(payoutratio, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_sm21_sl21_2d_v056_signal(dps, closeadj):
    base = _mean(dps.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_sm63_sl21_2d_v057_signal(dps, closeadj):
    base = _mean(dps.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_sm63_sl63_2d_v058_signal(dps, closeadj):
    base = _mean(dps.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_sm252_sl63_2d_v059_signal(dps, closeadj):
    base = _mean(dps.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_sm252_sl126_2d_v060_signal(dps, closeadj):
    base = _mean(dps.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_sm21_sl21_2d_v061_signal(ncfdiv, netinc, closeadj):
    base = _mean(ncfdiv / netinc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_sm63_sl21_2d_v062_signal(ncfdiv, netinc, closeadj):
    base = _mean(ncfdiv / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_sm63_sl63_2d_v063_signal(ncfdiv, netinc, closeadj):
    base = _mean(ncfdiv / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_sm252_sl63_2d_v064_signal(ncfdiv, netinc, closeadj):
    base = _mean(ncfdiv / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_sm252_sl126_2d_v065_signal(ncfdiv, netinc, closeadj):
    base = _mean(ncfdiv / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_sm21_sl21_2d_v066_signal(ncfdiv, fcf, closeadj):
    base = _mean(ncfdiv / fcf.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_sm63_sl21_2d_v067_signal(ncfdiv, fcf, closeadj):
    base = _mean(ncfdiv / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_sm63_sl63_2d_v068_signal(ncfdiv, fcf, closeadj):
    base = _mean(ncfdiv / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_sm252_sl63_2d_v069_signal(ncfdiv, fcf, closeadj):
    base = _mean(ncfdiv / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_sm252_sl126_2d_v070_signal(ncfdiv, fcf, closeadj):
    base = _mean(ncfdiv / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_pctslope_21d_2d_v071_signal(dps, closeadj):
    base = dps
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_pctslope_63d_2d_v072_signal(dps, closeadj):
    base = dps
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_pctslope_252d_2d_v073_signal(dps, closeadj):
    base = dps
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_pctslope_21d_2d_v074_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_pctslope_63d_2d_v075_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_pctslope_252d_2d_v076_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_pctslope_21d_2d_v077_signal(divyield, closeadj):
    base = divyield
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_pctslope_63d_2d_v078_signal(divyield, closeadj):
    base = divyield
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_pctslope_252d_2d_v079_signal(divyield, closeadj):
    base = divyield
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_pctslope_21d_2d_v080_signal(payoutratio, closeadj):
    base = payoutratio
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_pctslope_63d_2d_v081_signal(payoutratio, closeadj):
    base = payoutratio
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_pctslope_252d_2d_v082_signal(payoutratio, closeadj):
    base = payoutratio
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_pctslope_21d_2d_v083_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_pctslope_63d_2d_v084_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_pctslope_252d_2d_v085_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_pctslope_21d_2d_v086_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_pctslope_63d_2d_v087_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_pctslope_252d_2d_v088_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_pctslope_21d_2d_v089_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_pctslope_63d_2d_v090_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_pctslope_252d_2d_v091_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_sgnslope_21d_2d_v092_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_sgnslope_63d_2d_v093_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_sgnslope_252d_2d_v094_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_sgnslope_21d_2d_v095_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_sgnslope_63d_2d_v096_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_sgnslope_252d_2d_v097_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_sgnslope_21d_2d_v098_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_sgnslope_63d_2d_v099_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_sgnslope_252d_2d_v100_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_sgnslope_21d_2d_v101_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_sgnslope_63d_2d_v102_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_sgnslope_252d_2d_v103_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_sgnslope_21d_2d_v104_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_sgnslope_63d_2d_v105_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_sgnslope_252d_2d_v106_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_sgnslope_21d_2d_v107_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_sgnslope_63d_2d_v108_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_sgnslope_252d_2d_v109_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_sgnslope_21d_2d_v110_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_sgnslope_63d_2d_v111_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_sgnslope_252d_2d_v112_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_logmagslope_21d_2d_v113_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_logmagslope_63d_2d_v114_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_logmagslope_252d_2d_v115_signal(dps, closeadj):
    base = dps
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_logmagslope_21d_2d_v116_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_logmagslope_63d_2d_v117_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_logmagslope_252d_2d_v118_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_logmagslope_21d_2d_v119_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_logmagslope_63d_2d_v120_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_logmagslope_252d_2d_v121_signal(divyield, closeadj):
    base = divyield
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_logmagslope_21d_2d_v122_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_logmagslope_63d_2d_v123_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_logmagslope_252d_2d_v124_signal(payoutratio, closeadj):
    base = payoutratio
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_logmagslope_21d_2d_v125_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_logmagslope_63d_2d_v126_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_logmagslope_252d_2d_v127_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_logmagslope_21d_2d_v128_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_logmagslope_63d_2d_v129_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_logmagslope_252d_2d_v130_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_logmagslope_21d_2d_v131_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_logmagslope_63d_2d_v132_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_logmagslope_252d_2d_v133_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dps_lvl|
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_logslope_63d_2d_v134_signal(dps, closeadj):
    base = np.log((dps).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dps_lvl|
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_logslope_252d_2d_v135_signal(dps, closeadj):
    base = np.log((dps).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|divyield_calc|
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_logslope_63d_2d_v136_signal(dps, close, closeadj):
    base = np.log((_f074_divyield(dps, close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|divyield_calc|
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_logslope_252d_2d_v137_signal(dps, close, closeadj):
    base = np.log((_f074_divyield(dps, close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|divyieldforward_lvl|
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_logslope_63d_2d_v138_signal(divyield, closeadj):
    base = np.log((divyield).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|divyieldforward_lvl|
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_logslope_252d_2d_v139_signal(divyield, closeadj):
    base = np.log((divyield).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|payoutratio_lvl|
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_logslope_63d_2d_v140_signal(payoutratio, closeadj):
    base = np.log((payoutratio).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|payoutratio_lvl|
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_logslope_252d_2d_v141_signal(payoutratio, closeadj):
    base = np.log((payoutratio).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dps_yoy|
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_logslope_63d_2d_v142_signal(dps, closeadj):
    base = np.log((dps.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dps_yoy|
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_logslope_252d_2d_v143_signal(dps, closeadj):
    base = np.log((dps.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|div_payment_to_ni|
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_logslope_63d_2d_v144_signal(ncfdiv, netinc, closeadj):
    base = np.log((ncfdiv / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|div_payment_to_ni|
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_logslope_252d_2d_v145_signal(ncfdiv, netinc, closeadj):
    base = np.log((ncfdiv / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ncfdiv_to_fcf|
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_logslope_63d_2d_v146_signal(ncfdiv, fcf, closeadj):
    base = np.log((ncfdiv / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ncfdiv_to_fcf|
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_logslope_252d_2d_v147_signal(ncfdiv, fcf, closeadj):
    base = np.log((ncfdiv / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

