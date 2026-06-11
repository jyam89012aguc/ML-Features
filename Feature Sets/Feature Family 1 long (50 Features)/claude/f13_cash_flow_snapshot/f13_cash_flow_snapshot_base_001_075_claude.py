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


# 21d FCF margin times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_21d_base_v001_signal(fcf, revenue, closeadj):
    result = _mean(_f13_fcf_margin(fcf, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF margin times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_63d_base_v002_signal(fcf, revenue, closeadj):
    result = _mean(_f13_fcf_margin(fcf, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_252d_base_v003_signal(fcf, revenue, closeadj):
    result = _mean(_f13_fcf_margin(fcf, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF margin times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_504d_base_v004_signal(fcf, revenue, closeadj):
    result = _mean(_f13_fcf_margin(fcf, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d OCF margin times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmargin_21d_base_v005_signal(ncfo, revenue, closeadj):
    result = _mean(_f13_ocf_margin(ncfo, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d OCF margin times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmargin_63d_base_v006_signal(ncfo, revenue, closeadj):
    result = _mean(_f13_ocf_margin(ncfo, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF margin times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmargin_252d_base_v007_signal(ncfo, revenue, closeadj):
    result = _mean(_f13_ocf_margin(ncfo, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF margin times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmargin_504d_base_v008_signal(ncfo, revenue, closeadj):
    result = _mean(_f13_ocf_margin(ncfo, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF/marketcap times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomc_63d_base_v009_signal(fcf, marketcap, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF/marketcap (FCF yield) times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomc_252d_base_v010_signal(fcf, marketcap, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF/marketcap times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftomc_252d_base_v011_signal(ncfo, marketcap, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# FCF quality (FCF/OCF) 63d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfquality_63d_base_v012_signal(fcf, ncfo, closeadj):
    result = _mean(_f13_fcf_quality(fcf, ncfo), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# FCF quality 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfquality_252d_base_v013_signal(fcf, ncfo, closeadj):
    result = _mean(_f13_fcf_quality(fcf, ncfo), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF/assets times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoassets_63d_base_v014_signal(fcf, assets, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF/assets times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoassets_252d_base_v015_signal(fcf, assets, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF/assets times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoassets_252d_base_v016_signal(ncfo, assets, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF/equity times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoequity_252d_base_v017_signal(fcf, equity, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF/equity times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoequity_252d_base_v018_signal(ncfo, equity, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF/debt (debt service) times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftodebt_252d_base_v019_signal(fcf, debt, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, debt), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF/debt times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftodebt_252d_base_v020_signal(ncfo, debt, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, debt), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log FCF (smoothed 63d) times closeadj
def f13cfs_f13_cash_flow_snapshot_logfcf_63d_base_v021_signal(fcf, closeadj):
    result = _mean(_f13_cashflow_snapshot_log(fcf), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log FCF 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_logfcf_252d_base_v022_signal(fcf, closeadj):
    result = _mean(_f13_cashflow_snapshot_log(fcf), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log OCF 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_logocf_252d_base_v023_signal(ncfo, closeadj):
    result = _mean(_f13_cashflow_snapshot_log(ncfo), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF margin std times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginstd_63d_base_v024_signal(fcf, revenue, closeadj):
    result = _std(_f13_fcf_margin(fcf, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin std times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginstd_252d_base_v025_signal(fcf, revenue, closeadj):
    result = _std(_f13_fcf_margin(fcf, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF margin std times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginstd_252d_base_v026_signal(ncfo, revenue, closeadj):
    result = _std(_f13_ocf_margin(ncfo, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin zscore times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginz_252d_base_v027_signal(fcf, revenue, closeadj):
    result = _z(_f13_fcf_margin(fcf, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF margin zscore times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginz_252d_base_v028_signal(ncfo, revenue, closeadj):
    result = _z(_f13_ocf_margin(ncfo, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF/marketcap zscore times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomcz_504d_base_v029_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, marketcap)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF quality zscore times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfqualityz_504d_base_v030_signal(fcf, ncfo, closeadj):
    result = _z(_f13_fcf_quality(fcf, ncfo), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF per share times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfps_21d_base_v031_signal(fcf, sharesbas, closeadj):
    result = _mean(_f13_cashflow_snapshot_per_share(fcf, sharesbas), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF per share times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfps_252d_base_v032_signal(fcf, sharesbas, closeadj):
    result = _mean(_f13_cashflow_snapshot_per_share(fcf, sharesbas), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d OCF per share times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfps_21d_base_v033_signal(ncfo, sharesbas, closeadj):
    result = _mean(_f13_cashflow_snapshot_per_share(ncfo, sharesbas), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF per share times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfps_252d_base_v034_signal(ncfo, sharesbas, closeadj):
    result = _mean(_f13_cashflow_snapshot_per_share(ncfo, sharesbas), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin sq 252d (severity) times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginsq_252d_base_v035_signal(fcf, revenue, closeadj):
    fm = _f13_fcf_margin(fcf, revenue)
    result = _mean(fm * fm.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin sq 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginsq_252d_base_v036_signal(ncfo, revenue, closeadj):
    om = _f13_ocf_margin(ncfo, revenue)
    result = _mean(om * om.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF EMA times closeadj (level)
def f13cfs_f13_cash_flow_snapshot_fcfema_21d_base_v037_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfema_252d_base_v038_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF EMA times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfema_252d_base_v039_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin EMA 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginema_252d_base_v040_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin EMA 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginema_252d_base_v041_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin median times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmed_252d_base_v042_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF margin median times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginmed_252d_base_v043_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF margin rank times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginrank_504d_base_v044_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d OCF margin rank times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginrank_504d_base_v045_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count days FCF margin > 0.05 over 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginabove5_252d_base_v046_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = (base).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count days FCF margin > 0.10 over 504d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginabove10_504d_base_v047_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = (base).rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count days OCF margin > 0.10 over 504d times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginabove10_504d_base_v048_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    result = (base).rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count days FCF/marketcap > 0.05 over 252d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomcabove5_252d_base_v049_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, marketcap)
    result = (base).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin x marketcap composite times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginxmc_252d_base_v050_signal(fcf, revenue, marketcap, closeadj):
    base = _f13_fcf_margin(fcf, revenue) * np.log(marketcap.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF margin x marketcap composite times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginxmc_252d_base_v051_signal(ncfo, revenue, marketcap, closeadj):
    base = _f13_ocf_margin(ncfo, revenue) * np.log(marketcap.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF expanding mean x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfexp_base_v052_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF margin expanding mean x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginexp_base_v053_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = base.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF / capex (cash conversion to capex) times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftocapex_252d_base_v054_signal(fcf, capex, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, capex), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF / capex times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftocapex_252d_base_v055_signal(ncfo, capex, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, capex), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF / liabilities times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoliab_252d_base_v056_signal(fcf, liabilities, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(fcf, liabilities), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF / liabilities times closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoliab_252d_base_v057_signal(ncfo, liabilities, closeadj):
    result = _mean(_f13_cashflow_snapshot_scaled(ncfo, liabilities), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF rank vs prior 252 times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfrank_252d_base_v058_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF rank times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfrank_504d_base_v059_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF skewness times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfskew_252d_base_v060_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF skewness times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfskew_252d_base_v061_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF kurtosis times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfkurt_252d_base_v062_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF IQR times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfiqr_252d_base_v063_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    q3 = base.rolling(252, min_periods=63).quantile(0.75)
    q1 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q3 - q1) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF minimum times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmin_252d_base_v064_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF max times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmax_252d_base_v065_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OCF anomaly times closeadj
def f13cfs_f13_cash_flow_snapshot_ocfanomaly_252d_base_v066_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF anomaly times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfanomaly_252d_base_v067_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF + OCF composite log times closeadj
def f13cfs_f13_cash_flow_snapshot_cfsum_252d_base_v068_signal(fcf, ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) + _f13_cashflow_snapshot_log(ncfo)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF + OCF composite times closeadj
def f13cfs_f13_cash_flow_snapshot_cfsum_63d_base_v069_signal(fcf, ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) + _f13_cashflow_snapshot_log(ncfo)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin annualized times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginann_252d_base_v070_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    result = _mean(base, 252) * np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF/sqrt(assets) times closeadj
def f13cfs_f13_cash_flow_snapshot_fcftosqrtassets_252d_base_v071_signal(fcf, assets, closeadj):
    sa = np.sqrt(assets.abs().replace(0, np.nan))
    base = _f13_cashflow_snapshot_scaled(fcf, sa)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF * marketcap rank composite times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfxmclog_252d_base_v072_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) * np.log(marketcap.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj * 1e-3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF margin x marketcap composite times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginxmc_63d_base_v073_signal(fcf, revenue, marketcap, closeadj):
    base = _f13_fcf_margin(fcf, revenue) * np.log(marketcap.abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# OCF/sharesbas (per share OCF) 21d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfps_63d_base_v074_signal(ncfo, sharesbas, closeadj):
    result = _mean(_f13_cashflow_snapshot_per_share(ncfo, sharesbas), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# FCF/sharesbas 63d times closeadj
def f13cfs_f13_cash_flow_snapshot_fcfps_63d_base_v075_signal(fcf, sharesbas, closeadj):
    result = _mean(_f13_cashflow_snapshot_per_share(fcf, sharesbas), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13cfs_f13_cash_flow_snapshot_fcfmargin_21d_base_v001_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmargin_63d_base_v002_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmargin_252d_base_v003_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmargin_504d_base_v004_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmargin_21d_base_v005_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmargin_63d_base_v006_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmargin_252d_base_v007_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmargin_504d_base_v008_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomc_63d_base_v009_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomc_252d_base_v010_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomc_252d_base_v011_signal,
    f13cfs_f13_cash_flow_snapshot_fcfquality_63d_base_v012_signal,
    f13cfs_f13_cash_flow_snapshot_fcfquality_252d_base_v013_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoassets_63d_base_v014_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoassets_252d_base_v015_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoassets_252d_base_v016_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoequity_252d_base_v017_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoequity_252d_base_v018_signal,
    f13cfs_f13_cash_flow_snapshot_fcftodebt_252d_base_v019_signal,
    f13cfs_f13_cash_flow_snapshot_ocftodebt_252d_base_v020_signal,
    f13cfs_f13_cash_flow_snapshot_logfcf_63d_base_v021_signal,
    f13cfs_f13_cash_flow_snapshot_logfcf_252d_base_v022_signal,
    f13cfs_f13_cash_flow_snapshot_logocf_252d_base_v023_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginstd_63d_base_v024_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginstd_252d_base_v025_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginstd_252d_base_v026_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginz_252d_base_v027_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginz_252d_base_v028_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcz_504d_base_v029_signal,
    f13cfs_f13_cash_flow_snapshot_fcfqualityz_504d_base_v030_signal,
    f13cfs_f13_cash_flow_snapshot_fcfps_21d_base_v031_signal,
    f13cfs_f13_cash_flow_snapshot_fcfps_252d_base_v032_signal,
    f13cfs_f13_cash_flow_snapshot_ocfps_21d_base_v033_signal,
    f13cfs_f13_cash_flow_snapshot_ocfps_252d_base_v034_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginsq_252d_base_v035_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginsq_252d_base_v036_signal,
    f13cfs_f13_cash_flow_snapshot_fcfema_21d_base_v037_signal,
    f13cfs_f13_cash_flow_snapshot_fcfema_252d_base_v038_signal,
    f13cfs_f13_cash_flow_snapshot_ocfema_252d_base_v039_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginema_252d_base_v040_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginema_252d_base_v041_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmed_252d_base_v042_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginmed_252d_base_v043_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginrank_504d_base_v044_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginrank_504d_base_v045_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginabove5_252d_base_v046_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginabove10_504d_base_v047_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginabove10_504d_base_v048_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcabove5_252d_base_v049_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginxmc_252d_base_v050_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginxmc_252d_base_v051_signal,
    f13cfs_f13_cash_flow_snapshot_fcfexp_base_v052_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginexp_base_v053_signal,
    f13cfs_f13_cash_flow_snapshot_fcftocapex_252d_base_v054_signal,
    f13cfs_f13_cash_flow_snapshot_ocftocapex_252d_base_v055_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoliab_252d_base_v056_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoliab_252d_base_v057_signal,
    f13cfs_f13_cash_flow_snapshot_fcfrank_252d_base_v058_signal,
    f13cfs_f13_cash_flow_snapshot_fcfrank_504d_base_v059_signal,
    f13cfs_f13_cash_flow_snapshot_fcfskew_252d_base_v060_signal,
    f13cfs_f13_cash_flow_snapshot_ocfskew_252d_base_v061_signal,
    f13cfs_f13_cash_flow_snapshot_fcfkurt_252d_base_v062_signal,
    f13cfs_f13_cash_flow_snapshot_fcfiqr_252d_base_v063_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmin_252d_base_v064_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmax_252d_base_v065_signal,
    f13cfs_f13_cash_flow_snapshot_ocfanomaly_252d_base_v066_signal,
    f13cfs_f13_cash_flow_snapshot_fcfanomaly_252d_base_v067_signal,
    f13cfs_f13_cash_flow_snapshot_cfsum_252d_base_v068_signal,
    f13cfs_f13_cash_flow_snapshot_cfsum_63d_base_v069_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginann_252d_base_v070_signal,
    f13cfs_f13_cash_flow_snapshot_fcftosqrtassets_252d_base_v071_signal,
    f13cfs_f13_cash_flow_snapshot_fcfxmclog_252d_base_v072_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginxmc_63d_base_v073_signal,
    f13cfs_f13_cash_flow_snapshot_ocfps_63d_base_v074_signal,
    f13cfs_f13_cash_flow_snapshot_fcfps_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_CASH_FLOW_SNAPSHOT_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f13_cash_flow_snapshot_base_001_075_claude: {n_features} features pass")
