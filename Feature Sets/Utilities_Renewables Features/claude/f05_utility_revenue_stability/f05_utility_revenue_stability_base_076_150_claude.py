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


def _f05_revenue_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan)


def _f05_revenue_smoothness(revenue, w):
    pct = revenue.pct_change()
    return 1.0 / (pct.rolling(w, min_periods=max(1, w // 2)).std() + 1e-9)


def _f05_stability_score(revenue, ebitda, w):
    rev_cv = _f05_revenue_cv(revenue, w)
    ebt_cv = _f05_revenue_cv(ebitda, w)
    return (rev_cv + ebt_cv) / 2.0


# CV × dollar volume
def f05urs_f05_utility_revenue_stability_cvxdv_63d_base_v076_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 63)
    dv = closeadj * volume
    result = base * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxdv_252d_base_v077_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 252)
    dv = closeadj * volume
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxdv_252d_base_v078_signal(revenue, closeadj, volume):
    base = _f05_revenue_smoothness(revenue, 252)
    dv = closeadj * volume
    result = base * _mean(dv, 63) * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxdv_252d_base_v079_signal(revenue, ebitda, closeadj, volume):
    base = _f05_stability_score(revenue, ebitda, 252)
    dv = closeadj * volume
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# CV × ebitda margin proxy × close
def f05urs_f05_utility_revenue_stability_cvxmargin_252d_base_v080_signal(revenue, ebitda, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    m = ebitda / revenue.replace(0, np.nan)
    result = base * _mean(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxmargin_252d_base_v081_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    m = ebitda / revenue.replace(0, np.nan)
    result = base * _mean(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × revenue growth × close
def f05urs_f05_utility_revenue_stability_cvxrevgrowth_63d_base_v082_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63)
    g = revenue.pct_change(63)
    result = base * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxrevgrowth_252d_base_v083_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    g = revenue.pct_change(252)
    result = base * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth × ebitda growth × close
def f05urs_f05_utility_revenue_stability_smoothxebitda_252d_base_v084_signal(revenue, ebitda, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    g = ebitda.pct_change(252)
    result = base * g * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × ebitda growth × close
def f05urs_f05_utility_revenue_stability_stabxebitda_252d_base_v085_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    g = ebitda.pct_change(252)
    result = base * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Ebitda CV × close (analog to revenue CV)
def f05urs_f05_utility_revenue_stability_ebitdacv_63d_base_v086_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63)
    ec = _f05_revenue_cv(ebitda, 63)
    result = ec * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_ebitdacv_252d_base_v087_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    ec = _f05_revenue_cv(ebitda, 252)
    result = ec * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_ebitdacv_504d_base_v088_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 504)
    ec = _f05_revenue_cv(ebitda, 504)
    result = ec * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Ebitda smoothness × close
def f05urs_f05_utility_revenue_stability_ebitdasmooth_252d_base_v089_signal(revenue, ebitda, closeadj):
    rb = _f05_revenue_smoothness(revenue, 252)
    es = _f05_revenue_smoothness(ebitda, 252)
    result = es * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_ebitdasmooth_63d_base_v090_signal(revenue, ebitda, closeadj):
    rb = _f05_revenue_smoothness(revenue, 63)
    es = _f05_revenue_smoothness(ebitda, 63)
    result = es * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Revenue CV - Ebitda CV (relative stability) × close
def f05urs_f05_utility_revenue_stability_relcv_252d_base_v091_signal(revenue, ebitda, closeadj):
    rb = _f05_stability_score(revenue, ebitda, 252)
    rc = _f05_revenue_cv(revenue, 252)
    ec = _f05_revenue_cv(ebitda, 252)
    result = (rc - ec) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_relcv_63d_base_v092_signal(revenue, ebitda, closeadj):
    rb = _f05_stability_score(revenue, ebitda, 63)
    rc = _f05_revenue_cv(revenue, 63)
    ec = _f05_revenue_cv(ebitda, 63)
    result = (rc - ec) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Revenue smoothness - ebitda smoothness × close
def f05urs_f05_utility_revenue_stability_relsmooth_252d_base_v093_signal(revenue, ebitda, closeadj):
    rb = _f05_revenue_smoothness(revenue, 252)
    es = _f05_revenue_smoothness(ebitda, 252)
    result = (rb - es) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × log revenue × close
def f05urs_f05_utility_revenue_stability_cvxlogrev_252d_base_v094_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxlogrev_63d_base_v095_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63)
    result = base * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × inv price × scale
def f05urs_f05_utility_revenue_stability_cvxinvprice_252d_base_v096_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxinvprice_252d_base_v097_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = base * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan) * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


# CV sign × volume × close
def f05urs_f05_utility_revenue_stability_cvsign_252d_base_v098_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 252)
    result = np.sign(base - _mean(base, 504)) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab sign × volume × close
def f05urs_f05_utility_revenue_stability_stabsign_252d_base_v099_signal(revenue, ebitda, closeadj, volume):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = np.sign(base - _mean(base, 504)) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV sum × close
def f05urs_f05_utility_revenue_stability_cvsum_252d_base_v100_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabsum_252d_base_v101_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × payout × close (regulated utility payout)
def f05urs_f05_utility_revenue_stability_cvxret5_252d_base_v102_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * closeadj.pct_change(5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxret10_252d_base_v103_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * closeadj.pct_change(10) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × volatility × close
def f05urs_f05_utility_revenue_stability_stabxvol_63d_base_v104_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63)
    vol = _std(closeadj.pct_change(), 63)
    result = base * vol * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxvol2_252d_base_v105_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    vol = _std(closeadj.pct_change(), 252)
    result = base * vol * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × volatility
def f05urs_f05_utility_revenue_stability_cvxretvol_252d_base_v106_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    vol = _std(closeadj.pct_change(), 252)
    result = base * vol * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × close pct change cumulative × close
def f05urs_f05_utility_revenue_stability_stabxcumret_252d_base_v107_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    cum = _mean(closeadj.pct_change(), 252) * 252
    result = base * cum * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × cum return × close
def f05urs_f05_utility_revenue_stability_cvxcumret_252d_base_v108_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    cum = _mean(closeadj.pct_change(), 252) * 252
    result = base * cum * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × revenue × close
def f05urs_f05_utility_revenue_stability_stabxrev_63d_base_v109_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63)
    result = base * np.log(revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxrev_252d_base_v110_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base * np.log(revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV inverse × volume × close
def f05urs_f05_utility_revenue_stability_cvinvxvol_252d_base_v111_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 252)
    result = (1.0 / base.replace(0, np.nan)) * _mean(volume, 63) * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# CV × inverse stability × close
def f05urs_f05_utility_revenue_stability_cvxinvstab_252d_base_v112_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    rc = _f05_revenue_cv(revenue, 252)
    result = rc * (1.0 / base.replace(0, np.nan)) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


# CV cross 63-504
def f05urs_f05_utility_revenue_stability_cvcross_63_504_base_v113_signal(revenue, closeadj):
    short = _f05_revenue_cv(revenue, 63)
    long = _f05_revenue_cv(revenue, 504)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth cross 21-252
def f05urs_f05_utility_revenue_stability_smoothcross_21_252_base_v114_signal(revenue, closeadj):
    short = _f05_revenue_smoothness(revenue, 21)
    long = _f05_revenue_smoothness(revenue, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab cross 63-252
def f05urs_f05_utility_revenue_stability_stabcross_63_252_base_v115_signal(revenue, ebitda, closeadj):
    short = _f05_stability_score(revenue, ebitda, 63)
    long = _f05_stability_score(revenue, ebitda, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × revenue × close
def f05urs_f05_utility_revenue_stability_cvxrev_252d_base_v116_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * _mean(revenue, 252) / _mean(revenue, 504).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth × revenue × close
def f05urs_f05_utility_revenue_stability_smoothxrev_252d_base_v117_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = base * _mean(revenue, 252) / _mean(revenue, 504).replace(0, np.nan) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


# CV × log ebitda × close
def f05urs_f05_utility_revenue_stability_cvxlogebitda_252d_base_v118_signal(revenue, ebitda, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * np.log(ebitda.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × log ebitda × close
def f05urs_f05_utility_revenue_stability_stabxlogebitda_252d_base_v119_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base * np.log(ebitda.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth cube × close
def f05urs_f05_utility_revenue_stability_smoothcube_252d_base_v120_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = base * base * base * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# CV cube × close
def f05urs_f05_utility_revenue_stability_cvcube_252d_base_v121_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab cube × close
def f05urs_f05_utility_revenue_stability_stabcube_252d_base_v122_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base * base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV diff-norm × close
def f05urs_f05_utility_revenue_stability_cvdn_252d_base_v123_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base.diff(63) / base.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabdn_252d_base_v124_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base.diff(63) / base.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth dn
def f05urs_f05_utility_revenue_stability_smoothdn_252d_base_v125_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = base.diff(63) / base.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV pct change × close
def f05urs_f05_utility_revenue_stability_cvchg_252d_base_v126_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvchg_63d_base_v127_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth pct change
def f05urs_f05_utility_revenue_stability_smoothchg_252d_base_v128_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab pct change
def f05urs_f05_utility_revenue_stability_stabchg_252d_base_v129_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × revenue/ebitda ratio × close
def f05urs_f05_utility_revenue_stability_cvxratio_252d_base_v130_signal(revenue, ebitda, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    r = revenue / ebitda.replace(0, np.nan)
    result = base * _mean(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × revenue/ebitda ratio × close
def f05urs_f05_utility_revenue_stability_stabxratio_252d_base_v131_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    r = revenue / ebitda.replace(0, np.nan)
    result = base * _mean(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth × revenue/ebitda × close
def f05urs_f05_utility_revenue_stability_smoothxratio_252d_base_v132_signal(revenue, ebitda, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    r = revenue / ebitda.replace(0, np.nan)
    result = base * _mean(r, 252) * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# CV × ATR × volume
def f05urs_f05_utility_revenue_stability_cvxatrxvol_252d_base_v133_signal(revenue, closeadj, volume, high, low):
    base = _f05_revenue_cv(revenue, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr * _mean(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × ATR × volume
def f05urs_f05_utility_revenue_stability_stabxatrxvol_252d_base_v134_signal(revenue, ebitda, closeadj, volume, high, low):
    base = _f05_stability_score(revenue, ebitda, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr * _mean(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# CV × ATR × return
def f05urs_f05_utility_revenue_stability_cvxatrxret_252d_base_v135_signal(revenue, closeadj, high, low):
    base = _f05_revenue_cv(revenue, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr * closeadj.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × ATR × return
def f05urs_f05_utility_revenue_stability_stabxatrxret_252d_base_v136_signal(revenue, ebitda, closeadj, high, low):
    base = _f05_stability_score(revenue, ebitda, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr * closeadj.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV mean over 252d × close
def f05urs_f05_utility_revenue_stability_cvmean_252d_base_v137_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothmean_252d_base_v138_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = _mean(base, 252) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabmean_252d_base_v139_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × revenue/assets type signal × close (use ratio of revenue)
def f05urs_f05_utility_revenue_stability_cvxrevdyn_252d_base_v140_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    dyn = _mean(revenue, 63) / _mean(revenue, 252).replace(0, np.nan) - 1.0
    result = base * dyn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × ebitda margin dynamics × close
def f05urs_f05_utility_revenue_stability_stabxmargindyn_252d_base_v141_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    m = ebitda / revenue.replace(0, np.nan)
    dyn = _mean(m, 63) / _mean(m, 252).replace(0, np.nan) - 1.0
    result = base * dyn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × ebitda margin × volume × close
def f05urs_f05_utility_revenue_stability_cvxmarginxvol_252d_base_v142_signal(revenue, ebitda, closeadj, volume):
    base = _f05_revenue_cv(revenue, 252)
    m = ebitda / revenue.replace(0, np.nan)
    result = base * _mean(m, 252) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV ema short × close
def f05urs_f05_utility_revenue_stability_cvema_63d_base_v143_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothema_63d_base_v144_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabema_63d_base_v145_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab rank short × close
def f05urs_f05_utility_revenue_stability_stabrank_63d_base_v146_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV rank short × close
def f05urs_f05_utility_revenue_stability_cvrank_63d_base_v147_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth rank short × close
def f05urs_f05_utility_revenue_stability_smoothrank_63d_base_v148_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × log volume × close
def f05urs_f05_utility_revenue_stability_cvxlogvol_252d_base_v149_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 252)
    result = base * np.log(volume.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × log volume × close
def f05urs_f05_utility_revenue_stability_stabxlogvol_252d_base_v150_signal(revenue, ebitda, closeadj, volume):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base * np.log(volume.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05urs_f05_utility_revenue_stability_cvxdv_63d_base_v076_signal,
    f05urs_f05_utility_revenue_stability_cvxdv_252d_base_v077_signal,
    f05urs_f05_utility_revenue_stability_smoothxdv_252d_base_v078_signal,
    f05urs_f05_utility_revenue_stability_stabxdv_252d_base_v079_signal,
    f05urs_f05_utility_revenue_stability_cvxmargin_252d_base_v080_signal,
    f05urs_f05_utility_revenue_stability_stabxmargin_252d_base_v081_signal,
    f05urs_f05_utility_revenue_stability_cvxrevgrowth_63d_base_v082_signal,
    f05urs_f05_utility_revenue_stability_cvxrevgrowth_252d_base_v083_signal,
    f05urs_f05_utility_revenue_stability_smoothxebitda_252d_base_v084_signal,
    f05urs_f05_utility_revenue_stability_stabxebitda_252d_base_v085_signal,
    f05urs_f05_utility_revenue_stability_ebitdacv_63d_base_v086_signal,
    f05urs_f05_utility_revenue_stability_ebitdacv_252d_base_v087_signal,
    f05urs_f05_utility_revenue_stability_ebitdacv_504d_base_v088_signal,
    f05urs_f05_utility_revenue_stability_ebitdasmooth_252d_base_v089_signal,
    f05urs_f05_utility_revenue_stability_ebitdasmooth_63d_base_v090_signal,
    f05urs_f05_utility_revenue_stability_relcv_252d_base_v091_signal,
    f05urs_f05_utility_revenue_stability_relcv_63d_base_v092_signal,
    f05urs_f05_utility_revenue_stability_relsmooth_252d_base_v093_signal,
    f05urs_f05_utility_revenue_stability_cvxlogrev_252d_base_v094_signal,
    f05urs_f05_utility_revenue_stability_cvxlogrev_63d_base_v095_signal,
    f05urs_f05_utility_revenue_stability_cvxinvprice_252d_base_v096_signal,
    f05urs_f05_utility_revenue_stability_smoothxinvprice_252d_base_v097_signal,
    f05urs_f05_utility_revenue_stability_cvsign_252d_base_v098_signal,
    f05urs_f05_utility_revenue_stability_stabsign_252d_base_v099_signal,
    f05urs_f05_utility_revenue_stability_cvsum_252d_base_v100_signal,
    f05urs_f05_utility_revenue_stability_stabsum_252d_base_v101_signal,
    f05urs_f05_utility_revenue_stability_cvxret5_252d_base_v102_signal,
    f05urs_f05_utility_revenue_stability_cvxret10_252d_base_v103_signal,
    f05urs_f05_utility_revenue_stability_stabxvol_63d_base_v104_signal,
    f05urs_f05_utility_revenue_stability_stabxvol2_252d_base_v105_signal,
    f05urs_f05_utility_revenue_stability_cvxretvol_252d_base_v106_signal,
    f05urs_f05_utility_revenue_stability_stabxcumret_252d_base_v107_signal,
    f05urs_f05_utility_revenue_stability_cvxcumret_252d_base_v108_signal,
    f05urs_f05_utility_revenue_stability_stabxrev_63d_base_v109_signal,
    f05urs_f05_utility_revenue_stability_stabxrev_252d_base_v110_signal,
    f05urs_f05_utility_revenue_stability_cvinvxvol_252d_base_v111_signal,
    f05urs_f05_utility_revenue_stability_cvxinvstab_252d_base_v112_signal,
    f05urs_f05_utility_revenue_stability_cvcross_63_504_base_v113_signal,
    f05urs_f05_utility_revenue_stability_smoothcross_21_252_base_v114_signal,
    f05urs_f05_utility_revenue_stability_stabcross_63_252_base_v115_signal,
    f05urs_f05_utility_revenue_stability_cvxrev_252d_base_v116_signal,
    f05urs_f05_utility_revenue_stability_smoothxrev_252d_base_v117_signal,
    f05urs_f05_utility_revenue_stability_cvxlogebitda_252d_base_v118_signal,
    f05urs_f05_utility_revenue_stability_stabxlogebitda_252d_base_v119_signal,
    f05urs_f05_utility_revenue_stability_smoothcube_252d_base_v120_signal,
    f05urs_f05_utility_revenue_stability_cvcube_252d_base_v121_signal,
    f05urs_f05_utility_revenue_stability_stabcube_252d_base_v122_signal,
    f05urs_f05_utility_revenue_stability_cvdn_252d_base_v123_signal,
    f05urs_f05_utility_revenue_stability_stabdn_252d_base_v124_signal,
    f05urs_f05_utility_revenue_stability_smoothdn_252d_base_v125_signal,
    f05urs_f05_utility_revenue_stability_cvchg_252d_base_v126_signal,
    f05urs_f05_utility_revenue_stability_cvchg_63d_base_v127_signal,
    f05urs_f05_utility_revenue_stability_smoothchg_252d_base_v128_signal,
    f05urs_f05_utility_revenue_stability_stabchg_252d_base_v129_signal,
    f05urs_f05_utility_revenue_stability_cvxratio_252d_base_v130_signal,
    f05urs_f05_utility_revenue_stability_stabxratio_252d_base_v131_signal,
    f05urs_f05_utility_revenue_stability_smoothxratio_252d_base_v132_signal,
    f05urs_f05_utility_revenue_stability_cvxatrxvol_252d_base_v133_signal,
    f05urs_f05_utility_revenue_stability_stabxatrxvol_252d_base_v134_signal,
    f05urs_f05_utility_revenue_stability_cvxatrxret_252d_base_v135_signal,
    f05urs_f05_utility_revenue_stability_stabxatrxret_252d_base_v136_signal,
    f05urs_f05_utility_revenue_stability_cvmean_252d_base_v137_signal,
    f05urs_f05_utility_revenue_stability_smoothmean_252d_base_v138_signal,
    f05urs_f05_utility_revenue_stability_stabmean_252d_base_v139_signal,
    f05urs_f05_utility_revenue_stability_cvxrevdyn_252d_base_v140_signal,
    f05urs_f05_utility_revenue_stability_stabxmargindyn_252d_base_v141_signal,
    f05urs_f05_utility_revenue_stability_cvxmarginxvol_252d_base_v142_signal,
    f05urs_f05_utility_revenue_stability_cvema_63d_base_v143_signal,
    f05urs_f05_utility_revenue_stability_smoothema_63d_base_v144_signal,
    f05urs_f05_utility_revenue_stability_stabema_63d_base_v145_signal,
    f05urs_f05_utility_revenue_stability_stabrank_63d_base_v146_signal,
    f05urs_f05_utility_revenue_stability_cvrank_63d_base_v147_signal,
    f05urs_f05_utility_revenue_stability_smoothrank_63d_base_v148_signal,
    f05urs_f05_utility_revenue_stability_cvxlogvol_252d_base_v149_signal,
    f05urs_f05_utility_revenue_stability_stabxlogvol_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_UTILITY_REVENUE_STABILITY_REGISTRY_076_150 = REGISTRY


def _build_cols():
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj.values * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj.values * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    return {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda,
    }


if __name__ == "__main__":
    cols = _build_cols()
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f05_revenue_cv", "_f05_revenue_smoothness", "_f05_stability_score")
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
    print(f"OK f05_utility_revenue_stability_base_076_150_claude: {n_features} features pass")
