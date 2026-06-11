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


# 21d mean of dps_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_mean_21d_base_v001_signal(dps, closeadj):
    base = dps
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dps_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_mean_63d_base_v002_signal(dps, closeadj):
    base = dps
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dps_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_mean_126d_base_v003_signal(dps, closeadj):
    base = dps
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dps_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_mean_252d_base_v004_signal(dps, closeadj):
    base = dps
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dps_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_mean_504d_base_v005_signal(dps, closeadj):
    base = dps
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of divyield_calc scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_mean_21d_base_v006_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of divyield_calc scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_mean_63d_base_v007_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of divyield_calc scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_mean_126d_base_v008_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of divyield_calc scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_mean_252d_base_v009_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of divyield_calc scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_mean_504d_base_v010_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of divyieldforward_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_mean_21d_base_v011_signal(divyield, closeadj):
    base = divyield
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of divyieldforward_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_mean_63d_base_v012_signal(divyield, closeadj):
    base = divyield
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of divyieldforward_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_mean_126d_base_v013_signal(divyield, closeadj):
    base = divyield
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of divyieldforward_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_mean_252d_base_v014_signal(divyield, closeadj):
    base = divyield
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of divyieldforward_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_mean_504d_base_v015_signal(divyield, closeadj):
    base = divyield
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of payoutratio_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_mean_21d_base_v016_signal(payoutratio, closeadj):
    base = payoutratio
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of payoutratio_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_mean_63d_base_v017_signal(payoutratio, closeadj):
    base = payoutratio
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of payoutratio_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_mean_126d_base_v018_signal(payoutratio, closeadj):
    base = payoutratio
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of payoutratio_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_mean_252d_base_v019_signal(payoutratio, closeadj):
    base = payoutratio
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of payoutratio_lvl scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_mean_504d_base_v020_signal(payoutratio, closeadj):
    base = payoutratio
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dps_yoy scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_mean_21d_base_v021_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dps_yoy scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_mean_63d_base_v022_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dps_yoy scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_mean_126d_base_v023_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dps_yoy scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_mean_252d_base_v024_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dps_yoy scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_mean_504d_base_v025_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of div_payment_to_ni scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_mean_21d_base_v026_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of div_payment_to_ni scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_mean_63d_base_v027_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of div_payment_to_ni scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_mean_126d_base_v028_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of div_payment_to_ni scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_mean_252d_base_v029_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of div_payment_to_ni scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_mean_504d_base_v030_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ncfdiv_to_fcf scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_mean_21d_base_v031_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncfdiv_to_fcf scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_mean_63d_base_v032_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncfdiv_to_fcf scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_mean_126d_base_v033_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncfdiv_to_fcf scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_mean_252d_base_v034_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncfdiv_to_fcf scaled by closeadj
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_mean_504d_base_v035_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_median_63d_base_v036_signal(dps, closeadj):
    base = dps
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_median_252d_base_v037_signal(dps, closeadj):
    base = dps
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_median_504d_base_v038_signal(dps, closeadj):
    base = dps
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_median_63d_base_v039_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_median_252d_base_v040_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_median_504d_base_v041_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_median_63d_base_v042_signal(divyield, closeadj):
    base = divyield
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_median_252d_base_v043_signal(divyield, closeadj):
    base = divyield
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_median_504d_base_v044_signal(divyield, closeadj):
    base = divyield
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_median_63d_base_v045_signal(payoutratio, closeadj):
    base = payoutratio
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_median_252d_base_v046_signal(payoutratio, closeadj):
    base = payoutratio
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_median_504d_base_v047_signal(payoutratio, closeadj):
    base = payoutratio
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_median_63d_base_v048_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_median_252d_base_v049_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_median_504d_base_v050_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_median_63d_base_v051_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_median_252d_base_v052_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_median_504d_base_v053_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_median_63d_base_v054_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_median_252d_base_v055_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_median_504d_base_v056_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_rmax_252d_base_v057_signal(dps, closeadj):
    base = dps
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_rmax_504d_base_v058_signal(dps, closeadj):
    base = dps
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_rmax_252d_base_v059_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_rmax_504d_base_v060_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_rmax_252d_base_v061_signal(divyield, closeadj):
    base = divyield
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_rmax_504d_base_v062_signal(divyield, closeadj):
    base = divyield
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_rmax_252d_base_v063_signal(payoutratio, closeadj):
    base = payoutratio
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of payoutratio_lvl
def f074dpv_f074_dividend_and_payout_valuation_payoutratio_lvl_rmax_504d_base_v064_signal(payoutratio, closeadj):
    base = payoutratio
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_rmax_252d_base_v065_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dps_yoy
def f074dpv_f074_dividend_and_payout_valuation_dps_yoy_rmax_504d_base_v066_signal(dps, closeadj):
    base = dps.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_rmax_252d_base_v067_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of div_payment_to_ni
def f074dpv_f074_dividend_and_payout_valuation_div_payment_to_ni_rmax_504d_base_v068_signal(ncfdiv, netinc, closeadj):
    base = ncfdiv / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_rmax_252d_base_v069_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ncfdiv_to_fcf
def f074dpv_f074_dividend_and_payout_valuation_ncfdiv_to_fcf_rmax_504d_base_v070_signal(ncfdiv, fcf, closeadj):
    base = ncfdiv / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_rmin_252d_base_v071_signal(dps, closeadj):
    base = dps
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of dps_lvl
def f074dpv_f074_dividend_and_payout_valuation_dps_lvl_rmin_504d_base_v072_signal(dps, closeadj):
    base = dps
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_rmin_252d_base_v073_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of divyield_calc
def f074dpv_f074_dividend_and_payout_valuation_divyield_calc_rmin_504d_base_v074_signal(dps, close, closeadj):
    base = _f074_divyield(dps, close)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of divyieldforward_lvl
def f074dpv_f074_dividend_and_payout_valuation_divyieldforward_lvl_rmin_252d_base_v075_signal(divyield, closeadj):
    base = divyield
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

