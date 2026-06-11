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
def _f22_consumer_asset_growth(assets, w):
    return assets.pct_change(periods=w)


def _f22_loan_book_acceleration(assetsnc, w):
    g = assetsnc.pct_change(periods=w)
    return g.diff(periods=w)


def _f22_credit_origination_pulse(assets, revenue, w):
    ag = assets.pct_change(periods=w)
    rg = revenue.pct_change(periods=w)
    return ag - rg

def f22cfg_f22_consumer_finance_growth_aggrema_126d_xclose_base_v076_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 126).ewm(span=126, min_periods=max(1,126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrema_189d_xclose_base_v077_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 189).ewm(span=189, min_periods=max(1,189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrema_252d_xclose_base_v078_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 252).ewm(span=252, min_periods=max(1,252//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrema_378d_xclose_base_v079_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 378).ewm(span=378, min_periods=max(1,378//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrema_504d_xclose_base_v080_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 504).ewm(span=504, min_periods=max(1,504//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_5d_xclose2_base_v081_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 5)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_10d_xclose2_base_v082_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 10)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_21d_xclose2_base_v083_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_42d_xclose2_base_v084_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 42)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_63d_xclose2_base_v085_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_126d_xclose2_base_v086_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 126)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_189d_xclose2_base_v087_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 189)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_252d_xclose2_base_v088_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_378d_xclose2_base_v089_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 378)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggr_504d_xclose2_base_v090_signal(assets, closeadj):
    base = _f22_consumer_asset_growth(assets, 504)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_5d_xclose2_base_v091_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 5)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_10d_xclose2_base_v092_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 10)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_21d_xclose2_base_v093_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_42d_xclose2_base_v094_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 42)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_63d_xclose2_base_v095_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_126d_xclose2_base_v096_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 126)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_189d_xclose2_base_v097_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 189)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_252d_xclose2_base_v098_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_378d_xclose2_base_v099_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 378)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanacc_504d_xclose2_base_v100_signal(assetsnc, closeadj):
    base = _f22_loan_book_acceleration(assetsnc, 504)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_5d_xclose2_base_v101_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 5)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_10d_xclose2_base_v102_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 10)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_21d_xclose2_base_v103_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_42d_xclose2_base_v104_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 42)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_63d_xclose2_base_v105_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_126d_xclose2_base_v106_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 126)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_189d_xclose2_base_v107_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 189)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_252d_xclose2_base_v108_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_378d_xclose2_base_v109_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 378)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_origpulse_504d_xclose2_base_v110_signal(revenue, assets, closeadj):
    base = _f22_credit_origination_pulse(assets, revenue, 504)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_5d_xclose2_base_v111_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 5), 5)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_10d_xclose2_base_v112_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 10), 10)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_21d_xclose2_base_v113_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 21), 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_42d_xclose2_base_v114_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 42), 42)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_63d_xclose2_base_v115_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 63), 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_126d_xclose2_base_v116_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 126), 126)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_189d_xclose2_base_v117_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 189), 189)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_252d_xclose2_base_v118_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 252), 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_378d_xclose2_base_v119_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 378), 378)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrmean_504d_xclose2_base_v120_signal(assets, closeadj):
    base = _mean(_f22_consumer_asset_growth(assets, 504), 504)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_5d_xclose2_base_v121_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 5), 5)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_10d_xclose2_base_v122_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 10), 10)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_21d_xclose2_base_v123_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 21), 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_42d_xclose2_base_v124_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 42), 42)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_63d_xclose2_base_v125_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 63), 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_126d_xclose2_base_v126_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 126), 126)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_189d_xclose2_base_v127_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 189), 189)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_252d_xclose2_base_v128_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 252), 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_378d_xclose2_base_v129_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 378), 378)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_loanaccmean_504d_xclose2_base_v130_signal(assetsnc, closeadj):
    base = _mean(_f22_loan_book_acceleration(assetsnc, 504), 504)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_5d_xclose2_base_v131_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 5), 5)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_10d_xclose2_base_v132_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 10), 10)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_21d_xclose2_base_v133_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 21), 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_42d_xclose2_base_v134_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 42), 42)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_63d_xclose2_base_v135_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 63), 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_126d_xclose2_base_v136_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 126), 126)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_189d_xclose2_base_v137_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 189), 189)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_252d_xclose2_base_v138_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 252), 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_378d_xclose2_base_v139_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 378), 378)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_pulsestd_504d_xclose2_base_v140_signal(revenue, assets, closeadj):
    base = _std(_f22_credit_origination_pulse(assets, revenue, 504), 504)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_5d_xclose2_base_v141_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 5), 5)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_10d_xclose2_base_v142_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 10), 10)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_21d_xclose2_base_v143_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 21), 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_42d_xclose2_base_v144_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 42), 42)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_63d_xclose2_base_v145_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 63), 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_126d_xclose2_base_v146_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 126), 126)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_189d_xclose2_base_v147_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 189), 189)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_252d_xclose2_base_v148_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 252), 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_378d_xclose2_base_v149_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 378), 378)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22cfg_f22_consumer_finance_growth_aggrz_504d_xclose2_base_v150_signal(assets, closeadj):
    base = _z(_f22_consumer_asset_growth(assets, 504), 504)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f22cfg_f22_consumer_finance_growth_aggrema_126d_xclose_base_v076_signal,
    f22cfg_f22_consumer_finance_growth_aggrema_189d_xclose_base_v077_signal,
    f22cfg_f22_consumer_finance_growth_aggrema_252d_xclose_base_v078_signal,
    f22cfg_f22_consumer_finance_growth_aggrema_378d_xclose_base_v079_signal,
    f22cfg_f22_consumer_finance_growth_aggrema_504d_xclose_base_v080_signal,
    f22cfg_f22_consumer_finance_growth_aggr_5d_xclose2_base_v081_signal,
    f22cfg_f22_consumer_finance_growth_aggr_10d_xclose2_base_v082_signal,
    f22cfg_f22_consumer_finance_growth_aggr_21d_xclose2_base_v083_signal,
    f22cfg_f22_consumer_finance_growth_aggr_42d_xclose2_base_v084_signal,
    f22cfg_f22_consumer_finance_growth_aggr_63d_xclose2_base_v085_signal,
    f22cfg_f22_consumer_finance_growth_aggr_126d_xclose2_base_v086_signal,
    f22cfg_f22_consumer_finance_growth_aggr_189d_xclose2_base_v087_signal,
    f22cfg_f22_consumer_finance_growth_aggr_252d_xclose2_base_v088_signal,
    f22cfg_f22_consumer_finance_growth_aggr_378d_xclose2_base_v089_signal,
    f22cfg_f22_consumer_finance_growth_aggr_504d_xclose2_base_v090_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_5d_xclose2_base_v091_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_10d_xclose2_base_v092_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_21d_xclose2_base_v093_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_42d_xclose2_base_v094_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_63d_xclose2_base_v095_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_126d_xclose2_base_v096_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_189d_xclose2_base_v097_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_252d_xclose2_base_v098_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_378d_xclose2_base_v099_signal,
    f22cfg_f22_consumer_finance_growth_loanacc_504d_xclose2_base_v100_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_5d_xclose2_base_v101_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_10d_xclose2_base_v102_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_21d_xclose2_base_v103_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_42d_xclose2_base_v104_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_63d_xclose2_base_v105_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_126d_xclose2_base_v106_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_189d_xclose2_base_v107_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_252d_xclose2_base_v108_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_378d_xclose2_base_v109_signal,
    f22cfg_f22_consumer_finance_growth_origpulse_504d_xclose2_base_v110_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_5d_xclose2_base_v111_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_10d_xclose2_base_v112_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_21d_xclose2_base_v113_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_42d_xclose2_base_v114_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_63d_xclose2_base_v115_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_126d_xclose2_base_v116_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_189d_xclose2_base_v117_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_252d_xclose2_base_v118_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_378d_xclose2_base_v119_signal,
    f22cfg_f22_consumer_finance_growth_aggrmean_504d_xclose2_base_v120_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_5d_xclose2_base_v121_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_10d_xclose2_base_v122_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_21d_xclose2_base_v123_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_42d_xclose2_base_v124_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_63d_xclose2_base_v125_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_126d_xclose2_base_v126_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_189d_xclose2_base_v127_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_252d_xclose2_base_v128_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_378d_xclose2_base_v129_signal,
    f22cfg_f22_consumer_finance_growth_loanaccmean_504d_xclose2_base_v130_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_5d_xclose2_base_v131_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_10d_xclose2_base_v132_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_21d_xclose2_base_v133_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_42d_xclose2_base_v134_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_63d_xclose2_base_v135_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_126d_xclose2_base_v136_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_189d_xclose2_base_v137_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_252d_xclose2_base_v138_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_378d_xclose2_base_v139_signal,
    f22cfg_f22_consumer_finance_growth_pulsestd_504d_xclose2_base_v140_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_5d_xclose2_base_v141_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_10d_xclose2_base_v142_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_21d_xclose2_base_v143_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_42d_xclose2_base_v144_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_63d_xclose2_base_v145_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_126d_xclose2_base_v146_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_189d_xclose2_base_v147_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_252d_xclose2_base_v148_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_378d_xclose2_base_v149_signal,
    f22cfg_f22_consumer_finance_growth_aggrz_504d_xclose2_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_CONSUMER_FINANCE_GROWTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f22_consumer_asset_growth", "_f22_loan_book_acceleration", "_f22_credit_origination_pulse")
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
    print(f"OK f22_consumer_finance_growth: {n_features} features pass")
