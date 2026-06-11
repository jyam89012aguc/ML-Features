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


def _jerk_diff(slope_series, w):
    return slope_series.diff(periods=w)


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


# 5d jerk of 21d shares level slope
def f19sds_f19_share_and_dilution_snapshot_sharesout_21d_jerk_v001_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _jerk_diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d shares level slope
def f19sds_f19_share_and_dilution_snapshot_sharesout_21d_jerk_v002_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d shares level slope
def f19sds_f19_share_and_dilution_snapshot_sharesout_63d_jerk_v003_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d shares level slope
def f19sds_f19_share_and_dilution_snapshot_sharesout_63d_jerk_v004_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d shares level slope
def f19sds_f19_share_and_dilution_snapshot_sharesout_126d_jerk_v005_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d shares level slope
def f19sds_f19_share_and_dilution_snapshot_sharesout_252d_jerk_v006_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d shares level slope
def f19sds_f19_share_and_dilution_snapshot_sharesout_252d_jerk_v007_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d shares level slope
def f19sds_f19_share_and_dilution_snapshot_sharesout_504d_jerk_v008_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d shares level slope
def f19sds_f19_share_and_dilution_snapshot_sharesout_504d_jerk_v009_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_21d_jerk_v010_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _jerk_diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_21d_jerk_v011_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_63d_jerk_v012_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_63d_jerk_v013_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_126d_jerk_v014_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_126d_jerk_v015_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_252d_jerk_v016_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_252d_jerk_v017_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_504d_jerk_v018_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d dilution ratio slope
def f19sds_f19_share_and_dilution_snapshot_dilratio_504d_jerk_v019_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d dilution growth slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_21d_jerk_v020_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 21) * closeadj
    slope = _diff(base, 5)
    result = _jerk_diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d dilution growth slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_21d_jerk_v021_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 21) * closeadj
    slope = _diff(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d dilution growth slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_63d_jerk_v022_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 63) * closeadj
    slope = _diff(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d dilution growth slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_63d_jerk_v023_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 63) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d dilution growth slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_126d_jerk_v024_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 126) * closeadj
    slope = _diff(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d dilution growth slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_126d_jerk_v025_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 126) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d dilution growth slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_252d_jerk_v026_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 252) * closeadj
    slope = _diff(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d dilution growth slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_252d_jerk_v027_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 252) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d dilution growth slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_504d_jerk_v028_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 504) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilratioz 63d slope
def f19sds_f19_share_and_dilution_snapshot_dilratioz_63d_jerk_v029_signal(sharesbas, closeadj):
    base = _z(_f19_dilution_ratio(sharesbas, 63), 63) * closeadj
    slope = _diff(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilratioz 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilratioz_252d_jerk_v030_signal(sharesbas, closeadj):
    base = _z(_f19_dilution_ratio(sharesbas, 252), 252) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilratioz 504d slope
def f19sds_f19_share_and_dilution_snapshot_dilratioz_504d_jerk_v031_signal(sharesbas, closeadj):
    base = _z(_f19_dilution_ratio(sharesbas, 504), 504) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilgrowstd 63d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_63d_jerk_v032_signal(sharesbas, closeadj):
    base = _std(_f19_dilution_growth(sharesbas, 21), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrowstd 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_252d_jerk_v033_signal(sharesbas, closeadj):
    base = _std(_f19_dilution_growth(sharesbas, 21), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of implied mcap 21d slope
def f19sds_f19_share_and_dilution_snapshot_implmcap_21d_jerk_v034_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of implied mcap 63d slope
def f19sds_f19_share_and_dilution_snapshot_implmcap_63d_jerk_v035_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of implied mcap 252d slope
def f19sds_f19_share_and_dilution_snapshot_implmcap_252d_jerk_v036_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dollar issuance 252d slope
def f19sds_f19_share_and_dilution_snapshot_dollarissue_252d_jerk_v037_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 252) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dollar issuance 504d slope
def f19sds_f19_share_and_dilution_snapshot_dollarissue_504d_jerk_v038_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 504) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesdiff 63v252 slope
def f19sds_f19_share_and_dilution_snapshot_sharesdiff_63v252_jerk_v039_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 63)
    b = _f19_shares_outstanding_level(sharesbas, 252)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesdiff 21v63 slope
def f19sds_f19_share_and_dilution_snapshot_sharesdiff_21v63_jerk_v040_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 21)
    b = _f19_shares_outstanding_level(sharesbas, 63)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharesdiff 252v504 slope
def f19sds_f19_share_and_dilution_snapshot_sharesdiff_252v504_jerk_v041_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 252)
    b = _f19_shares_outstanding_level(sharesbas, 504)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of fully diluted 252d slope
def f19sds_f19_share_and_dilution_snapshot_fullydil_252d_jerk_v042_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    base = sharesbas * (1.0 + g.clip(lower=-0.5, upper=2.0)) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of fully diluted 504d slope
def f19sds_f19_share_and_dilution_snapshot_fullydil_504d_jerk_v043_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 504)
    base = sharesbas * (1.0 + g.clip(lower=-0.5, upper=2.0)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps 63d slope
def f19sds_f19_share_and_dilution_snapshot_revps_63d_jerk_v044_signal(sharesbas, revenue, closeadj):
    rps = (revenue / _f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(rps, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revps 252d slope
def f19sds_f19_share_and_dilution_snapshot_revps_252d_jerk_v045_signal(sharesbas, revenue, closeadj):
    rps = (revenue / _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(rps, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of nips 252d slope
def f19sds_f19_share_and_dilution_snapshot_nips_252d_jerk_v046_signal(sharesbas, netinc, closeadj):
    nps = (netinc / _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(nps, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of nips 63d slope
def f19sds_f19_share_and_dilution_snapshot_nips_63d_jerk_v047_signal(sharesbas, netinc, closeadj):
    nps = (netinc / _f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(nps, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of fcfps 252d slope
def f19sds_f19_share_and_dilution_snapshot_fcfps_252d_jerk_v048_signal(sharesbas, fcf, closeadj):
    fps = (fcf / _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(fps, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of bvps 252d slope
def f19sds_f19_share_and_dilution_snapshot_bvps_252d_jerk_v049_signal(sharesbas, equity, closeadj):
    bvps = (equity / _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(bvps, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of eps level 21d slope
def f19sds_f19_share_and_dilution_snapshot_epslevel_21d_jerk_v050_signal(sharesbas, eps, closeadj):
    base = _mean(eps, 21) * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of eps level 63d slope
def f19sds_f19_share_and_dilution_snapshot_epslevel_63d_jerk_v051_signal(sharesbas, eps, closeadj):
    base = _mean(eps, 63) * closeadj + _f19_shares_outstanding_level(sharesbas, 63) * 0.0
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of eps level 252d slope
def f19sds_f19_share_and_dilution_snapshot_epslevel_252d_jerk_v052_signal(sharesbas, eps, closeadj):
    base = _mean(eps, 252) * closeadj + _f19_shares_outstanding_level(sharesbas, 252) * 0.0
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesxrev 63d slope
def f19sds_f19_share_and_dilution_snapshot_sharesxrev_63d_jerk_v053_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63) * revenue * closeadj / sharesbas.replace(0, np.nan)
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharesxrev 252d slope
def f19sds_f19_share_and_dilution_snapshot_sharesxrev_252d_jerk_v054_signal(sharesbas, revenue, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252) * revenue * closeadj / sharesbas.replace(0, np.nan)
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilxret 63d slope
def f19sds_f19_share_and_dilution_snapshot_dilxret_63d_jerk_v055_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 63)
    base = g * closeadj.pct_change(63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilxret 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilxret_252d_jerk_v056_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    base = g * closeadj.pct_change(252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of buyback 63d slope
def f19sds_f19_share_and_dilution_snapshot_buyback_63d_jerk_v057_signal(sharesbas, closeadj):
    base = _f19_shares_buyback_proxy(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of buyback 252d slope
def f19sds_f19_share_and_dilution_snapshot_buyback_252d_jerk_v058_signal(sharesbas, closeadj):
    base = _f19_shares_buyback_proxy(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of buyback 504d slope
def f19sds_f19_share_and_dilution_snapshot_buyback_504d_jerk_v059_signal(sharesbas, closeadj):
    base = _f19_shares_buyback_proxy(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of buyback dollar 252d slope
def f19sds_f19_share_and_dilution_snapshot_buybackdollar_252d_jerk_v060_signal(sharesbas, closeadj):
    base = _f19_shares_buyback_proxy(sharesbas, 252) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of buyback dollar 504d slope
def f19sds_f19_share_and_dilution_snapshot_buybackdollar_504d_jerk_v061_signal(sharesbas, closeadj):
    base = _f19_shares_buyback_proxy(sharesbas, 504) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of net repurchase 252d slope
def f19sds_f19_share_and_dilution_snapshot_netrepurchase_252d_jerk_v062_signal(sharesbas, closeadj):
    bb = _f19_shares_buyback_proxy(sharesbas, 252)
    dg = _f19_dilution_growth(sharesbas, 252)
    base = (bb - dg) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of net repurchase 504d slope
def f19sds_f19_share_and_dilution_snapshot_netrepurchase_504d_jerk_v063_signal(sharesbas, closeadj):
    bb = _f19_shares_buyback_proxy(sharesbas, 504)
    dg = _f19_dilution_growth(sharesbas, 504)
    base = (bb - dg) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of shares per revenue 21d slope
def f19sds_f19_share_and_dilution_snapshot_sharesperrev_21d_jerk_v064_signal(sharesbas, revenue, closeadj):
    spr = (_f19_shares_outstanding_level(sharesbas, 21) / revenue.replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(spr, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of shares per revenue 63d slope
def f19sds_f19_share_and_dilution_snapshot_sharesperrev_63d_jerk_v065_signal(sharesbas, revenue, closeadj):
    spr = (_f19_shares_outstanding_level(sharesbas, 63) / revenue.replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(spr, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of shares per revenue 252d slope
def f19sds_f19_share_and_dilution_snapshot_sharesperrev_252d_jerk_v066_signal(sharesbas, revenue, closeadj):
    spr = (_f19_shares_outstanding_level(sharesbas, 252) / revenue.replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(spr, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of shares per netinc 21d slope
def f19sds_f19_share_and_dilution_snapshot_shareperni_21d_jerk_v067_signal(sharesbas, netinc, closeadj):
    spn = (_f19_shares_outstanding_level(sharesbas, 21) / netinc.abs().replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(spn, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of shares per netinc 252d slope
def f19sds_f19_share_and_dilution_snapshot_shareperni_252d_jerk_v068_signal(sharesbas, netinc, closeadj):
    spn = (_f19_shares_outstanding_level(sharesbas, 252) / netinc.abs().replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(spn, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilratio diff 63m252 slope
def f19sds_f19_share_and_dilution_snapshot_dilratiodiff_63m252_jerk_v069_signal(sharesbas, closeadj):
    a = _f19_dilution_ratio(sharesbas, 63)
    b = _f19_dilution_ratio(sharesbas, 252)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilratio diff 21m63 slope
def f19sds_f19_share_and_dilution_snapshot_dilratiodiff_21m63_jerk_v070_signal(sharesbas, closeadj):
    a = _f19_dilution_ratio(sharesbas, 21)
    b = _f19_dilution_ratio(sharesbas, 63)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilratio diff 252m504 slope
def f19sds_f19_share_and_dilution_snapshot_dilratiodiff_252m504_jerk_v071_signal(sharesbas, closeadj):
    a = _f19_dilution_ratio(sharesbas, 252)
    b = _f19_dilution_ratio(sharesbas, 504)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilgrow diff 63m252 slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_63m252_jerk_v072_signal(sharesbas, closeadj):
    a = _f19_dilution_growth(sharesbas, 63)
    b = _f19_dilution_growth(sharesbas, 252)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilgrow diff 21m63 slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_21m63_jerk_v073_signal(sharesbas, closeadj):
    a = _f19_dilution_growth(sharesbas, 21)
    b = _f19_dilution_growth(sharesbas, 63)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrow diff 252m504 slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_252m504_jerk_v074_signal(sharesbas, closeadj):
    a = _f19_dilution_growth(sharesbas, 252)
    b = _f19_dilution_growth(sharesbas, 504)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilgrowmean 63d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowmean_63d_jerk_v075_signal(sharesbas, closeadj):
    base = _mean(_f19_dilution_growth(sharesbas, 252), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrowmean 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowmean_252d_jerk_v076_signal(sharesbas, closeadj):
    base = _mean(_f19_dilution_growth(sharesbas, 252), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of logshares 63d slope
def f19sds_f19_share_and_dilution_snapshot_logshares_63d_jerk_v077_signal(sharesbas, closeadj):
    base = np.log(_f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of logshares 252d slope
def f19sds_f19_share_and_dilution_snapshot_logshares_252d_jerk_v078_signal(sharesbas, closeadj):
    base = np.log(_f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of logdilratio 252d slope
def f19sds_f19_share_and_dilution_snapshot_logdilratio_252d_jerk_v079_signal(sharesbas, closeadj):
    base = np.log(_f19_dilution_ratio(sharesbas, 252).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of logdilratio 504d slope
def f19sds_f19_share_and_dilution_snapshot_logdilratio_504d_jerk_v080_signal(sharesbas, closeadj):
    base = np.log(_f19_dilution_ratio(sharesbas, 504).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrowskew 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowskew_252d_jerk_v081_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    base = g.rolling(252, min_periods=63).skew() * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrowkurt 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowkurt_252d_jerk_v082_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    base = g.rolling(252, min_periods=63).kurt() * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharesperequity 252d slope
def f19sds_f19_share_and_dilution_snapshot_sharesperequity_252d_jerk_v083_signal(sharesbas, equity, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252) / equity.abs().replace(0, np.nan) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesperequity 63d slope
def f19sds_f19_share_and_dilution_snapshot_sharesperequity_63d_jerk_v084_signal(sharesbas, equity, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63) / equity.abs().replace(0, np.nan) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesxdv 252d slope
def f19sds_f19_share_and_dilution_snapshot_sharesxdv_252d_jerk_v085_signal(sharesbas, closeadj, volume):
    base = _f19_shares_outstanding_level(sharesbas, 252) * (closeadj * volume) / sharesbas.replace(0, np.nan)
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of turnover 504d slope
def f19sds_f19_share_and_dilution_snapshot_turnover_504d_jerk_v086_signal(sharesbas, closeadj, volume):
    vsum = volume.rolling(21, min_periods=5).sum()
    base = (vsum / _f19_shares_outstanding_level(sharesbas, 504).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of fcfps 63d slope
def f19sds_f19_share_and_dilution_snapshot_fcfps_63d_jerk_v087_signal(sharesbas, fcf, closeadj):
    base = (fcf / _f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of fcfps 504d slope
def f19sds_f19_share_and_dilution_snapshot_fcfps_504d_jerk_v088_signal(sharesbas, fcf, closeadj):
    base = (fcf / _f19_shares_outstanding_level(sharesbas, 504).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of bvps 63d slope
def f19sds_f19_share_and_dilution_snapshot_bvps_63d_jerk_v089_signal(sharesbas, equity, closeadj):
    base = (equity / _f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of bvps 504d slope
def f19sds_f19_share_and_dilution_snapshot_bvps_504d_jerk_v090_signal(sharesbas, equity, closeadj):
    base = (equity / _f19_shares_outstanding_level(sharesbas, 504).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesema 21d slope
def f19sds_f19_share_and_dilution_snapshot_sharesema_21d_jerk_v091_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 5).ewm(span=21, adjust=False).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrowema 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowema_252d_jerk_v092_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilratioema 63d slope
def f19sds_f19_share_and_dilution_snapshot_dilratioema_63d_jerk_v093_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 63).ewm(span=63, adjust=False).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilratioema 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilratioema_252d_jerk_v094_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrowannual 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowannual_252d_jerk_v095_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21) * 12.0
    base = _mean(g, 252) * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrowannual 504d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowannual_504d_jerk_v096_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21) * 12.0
    base = _mean(g, 504) * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharesxeps 252d slope
def f19sds_f19_share_and_dilution_snapshot_sharesxeps_252d_jerk_v097_signal(sharesbas, eps, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252) * eps * closeadj / sharesbas.replace(0, np.nan)
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of epsxdilratio 252d slope
def f19sds_f19_share_and_dilution_snapshot_epsxdilratio_252d_jerk_v098_signal(sharesbas, eps, closeadj):
    dr = _f19_dilution_ratio(sharesbas, 252)
    base = (eps / dr.replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of epsadj 504d slope
def f19sds_f19_share_and_dilution_snapshot_epsadj_504d_jerk_v099_signal(sharesbas, eps, closeadj):
    g = _f19_dilution_growth(sharesbas, 504)
    base = (eps / (1.0 + g.clip(lower=-0.5, upper=2.0))) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of epsmean 63d slope
def f19sds_f19_share_and_dilution_snapshot_epsmean_63d_jerk_v100_signal(sharesbas, eps, closeadj):
    base = _mean(eps, 63) * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of epsmean 504d slope
def f19sds_f19_share_and_dilution_snapshot_epsmean_504d_jerk_v101_signal(sharesbas, eps, closeadj):
    base = _mean(eps, 504) * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of revpsgrow 252d slope
def f19sds_f19_share_and_dilution_snapshot_revpsgrow_252d_jerk_v102_signal(sharesbas, revenue, closeadj):
    rps = revenue / _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)
    base = rps.pct_change(252) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revpsgrow 63d slope
def f19sds_f19_share_and_dilution_snapshot_revpsgrow_63d_jerk_v103_signal(sharesbas, revenue, closeadj):
    rps = revenue / _f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)
    base = rps.pct_change(63) * closeadj
    slope = _diff(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of nipsgrow 252d slope
def f19sds_f19_share_and_dilution_snapshot_nipsgrow_252d_jerk_v104_signal(sharesbas, netinc, closeadj):
    nps = netinc / _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)
    base = nps.pct_change(252) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of fcfpsgrow 504d slope
def f19sds_f19_share_and_dilution_snapshot_fcfpsgrow_504d_jerk_v105_signal(sharesbas, fcf, closeadj):
    fps = fcf / _f19_shares_outstanding_level(sharesbas, 504).replace(0, np.nan)
    base = fps.pct_change(252) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capraised 63d slope
def f19sds_f19_share_and_dilution_snapshot_capraised_63d_jerk_v106_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 63) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capraised 252d slope
def f19sds_f19_share_and_dilution_snapshot_capraised_252d_jerk_v107_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 252) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capraised 504d slope
def f19sds_f19_share_and_dilution_snapshot_capraised_504d_jerk_v108_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 504) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capraisedsum 63d slope
def f19sds_f19_share_and_dilution_snapshot_capraisedsum_63d_jerk_v109_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    cr = g * sharesbas * closeadj
    base = cr.rolling(63, min_periods=21).sum()
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capraisedsum 252d slope
def f19sds_f19_share_and_dilution_snapshot_capraisedsum_252d_jerk_v110_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    cr = g * sharesbas * closeadj
    base = cr.rolling(252, min_periods=63).sum()
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of issuevel 63d slope
def f19sds_f19_share_and_dilution_snapshot_issuevel_63d_jerk_v111_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 1)
    base = _mean(g, 63) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of issuevel 252d slope
def f19sds_f19_share_and_dilution_snapshot_issuevel_252d_jerk_v112_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 1)
    base = _mean(g, 252) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of issuevel 504d slope
def f19sds_f19_share_and_dilution_snapshot_issuevel_504d_jerk_v113_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 1)
    base = _mean(g, 504) * sharesbas * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilratiomax 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilratiomax_252d_jerk_v114_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 63).rolling(252, min_periods=63).max() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilratiorange 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilratiorange_252d_jerk_v115_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 252)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    slope = _slope_diff_norm(rng, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilratiorange 504d slope
def f19sds_f19_share_and_dilution_snapshot_dilratiorange_504d_jerk_v116_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 504)
    rng = (base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()) * closeadj
    slope = _slope_diff_norm(rng, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of mcap diff 63m252 slope
def f19sds_f19_share_and_dilution_snapshot_mcapdiff_63m252_jerk_v117_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 63) * closeadj
    b = _f19_shares_outstanding_level(sharesbas, 252) * closeadj
    base = a - b
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of mcap diff 252m504 slope
def f19sds_f19_share_and_dilution_snapshot_mcapdiff_252m504_jerk_v118_signal(sharesbas, closeadj):
    a = _f19_shares_outstanding_level(sharesbas, 252) * closeadj
    b = _f19_shares_outstanding_level(sharesbas, 504) * closeadj
    base = a - b
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilxrevps 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilxrevps_252d_jerk_v119_signal(sharesbas, revenue, closeadj):
    rps = revenue / _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)
    g = _f19_dilution_growth(sharesbas, 252)
    base = g * rps * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilxeps 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilxeps_252d_jerk_v120_signal(sharesbas, eps, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    base = g * eps * closeadj + _f19_shares_outstanding_level(sharesbas, 21) * 0.0
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compositedil 504d slope
def f19sds_f19_share_and_dilution_snapshot_compositedil_504d_jerk_v121_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504) * np.log(_f19_dilution_ratio(sharesbas, 504).replace(0, np.nan)) * closeadj / sharesbas.replace(0, np.nan)
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compositesnp 252d slope
def f19sds_f19_share_and_dilution_snapshot_compositesnp_252d_jerk_v122_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    bb = _f19_shares_buyback_proxy(sharesbas, 252)
    base = (g + bb) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compositesnp 504d slope
def f19sds_f19_share_and_dilution_snapshot_compositesnp_504d_jerk_v123_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 504) * _f19_dilution_growth(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cumdil 63d slope
def f19sds_f19_share_and_dilution_snapshot_cumdil_63d_jerk_v124_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    base = g.rolling(63, min_periods=21).sum() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cumdil 252d slope
def f19sds_f19_share_and_dilution_snapshot_cumdil_252d_jerk_v125_signal(sharesbas, closeadj):
    g = _f19_dilution_growth(sharesbas, 21)
    base = g.rolling(252, min_periods=63).sum() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesvspeak 63d slope
def f19sds_f19_share_and_dilution_snapshot_sharesvspeak_63d_jerk_v126_signal(sharesbas, closeadj):
    peak = sharesbas.rolling(63, min_periods=21).max()
    base = (_f19_shares_outstanding_level(sharesbas, 21) / peak.replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharesvspeak 252d slope
def f19sds_f19_share_and_dilution_snapshot_sharesvspeak_252d_jerk_v127_signal(sharesbas, closeadj):
    peak = sharesbas.rolling(252, min_periods=63).max()
    base = (_f19_shares_outstanding_level(sharesbas, 21) / peak.replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesvslow 252d slope
def f19sds_f19_share_and_dilution_snapshot_sharesvslow_252d_jerk_v128_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharesvslow 504d slope
def f19sds_f19_share_and_dilution_snapshot_sharesvslow_504d_jerk_v129_signal(sharesbas, closeadj):
    base = _f19_dilution_ratio(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharessq 63d slope
def f19sds_f19_share_and_dilution_snapshot_sharessq_63d_jerk_v130_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 63)
    sq = base * base * closeadj / sharesbas.replace(0, np.nan)
    slope = _slope_diff_norm(sq, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharessq 252d slope
def f19sds_f19_share_and_dilution_snapshot_sharessq_252d_jerk_v131_signal(sharesbas, closeadj):
    base = _f19_shares_outstanding_level(sharesbas, 252)
    sq = base * base * closeadj / sharesbas.replace(0, np.nan)
    slope = _slope_diff_norm(sq, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilxequity 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilxequity_252d_jerk_v132_signal(sharesbas, equity, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    base = g * equity.abs() * closeadj / equity.abs().replace(0, np.nan)
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilxrev 63d slope
def f19sds_f19_share_and_dilution_snapshot_dilxrev_63d_jerk_v133_signal(sharesbas, revenue, closeadj):
    g = _f19_dilution_growth(sharesbas, 63)
    base = g * revenue * closeadj / revenue.replace(0, np.nan)
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilxni 252d slope
def f19sds_f19_share_and_dilution_snapshot_dilxni_252d_jerk_v134_signal(sharesbas, netinc, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    base = g * netinc.abs() * closeadj / netinc.abs().replace(0, np.nan)
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilxfcf 504d slope
def f19sds_f19_share_and_dilution_snapshot_dilxfcf_504d_jerk_v135_signal(sharesbas, fcf, closeadj):
    g = _f19_dilution_growth(sharesbas, 504)
    base = g * fcf.abs() * closeadj / fcf.abs().replace(0, np.nan)
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesz 63d slope
def f19sds_f19_share_and_dilution_snapshot_sharesz_63d_jerk_v136_signal(sharesbas, closeadj):
    base = _z(_f19_shares_outstanding_level(sharesbas, 5), 63) * closeadj
    slope = _diff(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharesz 252d slope
def f19sds_f19_share_and_dilution_snapshot_sharesz_252d_jerk_v137_signal(sharesbas, closeadj):
    base = _z(_f19_shares_outstanding_level(sharesbas, 21), 252) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharesz 504d slope
def f19sds_f19_share_and_dilution_snapshot_sharesz_504d_jerk_v138_signal(sharesbas, closeadj):
    base = _z(_f19_shares_outstanding_level(sharesbas, 21), 504) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of dilgrowth 5d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_5d_jerk_v139_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 5) * closeadj
    slope = _diff(base, 5)
    result = _jerk_diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of dilgrowth 10d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_10d_jerk_v140_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 10) * closeadj
    slope = _diff(base, 5)
    result = _jerk_diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dilgrowth 42d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_42d_jerk_v141_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 42) * closeadj
    slope = _diff(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrowth 189d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_189d_jerk_v142_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 189) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dilgrowth 378d slope
def f19sds_f19_share_and_dilution_snapshot_dilgrowth_378d_jerk_v143_signal(sharesbas, closeadj):
    base = _f19_dilution_growth(sharesbas, 378) * closeadj
    slope = _diff(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of sharesxdv 21d slope
def f19sds_f19_share_and_dilution_snapshot_sharesxdv_21d_jerk_v144_signal(sharesbas, closeadj, volume):
    base = _f19_shares_outstanding_level(sharesbas, 21) * (closeadj * volume) / sharesbas.replace(0, np.nan)
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sharesxdv 63d slope
def f19sds_f19_share_and_dilution_snapshot_sharesxdv_63d_jerk_v145_signal(sharesbas, closeadj, volume):
    base = _f19_shares_outstanding_level(sharesbas, 63) * (closeadj * volume) / sharesbas.replace(0, np.nan)
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of turnover 21d slope
def f19sds_f19_share_and_dilution_snapshot_turnover_21d_jerk_v146_signal(sharesbas, closeadj, volume):
    vsum = volume.rolling(21, min_periods=5).sum()
    base = (vsum / _f19_shares_outstanding_level(sharesbas, 21).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of turnover 63d slope
def f19sds_f19_share_and_dilution_snapshot_turnover_63d_jerk_v147_signal(sharesbas, closeadj, volume):
    vsum = volume.rolling(21, min_periods=5).sum()
    base = (vsum / _f19_shares_outstanding_level(sharesbas, 63).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of turnover 252d slope
def f19sds_f19_share_and_dilution_snapshot_turnover_252d_jerk_v148_signal(sharesbas, closeadj, volume):
    vsum = volume.rolling(21, min_periods=5).sum()
    base = (vsum / _f19_shares_outstanding_level(sharesbas, 252).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of revps 21d slope
def f19sds_f19_share_and_dilution_snapshot_revps_21d_jerk_v149_signal(sharesbas, revenue, closeadj):
    rps = (revenue / _f19_shares_outstanding_level(sharesbas, 21).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(rps, 21)
    result = _jerk_diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of epsdilgap 252d slope
def f19sds_f19_share_and_dilution_snapshot_epsdilgap_252d_jerk_v150_signal(sharesbas, eps, closeadj):
    g = _f19_dilution_growth(sharesbas, 252)
    base = (eps - g.clip(lower=-0.5, upper=2.0)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _jerk_diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19sds_f19_share_and_dilution_snapshot_sharesout_21d_jerk_v001_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_21d_jerk_v002_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_63d_jerk_v003_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_63d_jerk_v004_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_126d_jerk_v005_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_252d_jerk_v006_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_252d_jerk_v007_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_504d_jerk_v008_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesout_504d_jerk_v009_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_21d_jerk_v010_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_21d_jerk_v011_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_63d_jerk_v012_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_63d_jerk_v013_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_126d_jerk_v014_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_126d_jerk_v015_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_252d_jerk_v016_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_252d_jerk_v017_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_504d_jerk_v018_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratio_504d_jerk_v019_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_21d_jerk_v020_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_21d_jerk_v021_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_63d_jerk_v022_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_63d_jerk_v023_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_126d_jerk_v024_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_126d_jerk_v025_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_252d_jerk_v026_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_252d_jerk_v027_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_504d_jerk_v028_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioz_63d_jerk_v029_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioz_252d_jerk_v030_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioz_504d_jerk_v031_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_63d_jerk_v032_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowthstd_252d_jerk_v033_signal,
    f19sds_f19_share_and_dilution_snapshot_implmcap_21d_jerk_v034_signal,
    f19sds_f19_share_and_dilution_snapshot_implmcap_63d_jerk_v035_signal,
    f19sds_f19_share_and_dilution_snapshot_implmcap_252d_jerk_v036_signal,
    f19sds_f19_share_and_dilution_snapshot_dollarissue_252d_jerk_v037_signal,
    f19sds_f19_share_and_dilution_snapshot_dollarissue_504d_jerk_v038_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesdiff_63v252_jerk_v039_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesdiff_21v63_jerk_v040_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesdiff_252v504_jerk_v041_signal,
    f19sds_f19_share_and_dilution_snapshot_fullydil_252d_jerk_v042_signal,
    f19sds_f19_share_and_dilution_snapshot_fullydil_504d_jerk_v043_signal,
    f19sds_f19_share_and_dilution_snapshot_revps_63d_jerk_v044_signal,
    f19sds_f19_share_and_dilution_snapshot_revps_252d_jerk_v045_signal,
    f19sds_f19_share_and_dilution_snapshot_nips_252d_jerk_v046_signal,
    f19sds_f19_share_and_dilution_snapshot_nips_63d_jerk_v047_signal,
    f19sds_f19_share_and_dilution_snapshot_fcfps_252d_jerk_v048_signal,
    f19sds_f19_share_and_dilution_snapshot_bvps_252d_jerk_v049_signal,
    f19sds_f19_share_and_dilution_snapshot_epslevel_21d_jerk_v050_signal,
    f19sds_f19_share_and_dilution_snapshot_epslevel_63d_jerk_v051_signal,
    f19sds_f19_share_and_dilution_snapshot_epslevel_252d_jerk_v052_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxrev_63d_jerk_v053_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxrev_252d_jerk_v054_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxret_63d_jerk_v055_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxret_252d_jerk_v056_signal,
    f19sds_f19_share_and_dilution_snapshot_buyback_63d_jerk_v057_signal,
    f19sds_f19_share_and_dilution_snapshot_buyback_252d_jerk_v058_signal,
    f19sds_f19_share_and_dilution_snapshot_buyback_504d_jerk_v059_signal,
    f19sds_f19_share_and_dilution_snapshot_buybackdollar_252d_jerk_v060_signal,
    f19sds_f19_share_and_dilution_snapshot_buybackdollar_504d_jerk_v061_signal,
    f19sds_f19_share_and_dilution_snapshot_netrepurchase_252d_jerk_v062_signal,
    f19sds_f19_share_and_dilution_snapshot_netrepurchase_504d_jerk_v063_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperrev_21d_jerk_v064_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperrev_63d_jerk_v065_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperrev_252d_jerk_v066_signal,
    f19sds_f19_share_and_dilution_snapshot_shareperni_21d_jerk_v067_signal,
    f19sds_f19_share_and_dilution_snapshot_shareperni_252d_jerk_v068_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiodiff_63m252_jerk_v069_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiodiff_21m63_jerk_v070_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiodiff_252m504_jerk_v071_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_63m252_jerk_v072_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_21m63_jerk_v073_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowdiff_252m504_jerk_v074_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowmean_63d_jerk_v075_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowmean_252d_jerk_v076_signal,
    f19sds_f19_share_and_dilution_snapshot_logshares_63d_jerk_v077_signal,
    f19sds_f19_share_and_dilution_snapshot_logshares_252d_jerk_v078_signal,
    f19sds_f19_share_and_dilution_snapshot_logdilratio_252d_jerk_v079_signal,
    f19sds_f19_share_and_dilution_snapshot_logdilratio_504d_jerk_v080_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowskew_252d_jerk_v081_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowkurt_252d_jerk_v082_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperequity_252d_jerk_v083_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesperequity_63d_jerk_v084_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxdv_252d_jerk_v085_signal,
    f19sds_f19_share_and_dilution_snapshot_turnover_504d_jerk_v086_signal,
    f19sds_f19_share_and_dilution_snapshot_fcfps_63d_jerk_v087_signal,
    f19sds_f19_share_and_dilution_snapshot_fcfps_504d_jerk_v088_signal,
    f19sds_f19_share_and_dilution_snapshot_bvps_63d_jerk_v089_signal,
    f19sds_f19_share_and_dilution_snapshot_bvps_504d_jerk_v090_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesema_21d_jerk_v091_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowema_252d_jerk_v092_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioema_63d_jerk_v093_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratioema_252d_jerk_v094_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowannual_252d_jerk_v095_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowannual_504d_jerk_v096_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxeps_252d_jerk_v097_signal,
    f19sds_f19_share_and_dilution_snapshot_epsxdilratio_252d_jerk_v098_signal,
    f19sds_f19_share_and_dilution_snapshot_epsadj_504d_jerk_v099_signal,
    f19sds_f19_share_and_dilution_snapshot_epsmean_63d_jerk_v100_signal,
    f19sds_f19_share_and_dilution_snapshot_epsmean_504d_jerk_v101_signal,
    f19sds_f19_share_and_dilution_snapshot_revpsgrow_252d_jerk_v102_signal,
    f19sds_f19_share_and_dilution_snapshot_revpsgrow_63d_jerk_v103_signal,
    f19sds_f19_share_and_dilution_snapshot_nipsgrow_252d_jerk_v104_signal,
    f19sds_f19_share_and_dilution_snapshot_fcfpsgrow_504d_jerk_v105_signal,
    f19sds_f19_share_and_dilution_snapshot_capraised_63d_jerk_v106_signal,
    f19sds_f19_share_and_dilution_snapshot_capraised_252d_jerk_v107_signal,
    f19sds_f19_share_and_dilution_snapshot_capraised_504d_jerk_v108_signal,
    f19sds_f19_share_and_dilution_snapshot_capraisedsum_63d_jerk_v109_signal,
    f19sds_f19_share_and_dilution_snapshot_capraisedsum_252d_jerk_v110_signal,
    f19sds_f19_share_and_dilution_snapshot_issuevel_63d_jerk_v111_signal,
    f19sds_f19_share_and_dilution_snapshot_issuevel_252d_jerk_v112_signal,
    f19sds_f19_share_and_dilution_snapshot_issuevel_504d_jerk_v113_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiomax_252d_jerk_v114_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiorange_252d_jerk_v115_signal,
    f19sds_f19_share_and_dilution_snapshot_dilratiorange_504d_jerk_v116_signal,
    f19sds_f19_share_and_dilution_snapshot_mcapdiff_63m252_jerk_v117_signal,
    f19sds_f19_share_and_dilution_snapshot_mcapdiff_252m504_jerk_v118_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxrevps_252d_jerk_v119_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxeps_252d_jerk_v120_signal,
    f19sds_f19_share_and_dilution_snapshot_compositedil_504d_jerk_v121_signal,
    f19sds_f19_share_and_dilution_snapshot_compositesnp_252d_jerk_v122_signal,
    f19sds_f19_share_and_dilution_snapshot_compositesnp_504d_jerk_v123_signal,
    f19sds_f19_share_and_dilution_snapshot_cumdil_63d_jerk_v124_signal,
    f19sds_f19_share_and_dilution_snapshot_cumdil_252d_jerk_v125_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesvspeak_63d_jerk_v126_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesvspeak_252d_jerk_v127_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesvslow_252d_jerk_v128_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesvslow_504d_jerk_v129_signal,
    f19sds_f19_share_and_dilution_snapshot_sharessq_63d_jerk_v130_signal,
    f19sds_f19_share_and_dilution_snapshot_sharessq_252d_jerk_v131_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxequity_252d_jerk_v132_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxrev_63d_jerk_v133_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxni_252d_jerk_v134_signal,
    f19sds_f19_share_and_dilution_snapshot_dilxfcf_504d_jerk_v135_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesz_63d_jerk_v136_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesz_252d_jerk_v137_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesz_504d_jerk_v138_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_5d_jerk_v139_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_10d_jerk_v140_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_42d_jerk_v141_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_189d_jerk_v142_signal,
    f19sds_f19_share_and_dilution_snapshot_dilgrowth_378d_jerk_v143_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxdv_21d_jerk_v144_signal,
    f19sds_f19_share_and_dilution_snapshot_sharesxdv_63d_jerk_v145_signal,
    f19sds_f19_share_and_dilution_snapshot_turnover_21d_jerk_v146_signal,
    f19sds_f19_share_and_dilution_snapshot_turnover_63d_jerk_v147_signal,
    f19sds_f19_share_and_dilution_snapshot_turnover_252d_jerk_v148_signal,
    f19sds_f19_share_and_dilution_snapshot_revps_21d_jerk_v149_signal,
    f19sds_f19_share_and_dilution_snapshot_epsdilgap_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_SHARE_AND_DILUTION_SNAPSHOT_REGISTRY_JERK = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f19_share_and_dilution_snapshot_3rd_derivatives_001_150_claude: {n_features} features pass")
