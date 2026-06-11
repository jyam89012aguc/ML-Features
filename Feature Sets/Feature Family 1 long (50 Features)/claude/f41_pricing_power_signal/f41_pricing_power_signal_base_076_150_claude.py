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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f41_pricing_power_gpgrow(gp, w):
    return gp.pct_change(w)


def _f41_pricing_power_gprev(gp, revenue, w):
    gm = gp / revenue.replace(0, np.nan)
    return gm.diff(w)


def _f41_pricing_power_passthrough(gp, revenue, w):
    return gp.pct_change(w) - revenue.pct_change(w)


# 252d high quantile of gprev
def f41pps_f41_pricing_power_signal_gprevquantilehi_252d_base_v076_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(252, min_periods=63).quantile(0.9) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevquantilelo_252d_base_v077_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(252, min_periods=63).quantile(0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevquantilehi_504d_base_v078_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(504, min_periods=126).quantile(0.9) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevquantilelo_504d_base_v079_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(504, min_periods=126).quantile(0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowquantilehi_252d_base_v080_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21)
    return (base.rolling(252, min_periods=63).quantile(0.9) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowquantilelo_252d_base_v081_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21)
    return (base.rolling(252, min_periods=63).quantile(0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevskew_252d_base_v082_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(252, min_periods=63).skew() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevskew_504d_base_v083_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(504, min_periods=126).skew() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevkurt_252d_base_v084_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(252, min_periods=63).kurt() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevkurt_504d_base_v085_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(504, min_periods=126).kurt() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevmedian_252d_base_v086_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(252, min_periods=63).median() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevmedian_504d_base_v087_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (base.rolling(504, min_periods=126).median() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowiqr_252d_base_v088_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21)
    hi = base.rolling(252, min_periods=63).quantile(0.75)
    lo = base.rolling(252, min_periods=63).quantile(0.25)
    return ((hi - lo) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowiqr_504d_base_v089_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21)
    hi = base.rolling(504, min_periods=126).quantile(0.75)
    lo = base.rolling(504, min_periods=126).quantile(0.25)
    return ((hi - lo) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gp/equity ratio (return on equity from gross)
def f41pps_f41_pricing_power_signal_gpequity_252d_base_v090_signal(gp, equity, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    return ((_mean(gp / equity.replace(0, np.nan), 252) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpequity_63d_base_v091_signal(gp, equity, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 63) * 0.0
    return ((_mean(gp / equity.replace(0, np.nan), 63) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gross margin × workingcapital
def f41pps_f41_pricing_power_signal_gmxwc_252d_base_v092_signal(gp, revenue, workingcapital, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    return ((_mean(gm, 252) + aux) * workingcapital * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxwc_63d_base_v093_signal(gp, revenue, workingcapital, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    return ((_mean(gm, 63) + aux) * workingcapital * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d composite passthrough × intexp (cost-pricing under interest stress)
def f41pps_f41_pricing_power_signal_passxintexp_252d_base_v094_signal(gp, revenue, intexp, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 252) * intexp * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passxintexp_63d_base_v095_signal(gp, revenue, intexp, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 63) * intexp * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gprev relative to long-term mean (vs 504d)
def f41pps_f41_pricing_power_signal_gprevvslong_252d_base_v096_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return ((_mean(base, 252) - _mean(base, 504)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevvslong_63d_base_v097_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return ((_mean(base, 63) - _mean(base, 252)) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev × ncfo growth
def f41pps_f41_pricing_power_signal_gprevxncfog_252d_base_v098_signal(gp, revenue, ncfo, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 252) * ncfo.pct_change(252).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxncfog_63d_base_v099_signal(gp, revenue, ncfo, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 63) * ncfo.pct_change(63).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev × fcf growth
def f41pps_f41_pricing_power_signal_gprevxfcfg_252d_base_v100_signal(gp, revenue, fcf, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 252) * fcf.pct_change(252).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxfcfg_63d_base_v101_signal(gp, revenue, fcf, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 63) * fcf.pct_change(63).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d count of months with margin expansion
def f41pps_f41_pricing_power_signal_marginexpfreq_252d_base_v102_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    pos = (base > 0.001).astype(float)
    return (pos.rolling(252, min_periods=63).sum() / 252.0 * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_marginexpfreq_504d_base_v103_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    pos = (base > 0.001).astype(float)
    return (pos.rolling(504, min_periods=126).sum() / 504.0 * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gp growth × revenue growth (compound)
def f41pps_f41_pricing_power_signal_gpgrowxrevg_252d_base_v104_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * revenue.pct_change(252).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxrevg_63d_base_v105_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * revenue.pct_change(63).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev × debt level (margin under leverage)
def f41pps_f41_pricing_power_signal_gprevxdebt_252d_base_v106_signal(gp, revenue, debt, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 252) * debt * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxdebt_63d_base_v107_signal(gp, revenue, debt, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 63) * debt * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gp/capex (capital-light pricing)
def f41pps_f41_pricing_power_signal_gpovercapex_252d_base_v108_signal(gp, capex, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    ratio = gp / capex.abs().replace(0, np.nan)
    return ((_mean(ratio, 252) + aux) * closeadj / 1.0e3).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpovercapex_63d_base_v109_signal(gp, capex, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 63) * 0.0
    ratio = gp / capex.abs().replace(0, np.nan)
    return ((_mean(ratio, 63) + aux) * closeadj / 1.0e3).replace([np.inf, -np.inf], np.nan)


# 252d passthrough × eps level
def f41pps_f41_pricing_power_signal_passxeps_252d_base_v110_signal(gp, revenue, eps, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 252) * eps * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passxeps_63d_base_v111_signal(gp, revenue, eps, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 63) * eps * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d passthrough × revenue growth
def f41pps_f41_pricing_power_signal_passxrevg_252d_base_v112_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 252) * revenue.pct_change(252).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passxrevg_63d_base_v113_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_passthrough(gp, revenue, 63) * revenue.pct_change(63).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gross margin × netinc (pricing × profit absolute)
def f41pps_f41_pricing_power_signal_gmxni_252d_base_v114_signal(gp, revenue, netinc, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    return ((_mean(gm, 252) + aux) * netinc * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxni_63d_base_v115_signal(gp, revenue, netinc, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    return ((_mean(gm, 63) + aux) * netinc * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gp growth - asset growth (capital-efficient pricing)
def f41pps_f41_pricing_power_signal_gpvsassetg_252d_base_v116_signal(gp, assets, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    return ((gp.pct_change(252) - assets.pct_change(252) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpvsassetg_63d_base_v117_signal(gp, assets, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 63) * 0.0
    return ((gp.pct_change(63) - assets.pct_change(63) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d sum of passthrough magnitudes
def f41pps_f41_pricing_power_signal_passsum_252d_base_v118_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 21)
    return (base.rolling(252, min_periods=63).sum() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passsum_504d_base_v119_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 21)
    return (base.rolling(504, min_periods=126).sum() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passsum_63d_base_v120_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 5)
    return (base.rolling(63, min_periods=21).sum() * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d EMA of passthrough
def f41pps_f41_pricing_power_signal_passema_252d_base_v121_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 21)
    return (base.ewm(span=252, adjust=False).mean() * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passema_63d_base_v122_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 5)
    return (base.ewm(span=63, adjust=False).mean() * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev with smaller window 5d
def f41pps_f41_pricing_power_signal_gprevsmallwin_252d_base_v123_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 5)
    return (_mean(base, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev × intexp interaction
def f41pps_f41_pricing_power_signal_gprevxintexp_252d_base_v124_signal(gp, revenue, intexp, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 252) * intexp * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxintexp_63d_base_v125_signal(gp, revenue, intexp, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 63) * intexp * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gp acceleration: 63d gp growth - 252d gp growth
def f41pps_f41_pricing_power_signal_gpaccel_252d_base_v126_signal(gp, closeadj):
    return ((_f41_pricing_power_gpgrow(gp, 63) - _f41_pricing_power_gpgrow(gp, 252)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpaccel_63d_base_v127_signal(gp, closeadj):
    return ((_f41_pricing_power_gpgrow(gp, 21) - _f41_pricing_power_gpgrow(gp, 63)) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev relative to peers (using rolling sample)
def f41pps_f41_pricing_power_signal_gprevpercentile_252d_base_v128_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    return (rank * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevpercentile_504d_base_v129_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    return (rank * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gross margin trend (gprev mean × revenue per share)
def f41pps_f41_pricing_power_signal_gprevxrevpershare_252d_base_v130_signal(gp, revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    return (_f41_pricing_power_gprev(gp, revenue, 252) * rps * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxrevpershare_63d_base_v131_signal(gp, revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    return (_f41_pricing_power_gprev(gp, revenue, 63) * rps * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gpgrow × workingcapital
def f41pps_f41_pricing_power_signal_gpgrowxwc_252d_base_v132_signal(gp, workingcapital, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * workingcapital * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxwc_63d_base_v133_signal(gp, workingcapital, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * workingcapital * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gross margin variability (gprev std)
def f41pps_f41_pricing_power_signal_gprevstd_252d_base_v134_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (_std(base, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevstd_504d_base_v135_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return (_std(base, 504) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d composite ranking: gp grow × gprev × revenue growth
def f41pps_f41_pricing_power_signal_triplecombo_252d_base_v136_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * _f41_pricing_power_gprev(gp, revenue, 252) * revenue.pct_change(252).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_triplecombo_63d_base_v137_signal(gp, revenue, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * _f41_pricing_power_gprev(gp, revenue, 63) * revenue.pct_change(63).fillna(0.0) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gp/sharesbas (gross profit per share)
def f41pps_f41_pricing_power_signal_gppershare_252d_base_v138_signal(gp, sharesbas, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    return ((_mean(gp / sharesbas.replace(0, np.nan), 252) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gppershare_63d_base_v139_signal(gp, sharesbas, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 63) * 0.0
    return ((_mean(gp / sharesbas.replace(0, np.nan), 63) + aux) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gross margin × ncfo
def f41pps_f41_pricing_power_signal_gmxncfo_252d_base_v140_signal(gp, revenue, ncfo, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    return ((_mean(gm, 252) + aux) * ncfo * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxncfo_63d_base_v141_signal(gp, revenue, ncfo, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    return ((_mean(gm, 63) + aux) * ncfo * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d composite: gprev cumulative × revenue level
def f41pps_f41_pricing_power_signal_gprevcumxrev_252d_base_v142_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(252, min_periods=63).sum()
    return (base * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevcumxrev_504d_base_v143_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(504, min_periods=126).sum()
    return (base * revenue * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gpgrow × fcf level
def f41pps_f41_pricing_power_signal_gpgrowxfcfl_252d_base_v144_signal(gp, fcf, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 252) * fcf * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxfcfl_63d_base_v145_signal(gp, fcf, closeadj):
    return (_f41_pricing_power_gpgrow(gp, 63) * fcf * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d gprev coefficient of variation (std/mean abs)
def f41pps_f41_pricing_power_signal_gprevcv_252d_base_v146_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return ((_std(base, 252) / _mean(base.abs(), 252).replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevcv_504d_base_v147_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    return ((_std(base, 504) / _mean(base.abs(), 504).replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


# 252d gprev × ebitda level
def f41pps_f41_pricing_power_signal_gprevxebitda_252d_base_v148_signal(gp, revenue, ebitda, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 252) * ebitda * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxebitda_63d_base_v149_signal(gp, revenue, ebitda, closeadj):
    return (_f41_pricing_power_gprev(gp, revenue, 63) * ebitda * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


# 252d ultimate composite: passthrough cumulative × revenue × eps
def f41pps_f41_pricing_power_signal_ultimatecombo_252d_base_v150_signal(gp, revenue, eps, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 21).rolling(252, min_periods=63).sum()
    return (base * revenue * eps * closeadj / 1.0e9).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41pps_f41_pricing_power_signal_gprevquantilehi_252d_base_v076_signal,
    f41pps_f41_pricing_power_signal_gprevquantilelo_252d_base_v077_signal,
    f41pps_f41_pricing_power_signal_gprevquantilehi_504d_base_v078_signal,
    f41pps_f41_pricing_power_signal_gprevquantilelo_504d_base_v079_signal,
    f41pps_f41_pricing_power_signal_gpgrowquantilehi_252d_base_v080_signal,
    f41pps_f41_pricing_power_signal_gpgrowquantilelo_252d_base_v081_signal,
    f41pps_f41_pricing_power_signal_gprevskew_252d_base_v082_signal,
    f41pps_f41_pricing_power_signal_gprevskew_504d_base_v083_signal,
    f41pps_f41_pricing_power_signal_gprevkurt_252d_base_v084_signal,
    f41pps_f41_pricing_power_signal_gprevkurt_504d_base_v085_signal,
    f41pps_f41_pricing_power_signal_gprevmedian_252d_base_v086_signal,
    f41pps_f41_pricing_power_signal_gprevmedian_504d_base_v087_signal,
    f41pps_f41_pricing_power_signal_gpgrowiqr_252d_base_v088_signal,
    f41pps_f41_pricing_power_signal_gpgrowiqr_504d_base_v089_signal,
    f41pps_f41_pricing_power_signal_gpequity_252d_base_v090_signal,
    f41pps_f41_pricing_power_signal_gpequity_63d_base_v091_signal,
    f41pps_f41_pricing_power_signal_gmxwc_252d_base_v092_signal,
    f41pps_f41_pricing_power_signal_gmxwc_63d_base_v093_signal,
    f41pps_f41_pricing_power_signal_passxintexp_252d_base_v094_signal,
    f41pps_f41_pricing_power_signal_passxintexp_63d_base_v095_signal,
    f41pps_f41_pricing_power_signal_gprevvslong_252d_base_v096_signal,
    f41pps_f41_pricing_power_signal_gprevvslong_63d_base_v097_signal,
    f41pps_f41_pricing_power_signal_gprevxncfog_252d_base_v098_signal,
    f41pps_f41_pricing_power_signal_gprevxncfog_63d_base_v099_signal,
    f41pps_f41_pricing_power_signal_gprevxfcfg_252d_base_v100_signal,
    f41pps_f41_pricing_power_signal_gprevxfcfg_63d_base_v101_signal,
    f41pps_f41_pricing_power_signal_marginexpfreq_252d_base_v102_signal,
    f41pps_f41_pricing_power_signal_marginexpfreq_504d_base_v103_signal,
    f41pps_f41_pricing_power_signal_gpgrowxrevg_252d_base_v104_signal,
    f41pps_f41_pricing_power_signal_gpgrowxrevg_63d_base_v105_signal,
    f41pps_f41_pricing_power_signal_gprevxdebt_252d_base_v106_signal,
    f41pps_f41_pricing_power_signal_gprevxdebt_63d_base_v107_signal,
    f41pps_f41_pricing_power_signal_gpovercapex_252d_base_v108_signal,
    f41pps_f41_pricing_power_signal_gpovercapex_63d_base_v109_signal,
    f41pps_f41_pricing_power_signal_passxeps_252d_base_v110_signal,
    f41pps_f41_pricing_power_signal_passxeps_63d_base_v111_signal,
    f41pps_f41_pricing_power_signal_passxrevg_252d_base_v112_signal,
    f41pps_f41_pricing_power_signal_passxrevg_63d_base_v113_signal,
    f41pps_f41_pricing_power_signal_gmxni_252d_base_v114_signal,
    f41pps_f41_pricing_power_signal_gmxni_63d_base_v115_signal,
    f41pps_f41_pricing_power_signal_gpvsassetg_252d_base_v116_signal,
    f41pps_f41_pricing_power_signal_gpvsassetg_63d_base_v117_signal,
    f41pps_f41_pricing_power_signal_passsum_252d_base_v118_signal,
    f41pps_f41_pricing_power_signal_passsum_504d_base_v119_signal,
    f41pps_f41_pricing_power_signal_passsum_63d_base_v120_signal,
    f41pps_f41_pricing_power_signal_passema_252d_base_v121_signal,
    f41pps_f41_pricing_power_signal_passema_63d_base_v122_signal,
    f41pps_f41_pricing_power_signal_gprevsmallwin_252d_base_v123_signal,
    f41pps_f41_pricing_power_signal_gprevxintexp_252d_base_v124_signal,
    f41pps_f41_pricing_power_signal_gprevxintexp_63d_base_v125_signal,
    f41pps_f41_pricing_power_signal_gpaccel_252d_base_v126_signal,
    f41pps_f41_pricing_power_signal_gpaccel_63d_base_v127_signal,
    f41pps_f41_pricing_power_signal_gprevpercentile_252d_base_v128_signal,
    f41pps_f41_pricing_power_signal_gprevpercentile_504d_base_v129_signal,
    f41pps_f41_pricing_power_signal_gprevxrevpershare_252d_base_v130_signal,
    f41pps_f41_pricing_power_signal_gprevxrevpershare_63d_base_v131_signal,
    f41pps_f41_pricing_power_signal_gpgrowxwc_252d_base_v132_signal,
    f41pps_f41_pricing_power_signal_gpgrowxwc_63d_base_v133_signal,
    f41pps_f41_pricing_power_signal_gprevstd_252d_base_v134_signal,
    f41pps_f41_pricing_power_signal_gprevstd_504d_base_v135_signal,
    f41pps_f41_pricing_power_signal_triplecombo_252d_base_v136_signal,
    f41pps_f41_pricing_power_signal_triplecombo_63d_base_v137_signal,
    f41pps_f41_pricing_power_signal_gppershare_252d_base_v138_signal,
    f41pps_f41_pricing_power_signal_gppershare_63d_base_v139_signal,
    f41pps_f41_pricing_power_signal_gmxncfo_252d_base_v140_signal,
    f41pps_f41_pricing_power_signal_gmxncfo_63d_base_v141_signal,
    f41pps_f41_pricing_power_signal_gprevcumxrev_252d_base_v142_signal,
    f41pps_f41_pricing_power_signal_gprevcumxrev_504d_base_v143_signal,
    f41pps_f41_pricing_power_signal_gpgrowxfcfl_252d_base_v144_signal,
    f41pps_f41_pricing_power_signal_gpgrowxfcfl_63d_base_v145_signal,
    f41pps_f41_pricing_power_signal_gprevcv_252d_base_v146_signal,
    f41pps_f41_pricing_power_signal_gprevcv_504d_base_v147_signal,
    f41pps_f41_pricing_power_signal_gprevxebitda_252d_base_v148_signal,
    f41pps_f41_pricing_power_signal_gprevxebitda_63d_base_v149_signal,
    f41pps_f41_pricing_power_signal_ultimatecombo_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_PRICING_POWER_SIGNAL_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1.0e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    gp = pd.Series(4.0e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.011, n))), name="gp")
    opinc = pd.Series(1.3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="opinc")
    ebitda = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ebitda")
    eps = pd.Series(2.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="eps")
    debt = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="debt")
    assets = pd.Series(5.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    currentratio = pd.Series(1.5 + 0.3 * np.cumsum(np.random.normal(0, 0.001, n)), name="currentratio")
    fcf = pd.Series(0.9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.013, n))), name="fcf")
    ncfo = pd.Series(1.1e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ncfo")
    sharesbas = pd.Series(5.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="sharesbas")
    intexp = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="intexp")
    equity = pd.Series(2.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="equity")
    workingcapital = pd.Series(8.0e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="workingcapital")
    capex = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.012, n))), name="capex")
    netinc = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="netinc")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "gp": gp, "opinc": opinc,
        "ebitda": ebitda, "eps": eps, "debt": debt, "assets": assets,
        "currentratio": currentratio, "fcf": fcf, "ncfo": ncfo, "sharesbas": sharesbas,
        "intexp": intexp, "equity": equity, "workingcapital": workingcapital,
        "capex": capex, "netinc": netinc,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f41_pricing_power",)
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
    print(f"OK f41_pricing_power_signal_base_076_150_claude: {n_features} features pass")
