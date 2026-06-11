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
def _f39_cash_earnings_div(fcf, netinc):
    return fcf - netinc


def _f39_cash_earnings_div_norm(fcf, netinc, scale):
    return (fcf - netinc) / scale.abs().replace(0, np.nan)


def _f39_fcf_minus_netinc_roll(fcf, netinc, w):
    gap = fcf - netinc
    return gap.rolling(w, min_periods=max(1, w // 2)).mean()


def _f39_ncfo_minus_netinc(ncfo, netinc):
    return ncfo - netinc


# 21d rolling mean of fcf-minus-netinc gap, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgap_21d_base_v001_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of fcf-minus-netinc gap, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgap_63d_base_v002_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of fcf-minus-netinc gap, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgap_126d_base_v003_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of fcf-minus-netinc gap, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgap_252d_base_v004_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of fcf-minus-netinc gap, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgap_504d_base_v005_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d normalized fcf-netinc gap (gap divided by netinc), scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapnorm_63d_base_v006_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, netinc)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d normalized fcf-netinc gap (gap divided by netinc), scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapnorm_252d_base_v007_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, netinc)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo-minus-netinc accruals quality signal, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_ncfogap_63d_base_v008_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncfo-minus-netinc accruals quality signal, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_ncfogap_126d_base_v009_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = _mean(gap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo-minus-netinc accruals quality signal, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_ncfogap_252d_base_v010_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo-minus-netinc accruals quality signal, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_ncfogap_504d_base_v011_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = _mean(gap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of fcf-netinc gap (volatility of cash-earnings divergence)
def f39ced_f39_cash_earnings_divergence_fcfgapstd_63d_base_v012_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _std(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgapstd_252d_base_v013_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _std(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgapz_252d_base_v014_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _z(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgapz_504d_base_v015_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _z(gap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ncfo-netinc gap (accruals zscore)
def f39ced_f39_cash_earnings_divergence_ncfogapz_252d_base_v016_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = _z(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ncfo-netinc gap
def f39ced_f39_cash_earnings_divergence_ncfogapz_504d_base_v017_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = _z(gap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf-netinc gap divided by assets (asset-scaled cash divergence)
def f39ced_f39_cash_earnings_divergence_fcfgapassets_63d_base_v018_signal(fcf, netinc, assets, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, assets)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf-netinc gap divided by assets
def f39ced_f39_cash_earnings_divergence_fcfgapassets_252d_base_v019_signal(fcf, netinc, assets, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, assets)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf-netinc gap divided by revenue (revenue-scaled cash divergence)
def f39ced_f39_cash_earnings_divergence_fcfgaprev_63d_base_v020_signal(fcf, netinc, revenue, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, revenue)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf-netinc gap divided by revenue
def f39ced_f39_cash_earnings_divergence_fcfgaprev_252d_base_v021_signal(fcf, netinc, revenue, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, revenue)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf-netinc gap divided by equity
def f39ced_f39_cash_earnings_divergence_fcfgapeq_63d_base_v022_signal(fcf, netinc, equity, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, equity)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf-netinc gap divided by equity
def f39ced_f39_cash_earnings_divergence_fcfgapeq_252d_base_v023_signal(fcf, netinc, equity, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, equity)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo-netinc gap divided by assets (accruals scaled by assets)
def f39ced_f39_cash_earnings_divergence_ncfogapassets_63d_base_v024_signal(ncfo, netinc, assets, closeadj):
    gap = (_f39_ncfo_minus_netinc(ncfo, netinc)) / assets.abs().replace(0, np.nan)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo-netinc gap divided by assets
def f39ced_f39_cash_earnings_divergence_ncfogapassets_252d_base_v025_signal(ncfo, netinc, assets, closeadj):
    gap = (_f39_ncfo_minus_netinc(ncfo, netinc)) / assets.abs().replace(0, np.nan)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo-netinc gap divided by revenue
def f39ced_f39_cash_earnings_divergence_ncfogaprev_63d_base_v026_signal(ncfo, netinc, revenue, closeadj):
    gap = (_f39_ncfo_minus_netinc(ncfo, netinc)) / revenue.abs().replace(0, np.nan)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo-netinc gap divided by revenue
def f39ced_f39_cash_earnings_divergence_ncfogaprev_252d_base_v027_signal(ncfo, netinc, revenue, closeadj):
    gap = (_f39_ncfo_minus_netinc(ncfo, netinc)) / revenue.abs().replace(0, np.nan)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf-netinc gap relative to ebitda
def f39ced_f39_cash_earnings_divergence_fcfgapebitda_252d_base_v028_signal(fcf, netinc, ebitda, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, ebitda)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf-netinc gap relative to ebitda
def f39ced_f39_cash_earnings_divergence_fcfgapebitda_63d_base_v029_signal(fcf, netinc, ebitda, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, ebitda)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d fcf-netinc gap × closeadj × current revenue (cap-weighted divergence)
def f39ced_f39_cash_earnings_divergence_fcfgapxrev_63d_base_v030_signal(fcf, netinc, revenue, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 63) * closeadj * revenue.pct_change(63).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf-netinc gap × closeadj × revenue growth
def f39ced_f39_cash_earnings_divergence_fcfgapxrev_252d_base_v031_signal(fcf, netinc, revenue, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 252) * closeadj * revenue.pct_change(252).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of fcf to netinc minus 1.0 (quality coverage), scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfratio_252d_base_v032_signal(fcf, netinc, closeadj):
    ratio = _safe_div(fcf, netinc) - 1.0
    gap = _f39_cash_earnings_div(fcf, netinc) * 0.0
    result = _mean(ratio + gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of fcf to netinc minus 1.0
def f39ced_f39_cash_earnings_divergence_fcfratio_63d_base_v033_signal(fcf, netinc, closeadj):
    ratio = _safe_div(fcf, netinc) - 1.0
    gap = _f39_cash_earnings_div(fcf, netinc) * 0.0
    result = _mean(ratio + gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of ncfo to netinc minus 1.0 (cash coverage)
def f39ced_f39_cash_earnings_divergence_ncforatio_252d_base_v034_signal(ncfo, netinc, closeadj):
    ratio = _safe_div(ncfo, netinc) - 1.0
    gap = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    result = _mean(ratio + gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of ncfo to netinc minus 1.0
def f39ced_f39_cash_earnings_divergence_ncforatio_63d_base_v035_signal(ncfo, netinc, closeadj):
    ratio = _safe_div(ncfo, netinc) - 1.0
    gap = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    result = _mean(ratio + gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d expanding fcf-netinc gap, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapexp_base_v036_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d expanding ncfo-netinc gap, scaled by closeadj
def f39ced_f39_cash_earnings_divergence_ncfogapexp_base_v037_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = gap.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of fcf-netinc gap (cumulative quality), scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapsum_63d_base_v038_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgapsum_252d_base_v039_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgapsum_504d_base_v040_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of ncfo-netinc gap (cumulative accruals)
def f39ced_f39_cash_earnings_divergence_ncfogapsum_63d_base_v041_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = gap.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of ncfo-netinc gap
def f39ced_f39_cash_earnings_divergence_ncfogapsum_252d_base_v042_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = gap.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of fcf-netinc gap × closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapema_252d_base_v043_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of fcf-netinc gap × closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapema_63d_base_v044_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of ncfo-netinc gap × closeadj
def f39ced_f39_cash_earnings_divergence_ncfogapema_252d_base_v045_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = gap.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of ncfo-netinc gap × closeadj
def f39ced_f39_cash_earnings_divergence_ncfogapema_63d_base_v046_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = gap.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap-mean × current closeadj × current netinc magnitude (scale-weighted)
def f39ced_f39_cash_earnings_divergence_fcfgapxni_252d_base_v047_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 252) * closeadj * netinc.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap-mean × current closeadj × current revenue (revenue-weighted)
def f39ced_f39_cash_earnings_divergence_fcfgapxrevcur_63d_base_v048_signal(fcf, netinc, revenue, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 63) * closeadj * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative ncfo minus cumulative netinc divided by cumulative netinc
def f39ced_f39_cash_earnings_divergence_cumcoverage_252d_base_v049_signal(ncfo, netinc, closeadj):
    cum_ncfo = ncfo.rolling(252, min_periods=63).sum()
    cum_ni = netinc.rolling(252, min_periods=63).sum()
    gap = _f39_ncfo_minus_netinc(cum_ncfo, cum_ni)
    result = gap / cum_ni.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative ncfo minus cumulative netinc divided by cumulative netinc
def f39ced_f39_cash_earnings_divergence_cumcoverage_504d_base_v050_signal(ncfo, netinc, closeadj):
    cum_ncfo = ncfo.rolling(504, min_periods=126).sum()
    cum_ni = netinc.rolling(504, min_periods=126).sum()
    gap = _f39_ncfo_minus_netinc(cum_ncfo, cum_ni)
    result = gap / cum_ni.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap-mean × eps level (per-share quality)
def f39ced_f39_cash_earnings_divergence_fcfgapxeps_252d_base_v051_signal(fcf, netinc, eps, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 252) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap-mean × eps
def f39ced_f39_cash_earnings_divergence_fcfgapxeps_63d_base_v052_signal(fcf, netinc, eps, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 63) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap normalized by sharesbas (per-share gap)
def f39ced_f39_cash_earnings_divergence_fcfgappershare_252d_base_v053_signal(fcf, netinc, sharesbas, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    per_share = gap / sharesbas.abs().replace(0, np.nan)
    result = _mean(per_share, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap normalized by sharesbas
def f39ced_f39_cash_earnings_divergence_fcfgappershare_63d_base_v054_signal(fcf, netinc, sharesbas, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    per_share = gap / sharesbas.abs().replace(0, np.nan)
    result = _mean(per_share, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo gap normalized by sharesbas
def f39ced_f39_cash_earnings_divergence_ncfogappershare_252d_base_v055_signal(ncfo, netinc, sharesbas, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    per_share = gap / sharesbas.abs().replace(0, np.nan)
    result = _mean(per_share, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo gap normalized by sharesbas
def f39ced_f39_cash_earnings_divergence_ncfogappershare_63d_base_v056_signal(ncfo, netinc, sharesbas, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    per_share = gap / sharesbas.abs().replace(0, np.nan)
    result = _mean(per_share, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap interaction with debt (cash-quality vs leverage)
def f39ced_f39_cash_earnings_divergence_fcfgapxdebt_252d_base_v057_signal(fcf, netinc, debt, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 252) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap interaction with debt
def f39ced_f39_cash_earnings_divergence_fcfgapxdebt_63d_base_v058_signal(fcf, netinc, debt, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 63) / debt.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap interaction with capex (cash-quality net of capex)
def f39ced_f39_cash_earnings_divergence_fcfgapxcapex_252d_base_v059_signal(fcf, netinc, capex, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 252) / capex.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap interaction with capex
def f39ced_f39_cash_earnings_divergence_fcfgapxcapex_63d_base_v060_signal(fcf, netinc, capex, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 63) / capex.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign of fcf-netinc gap × magnitude × closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapsignmag_252d_base_v061_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    rolling_gap = _mean(gap, 252)
    result = np.sign(rolling_gap) * rolling_gap.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of fcf-netinc gap × magnitude
def f39ced_f39_cash_earnings_divergence_fcfgapsignmag_63d_base_v062_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    rolling_gap = _mean(gap, 63)
    result = np.sign(rolling_gap) * rolling_gap.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap-mean / 504d gap-std (signal-to-noise of cash-earnings divergence)
def f39ced_f39_cash_earnings_divergence_fcfgapsnr_504d_base_v063_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    sd = _std(gap, 504).replace(0, np.nan)
    result = _mean(gap, 252) / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap-mean / 252d gap-std
def f39ced_f39_cash_earnings_divergence_fcfgapsnr_252d_base_v064_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    sd = _std(gap, 252).replace(0, np.nan)
    result = _mean(gap, 63) / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo-netinc gap / std (snr of accruals)
def f39ced_f39_cash_earnings_divergence_ncfogapsnr_252d_base_v065_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    sd = _std(gap, 252).replace(0, np.nan)
    result = _mean(gap, 63) / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo-netinc gap / std
def f39ced_f39_cash_earnings_divergence_ncfogapsnr_504d_base_v066_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    sd = _std(gap, 504).replace(0, np.nan)
    result = _mean(gap, 252) / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d divergence between fcf gap and ncfo gap (capex effect signal)
def f39ced_f39_cash_earnings_divergence_fcfvsncfogap_252d_base_v067_signal(fcf, ncfo, netinc, closeadj):
    fcf_gap = _f39_cash_earnings_div(fcf, netinc)
    ncfo_gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = (_mean(fcf_gap, 252) - _mean(ncfo_gap, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d divergence between fcf gap and ncfo gap
def f39ced_f39_cash_earnings_divergence_fcfvsncfogap_63d_base_v068_signal(fcf, ncfo, netinc, closeadj):
    fcf_gap = _f39_cash_earnings_div(fcf, netinc)
    ncfo_gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = (_mean(fcf_gap, 63) - _mean(ncfo_gap, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × workingcapital change (working capital absorption proxy)
def f39ced_f39_cash_earnings_divergence_fcfgapxwc_252d_base_v069_signal(fcf, netinc, workingcapital, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    wc_chg = workingcapital.diff(252)
    result = _mean(gap, 252) * wc_chg.abs() * closeadj / 1.0e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × workingcapital change
def f39ced_f39_cash_earnings_divergence_fcfgapxwc_63d_base_v070_signal(fcf, netinc, workingcapital, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    wc_chg = workingcapital.diff(63)
    result = _mean(gap, 63) * wc_chg.abs() * closeadj / 1.0e6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d expanding zscore of fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgapexpz_base_v071_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    m = gap.expanding(min_periods=63).mean()
    sd = gap.expanding(min_periods=63).std().replace(0, np.nan)
    result = (gap - m) / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d expanding zscore of ncfo-netinc gap
def f39ced_f39_cash_earnings_divergence_ncfogapexpz_base_v072_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    m = gap.expanding(min_periods=63).mean()
    sd = gap.expanding(min_periods=63).std().replace(0, np.nan)
    result = (gap - m) / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap-mean × revenue × closeadj × eps composite
def f39ced_f39_cash_earnings_divergence_fcfgapcomposite_252d_base_v073_signal(fcf, netinc, revenue, eps, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 252) * revenue.pct_change(252).fillna(0.0) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap-mean × revenue growth × closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapcomposite_63d_base_v074_signal(fcf, netinc, revenue, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 63) * revenue.pct_change(63).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite quality: (ncfo-netinc) divided by assets × closeadj × revenue growth
def f39ced_f39_cash_earnings_divergence_qualitycomposite_252d_base_v075_signal(ncfo, netinc, assets, revenue, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    quality = gap / assets.abs().replace(0, np.nan)
    result = _mean(quality, 252) * revenue.pct_change(252).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39ced_f39_cash_earnings_divergence_fcfgap_21d_base_v001_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_63d_base_v002_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_126d_base_v003_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_252d_base_v004_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_504d_base_v005_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapnorm_63d_base_v006_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapnorm_252d_base_v007_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_63d_base_v008_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_126d_base_v009_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_252d_base_v010_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_504d_base_v011_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapstd_63d_base_v012_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapstd_252d_base_v013_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapz_252d_base_v014_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapz_504d_base_v015_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapz_252d_base_v016_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapz_504d_base_v017_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapassets_63d_base_v018_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapassets_252d_base_v019_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaprev_63d_base_v020_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaprev_252d_base_v021_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapeq_63d_base_v022_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapeq_252d_base_v023_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapassets_63d_base_v024_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapassets_252d_base_v025_signal,
    f39ced_f39_cash_earnings_divergence_ncfogaprev_63d_base_v026_signal,
    f39ced_f39_cash_earnings_divergence_ncfogaprev_252d_base_v027_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapebitda_252d_base_v028_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapebitda_63d_base_v029_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxrev_63d_base_v030_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxrev_252d_base_v031_signal,
    f39ced_f39_cash_earnings_divergence_fcfratio_252d_base_v032_signal,
    f39ced_f39_cash_earnings_divergence_fcfratio_63d_base_v033_signal,
    f39ced_f39_cash_earnings_divergence_ncforatio_252d_base_v034_signal,
    f39ced_f39_cash_earnings_divergence_ncforatio_63d_base_v035_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapexp_base_v036_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapexp_base_v037_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsum_63d_base_v038_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsum_252d_base_v039_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsum_504d_base_v040_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapsum_63d_base_v041_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapsum_252d_base_v042_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapema_252d_base_v043_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapema_63d_base_v044_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapema_252d_base_v045_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapema_63d_base_v046_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxni_252d_base_v047_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxrevcur_63d_base_v048_signal,
    f39ced_f39_cash_earnings_divergence_cumcoverage_252d_base_v049_signal,
    f39ced_f39_cash_earnings_divergence_cumcoverage_504d_base_v050_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxeps_252d_base_v051_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxeps_63d_base_v052_signal,
    f39ced_f39_cash_earnings_divergence_fcfgappershare_252d_base_v053_signal,
    f39ced_f39_cash_earnings_divergence_fcfgappershare_63d_base_v054_signal,
    f39ced_f39_cash_earnings_divergence_ncfogappershare_252d_base_v055_signal,
    f39ced_f39_cash_earnings_divergence_ncfogappershare_63d_base_v056_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxdebt_252d_base_v057_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxdebt_63d_base_v058_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxcapex_252d_base_v059_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxcapex_63d_base_v060_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsignmag_252d_base_v061_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsignmag_63d_base_v062_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsnr_504d_base_v063_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsnr_252d_base_v064_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapsnr_252d_base_v065_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapsnr_504d_base_v066_signal,
    f39ced_f39_cash_earnings_divergence_fcfvsncfogap_252d_base_v067_signal,
    f39ced_f39_cash_earnings_divergence_fcfvsncfogap_63d_base_v068_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxwc_252d_base_v069_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxwc_63d_base_v070_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapexpz_base_v071_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapexpz_base_v072_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapcomposite_252d_base_v073_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapcomposite_63d_base_v074_signal,
    f39ced_f39_cash_earnings_divergence_qualitycomposite_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_CASH_EARNINGS_DIVERGENCE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1.0e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="netinc")
    fcf = pd.Series(0.9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.013, n))), name="fcf")
    ncfo = pd.Series(1.1e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ncfo")
    assets = pd.Series(5.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(2.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="equity")
    debt = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="debt")
    capex = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.012, n))), name="capex")
    eps = pd.Series(2.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="eps")
    sharesbas = pd.Series(5.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="sharesbas")
    ebitda = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ebitda")
    workingcapital = pd.Series(8.0e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="workingcapital")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "assets": assets, "equity": equity, "debt": debt,
        "capex": capex, "eps": eps, "sharesbas": sharesbas, "ebitda": ebitda,
        "workingcapital": workingcapital,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f39_cash_earnings_div", "_f39_fcf_minus_netinc", "_f39_ncfo_minus_netinc")
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
    print(f"OK f39_cash_earnings_divergence_base_001_075_claude: {n_features} features pass")
