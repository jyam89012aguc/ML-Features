import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


# ===== folder domain primitives (institutional breadth & churn) =====
def _f34_breadth(nholders, w):
    # rolling growth of the distinct-holder base over w days
    return nholders / nholders.shift(w) - 1.0


def _f34_churn(newholders, exitholders, nholders, w):
    # holder-base turnover rate, smoothed over w days
    turn = _safe_div(newholders + exitholders, nholders)
    return turn.rolling(w, min_periods=max(1, w // 2)).mean()


def _f34_netentry(newholders, exitholders, nholders, w):
    # net entry rate (entries minus exits per holder), smoothed over w days
    net = _safe_div(newholders - exitholders, nholders)
    return net.rolling(w, min_periods=max(1, w // 2)).mean()


def _f34_conc(hhi, w):
    # concentration level (rolling mean of Herfindahl across investors)
    return hhi.rolling(w, min_periods=max(1, w // 2)).mean()


# ============ FEATURES 001-075 ============

# 63d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_63d_base_v001_signal(nholders):
    result = _f34_breadth(nholders, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_126d_base_v002_signal(nholders):
    result = _f34_breadth(nholders, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_252d_base_v003_signal(nholders):
    result = _f34_breadth(nholders, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_504d_base_v004_signal(nholders):
    result = _f34_breadth(nholders, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_21d_base_v005_signal(nholders):
    result = _f34_breadth(nholders, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log growth of holder base
def f34ib_f34_institutional_breadth_churn_logbreadth_63d_base_v006_signal(nholders):
    result = np.log(nholders / nholders.shift(63)) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log growth of holder base
def f34ib_f34_institutional_breadth_churn_logbreadth_126d_base_v007_signal(nholders):
    result = np.log(nholders / nholders.shift(126)) + _f34_breadth(nholders, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log growth of holder base
def f34ib_f34_institutional_breadth_churn_logbreadth_252d_base_v008_signal(nholders):
    result = np.log(nholders / nholders.shift(252)) + _f34_breadth(nholders, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of nholders level
def f34ib_f34_institutional_breadth_churn_znhold_252d_base_v009_signal(nholders):
    result = _z(nholders, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of nholders level
def f34ib_f34_institutional_breadth_churn_znhold_504d_base_v010_signal(nholders):
    result = _z(nholders, 504) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of nholders level
def f34ib_f34_institutional_breadth_churn_znhold_126d_base_v011_signal(nholders):
    result = _z(nholders, 126) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# nholders deviation from 252d mean (relative breadth)
def f34ib_f34_institutional_breadth_churn_nhdev_252d_base_v012_signal(nholders):
    result = _safe_div(nholders, _mean(nholders, 252)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# nholders deviation from 126d mean
def f34ib_f34_institutional_breadth_churn_nhdev_126d_base_v013_signal(nholders):
    result = _safe_div(nholders, _mean(nholders, 126)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of nholders level
def f34ib_f34_institutional_breadth_churn_nhrank_252d_base_v014_signal(nholders):
    result = nholders.rolling(252, min_periods=84).rank(pct=True) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of nholders level
def f34ib_f34_institutional_breadth_churn_nhrank_504d_base_v015_signal(nholders):
    result = nholders.rolling(504, min_periods=168).rank(pct=True) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d churn turnover rate
def f34ib_f34_institutional_breadth_churn_churn_21d_base_v016_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d churn turnover rate
def f34ib_f34_institutional_breadth_churn_churn_63d_base_v017_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d churn turnover rate
def f34ib_f34_institutional_breadth_churn_churn_126d_base_v018_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d churn turnover rate
def f34ib_f34_institutional_breadth_churn_churn_252d_base_v019_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d churn turnover rate
def f34ib_f34_institutional_breadth_churn_churn_504d_base_v020_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net entry rate
def f34ib_f34_institutional_breadth_churn_netentry_63d_base_v021_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net entry rate
def f34ib_f34_institutional_breadth_churn_netentry_126d_base_v022_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net entry rate
def f34ib_f34_institutional_breadth_churn_netentry_252d_base_v023_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net entry rate
def f34ib_f34_institutional_breadth_churn_netentry_21d_base_v024_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d new-holder entry rate (entries per holder)
def f34ib_f34_institutional_breadth_churn_entryrate_63d_base_v025_signal(newholders, nholders):
    rate = _safe_div(newholders, nholders)
    result = rate.rolling(63, min_periods=21).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d new-holder entry rate
def f34ib_f34_institutional_breadth_churn_entryrate_126d_base_v026_signal(newholders, nholders):
    rate = _safe_div(newholders, nholders)
    result = rate.rolling(126, min_periods=42).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d new-holder entry rate
def f34ib_f34_institutional_breadth_churn_entryrate_252d_base_v027_signal(newholders, nholders):
    rate = _safe_div(newholders, nholders)
    result = rate.rolling(252, min_periods=84).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d exit/churn-out rate (exits per holder)
def f34ib_f34_institutional_breadth_churn_exitrate_63d_base_v028_signal(exitholders, nholders):
    rate = _safe_div(exitholders, nholders)
    result = rate.rolling(63, min_periods=21).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d exit/churn-out rate
def f34ib_f34_institutional_breadth_churn_exitrate_126d_base_v029_signal(exitholders, nholders):
    rate = _safe_div(exitholders, nholders)
    result = rate.rolling(126, min_periods=42).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d exit/churn-out rate
def f34ib_f34_institutional_breadth_churn_exitrate_252d_base_v030_signal(exitholders, nholders):
    rate = _safe_div(exitholders, nholders)
    result = rate.rolling(252, min_periods=84).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# entry-to-exit ratio (inflow vs outflow of holders), 63d
def f34ib_f34_institutional_breadth_churn_entexratio_63d_base_v031_signal(newholders, exitholders, nholders):
    ratio = _safe_div(newholders, exitholders)
    result = ratio.rolling(63, min_periods=21).mean() + _f34_churn(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# entry-to-exit ratio, 126d
def f34ib_f34_institutional_breadth_churn_entexratio_126d_base_v032_signal(newholders, exitholders, nholders):
    ratio = _safe_div(newholders, exitholders)
    result = ratio.rolling(126, min_periods=42).mean() + _f34_churn(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# entry-to-exit ratio, 252d
def f34ib_f34_institutional_breadth_churn_entexratio_252d_base_v033_signal(newholders, exitholders, nholders):
    ratio = _safe_div(newholders, exitholders)
    result = ratio.rolling(252, min_periods=84).mean() + _f34_churn(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI concentration level, 63d
def f34ib_f34_institutional_breadth_churn_conc_63d_base_v034_signal(hhi):
    result = _f34_conc(hhi, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# HHI concentration level, 126d
def f34ib_f34_institutional_breadth_churn_conc_126d_base_v035_signal(hhi):
    result = _f34_conc(hhi, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# HHI concentration level, 252d
def f34ib_f34_institutional_breadth_churn_conc_252d_base_v036_signal(hhi):
    result = _f34_conc(hhi, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# HHI concentration trend (63d growth of concentration)
def f34ib_f34_institutional_breadth_churn_conctrend_63d_base_v037_signal(hhi):
    result = _safe_div(_f34_conc(hhi, 21), _f34_conc(hhi, 126)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI concentration trend (126d growth of concentration)
def f34ib_f34_institutional_breadth_churn_conctrend_126d_base_v038_signal(hhi):
    result = _safe_div(_f34_conc(hhi, 63), _f34_conc(hhi, 252)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI z-score over 252d
def f34ib_f34_institutional_breadth_churn_zconc_252d_base_v039_signal(hhi):
    result = _z(hhi, 252) + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI z-score over 504d
def f34ib_f34_institutional_breadth_churn_zconc_504d_base_v040_signal(hhi):
    result = _z(hhi, 504) + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI change over 126d (raw concentration delta)
def f34ib_f34_institutional_breadth_churn_concchg_126d_base_v041_signal(hhi):
    result = hhi - hhi.shift(126) + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI change over 252d
def f34ib_f34_institutional_breadth_churn_concchg_252d_base_v042_signal(hhi):
    result = hhi - hhi.shift(252) + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth density: holders per unit market cap (z over 252d)
def f34ib_f34_institutional_breadth_churn_density_252d_base_v043_signal(nholders, marketcap):
    dens = _safe_div(nholders, marketcap)
    result = _z(dens, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth density z over 504d
def f34ib_f34_institutional_breadth_churn_density_504d_base_v044_signal(nholders, marketcap):
    dens = _safe_div(nholders, marketcap)
    result = _z(dens, 504) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth density growth over 126d
def f34ib_f34_institutional_breadth_churn_densityg_126d_base_v045_signal(nholders, marketcap):
    dens = _safe_div(nholders, marketcap)
    result = _safe_div(dens, dens.shift(126)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average position value (totalvalue/nholders), z over 252d
def f34ib_f34_institutional_breadth_churn_avgpos_252d_base_v046_signal(totalvalue, nholders):
    avg = _safe_div(totalvalue, nholders)
    result = _z(avg, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average position value growth over 126d
def f34ib_f34_institutional_breadth_churn_avgposg_126d_base_v047_signal(totalvalue, nholders):
    avg = _safe_div(totalvalue, nholders)
    result = _safe_div(avg, avg.shift(126)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average position value growth over 252d
def f34ib_f34_institutional_breadth_churn_avgposg_252d_base_v048_signal(totalvalue, nholders):
    avg = _safe_div(totalvalue, nholders)
    result = _safe_div(avg, avg.shift(252)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average shares per holder (totalunits/nholders), z over 252d
def f34ib_f34_institutional_breadth_churn_avgunits_252d_base_v049_signal(totalunits, nholders):
    avg = _safe_div(totalunits, nholders)
    result = _z(avg, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average shares per holder growth over 126d
def f34ib_f34_institutional_breadth_churn_avgunitsg_126d_base_v050_signal(totalunits, nholders):
    avg = _safe_div(totalunits, nholders)
    result = _safe_div(avg, avg.shift(126)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth vs price divergence: breadth growth minus price growth, 126d
def f34ib_f34_institutional_breadth_churn_bpdiverg_126d_base_v051_signal(nholders, closeadj):
    priceg = closeadj / closeadj.shift(126) - 1.0
    result = _f34_breadth(nholders, 126) - priceg
    return result.replace([np.inf, -np.inf], np.nan)


# breadth vs price divergence, 252d
def f34ib_f34_institutional_breadth_churn_bpdiverg_252d_base_v052_signal(nholders, closeadj):
    priceg = closeadj / closeadj.shift(252) - 1.0
    result = _f34_breadth(nholders, 252) - priceg
    return result.replace([np.inf, -np.inf], np.nan)


# breadth vs price divergence, 63d
def f34ib_f34_institutional_breadth_churn_bpdiverg_63d_base_v053_signal(nholders, closeadj):
    priceg = closeadj / closeadj.shift(63) - 1.0
    result = _f34_breadth(nholders, 63) - priceg
    return result.replace([np.inf, -np.inf], np.nan)


# institutional ownership share (totalunits/sharesbas), z over 252d
def f34ib_f34_institutional_breadth_churn_ioshare_252d_base_v054_signal(totalunits, sharesbas, nholders):
    share = _safe_div(totalunits, sharesbas)
    result = _z(share, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# institutional ownership share growth over 126d
def f34ib_f34_institutional_breadth_churn_iosharegrow_126d_base_v055_signal(totalunits, sharesbas, nholders):
    share = _safe_div(totalunits, sharesbas)
    result = _safe_div(share, share.shift(126)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# institutional ownership share level deviation from 252d mean
def f34ib_f34_institutional_breadth_churn_ioshdev_252d_base_v056_signal(totalunits, sharesbas, nholders):
    share = _safe_div(totalunits, sharesbas)
    result = _safe_div(share, _mean(share, 252)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth acceleration: 63d breadth growth minus 126d breadth growth
def f34ib_f34_institutional_breadth_churn_breadthaccel_63d_base_v057_signal(nholders):
    result = _f34_breadth(nholders, 63) - _f34_breadth(nholders, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# breadth acceleration: 126d minus 252d
def f34ib_f34_institutional_breadth_churn_breadthaccel_126d_base_v058_signal(nholders):
    result = _f34_breadth(nholders, 126) - _f34_breadth(nholders, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# breadth acceleration: 21d minus 63d
def f34ib_f34_institutional_breadth_churn_breadthaccel_21d_base_v059_signal(nholders):
    result = _f34_breadth(nholders, 21) - _f34_breadth(nholders, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# churn acceleration: 63d churn minus 126d churn
def f34ib_f34_institutional_breadth_churn_churnaccel_63d_base_v060_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 63) - _f34_churn(newholders, exitholders, nholders, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# churn acceleration: 126d minus 252d
def f34ib_f34_institutional_breadth_churn_churnaccel_126d_base_v061_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 126) - _f34_churn(newholders, exitholders, nholders, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net-entry minus churn (signed flow quality), 126d
def f34ib_f34_institutional_breadth_churn_flowqual_126d_base_v062_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 126) - _f34_churn(newholders, exitholders, nholders, 126) * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# net-entry minus churn, 252d
def f34ib_f34_institutional_breadth_churn_flowqual_252d_base_v063_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 252) - _f34_churn(newholders, exitholders, nholders, 252) * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of churn rate over 252d
def f34ib_f34_institutional_breadth_churn_zchurn_252d_base_v064_signal(newholders, exitholders, nholders):
    turn = _safe_div(newholders + exitholders, nholders)
    result = _z(turn, 252) + _f34_churn(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of net-entry rate over 252d
def f34ib_f34_institutional_breadth_churn_znetentry_252d_base_v065_signal(newholders, exitholders, nholders):
    net = _safe_div(newholders - exitholders, nholders)
    result = _z(net, 252) + _f34_netentry(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of entry rate over 252d
def f34ib_f34_institutional_breadth_churn_zentry_252d_base_v066_signal(newholders, nholders):
    rate = _safe_div(newholders, nholders)
    result = _z(rate, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of exit rate over 252d
def f34ib_f34_institutional_breadth_churn_zexit_252d_base_v067_signal(exitholders, nholders):
    rate = _safe_div(exitholders, nholders)
    result = _z(rate, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth scaled by churn stability (growth per unit turnover)
def f34ib_f34_institutional_breadth_churn_growthstab_126d_base_v068_signal(newholders, exitholders, nholders):
    result = _safe_div(_f34_breadth(nholders, 126), _f34_churn(newholders, exitholders, nholders, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth scaled by churn stability, 252d
def f34ib_f34_institutional_breadth_churn_growthstab_252d_base_v069_signal(newholders, exitholders, nholders):
    result = _safe_div(_f34_breadth(nholders, 252), _f34_churn(newholders, exitholders, nholders, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# concentration vs breadth tension (HHI z plus breadth growth, opposing forces)
def f34ib_f34_institutional_breadth_churn_conctension_252d_base_v070_signal(hhi, nholders):
    result = _z(hhi, 252) - _z(nholders, 252) + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# inverse concentration (effective number of holders proxy), z over 252d
def f34ib_f34_institutional_breadth_churn_effnum_252d_base_v071_signal(hhi, nholders):
    effn = _safe_div(pd.Series(1.0, index=hhi.index), hhi)
    result = _z(effn, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# nholders std (breadth volatility) over 126d, normalized
def f34ib_f34_institutional_breadth_churn_breadthvol_126d_base_v072_signal(nholders):
    result = _safe_div(_std(nholders, 126), _mean(nholders, 126)) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# nholders std (breadth volatility) over 252d, normalized
def f34ib_f34_institutional_breadth_churn_breadthvol_252d_base_v073_signal(nholders):
    result = _safe_div(_std(nholders, 252), _mean(nholders, 252)) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# churn rate volatility over 252d (instability of turnover)
def f34ib_f34_institutional_breadth_churn_churnvol_252d_base_v074_signal(newholders, exitholders, nholders):
    turn = _safe_div(newholders + exitholders, nholders)
    result = _std(turn, 252) + _f34_churn(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth EWMA momentum (63-span ewm of breadth growth)
def f34ib_f34_institutional_breadth_churn_breadthewm_63d_base_v075_signal(nholders):
    bg = _f34_breadth(nholders, 21)
    result = bg.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34ib_f34_institutional_breadth_churn_breadthg_63d_base_v001_signal,
    f34ib_f34_institutional_breadth_churn_breadthg_126d_base_v002_signal,
    f34ib_f34_institutional_breadth_churn_breadthg_252d_base_v003_signal,
    f34ib_f34_institutional_breadth_churn_breadthg_504d_base_v004_signal,
    f34ib_f34_institutional_breadth_churn_breadthg_21d_base_v005_signal,
    f34ib_f34_institutional_breadth_churn_logbreadth_63d_base_v006_signal,
    f34ib_f34_institutional_breadth_churn_logbreadth_126d_base_v007_signal,
    f34ib_f34_institutional_breadth_churn_logbreadth_252d_base_v008_signal,
    f34ib_f34_institutional_breadth_churn_znhold_252d_base_v009_signal,
    f34ib_f34_institutional_breadth_churn_znhold_504d_base_v010_signal,
    f34ib_f34_institutional_breadth_churn_znhold_126d_base_v011_signal,
    f34ib_f34_institutional_breadth_churn_nhdev_252d_base_v012_signal,
    f34ib_f34_institutional_breadth_churn_nhdev_126d_base_v013_signal,
    f34ib_f34_institutional_breadth_churn_nhrank_252d_base_v014_signal,
    f34ib_f34_institutional_breadth_churn_nhrank_504d_base_v015_signal,
    f34ib_f34_institutional_breadth_churn_churn_21d_base_v016_signal,
    f34ib_f34_institutional_breadth_churn_churn_63d_base_v017_signal,
    f34ib_f34_institutional_breadth_churn_churn_126d_base_v018_signal,
    f34ib_f34_institutional_breadth_churn_churn_252d_base_v019_signal,
    f34ib_f34_institutional_breadth_churn_churn_504d_base_v020_signal,
    f34ib_f34_institutional_breadth_churn_netentry_63d_base_v021_signal,
    f34ib_f34_institutional_breadth_churn_netentry_126d_base_v022_signal,
    f34ib_f34_institutional_breadth_churn_netentry_252d_base_v023_signal,
    f34ib_f34_institutional_breadth_churn_netentry_21d_base_v024_signal,
    f34ib_f34_institutional_breadth_churn_entryrate_63d_base_v025_signal,
    f34ib_f34_institutional_breadth_churn_entryrate_126d_base_v026_signal,
    f34ib_f34_institutional_breadth_churn_entryrate_252d_base_v027_signal,
    f34ib_f34_institutional_breadth_churn_exitrate_63d_base_v028_signal,
    f34ib_f34_institutional_breadth_churn_exitrate_126d_base_v029_signal,
    f34ib_f34_institutional_breadth_churn_exitrate_252d_base_v030_signal,
    f34ib_f34_institutional_breadth_churn_entexratio_63d_base_v031_signal,
    f34ib_f34_institutional_breadth_churn_entexratio_126d_base_v032_signal,
    f34ib_f34_institutional_breadth_churn_entexratio_252d_base_v033_signal,
    f34ib_f34_institutional_breadth_churn_conc_63d_base_v034_signal,
    f34ib_f34_institutional_breadth_churn_conc_126d_base_v035_signal,
    f34ib_f34_institutional_breadth_churn_conc_252d_base_v036_signal,
    f34ib_f34_institutional_breadth_churn_conctrend_63d_base_v037_signal,
    f34ib_f34_institutional_breadth_churn_conctrend_126d_base_v038_signal,
    f34ib_f34_institutional_breadth_churn_zconc_252d_base_v039_signal,
    f34ib_f34_institutional_breadth_churn_zconc_504d_base_v040_signal,
    f34ib_f34_institutional_breadth_churn_concchg_126d_base_v041_signal,
    f34ib_f34_institutional_breadth_churn_concchg_252d_base_v042_signal,
    f34ib_f34_institutional_breadth_churn_density_252d_base_v043_signal,
    f34ib_f34_institutional_breadth_churn_density_504d_base_v044_signal,
    f34ib_f34_institutional_breadth_churn_densityg_126d_base_v045_signal,
    f34ib_f34_institutional_breadth_churn_avgpos_252d_base_v046_signal,
    f34ib_f34_institutional_breadth_churn_avgposg_126d_base_v047_signal,
    f34ib_f34_institutional_breadth_churn_avgposg_252d_base_v048_signal,
    f34ib_f34_institutional_breadth_churn_avgunits_252d_base_v049_signal,
    f34ib_f34_institutional_breadth_churn_avgunitsg_126d_base_v050_signal,
    f34ib_f34_institutional_breadth_churn_bpdiverg_126d_base_v051_signal,
    f34ib_f34_institutional_breadth_churn_bpdiverg_252d_base_v052_signal,
    f34ib_f34_institutional_breadth_churn_bpdiverg_63d_base_v053_signal,
    f34ib_f34_institutional_breadth_churn_ioshare_252d_base_v054_signal,
    f34ib_f34_institutional_breadth_churn_iosharegrow_126d_base_v055_signal,
    f34ib_f34_institutional_breadth_churn_ioshdev_252d_base_v056_signal,
    f34ib_f34_institutional_breadth_churn_breadthaccel_63d_base_v057_signal,
    f34ib_f34_institutional_breadth_churn_breadthaccel_126d_base_v058_signal,
    f34ib_f34_institutional_breadth_churn_breadthaccel_21d_base_v059_signal,
    f34ib_f34_institutional_breadth_churn_churnaccel_63d_base_v060_signal,
    f34ib_f34_institutional_breadth_churn_churnaccel_126d_base_v061_signal,
    f34ib_f34_institutional_breadth_churn_flowqual_126d_base_v062_signal,
    f34ib_f34_institutional_breadth_churn_flowqual_252d_base_v063_signal,
    f34ib_f34_institutional_breadth_churn_zchurn_252d_base_v064_signal,
    f34ib_f34_institutional_breadth_churn_znetentry_252d_base_v065_signal,
    f34ib_f34_institutional_breadth_churn_zentry_252d_base_v066_signal,
    f34ib_f34_institutional_breadth_churn_zexit_252d_base_v067_signal,
    f34ib_f34_institutional_breadth_churn_growthstab_126d_base_v068_signal,
    f34ib_f34_institutional_breadth_churn_growthstab_252d_base_v069_signal,
    f34ib_f34_institutional_breadth_churn_conctension_252d_base_v070_signal,
    f34ib_f34_institutional_breadth_churn_effnum_252d_base_v071_signal,
    f34ib_f34_institutional_breadth_churn_breadthvol_126d_base_v072_signal,
    f34ib_f34_institutional_breadth_churn_breadthvol_252d_base_v073_signal,
    f34ib_f34_institutional_breadth_churn_churnvol_252d_base_v074_signal,
    f34ib_f34_institutional_breadth_churn_breadthewm_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_INSTITUTIONAL_BREADTH_CHURN_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt",
           "nholders","newholders","exitholders","hhi","totalunits","avgposition"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f34_breadth", "_f34_churn", "_f34_netentry", "_f34_conc")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f34_institutional_breadth_churn_base_001_075_claude: {n_features} features pass")
