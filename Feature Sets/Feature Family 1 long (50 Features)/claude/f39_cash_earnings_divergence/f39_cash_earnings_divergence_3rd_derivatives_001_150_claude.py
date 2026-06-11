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


def _slope(s, w):
    return s.diff(periods=w)


def _jerk(s, w1, w2):
    sl = s.diff(periods=w1)
    return sl.diff(periods=w2)


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


# 21d jerk of 21d fcf-netinc gap (slope diff)
def f39ced_f39_cash_earnings_divergence_fcfgap_21d_jerk_v001_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 21) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgap_21d_jerk_v002_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 21) * closeadj
    result = _jerk(base, 5, 5) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgap_63d_jerk_v003_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 63) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgap_63d_jerk_v004_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 63) * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgap_126d_jerk_v005_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 126) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgap_126d_jerk_v006_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 126) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgap_252d_jerk_v007_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 252) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgap_252d_jerk_v008_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 252) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgap_504d_jerk_v009_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 504) * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgap_504d_jerk_v010_signal(fcf, netinc, closeadj):
    base = _f39_fcf_minus_netinc_roll(fcf, netinc, 504) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d normalized gap
def f39ced_f39_cash_earnings_divergence_fcfgapnorm_63d_jerk_v011_signal(fcf, netinc, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, netinc), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d normalized gap
def f39ced_f39_cash_earnings_divergence_fcfgapnorm_252d_jerk_v012_signal(fcf, netinc, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, netinc), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo gap
def f39ced_f39_cash_earnings_divergence_ncfogap_63d_jerk_v013_signal(ncfo, netinc, closeadj):
    base = _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 63) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d ncfo gap
def f39ced_f39_cash_earnings_divergence_ncfogap_126d_jerk_v014_signal(ncfo, netinc, closeadj):
    base = _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 126) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo gap
def f39ced_f39_cash_earnings_divergence_ncfogap_252d_jerk_v015_signal(ncfo, netinc, closeadj):
    base = _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 252) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d ncfo gap
def f39ced_f39_cash_earnings_divergence_ncfogap_252d_jerk_v016_signal(ncfo, netinc, closeadj):
    base = _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 252) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ncfo gap
def f39ced_f39_cash_earnings_divergence_ncfogap_504d_jerk_v017_signal(ncfo, netinc, closeadj):
    base = _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 504) * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d ncfo gap
def f39ced_f39_cash_earnings_divergence_ncfogap_504d_jerk_v018_signal(ncfo, netinc, closeadj):
    base = _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 504) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap std
def f39ced_f39_cash_earnings_divergence_fcfgapstd_63d_jerk_v019_signal(fcf, netinc, closeadj):
    base = _std(_f39_cash_earnings_div(fcf, netinc), 63) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap std
def f39ced_f39_cash_earnings_divergence_fcfgapstd_252d_jerk_v020_signal(fcf, netinc, closeadj):
    base = _std(_f39_cash_earnings_div(fcf, netinc), 252) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d gap zscore
def f39ced_f39_cash_earnings_divergence_fcfgapz_252d_jerk_v021_signal(fcf, netinc, closeadj):
    base = _z(_f39_cash_earnings_div(fcf, netinc), 252) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap zscore
def f39ced_f39_cash_earnings_divergence_fcfgapz_504d_jerk_v022_signal(fcf, netinc, closeadj):
    base = _z(_f39_cash_earnings_div(fcf, netinc), 504) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d ncfo zscore
def f39ced_f39_cash_earnings_divergence_ncfogapz_252d_jerk_v023_signal(ncfo, netinc, closeadj):
    base = _z(_f39_ncfo_minus_netinc(ncfo, netinc), 252) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ncfo zscore
def f39ced_f39_cash_earnings_divergence_ncfogapz_504d_jerk_v024_signal(ncfo, netinc, closeadj):
    base = _z(_f39_ncfo_minus_netinc(ncfo, netinc), 504) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/assets
def f39ced_f39_cash_earnings_divergence_fcfgapassets_63d_jerk_v025_signal(fcf, netinc, assets, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, assets), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/assets
def f39ced_f39_cash_earnings_divergence_fcfgapassets_252d_jerk_v026_signal(fcf, netinc, assets, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, assets), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/revenue
def f39ced_f39_cash_earnings_divergence_fcfgaprev_63d_jerk_v027_signal(fcf, netinc, revenue, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, revenue), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/revenue
def f39ced_f39_cash_earnings_divergence_fcfgaprev_252d_jerk_v028_signal(fcf, netinc, revenue, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, revenue), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/equity
def f39ced_f39_cash_earnings_divergence_fcfgapeq_63d_jerk_v029_signal(fcf, netinc, equity, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, equity), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/equity
def f39ced_f39_cash_earnings_divergence_fcfgapeq_252d_jerk_v030_signal(fcf, netinc, equity, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, equity), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo gap/assets
def f39ced_f39_cash_earnings_divergence_ncfogapassets_63d_jerk_v031_signal(ncfo, netinc, assets, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc) / assets.abs().replace(0, np.nan)
    base = _mean(gap, 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo gap/assets
def f39ced_f39_cash_earnings_divergence_ncfogapassets_252d_jerk_v032_signal(ncfo, netinc, assets, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc) / assets.abs().replace(0, np.nan)
    base = _mean(gap, 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo gap/revenue
def f39ced_f39_cash_earnings_divergence_ncfogaprev_63d_jerk_v033_signal(ncfo, netinc, revenue, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc) / revenue.abs().replace(0, np.nan)
    base = _mean(gap, 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo gap/revenue
def f39ced_f39_cash_earnings_divergence_ncfogaprev_252d_jerk_v034_signal(ncfo, netinc, revenue, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc) / revenue.abs().replace(0, np.nan)
    base = _mean(gap, 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/ebitda
def f39ced_f39_cash_earnings_divergence_fcfgapebitda_252d_jerk_v035_signal(fcf, netinc, ebitda, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, ebitda), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/ebitda
def f39ced_f39_cash_earnings_divergence_fcfgapebitda_63d_jerk_v036_signal(fcf, netinc, ebitda, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, ebitda), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap × revenue growth
def f39ced_f39_cash_earnings_divergence_fcfgapxrev_63d_jerk_v037_signal(fcf, netinc, revenue, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) * closeadj * revenue.pct_change(63).fillna(0.0)
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap × revenue growth
def f39ced_f39_cash_earnings_divergence_fcfgapxrev_252d_jerk_v038_signal(fcf, netinc, revenue, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) * closeadj * revenue.pct_change(252).fillna(0.0)
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d fcf/netinc ratio
def f39ced_f39_cash_earnings_divergence_fcfratio_252d_jerk_v039_signal(fcf, netinc, closeadj):
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    base = _mean(_safe_div(fcf, netinc) - 1.0 + aux, 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d fcf/netinc ratio
def f39ced_f39_cash_earnings_divergence_fcfratio_63d_jerk_v040_signal(fcf, netinc, closeadj):
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    base = _mean(_safe_div(fcf, netinc) - 1.0 + aux, 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo/netinc ratio
def f39ced_f39_cash_earnings_divergence_ncforatio_252d_jerk_v041_signal(ncfo, netinc, closeadj):
    aux = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    base = _mean(_safe_div(ncfo, netinc) - 1.0 + aux, 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo/netinc ratio
def f39ced_f39_cash_earnings_divergence_ncforatio_63d_jerk_v042_signal(ncfo, netinc, closeadj):
    aux = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    base = _mean(_safe_div(ncfo, netinc) - 1.0 + aux, 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding fcf-netinc gap mean
def f39ced_f39_cash_earnings_divergence_fcfgapexp_jerk_v043_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).expanding(min_periods=63).mean() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding ncfo-netinc gap mean
def f39ced_f39_cash_earnings_divergence_ncfogapexp_jerk_v044_signal(ncfo, netinc, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc).expanding(min_periods=63).mean() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap sum
def f39ced_f39_cash_earnings_divergence_fcfgapsum_63d_jerk_v045_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap sum
def f39ced_f39_cash_earnings_divergence_fcfgapsum_252d_jerk_v046_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap sum
def f39ced_f39_cash_earnings_divergence_fcfgapsum_504d_jerk_v047_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo sum
def f39ced_f39_cash_earnings_divergence_ncfogapsum_63d_jerk_v048_signal(ncfo, netinc, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo sum
def f39ced_f39_cash_earnings_divergence_ncfogapsum_252d_jerk_v049_signal(ncfo, netinc, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap EMA
def f39ced_f39_cash_earnings_divergence_fcfgapema_252d_jerk_v050_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap EMA
def f39ced_f39_cash_earnings_divergence_fcfgapema_63d_jerk_v051_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo gap EMA
def f39ced_f39_cash_earnings_divergence_ncfogapema_252d_jerk_v052_signal(ncfo, netinc, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo gap EMA
def f39ced_f39_cash_earnings_divergence_ncfogapema_63d_jerk_v053_signal(ncfo, netinc, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap × netinc magnitude
def f39ced_f39_cash_earnings_divergence_fcfgapxni_252d_jerk_v054_signal(fcf, netinc, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) * closeadj * netinc.abs()
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap × revenue level
def f39ced_f39_cash_earnings_divergence_fcfgapxrevcur_63d_jerk_v055_signal(fcf, netinc, revenue, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) * closeadj * revenue
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d cumulative coverage
def f39ced_f39_cash_earnings_divergence_cumcoverage_252d_jerk_v056_signal(ncfo, netinc, closeadj):
    cum_ncfo = ncfo.rolling(252, min_periods=63).sum()
    cum_ni = netinc.rolling(252, min_periods=63).sum()
    aux = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    base = (_f39_ncfo_minus_netinc(cum_ncfo, cum_ni) / cum_ni.abs().replace(0, np.nan)) * closeadj + aux
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d cumulative coverage
def f39ced_f39_cash_earnings_divergence_cumcoverage_504d_jerk_v057_signal(ncfo, netinc, closeadj):
    cum_ncfo = ncfo.rolling(504, min_periods=126).sum()
    cum_ni = netinc.rolling(504, min_periods=126).sum()
    aux = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    base = (_f39_ncfo_minus_netinc(cum_ncfo, cum_ni) / cum_ni.abs().replace(0, np.nan)) * closeadj + aux
    result = _jerk(base, 63, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap × eps
def f39ced_f39_cash_earnings_divergence_fcfgapxeps_252d_jerk_v058_signal(fcf, netinc, eps, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) * eps * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap × eps
def f39ced_f39_cash_earnings_divergence_fcfgapxeps_63d_jerk_v059_signal(fcf, netinc, eps, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) * eps * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap per share
def f39ced_f39_cash_earnings_divergence_fcfgappershare_252d_jerk_v060_signal(fcf, netinc, sharesbas, closeadj):
    per_share = _f39_cash_earnings_div(fcf, netinc) / sharesbas.abs().replace(0, np.nan)
    base = _mean(per_share, 252) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap per share
def f39ced_f39_cash_earnings_divergence_fcfgappershare_63d_jerk_v061_signal(fcf, netinc, sharesbas, closeadj):
    per_share = _f39_cash_earnings_div(fcf, netinc) / sharesbas.abs().replace(0, np.nan)
    base = _mean(per_share, 63) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo gap per share
def f39ced_f39_cash_earnings_divergence_ncfogappershare_252d_jerk_v062_signal(ncfo, netinc, sharesbas, closeadj):
    per_share = _f39_ncfo_minus_netinc(ncfo, netinc) / sharesbas.abs().replace(0, np.nan)
    base = _mean(per_share, 252) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo gap per share
def f39ced_f39_cash_earnings_divergence_ncfogappershare_63d_jerk_v063_signal(ncfo, netinc, sharesbas, closeadj):
    per_share = _f39_ncfo_minus_netinc(ncfo, netinc) / sharesbas.abs().replace(0, np.nan)
    base = _mean(per_share, 63) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/debt
def f39ced_f39_cash_earnings_divergence_fcfgapxdebt_252d_jerk_v064_signal(fcf, netinc, debt, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/debt
def f39ced_f39_cash_earnings_divergence_fcfgapxdebt_63d_jerk_v065_signal(fcf, netinc, debt, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) / debt.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/capex
def f39ced_f39_cash_earnings_divergence_fcfgapxcapex_252d_jerk_v066_signal(fcf, netinc, capex, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) / capex.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/capex
def f39ced_f39_cash_earnings_divergence_fcfgapxcapex_63d_jerk_v067_signal(fcf, netinc, capex, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) / capex.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap signed magnitude
def f39ced_f39_cash_earnings_divergence_fcfgapsignmag_252d_jerk_v068_signal(fcf, netinc, closeadj):
    rolling_gap = _mean(_f39_cash_earnings_div(fcf, netinc), 252)
    base = np.sign(rolling_gap) * rolling_gap.abs() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap signed magnitude
def f39ced_f39_cash_earnings_divergence_fcfgapsignmag_63d_jerk_v069_signal(fcf, netinc, closeadj):
    rolling_gap = _mean(_f39_cash_earnings_div(fcf, netinc), 63)
    base = np.sign(rolling_gap) * rolling_gap.abs() * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d snr
def f39ced_f39_cash_earnings_divergence_fcfgapsnr_504d_jerk_v070_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    base = _mean(gap, 252) / _std(gap, 504).replace(0, np.nan) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d snr
def f39ced_f39_cash_earnings_divergence_fcfgapsnr_252d_jerk_v071_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    base = _mean(gap, 63) / _std(gap, 252).replace(0, np.nan) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d ncfo snr
def f39ced_f39_cash_earnings_divergence_ncfogapsnr_252d_jerk_v072_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    base = _mean(gap, 63) / _std(gap, 252).replace(0, np.nan) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ncfo snr
def f39ced_f39_cash_earnings_divergence_ncfogapsnr_504d_jerk_v073_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    base = _mean(gap, 252) / _std(gap, 504).replace(0, np.nan) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d fcf-vs-ncfo gap divergence
def f39ced_f39_cash_earnings_divergence_fcfvsncfogap_252d_jerk_v074_signal(fcf, ncfo, netinc, closeadj):
    base = (_mean(_f39_cash_earnings_div(fcf, netinc), 252) - _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 252)) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d fcf-vs-ncfo gap
def f39ced_f39_cash_earnings_divergence_fcfvsncfogap_63d_jerk_v075_signal(fcf, ncfo, netinc, closeadj):
    base = (_mean(_f39_cash_earnings_div(fcf, netinc), 63) - _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 63)) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap × workingcapital change
def f39ced_f39_cash_earnings_divergence_fcfgapxwc_252d_jerk_v076_signal(fcf, netinc, workingcapital, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) * workingcapital.diff(252).abs() * closeadj / 1.0e6
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap × workingcapital change
def f39ced_f39_cash_earnings_divergence_fcfgapxwc_63d_jerk_v077_signal(fcf, netinc, workingcapital, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) * workingcapital.diff(63).abs() * closeadj / 1.0e6
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding zscore of fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgapexpz_jerk_v078_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    m = gap.expanding(min_periods=63).mean()
    sd = gap.expanding(min_periods=63).std().replace(0, np.nan)
    base = (gap - m) / sd * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding zscore of ncfo-netinc gap
def f39ced_f39_cash_earnings_divergence_ncfogapexpz_jerk_v079_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    m = gap.expanding(min_periods=63).mean()
    sd = gap.expanding(min_periods=63).std().replace(0, np.nan)
    base = (gap - m) / sd * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d composite (gap × revgrow × eps)
def f39ced_f39_cash_earnings_divergence_fcfgapcomposite_252d_jerk_v080_signal(fcf, netinc, revenue, eps, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) * revenue.pct_change(252).fillna(0.0) * eps * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d composite (gap × revgrow)
def f39ced_f39_cash_earnings_divergence_fcfgapcomposite_63d_jerk_v081_signal(fcf, netinc, revenue, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) * revenue.pct_change(63).fillna(0.0) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d quality composite
def f39ced_f39_cash_earnings_divergence_qualitycomposite_252d_jerk_v082_signal(ncfo, netinc, assets, revenue, closeadj):
    quality = _f39_ncfo_minus_netinc(ncfo, netinc) / assets.abs().replace(0, np.nan)
    base = _mean(quality, 252) * revenue.pct_change(252).fillna(0.0) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap z over 63d
def f39ced_f39_cash_earnings_divergence_fcfgapz_63d_jerk_v083_signal(fcf, netinc, closeadj):
    base = _z(_mean(_f39_cash_earnings_div(fcf, netinc), 21), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d gap z
def f39ced_f39_cash_earnings_divergence_fcfgapz_126d_jerk_v084_signal(fcf, netinc, closeadj):
    base = _z(_mean(_f39_cash_earnings_div(fcf, netinc), 63), 126) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d positive divergence frequency
def f39ced_f39_cash_earnings_divergence_posdivfreq_252d_jerk_v085_signal(fcf, netinc, closeadj):
    pos = (_f39_cash_earnings_div(fcf, netinc) > 0).astype(float)
    base = pos.rolling(252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d positive divergence frequency
def f39ced_f39_cash_earnings_divergence_posdivfreq_504d_jerk_v086_signal(fcf, netinc, closeadj):
    pos = (_f39_cash_earnings_div(fcf, netinc) > 0).astype(float)
    base = pos.rolling(504, min_periods=126).mean() * closeadj
    result = _jerk(base, 63, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo positive frequency
def f39ced_f39_cash_earnings_divergence_posncfofreq_252d_jerk_v087_signal(ncfo, netinc, closeadj):
    pos = (_f39_ncfo_minus_netinc(ncfo, netinc) > 0).astype(float)
    base = pos.rolling(252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ncfo positive frequency
def f39ced_f39_cash_earnings_divergence_posncfofreq_504d_jerk_v088_signal(ncfo, netinc, closeadj):
    pos = (_f39_ncfo_minus_netinc(ncfo, netinc) > 0).astype(float)
    base = pos.rolling(504, min_periods=126).mean() * closeadj
    result = _jerk(base, 63, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d pos/neg ratio
def f39ced_f39_cash_earnings_divergence_fcfposnegratio_252d_jerk_v089_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    pos = gap.where(gap > 0, 0.0).rolling(252, min_periods=63).mean()
    neg = gap.where(gap < 0, 0.0).abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    base = pos / neg * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d pos/neg ratio
def f39ced_f39_cash_earnings_divergence_fcfposnegratio_63d_jerk_v090_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    pos = gap.where(gap > 0, 0.0).rolling(63, min_periods=21).mean()
    neg = gap.where(gap < 0, 0.0).abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = pos / neg * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap change
def f39ced_f39_cash_earnings_divergence_fcfgapchg_252d_jerk_v091_signal(fcf, netinc, closeadj):
    base = _diff(_mean(_f39_cash_earnings_div(fcf, netinc), 63), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap change
def f39ced_f39_cash_earnings_divergence_fcfgapchg_63d_jerk_v092_signal(fcf, netinc, closeadj):
    base = _diff(_mean(_f39_cash_earnings_div(fcf, netinc), 21), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo gap delta
def f39ced_f39_cash_earnings_divergence_ncfogapdelta_252d_jerk_v093_signal(ncfo, netinc, closeadj):
    base = (_mean(_f39_ncfo_minus_netinc(ncfo, netinc), 252) - _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 504)) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo gap delta
def f39ced_f39_cash_earnings_divergence_ncfogapdelta_63d_jerk_v094_signal(ncfo, netinc, closeadj):
    base = (_mean(_f39_ncfo_minus_netinc(ncfo, netinc), 63) - _mean(_f39_ncfo_minus_netinc(ncfo, netinc), 252)) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/opinc
def f39ced_f39_cash_earnings_divergence_fcfgapopinc_252d_jerk_v095_signal(fcf, netinc, opinc, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, opinc), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/opinc
def f39ced_f39_cash_earnings_divergence_fcfgapopinc_63d_jerk_v096_signal(fcf, netinc, opinc, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, opinc), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/gp
def f39ced_f39_cash_earnings_divergence_fcfgapgp_252d_jerk_v097_signal(fcf, netinc, gp, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, gp), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/gp
def f39ced_f39_cash_earnings_divergence_fcfgapgp_63d_jerk_v098_signal(fcf, netinc, gp, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, gp), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap area
def f39ced_f39_cash_earnings_divergence_fcfgaparea_252d_jerk_v099_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).abs().rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap area
def f39ced_f39_cash_earnings_divergence_fcfgaparea_63d_jerk_v100_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).abs().rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap area
def f39ced_f39_cash_earnings_divergence_fcfgaparea_504d_jerk_v101_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).abs().rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap high quantile
def f39ced_f39_cash_earnings_divergence_fcfgapquantilehi_252d_jerk_v102_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(252, min_periods=63).quantile(0.9) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap low quantile
def f39ced_f39_cash_earnings_divergence_fcfgapquantilelo_252d_jerk_v103_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(252, min_periods=63).quantile(0.1) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap high quantile
def f39ced_f39_cash_earnings_divergence_fcfgapquantilehi_504d_jerk_v104_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(504, min_periods=126).quantile(0.9) * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap low quantile
def f39ced_f39_cash_earnings_divergence_fcfgapquantilelo_504d_jerk_v105_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(504, min_periods=126).quantile(0.1) * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo gap high quantile
def f39ced_f39_cash_earnings_divergence_ncfogapquantilehi_252d_jerk_v106_signal(ncfo, netinc, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc).rolling(252, min_periods=63).quantile(0.9) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo gap low quantile
def f39ced_f39_cash_earnings_divergence_ncfogapquantilelo_252d_jerk_v107_signal(ncfo, netinc, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc).rolling(252, min_periods=63).quantile(0.1) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap iqr
def f39ced_f39_cash_earnings_divergence_fcfgapiqr_252d_jerk_v108_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    base = (gap.rolling(252, min_periods=63).quantile(0.75) - gap.rolling(252, min_periods=63).quantile(0.25)) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap iqr
def f39ced_f39_cash_earnings_divergence_fcfgapiqr_504d_jerk_v109_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    base = (gap.rolling(504, min_periods=126).quantile(0.75) - gap.rolling(504, min_periods=126).quantile(0.25)) * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap median
def f39ced_f39_cash_earnings_divergence_fcfgapmedian_252d_jerk_v110_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap median
def f39ced_f39_cash_earnings_divergence_fcfgapmedian_504d_jerk_v111_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(504, min_periods=126).median() * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap skew
def f39ced_f39_cash_earnings_divergence_fcfgapskew_252d_jerk_v112_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap skew
def f39ced_f39_cash_earnings_divergence_fcfgapskew_504d_jerk_v113_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(504, min_periods=126).skew() * closeadj
    result = _jerk(base, 63, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap kurt
def f39ced_f39_cash_earnings_divergence_fcfgapkurt_252d_jerk_v114_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(252, min_periods=63).kurt() * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap kurt
def f39ced_f39_cash_earnings_divergence_fcfgapkurt_504d_jerk_v115_signal(fcf, netinc, closeadj):
    base = _f39_cash_earnings_div(fcf, netinc).rolling(504, min_periods=126).kurt() * closeadj
    result = _jerk(base, 63, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap CV
def f39ced_f39_cash_earnings_divergence_fcfgapcv_252d_jerk_v116_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    base = (_std(gap, 252) / _mean(gap.abs(), 252).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap CV
def f39ced_f39_cash_earnings_divergence_fcfgapcv_504d_jerk_v117_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    base = (_std(gap, 504) / _mean(gap.abs(), 504).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d quality drag
def f39ced_f39_cash_earnings_divergence_qualitydrag_252d_jerk_v118_signal(fcf, netinc, closeadj):
    base = (-_f39_cash_earnings_div(fcf, netinc)).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d quality drag
def f39ced_f39_cash_earnings_divergence_qualitydrag_504d_jerk_v119_signal(fcf, netinc, closeadj):
    base = (-_f39_cash_earnings_div(fcf, netinc)).rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap × marketcap proxy
def f39ced_f39_cash_earnings_divergence_fcfgapxmc_252d_jerk_v120_signal(fcf, netinc, sharesbas, closeadj):
    mc = (closeadj * sharesbas).replace(0, np.nan)
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) * closeadj / mc
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap × marketcap proxy
def f39ced_f39_cash_earnings_divergence_fcfgapxmc_63d_jerk_v121_signal(fcf, netinc, sharesbas, closeadj):
    mc = (closeadj * sharesbas).replace(0, np.nan)
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) * closeadj / mc
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap × currentratio
def f39ced_f39_cash_earnings_divergence_fcfgapxcr_252d_jerk_v122_signal(fcf, netinc, currentratio, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) * currentratio * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap × currentratio
def f39ced_f39_cash_earnings_divergence_fcfgapxcr_63d_jerk_v123_signal(fcf, netinc, currentratio, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) * currentratio * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d relative gap intensity
def f39ced_f39_cash_earnings_divergence_relgapintensity_252d_jerk_v124_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc).abs()
    base = gap.rolling(252, min_periods=63).sum() / netinc.abs().rolling(252, min_periods=63).sum().replace(0, np.nan) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d relative gap intensity
def f39ced_f39_cash_earnings_divergence_relgapintensity_63d_jerk_v125_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc).abs()
    base = gap.rolling(63, min_periods=21).sum() / netinc.abs().rolling(63, min_periods=21).sum().replace(0, np.nan) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo relative intensity
def f39ced_f39_cash_earnings_divergence_ncforelintensity_252d_jerk_v126_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc).abs()
    base = gap.rolling(252, min_periods=63).sum() / netinc.abs().rolling(252, min_periods=63).sum().replace(0, np.nan) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo relative intensity
def f39ced_f39_cash_earnings_divergence_ncforelintensity_63d_jerk_v127_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc).abs()
    base = gap.rolling(63, min_periods=21).sum() / netinc.abs().rolling(63, min_periods=21).sum().replace(0, np.nan) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap persistence
def f39ced_f39_cash_earnings_divergence_fcfgappersist_252d_jerk_v128_signal(fcf, netinc, closeadj):
    delta = _diff(_mean(_f39_cash_earnings_div(fcf, netinc), 63), 21)
    base = _std(delta, 252) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d gap persistence
def f39ced_f39_cash_earnings_divergence_fcfgappersist_504d_jerk_v129_signal(fcf, netinc, closeadj):
    delta = _diff(_mean(_f39_cash_earnings_div(fcf, netinc), 126), 63)
    base = _std(delta, 504) * closeadj
    result = _jerk(base, 63, 63) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d cumulative ncfo coverage ratio
def f39ced_f39_cash_earnings_divergence_ncforatiocum_252d_jerk_v130_signal(ncfo, netinc, closeadj):
    cum_ncfo = ncfo.rolling(252, min_periods=63).sum()
    cum_ni = netinc.rolling(252, min_periods=63).sum()
    aux = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    base = (cum_ncfo / cum_ni.abs().replace(0, np.nan) - 1.0 + aux) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d cumulative ncfo coverage
def f39ced_f39_cash_earnings_divergence_ncforatiocum_504d_jerk_v131_signal(ncfo, netinc, closeadj):
    cum_ncfo = ncfo.rolling(504, min_periods=126).sum()
    cum_ni = netinc.rolling(504, min_periods=126).sum()
    aux = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    base = (cum_ncfo / cum_ni.abs().replace(0, np.nan) - 1.0 + aux) * closeadj
    result = _jerk(base, 63, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d cumulative fcf coverage
def f39ced_f39_cash_earnings_divergence_fcfratiocum_252d_jerk_v132_signal(fcf, netinc, closeadj):
    cum_fcf = fcf.rolling(252, min_periods=63).sum()
    cum_ni = netinc.rolling(252, min_periods=63).sum()
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    base = (cum_fcf / cum_ni.abs().replace(0, np.nan) - 1.0 + aux) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d cumulative fcf coverage
def f39ced_f39_cash_earnings_divergence_fcfratiocum_504d_jerk_v133_signal(fcf, netinc, closeadj):
    cum_fcf = fcf.rolling(504, min_periods=126).sum()
    cum_ni = netinc.rolling(504, min_periods=126).sum()
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    base = (cum_fcf / cum_ni.abs().replace(0, np.nan) - 1.0 + aux) * closeadj
    result = _jerk(base, 63, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EMA fcf ratio
def f39ced_f39_cash_earnings_divergence_fcfratioema_252d_jerk_v134_signal(fcf, netinc, closeadj):
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    base = (_safe_div(fcf, netinc) - 1.0 + aux).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EMA fcf ratio
def f39ced_f39_cash_earnings_divergence_fcfratioema_63d_jerk_v135_signal(fcf, netinc, closeadj):
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    base = (_safe_div(fcf, netinc) - 1.0 + aux).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap × ebitda growth
def f39ced_f39_cash_earnings_divergence_fcfgapebgrow_252d_jerk_v136_signal(fcf, netinc, ebitda, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) * ebitda.pct_change(252).fillna(0.0) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap × ebitda growth
def f39ced_f39_cash_earnings_divergence_fcfgapebgrow_63d_jerk_v137_signal(fcf, netinc, ebitda, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) * ebitda.pct_change(63).fillna(0.0) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d cum ncfo gap × eps
def f39ced_f39_cash_earnings_divergence_ncfocumxeps_252d_jerk_v138_signal(ncfo, netinc, eps, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc).rolling(252, min_periods=63).sum() * eps * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d cum ncfo gap × eps
def f39ced_f39_cash_earnings_divergence_ncfocumxeps_63d_jerk_v139_signal(ncfo, netinc, eps, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc).rolling(63, min_periods=21).sum() * eps * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap × debt change
def f39ced_f39_cash_earnings_divergence_fcfgapdebtchg_252d_jerk_v140_signal(fcf, netinc, debt, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 252) * debt.pct_change(252).fillna(0.0) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap × debt change
def f39ced_f39_cash_earnings_divergence_fcfgapdebtchg_63d_jerk_v141_signal(fcf, netinc, debt, closeadj):
    base = _mean(_f39_cash_earnings_div(fcf, netinc), 63) * debt.pct_change(63).fillna(0.0) * closeadj
    result = _jerk(base, 21, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/liabilities
def f39ced_f39_cash_earnings_divergence_fcfgaplia_252d_jerk_v142_signal(fcf, netinc, liabilities, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, liabilities), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/liabilities
def f39ced_f39_cash_earnings_divergence_fcfgaplia_63d_jerk_v143_signal(fcf, netinc, liabilities, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, liabilities), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap/retearn
def f39ced_f39_cash_earnings_divergence_fcfgapretearn_252d_jerk_v144_signal(fcf, netinc, retearn, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, retearn), 252) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap/retearn
def f39ced_f39_cash_earnings_divergence_fcfgapretearn_63d_jerk_v145_signal(fcf, netinc, retearn, closeadj):
    base = _mean(_f39_cash_earnings_div_norm(fcf, netinc, retearn), 63) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gap z × ebitda growth
def f39ced_f39_cash_earnings_divergence_fcfgapzxgrow_252d_jerk_v146_signal(fcf, netinc, ebitda, closeadj):
    z = _z(_mean(_f39_cash_earnings_div(fcf, netinc), 63), 252)
    base = z * ebitda.pct_change(252).fillna(0.0) * closeadj
    result = _jerk(base, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d gap z × revenue growth
def f39ced_f39_cash_earnings_divergence_fcfgapzxrev_63d_jerk_v147_signal(fcf, netinc, revenue, closeadj):
    z = _z(_mean(_f39_cash_earnings_div(fcf, netinc), 21), 63)
    base = z * revenue.pct_change(63).fillna(0.0) * closeadj
    result = _jerk(base, 21, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d combined gap (fcf + ncfo gaps)
def f39ced_f39_cash_earnings_divergence_combinedgap_252d_jerk_v148_signal(fcf, ncfo, netinc, closeadj):
    combined = _f39_cash_earnings_div(fcf, netinc) + _f39_ncfo_minus_netinc(ncfo, netinc)
    base = _mean(combined, 252) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d net-of-capex quality
def f39ced_f39_cash_earnings_divergence_netofcapex_252d_jerk_v149_signal(ncfo, netinc, capex, closeadj):
    base = _mean(_f39_ncfo_minus_netinc(ncfo, netinc) - capex.abs(), 252) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ultimate composite
def f39ced_f39_cash_earnings_divergence_ultimatecomposite_252d_jerk_v150_signal(fcf, ncfo, netinc, revenue, closeadj):
    fcf_gap = _f39_cash_earnings_div_norm(fcf, netinc, revenue)
    ncfo_gap = _f39_ncfo_minus_netinc(ncfo, netinc) / revenue.abs().replace(0, np.nan)
    combined = fcf_gap + ncfo_gap
    base = _mean(combined, 252) * revenue.pct_change(252).fillna(0.0) * closeadj
    result = _jerk(base, 63, 21) / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39ced_f39_cash_earnings_divergence_fcfgap_21d_jerk_v001_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_21d_jerk_v002_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_63d_jerk_v003_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_63d_jerk_v004_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_126d_jerk_v005_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_126d_jerk_v006_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_252d_jerk_v007_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_252d_jerk_v008_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_504d_jerk_v009_signal,
    f39ced_f39_cash_earnings_divergence_fcfgap_504d_jerk_v010_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapnorm_63d_jerk_v011_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapnorm_252d_jerk_v012_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_63d_jerk_v013_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_126d_jerk_v014_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_252d_jerk_v015_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_252d_jerk_v016_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_504d_jerk_v017_signal,
    f39ced_f39_cash_earnings_divergence_ncfogap_504d_jerk_v018_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapstd_63d_jerk_v019_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapstd_252d_jerk_v020_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapz_252d_jerk_v021_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapz_504d_jerk_v022_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapz_252d_jerk_v023_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapz_504d_jerk_v024_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapassets_63d_jerk_v025_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapassets_252d_jerk_v026_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaprev_63d_jerk_v027_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaprev_252d_jerk_v028_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapeq_63d_jerk_v029_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapeq_252d_jerk_v030_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapassets_63d_jerk_v031_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapassets_252d_jerk_v032_signal,
    f39ced_f39_cash_earnings_divergence_ncfogaprev_63d_jerk_v033_signal,
    f39ced_f39_cash_earnings_divergence_ncfogaprev_252d_jerk_v034_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapebitda_252d_jerk_v035_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapebitda_63d_jerk_v036_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxrev_63d_jerk_v037_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxrev_252d_jerk_v038_signal,
    f39ced_f39_cash_earnings_divergence_fcfratio_252d_jerk_v039_signal,
    f39ced_f39_cash_earnings_divergence_fcfratio_63d_jerk_v040_signal,
    f39ced_f39_cash_earnings_divergence_ncforatio_252d_jerk_v041_signal,
    f39ced_f39_cash_earnings_divergence_ncforatio_63d_jerk_v042_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapexp_jerk_v043_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapexp_jerk_v044_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsum_63d_jerk_v045_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsum_252d_jerk_v046_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsum_504d_jerk_v047_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapsum_63d_jerk_v048_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapsum_252d_jerk_v049_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapema_252d_jerk_v050_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapema_63d_jerk_v051_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapema_252d_jerk_v052_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapema_63d_jerk_v053_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxni_252d_jerk_v054_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxrevcur_63d_jerk_v055_signal,
    f39ced_f39_cash_earnings_divergence_cumcoverage_252d_jerk_v056_signal,
    f39ced_f39_cash_earnings_divergence_cumcoverage_504d_jerk_v057_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxeps_252d_jerk_v058_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxeps_63d_jerk_v059_signal,
    f39ced_f39_cash_earnings_divergence_fcfgappershare_252d_jerk_v060_signal,
    f39ced_f39_cash_earnings_divergence_fcfgappershare_63d_jerk_v061_signal,
    f39ced_f39_cash_earnings_divergence_ncfogappershare_252d_jerk_v062_signal,
    f39ced_f39_cash_earnings_divergence_ncfogappershare_63d_jerk_v063_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxdebt_252d_jerk_v064_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxdebt_63d_jerk_v065_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxcapex_252d_jerk_v066_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxcapex_63d_jerk_v067_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsignmag_252d_jerk_v068_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsignmag_63d_jerk_v069_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsnr_504d_jerk_v070_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapsnr_252d_jerk_v071_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapsnr_252d_jerk_v072_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapsnr_504d_jerk_v073_signal,
    f39ced_f39_cash_earnings_divergence_fcfvsncfogap_252d_jerk_v074_signal,
    f39ced_f39_cash_earnings_divergence_fcfvsncfogap_63d_jerk_v075_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxwc_252d_jerk_v076_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxwc_63d_jerk_v077_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapexpz_jerk_v078_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapexpz_jerk_v079_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapcomposite_252d_jerk_v080_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapcomposite_63d_jerk_v081_signal,
    f39ced_f39_cash_earnings_divergence_qualitycomposite_252d_jerk_v082_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapz_63d_jerk_v083_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapz_126d_jerk_v084_signal,
    f39ced_f39_cash_earnings_divergence_posdivfreq_252d_jerk_v085_signal,
    f39ced_f39_cash_earnings_divergence_posdivfreq_504d_jerk_v086_signal,
    f39ced_f39_cash_earnings_divergence_posncfofreq_252d_jerk_v087_signal,
    f39ced_f39_cash_earnings_divergence_posncfofreq_504d_jerk_v088_signal,
    f39ced_f39_cash_earnings_divergence_fcfposnegratio_252d_jerk_v089_signal,
    f39ced_f39_cash_earnings_divergence_fcfposnegratio_63d_jerk_v090_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapchg_252d_jerk_v091_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapchg_63d_jerk_v092_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapdelta_252d_jerk_v093_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapdelta_63d_jerk_v094_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapopinc_252d_jerk_v095_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapopinc_63d_jerk_v096_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapgp_252d_jerk_v097_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapgp_63d_jerk_v098_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaparea_252d_jerk_v099_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaparea_63d_jerk_v100_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaparea_504d_jerk_v101_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapquantilehi_252d_jerk_v102_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapquantilelo_252d_jerk_v103_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapquantilehi_504d_jerk_v104_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapquantilelo_504d_jerk_v105_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapquantilehi_252d_jerk_v106_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapquantilelo_252d_jerk_v107_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapiqr_252d_jerk_v108_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapiqr_504d_jerk_v109_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapmedian_252d_jerk_v110_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapmedian_504d_jerk_v111_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapskew_252d_jerk_v112_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapskew_504d_jerk_v113_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapkurt_252d_jerk_v114_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapkurt_504d_jerk_v115_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapcv_252d_jerk_v116_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapcv_504d_jerk_v117_signal,
    f39ced_f39_cash_earnings_divergence_qualitydrag_252d_jerk_v118_signal,
    f39ced_f39_cash_earnings_divergence_qualitydrag_504d_jerk_v119_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxmc_252d_jerk_v120_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxmc_63d_jerk_v121_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxcr_252d_jerk_v122_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxcr_63d_jerk_v123_signal,
    f39ced_f39_cash_earnings_divergence_relgapintensity_252d_jerk_v124_signal,
    f39ced_f39_cash_earnings_divergence_relgapintensity_63d_jerk_v125_signal,
    f39ced_f39_cash_earnings_divergence_ncforelintensity_252d_jerk_v126_signal,
    f39ced_f39_cash_earnings_divergence_ncforelintensity_63d_jerk_v127_signal,
    f39ced_f39_cash_earnings_divergence_fcfgappersist_252d_jerk_v128_signal,
    f39ced_f39_cash_earnings_divergence_fcfgappersist_504d_jerk_v129_signal,
    f39ced_f39_cash_earnings_divergence_ncforatiocum_252d_jerk_v130_signal,
    f39ced_f39_cash_earnings_divergence_ncforatiocum_504d_jerk_v131_signal,
    f39ced_f39_cash_earnings_divergence_fcfratiocum_252d_jerk_v132_signal,
    f39ced_f39_cash_earnings_divergence_fcfratiocum_504d_jerk_v133_signal,
    f39ced_f39_cash_earnings_divergence_fcfratioema_252d_jerk_v134_signal,
    f39ced_f39_cash_earnings_divergence_fcfratioema_63d_jerk_v135_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapebgrow_252d_jerk_v136_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapebgrow_63d_jerk_v137_signal,
    f39ced_f39_cash_earnings_divergence_ncfocumxeps_252d_jerk_v138_signal,
    f39ced_f39_cash_earnings_divergence_ncfocumxeps_63d_jerk_v139_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapdebtchg_252d_jerk_v140_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapdebtchg_63d_jerk_v141_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaplia_252d_jerk_v142_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaplia_63d_jerk_v143_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapretearn_252d_jerk_v144_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapretearn_63d_jerk_v145_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapzxgrow_252d_jerk_v146_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapzxrev_63d_jerk_v147_signal,
    f39ced_f39_cash_earnings_divergence_combinedgap_252d_jerk_v148_signal,
    f39ced_f39_cash_earnings_divergence_netofcapex_252d_jerk_v149_signal,
    f39ced_f39_cash_earnings_divergence_ultimatecomposite_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_CASH_EARNINGS_DIVERGENCE_REGISTRY_JERK = REGISTRY


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
    opinc = pd.Series(1.3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="opinc")
    gp = pd.Series(4.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="gp")
    liabilities = pd.Series(3.0e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="liabilities")
    retearn = pd.Series(2.5e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="retearn")
    currentratio = pd.Series(1.5 + 0.3 * np.cumsum(np.random.normal(0, 0.001, n)), name="currentratio")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "assets": assets, "equity": equity, "debt": debt,
        "capex": capex, "eps": eps, "sharesbas": sharesbas, "ebitda": ebitda,
        "workingcapital": workingcapital, "opinc": opinc, "gp": gp,
        "liabilities": liabilities, "retearn": retearn, "currentratio": currentratio,
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f39_cash_earnings_divergence_3rd_derivatives_001_150_claude: {n_features} features pass")
