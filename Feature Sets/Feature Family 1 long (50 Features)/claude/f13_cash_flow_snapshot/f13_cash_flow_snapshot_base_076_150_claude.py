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


# ===== folder domain primitives =====
def _f13_cashflow_snapshot_scaled(cf, scale):
    return cf / scale.replace(0, np.nan).abs()


def _f13_cashflow_snapshot_log(cf):
    return np.log(cf.abs().replace(0, np.nan))


def _f13_fcf_quality(fcf, ncfo):
    return fcf / ncfo.replace(0, np.nan).abs()


def _f13_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan).abs()


def _f13_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan).abs()


def _f13_cashflow_snapshot_per_share(cf, sharesbas):
    return cf / sharesbas.replace(0, np.nan).abs()


# 21d FCF/marketcap times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomc_21d_base_v076_signal(fcf, marketcap, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d OCF/marketcap times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftomc_21d_base_v077_signal(ncfo, marketcap, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF/marketcap times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftomc_504d_base_v078_signal(ncfo, marketcap, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, marketcap), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF/marketcap times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomc_504d_base_v079_signal(fcf, marketcap, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, marketcap), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF quality times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfquality_504d_base_v080_signal(fcf, ncfo, closeadj):
    result = _mean(_f13_fcf_quality(fcf, ncfo), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF quality times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfquality_21d_base_v081_signal(fcf, ncfo, closeadj):
    result = _mean(_f13_fcf_quality(fcf, ncfo), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF/assets times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoassets_504d_base_v082_signal(fcf, assets, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF/assets times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoassets_504d_base_v083_signal(ncfo, assets, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF/equity times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoequity_504d_base_v084_signal(fcf, equity, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, equity), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF/equity times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoequity_504d_base_v085_signal(ncfo, equity, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, equity), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF/debt times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftodebt_504d_base_v086_signal(fcf, debt, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, debt), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF/debt times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftodebt_504d_base_v087_signal(ncfo, debt, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, debt), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF margin EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginema_504d_base_v088_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF margin EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginema_504d_base_v089_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF margin EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginema_21d_base_v090_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d OCF margin EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginema_21d_base_v091_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfema_63d_base_v092_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfema_504d_base_v093_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d OCF EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfema_21d_base_v094_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfema_504d_base_v095_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF margin median times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmed_504d_base_v096_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF margin median times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginmed_504d_base_v097_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = base.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF margin skew times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginskew_504d_base_v098_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF margin kurt times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginkurt_504d_base_v099_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.rolling(504, min_periods=126).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF margin skew times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginskew_504d_base_v100_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF/marketcap rank times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomcrank_504d_base_v101_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, marketcap)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF/marketcap rank times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftomcrank_252d_base_v102_signal(ncfo, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(ncfo, marketcap)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF/equity rank times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoequityrank_504d_base_v103_signal(fcf, equity, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, equity)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF/assets rank times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoassetsrank_504d_base_v104_signal(fcf, assets, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, assets)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF margin std times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginstd_504d_base_v105_signal(fcf, revenue, closeadj):
    result = _std(_f13_fcf_margin(fcf, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF margin std times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginstd_504d_base_v106_signal(ncfo, revenue, closeadj):
    result = _std(_f13_ocf_margin(ncfo, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF z 504d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfz_504d_base_v107_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF z 504d times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfz_504d_base_v108_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF/marketcap times sqrt(252) annualized times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomcann_252d_base_v109_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, marketcap)
    result = _mean(base, 252) * np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF margin annualized times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginann_252d_base_v110_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = _mean(base, 252) * np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfema_21d_base_v111_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log FCF + log OCF composite x closeadj 21d
def f13cfs_f13_cash_flow_snapshot_logfcfplusocf_21d_base_v112_signal(fcf, ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) + _f13_cashflow_snapshot_log(ncfo)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log FCF * log OCF composite 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_logfcfxlogocf_252d_base_v113_signal(fcf, ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) * _f13_cashflow_snapshot_log(ncfo)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log FCF * log marketcap composite times closeadj
def f13cfs_f13_cash_flow_snapshot_logfcfxlogmc_252d_base_v114_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) * np.log(marketcap.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj * 1e-3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log FCF - log debt composite times closeadj
def f13cfs_f13_cash_flow_snapshot_logfcfminusdebt_252d_base_v115_signal(fcf, debt, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) - np.log(debt.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log OCF - log debt composite times closeadj
def f13cfs_f13_cash_flow_snapshot_logocfminusdebt_252d_base_v116_signal(ncfo, debt, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo) - np.log(debt.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log FCF - log assets composite times closeadj
def f13cfs_f13_cash_flow_snapshot_logfcfminusassets_252d_base_v117_signal(fcf, assets, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) - np.log(assets.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF/(assets+debt) times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftolevbase_252d_base_v118_signal(fcf, assets, debt, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, assets + debt)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF/(equity+debt+marketcap) times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftototalcap_252d_base_v119_signal(ncfo, equity, debt, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(ncfo, equity + debt + marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF/(assets+debt) times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftolevbase_63d_base_v120_signal(fcf, assets, debt, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, assets + debt)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF skew times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfskew_504d_base_v121_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF kurtosis times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfkurt_504d_base_v122_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo)
    result = base.rolling(504, min_periods=126).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF margin minimum times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmin_63d_base_v123_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin maximum times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmax_252d_base_v124_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF margin maximum times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginmax_252d_base_v125_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin minimum times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmin_252d_base_v126_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count days FCF/marketcap > 0.05 times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomcabove5_504d_base_v127_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, marketcap)
    result = (base).rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count days OCF/marketcap > 0.10 times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftomcabove10_504d_base_v128_signal(ncfo, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(ncfo, marketcap)
    result = (base).rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count days FCF margin > rolling mean
def f13cfs_f13_cash_flow_snapshot_fcfmarginabovemean_504d_base_v129_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    flag = (base > _mean(base, 504)).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF * netinc composite times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfxni_252d_base_v130_signal(fcf, netinc, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) * np.log(netinc.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF * netinc composite times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfxni_252d_base_v131_signal(ncfo, netinc, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo) * np.log(netinc.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF / netinc (cash conversion to ni) times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoni_63d_base_v132_signal(fcf, netinc, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, netinc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF / netinc times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoni_252d_base_v133_signal(fcf, netinc, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, netinc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF / netinc times closeadj (Earnings quality)
def f13cfs_f13_cash_flow_snapshot_ocftoni_252d_base_v134_signal(ncfo, netinc, closeadj):
    base = _f13_cashflow_snapshot_scaled(ncfo, netinc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF margin x revenue scale composite times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginxrev_63d_base_v135_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue) * np.log(revenue.abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin x revenue scale composite times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginxrev_252d_base_v136_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue) * np.log(revenue.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF margin x revenue composite times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginxrev_252d_base_v137_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue) * np.log(revenue.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# FCF / (debt + marketcap) (FCF yield to enterprise) 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoev_252d_base_v138_signal(fcf, debt, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, debt + marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# OCF / (debt + marketcap) 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoev_252d_base_v139_signal(ncfo, debt, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(ncfo, debt + marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF/(debt+marketcap) zscore times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoevz_504d_base_v140_signal(fcf, debt, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, debt + marketcap)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin per share 21d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfpsxrev_21d_base_v141_signal(fcf, sharesbas, revenue, closeadj):
    base = _f13_cashflow_snapshot_per_share(fcf, sharesbas) * np.log(revenue.abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# OCF per share x revenue 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfpsxrev_252d_base_v142_signal(ncfo, sharesbas, revenue, closeadj):
    base = _f13_cashflow_snapshot_per_share(ncfo, sharesbas) * np.log(revenue.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF / ebitda (cash conversion) times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoebitda_252d_base_v143_signal(fcf, ebitda, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, ebitda)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF / ebitda times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoebitda_252d_base_v144_signal(ncfo, ebitda, closeadj):
    base = _f13_cashflow_snapshot_scaled(ncfo, ebitda)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF / opinc times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoopinc_252d_base_v145_signal(fcf, opinc, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, opinc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF / opinc times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoopinc_252d_base_v146_signal(ncfo, opinc, closeadj):
    base = _f13_cashflow_snapshot_scaled(ncfo, opinc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin EWM 63d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginema_63d_base_v147_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF margin EWM 63d times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginema_63d_base_v148_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF + OCF + netinc composite scaled by revenue times closeadj
def f13cfs_f13_cash_flow_snapshot_cashearnings_252d_base_v149_signal(fcf, ncfo, netinc, revenue, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf + ncfo + netinc, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF + OCF composite scaled by revenue times closeadj
def f13cfs_f13_cash_flow_snapshot_cashearnings_63d_base_v150_signal(fcf, ncfo, revenue, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf + ncfo, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13cfs_f13_cash_flow_snapshot_fcftomc_21d_base_v076_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomc_21d_base_v077_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomc_504d_base_v078_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomc_504d_base_v079_signal,
    f13cfs_f13_cash_flow_snapshot_fcfquality_504d_base_v080_signal,
    f13cfs_f13_cash_flow_snapshot_fcfquality_21d_base_v081_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoassets_504d_base_v082_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoassets_504d_base_v083_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoequity_504d_base_v084_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoequity_504d_base_v085_signal,
    f13cfs_f13_cash_flow_snapshot_fcftodebt_504d_base_v086_signal,
    f13cfs_f13_cash_flow_snapshot_ocftodebt_504d_base_v087_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginema_504d_base_v088_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginema_504d_base_v089_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginema_21d_base_v090_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginema_21d_base_v091_signal,
    f13cfs_f13_cash_flow_snapshot_fcfema_63d_base_v092_signal,
    f13cfs_f13_cash_flow_snapshot_fcfema_504d_base_v093_signal,
    f13cfs_f13_cash_flow_snapshot_ocfema_21d_base_v094_signal,
    f13cfs_f13_cash_flow_snapshot_ocfema_504d_base_v095_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmed_504d_base_v096_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginmed_504d_base_v097_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginskew_504d_base_v098_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginkurt_504d_base_v099_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginskew_504d_base_v100_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcrank_504d_base_v101_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomcrank_252d_base_v102_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoequityrank_504d_base_v103_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoassetsrank_504d_base_v104_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginstd_504d_base_v105_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginstd_504d_base_v106_signal,
    f13cfs_f13_cash_flow_snapshot_fcfz_504d_base_v107_signal,
    f13cfs_f13_cash_flow_snapshot_ocfz_504d_base_v108_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcann_252d_base_v109_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginann_252d_base_v110_signal,
    f13cfs_f13_cash_flow_snapshot_fcfema_21d_base_v111_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfplusocf_21d_base_v112_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfxlogocf_252d_base_v113_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfxlogmc_252d_base_v114_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfminusdebt_252d_base_v115_signal,
    f13cfs_f13_cash_flow_snapshot_logocfminusdebt_252d_base_v116_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfminusassets_252d_base_v117_signal,
    f13cfs_f13_cash_flow_snapshot_fcftolevbase_252d_base_v118_signal,
    f13cfs_f13_cash_flow_snapshot_ocftototalcap_252d_base_v119_signal,
    f13cfs_f13_cash_flow_snapshot_fcftolevbase_63d_base_v120_signal,
    f13cfs_f13_cash_flow_snapshot_fcfskew_504d_base_v121_signal,
    f13cfs_f13_cash_flow_snapshot_ocfkurt_504d_base_v122_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmin_63d_base_v123_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmax_252d_base_v124_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginmax_252d_base_v125_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmin_252d_base_v126_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcabove5_504d_base_v127_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomcabove10_504d_base_v128_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginabovemean_504d_base_v129_signal,
    f13cfs_f13_cash_flow_snapshot_fcfxni_252d_base_v130_signal,
    f13cfs_f13_cash_flow_snapshot_ocfxni_252d_base_v131_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoni_63d_base_v132_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoni_252d_base_v133_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoni_252d_base_v134_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginxrev_63d_base_v135_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginxrev_252d_base_v136_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginxrev_252d_base_v137_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoev_252d_base_v138_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoev_252d_base_v139_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoevz_504d_base_v140_signal,
    f13cfs_f13_cash_flow_snapshot_fcfpsxrev_21d_base_v141_signal,
    f13cfs_f13_cash_flow_snapshot_ocfpsxrev_252d_base_v142_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoebitda_252d_base_v143_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoebitda_252d_base_v144_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoopinc_252d_base_v145_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoopinc_252d_base_v146_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginema_63d_base_v147_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginema_63d_base_v148_signal,
    f13cfs_f13_cash_flow_snapshot_cashearnings_252d_base_v149_signal,
    f13cfs_f13_cash_flow_snapshot_cashearnings_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_CASH_FLOW_SNAPSHOT_REGISTRY_076_150 = REGISTRY


def _build_log_walk(seed_offset, base_val, drift, vol, n):
    rs = np.random.RandomState(42 + seed_offset)
    return base_val * np.exp(np.cumsum(rs.normal(drift, vol, n)))


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(_build_log_walk(0, 5e8, 0.0003, 0.005, n), name="revenue")
    netinc = pd.Series(_build_log_walk(1, 5e7, 0.0002, 0.008, n), name="netinc")
    fcf = pd.Series(_build_log_walk(2, 4e7, 0.0002, 0.009, n), name="fcf")
    ncfo = pd.Series(_build_log_walk(3, 6e7, 0.0002, 0.008, n), name="ncfo")
    equity = pd.Series(_build_log_walk(4, 1e9, 0.0002, 0.004, n), name="equity")
    debt = pd.Series(_build_log_walk(5, 4e8, 0.0001, 0.005, n), name="debt")
    assets = pd.Series(_build_log_walk(6, 2e9, 0.0002, 0.003, n), name="assets")
    ebitda = pd.Series(_build_log_walk(7, 1.2e8, 0.0002, 0.007, n), name="ebitda")
    capex = pd.Series(_build_log_walk(8, 3e7, 0.0002, 0.01, n), name="capex")
    eps = pd.Series(_build_log_walk(9, 2.0, 0.0002, 0.008, n), name="eps")
    sharesbas = pd.Series(_build_log_walk(10, 5e7, 0.0001, 0.002, n), name="sharesbas")
    opinc = pd.Series(_build_log_walk(11, 8e7, 0.0002, 0.007, n), name="opinc")
    gp = pd.Series(_build_log_walk(12, 2e8, 0.0002, 0.006, n), name="gp")
    workingcapital = pd.Series(_build_log_walk(13, 2e8, 0.0002, 0.006, n), name="workingcapital")
    currentratio = pd.Series(_build_log_walk(14, 1.8, 0.0001, 0.004, n), name="currentratio")
    retearn = pd.Series(_build_log_walk(15, 5e8, 0.0002, 0.005, n), name="retearn")
    intexp = pd.Series(_build_log_walk(17, 1e7, 0.0001, 0.008, n), name="intexp")
    liabilities = pd.Series(_build_log_walk(18, 1e9, 0.0001, 0.004, n), name="liabilities")
    closeadj = pd.Series(_build_log_walk(19, 100.0, 0.0005, 0.02, n), name="closeadj")
    marketcap = closeadj * 1e7
    marketcap.name = "marketcap"

    cols = {
        "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
        "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda,
        "capex": capex, "eps": eps, "sharesbas": sharesbas, "opinc": opinc,
        "gp": gp, "workingcapital": workingcapital, "currentratio": currentratio,
        "retearn": retearn, "intexp": intexp,
        "liabilities": liabilities, "closeadj": closeadj, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f13_cashflow_snapshot_scaled", "_f13_cashflow_snapshot_log",
                         "_f13_fcf_quality", "_f13_fcf_margin", "_f13_ocf_margin",
                         "_f13_cashflow_snapshot_per_share")
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
    print(f"OK f13_cash_flow_snapshot_base_076_150_claude: {n_features} features pass")
