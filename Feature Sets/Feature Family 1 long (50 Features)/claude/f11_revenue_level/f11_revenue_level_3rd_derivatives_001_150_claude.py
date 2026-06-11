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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f11_revenue_level_scaled(revenue, scale):
    return revenue / scale.replace(0, np.nan).abs()


def _f11_revenue_level_log(revenue):
    return np.log(revenue.abs().replace(0, np.nan))


def _f11_revenue_per_share(revenue, sharesbas):
    return revenue / sharesbas.replace(0, np.nan).abs()


# 5d jerk of 21d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_21d_jerk_v001_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_21d_jerk_v002_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 63d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_63d_jerk_v003_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_63d_jerk_v004_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_63d_jerk_v005_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_126d_jerk_v006_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_126d_jerk_v007_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_252d_jerk_v008_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_252d_jerk_v009_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d revenue per share x closeadj
def f11rl_f11_revenue_level_revps_504d_jerk_v010_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d log revenue x closeadj
def f11rl_f11_revenue_level_logrev_21d_jerk_v011_signal(revenue, closeadj):
    base = _mean(_f11_revenue_level_log(revenue), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d log revenue x closeadj
def f11rl_f11_revenue_level_logrev_63d_jerk_v012_signal(revenue, closeadj):
    base = _mean(_f11_revenue_level_log(revenue), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d log revenue x closeadj
def f11rl_f11_revenue_level_logrev_252d_jerk_v013_signal(revenue, closeadj):
    base = _mean(_f11_revenue_level_log(revenue), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d revenue/marketcap x closeadj
def f11rl_f11_revenue_level_revtomc_21d_jerk_v014_signal(revenue, marketcap, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, marketcap), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d revenue/marketcap x closeadj
def f11rl_f11_revenue_level_revtomc_63d_jerk_v015_signal(revenue, marketcap, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, marketcap), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d revenue/marketcap x closeadj
def f11rl_f11_revenue_level_revtomc_252d_jerk_v016_signal(revenue, marketcap, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, marketcap), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d revenue/assets x closeadj
def f11rl_f11_revenue_level_revtoassets_63d_jerk_v017_signal(revenue, assets, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, assets), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d revenue/assets x closeadj
def f11rl_f11_revenue_level_revtoassets_252d_jerk_v018_signal(revenue, assets, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, assets), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d revenue/equity x closeadj
def f11rl_f11_revenue_level_revtoequity_63d_jerk_v019_signal(revenue, equity, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, equity), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d revenue/equity x closeadj
def f11rl_f11_revenue_level_revtoequity_252d_jerk_v020_signal(revenue, equity, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, equity), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of revps x closeadj
def f11rl_f11_revenue_level_revpsxprice_21d_jerk_v021_signal(revenue, sharesbas, closeadj):
    base = _f11_revenue_per_share(revenue, sharesbas) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps x closeadj
def f11rl_f11_revenue_level_revpsxprice_21d_jerk_v022_signal(revenue, sharesbas, closeadj):
    base = _f11_revenue_per_share(revenue, sharesbas) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d revps x closeadj
def f11rl_f11_revenue_level_revpsxprice_252d_jerk_v023_signal(revenue, sharesbas, closeadj):
    base = _mean(_f11_revenue_per_share(revenue, sharesbas) * closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps std 63d x closeadj
def f11rl_f11_revenue_level_revpsstd_63d_jerk_v024_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _std(rps, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps std 252d x closeadj
def f11rl_f11_revenue_level_revpsstd_252d_jerk_v025_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _std(rps, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps z 252d
def f11rl_f11_revenue_level_revpsz_252d_jerk_v026_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _z(rps, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps z 504d
def f11rl_f11_revenue_level_revpsz_504d_jerk_v027_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _z(rps, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log rev z 252d
def f11rl_f11_revenue_level_logrevz_252d_jerk_v028_signal(revenue, closeadj):
    lr = _f11_revenue_level_log(revenue)
    base = _z(lr, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log rev z 504d
def f11rl_f11_revenue_level_logrevz_504d_jerk_v029_signal(revenue, closeadj):
    lr = _f11_revenue_level_log(revenue)
    base = _z(lr, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/mc z 252d
def f11rl_f11_revenue_level_revtomcz_252d_jerk_v030_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    base = _z(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/assets z 252d
def f11rl_f11_revenue_level_revtoassetsz_252d_jerk_v031_signal(revenue, assets, closeadj):
    r = _f11_revenue_level_scaled(revenue, assets)
    base = _z(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps^2 63d x closeadj
def f11rl_f11_revenue_level_revpssq_63d_jerk_v032_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * rps, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps^2 252d x closeadj
def f11rl_f11_revenue_level_revpssq_252d_jerk_v033_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * rps, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revenue/debt 63d x closeadj
def f11rl_f11_revenue_level_revtodebt_63d_jerk_v034_signal(revenue, debt, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, debt), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revenue/debt 252d x closeadj
def f11rl_f11_revenue_level_revtodebt_252d_jerk_v035_signal(revenue, debt, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, debt), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revenue/liab 63d x closeadj
def f11rl_f11_revenue_level_revtoliab_63d_jerk_v036_signal(revenue, liabilities, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, liabilities), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revenue/liab 252d x closeadj
def f11rl_f11_revenue_level_revtoliab_252d_jerk_v037_signal(revenue, liabilities, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, liabilities), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revenue/capex 63d x closeadj
def f11rl_f11_revenue_level_revtocapex_63d_jerk_v038_signal(revenue, capex, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, capex), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revenue/capex 252d x closeadj
def f11rl_f11_revenue_level_revtocapex_252d_jerk_v039_signal(revenue, capex, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, capex), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revenue/ebitda 63d
def f11rl_f11_revenue_level_revtoebitda_63d_jerk_v040_signal(revenue, ebitda, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, ebitda), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revenue/ebitda 252d
def f11rl_f11_revenue_level_revtoebitda_252d_jerk_v041_signal(revenue, ebitda, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, ebitda), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps norm 252d
def f11rl_f11_revenue_level_revpsnorm_252d_jerk_v042_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps, 252) / np.sqrt(252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev relative 504d
def f11rl_f11_revenue_level_revrel_504d_jerk_v043_signal(revenue, closeadj):
    base_rev = _mean(revenue, 504).replace(0, np.nan)
    base = (revenue / base_rev.abs()) * closeadj + _f11_revenue_level_scaled(revenue, closeadj) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revrel max 252d
def f11rl_f11_revenue_level_revrelmax_252d_jerk_v044_signal(revenue, closeadj):
    peak = revenue.rolling(252, min_periods=63).max().replace(0, np.nan)
    base = (revenue / peak.abs()) * closeadj + _f11_revenue_level_scaled(revenue, closeadj) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revrel max 504d
def f11rl_f11_revenue_level_revrelmax_504d_jerk_v045_signal(revenue, closeadj):
    peak = revenue.rolling(504, min_periods=126).max().replace(0, np.nan)
    base = (revenue / peak.abs()) * closeadj + _f11_revenue_level_scaled(revenue, closeadj) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x mc 21d
def f11rl_f11_revenue_level_revpsxmc_21d_jerk_v046_signal(revenue, sharesbas, marketcap):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * marketcap, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x mc 63d
def f11rl_f11_revenue_level_revpsxmc_63d_jerk_v047_signal(revenue, sharesbas, marketcap):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * marketcap, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x mc 252d
def f11rl_f11_revenue_level_revpsxmc_252d_jerk_v048_signal(revenue, sharesbas, marketcap):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * marketcap, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/sqrt(assets) 63d
def f11rl_f11_revenue_level_revtosqrtassets_63d_jerk_v049_signal(revenue, assets, closeadj):
    sa = np.sqrt(assets.abs().replace(0, np.nan))
    base = _mean(revenue / sa, 63) * closeadj + _f11_revenue_level_scaled(revenue, sa) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/sqrt(assets) 252d
def f11rl_f11_revenue_level_revtosqrtassets_252d_jerk_v050_signal(revenue, assets, closeadj):
    sa = np.sqrt(assets.abs().replace(0, np.nan))
    base = _mean(revenue / sa, 252) * closeadj + _f11_revenue_level_scaled(revenue, sa) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log(rev)+log(ebitda) 21d
def f11rl_f11_revenue_level_revxebitda_21d_jerk_v051_signal(revenue, ebitda, closeadj):
    base = _mean(_f11_revenue_level_log(revenue) + _f11_revenue_level_log(ebitda), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log(rev)+log(ebitda) 252d
def f11rl_f11_revenue_level_revxebitda_252d_jerk_v052_signal(revenue, ebitda, closeadj):
    base = _mean(_f11_revenue_level_log(revenue) + _f11_revenue_level_log(ebitda), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps anomaly 252d
def f11rl_f11_revenue_level_revpsanomaly_252d_jerk_v053_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = (rps - _mean(rps, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps anomaly 504d
def f11rl_f11_revenue_level_revpsanomaly_504d_jerk_v054_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = (rps - _mean(rps, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps composite 63d
def f11rl_f11_revenue_level_revcomp_63d_jerk_v055_signal(revenue, sharesbas, marketcap, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    rmc = _f11_revenue_level_scaled(revenue, marketcap)
    base = _mean(rps + rmc * 1e8, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x ebitda 63d
def f11rl_f11_revenue_level_revpsxebitda_63d_jerk_v056_signal(revenue, sharesbas, ebitda):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * ebitda, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x ebitda 252d
def f11rl_f11_revenue_level_revpsxebitda_252d_jerk_v057_signal(revenue, sharesbas, ebitda):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * ebitda, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x opinc 63d
def f11rl_f11_revenue_level_revpsxopinc_63d_jerk_v058_signal(revenue, sharesbas, opinc):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * opinc, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x opinc 252d
def f11rl_f11_revenue_level_revpsxopinc_252d_jerk_v059_signal(revenue, sharesbas, opinc):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * opinc, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x gp 63d
def f11rl_f11_revenue_level_revpsxgp_63d_jerk_v060_signal(revenue, sharesbas, gp):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * gp, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x gp 252d
def f11rl_f11_revenue_level_revpsxgp_252d_jerk_v061_signal(revenue, sharesbas, gp):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * gp, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revrank 252d
def f11rl_f11_revenue_level_revrank_252d_jerk_v062_signal(revenue, closeadj):
    rk = revenue.rolling(252, min_periods=63).rank(pct=True)
    base = rk * closeadj + _f11_revenue_level_scaled(revenue, closeadj) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revrank 504d
def f11rl_f11_revenue_level_revrank_504d_jerk_v063_signal(revenue, closeadj):
    rk = revenue.rolling(504, min_periods=126).rank(pct=True)
    base = rk * closeadj + _f11_revenue_level_scaled(revenue, closeadj) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x retearn 63d
def f11rl_f11_revenue_level_revpsxretearn_63d_jerk_v064_signal(revenue, sharesbas, retearn):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * retearn, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x retearn 252d
def f11rl_f11_revenue_level_revpsxretearn_252d_jerk_v065_signal(revenue, sharesbas, retearn):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * retearn, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/wc 63d
def f11rl_f11_revenue_level_revtowc_63d_jerk_v066_signal(revenue, workingcapital, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, workingcapital), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/wc 252d
def f11rl_f11_revenue_level_revtowc_252d_jerk_v067_signal(revenue, workingcapital, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, workingcapital), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/intexp 63d
def f11rl_f11_revenue_level_revtoint_63d_jerk_v068_signal(revenue, intexp, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, intexp), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/intexp 252d
def f11rl_f11_revenue_level_revtoint_252d_jerk_v069_signal(revenue, intexp, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, intexp), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x equity 63d
def f11rl_f11_revenue_level_revpsxequity_63d_jerk_v070_signal(revenue, sharesbas, equity):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * equity, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x equity 252d
def f11rl_f11_revenue_level_revpsxequity_252d_jerk_v071_signal(revenue, sharesbas, equity):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * equity, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log(rev)-log(assets) 63d
def f11rl_f11_revenue_level_logrevminuslogassets_63d_jerk_v072_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    base = _mean(lr - la, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log(rev)-log(assets) 252d
def f11rl_f11_revenue_level_logrevminuslogassets_252d_jerk_v073_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    base = _mean(lr - la, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x sharesbas 63d
def f11rl_f11_revenue_level_revpsxshares_63d_jerk_v074_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * sharesbas, 63) * closeadj * 1e-9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x sharesbas 252d
def f11rl_f11_revenue_level_revpsxshares_252d_jerk_v075_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * sharesbas, 252) * closeadj * 1e-9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x eps 63d
def f11rl_f11_revenue_level_revpsxeps_63d_jerk_v076_signal(revenue, sharesbas, eps):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * eps, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x eps 252d
def f11rl_f11_revenue_level_revpsxeps_252d_jerk_v077_signal(revenue, sharesbas, eps):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * eps, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x ncfo 63d
def f11rl_f11_revenue_level_revpsxncfo_63d_jerk_v078_signal(revenue, sharesbas, ncfo):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * ncfo, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x ncfo 252d
def f11rl_f11_revenue_level_revpsxncfo_252d_jerk_v079_signal(revenue, sharesbas, ncfo):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * ncfo, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x fcf 63d
def f11rl_f11_revenue_level_revpsxfcf_63d_jerk_v080_signal(revenue, sharesbas, fcf):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * fcf, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x fcf 252d
def f11rl_f11_revenue_level_revpsxfcf_252d_jerk_v081_signal(revenue, sharesbas, fcf):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * fcf, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log rev 504d x closeadj
def f11rl_f11_revenue_level_logrev_504d_jerk_v082_signal(revenue, closeadj):
    base = _mean(_f11_revenue_level_log(revenue), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps 504d x closeadj
def f11rl_f11_revenue_level_revps_504d_jerk_v083_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/ev 252d
def f11rl_f11_revenue_level_revtoev_252d_jerk_v084_signal(revenue, marketcap, debt, closeadj):
    ev = marketcap + debt
    base = _mean(_f11_revenue_level_scaled(revenue, ev), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding log revenue x closeadj
def f11rl_f11_revenue_level_logrevexp_jerk_v085_signal(revenue, closeadj):
    base = _f11_revenue_level_log(revenue).expanding(min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revenue median 63d x closeadj
def f11rl_f11_revenue_level_revmedian_63d_jerk_v086_signal(revenue, closeadj):
    rps = _f11_revenue_level_log(revenue)
    base = rps.rolling(63, min_periods=21).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revenue median 252d x closeadj
def f11rl_f11_revenue_level_revmedian_252d_jerk_v087_signal(revenue, closeadj):
    rps = _f11_revenue_level_log(revenue)
    base = rps.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps IQR 252d x closeadj
def f11rl_f11_revenue_level_revpsiqr_252d_jerk_v088_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    q3 = rps.rolling(252, min_periods=63).quantile(0.75)
    q1 = rps.rolling(252, min_periods=63).quantile(0.25)
    base = (q3 - q1) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps skew 252d x closeadj
def f11rl_f11_revenue_level_revpsskew_252d_jerk_v089_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps kurt 252d x closeadj
def f11rl_f11_revenue_level_revpskurt_252d_jerk_v090_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.rolling(252, min_periods=63).kurt() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/mc rank 252d
def f11rl_f11_revenue_level_revtomcrank_252d_jerk_v091_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    base = r.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/mc rank 504d
def f11rl_f11_revenue_level_revtomcrank_504d_jerk_v092_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    base = r.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log(rev)-log(debt) 252d
def f11rl_f11_revenue_level_logrevminusdebt_252d_jerk_v093_signal(revenue, debt, closeadj):
    lr = _f11_revenue_level_log(revenue)
    ld = np.log(debt.abs().replace(0, np.nan))
    base = _mean(lr - ld, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log(rev)-log(equity) 252d
def f11rl_f11_revenue_level_logrevminusequity_252d_jerk_v094_signal(revenue, equity, closeadj):
    lr = _f11_revenue_level_log(revenue)
    le = np.log(equity.abs().replace(0, np.nan))
    base = _mean(lr - le, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps min 63d x closeadj
def f11rl_f11_revenue_level_revpsmin_63d_jerk_v095_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps max 252d x closeadj
def f11rl_f11_revenue_level_revpsmax_252d_jerk_v096_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps relmax 504d x closeadj
def f11rl_f11_revenue_level_revpsrelmax_504d_jerk_v097_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    peak = rps.rolling(504, min_periods=126).max().replace(0, np.nan)
    base = (rps / peak.abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps relmin 504d x closeadj
def f11rl_f11_revenue_level_revpsrelmin_504d_jerk_v098_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    trough = rps.rolling(504, min_periods=126).min().replace(0, np.nan)
    base = (rps / trough.abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of count rev/mc>0.05 252d
def f11rl_f11_revenue_level_revtomcabove5_252d_jerk_v099_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    base = (r).rolling(252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of count rev/mc>0.10 504d
def f11rl_f11_revenue_level_revtomcabove10_504d_jerk_v100_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    base = (r).rolling(504, min_periods=126).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of count revps>mean 252d
def f11rl_f11_revenue_level_revpsabovemean_252d_jerk_v101_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    flag = (rps > _mean(rps, 252)).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log rev z 126d
def f11rl_f11_revenue_level_logrevz_126d_jerk_v102_signal(revenue, closeadj):
    lr = _f11_revenue_level_log(revenue)
    base = _z(lr, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps z 126d
def f11rl_f11_revenue_level_revpsz_126d_jerk_v103_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _z(rps, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/mc z 504d
def f11rl_f11_revenue_level_revtomcz_504d_jerk_v104_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    base = _z(r, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/assets z 504d
def f11rl_f11_revenue_level_revtoassetsz_504d_jerk_v105_signal(revenue, assets, closeadj):
    r = _f11_revenue_level_scaled(revenue, assets)
    base = _z(r, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/equity z 252d
def f11rl_f11_revenue_level_revtoequityz_252d_jerk_v106_signal(revenue, equity, closeadj):
    r = _f11_revenue_level_scaled(revenue, equity)
    base = _z(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log revps 21d
def f11rl_f11_revenue_level_logrevps_21d_jerk_v107_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = np.log(rps.abs().replace(0, np.nan))
    base = _mean(lr, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log revps 63d
def f11rl_f11_revenue_level_logrevps_63d_jerk_v108_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = np.log(rps.abs().replace(0, np.nan))
    base = _mean(lr, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log revps 252d
def f11rl_f11_revenue_level_logrevps_252d_jerk_v109_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = np.log(rps.abs().replace(0, np.nan))
    base = _mean(lr, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps EMA 21d x closeadj
def f11rl_f11_revenue_level_revpsema_21d_jerk_v110_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps EMA 63d x closeadj
def f11rl_f11_revenue_level_revpsema_63d_jerk_v111_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps EMA 252d x closeadj
def f11rl_f11_revenue_level_revpsema_252d_jerk_v112_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log rev EMA 63d x closeadj
def f11rl_f11_revenue_level_logrevema_63d_jerk_v113_signal(revenue, closeadj):
    lr = _f11_revenue_level_log(revenue)
    base = lr.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log rev EMA 252d x closeadj
def f11rl_f11_revenue_level_logrevema_252d_jerk_v114_signal(revenue, closeadj):
    lr = _f11_revenue_level_log(revenue)
    base = lr.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/cap base 252d
def f11rl_f11_revenue_level_revtocapbase_252d_jerk_v115_signal(revenue, marketcap, debt, equity, closeadj):
    base_capital = marketcap + debt + equity
    base = _mean(_f11_revenue_level_scaled(revenue, base_capital), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/lev base 63d
def f11rl_f11_revenue_level_revtolevbase_63d_jerk_v116_signal(revenue, assets, debt, closeadj):
    base_lev = assets + debt
    base = _mean(_f11_revenue_level_scaled(revenue, base_lev), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/lev base 252d
def f11rl_f11_revenue_level_revtolevbase_252d_jerk_v117_signal(revenue, assets, debt, closeadj):
    base_lev = assets + debt
    base = _mean(_f11_revenue_level_scaled(revenue, base_lev), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rps x current 63d
def f11rl_f11_revenue_level_revpsxcurrent_63d_jerk_v118_signal(revenue, sharesbas, currentratio, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * (1.0 + currentratio), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rps x current 252d
def f11rl_f11_revenue_level_revpsxcurrent_252d_jerk_v119_signal(revenue, sharesbas, currentratio, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps * (1.0 + currentratio), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/|netinc| 63d
def f11rl_f11_revenue_level_revtoni_63d_jerk_v120_signal(revenue, netinc, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, netinc.abs()), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/|netinc| 252d
def f11rl_f11_revenue_level_revtoni_252d_jerk_v121_signal(revenue, netinc, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, netinc.abs()), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/|ncfo| 252d
def f11rl_f11_revenue_level_revtoncfo_252d_jerk_v122_signal(revenue, ncfo, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, ncfo.abs()), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/|fcf| 252d
def f11rl_f11_revenue_level_revtofcf_252d_jerk_v123_signal(revenue, fcf, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, fcf.abs()), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/gp 63d
def f11rl_f11_revenue_level_revtogp_63d_jerk_v124_signal(revenue, gp, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, gp), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/gp 252d
def f11rl_f11_revenue_level_revtogp_252d_jerk_v125_signal(revenue, gp, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, gp), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/opinc 252d
def f11rl_f11_revenue_level_revtoopinc_252d_jerk_v126_signal(revenue, opinc, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, opinc), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/sharesbas 504d
def f11rl_f11_revenue_level_revtoshares_504d_jerk_v127_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = _mean(rps, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log(rev) x log(equity) 63d
def f11rl_f11_revenue_level_revxequity_63d_jerk_v128_signal(revenue, equity, closeadj):
    lr = _f11_revenue_level_log(revenue)
    le = np.log(equity.abs().replace(0, np.nan))
    base = _mean(lr * le, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log(rev) x log(equity) 252d
def f11rl_f11_revenue_level_revxequity_252d_jerk_v129_signal(revenue, equity, closeadj):
    lr = _f11_revenue_level_log(revenue)
    le = np.log(equity.abs().replace(0, np.nan))
    base = _mean(lr * le, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log(rev) x log(assets) 63d
def f11rl_f11_revenue_level_revxassets_63d_jerk_v130_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    base = _mean(lr * la, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log(rev) x log(assets) 252d
def f11rl_f11_revenue_level_revxassets_252d_jerk_v131_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    base = _mean(lr * la, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/sqrt(equity) 63d
def f11rl_f11_revenue_level_revtosqrtequity_63d_jerk_v132_signal(revenue, equity, closeadj):
    se = np.sqrt(equity.abs().replace(0, np.nan))
    base = _mean(revenue / se, 63) * closeadj + _f11_revenue_level_scaled(revenue, se) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/sqrt(equity) 252d
def f11rl_f11_revenue_level_revtosqrtequity_252d_jerk_v133_signal(revenue, equity, closeadj):
    se = np.sqrt(equity.abs().replace(0, np.nan))
    base = _mean(revenue / se, 252) * closeadj + _f11_revenue_level_scaled(revenue, se) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/sqrt(mc) 252d
def f11rl_f11_revenue_level_revtosqrtmc_252d_jerk_v134_signal(revenue, marketcap, closeadj):
    sm = np.sqrt(marketcap.abs().replace(0, np.nan))
    base = _mean(revenue / sm, 252) * closeadj + _f11_revenue_level_scaled(revenue, sm) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev change 21d x closeadj
def f11rl_f11_revenue_level_revchg_21d_jerk_v135_signal(revenue, closeadj):
    base = _diff(_f11_revenue_level_log(revenue), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev change 63d x closeadj
def f11rl_f11_revenue_level_revchg_63d_jerk_v136_signal(revenue, closeadj):
    base = _diff(_f11_revenue_level_log(revenue), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev change 252d x closeadj
def f11rl_f11_revenue_level_revchg_252d_jerk_v137_signal(revenue, closeadj):
    base = _diff(_f11_revenue_level_log(revenue), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps annualized 252d
def f11rl_f11_revenue_level_revpsann_252d_jerk_v138_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = (rps * np.sqrt(252.0)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rev/mc annualized 252d
def f11rl_f11_revenue_level_revtomcann_252d_jerk_v139_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    base = (r * np.sqrt(252.0)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps composite 63d
def f11rl_f11_revenue_level_revpscomposite_63d_jerk_v140_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = _f11_revenue_level_log(revenue)
    base = _mean(rps + lr, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps composite 252d
def f11rl_f11_revenue_level_revpscomposite_252d_jerk_v141_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = _f11_revenue_level_log(revenue)
    base = _mean(rps + lr, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of log(rev)+log(assets) 63d
def f11rl_f11_revenue_level_logrevxlogassets_63d_jerk_v142_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    base = _mean(lr + la, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log(rev)+log(mc) 252d
def f11rl_f11_revenue_level_logrevxlogmc_252d_jerk_v143_signal(revenue, marketcap, closeadj):
    lr = _f11_revenue_level_log(revenue)
    lm = np.log(marketcap.abs().replace(0, np.nan))
    base = _mean(lr + lm, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/|capex| 504d
def f11rl_f11_revenue_level_revtocapex_504d_jerk_v144_signal(revenue, capex, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, capex.abs()), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rev/|intexp| 504d
def f11rl_f11_revenue_level_revtoint_504d_jerk_v145_signal(revenue, intexp, closeadj):
    base = _mean(_f11_revenue_level_scaled(revenue, intexp.abs()), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps 3way 63d
def f11rl_f11_revenue_level_revps3way_63d_jerk_v146_signal(revenue, sharesbas, ebitda, equity):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    le = np.log(equity.abs().replace(0, np.nan))
    base = _mean(rps * ebitda * le, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps 3way 252d
def f11rl_f11_revenue_level_revps3way_252d_jerk_v147_signal(revenue, sharesbas, ebitda, equity):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    le = np.log(equity.abs().replace(0, np.nan))
    base = _mean(rps * ebitda * le, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps sum 63d x closeadj
def f11rl_f11_revenue_level_revpssum_63d_jerk_v148_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps sum 252d x closeadj
def f11rl_f11_revenue_level_revpssum_252d_jerk_v149_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps EMA 504d x closeadj
def f11rl_f11_revenue_level_revpsema_504d_jerk_v150_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    base = rps.ewm(span=504, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11rl_f11_revenue_level_revps_21d_jerk_v001_signal,
    f11rl_f11_revenue_level_revps_21d_jerk_v002_signal,
    f11rl_f11_revenue_level_revps_63d_jerk_v003_signal,
    f11rl_f11_revenue_level_revps_63d_jerk_v004_signal,
    f11rl_f11_revenue_level_revps_63d_jerk_v005_signal,
    f11rl_f11_revenue_level_revps_126d_jerk_v006_signal,
    f11rl_f11_revenue_level_revps_126d_jerk_v007_signal,
    f11rl_f11_revenue_level_revps_252d_jerk_v008_signal,
    f11rl_f11_revenue_level_revps_252d_jerk_v009_signal,
    f11rl_f11_revenue_level_revps_504d_jerk_v010_signal,
    f11rl_f11_revenue_level_logrev_21d_jerk_v011_signal,
    f11rl_f11_revenue_level_logrev_63d_jerk_v012_signal,
    f11rl_f11_revenue_level_logrev_252d_jerk_v013_signal,
    f11rl_f11_revenue_level_revtomc_21d_jerk_v014_signal,
    f11rl_f11_revenue_level_revtomc_63d_jerk_v015_signal,
    f11rl_f11_revenue_level_revtomc_252d_jerk_v016_signal,
    f11rl_f11_revenue_level_revtoassets_63d_jerk_v017_signal,
    f11rl_f11_revenue_level_revtoassets_252d_jerk_v018_signal,
    f11rl_f11_revenue_level_revtoequity_63d_jerk_v019_signal,
    f11rl_f11_revenue_level_revtoequity_252d_jerk_v020_signal,
    f11rl_f11_revenue_level_revpsxprice_21d_jerk_v021_signal,
    f11rl_f11_revenue_level_revpsxprice_21d_jerk_v022_signal,
    f11rl_f11_revenue_level_revpsxprice_252d_jerk_v023_signal,
    f11rl_f11_revenue_level_revpsstd_63d_jerk_v024_signal,
    f11rl_f11_revenue_level_revpsstd_252d_jerk_v025_signal,
    f11rl_f11_revenue_level_revpsz_252d_jerk_v026_signal,
    f11rl_f11_revenue_level_revpsz_504d_jerk_v027_signal,
    f11rl_f11_revenue_level_logrevz_252d_jerk_v028_signal,
    f11rl_f11_revenue_level_logrevz_504d_jerk_v029_signal,
    f11rl_f11_revenue_level_revtomcz_252d_jerk_v030_signal,
    f11rl_f11_revenue_level_revtoassetsz_252d_jerk_v031_signal,
    f11rl_f11_revenue_level_revpssq_63d_jerk_v032_signal,
    f11rl_f11_revenue_level_revpssq_252d_jerk_v033_signal,
    f11rl_f11_revenue_level_revtodebt_63d_jerk_v034_signal,
    f11rl_f11_revenue_level_revtodebt_252d_jerk_v035_signal,
    f11rl_f11_revenue_level_revtoliab_63d_jerk_v036_signal,
    f11rl_f11_revenue_level_revtoliab_252d_jerk_v037_signal,
    f11rl_f11_revenue_level_revtocapex_63d_jerk_v038_signal,
    f11rl_f11_revenue_level_revtocapex_252d_jerk_v039_signal,
    f11rl_f11_revenue_level_revtoebitda_63d_jerk_v040_signal,
    f11rl_f11_revenue_level_revtoebitda_252d_jerk_v041_signal,
    f11rl_f11_revenue_level_revpsnorm_252d_jerk_v042_signal,
    f11rl_f11_revenue_level_revrel_504d_jerk_v043_signal,
    f11rl_f11_revenue_level_revrelmax_252d_jerk_v044_signal,
    f11rl_f11_revenue_level_revrelmax_504d_jerk_v045_signal,
    f11rl_f11_revenue_level_revpsxmc_21d_jerk_v046_signal,
    f11rl_f11_revenue_level_revpsxmc_63d_jerk_v047_signal,
    f11rl_f11_revenue_level_revpsxmc_252d_jerk_v048_signal,
    f11rl_f11_revenue_level_revtosqrtassets_63d_jerk_v049_signal,
    f11rl_f11_revenue_level_revtosqrtassets_252d_jerk_v050_signal,
    f11rl_f11_revenue_level_revxebitda_21d_jerk_v051_signal,
    f11rl_f11_revenue_level_revxebitda_252d_jerk_v052_signal,
    f11rl_f11_revenue_level_revpsanomaly_252d_jerk_v053_signal,
    f11rl_f11_revenue_level_revpsanomaly_504d_jerk_v054_signal,
    f11rl_f11_revenue_level_revcomp_63d_jerk_v055_signal,
    f11rl_f11_revenue_level_revpsxebitda_63d_jerk_v056_signal,
    f11rl_f11_revenue_level_revpsxebitda_252d_jerk_v057_signal,
    f11rl_f11_revenue_level_revpsxopinc_63d_jerk_v058_signal,
    f11rl_f11_revenue_level_revpsxopinc_252d_jerk_v059_signal,
    f11rl_f11_revenue_level_revpsxgp_63d_jerk_v060_signal,
    f11rl_f11_revenue_level_revpsxgp_252d_jerk_v061_signal,
    f11rl_f11_revenue_level_revrank_252d_jerk_v062_signal,
    f11rl_f11_revenue_level_revrank_504d_jerk_v063_signal,
    f11rl_f11_revenue_level_revpsxretearn_63d_jerk_v064_signal,
    f11rl_f11_revenue_level_revpsxretearn_252d_jerk_v065_signal,
    f11rl_f11_revenue_level_revtowc_63d_jerk_v066_signal,
    f11rl_f11_revenue_level_revtowc_252d_jerk_v067_signal,
    f11rl_f11_revenue_level_revtoint_63d_jerk_v068_signal,
    f11rl_f11_revenue_level_revtoint_252d_jerk_v069_signal,
    f11rl_f11_revenue_level_revpsxequity_63d_jerk_v070_signal,
    f11rl_f11_revenue_level_revpsxequity_252d_jerk_v071_signal,
    f11rl_f11_revenue_level_logrevminuslogassets_63d_jerk_v072_signal,
    f11rl_f11_revenue_level_logrevminuslogassets_252d_jerk_v073_signal,
    f11rl_f11_revenue_level_revpsxshares_63d_jerk_v074_signal,
    f11rl_f11_revenue_level_revpsxshares_252d_jerk_v075_signal,
    f11rl_f11_revenue_level_revpsxeps_63d_jerk_v076_signal,
    f11rl_f11_revenue_level_revpsxeps_252d_jerk_v077_signal,
    f11rl_f11_revenue_level_revpsxncfo_63d_jerk_v078_signal,
    f11rl_f11_revenue_level_revpsxncfo_252d_jerk_v079_signal,
    f11rl_f11_revenue_level_revpsxfcf_63d_jerk_v080_signal,
    f11rl_f11_revenue_level_revpsxfcf_252d_jerk_v081_signal,
    f11rl_f11_revenue_level_logrev_504d_jerk_v082_signal,
    f11rl_f11_revenue_level_revps_504d_jerk_v083_signal,
    f11rl_f11_revenue_level_revtoev_252d_jerk_v084_signal,
    f11rl_f11_revenue_level_logrevexp_jerk_v085_signal,
    f11rl_f11_revenue_level_revmedian_63d_jerk_v086_signal,
    f11rl_f11_revenue_level_revmedian_252d_jerk_v087_signal,
    f11rl_f11_revenue_level_revpsiqr_252d_jerk_v088_signal,
    f11rl_f11_revenue_level_revpsskew_252d_jerk_v089_signal,
    f11rl_f11_revenue_level_revpskurt_252d_jerk_v090_signal,
    f11rl_f11_revenue_level_revtomcrank_252d_jerk_v091_signal,
    f11rl_f11_revenue_level_revtomcrank_504d_jerk_v092_signal,
    f11rl_f11_revenue_level_logrevminusdebt_252d_jerk_v093_signal,
    f11rl_f11_revenue_level_logrevminusequity_252d_jerk_v094_signal,
    f11rl_f11_revenue_level_revpsmin_63d_jerk_v095_signal,
    f11rl_f11_revenue_level_revpsmax_252d_jerk_v096_signal,
    f11rl_f11_revenue_level_revpsrelmax_504d_jerk_v097_signal,
    f11rl_f11_revenue_level_revpsrelmin_504d_jerk_v098_signal,
    f11rl_f11_revenue_level_revtomcabove5_252d_jerk_v099_signal,
    f11rl_f11_revenue_level_revtomcabove10_504d_jerk_v100_signal,
    f11rl_f11_revenue_level_revpsabovemean_252d_jerk_v101_signal,
    f11rl_f11_revenue_level_logrevz_126d_jerk_v102_signal,
    f11rl_f11_revenue_level_revpsz_126d_jerk_v103_signal,
    f11rl_f11_revenue_level_revtomcz_504d_jerk_v104_signal,
    f11rl_f11_revenue_level_revtoassetsz_504d_jerk_v105_signal,
    f11rl_f11_revenue_level_revtoequityz_252d_jerk_v106_signal,
    f11rl_f11_revenue_level_logrevps_21d_jerk_v107_signal,
    f11rl_f11_revenue_level_logrevps_63d_jerk_v108_signal,
    f11rl_f11_revenue_level_logrevps_252d_jerk_v109_signal,
    f11rl_f11_revenue_level_revpsema_21d_jerk_v110_signal,
    f11rl_f11_revenue_level_revpsema_63d_jerk_v111_signal,
    f11rl_f11_revenue_level_revpsema_252d_jerk_v112_signal,
    f11rl_f11_revenue_level_logrevema_63d_jerk_v113_signal,
    f11rl_f11_revenue_level_logrevema_252d_jerk_v114_signal,
    f11rl_f11_revenue_level_revtocapbase_252d_jerk_v115_signal,
    f11rl_f11_revenue_level_revtolevbase_63d_jerk_v116_signal,
    f11rl_f11_revenue_level_revtolevbase_252d_jerk_v117_signal,
    f11rl_f11_revenue_level_revpsxcurrent_63d_jerk_v118_signal,
    f11rl_f11_revenue_level_revpsxcurrent_252d_jerk_v119_signal,
    f11rl_f11_revenue_level_revtoni_63d_jerk_v120_signal,
    f11rl_f11_revenue_level_revtoni_252d_jerk_v121_signal,
    f11rl_f11_revenue_level_revtoncfo_252d_jerk_v122_signal,
    f11rl_f11_revenue_level_revtofcf_252d_jerk_v123_signal,
    f11rl_f11_revenue_level_revtogp_63d_jerk_v124_signal,
    f11rl_f11_revenue_level_revtogp_252d_jerk_v125_signal,
    f11rl_f11_revenue_level_revtoopinc_252d_jerk_v126_signal,
    f11rl_f11_revenue_level_revtoshares_504d_jerk_v127_signal,
    f11rl_f11_revenue_level_revxequity_63d_jerk_v128_signal,
    f11rl_f11_revenue_level_revxequity_252d_jerk_v129_signal,
    f11rl_f11_revenue_level_revxassets_63d_jerk_v130_signal,
    f11rl_f11_revenue_level_revxassets_252d_jerk_v131_signal,
    f11rl_f11_revenue_level_revtosqrtequity_63d_jerk_v132_signal,
    f11rl_f11_revenue_level_revtosqrtequity_252d_jerk_v133_signal,
    f11rl_f11_revenue_level_revtosqrtmc_252d_jerk_v134_signal,
    f11rl_f11_revenue_level_revchg_21d_jerk_v135_signal,
    f11rl_f11_revenue_level_revchg_63d_jerk_v136_signal,
    f11rl_f11_revenue_level_revchg_252d_jerk_v137_signal,
    f11rl_f11_revenue_level_revpsann_252d_jerk_v138_signal,
    f11rl_f11_revenue_level_revtomcann_252d_jerk_v139_signal,
    f11rl_f11_revenue_level_revpscomposite_63d_jerk_v140_signal,
    f11rl_f11_revenue_level_revpscomposite_252d_jerk_v141_signal,
    f11rl_f11_revenue_level_logrevxlogassets_63d_jerk_v142_signal,
    f11rl_f11_revenue_level_logrevxlogmc_252d_jerk_v143_signal,
    f11rl_f11_revenue_level_revtocapex_504d_jerk_v144_signal,
    f11rl_f11_revenue_level_revtoint_504d_jerk_v145_signal,
    f11rl_f11_revenue_level_revps3way_63d_jerk_v146_signal,
    f11rl_f11_revenue_level_revps3way_252d_jerk_v147_signal,
    f11rl_f11_revenue_level_revpssum_63d_jerk_v148_signal,
    f11rl_f11_revenue_level_revpssum_252d_jerk_v149_signal,
    f11rl_f11_revenue_level_revpsema_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_REVENUE_LEVEL_REGISTRY_JERK = REGISTRY


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
    taxexp = pd.Series(_build_log_walk(16, 2e7, 0.0002, 0.009, n), name="taxexp")
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
        "retearn": retearn, "taxexp": taxexp, "intexp": intexp,
        "liabilities": liabilities, "closeadj": closeadj, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f11_revenue_level_scaled", "_f11_revenue_level_log", "_f11_revenue_per_share")
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
    print(f"OK f11_revenue_level_3rd_derivatives_001_150_claude: {n_features} features pass")
