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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# 21d slope of 21d FCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_21d_slope_v001_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue), 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_21d_slope_v002_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue), 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_63d_slope_v003_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d FCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_63d_slope_v004_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue), 63) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d FCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_252d_slope_v005_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue), 252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_252d_slope_v006_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmargin_504d_slope_v007_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d OCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmargin_21d_slope_v008_signal(ncfo, revenue, closeadj):
    base = _mean(_f13_ocf_margin(ncfo, revenue), 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d OCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmargin_21d_slope_v009_signal(ncfo, revenue, closeadj):
    base = _mean(_f13_ocf_margin(ncfo, revenue), 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d OCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmargin_63d_slope_v010_signal(ncfo, revenue, closeadj):
    base = _mean(_f13_ocf_margin(ncfo, revenue), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmargin_252d_slope_v011_signal(ncfo, revenue, closeadj):
    base = _mean(_f13_ocf_margin(ncfo, revenue), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d OCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmargin_504d_slope_v012_signal(ncfo, revenue, closeadj):
    base = _mean(_f13_ocf_margin(ncfo, revenue), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF/marketcap x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomc_63d_slope_v013_signal(fcf, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, marketcap), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF/marketcap x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomc_252d_slope_v014_signal(fcf, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, marketcap), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OCF/marketcap x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftomc_252d_slope_v015_signal(ncfo, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, marketcap), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF quality x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfquality_63d_slope_v016_signal(fcf, ncfo, closeadj):
    base = _mean(_f13_fcf_quality(fcf, ncfo), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF quality x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfquality_252d_slope_v017_signal(fcf, ncfo, closeadj):
    base = _mean(_f13_fcf_quality(fcf, ncfo), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF/assets x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoassets_63d_slope_v018_signal(fcf, assets, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, assets), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF/assets x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoassets_252d_slope_v019_signal(fcf, assets, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, assets), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OCF/assets x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoassets_252d_slope_v020_signal(ncfo, assets, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, assets), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF/equity x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoequity_252d_slope_v021_signal(fcf, equity, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, equity), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OCF/equity x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoequity_252d_slope_v022_signal(ncfo, equity, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, equity), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF/debt x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftodebt_252d_slope_v023_signal(fcf, debt, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, debt), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OCF/debt x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftodebt_252d_slope_v024_signal(ncfo, debt, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, debt), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log FCF x closeadj
def f13cfs_f13_cash_flow_snapshot_logfcf_63d_slope_v025_signal(fcf, closeadj):
    base = _mean(_f13_cashflow_snapshot_log(fcf), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log FCF x closeadj
def f13cfs_f13_cash_flow_snapshot_logfcf_252d_slope_v026_signal(fcf, closeadj):
    base = _mean(_f13_cashflow_snapshot_log(fcf), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log OCF x closeadj
def f13cfs_f13_cash_flow_snapshot_logocf_252d_slope_v027_signal(ncfo, closeadj):
    base = _mean(_f13_cashflow_snapshot_log(ncfo), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF margin std x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginstd_63d_slope_v028_signal(fcf, revenue, closeadj):
    base = _std(_f13_fcf_margin(fcf, revenue), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF margin std x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginstd_252d_slope_v029_signal(fcf, revenue, closeadj):
    base = _std(_f13_fcf_margin(fcf, revenue), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OCF margin std x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginstd_252d_slope_v030_signal(ncfo, revenue, closeadj):
    base = _std(_f13_ocf_margin(ncfo, revenue), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF margin z 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginz_252d_slope_v031_signal(fcf, revenue, closeadj):
    base = _z(_f13_fcf_margin(fcf, revenue), 252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 21d slope of OCF margin z 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginz_252d_slope_v032_signal(ncfo, revenue, closeadj):
    base = _z(_f13_ocf_margin(ncfo, revenue), 252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/mc z 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomcz_504d_slope_v033_signal(fcf, marketcap, closeadj):
    base = _z(_f13_cashflow_snapshot_scaled(fcf, marketcap), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF quality z 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfqualityz_504d_slope_v034_signal(fcf, ncfo, closeadj):
    base = _z(_f13_fcf_quality(fcf, ncfo), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF per share x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfps_21d_slope_v035_signal(fcf, sharesbas, closeadj):
    base = _mean(_f13_cashflow_snapshot_per_share(fcf, sharesbas), 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF per share x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfps_252d_slope_v036_signal(fcf, sharesbas, closeadj):
    base = _mean(_f13_cashflow_snapshot_per_share(fcf, sharesbas), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d OCF per share x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfps_21d_slope_v037_signal(ncfo, sharesbas, closeadj):
    base = _mean(_f13_cashflow_snapshot_per_share(ncfo, sharesbas), 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OCF per share x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfps_252d_slope_v038_signal(ncfo, sharesbas, closeadj):
    base = _mean(_f13_cashflow_snapshot_per_share(ncfo, sharesbas), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF margin sq x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginsq_252d_slope_v039_signal(fcf, revenue, closeadj):
    fm = _f13_fcf_margin(fcf, revenue)
    base = _mean(fm * fm.abs(), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OCF margin sq x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginsq_252d_slope_v040_signal(ncfo, revenue, closeadj):
    om = _f13_ocf_margin(ncfo, revenue)
    base = _mean(om * om.abs(), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF EMA x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfema_21d_slope_v041_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF EMA x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfema_252d_slope_v042_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d OCF EMA x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfema_252d_slope_v043_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin EMA 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginema_252d_slope_v044_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin EMA 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginema_252d_slope_v045_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin median 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmed_252d_slope_v046_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).rolling(252, min_periods=63).median() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin median 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginmed_252d_slope_v047_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue).rolling(252, min_periods=63).median() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin rank 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginrank_504d_slope_v048_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).rolling(504, min_periods=126).rank(pct=True) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin rank 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginrank_504d_slope_v049_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue).rolling(504, min_periods=126).rank(pct=True) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of count days FCF margin > 5pct over 252d
def f13cfs_f13_cash_flow_snapshot_fcfmarginabove5_252d_slope_v050_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    flag = (base > 0.05).astype(float)
    b = flag.rolling(252, min_periods=63).sum() * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of count days FCF margin > 10pct over 504d
def f13cfs_f13_cash_flow_snapshot_fcfmarginabove10_504d_slope_v051_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    flag = (base > 0.10).astype(float)
    b = flag.rolling(504, min_periods=126).sum() * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of count days OCF margin > 10pct over 504d
def f13cfs_f13_cash_flow_snapshot_ocfmarginabove10_504d_slope_v052_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue)
    flag = (base > 0.10).astype(float)
    b = flag.rolling(504, min_periods=126).sum() * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of count days FCF/mc > 5pct over 252d
def f13cfs_f13_cash_flow_snapshot_fcftomcabove5_252d_slope_v053_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, marketcap)
    flag = (base > 0.05).astype(float)
    b = flag.rolling(252, min_periods=63).sum() * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin x mc 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginxmc_252d_slope_v054_signal(fcf, revenue, marketcap, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue) * np.log(marketcap.abs().replace(0, np.nan)), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin x mc 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginxmc_252d_slope_v055_signal(ncfo, revenue, marketcap, closeadj):
    base = _mean(_f13_ocf_margin(ncfo, revenue) * np.log(marketcap.abs().replace(0, np.nan)), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding FCF x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfexp_slope_v056_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).expanding(min_periods=63).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding FCF margin x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginexp_slope_v057_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).expanding(min_periods=63).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/capex 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftocapex_252d_slope_v058_signal(fcf, capex, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, capex), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF/capex 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftocapex_252d_slope_v059_signal(ncfo, capex, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, capex), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/liabilities 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoliab_252d_slope_v060_signal(fcf, liabilities, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, liabilities), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF/liabilities 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoliab_252d_slope_v061_signal(ncfo, liabilities, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, liabilities), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF rank 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfrank_252d_slope_v062_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF rank 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfrank_504d_slope_v063_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).rolling(504, min_periods=126).rank(pct=True) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF skew 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfskew_252d_slope_v064_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).rolling(252, min_periods=63).skew() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF skew 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfskew_252d_slope_v065_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo).rolling(252, min_periods=63).skew() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF kurt 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfkurt_252d_slope_v066_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).rolling(252, min_periods=63).kurt() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF IQR 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfiqr_252d_slope_v067_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    q3 = base.rolling(252, min_periods=63).quantile(0.75)
    q1 = base.rolling(252, min_periods=63).quantile(0.25)
    b = (q3 - q1) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF min 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmin_252d_slope_v068_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).rolling(252, min_periods=63).min() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF max 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmax_252d_slope_v069_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).rolling(252, min_periods=63).max() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF anomaly 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfanomaly_252d_slope_v070_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo)
    b = (base - _mean(base, 504)) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF anomaly 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfanomaly_252d_slope_v071_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf)
    b = (base - _mean(base, 504)) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF+OCF composite 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_cfsum_252d_slope_v072_signal(fcf, ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) + _f13_cashflow_snapshot_log(ncfo)
    b = _mean(base, 252) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF+OCF 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_cfsum_63d_slope_v073_signal(fcf, ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) + _f13_cashflow_snapshot_log(ncfo)
    b = _mean(base, 63) * closeadj
    return _slope_diff_norm(b, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin annualized 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginann_252d_slope_v074_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue), 252) * np.sqrt(252.0) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/sqrt(assets) 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftosqrtassets_252d_slope_v075_signal(fcf, assets, closeadj):
    sa = np.sqrt(assets.abs().replace(0, np.nan))
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, sa), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF * log(mc) 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfxmclog_252d_slope_v076_signal(fcf, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_log(fcf) * np.log(marketcap.abs().replace(0, np.nan)), 252) * closeadj * 1e-3
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF margin x mc 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginxmc_63d_slope_v077_signal(fcf, revenue, marketcap, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue) * np.log(marketcap.abs().replace(0, np.nan)), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 21d slope of OCF per share 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfps_63d_slope_v078_signal(ncfo, sharesbas, closeadj):
    base = _mean(_f13_cashflow_snapshot_per_share(ncfo, sharesbas), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF per share 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfps_63d_slope_v079_signal(fcf, sharesbas, closeadj):
    base = _mean(_f13_cashflow_snapshot_per_share(fcf, sharesbas), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF/mc x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomc_21d_slope_v080_signal(fcf, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, marketcap), 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d OCF/mc x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftomc_21d_slope_v081_signal(ncfo, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, marketcap), 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d OCF/mc x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftomc_504d_slope_v082_signal(ncfo, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, marketcap), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF/mc x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomc_504d_slope_v083_signal(fcf, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, marketcap), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF quality 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfquality_504d_slope_v084_signal(fcf, ncfo, closeadj):
    base = _mean(_f13_fcf_quality(fcf, ncfo), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF quality x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfquality_21d_slope_v085_signal(fcf, ncfo, closeadj):
    base = _mean(_f13_fcf_quality(fcf, ncfo), 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF/assets x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoassets_504d_slope_v086_signal(fcf, assets, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, assets), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d OCF/assets x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoassets_504d_slope_v087_signal(ncfo, assets, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, assets), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF/equity x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoequity_504d_slope_v088_signal(fcf, equity, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, equity), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d OCF/equity x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoequity_504d_slope_v089_signal(ncfo, equity, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, equity), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF/debt x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftodebt_504d_slope_v090_signal(fcf, debt, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, debt), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d OCF/debt x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftodebt_504d_slope_v091_signal(ncfo, debt, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, debt), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin EMA 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginema_504d_slope_v092_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).ewm(span=504, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin EMA 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginema_504d_slope_v093_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue).ewm(span=504, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 5d slope of FCF margin EMA 21d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginema_21d_slope_v094_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 5d slope of OCF margin EMA 21d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginema_21d_slope_v095_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF EMA 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfema_63d_slope_v096_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).ewm(span=63, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF EMA 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfema_504d_slope_v097_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).ewm(span=504, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 5d slope of OCF EMA 21d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfema_21d_slope_v098_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF EMA 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfema_504d_slope_v099_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo).ewm(span=504, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin median 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmed_504d_slope_v100_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).rolling(504, min_periods=126).median() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin median 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginmed_504d_slope_v101_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue).rolling(504, min_periods=126).median() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin skew 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginskew_504d_slope_v102_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).rolling(504, min_periods=126).skew() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin kurt 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginkurt_504d_slope_v103_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).rolling(504, min_periods=126).kurt() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin skew 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginskew_504d_slope_v104_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue).rolling(504, min_periods=126).skew() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/mc rank 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftomcrank_504d_slope_v105_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, marketcap).rolling(504, min_periods=126).rank(pct=True) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of OCF/mc rank 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftomcrank_252d_slope_v106_signal(ncfo, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(ncfo, marketcap).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/equity rank 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoequityrank_504d_slope_v107_signal(fcf, equity, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, equity).rolling(504, min_periods=126).rank(pct=True) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/assets rank 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoassetsrank_504d_slope_v108_signal(fcf, assets, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, assets).rolling(504, min_periods=126).rank(pct=True) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin std 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginstd_504d_slope_v109_signal(fcf, revenue, closeadj):
    base = _std(_f13_fcf_margin(fcf, revenue), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin std 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginstd_504d_slope_v110_signal(ncfo, revenue, closeadj):
    base = _std(_f13_ocf_margin(ncfo, revenue), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF z 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfz_504d_slope_v111_signal(fcf, closeadj):
    base = _z(_f13_cashflow_snapshot_log(fcf), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF z 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfz_504d_slope_v112_signal(ncfo, closeadj):
    base = _z(_f13_cashflow_snapshot_log(ncfo), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/mc annualized 252d
def f13cfs_f13_cash_flow_snapshot_fcftomcann_252d_slope_v113_signal(fcf, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, marketcap), 252) * np.sqrt(252.0) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin annualized 252d
def f13cfs_f13_cash_flow_snapshot_ocfmarginann_252d_slope_v114_signal(ncfo, revenue, closeadj):
    base = _mean(_f13_ocf_margin(ncfo, revenue), 252) * np.sqrt(252.0) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of log FCF + log OCF 21d x closeadj
def f13cfs_f13_cash_flow_snapshot_logfcfplusocf_21d_slope_v115_signal(fcf, ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) + _f13_cashflow_snapshot_log(ncfo)
    b = _mean(base, 21) * closeadj
    return _slope_diff_norm(b, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of log FCF * log OCF 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_logfcfxlogocf_252d_slope_v116_signal(fcf, ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) * _f13_cashflow_snapshot_log(ncfo)
    b = _mean(base, 252) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of log FCF x log mc 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_logfcfxlogmc_252d_slope_v117_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) * np.log(marketcap.abs().replace(0, np.nan))
    b = _mean(base, 252) * closeadj * 1e-3
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of log FCF - log debt 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_logfcfminusdebt_252d_slope_v118_signal(fcf, debt, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) - np.log(debt.abs().replace(0, np.nan))
    b = _mean(base, 252) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of log OCF - log debt 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_logocfminusdebt_252d_slope_v119_signal(ncfo, debt, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo) - np.log(debt.abs().replace(0, np.nan))
    b = _mean(base, 252) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of log FCF - log assets 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_logfcfminusassets_252d_slope_v120_signal(fcf, assets, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) - np.log(assets.abs().replace(0, np.nan))
    b = _mean(base, 252) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/(assets+debt) 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftolevbase_252d_slope_v121_signal(fcf, assets, debt, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, assets + debt), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF/total cap 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftototalcap_252d_slope_v122_signal(ncfo, equity, debt, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, equity + debt + marketcap), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF/(assets+debt) 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftolevbase_63d_slope_v123_signal(fcf, assets, debt, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, assets + debt), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF skew 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfskew_504d_slope_v124_signal(fcf, closeadj):
    base = _f13_cashflow_snapshot_log(fcf).rolling(504, min_periods=126).skew() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF kurt 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfkurt_504d_slope_v125_signal(ncfo, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo).rolling(504, min_periods=126).kurt() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF margin min 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmin_63d_slope_v126_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).rolling(63, min_periods=21).min() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin max 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmax_252d_slope_v127_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).rolling(252, min_periods=63).max() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin max 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginmax_252d_slope_v128_signal(ncfo, revenue, closeadj):
    base = _f13_ocf_margin(ncfo, revenue).rolling(252, min_periods=63).max() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin min 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginmin_252d_slope_v129_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).rolling(252, min_periods=63).min() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of count days FCF/mc > 5pct 504d
def f13cfs_f13_cash_flow_snapshot_fcftomcabove5_504d_slope_v130_signal(fcf, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(fcf, marketcap)
    flag = (base > 0.05).astype(float)
    b = flag.rolling(504, min_periods=126).sum() * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of count days OCF/mc > 10pct 504d
def f13cfs_f13_cash_flow_snapshot_ocftomcabove10_504d_slope_v131_signal(ncfo, marketcap, closeadj):
    base = _f13_cashflow_snapshot_scaled(ncfo, marketcap)
    flag = (base > 0.10).astype(float)
    b = flag.rolling(504, min_periods=126).sum() * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of count days FCF margin > rolling mean 504d
def f13cfs_f13_cash_flow_snapshot_fcfmarginabovemean_504d_slope_v132_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue)
    flag = (base > _mean(base, 504)).astype(float)
    b = flag.rolling(504, min_periods=126).sum() * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF * netinc 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfxni_252d_slope_v133_signal(fcf, netinc, closeadj):
    base = _f13_cashflow_snapshot_log(fcf) * np.log(netinc.abs().replace(0, np.nan))
    b = _mean(base, 252) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF * netinc 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfxni_252d_slope_v134_signal(ncfo, netinc, closeadj):
    base = _f13_cashflow_snapshot_log(ncfo) * np.log(netinc.abs().replace(0, np.nan))
    b = _mean(base, 252) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF/netinc 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoni_63d_slope_v135_signal(fcf, netinc, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, netinc), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/netinc 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoni_252d_slope_v136_signal(fcf, netinc, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, netinc), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF/netinc 252d x closeadj (Earnings quality slope)
def f13cfs_f13_cash_flow_snapshot_ocftoni_252d_slope_v137_signal(ncfo, netinc, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, netinc), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF margin x rev 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginxrev_63d_slope_v138_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue) * np.log(revenue.abs().replace(0, np.nan)), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF margin x rev 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginxrev_252d_slope_v139_signal(fcf, revenue, closeadj):
    base = _mean(_f13_fcf_margin(fcf, revenue) * np.log(revenue.abs().replace(0, np.nan)), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF margin x rev 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfmarginxrev_252d_slope_v140_signal(ncfo, revenue, closeadj):
    base = _mean(_f13_ocf_margin(ncfo, revenue) * np.log(revenue.abs().replace(0, np.nan)), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/(debt+mc) 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoev_252d_slope_v141_signal(fcf, debt, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, debt + marketcap), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF/(debt+mc) 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoev_252d_slope_v142_signal(ncfo, debt, marketcap, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, debt + marketcap), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/(debt+mc) z 504d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoevz_504d_slope_v143_signal(fcf, debt, marketcap, closeadj):
    base = _z(_f13_cashflow_snapshot_scaled(fcf, debt + marketcap), 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 5d slope of FCF per share x rev 21d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfpsxrev_21d_slope_v144_signal(fcf, sharesbas, revenue, closeadj):
    base = _f13_cashflow_snapshot_per_share(fcf, sharesbas) * np.log(revenue.abs().replace(0, np.nan))
    b = _mean(base, 21) * closeadj
    return _slope_diff_norm(b, 5).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF per share x rev 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocfpsxrev_252d_slope_v145_signal(ncfo, sharesbas, revenue, closeadj):
    base = _f13_cashflow_snapshot_per_share(ncfo, sharesbas) * np.log(revenue.abs().replace(0, np.nan))
    b = _mean(base, 252) * closeadj
    return _slope_diff_norm(b, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/ebitda 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcftoebitda_252d_slope_v146_signal(fcf, ebitda, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf, ebitda), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 63d slope of OCF/ebitda 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_ocftoebitda_252d_slope_v147_signal(ncfo, ebitda, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(ncfo, ebitda), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF margin EMA 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_fcfmarginema_63d_slope_v148_signal(fcf, revenue, closeadj):
    base = _f13_fcf_margin(fcf, revenue).ewm(span=63, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


# 63d slope of cash earnings 252d x closeadj
def f13cfs_f13_cash_flow_snapshot_cashearnings_252d_slope_v149_signal(fcf, ncfo, netinc, revenue, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf + ncfo + netinc, revenue), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


# 21d slope of cash earnings 63d x closeadj
def f13cfs_f13_cash_flow_snapshot_cashearnings_63d_slope_v150_signal(fcf, ncfo, revenue, closeadj):
    base = _mean(_f13_cashflow_snapshot_scaled(fcf + ncfo, revenue), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13cfs_f13_cash_flow_snapshot_fcfmargin_21d_slope_v001_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmargin_21d_slope_v002_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmargin_63d_slope_v003_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmargin_63d_slope_v004_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmargin_252d_slope_v005_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmargin_252d_slope_v006_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmargin_504d_slope_v007_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmargin_21d_slope_v008_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmargin_21d_slope_v009_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmargin_63d_slope_v010_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmargin_252d_slope_v011_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmargin_504d_slope_v012_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomc_63d_slope_v013_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomc_252d_slope_v014_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomc_252d_slope_v015_signal,
    f13cfs_f13_cash_flow_snapshot_fcfquality_63d_slope_v016_signal,
    f13cfs_f13_cash_flow_snapshot_fcfquality_252d_slope_v017_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoassets_63d_slope_v018_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoassets_252d_slope_v019_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoassets_252d_slope_v020_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoequity_252d_slope_v021_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoequity_252d_slope_v022_signal,
    f13cfs_f13_cash_flow_snapshot_fcftodebt_252d_slope_v023_signal,
    f13cfs_f13_cash_flow_snapshot_ocftodebt_252d_slope_v024_signal,
    f13cfs_f13_cash_flow_snapshot_logfcf_63d_slope_v025_signal,
    f13cfs_f13_cash_flow_snapshot_logfcf_252d_slope_v026_signal,
    f13cfs_f13_cash_flow_snapshot_logocf_252d_slope_v027_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginstd_63d_slope_v028_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginstd_252d_slope_v029_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginstd_252d_slope_v030_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginz_252d_slope_v031_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginz_252d_slope_v032_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcz_504d_slope_v033_signal,
    f13cfs_f13_cash_flow_snapshot_fcfqualityz_504d_slope_v034_signal,
    f13cfs_f13_cash_flow_snapshot_fcfps_21d_slope_v035_signal,
    f13cfs_f13_cash_flow_snapshot_fcfps_252d_slope_v036_signal,
    f13cfs_f13_cash_flow_snapshot_ocfps_21d_slope_v037_signal,
    f13cfs_f13_cash_flow_snapshot_ocfps_252d_slope_v038_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginsq_252d_slope_v039_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginsq_252d_slope_v040_signal,
    f13cfs_f13_cash_flow_snapshot_fcfema_21d_slope_v041_signal,
    f13cfs_f13_cash_flow_snapshot_fcfema_252d_slope_v042_signal,
    f13cfs_f13_cash_flow_snapshot_ocfema_252d_slope_v043_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginema_252d_slope_v044_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginema_252d_slope_v045_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmed_252d_slope_v046_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginmed_252d_slope_v047_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginrank_504d_slope_v048_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginrank_504d_slope_v049_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginabove5_252d_slope_v050_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginabove10_504d_slope_v051_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginabove10_504d_slope_v052_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcabove5_252d_slope_v053_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginxmc_252d_slope_v054_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginxmc_252d_slope_v055_signal,
    f13cfs_f13_cash_flow_snapshot_fcfexp_slope_v056_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginexp_slope_v057_signal,
    f13cfs_f13_cash_flow_snapshot_fcftocapex_252d_slope_v058_signal,
    f13cfs_f13_cash_flow_snapshot_ocftocapex_252d_slope_v059_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoliab_252d_slope_v060_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoliab_252d_slope_v061_signal,
    f13cfs_f13_cash_flow_snapshot_fcfrank_252d_slope_v062_signal,
    f13cfs_f13_cash_flow_snapshot_fcfrank_504d_slope_v063_signal,
    f13cfs_f13_cash_flow_snapshot_fcfskew_252d_slope_v064_signal,
    f13cfs_f13_cash_flow_snapshot_ocfskew_252d_slope_v065_signal,
    f13cfs_f13_cash_flow_snapshot_fcfkurt_252d_slope_v066_signal,
    f13cfs_f13_cash_flow_snapshot_fcfiqr_252d_slope_v067_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmin_252d_slope_v068_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmax_252d_slope_v069_signal,
    f13cfs_f13_cash_flow_snapshot_ocfanomaly_252d_slope_v070_signal,
    f13cfs_f13_cash_flow_snapshot_fcfanomaly_252d_slope_v071_signal,
    f13cfs_f13_cash_flow_snapshot_cfsum_252d_slope_v072_signal,
    f13cfs_f13_cash_flow_snapshot_cfsum_63d_slope_v073_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginann_252d_slope_v074_signal,
    f13cfs_f13_cash_flow_snapshot_fcftosqrtassets_252d_slope_v075_signal,
    f13cfs_f13_cash_flow_snapshot_fcfxmclog_252d_slope_v076_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginxmc_63d_slope_v077_signal,
    f13cfs_f13_cash_flow_snapshot_ocfps_63d_slope_v078_signal,
    f13cfs_f13_cash_flow_snapshot_fcfps_63d_slope_v079_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomc_21d_slope_v080_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomc_21d_slope_v081_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomc_504d_slope_v082_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomc_504d_slope_v083_signal,
    f13cfs_f13_cash_flow_snapshot_fcfquality_504d_slope_v084_signal,
    f13cfs_f13_cash_flow_snapshot_fcfquality_21d_slope_v085_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoassets_504d_slope_v086_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoassets_504d_slope_v087_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoequity_504d_slope_v088_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoequity_504d_slope_v089_signal,
    f13cfs_f13_cash_flow_snapshot_fcftodebt_504d_slope_v090_signal,
    f13cfs_f13_cash_flow_snapshot_ocftodebt_504d_slope_v091_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginema_504d_slope_v092_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginema_504d_slope_v093_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginema_21d_slope_v094_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginema_21d_slope_v095_signal,
    f13cfs_f13_cash_flow_snapshot_fcfema_63d_slope_v096_signal,
    f13cfs_f13_cash_flow_snapshot_fcfema_504d_slope_v097_signal,
    f13cfs_f13_cash_flow_snapshot_ocfema_21d_slope_v098_signal,
    f13cfs_f13_cash_flow_snapshot_ocfema_504d_slope_v099_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmed_504d_slope_v100_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginmed_504d_slope_v101_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginskew_504d_slope_v102_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginkurt_504d_slope_v103_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginskew_504d_slope_v104_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcrank_504d_slope_v105_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomcrank_252d_slope_v106_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoequityrank_504d_slope_v107_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoassetsrank_504d_slope_v108_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginstd_504d_slope_v109_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginstd_504d_slope_v110_signal,
    f13cfs_f13_cash_flow_snapshot_fcfz_504d_slope_v111_signal,
    f13cfs_f13_cash_flow_snapshot_ocfz_504d_slope_v112_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcann_252d_slope_v113_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginann_252d_slope_v114_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfplusocf_21d_slope_v115_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfxlogocf_252d_slope_v116_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfxlogmc_252d_slope_v117_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfminusdebt_252d_slope_v118_signal,
    f13cfs_f13_cash_flow_snapshot_logocfminusdebt_252d_slope_v119_signal,
    f13cfs_f13_cash_flow_snapshot_logfcfminusassets_252d_slope_v120_signal,
    f13cfs_f13_cash_flow_snapshot_fcftolevbase_252d_slope_v121_signal,
    f13cfs_f13_cash_flow_snapshot_ocftototalcap_252d_slope_v122_signal,
    f13cfs_f13_cash_flow_snapshot_fcftolevbase_63d_slope_v123_signal,
    f13cfs_f13_cash_flow_snapshot_fcfskew_504d_slope_v124_signal,
    f13cfs_f13_cash_flow_snapshot_ocfkurt_504d_slope_v125_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmin_63d_slope_v126_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmax_252d_slope_v127_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginmax_252d_slope_v128_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginmin_252d_slope_v129_signal,
    f13cfs_f13_cash_flow_snapshot_fcftomcabove5_504d_slope_v130_signal,
    f13cfs_f13_cash_flow_snapshot_ocftomcabove10_504d_slope_v131_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginabovemean_504d_slope_v132_signal,
    f13cfs_f13_cash_flow_snapshot_fcfxni_252d_slope_v133_signal,
    f13cfs_f13_cash_flow_snapshot_ocfxni_252d_slope_v134_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoni_63d_slope_v135_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoni_252d_slope_v136_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoni_252d_slope_v137_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginxrev_63d_slope_v138_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginxrev_252d_slope_v139_signal,
    f13cfs_f13_cash_flow_snapshot_ocfmarginxrev_252d_slope_v140_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoev_252d_slope_v141_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoev_252d_slope_v142_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoevz_504d_slope_v143_signal,
    f13cfs_f13_cash_flow_snapshot_fcfpsxrev_21d_slope_v144_signal,
    f13cfs_f13_cash_flow_snapshot_ocfpsxrev_252d_slope_v145_signal,
    f13cfs_f13_cash_flow_snapshot_fcftoebitda_252d_slope_v146_signal,
    f13cfs_f13_cash_flow_snapshot_ocftoebitda_252d_slope_v147_signal,
    f13cfs_f13_cash_flow_snapshot_fcfmarginema_63d_slope_v148_signal,
    f13cfs_f13_cash_flow_snapshot_cashearnings_252d_slope_v149_signal,
    f13cfs_f13_cash_flow_snapshot_cashearnings_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_CASH_FLOW_SNAPSHOT_REGISTRY_SLOPE = REGISTRY


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
    sharesbas = pd.Series(_build_log_walk(10, 5e7, 0.0001, 0.002, n), name="sharesbas")
    opinc = pd.Series(_build_log_walk(11, 8e7, 0.0002, 0.007, n), name="opinc")
    liabilities = pd.Series(_build_log_walk(18, 1e9, 0.0001, 0.004, n), name="liabilities")
    closeadj = pd.Series(_build_log_walk(19, 100.0, 0.0005, 0.02, n), name="closeadj")
    marketcap = closeadj * 1e7
    marketcap.name = "marketcap"

    cols = {
        "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
        "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda,
        "capex": capex, "sharesbas": sharesbas, "opinc": opinc,
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f13_cash_flow_snapshot_2nd_derivatives_001_150_claude: {n_features} features pass")
