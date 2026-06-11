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
def _f11_revenue_level_scaled(revenue, scale):
    return revenue / scale.replace(0, np.nan).abs()


def _f11_revenue_level_log(revenue):
    return np.log(revenue.abs().replace(0, np.nan))


def _f11_revenue_per_share(revenue, sharesbas):
    return revenue / sharesbas.replace(0, np.nan).abs()


# revenue per share x ncfo (cash-backed revenue per share) 63d
def f11rl_f11_revenue_level_revpsxncfo_63d_base_v076_signal(revenue, sharesbas, ncfo):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x ncfo 252d
def f11rl_f11_revenue_level_revpsxncfo_252d_base_v077_signal(revenue, sharesbas, ncfo):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x fcf 63d
def f11rl_f11_revenue_level_revpsxfcf_63d_base_v078_signal(revenue, sharesbas, fcf):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * fcf, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x fcf 252d
def f11rl_f11_revenue_level_revpsxfcf_252d_base_v079_signal(revenue, sharesbas, fcf):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue level smoothed 504d times closeadj
def f11rl_f11_revenue_level_logrev_504d_base_v080_signal(revenue, closeadj):
    result = _mean(_f11_revenue_level_log(revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share level over 504d weighted by closeadj
def f11rl_f11_revenue_level_revps_504d_base_v081_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x marketcap, 504d
def f11rl_f11_revenue_level_revpsxmc_504d_base_v082_signal(revenue, sharesbas, marketcap):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by ev (revenue yield to ev) 63d
def f11rl_f11_revenue_level_revtoev_63d_base_v083_signal(revenue, marketcap, debt):
    ev = marketcap + debt
    result = _mean(_f11_revenue_level_scaled(revenue, ev), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by ev 252d
def f11rl_f11_revenue_level_revtoev_252d_base_v084_signal(revenue, marketcap, debt):
    ev = marketcap + debt
    result = _mean(_f11_revenue_level_scaled(revenue, ev), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue level expanding mean times closeadj
def f11rl_f11_revenue_level_logrevexp_base_v085_signal(revenue, closeadj):
    result = _f11_revenue_level_log(revenue).expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share expanding mean times closeadj
def f11rl_f11_revenue_level_revpsexp_base_v086_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue rolling median 63d times closeadj
def f11rl_f11_revenue_level_revmedian_63d_base_v087_signal(revenue, closeadj):
    rps = _f11_revenue_level_log(revenue)
    result = rps.rolling(63, min_periods=21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue rolling median 252d times closeadj
def f11rl_f11_revenue_level_revmedian_252d_base_v088_signal(revenue, closeadj):
    rps = _f11_revenue_level_log(revenue)
    result = rps.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share IQR 252d times closeadj
def f11rl_f11_revenue_level_revpsiqr_252d_base_v089_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    q3 = rps.rolling(252, min_periods=63).quantile(0.75)
    q1 = rps.rolling(252, min_periods=63).quantile(0.25)
    result = (q3 - q1) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share rolling skew 252d times closeadj
def f11rl_f11_revenue_level_revpsskew_252d_base_v090_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share rolling kurtosis 252d times closeadj
def f11rl_f11_revenue_level_revpskurt_252d_base_v091_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / marketcap percentile rank 252d times closeadj
def f11rl_f11_revenue_level_revtomcrank_252d_base_v092_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    result = r.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / marketcap percentile rank 504d times closeadj
def f11rl_f11_revenue_level_revtomcrank_504d_base_v093_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    result = r.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue minus log debt 252d times closeadj
def f11rl_f11_revenue_level_logrevminusdebt_252d_base_v094_signal(revenue, debt, closeadj):
    lr = _f11_revenue_level_log(revenue)
    ld = np.log(debt.abs().replace(0, np.nan))
    result = _mean(lr - ld, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue minus log equity 252d times closeadj
def f11rl_f11_revenue_level_logrevminusequity_252d_base_v095_signal(revenue, equity, closeadj):
    lr = _f11_revenue_level_log(revenue)
    le = np.log(equity.abs().replace(0, np.nan))
    result = _mean(lr - le, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share minimum 63d times closeadj
def f11rl_f11_revenue_level_revpsmin_63d_base_v096_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share max 252d times closeadj
def f11rl_f11_revenue_level_revpsmax_252d_base_v097_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / sharesbas relative to 504d max
def f11rl_f11_revenue_level_revpsrelmax_504d_base_v098_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    peak = rps.rolling(504, min_periods=126).max().replace(0, np.nan)
    result = (rps / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share relative to 504d min times closeadj
def f11rl_f11_revenue_level_revpsrelmin_504d_base_v099_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    trough = rps.rolling(504, min_periods=126).min().replace(0, np.nan)
    result = (rps / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count of days revenue/marketcap above 0.05 in 252d
def f11rl_f11_revenue_level_revtomcabove5_252d_base_v100_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    result = (r).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count of days revenue/marketcap above 0.10 in 504d
def f11rl_f11_revenue_level_revtomcabove10_504d_base_v101_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    result = (r).rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count of days revenue per share above 252d mean over 252d
def f11rl_f11_revenue_level_revpsabovemean_252d_base_v102_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    flag = (rps > _mean(rps, 252)).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue level 504d zscore
def f11rl_f11_revenue_level_logrevz_126d_base_v103_signal(revenue):
    lr = _f11_revenue_level_log(revenue)
    result = _z(lr, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share 126d zscore
def f11rl_f11_revenue_level_revpsz_126d_base_v104_signal(revenue, sharesbas):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _z(rps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/marketcap 504d zscore
def f11rl_f11_revenue_level_revtomcz_504d_base_v105_signal(revenue, marketcap):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/assets 504d zscore
def f11rl_f11_revenue_level_revtoassetsz_504d_base_v106_signal(revenue, assets):
    r = _f11_revenue_level_scaled(revenue, assets)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/equity 252d zscore
def f11rl_f11_revenue_level_revtoequityz_252d_base_v107_signal(revenue, equity):
    r = _f11_revenue_level_scaled(revenue, equity)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue per share times closeadj 21d mean
def f11rl_f11_revenue_level_logrevps_21d_base_v108_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = np.log(rps.abs().replace(0, np.nan))
    result = _mean(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue per share times closeadj 63d mean
def f11rl_f11_revenue_level_logrevps_63d_base_v109_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = np.log(rps.abs().replace(0, np.nan))
    result = _mean(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue per share times closeadj 252d mean
def f11rl_f11_revenue_level_logrevps_252d_base_v110_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = np.log(rps.abs().replace(0, np.nan))
    result = _mean(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share EMA 21d times closeadj
def f11rl_f11_revenue_level_revpsema_21d_base_v111_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share EMA 63d times closeadj
def f11rl_f11_revenue_level_revpsema_63d_base_v112_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share EMA 252d times closeadj
def f11rl_f11_revenue_level_revpsema_252d_base_v113_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue EMA 63d times closeadj
def f11rl_f11_revenue_level_logrevema_63d_base_v114_signal(revenue, closeadj):
    lr = _f11_revenue_level_log(revenue)
    result = lr.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue EMA 252d times closeadj
def f11rl_f11_revenue_level_logrevema_252d_base_v115_signal(revenue, closeadj):
    lr = _f11_revenue_level_log(revenue)
    result = lr.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / (marketcap+debt+equity) capital base 252d
def f11rl_f11_revenue_level_revtocapbase_252d_base_v116_signal(revenue, marketcap, debt, equity):
    base = marketcap + debt + equity
    result = _mean(_f11_revenue_level_scaled(revenue, base), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / (assets+debt) leverage base 63d
def f11rl_f11_revenue_level_revtolevbase_63d_base_v117_signal(revenue, assets, debt):
    base = assets + debt
    result = _mean(_f11_revenue_level_scaled(revenue, base), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / (assets+debt) leverage base 252d
def f11rl_f11_revenue_level_revtolevbase_252d_base_v118_signal(revenue, assets, debt):
    base = assets + debt
    result = _mean(_f11_revenue_level_scaled(revenue, base), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x (1+currentratio) 63d
def f11rl_f11_revenue_level_revpsxcurrent_63d_base_v119_signal(revenue, sharesbas, currentratio, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * (1.0 + currentratio), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x (1+currentratio) 252d
def f11rl_f11_revenue_level_revpsxcurrent_252d_base_v120_signal(revenue, sharesbas, currentratio, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps * (1.0 + currentratio), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by netinc magnitude 63d (revenue per dollar of profit)
def f11rl_f11_revenue_level_revtoni_63d_base_v121_signal(revenue, netinc):
    result = _mean(_f11_revenue_level_scaled(revenue, netinc.abs()), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by netinc magnitude 252d
def f11rl_f11_revenue_level_revtoni_252d_base_v122_signal(revenue, netinc):
    result = _mean(_f11_revenue_level_scaled(revenue, netinc.abs()), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by ncfo 252d
def f11rl_f11_revenue_level_revtoncfo_252d_base_v123_signal(revenue, ncfo):
    result = _mean(_f11_revenue_level_scaled(revenue, ncfo.abs()), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by fcf 252d
def f11rl_f11_revenue_level_revtofcf_252d_base_v124_signal(revenue, fcf):
    result = _mean(_f11_revenue_level_scaled(revenue, fcf.abs()), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by gp 63d
def f11rl_f11_revenue_level_revtogp_63d_base_v125_signal(revenue, gp):
    result = _mean(_f11_revenue_level_scaled(revenue, gp), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by gp 252d
def f11rl_f11_revenue_level_revtogp_252d_base_v126_signal(revenue, gp):
    result = _mean(_f11_revenue_level_scaled(revenue, gp), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by opinc 252d
def f11rl_f11_revenue_level_revtoopinc_252d_base_v127_signal(revenue, opinc):
    result = _mean(_f11_revenue_level_scaled(revenue, opinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by sharesbas (revenue per share, smoothed) 504d
def f11rl_f11_revenue_level_revtoshares_504d_base_v128_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = _mean(rps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue x equity (combined scale composite) 63d
def f11rl_f11_revenue_level_revxequity_63d_base_v129_signal(revenue, equity):
    lr = _f11_revenue_level_log(revenue)
    le = np.log(equity.abs().replace(0, np.nan))
    result = _mean(lr * le, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue x equity (combined scale composite) 252d
def f11rl_f11_revenue_level_revxequity_252d_base_v130_signal(revenue, equity):
    lr = _f11_revenue_level_log(revenue)
    le = np.log(equity.abs().replace(0, np.nan))
    result = _mean(lr * le, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue x assets composite 63d
def f11rl_f11_revenue_level_revxassets_63d_base_v131_signal(revenue, assets):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    result = _mean(lr * la, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue x assets composite 252d
def f11rl_f11_revenue_level_revxassets_252d_base_v132_signal(revenue, assets):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    result = _mean(lr * la, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / sqrt(equity) 63d
def f11rl_f11_revenue_level_revtosqrtequity_63d_base_v133_signal(revenue, equity, closeadj):
    lvl = _f11_revenue_level_scaled(revenue, closeadj)
    se = np.sqrt(equity.abs().replace(0, np.nan))
    result = _mean(revenue / se, 63) * lvl
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / sqrt(equity) 252d
def f11rl_f11_revenue_level_revtosqrtequity_252d_base_v134_signal(revenue, equity, closeadj):
    lvl = _f11_revenue_level_scaled(revenue, closeadj)
    se = np.sqrt(equity.abs().replace(0, np.nan))
    result = _mean(revenue / se, 252) * lvl
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / sqrt(marketcap) 252d
def f11rl_f11_revenue_level_revtosqrtmc_252d_base_v135_signal(revenue, marketcap, closeadj):
    lvl = _f11_revenue_level_scaled(revenue, closeadj)
    sm = np.sqrt(marketcap.abs().replace(0, np.nan))
    result = _mean(revenue / sm, 252) * lvl
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 21d momentum-style (level - lag) times closeadj
def f11rl_f11_revenue_level_revchg_21d_base_v136_signal(revenue, closeadj):
    base = _f11_revenue_level_log(revenue)
    result = _diff(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 63d momentum-style (level - lag) times closeadj
def f11rl_f11_revenue_level_revchg_63d_base_v137_signal(revenue, closeadj):
    base = _f11_revenue_level_log(revenue)
    result = _diff(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 252d momentum-style (level - lag) times closeadj
def f11rl_f11_revenue_level_revchg_252d_base_v138_signal(revenue, closeadj):
    base = _f11_revenue_level_log(revenue)
    result = _diff(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x sqrt(252) normalization (annualized scale)
def f11rl_f11_revenue_level_revpsann_252d_base_v139_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = (rps * np.sqrt(252.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / marketcap x sqrt(252) annualized
def f11rl_f11_revenue_level_revtomcann_252d_base_v140_signal(revenue, marketcap, closeadj):
    r = _f11_revenue_level_scaled(revenue, marketcap)
    result = (r * np.sqrt(252.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share + log revenue composite times closeadj
def f11rl_f11_revenue_level_revpscomposite_63d_base_v141_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = _f11_revenue_level_log(revenue)
    result = _mean(rps + lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share + log revenue composite 252d
def f11rl_f11_revenue_level_revpscomposite_252d_base_v142_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    lr = _f11_revenue_level_log(revenue)
    result = _mean(rps + lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue x log assets composite 63d times closeadj
def f11rl_f11_revenue_level_logrevxlogassets_63d_base_v143_signal(revenue, assets, closeadj):
    lr = _f11_revenue_level_log(revenue)
    la = np.log(assets.abs().replace(0, np.nan))
    result = _mean(lr + la, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue x log marketcap composite 252d times closeadj
def f11rl_f11_revenue_level_logrevxlogmc_252d_base_v144_signal(revenue, marketcap, closeadj):
    lr = _f11_revenue_level_log(revenue)
    lm = np.log(marketcap.abs().replace(0, np.nan))
    result = _mean(lr + lm, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / capex magnitude (capital efficiency proxy) 252d
def f11rl_f11_revenue_level_revtocapex_504d_base_v145_signal(revenue, capex):
    result = _mean(_f11_revenue_level_scaled(revenue, capex.abs()), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by intexp 252d
def f11rl_f11_revenue_level_revtoint_504d_base_v146_signal(revenue, intexp):
    result = _mean(_f11_revenue_level_scaled(revenue, intexp.abs()), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x ebitda x equity composite 63d
def f11rl_f11_revenue_level_revps3way_63d_base_v147_signal(revenue, sharesbas, ebitda, equity):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    le = np.log(equity.abs().replace(0, np.nan))
    result = _mean(rps * ebitda * le, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share x ebitda x equity composite 252d
def f11rl_f11_revenue_level_revps3way_252d_base_v148_signal(revenue, sharesbas, ebitda, equity):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    le = np.log(equity.abs().replace(0, np.nan))
    result = _mean(rps * ebitda * le, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share rolling sum 63d times closeadj
def f11rl_f11_revenue_level_revpssum_63d_base_v149_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share rolling sum 252d times closeadj
def f11rl_f11_revenue_level_revpssum_252d_base_v150_signal(revenue, sharesbas, closeadj):
    rps = _f11_revenue_per_share(revenue, sharesbas)
    result = rps.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11rl_f11_revenue_level_revpsxncfo_63d_base_v076_signal,
    f11rl_f11_revenue_level_revpsxncfo_252d_base_v077_signal,
    f11rl_f11_revenue_level_revpsxfcf_63d_base_v078_signal,
    f11rl_f11_revenue_level_revpsxfcf_252d_base_v079_signal,
    f11rl_f11_revenue_level_logrev_504d_base_v080_signal,
    f11rl_f11_revenue_level_revps_504d_base_v081_signal,
    f11rl_f11_revenue_level_revpsxmc_504d_base_v082_signal,
    f11rl_f11_revenue_level_revtoev_63d_base_v083_signal,
    f11rl_f11_revenue_level_revtoev_252d_base_v084_signal,
    f11rl_f11_revenue_level_logrevexp_base_v085_signal,
    f11rl_f11_revenue_level_revpsexp_base_v086_signal,
    f11rl_f11_revenue_level_revmedian_63d_base_v087_signal,
    f11rl_f11_revenue_level_revmedian_252d_base_v088_signal,
    f11rl_f11_revenue_level_revpsiqr_252d_base_v089_signal,
    f11rl_f11_revenue_level_revpsskew_252d_base_v090_signal,
    f11rl_f11_revenue_level_revpskurt_252d_base_v091_signal,
    f11rl_f11_revenue_level_revtomcrank_252d_base_v092_signal,
    f11rl_f11_revenue_level_revtomcrank_504d_base_v093_signal,
    f11rl_f11_revenue_level_logrevminusdebt_252d_base_v094_signal,
    f11rl_f11_revenue_level_logrevminusequity_252d_base_v095_signal,
    f11rl_f11_revenue_level_revpsmin_63d_base_v096_signal,
    f11rl_f11_revenue_level_revpsmax_252d_base_v097_signal,
    f11rl_f11_revenue_level_revpsrelmax_504d_base_v098_signal,
    f11rl_f11_revenue_level_revpsrelmin_504d_base_v099_signal,
    f11rl_f11_revenue_level_revtomcabove5_252d_base_v100_signal,
    f11rl_f11_revenue_level_revtomcabove10_504d_base_v101_signal,
    f11rl_f11_revenue_level_revpsabovemean_252d_base_v102_signal,
    f11rl_f11_revenue_level_logrevz_126d_base_v103_signal,
    f11rl_f11_revenue_level_revpsz_126d_base_v104_signal,
    f11rl_f11_revenue_level_revtomcz_504d_base_v105_signal,
    f11rl_f11_revenue_level_revtoassetsz_504d_base_v106_signal,
    f11rl_f11_revenue_level_revtoequityz_252d_base_v107_signal,
    f11rl_f11_revenue_level_logrevps_21d_base_v108_signal,
    f11rl_f11_revenue_level_logrevps_63d_base_v109_signal,
    f11rl_f11_revenue_level_logrevps_252d_base_v110_signal,
    f11rl_f11_revenue_level_revpsema_21d_base_v111_signal,
    f11rl_f11_revenue_level_revpsema_63d_base_v112_signal,
    f11rl_f11_revenue_level_revpsema_252d_base_v113_signal,
    f11rl_f11_revenue_level_logrevema_63d_base_v114_signal,
    f11rl_f11_revenue_level_logrevema_252d_base_v115_signal,
    f11rl_f11_revenue_level_revtocapbase_252d_base_v116_signal,
    f11rl_f11_revenue_level_revtolevbase_63d_base_v117_signal,
    f11rl_f11_revenue_level_revtolevbase_252d_base_v118_signal,
    f11rl_f11_revenue_level_revpsxcurrent_63d_base_v119_signal,
    f11rl_f11_revenue_level_revpsxcurrent_252d_base_v120_signal,
    f11rl_f11_revenue_level_revtoni_63d_base_v121_signal,
    f11rl_f11_revenue_level_revtoni_252d_base_v122_signal,
    f11rl_f11_revenue_level_revtoncfo_252d_base_v123_signal,
    f11rl_f11_revenue_level_revtofcf_252d_base_v124_signal,
    f11rl_f11_revenue_level_revtogp_63d_base_v125_signal,
    f11rl_f11_revenue_level_revtogp_252d_base_v126_signal,
    f11rl_f11_revenue_level_revtoopinc_252d_base_v127_signal,
    f11rl_f11_revenue_level_revtoshares_504d_base_v128_signal,
    f11rl_f11_revenue_level_revxequity_63d_base_v129_signal,
    f11rl_f11_revenue_level_revxequity_252d_base_v130_signal,
    f11rl_f11_revenue_level_revxassets_63d_base_v131_signal,
    f11rl_f11_revenue_level_revxassets_252d_base_v132_signal,
    f11rl_f11_revenue_level_revtosqrtequity_63d_base_v133_signal,
    f11rl_f11_revenue_level_revtosqrtequity_252d_base_v134_signal,
    f11rl_f11_revenue_level_revtosqrtmc_252d_base_v135_signal,
    f11rl_f11_revenue_level_revchg_21d_base_v136_signal,
    f11rl_f11_revenue_level_revchg_63d_base_v137_signal,
    f11rl_f11_revenue_level_revchg_252d_base_v138_signal,
    f11rl_f11_revenue_level_revpsann_252d_base_v139_signal,
    f11rl_f11_revenue_level_revtomcann_252d_base_v140_signal,
    f11rl_f11_revenue_level_revpscomposite_63d_base_v141_signal,
    f11rl_f11_revenue_level_revpscomposite_252d_base_v142_signal,
    f11rl_f11_revenue_level_logrevxlogassets_63d_base_v143_signal,
    f11rl_f11_revenue_level_logrevxlogmc_252d_base_v144_signal,
    f11rl_f11_revenue_level_revtocapex_504d_base_v145_signal,
    f11rl_f11_revenue_level_revtoint_504d_base_v146_signal,
    f11rl_f11_revenue_level_revps3way_63d_base_v147_signal,
    f11rl_f11_revenue_level_revps3way_252d_base_v148_signal,
    f11rl_f11_revenue_level_revpssum_63d_base_v149_signal,
    f11rl_f11_revenue_level_revpssum_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_REVENUE_LEVEL_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f11_revenue_level_base_076_150_claude: {n_features} features pass")
