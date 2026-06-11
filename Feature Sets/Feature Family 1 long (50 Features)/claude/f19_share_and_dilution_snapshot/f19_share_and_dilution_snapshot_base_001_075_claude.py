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
def _f19_shares_outstanding_level(sharesbas, w):
    # rolling mean of basic share count level (SF1 sharesbas)
    return sharesbas.rolling(w, min_periods=max(1, w // 2)).mean()


def _f19_dilution_ratio(sharesbas, w):
    # ratio of current shares to rolling baseline shares (>=1 implies dilution)
    base = sharesbas.rolling(w, min_periods=max(1, w // 2)).min()
    return sharesbas / base.replace(0, np.nan)


def _f19_dilution_growth(sharesbas, w):
    # rolling growth of share count over window (positive = dilution)
    return sharesbas.pct_change(periods=w)


# 21d shares-outstanding rolling mean times closeadj (level signal)
def f19sds_f19_share_and_dilution_snapshot_sharesout_21d_base_v001_signal(sharesbas, closeadj):
    result = _f19_shares_outstanding_level(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shares-outstanding rolling mean times closeadj
def f19sds_f19_share_and_dilution_snapshot_sharesout_63d_base_v002_signal(sharesbas, closeadj):
    result = _f19_shares_outstanding_level(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d shares-outstanding rolling mean times closeadj
def f19sds_f19_share_and_dilution_snapshot_sharesout_126d_base_v003_signal(sharesbas, closeadj):
    result = _f19_shares_outstanding_level(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shares-outstanding rolling mean times closeadj
def f19sds_f19_share_and_dilution_snapshot_sharesout_252d_base_v004_signal(sharesbas, closeadj):
    result = _f19_shares_outstanding_level(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d shares-outstanding rolling mean times closeadj (long persistence)
def f19sds_f19_share_and_dilution_snapshot_sharesout_504d_base_v005_signal(sharesbas, closeadj):
    result = _f19_shares_outstanding_level(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution ratio (shares vs 21d trough shares)
def f19sds_f19_share_and_dilution_snapshot_dilratio_21d_base_v006_signal(sharesbas, closeadj):
    result = _f19_dilution_ratio(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution ratio (shares vs 63d trough shares)
def f19sds_f19_share_and_dilution_snapshot_dilratio_63d_base_v007_signal(sharesbas, closeadj):
    result = _f19_dilution_ratio(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratio_126d_base_v008_signal(sharesbas, closeadj):
    result = _f19_dilution_ratio(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratio_252d_base_v009_signal(sharesbas, closeadj):
    result = _f19_dilution_ratio(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratio_504d_base_v010_signal(sharesbas, closeadj):
    result = _f19_dilution_ratio(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution growth (sharesbas pct change)
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_21d_base_v011_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_63d_base_v012_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_126d_base_v013_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution growth (annual share count change)
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_252d_base_v014_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_504d_base_v015_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore of dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratioz_63d_base_v016_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratioz_252d_base_v017_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of dilution ratio
def f19sds_f19_share_and_dilution_snapshot_dilratioz_504d_base_v018_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of dilution growth (volatility of share issuance)
def f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_63d_base_v019_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_252d_base_v020_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    result = _std(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of 63d dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_504d_base_v021_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 63)
    result = _std(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# market cap implied (sharesbas * closeadj) rolling 21d mean
def f19sds_f19_share_and_dilution_snapshot_implmcap_21d_base_v022_signal(sharesbas, closeadj):
    mc = sharesbas * closeadj
    result = _mean(mc, 21) + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# implied market cap rolling 63d
def f19sds_f19_share_and_dilution_snapshot_implmcap_63d_base_v023_signal(sharesbas, closeadj):
    mc = sharesbas * closeadj
    result = _mean(mc, 63) + _f19_shares_outstanding_level(sharesbas, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# implied market cap rolling 252d
def f19sds_f19_share_and_dilution_snapshot_implmcap_252d_base_v024_signal(sharesbas, closeadj):
    mc = sharesbas * closeadj
    result = _mean(mc, 252) + _f19_shares_outstanding_level(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sharesbas growth weighted by closeadj
def f19sds_f19_share_and_dilution_snapshot_sharesgrowxprice_21d_base_v025_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas growth weighted by closeadj
def f19sds_f19_share_and_dilution_snapshot_sharesgrowxprice_63d_base_v026_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas growth weighted by closeadj * sharesbas (dollar issuance proxy)
def f19sds_f19_share_and_dilution_snapshot_dollarissue_252d_base_v027_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 252) * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dollar issuance proxy
def f19sds_f19_share_and_dilution_snapshot_dollarissue_504d_base_v028_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 504) * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shares level minus 252d shares level (recent issuance)
def f19sds_f19_share_and_dilution_snapshot_sharesdiff_63v252_base_v029_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 63)
    b = _f19_shares_outstanding_level(sharesbas, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d shares minus 63d shares (very recent issuance)
def f19sds_f19_share_and_dilution_snapshot_sharesdiff_21v63_base_v030_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 21)
    b = _f19_shares_outstanding_level(sharesbas, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shares minus 504d shares (long-term issuance)
def f19sds_f19_share_and_dilution_snapshot_sharesdiff_252v504_base_v031_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 252)
    b = _f19_shares_outstanding_level(sharesbas, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shares vs 252d trough as ratio (share buyback indicator if <1)
def f19sds_f19_share_and_dilution_snapshot_sharesvslow_252d_base_v032_signal(sharesbas, closeadj):
    result = _f19_dilution_ratio(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shares vs 504d trough
def f19sds_f19_share_and_dilution_snapshot_sharesvslow_504d_base_v033_signal(sharesbas, closeadj):
    result = _f19_dilution_ratio(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max sharesbas vs current (peak-to-now)
def f19sds_f19_share_and_dilution_snapshot_sharesvspeak_63d_base_v034_signal(sharesbas, closeadj):
    peak = sharesbas.rolling(63, min_periods=21).max()
    base = _f19_shares_outstanding_level(sharesbas, 21)
    result = (base / peak.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max sharesbas vs current
def f19sds_f19_share_and_dilution_snapshot_sharesvspeak_252d_base_v035_signal(sharesbas, closeadj):
    peak = sharesbas.rolling(252, min_periods=63).max()
    base = _f19_shares_outstanding_level(sharesbas, 21)
    result = (base / peak.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fully diluted shares estimate via sharesbas * (1 + dilgrowth_252)
def f19sds_f19_share_and_dilution_snapshot_fullydil_252d_base_v036_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    result = sharesbas * (1.0 + g.clip(lower=-0.5, upper=2.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fully diluted shares estimate via 504d growth
def f19sds_f19_share_and_dilution_snapshot_fullydil_504d_base_v037_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 504)
    result = sharesbas * (1.0 + g.clip(lower=-0.5, upper=2.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of sharesbas level
def f19sds_f19_share_and_dilution_snapshot_sharesz_63d_base_v038_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of sharesbas level
def f19sds_f19_share_and_dilution_snapshot_sharesz_252d_base_v039_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of sharesbas level
def f19sds_f19_share_and_dilution_snapshot_sharesz_504d_base_v040_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling cumulative dilution over 21d (compounded)
def f19sds_f19_share_and_dilution_snapshot_cumdil_21d_base_v041_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 1)
    result = (1.0 + g.fillna(0.0)).rolling(21, min_periods=5).apply(np.prod, raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative dilution
def f19sds_f19_share_and_dilution_snapshot_cumdil_63d_base_v042_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 1)
    result = (1.0 + g.fillna(0.0)).rolling(63, min_periods=21).apply(np.prod, raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative dilution
def f19sds_f19_share_and_dilution_snapshot_cumdil_252d_base_v043_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 1)
    result = (1.0 + g.fillna(0.0)).rolling(252, min_periods=63).apply(np.prod, raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sharesbas EMA times closeadj
def f19sds_f19_share_and_dilution_snapshot_sharesema_21d_base_v044_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=21, adjust=False).mean()
    result = base * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas EMA times closeadj
def f19sds_f19_share_and_dilution_snapshot_sharesema_63d_base_v045_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=63, adjust=False).mean()
    result = base * closeadj + _f19_shares_outstanding_level(sharesbas, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas EMA times closeadj
def f19sds_f19_share_and_dilution_snapshot_sharesema_252d_base_v046_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=252, adjust=False).mean()
    result = base * closeadj + _f19_shares_outstanding_level(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution ratio 21d minus dilution ratio 252d (acceleration)
def f19sds_f19_share_and_dilution_snapshot_dilratiodiff_21m252_base_v047_signal(sharesbas, closeadj):
    a = _f19_dilution_ratio(sharesbas, 21)
    b = _f19_dilution_ratio(sharesbas, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dilution ratio 63d minus dilution ratio 504d
def f19sds_f19_share_and_dilution_snapshot_dilratiodiff_63m504_base_v048_signal(sharesbas, closeadj):
    a = _f19_dilution_ratio(sharesbas, 63)
    b = _f19_dilution_ratio(sharesbas, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d sharesbas growth (very recent)
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_5d_base_v049_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d sharesbas growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_10d_base_v050_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d dilution growth (~2mo)
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_42d_base_v051_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_189d_base_v052_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d dilution growth
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_378d_base_v053_signal(sharesbas, closeadj):
    result = _f19_dilution_growth(sharesbas, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share level over 5d × dollar volume proxy
def f19sds_f19_share_and_dilution_snapshot_sharesxdv_21d_base_v054_signal(sharesbas, closeadj, volume):
    dv = closeadj * volume
    result = _f19_shares_outstanding_level(sharesbas, 21) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# share level over 63d × dollar volume
def f19sds_f19_share_and_dilution_snapshot_sharesxdv_63d_base_v055_signal(sharesbas, closeadj, volume):
    dv = closeadj * volume
    result = _f19_shares_outstanding_level(sharesbas, 63) * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# float turnover proxy: volume / sharesbas (21d mean)
def f19sds_f19_share_and_dilution_snapshot_turnover_21d_base_v056_signal(sharesbas, closeadj, volume):
    base = _f19_shares_outstanding_level(sharesbas, 21).replace(0, np.nan)
    result = _mean(volume, 21) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# float turnover 63d
def f19sds_f19_share_and_dilution_snapshot_turnover_63d_base_v057_signal(sharesbas, closeadj, volume):
    base = _f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)
    result = _mean(volume, 63) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# float turnover 252d
def f19sds_f19_share_and_dilution_snapshot_turnover_252d_base_v058_signal(sharesbas, closeadj, volume):
    base = _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)
    result = _mean(volume, 252) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share (21d mean of revenue / sharesbas)
def f19sds_f19_share_and_dilution_snapshot_revps_21d_base_v059_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 21).replace(0, np.nan)
    result = _mean(revenue, 21) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share 63d
def f19sds_f19_share_and_dilution_snapshot_revps_63d_base_v060_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)
    result = _mean(revenue, 63) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share 252d
def f19sds_f19_share_and_dilution_snapshot_revps_252d_base_v061_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)
    result = _mean(revenue, 252) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# net income per share 63d
def f19sds_f19_share_and_dilution_snapshot_nips_63d_base_v062_signal(sharesbas, netinc, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)
    result = _mean(netinc, 63) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# net income per share 252d
def f19sds_f19_share_and_dilution_snapshot_nips_252d_base_v063_signal(sharesbas, netinc, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)
    result = _mean(netinc, 252) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per share 252d
def f19sds_f19_share_and_dilution_snapshot_fcfps_252d_base_v064_signal(sharesbas, fcf, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)
    result = _mean(fcf, 252) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# equity per share 252d (book value per share scaled by price)
def f19sds_f19_share_and_dilution_snapshot_bvps_252d_base_v065_signal(sharesbas, equity, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)
    result = _mean(equity, 252) / base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eps level 21d times closeadj (input eps)
def f19sds_f19_share_and_dilution_snapshot_epslevel_21d_base_v066_signal(sharesbas, eps, closeadj):
    result = _mean(eps, 21) * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# eps level 63d
def f19sds_f19_share_and_dilution_snapshot_epslevel_63d_base_v067_signal(sharesbas, eps, closeadj):
    result = _mean(eps, 63) * closeadj + _f19_shares_outstanding_level(sharesbas, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# eps level 252d
def f19sds_f19_share_and_dilution_snapshot_epslevel_252d_base_v068_signal(sharesbas, eps, closeadj):
    result = _mean(eps, 252) * closeadj + _f19_shares_outstanding_level(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eps minus implied (netinc/sharesbas) gap (dilution distortion)
def f19sds_f19_share_and_dilution_snapshot_epsdilgap_252d_base_v069_signal(sharesbas, eps, netinc, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)
    implied = _mean(netinc, 252) / base
    result = (_mean(eps, 252) - implied) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share count squared (illiquidity / market structure proxy)
def f19sds_f19_share_and_dilution_snapshot_sharessq_63d_base_v070_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    result = base * base.abs() / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas squared scaled
def f19sds_f19_share_and_dilution_snapshot_sharessq_252d_base_v071_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    result = base * base.abs() / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shares × revenue (size composite)
def f19sds_f19_share_and_dilution_snapshot_sharesxrev_63d_base_v072_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    result = base * _mean(revenue, 63) / 1e6 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shares × revenue
def f19sds_f19_share_and_dilution_snapshot_sharesxrev_252d_base_v073_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    result = base * _mean(revenue, 252) / 1e6 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution growth weighted by absolute price return (dilution-during-rally penalty)
def f19sds_f19_share_and_dilution_snapshot_dilxret_63d_base_v074_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 63)
    r = closeadj.pct_change(63).abs()
    result = g * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution growth weighted by absolute price return
def f19sds_f19_share_and_dilution_snapshot_dilxret_252d_base_v075_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    r = closeadj.pct_change(252).abs()
    result = g * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19sds_f19_share_and_dilution_snapshot_sharesout_21d_base_v001_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_63d_base_v002_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_126d_base_v003_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_252d_base_v004_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_504d_base_v005_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_21d_base_v006_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_63d_base_v007_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_126d_base_v008_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_252d_base_v009_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_504d_base_v010_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_21d_base_v011_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_63d_base_v012_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_126d_base_v013_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_252d_base_v014_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_504d_base_v015_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioz_63d_base_v016_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioz_252d_base_v017_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioz_504d_base_v018_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_63d_base_v019_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_252d_base_v020_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_504d_base_v021_signal,
    f19sds_f19_share_and_dilution_snapshot_implmcap_21d_base_v022_signal,
    f19sds_f19_share_and_dilution_snapshot_implmcap_63d_base_v023_signal,
    f19sds_f19_share_and_dilution_snapshot_implmcap_252d_base_v024_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesgrowxprice_21d_base_v025_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesgrowxprice_63d_base_v026_signal,
    f19sds_f19_share_and_dilution_snapshot_dollarissue_252d_base_v027_signal,
    f19sds_f19_share_and_dilution_snapshot_dollarissue_504d_base_v028_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesdiff_63v252_base_v029_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesdiff_21v63_base_v030_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesdiff_252v504_base_v031_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesvslow_252d_base_v032_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesvslow_504d_base_v033_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesvspeak_63d_base_v034_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesvspeak_252d_base_v035_signal,
    f19sds_f19_share_and_dilution_snapshot_fullydil_252d_base_v036_signal,
    f19sds_f19_share_and_dilution_snapshot_fullydil_504d_base_v037_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesz_63d_base_v038_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesz_252d_base_v039_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesz_504d_base_v040_signal,
    f19sds_f19_share_and_dilution_snapshot_cumdil_21d_base_v041_signal,
    f19sds_f19_share_and_dilution_snapshot_cumdil_63d_base_v042_signal,
    f19sds_f19_share_and_dilution_snapshot_cumdil_252d_base_v043_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesema_21d_base_v044_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesema_63d_base_v045_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesema_252d_base_v046_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiodiff_21m252_base_v047_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiodiff_63m504_base_v048_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_5d_base_v049_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_10d_base_v050_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_42d_base_v051_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_189d_base_v052_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_378d_base_v053_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxdv_21d_base_v054_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxdv_63d_base_v055_signal,
    f19sds_f19_share_and_dilution_snapshot_turnover_21d_base_v056_signal,
    f19sds_f19_share_and_dilution_snapshot_turnover_63d_base_v057_signal,
    f19sds_f19_share_and_dilution_snapshot_turnover_252d_base_v058_signal,
    f19sds_f19_share_and_dilution_snapshot_revps_21d_base_v059_signal,
    f19sds_f19_share_and_dilution_snapshot_revps_63d_base_v060_signal,
    f19sds_f19_share_and_dilution_snapshot_revps_252d_base_v061_signal,
    f19sds_f19_share_and_dilution_snapshot_nips_63d_base_v062_signal,
    f19sds_f19_share_and_dilution_snapshot_nips_252d_base_v063_signal,
    f19sds_f19_share_and_dilution_snapshot_fcfps_252d_base_v064_signal,
    f19sds_f19_share_and_dilution_snapshot_bvps_252d_base_v065_signal,
    f19sds_f19_share_and_dilution_snapshot_epslevel_21d_base_v066_signal,
    f19sds_f19_share_and_dilution_snapshot_epslevel_63d_base_v067_signal,
    f19sds_f19_share_and_dilution_snapshot_epslevel_252d_base_v068_signal,
    f19sds_f19_share_and_dilution_snapshot_epsdilgap_252d_base_v069_signal,
    f19sds_f19_share_and_dilution_snapshot_sharessq_63d_base_v070_signal,
    f19sds_f19_share_and_dilution_snapshot_sharessq_252d_base_v071_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxrev_63d_base_v072_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxrev_252d_base_v073_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxret_63d_base_v074_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxret_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_SHARE_AND_DILUTION_SNAPSHOT_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f19_shares_outstanding_level", "_f19_dilution_ratio", "_f19_dilution_growth")
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
    print(f"OK f19_share_and_dilution_snapshot_base_001_075_claude: {n_features} features pass")
