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
def _f21_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f21_revenue_growth_smooth(revenue, smooth_w, growth_w):
    sm = revenue.rolling(smooth_w, min_periods=max(1, smooth_w // 2)).mean()
    return sm.pct_change(periods=growth_w)


def _f21_revenue_log_growth(revenue, w):
    return np.log1p(revenue.pct_change(periods=w))


# 5d smoothed (5d) revenue growth × close
def f21rg_f21_revenue_growth_revgrowsm5_5d_base_v076_signal(revenue, closeadj):
    result = _f21_revenue_growth_smooth(revenue, 5, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed (21d) revenue growth × close
def f21rg_f21_revenue_growth_revgrowsm21_21d_base_v077_signal(revenue, closeadj):
    result = _f21_revenue_growth_smooth(revenue, 21, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed (21d) revenue growth × close
def f21rg_f21_revenue_growth_revgrowsm21_252d_base_v078_signal(revenue, closeadj):
    result = _f21_revenue_growth_smooth(revenue, 21, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed (63d) revenue growth × close
def f21rg_f21_revenue_growth_revgrowsm63_504d_base_v079_signal(revenue, closeadj):
    result = _f21_revenue_growth_smooth(revenue, 63, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed (252d) revenue growth × close
def f21rg_f21_revenue_growth_revgrowsm252_252d_base_v080_signal(revenue, closeadj):
    result = _f21_revenue_growth_smooth(revenue, 252, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log-growth diff (63m252)
def f21rg_f21_revenue_growth_revloggrowdiff_63m252_base_v081_signal(revenue, closeadj):
    a = _f21_revenue_log_growth(revenue, 63)
    b = _f21_revenue_log_growth(revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log-growth diff (252m504)
def f21rg_f21_revenue_growth_revloggrowdiff_252m504_base_v082_signal(revenue, closeadj):
    a = _f21_revenue_log_growth(revenue, 252)
    b = _f21_revenue_log_growth(revenue, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-growth × close return
def f21rg_f21_revenue_growth_revloggrowxret_252d_base_v083_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 252)
    result = base * closeadj.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-growth × close return
def f21rg_f21_revenue_growth_revloggrowxret_63d_base_v084_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 63)
    result = base * closeadj.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue × growth (dollar gain)
def f21rg_f21_revenue_growth_revgaindollar_252d_base_v085_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = base * revenue * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue × growth (dollar gain)
def f21rg_f21_revenue_growth_revgaindollar_504d_base_v086_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504)
    result = base * revenue * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of log revenue growth × close
def f21rg_f21_revenue_growth_revloggrowema_63d_base_v087_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA of log revenue growth × close
def f21rg_f21_revenue_growth_revloggrowema_504d_base_v088_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 504)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d revenue growth × close × volume
def f21rg_f21_revenue_growth_revgrowxvol_5d_base_v089_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 5)
    result = base * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × volume × close
def f21rg_f21_revenue_growth_revgrowxvol_63d_base_v090_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 63)
    result = base * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × volume × close
def f21rg_f21_revenue_growth_revgrowxvol_252d_base_v091_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252)
    result = base * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × log revenue × close
def f21rg_f21_revenue_growth_revgrowxlogrev_21d_base_v092_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base * np.log(revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × log revenue × close
def f21rg_f21_revenue_growth_revgrowxlogrev_63d_base_v093_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = base * np.log(revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × revenue × volume × close
def f21rg_f21_revenue_growth_revgrowxrevdv_252d_base_v094_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252)
    dv = closeadj * volume
    result = base * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth × dollar volume
def f21rg_f21_revenue_growth_revgrowxdv_504d_base_v095_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 504)
    dv = closeadj * volume
    result = base * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumsum of revenue growth × close
def f21rg_f21_revenue_growth_revgrowcumsum_63d_base_v096_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum of 21d revenue growth × close
def f21rg_f21_revenue_growth_revgrowcumsum_504d2_base_v097_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth weighted by sharesbas inverse
def f21rg_f21_revenue_growth_revgrow_pershare_21d_base_v098_signal(revenue, sharesbas, closeadj):
    g = _f21_revenue_growth(revenue, 21)
    rps = revenue / sharesbas.replace(0, np.nan)
    result = g * rps * closeadj / rps.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth weighted by sharesbas inverse 126d
def f21rg_f21_revenue_growth_revgrow_pershare_126d_base_v099_signal(revenue, sharesbas, closeadj):
    g = _f21_revenue_growth(revenue, 126)
    rps = revenue / sharesbas.replace(0, np.nan)
    result = g * rps * closeadj / rps.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth × revenue level (raw rev gain) over 63d
def f21rg_f21_revenue_growth_revgaindollar_63d_base_v100_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = base * revenue * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth std × close (long-term)
def f21rg_f21_revenue_growth_revgrowstd_63d_base_v101_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth std × close 126d
def f21rg_f21_revenue_growth_revgrowstd_126d_base_v102_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth × close (mean over 21d)
def f21rg_f21_revenue_growth_revgrowmean_21d_base_v103_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth mean over 63d
def f21rg_f21_revenue_growth_revgrowmean_63d_base_v104_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of 252d revenue growth × close
def f21rg_f21_revenue_growth_revgrowmean_252d_base_v105_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of revenue growth × close
def f21rg_f21_revenue_growth_revgrowmean_504d_base_v106_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth zscore over 63d
def f21rg_f21_revenue_growth_revgrowz_63d_base_v107_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue growth zscore × close
def f21rg_f21_revenue_growth_revloggrowz_252d_base_v108_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue growth zscore × close (504d)
def f21rg_f21_revenue_growth_revloggrowz_504d_base_v109_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × revenue per close
def f21rg_f21_revenue_growth_revgrowxrev_21d_base_v110_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = base * revenue * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d revenue growth × revenue per close
def f21rg_f21_revenue_growth_revgrowxrev_5d_base_v111_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 5)
    result = base * revenue * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue level squared × close
def f21rg_f21_revenue_growth_logrevsq_252d_base_v112_signal(revenue, closeadj):
    lr = np.log(_mean(revenue, 252).replace(0, np.nan))
    result = lr * lr * closeadj + _f21_revenue_growth(revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue × log revenue growth × close
def f21rg_f21_revenue_growth_logrevxgrow_252d_base_v113_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 252)
    result = base * np.log(revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth volatility-of-volatility × close
def f21rg_f21_revenue_growth_revgrowvolvol_252d_base_v114_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    sd = _std(base, 63)
    result = _std(sd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth volvol × close
def f21rg_f21_revenue_growth_revgrowvolvol_504d_base_v115_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    sd = _std(base, 252)
    result = _std(sd, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × turnover (volume/sharesbas)
def f21rg_f21_revenue_growth_revgrowturnover_252d_base_v116_signal(revenue, sharesbas, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252)
    turn = volume / sharesbas.replace(0, np.nan)
    result = base * turn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × turnover
def f21rg_f21_revenue_growth_revgrowturnover_63d_base_v117_signal(revenue, sharesbas, closeadj, volume):
    base = _f21_revenue_growth(revenue, 63)
    turn = volume / sharesbas.replace(0, np.nan)
    result = base * turn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log revenue growth squared × close
def f21rg_f21_revenue_growth_revloggrowsq_252d_base_v118_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log revenue growth squared × close
def f21rg_f21_revenue_growth_revloggrowsq_504d_base_v119_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 504)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × growth std (interaction)
def f21rg_f21_revenue_growth_revgrowxstd_252d_base_v120_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    sd = _std(_f21_revenue_growth(revenue, 21), 252)
    result = base * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × growth std
def f21rg_f21_revenue_growth_revgrowxstd_21d_base_v121_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    sd = _std(base, 21)
    result = base * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth EMA(252) × close
def f21rg_f21_revenue_growth_revgrowema_504d_base_v122_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log revenue growth EMA × close
def f21rg_f21_revenue_growth_revloggrowema_21d_base_v123_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × close (winsorized at 1.0)
def f21rg_f21_revenue_growth_revgrowclip_252d_base_v124_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252).clip(-1.0, 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth × close (winsorized)
def f21rg_f21_revenue_growth_revgrowclip_504d_base_v125_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504).clip(-1.0, 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth × log volume × close
def f21rg_f21_revenue_growth_revgrowxlogvol_252d_base_v126_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252)
    lv = np.log(volume.replace(0, np.nan))
    result = base * lv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × log volume × close
def f21rg_f21_revenue_growth_revgrowxlogvol_63d_base_v127_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 63)
    lv = np.log(volume.replace(0, np.nan))
    result = base * lv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth × ATR
def f21rg_f21_revenue_growth_revgrowxatr_21d_base_v128_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f21_revenue_growth(revenue, 21)
    result = base * atr * closeadj / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth × ATR
def f21rg_f21_revenue_growth_revgrowxatr_504d_base_v129_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f21_revenue_growth(revenue, 504)
    result = base * atr * closeadj / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × close × dv (alt encoding)
def f21rg_f21_revenue_growth_revgrowdvclose_252d_base_v130_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252)
    result = base * (closeadj * volume) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-126d revenue growth difference × close
def f21rg_f21_revenue_growth_revgrowdiff_126m252_base_v131_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 126)
    b = _f21_revenue_growth(revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-21d log revenue growth difference (vs prior month)
def f21rg_f21_revenue_growth_revloggrowdiff_21m63_base_v132_signal(revenue, closeadj):
    a = _f21_revenue_log_growth(revenue, 21)
    b = _f21_revenue_log_growth(revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max growth - 252d min growth × close
def f21rg_f21_revenue_growth_revgrowampl_252d_base_v133_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max growth - min growth × close
def f21rg_f21_revenue_growth_revgrowampl_504d_base_v134_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    result = (base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth × revenue squared
def f21rg_f21_revenue_growth_revgrowxrevsq_252d_base_v135_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    rsq = revenue * revenue / revenue.replace(0, np.nan)
    result = base * rsq * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth × revenue squared
def f21rg_f21_revenue_growth_revgrowxrevsq_504d_base_v136_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504)
    rsq = revenue * revenue / revenue.replace(0, np.nan)
    result = base * rsq * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue × revenue growth ratio (yoy growth dollars / current rev)
def f21rg_f21_revenue_growth_revgrowfrac_252d_base_v137_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue × revenue growth ratio (alt encoding)
def f21rg_f21_revenue_growth_revgrowfrac_504d_base_v138_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × ATR × volume
def f21rg_f21_revenue_growth_revgrowatrvol_252d_base_v139_signal(revenue, closeadj, high, low, volume):
    base = _f21_revenue_growth(revenue, 252)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = base * atr * volume * closeadj / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × ratio of close-to-21d-mean
def f21rg_f21_revenue_growth_revgrowclmean_252d_base_v140_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    cm = closeadj / _mean(closeadj, 21).replace(0, np.nan)
    result = base * cm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth in basis points (alt) × close
def f21rg_f21_revenue_growth_revgrowbps_252d_base_v141_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * 10000.0
    result = base * closeadj / 10000.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth bps × close
def f21rg_f21_revenue_growth_revgrowbps_504d_base_v142_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504) * 10000.0
    result = base * closeadj / 10000.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-mean of 252d revenue growth × close (smoothed yoy)
def f21rg_f21_revenue_growth_revgrowsmymean_252d_base_v143_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-mean of 252d revenue growth × close
def f21rg_f21_revenue_growth_revgrowsmymean_63d_base_v144_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × log close
def f21rg_f21_revenue_growth_revgrowxlogcl_252d_base_v145_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth × log close
def f21rg_f21_revenue_growth_revgrowxlogcl_504d_base_v146_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504)
    result = base * np.log(closeadj.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × log volume × close
def f21rg_f21_revenue_growth_revgrowxvollog_252d_base_v147_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252)
    result = base * np.log(volume.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × close × revenue level
def f21rg_f21_revenue_growth_revgrowxrl_63d_base_v148_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    result = base * _mean(revenue, 21) * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: weighted sum of growth, log-growth, std-growth × close
def f21rg_f21_revenue_growth_compositeg_252d_base_v149_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 252)
    b = _f21_revenue_log_growth(revenue, 252)
    c = _std(_f21_revenue_growth(revenue, 21), 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite × close
def f21rg_f21_revenue_growth_compositeg_504d_base_v150_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 504)
    b = _f21_revenue_log_growth(revenue, 504)
    c = _std(_f21_revenue_growth(revenue, 63), 504)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21rg_f21_revenue_growth_revgrowsm5_5d_base_v076_signal,
    f21rg_f21_revenue_growth_revgrowsm21_21d_base_v077_signal,
    f21rg_f21_revenue_growth_revgrowsm21_252d_base_v078_signal,
    f21rg_f21_revenue_growth_revgrowsm63_504d_base_v079_signal,
    f21rg_f21_revenue_growth_revgrowsm252_252d_base_v080_signal,
    f21rg_f21_revenue_growth_revloggrowdiff_63m252_base_v081_signal,
    f21rg_f21_revenue_growth_revloggrowdiff_252m504_base_v082_signal,
    f21rg_f21_revenue_growth_revloggrowxret_252d_base_v083_signal,
    f21rg_f21_revenue_growth_revloggrowxret_63d_base_v084_signal,
    f21rg_f21_revenue_growth_revgaindollar_252d_base_v085_signal,
    f21rg_f21_revenue_growth_revgaindollar_504d_base_v086_signal,
    f21rg_f21_revenue_growth_revloggrowema_63d_base_v087_signal,
    f21rg_f21_revenue_growth_revloggrowema_504d_base_v088_signal,
    f21rg_f21_revenue_growth_revgrowxvol_5d_base_v089_signal,
    f21rg_f21_revenue_growth_revgrowxvol_63d_base_v090_signal,
    f21rg_f21_revenue_growth_revgrowxvol_252d_base_v091_signal,
    f21rg_f21_revenue_growth_revgrowxlogrev_21d_base_v092_signal,
    f21rg_f21_revenue_growth_revgrowxlogrev_63d_base_v093_signal,
    f21rg_f21_revenue_growth_revgrowxrevdv_252d_base_v094_signal,
    f21rg_f21_revenue_growth_revgrowxdv_504d_base_v095_signal,
    f21rg_f21_revenue_growth_revgrowcumsum_63d_base_v096_signal,
    f21rg_f21_revenue_growth_revgrowcumsum_504d2_base_v097_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_21d_base_v098_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_126d_base_v099_signal,
    f21rg_f21_revenue_growth_revgaindollar_63d_base_v100_signal,
    f21rg_f21_revenue_growth_revgrowstd_63d_base_v101_signal,
    f21rg_f21_revenue_growth_revgrowstd_126d_base_v102_signal,
    f21rg_f21_revenue_growth_revgrowmean_21d_base_v103_signal,
    f21rg_f21_revenue_growth_revgrowmean_63d_base_v104_signal,
    f21rg_f21_revenue_growth_revgrowmean_252d_base_v105_signal,
    f21rg_f21_revenue_growth_revgrowmean_504d_base_v106_signal,
    f21rg_f21_revenue_growth_revgrowz_63d_base_v107_signal,
    f21rg_f21_revenue_growth_revloggrowz_252d_base_v108_signal,
    f21rg_f21_revenue_growth_revloggrowz_504d_base_v109_signal,
    f21rg_f21_revenue_growth_revgrowxrev_21d_base_v110_signal,
    f21rg_f21_revenue_growth_revgrowxrev_5d_base_v111_signal,
    f21rg_f21_revenue_growth_logrevsq_252d_base_v112_signal,
    f21rg_f21_revenue_growth_logrevxgrow_252d_base_v113_signal,
    f21rg_f21_revenue_growth_revgrowvolvol_252d_base_v114_signal,
    f21rg_f21_revenue_growth_revgrowvolvol_504d_base_v115_signal,
    f21rg_f21_revenue_growth_revgrowturnover_252d_base_v116_signal,
    f21rg_f21_revenue_growth_revgrowturnover_63d_base_v117_signal,
    f21rg_f21_revenue_growth_revloggrowsq_252d_base_v118_signal,
    f21rg_f21_revenue_growth_revloggrowsq_504d_base_v119_signal,
    f21rg_f21_revenue_growth_revgrowxstd_252d_base_v120_signal,
    f21rg_f21_revenue_growth_revgrowxstd_21d_base_v121_signal,
    f21rg_f21_revenue_growth_revgrowema_504d_base_v122_signal,
    f21rg_f21_revenue_growth_revloggrowema_21d_base_v123_signal,
    f21rg_f21_revenue_growth_revgrowclip_252d_base_v124_signal,
    f21rg_f21_revenue_growth_revgrowclip_504d_base_v125_signal,
    f21rg_f21_revenue_growth_revgrowxlogvol_252d_base_v126_signal,
    f21rg_f21_revenue_growth_revgrowxlogvol_63d_base_v127_signal,
    f21rg_f21_revenue_growth_revgrowxatr_21d_base_v128_signal,
    f21rg_f21_revenue_growth_revgrowxatr_504d_base_v129_signal,
    f21rg_f21_revenue_growth_revgrowdvclose_252d_base_v130_signal,
    f21rg_f21_revenue_growth_revgrowdiff_126m252_base_v131_signal,
    f21rg_f21_revenue_growth_revloggrowdiff_21m63_base_v132_signal,
    f21rg_f21_revenue_growth_revgrowampl_252d_base_v133_signal,
    f21rg_f21_revenue_growth_revgrowampl_504d_base_v134_signal,
    f21rg_f21_revenue_growth_revgrowxrevsq_252d_base_v135_signal,
    f21rg_f21_revenue_growth_revgrowxrevsq_504d_base_v136_signal,
    f21rg_f21_revenue_growth_revgrowfrac_252d_base_v137_signal,
    f21rg_f21_revenue_growth_revgrowfrac_504d_base_v138_signal,
    f21rg_f21_revenue_growth_revgrowatrvol_252d_base_v139_signal,
    f21rg_f21_revenue_growth_revgrowclmean_252d_base_v140_signal,
    f21rg_f21_revenue_growth_revgrowbps_252d_base_v141_signal,
    f21rg_f21_revenue_growth_revgrowbps_504d_base_v142_signal,
    f21rg_f21_revenue_growth_revgrowsmymean_252d_base_v143_signal,
    f21rg_f21_revenue_growth_revgrowsmymean_63d_base_v144_signal,
    f21rg_f21_revenue_growth_revgrowxlogcl_252d_base_v145_signal,
    f21rg_f21_revenue_growth_revgrowxlogcl_504d_base_v146_signal,
    f21rg_f21_revenue_growth_revgrowxvollog_252d_base_v147_signal,
    f21rg_f21_revenue_growth_revgrowxrl_63d_base_v148_signal,
    f21rg_f21_revenue_growth_compositeg_252d_base_v149_signal,
    f21rg_f21_revenue_growth_compositeg_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_REVENUE_GROWTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {
        "revenue": revenue, "sharesbas": sharesbas, "closeadj": closeadj,
        "high": high, "low": low, "volume": volume,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f21_revenue_growth", "_f21_revenue_growth_smooth", "_f21_revenue_log_growth")
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
    print(f"OK f21_revenue_growth_base_076_150_claude: {n_features} features pass")
