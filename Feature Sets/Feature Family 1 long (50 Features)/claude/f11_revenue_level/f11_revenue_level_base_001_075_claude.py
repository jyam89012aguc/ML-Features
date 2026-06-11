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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f11_revenue_level_scaled(revenue, scale):
    return revenue / scale.replace(0, np.nan).abs()


def _f11_revenue_level_log(revenue):
    return np.log(revenue.abs().replace(0, np.nan))


def _f11_revenue_per_share(revenue, sharesbas):
    return revenue / sharesbas.replace(0, np.nan).abs()


# 21d mean of revenue per share (scaled by closeadj for continuous variation)
def f11rl_f11_revenue_level_revps_21d_base_v001_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of revenue per share weighted by closeadj
def f11rl_f11_revenue_level_revps_63d_base_v002_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of revenue per share weighted by closeadj
def f11rl_f11_revenue_level_revps_126d_base_v003_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of revenue per share weighted by closeadj
def f11rl_f11_revenue_level_revps_252d_base_v004_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of revenue per share weighted by closeadj
def f11rl_f11_revenue_level_revps_504d_base_v005_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue level (smoothed 21d) times closeadj
def f11rl_f11_revenue_level_logrev_21d_base_v006_signal(revenue, closeadj):
    result = _mean(_f11_revenue_level_log(revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue level smoothed 63d times closeadj
def f11rl_f11_revenue_level_logrev_63d_base_v007_signal(revenue, closeadj):
    result = _mean(_f11_revenue_level_log(revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue level smoothed 252d times closeadj
def f11rl_f11_revenue_level_logrev_252d_base_v008_signal(revenue, closeadj):
    result = _mean(_f11_revenue_level_log(revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by marketcap (revenue / marketcap = inverse of P/S level)
def f11rl_f11_revenue_level_revtomc_21d_base_v009_signal(revenue, marketcap):
    result = _mean(_f11_revenue_level_scaled(revenue, marketcap), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by marketcap, 63d mean
def f11rl_f11_revenue_level_revtomc_63d_base_v010_signal(revenue, marketcap):
    result = _mean(_f11_revenue_level_scaled(revenue, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by marketcap, 252d mean
def f11rl_f11_revenue_level_revtomc_252d_base_v011_signal(revenue, marketcap):
    result = _mean(_f11_revenue_level_scaled(revenue, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by assets (asset turnover proxy), 63d mean
def f11rl_f11_revenue_level_revtoassets_63d_base_v012_signal(revenue, assets):
    result = _mean(_f11_revenue_level_scaled(revenue, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by assets, 252d mean
def f11rl_f11_revenue_level_revtoassets_252d_base_v013_signal(revenue, assets):
    result = _mean(_f11_revenue_level_scaled(revenue, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by equity, 63d mean
def f11rl_f11_revenue_level_revtoequity_63d_base_v014_signal(revenue, equity):
    result = _mean(_f11_revenue_level_scaled(revenue, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by equity, 252d mean
def f11rl_f11_revenue_level_revtoequity_252d_base_v015_signal(revenue, equity):
    result = _mean(_f11_revenue_level_scaled(revenue, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share times closeadj (price-weighted revenue)
def f11rl_f11_revenue_level_revpsxprice_21d_base_v016_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x closeadj, 252d smoothed
def f11rl_f11_revenue_level_revpsxprice_252d_base_v017_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of revenue per share over 63d weighted by closeadj
def f11rl_f11_revenue_level_revpsstd_63d_base_v018_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _std(rps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of revenue per share over 252d weighted by closeadj
def f11rl_f11_revenue_level_revpsstd_252d_base_v019_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _std(rps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of revenue per share over 252d
def f11rl_f11_revenue_level_revpsz_252d_base_v020_signal(revenue, sharesbas):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _z(rps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of revenue per share over 504d
def f11rl_f11_revenue_level_revpsz_504d_base_v021_signal(revenue, sharesbas):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _z(rps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of log revenue over 252d
def f11rl_f11_revenue_level_logrevz_252d_base_v022_signal(revenue):
    lr = _f11_revenue_level_log(revenue)
    result = _z(lr, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of log revenue over 504d
def f11rl_f11_revenue_level_logrevz_504d_base_v023_signal(revenue):
    lr = _f11_revenue_level_log(revenue)
    result = _z(lr, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of revenue/marketcap over 252d
def f11rl_f11_revenue_level_revtomcz_252d_base_v024_signal(revenue, marketcap):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of revenue/assets over 252d
def f11rl_f11_revenue_level_revtoassetsz_252d_base_v025_signal(revenue, assets):
    r = _f11_revenue_level_scaled(revenue, assets)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share squared (size emphasis) times closeadj
def f11rl_f11_revenue_level_revpssq_63d_base_v026_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * rps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share squared smoothed 252d times closeadj
def f11rl_f11_revenue_level_revpssq_252d_base_v027_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * rps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per dollar of debt scaled, 63d
def f11rl_f11_revenue_level_revtodebt_63d_base_v028_signal(revenue, debt):
    result = _mean(_f11_revenue_level_scaled(revenue, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per dollar of debt scaled, 252d
def f11rl_f11_revenue_level_revtodebt_252d_base_v029_signal(revenue, debt):
    result = _mean(_f11_revenue_level_scaled(revenue, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by liabilities, 63d
def f11rl_f11_revenue_level_revtoliab_63d_base_v030_signal(revenue, liabilities):
    result = _mean(_f11_revenue_level_scaled(revenue, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by liabilities, 252d
def f11rl_f11_revenue_level_revtoliab_252d_base_v031_signal(revenue, liabilities):
    result = _mean(_f11_revenue_level_scaled(revenue, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by capex, 63d
def f11rl_f11_revenue_level_revtocapex_63d_base_v032_signal(revenue, capex):
    result = _mean(_f11_revenue_level_scaled(revenue, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by capex, 252d
def f11rl_f11_revenue_level_revtocapex_252d_base_v033_signal(revenue, capex):
    result = _mean(_f11_revenue_level_scaled(revenue, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by ebitda, 63d
def f11rl_f11_revenue_level_revtoebitda_63d_base_v034_signal(revenue, ebitda):
    result = _mean(_f11_revenue_level_scaled(revenue, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by ebitda, 252d
def f11rl_f11_revenue_level_revtoebitda_252d_base_v035_signal(revenue, ebitda):
    result = _mean(_f11_revenue_level_scaled(revenue, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share times sqrt(252) normalizer x closeadj
def f11rl_f11_revenue_level_revpsnorm_252d_base_v036_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps, 252) / np.sqrt(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/marketcap times sqrt(63)
def f11rl_f11_revenue_level_revtomcnorm_63d_base_v037_signal(revenue, marketcap):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level normalized by 504d revenue mean (relative size)
def f11rl_f11_revenue_level_revrel_504d_base_v038_signal(revenue, closeadj):
    lvl = _f11_revenue_level_scaled(revenue, closeadj)
    base = _mean(revenue, 504).replace(0, np.nan)
    result = (revenue / base.abs()) * lvl
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level relative to 252d max
def f11rl_f11_revenue_level_revrelmax_252d_base_v039_signal(revenue, closeadj):
    lvl = _f11_revenue_level_scaled(revenue, closeadj)
    peak = revenue.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (revenue / peak.abs()) * lvl
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level relative to 504d max
def f11rl_f11_revenue_level_revrelmax_504d_base_v040_signal(revenue, closeadj):
    lvl = _f11_revenue_level_scaled(revenue, closeadj)
    peak = revenue.rolling(504, min_periods=126).max().replace(0, np.nan)
    result = (revenue / peak.abs()) * lvl
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x marketcap (revenue scale)
def f11rl_f11_revenue_level_revpsxmc_21d_base_v041_signal(revenue, sharesbas, marketcap):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x marketcap, 63d
def f11rl_f11_revenue_level_revpsxmc_63d_base_v042_signal(revenue, sharesbas, marketcap):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x marketcap, 252d
def f11rl_f11_revenue_level_revpsxmc_252d_base_v043_signal(revenue, sharesbas, marketcap):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by sqrt(assets), 63d weighted by closeadj
def f11rl_f11_revenue_level_revtosqrtassets_63d_base_v044_signal(revenue, assets, closeadj):
    lvl = _f11_revenue_level_scaled(revenue, closeadj)
    sa = np.sqrt(assets.abs().replace(0, np.nan))
    result = _mean(revenue / sa, 63) * lvl
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by sqrt(assets), 252d weighted by closeadj
def f11rl_f11_revenue_level_revtosqrtassets_252d_base_v045_signal(revenue, assets, closeadj):
    lvl = _f11_revenue_level_scaled(revenue, closeadj)
    sa = np.sqrt(assets.abs().replace(0, np.nan))
    result = _mean(revenue / sa, 252) * lvl
    return result.replace([np.inf, -np.inf], np.nan)


# revenue x ebitda (combined size signal, smoothed 21d)
def f11rl_f11_revenue_level_revxebitda_21d_base_v046_signal(revenue, ebitda):
    rps = _f11_revenue_level_log(revenue)
    result = _mean(rps + _f11_revenue_level_log(ebitda), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue + log ebitda smoothed 252d
def f11rl_f11_revenue_level_revxebitda_252d_base_v047_signal(revenue, ebitda):
    result = _mean(_f11_revenue_level_log(revenue) + _f11_revenue_level_log(ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share level diff to 252d mean times closeadj
def f11rl_f11_revenue_level_revpsanomaly_252d_base_v048_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = (rps - _mean(rps, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share level diff to 504d mean times closeadj
def f11rl_f11_revenue_level_revpsanomaly_504d_base_v049_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = (rps - _mean(rps, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share + revenue/marketcap composite times closeadj
def f11rl_f11_revenue_level_revcomp_63d_base_v050_signal(revenue, sharesbas, marketcap, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    rmc = _f11_revenue_level_scaled(revenue, marketcap)
    result = _mean(rps + rmc * 1e8, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x ebitda (cash earning power) smoothed 63d
def f11rl_f11_revenue_level_revpsxebitda_63d_base_v051_signal(revenue, sharesbas, ebitda):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * ebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x ebitda smoothed 252d
def f11rl_f11_revenue_level_revpsxebitda_252d_base_v052_signal(revenue, sharesbas, ebitda):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * ebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x opinc smoothed 63d
def f11rl_f11_revenue_level_revpsxopinc_63d_base_v053_signal(revenue, sharesbas, opinc):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * opinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x opinc smoothed 252d
def f11rl_f11_revenue_level_revpsxopinc_252d_base_v054_signal(revenue, sharesbas, opinc):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * opinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x gp (gross-profit-weighted revenue per share) 63d
def f11rl_f11_revenue_level_revpsxgp_63d_base_v055_signal(revenue, sharesbas, gp):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * gp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x gp 252d
def f11rl_f11_revenue_level_revpsxgp_252d_base_v056_signal(revenue, sharesbas, gp):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue x sqrt(assets), 63d
def f11rl_f11_revenue_level_logrevxsqrta_63d_base_v057_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    sa = np.sqrt(assets.abs().replace(0, np.nan))
    result = _mean(lr * sa, 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue x sqrt(assets), 252d
def f11rl_f11_revenue_level_logrevxsqrta_252d_base_v058_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    sa = np.sqrt(assets.abs().replace(0, np.nan))
    result = _mean(lr * sa, 252) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale-rank within 504d (relative size)
def f11rl_f11_revenue_level_revrank_504d_base_v059_signal(revenue, closeadj):
    rk = revenue.rolling(504, min_periods=126).rank(pct=True)
    result = rk * closeadj + _f11_revenue_level_scaled(revenue, closeadj) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale-rank within 252d
def f11rl_f11_revenue_level_revrank_252d_base_v060_signal(revenue, closeadj):
    rk = revenue.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj + _f11_revenue_level_scaled(revenue, closeadj) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x retearn 63d
def f11rl_f11_revenue_level_revpsxretearn_63d_base_v061_signal(revenue, sharesbas, retearn):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * retearn, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x retearn 252d
def f11rl_f11_revenue_level_revpsxretearn_252d_base_v062_signal(revenue, sharesbas, retearn):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * retearn, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by workingcapital, 63d
def f11rl_f11_revenue_level_revtowc_63d_base_v063_signal(revenue, workingcapital):
    result = _mean(_f11_revenue_level_scaled(revenue, workingcapital), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by workingcapital, 252d
def f11rl_f11_revenue_level_revtowc_252d_base_v064_signal(revenue, workingcapital):
    result = _mean(_f11_revenue_level_scaled(revenue, workingcapital), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per dollar tax expense, 63d
def f11rl_f11_revenue_level_revtotax_63d_base_v065_signal(revenue, taxexp):
    result = _mean(_f11_revenue_level_scaled(revenue, taxexp), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per dollar interest expense, 63d
def f11rl_f11_revenue_level_revtoint_63d_base_v066_signal(revenue, intexp):
    result = _mean(_f11_revenue_level_scaled(revenue, intexp), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per dollar interest expense 252d
def f11rl_f11_revenue_level_revtoint_252d_base_v067_signal(revenue, intexp):
    result = _mean(_f11_revenue_level_scaled(revenue, intexp), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x equity 63d
def f11rl_f11_revenue_level_revpsxequity_63d_base_v068_signal(revenue, sharesbas, equity):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * equity, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x equity 252d
def f11rl_f11_revenue_level_revpsxequity_252d_base_v069_signal(revenue, sharesbas, equity):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * equity, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue minus log assets, 63d (revenue intensity)
def f11rl_f11_revenue_level_logrevminuslogassets_63d_base_v070_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    result = _mean(lr - la, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue minus log assets, 252d
def f11rl_f11_revenue_level_logrevminuslogassets_252d_base_v071_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    result = _mean(lr - la, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x sharesbas (back-out scale)
def f11rl_f11_revenue_level_revpsxshares_63d_base_v072_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * sharesbas, 63) * closeadj * 1e-9
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x sharesbas 252d
def f11rl_f11_revenue_level_revpsxshares_252d_base_v073_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * sharesbas, 252) * closeadj * 1e-9
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x eps 63d
def f11rl_f11_revenue_level_revpsxeps_63d_base_v074_signal(revenue, sharesbas, eps):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * eps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x eps 252d
def f11rl_f11_revenue_level_revpsxeps_252d_base_v075_signal(revenue, sharesbas, eps):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * eps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11rl_f11_revenue_level_revps_21d_base_v001_signal,
    f11rl_f11_revenue_level_revps_63d_base_v002_signal,
    f11rl_f11_revenue_level_revps_126d_base_v003_signal,
    f11rl_f11_revenue_level_revps_252d_base_v004_signal,
    f11rl_f11_revenue_level_revps_504d_base_v005_signal,
    f11rl_f11_revenue_level_logrev_21d_base_v006_signal,
    f11rl_f11_revenue_level_logrev_63d_base_v007_signal,
    f11rl_f11_revenue_level_logrev_252d_base_v008_signal,
    f11rl_f11_revenue_level_revtomc_21d_base_v009_signal,
    f11rl_f11_revenue_level_revtomc_63d_base_v010_signal,
    f11rl_f11_revenue_level_revtomc_252d_base_v011_signal,
    f11rl_f11_revenue_level_revtoassets_63d_base_v012_signal,
    f11rl_f11_revenue_level_revtoassets_252d_base_v013_signal,
    f11rl_f11_revenue_level_revtoequity_63d_base_v014_signal,
    f11rl_f11_revenue_level_revtoequity_252d_base_v015_signal,
    f11rl_f11_revenue_level_revpsxprice_21d_base_v016_signal,
    f11rl_f11_revenue_level_revpsxprice_252d_base_v017_signal,
    f11rl_f11_revenue_level_revpsstd_63d_base_v018_signal,
    f11rl_f11_revenue_level_revpsstd_252d_base_v019_signal,
    f11rl_f11_revenue_level_revpsz_252d_base_v020_signal,
    f11rl_f11_revenue_level_revpsz_504d_base_v021_signal,
    f11rl_f11_revenue_level_logrevz_252d_base_v022_signal,
    f11rl_f11_revenue_level_logrevz_504d_base_v023_signal,
    f11rl_f11_revenue_level_revtomcz_252d_base_v024_signal,
    f11rl_f11_revenue_level_revtoassetsz_252d_base_v025_signal,
    f11rl_f11_revenue_level_revpssq_63d_base_v026_signal,
    f11rl_f11_revenue_level_revpssq_252d_base_v027_signal,
    f11rl_f11_revenue_level_revtodebt_63d_base_v028_signal,
    f11rl_f11_revenue_level_revtodebt_252d_base_v029_signal,
    f11rl_f11_revenue_level_revtoliab_63d_base_v030_signal,
    f11rl_f11_revenue_level_revtoliab_252d_base_v031_signal,
    f11rl_f11_revenue_level_revtocapex_63d_base_v032_signal,
    f11rl_f11_revenue_level_revtocapex_252d_base_v033_signal,
    f11rl_f11_revenue_level_revtoebitda_63d_base_v034_signal,
    f11rl_f11_revenue_level_revtoebitda_252d_base_v035_signal,
    f11rl_f11_revenue_level_revpsnorm_252d_base_v036_signal,
    f11rl_f11_revenue_level_revtomcnorm_63d_base_v037_signal,
    f11rl_f11_revenue_level_revrel_504d_base_v038_signal,
    f11rl_f11_revenue_level_revrelmax_252d_base_v039_signal,
    f11rl_f11_revenue_level_revrelmax_504d_base_v040_signal,
    f11rl_f11_revenue_level_revpsxmc_21d_base_v041_signal,
    f11rl_f11_revenue_level_revpsxmc_63d_base_v042_signal,
    f11rl_f11_revenue_level_revpsxmc_252d_base_v043_signal,
    f11rl_f11_revenue_level_revtosqrtassets_63d_base_v044_signal,
    f11rl_f11_revenue_level_revtosqrtassets_252d_base_v045_signal,
    f11rl_f11_revenue_level_revxebitda_21d_base_v046_signal,
    f11rl_f11_revenue_level_revxebitda_252d_base_v047_signal,
    f11rl_f11_revenue_level_revpsanomaly_252d_base_v048_signal,
    f11rl_f11_revenue_level_revpsanomaly_504d_base_v049_signal,
    f11rl_f11_revenue_level_revcomp_63d_base_v050_signal,
    f11rl_f11_revenue_level_revpsxebitda_63d_base_v051_signal,
    f11rl_f11_revenue_level_revpsxebitda_252d_base_v052_signal,
    f11rl_f11_revenue_level_revpsxopinc_63d_base_v053_signal,
    f11rl_f11_revenue_level_revpsxopinc_252d_base_v054_signal,
    f11rl_f11_revenue_level_revpsxgp_63d_base_v055_signal,
    f11rl_f11_revenue_level_revpsxgp_252d_base_v056_signal,
    f11rl_f11_revenue_level_logrevxsqrta_63d_base_v057_signal,
    f11rl_f11_revenue_level_logrevxsqrta_252d_base_v058_signal,
    f11rl_f11_revenue_level_revrank_504d_base_v059_signal,
    f11rl_f11_revenue_level_revrank_252d_base_v060_signal,
    f11rl_f11_revenue_level_revpsxretearn_63d_base_v061_signal,
    f11rl_f11_revenue_level_revpsxretearn_252d_base_v062_signal,
    f11rl_f11_revenue_level_revtowc_63d_base_v063_signal,
    f11rl_f11_revenue_level_revtowc_252d_base_v064_signal,
    f11rl_f11_revenue_level_revtotax_63d_base_v065_signal,
    f11rl_f11_revenue_level_revtoint_63d_base_v066_signal,
    f11rl_f11_revenue_level_revtoint_252d_base_v067_signal,
    f11rl_f11_revenue_level_revpsxequity_63d_base_v068_signal,
    f11rl_f11_revenue_level_revpsxequity_252d_base_v069_signal,
    f11rl_f11_revenue_level_logrevminuslogassets_63d_base_v070_signal,
    f11rl_f11_revenue_level_logrevminuslogassets_252d_base_v071_signal,
    f11rl_f11_revenue_level_revpsxshares_63d_base_v072_signal,
    f11rl_f11_revenue_level_revpsxshares_252d_base_v073_signal,
    f11rl_f11_revenue_level_revpsxeps_63d_base_v074_signal,
    f11rl_f11_revenue_level_revpsxeps_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_REVENUE_LEVEL_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f11_revenue_level_base_001_075_claude: {n_features} features pass")
