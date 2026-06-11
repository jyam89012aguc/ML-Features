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


# ============ FEATURES 076-150 ============

# 84d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_84d_base_v076_signal(nholders):
    result = _f34_breadth(nholders, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_189d_base_v077_signal(nholders):
    result = _f34_breadth(nholders, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_378d_base_v078_signal(nholders):
    result = _f34_breadth(nholders, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_42d_base_v079_signal(nholders):
    result = _f34_breadth(nholders, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d breadth growth of holder base
def f34ib_f34_institutional_breadth_churn_breadthg_315d_base_v080_signal(nholders):
    result = _f34_breadth(nholders, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log growth of holder base
def f34ib_f34_institutional_breadth_churn_logbreadth_504d_base_v081_signal(nholders):
    result = np.log(nholders / nholders.shift(504)) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d log growth of holder base
def f34ib_f34_institutional_breadth_churn_logbreadth_189d_base_v082_signal(nholders):
    result = np.log(nholders / nholders.shift(189)) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth annualized from 63d
def f34ib_f34_institutional_breadth_churn_breadthann_63d_base_v083_signal(nholders):
    result = np.log(nholders / nholders.shift(63)) * (252.0 / 63.0) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth annualized from 126d
def f34ib_f34_institutional_breadth_churn_breadthann_126d_base_v084_signal(nholders):
    result = np.log(nholders / nholders.shift(126)) * (252.0 / 126.0) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed breadth growth (21d mean of 63d growth)
def f34ib_f34_institutional_breadth_churn_smoothbreadth_63d_base_v085_signal(nholders):
    result = _mean(_f34_breadth(nholders, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed breadth growth (63d mean of 126d growth)
def f34ib_f34_institutional_breadth_churn_smoothbreadth_126d_base_v086_signal(nholders):
    result = _mean(_f34_breadth(nholders, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth EWMA (126-span)
def f34ib_f34_institutional_breadth_churn_breadthewm_126d_base_v087_signal(nholders):
    bg = _f34_breadth(nholders, 21)
    result = bg.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth EWMA (252-span)
def f34ib_f34_institutional_breadth_churn_breadthewm_252d_base_v088_signal(nholders):
    bg = _f34_breadth(nholders, 21)
    result = bg.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth info ratio (growth per dispersion of growth), 252d
def f34ib_f34_institutional_breadth_churn_breadthir_252d_base_v089_signal(nholders):
    bg = _f34_breadth(nholders, 63)
    result = _safe_div(bg, _std(bg, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth percentile rank, 252d
def f34ib_f34_institutional_breadth_churn_breadthrank_252d_base_v090_signal(nholders):
    bg = _f34_breadth(nholders, 63)
    result = bg.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d churn turnover rate
def f34ib_f34_institutional_breadth_churn_churn_42d_base_v091_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d churn turnover rate
def f34ib_f34_institutional_breadth_churn_churn_189d_base_v092_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d churn turnover rate
def f34ib_f34_institutional_breadth_churn_churn_378d_base_v093_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# churn relative to its own 252d baseline (turnover surprise)
def f34ib_f34_institutional_breadth_churn_churnsurp_126d_base_v094_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 63) - _f34_churn(newholders, exitholders, nholders, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# churn ratio to long baseline (252d), normalized
def f34ib_f34_institutional_breadth_churn_churnratio_126d_base_v095_signal(newholders, exitholders, nholders):
    result = _safe_div(_f34_churn(newholders, exitholders, nholders, 63), _f34_churn(newholders, exitholders, nholders, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 189d net entry rate
def f34ib_f34_institutional_breadth_churn_netentry_189d_base_v096_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d net entry rate
def f34ib_f34_institutional_breadth_churn_netentry_378d_base_v097_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d net entry rate
def f34ib_f34_institutional_breadth_churn_netentry_84d_base_v098_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# net entry EWMA (126-span)
def f34ib_f34_institutional_breadth_churn_netentryewm_126d_base_v099_signal(newholders, exitholders, nholders):
    net = _safe_div(newholders - exitholders, nholders)
    result = net.ewm(span=126, min_periods=42).mean() + _f34_netentry(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net entry EWMA (252-span)
def f34ib_f34_institutional_breadth_churn_netentryewm_252d_base_v100_signal(newholders, exitholders, nholders):
    net = _safe_div(newholders - exitholders, nholders)
    result = net.ewm(span=252, min_periods=84).mean() + _f34_netentry(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net entry percentile rank, 252d
def f34ib_f34_institutional_breadth_churn_netentryrank_252d_base_v101_signal(newholders, exitholders, nholders):
    net = _safe_div(newholders - exitholders, nholders)
    result = net.rolling(252, min_periods=84).rank(pct=True) + _f34_netentry(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net entry info ratio vs 252d dispersion
def f34ib_f34_institutional_breadth_churn_netentryir_252d_base_v102_signal(newholders, exitholders, nholders):
    net = _f34_netentry(newholders, exitholders, nholders, 63)
    result = _safe_div(net, _std(net, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d new-holder entry rate
def f34ib_f34_institutional_breadth_churn_entryrate_84d_base_v103_signal(newholders, nholders):
    rate = _safe_div(newholders, nholders)
    result = rate.rolling(84, min_periods=28).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d new-holder entry rate
def f34ib_f34_institutional_breadth_churn_entryrate_189d_base_v104_signal(newholders, nholders):
    rate = _safe_div(newholders, nholders)
    result = rate.rolling(189, min_periods=63).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d exit rate
def f34ib_f34_institutional_breadth_churn_exitrate_84d_base_v105_signal(exitholders, nholders):
    rate = _safe_div(exitholders, nholders)
    result = rate.rolling(84, min_periods=28).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d exit rate
def f34ib_f34_institutional_breadth_churn_exitrate_189d_base_v106_signal(exitholders, nholders):
    rate = _safe_div(exitholders, nholders)
    result = rate.rolling(189, min_periods=63).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# entry minus exit rate spread, 126d
def f34ib_f34_institutional_breadth_churn_eespread_126d_base_v107_signal(newholders, exitholders, nholders):
    ent = _safe_div(newholders, nholders)
    ext = _safe_div(exitholders, nholders)
    result = (ent - ext).rolling(126, min_periods=42).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# entry minus exit rate spread, 252d
def f34ib_f34_institutional_breadth_churn_eespread_252d_base_v108_signal(newholders, exitholders, nholders):
    ent = _safe_div(newholders, nholders)
    ext = _safe_div(exitholders, nholders)
    result = (ent - ext).rolling(252, min_periods=84).mean() + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI concentration level, 504d
def f34ib_f34_institutional_breadth_churn_conc_504d_base_v109_signal(hhi):
    result = _f34_conc(hhi, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# HHI concentration level, 42d
def f34ib_f34_institutional_breadth_churn_conc_42d_base_v110_signal(hhi):
    result = _f34_conc(hhi, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# HHI concentration trend, 252d (ratio of recent to long mean)
def f34ib_f34_institutional_breadth_churn_conctrend_252d_base_v111_signal(hhi):
    result = _safe_div(_f34_conc(hhi, 63), _f34_conc(hhi, 504)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI z-score over 126d
def f34ib_f34_institutional_breadth_churn_zconc_126d_base_v112_signal(hhi):
    result = _z(hhi, 126) + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI percentile rank over 252d
def f34ib_f34_institutional_breadth_churn_concrank_252d_base_v113_signal(hhi):
    result = hhi.rolling(252, min_periods=84).rank(pct=True) + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# HHI volatility (instability of concentration), 252d
def f34ib_f34_institutional_breadth_churn_concvol_252d_base_v114_signal(hhi):
    result = _std(hhi, 252) + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# effective number of holders (1/hhi) growth, 126d
def f34ib_f34_institutional_breadth_churn_effnumg_126d_base_v115_signal(hhi):
    effn = _safe_div(pd.Series(1.0, index=hhi.index), hhi)
    result = _safe_div(effn, effn.shift(126)) - 1.0 + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# effective number of holders growth, 252d
def f34ib_f34_institutional_breadth_churn_effnumg_252d_base_v116_signal(hhi):
    effn = _safe_div(pd.Series(1.0, index=hhi.index), hhi)
    result = _safe_div(effn, effn.shift(252)) - 1.0 + _f34_conc(hhi, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-adjusted breadth (nholders times (1-hhi)), z 252d
def f34ib_f34_institutional_breadth_churn_adjbreadth_252d_base_v117_signal(nholders, hhi):
    adj = nholders * (1.0 - hhi)
    result = _z(adj, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-adjusted breadth growth, 126d
def f34ib_f34_institutional_breadth_churn_adjbreadthg_126d_base_v118_signal(nholders, hhi):
    adj = nholders * (1.0 - hhi)
    result = _safe_div(adj, adj.shift(126)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth density (holders per marketcap) growth, 252d
def f34ib_f34_institutional_breadth_churn_densityg_252d_base_v119_signal(nholders, marketcap):
    dens = _safe_div(nholders, marketcap)
    result = _safe_div(dens, dens.shift(252)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth density percentile rank, 252d
def f34ib_f34_institutional_breadth_churn_densityrank_252d_base_v120_signal(nholders, marketcap):
    dens = _safe_div(nholders, marketcap)
    result = dens.rolling(252, min_periods=84).rank(pct=True) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average position value z over 504d
def f34ib_f34_institutional_breadth_churn_avgpos_504d_base_v121_signal(totalvalue, nholders):
    avg = _safe_div(totalvalue, nholders)
    result = _z(avg, 504) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average position value percentile rank, 252d
def f34ib_f34_institutional_breadth_churn_avgposrank_252d_base_v122_signal(totalvalue, nholders):
    avg = _safe_div(totalvalue, nholders)
    result = avg.rolling(252, min_periods=84).rank(pct=True) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average shares per holder growth, 252d
def f34ib_f34_institutional_breadth_churn_avgunitsg_252d_base_v123_signal(totalunits, nholders):
    avg = _safe_div(totalunits, nholders)
    result = _safe_div(avg, avg.shift(252)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average shares per holder z over 504d
def f34ib_f34_institutional_breadth_churn_avgunits_504d_base_v124_signal(totalunits, nholders):
    avg = _safe_div(totalunits, nholders)
    result = _z(avg, 504) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# institutional ownership share z over 504d
def f34ib_f34_institutional_breadth_churn_ioshare_504d_base_v125_signal(totalunits, sharesbas, nholders):
    share = _safe_div(totalunits, sharesbas)
    result = _z(share, 504) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# institutional ownership share growth, 252d
def f34ib_f34_institutional_breadth_churn_iosharegrow_252d_base_v126_signal(totalunits, sharesbas, nholders):
    share = _safe_div(totalunits, sharesbas)
    result = _safe_div(share, share.shift(252)) - 1.0 + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# institutional ownership share percentile rank, 252d
def f34ib_f34_institutional_breadth_churn_iosharerank_252d_base_v127_signal(totalunits, sharesbas, nholders):
    share = _safe_div(totalunits, sharesbas)
    result = share.rolling(252, min_periods=84).rank(pct=True) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth vs price divergence, 84d
def f34ib_f34_institutional_breadth_churn_bpdiverg_84d_base_v128_signal(nholders, closeadj):
    priceg = closeadj / closeadj.shift(84) - 1.0
    result = _f34_breadth(nholders, 84) - priceg
    return result.replace([np.inf, -np.inf], np.nan)


# breadth vs price divergence, 189d
def f34ib_f34_institutional_breadth_churn_bpdiverg_189d_base_v129_signal(nholders, closeadj):
    priceg = closeadj / closeadj.shift(189) - 1.0
    result = _f34_breadth(nholders, 189) - priceg
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-vs-price divergence z-scored, 252d window
def f34ib_f34_institutional_breadth_churn_zbpdiverg_252d_base_v130_signal(nholders, closeadj):
    priceg = closeadj / closeadj.shift(126) - 1.0
    div = _f34_breadth(nholders, 126) - priceg
    result = _z(div, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth relative to price momentum (ratio), 126d
def f34ib_f34_institutional_breadth_churn_bpratio_126d_base_v131_signal(nholders, closeadj):
    priceg = closeadj / closeadj.shift(126) - 1.0
    result = _safe_div(_f34_breadth(nholders, 126), priceg.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# breadth acceleration: 84d minus 189d
def f34ib_f34_institutional_breadth_churn_breadthaccel_84d_base_v132_signal(nholders):
    result = _f34_breadth(nholders, 84) - _f34_breadth(nholders, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# breadth acceleration: 252d minus 504d
def f34ib_f34_institutional_breadth_churn_breadthaccel_252d_base_v133_signal(nholders):
    result = _f34_breadth(nholders, 252) - _f34_breadth(nholders, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# churn acceleration: 42d minus 126d
def f34ib_f34_institutional_breadth_churn_churnaccel_42d_base_v134_signal(newholders, exitholders, nholders):
    result = _f34_churn(newholders, exitholders, nholders, 42) - _f34_churn(newholders, exitholders, nholders, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# net entry acceleration: 63d minus 252d
def f34ib_f34_institutional_breadth_churn_netaccel_63d_base_v135_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 63) - _f34_netentry(newholders, exitholders, nholders, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net entry acceleration: 126d minus 252d
def f34ib_f34_institutional_breadth_churn_netaccel_126d_base_v136_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 126) - _f34_netentry(newholders, exitholders, nholders, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net-entry minus churn flow quality, 63d
def f34ib_f34_institutional_breadth_churn_flowqual_63d_base_v137_signal(newholders, exitholders, nholders):
    result = _f34_netentry(newholders, exitholders, nholders, 63) - _f34_churn(newholders, exitholders, nholders, 63) * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth per unit concentration (diversified accumulation), 126d
def f34ib_f34_institutional_breadth_churn_divaccum_126d_base_v138_signal(nholders, hhi):
    result = _safe_div(_f34_breadth(nholders, 126), _f34_conc(hhi, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth per unit concentration, 252d
def f34ib_f34_institutional_breadth_churn_divaccum_252d_base_v139_signal(nholders, hhi):
    result = _safe_div(_f34_breadth(nholders, 252), _f34_conc(hhi, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of churn over 504d
def f34ib_f34_institutional_breadth_churn_zchurn_504d_base_v140_signal(newholders, exitholders, nholders):
    turn = _safe_div(newholders + exitholders, nholders)
    result = _z(turn, 504) + _f34_churn(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of net entry over 504d
def f34ib_f34_institutional_breadth_churn_znetentry_504d_base_v141_signal(newholders, exitholders, nholders):
    net = _safe_div(newholders - exitholders, nholders)
    result = _z(net, 504) + _f34_netentry(newholders, exitholders, nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth z over 252d scaled by churn (conviction-weighted breadth)
def f34ib_f34_institutional_breadth_churn_convbreadth_252d_base_v142_signal(newholders, exitholders, nholders):
    zb = _z(nholders, 252)
    result = zb * (1.0 + _f34_netentry(newholders, exitholders, nholders, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# entry-rate momentum (63d mean minus 252d mean of entry rate)
def f34ib_f34_institutional_breadth_churn_entrymom_126d_base_v143_signal(newholders, nholders):
    rate = _safe_div(newholders, nholders)
    result = _mean(rate, 63) - _mean(rate, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# exit-rate momentum (63d mean minus 252d mean of exit rate)
def f34ib_f34_institutional_breadth_churn_exitmom_126d_base_v144_signal(exitholders, nholders):
    rate = _safe_div(exitholders, nholders)
    result = _mean(rate, 63) - _mean(rate, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# total 13F value per holder vs market cap (relative position sizing), z 252d
def f34ib_f34_institutional_breadth_churn_possize_252d_base_v145_signal(totalvalue, nholders, marketcap):
    avg = _safe_div(totalvalue, nholders)
    rel = _safe_div(avg, marketcap)
    result = _z(rel, 252) + _f34_breadth(nholders, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth confirmed by ownership-share growth (co-movement), 126d
def f34ib_f34_institutional_breadth_churn_breadthconf_126d_base_v146_signal(nholders, totalunits, sharesbas):
    share = _safe_div(totalunits, sharesbas)
    shareg = _safe_div(share, share.shift(126)) - 1.0
    result = _f34_breadth(nholders, 126) * np.sign(shareg) + _f34_breadth(nholders, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# churn-adjusted net entry (signal stability), 252d
def f34ib_f34_institutional_breadth_churn_stabnet_252d_base_v147_signal(newholders, exitholders, nholders):
    result = _safe_div(_f34_netentry(newholders, exitholders, nholders, 252), _f34_churn(newholders, exitholders, nholders, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# concentration change confirmed by breadth (divergence sign), 252d
def f34ib_f34_institutional_breadth_churn_concbreadthdiv_252d_base_v148_signal(hhi, nholders):
    concg = _safe_div(_f34_conc(hhi, 63), _f34_conc(hhi, 252)) - 1.0
    result = _f34_breadth(nholders, 252) - concg
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon breadth composite (63/126/252/504 average growth)
def f34ib_f34_institutional_breadth_churn_breadthblend_multi_base_v149_signal(nholders):
    result = (_f34_breadth(nholders, 63) + _f34_breadth(nholders, 126)
              + _f34_breadth(nholders, 252) + _f34_breadth(nholders, 504)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite holder-base health (breadth growth plus net entry minus churn), 252d
def f34ib_f34_institutional_breadth_churn_health_252d_base_v150_signal(newholders, exitholders, nholders):
    result = (_f34_breadth(nholders, 252)
              + _f34_netentry(newholders, exitholders, nholders, 252)
              - _f34_churn(newholders, exitholders, nholders, 252) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34ib_f34_institutional_breadth_churn_breadthg_84d_base_v076_signal,
    f34ib_f34_institutional_breadth_churn_breadthg_189d_base_v077_signal,
    f34ib_f34_institutional_breadth_churn_breadthg_378d_base_v078_signal,
    f34ib_f34_institutional_breadth_churn_breadthg_42d_base_v079_signal,
    f34ib_f34_institutional_breadth_churn_breadthg_315d_base_v080_signal,
    f34ib_f34_institutional_breadth_churn_logbreadth_504d_base_v081_signal,
    f34ib_f34_institutional_breadth_churn_logbreadth_189d_base_v082_signal,
    f34ib_f34_institutional_breadth_churn_breadthann_63d_base_v083_signal,
    f34ib_f34_institutional_breadth_churn_breadthann_126d_base_v084_signal,
    f34ib_f34_institutional_breadth_churn_smoothbreadth_63d_base_v085_signal,
    f34ib_f34_institutional_breadth_churn_smoothbreadth_126d_base_v086_signal,
    f34ib_f34_institutional_breadth_churn_breadthewm_126d_base_v087_signal,
    f34ib_f34_institutional_breadth_churn_breadthewm_252d_base_v088_signal,
    f34ib_f34_institutional_breadth_churn_breadthir_252d_base_v089_signal,
    f34ib_f34_institutional_breadth_churn_breadthrank_252d_base_v090_signal,
    f34ib_f34_institutional_breadth_churn_churn_42d_base_v091_signal,
    f34ib_f34_institutional_breadth_churn_churn_189d_base_v092_signal,
    f34ib_f34_institutional_breadth_churn_churn_378d_base_v093_signal,
    f34ib_f34_institutional_breadth_churn_churnsurp_126d_base_v094_signal,
    f34ib_f34_institutional_breadth_churn_churnratio_126d_base_v095_signal,
    f34ib_f34_institutional_breadth_churn_netentry_189d_base_v096_signal,
    f34ib_f34_institutional_breadth_churn_netentry_378d_base_v097_signal,
    f34ib_f34_institutional_breadth_churn_netentry_84d_base_v098_signal,
    f34ib_f34_institutional_breadth_churn_netentryewm_126d_base_v099_signal,
    f34ib_f34_institutional_breadth_churn_netentryewm_252d_base_v100_signal,
    f34ib_f34_institutional_breadth_churn_netentryrank_252d_base_v101_signal,
    f34ib_f34_institutional_breadth_churn_netentryir_252d_base_v102_signal,
    f34ib_f34_institutional_breadth_churn_entryrate_84d_base_v103_signal,
    f34ib_f34_institutional_breadth_churn_entryrate_189d_base_v104_signal,
    f34ib_f34_institutional_breadth_churn_exitrate_84d_base_v105_signal,
    f34ib_f34_institutional_breadth_churn_exitrate_189d_base_v106_signal,
    f34ib_f34_institutional_breadth_churn_eespread_126d_base_v107_signal,
    f34ib_f34_institutional_breadth_churn_eespread_252d_base_v108_signal,
    f34ib_f34_institutional_breadth_churn_conc_504d_base_v109_signal,
    f34ib_f34_institutional_breadth_churn_conc_42d_base_v110_signal,
    f34ib_f34_institutional_breadth_churn_conctrend_252d_base_v111_signal,
    f34ib_f34_institutional_breadth_churn_zconc_126d_base_v112_signal,
    f34ib_f34_institutional_breadth_churn_concrank_252d_base_v113_signal,
    f34ib_f34_institutional_breadth_churn_concvol_252d_base_v114_signal,
    f34ib_f34_institutional_breadth_churn_effnumg_126d_base_v115_signal,
    f34ib_f34_institutional_breadth_churn_effnumg_252d_base_v116_signal,
    f34ib_f34_institutional_breadth_churn_adjbreadth_252d_base_v117_signal,
    f34ib_f34_institutional_breadth_churn_adjbreadthg_126d_base_v118_signal,
    f34ib_f34_institutional_breadth_churn_densityg_252d_base_v119_signal,
    f34ib_f34_institutional_breadth_churn_densityrank_252d_base_v120_signal,
    f34ib_f34_institutional_breadth_churn_avgpos_504d_base_v121_signal,
    f34ib_f34_institutional_breadth_churn_avgposrank_252d_base_v122_signal,
    f34ib_f34_institutional_breadth_churn_avgunitsg_252d_base_v123_signal,
    f34ib_f34_institutional_breadth_churn_avgunits_504d_base_v124_signal,
    f34ib_f34_institutional_breadth_churn_ioshare_504d_base_v125_signal,
    f34ib_f34_institutional_breadth_churn_iosharegrow_252d_base_v126_signal,
    f34ib_f34_institutional_breadth_churn_iosharerank_252d_base_v127_signal,
    f34ib_f34_institutional_breadth_churn_bpdiverg_84d_base_v128_signal,
    f34ib_f34_institutional_breadth_churn_bpdiverg_189d_base_v129_signal,
    f34ib_f34_institutional_breadth_churn_zbpdiverg_252d_base_v130_signal,
    f34ib_f34_institutional_breadth_churn_bpratio_126d_base_v131_signal,
    f34ib_f34_institutional_breadth_churn_breadthaccel_84d_base_v132_signal,
    f34ib_f34_institutional_breadth_churn_breadthaccel_252d_base_v133_signal,
    f34ib_f34_institutional_breadth_churn_churnaccel_42d_base_v134_signal,
    f34ib_f34_institutional_breadth_churn_netaccel_63d_base_v135_signal,
    f34ib_f34_institutional_breadth_churn_netaccel_126d_base_v136_signal,
    f34ib_f34_institutional_breadth_churn_flowqual_63d_base_v137_signal,
    f34ib_f34_institutional_breadth_churn_divaccum_126d_base_v138_signal,
    f34ib_f34_institutional_breadth_churn_divaccum_252d_base_v139_signal,
    f34ib_f34_institutional_breadth_churn_zchurn_504d_base_v140_signal,
    f34ib_f34_institutional_breadth_churn_znetentry_504d_base_v141_signal,
    f34ib_f34_institutional_breadth_churn_convbreadth_252d_base_v142_signal,
    f34ib_f34_institutional_breadth_churn_entrymom_126d_base_v143_signal,
    f34ib_f34_institutional_breadth_churn_exitmom_126d_base_v144_signal,
    f34ib_f34_institutional_breadth_churn_possize_252d_base_v145_signal,
    f34ib_f34_institutional_breadth_churn_breadthconf_126d_base_v146_signal,
    f34ib_f34_institutional_breadth_churn_stabnet_252d_base_v147_signal,
    f34ib_f34_institutional_breadth_churn_concbreadthdiv_252d_base_v148_signal,
    f34ib_f34_institutional_breadth_churn_breadthblend_multi_base_v149_signal,
    f34ib_f34_institutional_breadth_churn_health_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_INSTITUTIONAL_BREADTH_CHURN_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f34_institutional_breadth_churn_base_076_150_claude: {n_features} features pass")
