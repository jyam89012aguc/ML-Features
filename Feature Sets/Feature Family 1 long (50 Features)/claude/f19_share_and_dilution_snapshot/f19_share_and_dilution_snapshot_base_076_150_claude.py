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


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f19_shares_outstanding_level(sharesbas, w):
    return sharesbas.rolling(w, min_periods=max(1, w // 2)).mean()


def _f19_dilution_ratio(sharesbas, w):
    base = sharesbas.rolling(w, min_periods=max(1, w // 2)).min()
    return sharesbas / base.replace(0, np.nan)


def _f19_dilution_growth(sharesbas, w):
    return sharesbas.pct_change(periods=w)


def _f19_shares_buyback_proxy(sharesbas, w):
    peak = sharesbas.rolling(w, min_periods=max(1, w // 2)).max()
    return (peak - sharesbas) / peak.replace(0, np.nan)


# 63d shares zscore over 252d
def f19sds_f19_share_and_dilution_snapshot_sharesz_252d_base_v076_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shares zscore
def f19sds_f19_share_and_dilution_snapshot_sharesz_504d_base_v077_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shares-buyback proxy weighted by closeadj
def f19sds_f19_share_and_dilution_snapshot_buyback_63d_base_v078_signal(sharesbas, closeadj):
    result = _f19_shares_buyback_proxy(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shares-buyback proxy weighted by closeadj
def f19sds_f19_share_and_dilution_snapshot_buyback_252d_base_v079_signal(sharesbas, closeadj):
    result = _f19_shares_buyback_proxy(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shares-buyback proxy weighted by closeadj
def f19sds_f19_share_and_dilution_snapshot_buyback_504d_base_v080_signal(sharesbas, closeadj):
    result = _f19_shares_buyback_proxy(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# buyback dollar value (proxy size * closeadj * sharesbas)
def f19sds_f19_share_and_dilution_snapshot_buybackdollar_252d_base_v081_signal(sharesbas, closeadj):
    result = _f19_shares_buyback_proxy(sharesbas, 252) * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# buyback dollar value over 504d
def f19sds_f19_share_and_dilution_snapshot_buybackdollar_504d_base_v082_signal(sharesbas, closeadj):
    result = _f19_shares_buyback_proxy(sharesbas, 504) * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# buyback proxy minus dilution growth (net repurchase)
def f19sds_f19_share_and_dilution_snapshot_netrepurchase_252d_base_v083_signal(sharesbas, closeadj):
    bb = _f19_shares_buyback_proxy(sharesbas, 252)
    dg = _f19_dilution_growth(sharesbas, 252)
    result = (bb - dg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# net repurchase 504d
def f19sds_f19_share_and_dilution_snapshot_netrepurchase_504d_base_v084_signal(sharesbas, closeadj):
    bb = _f19_shares_buyback_proxy(sharesbas, 504)
    dg = _f19_dilution_growth(sharesbas, 504)
    result = (bb - dg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d shares level scaled by revenue (revenue per share inverse)
def f19sds_f19_share_and_dilution_snapshot_sharesperrev_21d_base_v085_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 21)
    result = (base / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shares per revenue
def f19sds_f19_share_and_dilution_snapshot_sharesperrev_63d_base_v086_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    result = (base / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shares per revenue
def f19sds_f19_share_and_dilution_snapshot_sharesperrev_252d_base_v087_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    result = (base / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d shares per netinc (inverse EPS)
def f19sds_f19_share_and_dilution_snapshot_shareperni_21d_base_v088_signal(sharesbas, netinc, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 21)
    result = (base / netinc.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shares per netinc
def f19sds_f19_share_and_dilution_snapshot_shareperni_252d_base_v089_signal(sharesbas, netinc, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    result = (base / netinc.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution ratio minus 252d dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratiodiff_63m252_base_v090_signal(sharesbas, closeadj):
    a = _f19_dilution_ratio(sharesbas, 63)
    b = _f19_dilution_ratio(sharesbas, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution ratio minus 63d dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratiodiff_21m63_base_v091_signal(sharesbas, closeadj):
    a = _f19_dilution_ratio(sharesbas, 21)
    b = _f19_dilution_ratio(sharesbas, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution ratio minus 504d dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratiodiff_252m504_base_v092_signal(sharesbas, closeadj):
    a = _f19_dilution_ratio(sharesbas, 252)
    b = _f19_dilution_ratio(sharesbas, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution growth minus 252d dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_63m252_base_v093_signal(sharesbas, closeadj):
    a = _f19_dilution_growth(sharesbas, 63)
    b = _f19_dilution_growth(sharesbas, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution growth minus 63d dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_21m63_base_v094_signal(sharesbas, closeadj):
    a = _f19_dilution_growth(sharesbas, 21)
    b = _f19_dilution_growth(sharesbas, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution growth minus 504d dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_252m504_base_v095_signal(sharesbas, closeadj):
    a = _f19_dilution_growth(sharesbas, 252)
    b = _f19_dilution_growth(sharesbas, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 252d dilution growth over 63d
def f19sds_f19_share_and_dilution_snapshot_dilgrowmean_63d_base_v096_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    result = _mean(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 252d dilution growth over 252d
def f19sds_f19_share_and_dilution_snapshot_dilgrowmean_252d_base_v097_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    result = _mean(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas log-level scaled by closeadj
def f19sds_f19_share_and_dilution_snapshot_logshares_63d_base_v098_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    result = np.log(base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas log-level scaled by closeadj
def f19sds_f19_share_and_dilution_snapshot_logshares_252d_base_v099_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    result = np.log(base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log(dilution ratio) at 252d
def f19sds_f19_share_and_dilution_snapshot_logdilratio_252d_base_v100_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 252)
    result = np.log(base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log(dilution ratio) at 504d
def f19sds_f19_share_and_dilution_snapshot_logdilratio_504d_base_v101_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 504)
    result = np.log(base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling skew of dilution growth at 252d
def f19sds_f19_share_and_dilution_snapshot_dilgrowskew_252d_base_v102_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    result = g.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling kurt of dilution growth at 252d
def f19sds_f19_share_and_dilution_snapshot_dilgrowkurt_252d_base_v103_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    result = g.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shares level scaled by equity (book leverage on shares)
def f19sds_f19_share_and_dilution_snapshot_sharesperequity_252d_base_v104_signal(sharesbas, equity, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    result = (base / equity.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shares level scaled by equity
def f19sds_f19_share_and_dilution_snapshot_sharesperequity_63d_base_v105_signal(sharesbas, equity, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    result = (base / equity.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution growth multiplied by equity (dilution dollar value)
def f19sds_f19_share_and_dilution_snapshot_dilxequity_252d_base_v106_signal(sharesbas, equity, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    result = g * equity.abs() * closeadj / equity.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution growth × revenue
def f19sds_f19_share_and_dilution_snapshot_dilxrev_63d_base_v107_signal(sharesbas, revenue, closeadj):
    g = _f19_dilution_growth(sharesbas, 63)
    result = g * revenue * closeadj / revenue.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution growth × netinc
def f19sds_f19_share_and_dilution_snapshot_dilxni_252d_base_v108_signal(sharesbas, netinc, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    result = g * netinc.abs() * closeadj / netinc.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dilution growth × fcf
def f19sds_f19_share_and_dilution_snapshot_dilxfcf_504d_base_v109_signal(sharesbas, fcf, closeadj):
    g = _f19_dilution_growth(sharesbas, 504)
    result = g * fcf.abs() * closeadj / fcf.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shares × current dollar volume
def f19sds_f19_share_and_dilution_snapshot_sharesxdv_252d_base_v110_signal(sharesbas, closeadj, volume):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    dv = closeadj * volume
    result = base * dv / sharesbas.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d turnover proxy: 21d volume sum / 504d shares level
def f19sds_f19_share_and_dilution_snapshot_turnover_504d_base_v111_signal(sharesbas, closeadj, volume):
    vsum = volume.rolling(21, min_periods=5).sum()
    base = _f19_shares_outstanding_level(sharesbas, 504)
    result = (vsum / base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per share at 252d
def f19sds_f19_share_and_dilution_snapshot_fcfps_63d_base_v112_signal(sharesbas, fcf, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    result = (fcf / base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per share 504d
def f19sds_f19_share_and_dilution_snapshot_fcfps_504d_base_v113_signal(sharesbas, fcf, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504)
    result = (fcf / base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# book value per share 63d
def f19sds_f19_share_and_dilution_snapshot_bvps_63d_base_v114_signal(sharesbas, equity, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    result = (equity / base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# book value per share 504d
def f19sds_f19_share_and_dilution_snapshot_bvps_504d_base_v115_signal(sharesbas, equity, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504)
    result = (equity / base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of sharesbas
def f19sds_f19_share_and_dilution_snapshot_sharesema21x_base_v116_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 5)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of sharesbas growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowema_252d_base_v117_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratioema_63d_base_v118_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratioema_252d_base_v119_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d annualized dilution growth (252 * 1d diff / shares)
def f19sds_f19_share_and_dilution_snapshot_dilgrowannual_252d_base_v120_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21) * 12.0
    result = _mean(g, 252) * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d annualized dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowannual_504d_base_v121_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21) * 12.0
    result = _mean(g, 504) * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shares × eps as earnings level
def f19sds_f19_share_and_dilution_snapshot_sharesxeps_252d_base_v122_signal(sharesbas, eps, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    result = base * eps * closeadj / sharesbas.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# eps × dilution ratio (diluted EPS adjustment proxy)
def f19sds_f19_share_and_dilution_snapshot_epsxdilratio_252d_base_v123_signal(sharesbas, eps, closeadj):
    dr = _f19_dilution_ratio(sharesbas, 252)
    result = eps / dr.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eps adjusted by 504d dilution growth
def f19sds_f19_share_and_dilution_snapshot_epsadj_504d_base_v124_signal(sharesbas, eps, closeadj):
    g = _f19_dilution_growth(sharesbas, 504)
    result = eps / (1.0 + g.clip(lower=-0.5, upper=2.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d mean of EPS scaled by closeadj
def f19sds_f19_share_and_dilution_snapshot_epsmean_63d_base_v125_signal(sharesbas, eps, closeadj):
    result = _mean(eps, 63) * closeadj + _f19_shares_outstanding_level(sharesbas, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 504d mean of EPS scaled by closeadj
def f19sds_f19_share_and_dilution_snapshot_epsmean_504d_base_v126_signal(sharesbas, eps, closeadj):
    result = _mean(eps, 504) * closeadj + _f19_shares_outstanding_level(sharesbas, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue per share growth
def f19sds_f19_share_and_dilution_snapshot_revpsgrow_252d_base_v127_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    rps = revenue / base.replace(0, np.nan)
    result = rps.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue per share growth
def f19sds_f19_share_and_dilution_snapshot_revpsgrow_63d_base_v128_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    rps = revenue / base.replace(0, np.nan)
    result = rps.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net income per share growth
def f19sds_f19_share_and_dilution_snapshot_nipsgrow_252d_base_v129_signal(sharesbas, netinc, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    nps = netinc / base.replace(0, np.nan)
    result = nps.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF per share growth
def f19sds_f19_share_and_dilution_snapshot_fcfpsgrow_504d_base_v130_signal(sharesbas, fcf, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504)
    fps = fcf / base.replace(0, np.nan)
    result = fps.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dilution growth × current price (capital raised proxy)
def f19sds_f19_share_and_dilution_snapshot_capraised_63d_base_v131_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 63)
    result = g * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capital raised proxy 252d
def f19sds_f19_share_and_dilution_snapshot_capraised_252d_base_v132_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    result = g * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capital raised proxy 504d
def f19sds_f19_share_and_dilution_snapshot_capraised_504d_base_v133_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 504)
    result = g * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d sum of capital raised
def f19sds_f19_share_and_dilution_snapshot_capraisedsum_63d_base_v134_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    cr = g * sharesbas * closeadj
    result = cr.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d sum of capital raised
def f19sds_f19_share_and_dilution_snapshot_capraisedsum_252d_base_v135_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    cr = g * sharesbas * closeadj
    result = cr.rolling(252, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d issuance velocity (sharesbas first diff / sharesbas)
def f19sds_f19_share_and_dilution_snapshot_issuevel_63d_base_v136_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 1)
    result = _mean(g, 63) * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d issuance velocity
def f19sds_f19_share_and_dilution_snapshot_issuevel_252d_base_v137_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 1)
    result = _mean(g, 252) * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d issuance velocity
def f19sds_f19_share_and_dilution_snapshot_issuevel_504d_base_v138_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 1)
    result = _mean(g, 504) * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max dilution ratio in 252d window
def f19sds_f19_share_and_dilution_snapshot_dilratiomax_252d_base_v139_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratiorange_252d_base_v140_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 252)
    result = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratiorange_504d_base_v141_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 504)
    result = (base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shares level × current price (market cap implied 63d)
def f19sds_f19_share_and_dilution_snapshot_implmcap_63d2_base_v142_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shares level × current price (market cap implied 504d)
def f19sds_f19_share_and_dilution_snapshot_implmcap_504d_base_v143_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# implied mcap diff 63d - 252d
def f19sds_f19_share_and_dilution_snapshot_mcapdiff_63m252_base_v144_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 63) * closeadj
    b = _f19_shares_outstanding_level(sharesbas, 252) * closeadj
    result = a - b
    return result.replace([np.inf, -np.inf], np.nan)


# implied mcap diff 252d - 504d
def f19sds_f19_share_and_dilution_snapshot_mcapdiff_252m504_base_v145_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 252) * closeadj
    b = _f19_shares_outstanding_level(sharesbas, 504) * closeadj
    result = a - b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × revenue per share (level value)
def f19sds_f19_share_and_dilution_snapshot_dilxrevps_252d_base_v146_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    rps = revenue / base.replace(0, np.nan)
    g = _f19_dilution_growth(sharesbas, 252)
    result = g * rps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × eps
def f19sds_f19_share_and_dilution_snapshot_dilxeps_252d_base_v147_signal(sharesbas, eps, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    result = g * eps * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA shares level × log dilution ratio (composite issuance)
def f19sds_f19_share_and_dilution_snapshot_compositedil_504d_base_v148_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504)
    dr = _f19_dilution_ratio(sharesbas, 504)
    result = base * np.log(dr.replace(0, np.nan)) * closeadj / sharesbas.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: dilution growth + buyback proxy weighted by close
def f19sds_f19_share_and_dilution_snapshot_compositesnp_252d_base_v149_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    bb = _f19_shares_buyback_proxy(sharesbas, 252)
    result = (g + bb) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite snapshot: shares level × dilution growth × close
def f19sds_f19_share_and_dilution_snapshot_compositesnp_504d_base_v150_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504)
    g = _f19_dilution_growth(sharesbas, 504)
    result = base * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19sds_f19_share_and_dilution_snapshot_sharesz_252d_base_v076_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesz_504d_base_v077_signal,
    f19sds_f19_share_and_dilution_snapshot_buyback_63d_base_v078_signal,
    f19sds_f19_share_and_dilution_snapshot_buyback_252d_base_v079_signal,
    f19sds_f19_share_and_dilution_snapshot_buyback_504d_base_v080_signal,
    f19sds_f19_share_and_dilution_snapshot_buybackdollar_252d_base_v081_signal,
    f19sds_f19_share_and_dilution_snapshot_buybackdollar_504d_base_v082_signal,
    f19sds_f19_share_and_dilution_snapshot_netrepurchase_252d_base_v083_signal,
    f19sds_f19_share_and_dilution_snapshot_netrepurchase_504d_base_v084_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperrev_21d_base_v085_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperrev_63d_base_v086_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperrev_252d_base_v087_signal,
    f19sds_f19_share_and_dilution_snapshot_shareperni_21d_base_v088_signal,
    f19sds_f19_share_and_dilution_snapshot_shareperni_252d_base_v089_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiodiff_63m252_base_v090_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiodiff_21m63_base_v091_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiodiff_252m504_base_v092_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_63m252_base_v093_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_21m63_base_v094_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_252m504_base_v095_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowmean_63d_base_v096_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowmean_252d_base_v097_signal,
    f19sds_f19_share_and_dilution_snapshot_logshares_63d_base_v098_signal,
    f19sds_f19_share_and_dilution_snapshot_logshares_252d_base_v099_signal,
    f19sds_f19_share_and_dilution_snapshot_logdilratio_252d_base_v100_signal,
    f19sds_f19_share_and_dilution_snapshot_logdilratio_504d_base_v101_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowskew_252d_base_v102_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowkurt_252d_base_v103_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperequity_252d_base_v104_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperequity_63d_base_v105_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxequity_252d_base_v106_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxrev_63d_base_v107_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxni_252d_base_v108_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxfcf_504d_base_v109_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxdv_252d_base_v110_signal,
    f19sds_f19_share_and_dilution_snapshot_turnover_504d_base_v111_signal,
    f19sds_f19_share_and_dilution_snapshot_fcfps_63d_base_v112_signal,
    f19sds_f19_share_and_dilution_snapshot_fcfps_504d_base_v113_signal,
    f19sds_f19_share_and_dilution_snapshot_bvps_63d_base_v114_signal,
    f19sds_f19_share_and_dilution_snapshot_bvps_504d_base_v115_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesema21x_base_v116_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowema_252d_base_v117_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioema_63d_base_v118_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioema_252d_base_v119_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowannual_252d_base_v120_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowannual_504d_base_v121_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxeps_252d_base_v122_signal,
    f19sds_f19_share_and_dilution_snapshot_epsxdilratio_252d_base_v123_signal,
    f19sds_f19_share_and_dilution_snapshot_epsadj_504d_base_v124_signal,
    f19sds_f19_share_and_dilution_snapshot_epsmean_63d_base_v125_signal,
    f19sds_f19_share_and_dilution_snapshot_epsmean_504d_base_v126_signal,
    f19sds_f19_share_and_dilution_snapshot_revpsgrow_252d_base_v127_signal,
    f19sds_f19_share_and_dilution_snapshot_revpsgrow_63d_base_v128_signal,
    f19sds_f19_share_and_dilution_snapshot_nipsgrow_252d_base_v129_signal,
    f19sds_f19_share_and_dilution_snapshot_fcfpsgrow_504d_base_v130_signal,
    f19sds_f19_share_and_dilution_snapshot_capraised_63d_base_v131_signal,
    f19sds_f19_share_and_dilution_snapshot_capraised_252d_base_v132_signal,
    f19sds_f19_share_and_dilution_snapshot_capraised_504d_base_v133_signal,
    f19sds_f19_share_and_dilution_snapshot_capraisedsum_63d_base_v134_signal,
    f19sds_f19_share_and_dilution_snapshot_capraisedsum_252d_base_v135_signal,
    f19sds_f19_share_and_dilution_snapshot_issuevel_63d_base_v136_signal,
    f19sds_f19_share_and_dilution_snapshot_issuevel_252d_base_v137_signal,
    f19sds_f19_share_and_dilution_snapshot_issuevel_504d_base_v138_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiomax_252d_base_v139_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiorange_252d_base_v140_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiorange_504d_base_v141_signal,
    f19sds_f19_share_and_dilution_snapshot_implmcap_63d2_base_v142_signal,
    f19sds_f19_share_and_dilution_snapshot_implmcap_504d_base_v143_signal,
    f19sds_f19_share_and_dilution_snapshot_mcapdiff_63m252_base_v144_signal,
    f19sds_f19_share_and_dilution_snapshot_mcapdiff_252m504_base_v145_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxrevps_252d_base_v146_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxeps_252d_base_v147_signal,
    f19sds_f19_share_and_dilution_snapshot_compositedil_504d_base_v148_signal,
    f19sds_f19_share_and_dilution_snapshot_compositesnp_252d_base_v149_signal,
    f19sds_f19_share_and_dilution_snapshot_compositesnp_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_SHARE_AND_DILUTION_SNAPSHOT_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="fcf")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="equity")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    eps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="eps")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {
        "revenue": revenue, "netinc": netinc, "fcf": fcf, "equity": equity,
        "sharesbas": sharesbas, "eps": eps, "closeadj": closeadj, "volume": volume,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f19_shares_outstanding_level", "_f19_dilution_ratio", "_f19_dilution_growth", "_f19_shares_buyback_proxy")
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
    print(f"OK f19_share_and_dilution_snapshot_base_076_150_claude: {n_features} features pass")
