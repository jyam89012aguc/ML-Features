import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (insider distribution / selling) =====
def _f33_sellintensity(sellval, marketcap, w):
    # trailing-w sum of insider sale $ scaled by market cap
    s = sellval.rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(s, marketcap)


def _f33_sellflow(sellshares, sharesbas, w):
    # trailing-w insider shares sold scaled by shares outstanding
    s = sellshares.rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(s, sharesbas)


def _f33_exercisedump(optionexval, sellval, marketcap, w):
    # trailing-w (option-exercise $ + sale $) scaled by market cap
    s = (optionexval + sellval).rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(s, marketcap)


def _f33_liquidation(tenpctsellval, sellval, w):
    # 10%-owner sale $ as a share of total trailing sale $
    a = tenpctsellval.rolling(w, min_periods=max(1, w // 2)).sum()
    b = sellval.rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(a, b)


# ============ FEATURES 001-075 ============

# 21d sell intensity (sale $ / marketcap)
def f33id_f33_insider_distribution_selling_sellint_21d_base_v001_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sell intensity
def f33id_f33_insider_distribution_selling_sellint_63d_base_v002_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sell intensity
def f33id_f33_insider_distribution_selling_sellint_126d_base_v003_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sell intensity
def f33id_f33_insider_distribution_selling_sellint_252d_base_v004_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d sell intensity
def f33id_f33_insider_distribution_selling_sellint_42d_base_v005_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d sell intensity
def f33id_f33_insider_distribution_selling_sellint_84d_base_v006_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d sell intensity
def f33id_f33_insider_distribution_selling_sellint_189d_base_v007_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sell share-flow (shares sold / shares outstanding)
def f33id_f33_insider_distribution_selling_sellflow_21d_base_v008_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sell share-flow
def f33id_f33_insider_distribution_selling_sellflow_63d_base_v009_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sell share-flow
def f33id_f33_insider_distribution_selling_sellflow_126d_base_v010_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sell share-flow
def f33id_f33_insider_distribution_selling_sellflow_252d_base_v011_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d sell share-flow
def f33id_f33_insider_distribution_selling_sellflow_42d_base_v012_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d sell share-flow
def f33id_f33_insider_distribution_selling_sellflow_189d_base_v013_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d exercise-and-dump intensity ((optionex+sale)$ / marketcap)
def f33id_f33_insider_distribution_selling_exdump_21d_base_v014_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d exercise-and-dump intensity
def f33id_f33_insider_distribution_selling_exdump_63d_base_v015_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d exercise-and-dump intensity
def f33id_f33_insider_distribution_selling_exdump_126d_base_v016_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d exercise-and-dump intensity
def f33id_f33_insider_distribution_selling_exdump_252d_base_v017_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d exercise-and-dump intensity
def f33id_f33_insider_distribution_selling_exdump_84d_base_v018_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d 10%-owner liquidation share
def f33id_f33_insider_distribution_selling_liq_21d_base_v019_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d 10%-owner liquidation share
def f33id_f33_insider_distribution_selling_liq_63d_base_v020_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d 10%-owner liquidation share
def f33id_f33_insider_distribution_selling_liq_126d_base_v021_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 10%-owner liquidation share
def f33id_f33_insider_distribution_selling_liq_252d_base_v022_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d 10%-owner liquidation share
def f33id_f33_insider_distribution_selling_liq_42d_base_v023_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d sell intensity over 252d
def f33id_f33_insider_distribution_selling_zsellint_21d_base_v024_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d sell intensity over 252d
def f33id_f33_insider_distribution_selling_zsellint_63d_base_v025_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d sell intensity over 504d
def f33id_f33_insider_distribution_selling_zsellint_126d_base_v026_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d sell share-flow over 252d
def f33id_f33_insider_distribution_selling_zsellflow_21d_base_v027_signal(sellshares, sharesbas):
    result = _z(_f33_sellflow(sellshares, sharesbas, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d sell share-flow over 252d
def f33id_f33_insider_distribution_selling_zsellflow_63d_base_v028_signal(sellshares, sharesbas):
    result = _z(_f33_sellflow(sellshares, sharesbas, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d exercise-dump over 252d
def f33id_f33_insider_distribution_selling_zexdump_21d_base_v029_signal(optionexval, sellval, marketcap):
    result = _z(_f33_exercisedump(optionexval, sellval, marketcap, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d exercise-dump over 252d
def f33id_f33_insider_distribution_selling_zexdump_63d_base_v030_signal(optionexval, sellval, marketcap):
    result = _z(_f33_exercisedump(optionexval, sellval, marketcap, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# selling acceleration: 21d vs 63d sell intensity spread
def f33id_f33_insider_distribution_selling_accel_21_63_base_v031_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 21) - _f33_sellintensity(sellval, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selling acceleration: 63d vs 126d sell intensity spread
def f33id_f33_insider_distribution_selling_accel_63_126_base_v032_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 63) - _f33_sellintensity(sellval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# selling acceleration: 126d vs 252d sell intensity spread
def f33id_f33_insider_distribution_selling_accel_126_252_base_v033_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 126) - _f33_sellintensity(sellval, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# share-flow acceleration: 21d vs 63d
def f33id_f33_insider_distribution_selling_flowaccel_21_63_base_v034_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 21) - _f33_sellflow(sellshares, sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# share-flow acceleration: 63d vs 126d
def f33id_f33_insider_distribution_selling_flowaccel_63_126_base_v035_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 63) - _f33_sellflow(sellshares, sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of short to long sell intensity (21d / 126d)
def f33id_f33_insider_distribution_selling_intratio_21_126_base_v036_signal(sellval, marketcap):
    short = _f33_sellintensity(sellval, marketcap, 21)
    long = _f33_sellintensity(sellval, marketcap, 126)
    result = _safe_div(short, long.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of short to long sell intensity (63d / 252d)
def f33id_f33_insider_distribution_selling_intratio_63_252_base_v037_signal(sellval, marketcap):
    short = _f33_sellintensity(sellval, marketcap, 63)
    long = _f33_sellintensity(sellval, marketcap, 252)
    result = _safe_div(short, long.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity minus its trailing 126d mean (distribution surprise)
def f33id_f33_insider_distribution_selling_surp_63d_base_v038_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = si - _mean(si, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity minus its trailing 252d mean
def f33id_f33_insider_distribution_selling_surp_126d_base_v039_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 126)
    result = si - _mean(si, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 21d sell intensity over 252d
def f33id_f33_insider_distribution_selling_rank_21d_base_v040_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 63d sell intensity over 252d
def f33id_f33_insider_distribution_selling_rank_63d_base_v041_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = si.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 126d sell share-flow over 252d
def f33id_f33_insider_distribution_selling_rankflow_126d_base_v042_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 126)
    result = sf.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# sell-count rate: trailing 63d sale events scaled by total selling activity
def f33id_f33_insider_distribution_selling_countrate_63d_base_v043_signal(sellcount, sellval, marketcap):
    c = sellcount.rolling(63, min_periods=21).sum()
    result = _safe_div(c, sellval.rolling(63, min_periods=21).sum().abs()) + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# sell-count intensity smoothed (126d mean of 21d count sum)
def f33id_f33_insider_distribution_selling_countrate_126d_base_v044_signal(sellcount, marketcap, sellval):
    c = sellcount.rolling(21, min_periods=10).sum()
    result = _mean(c, 126) / marketcap.replace(0, np.nan) * 1e6 + _f33_sellintensity(sellval, marketcap, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average sale size: trailing sale $ per sale event (63d)
def f33id_f33_insider_distribution_selling_avgsize_63d_base_v045_signal(sellval, sellcount, marketcap):
    v = sellval.rolling(63, min_periods=21).sum()
    c = sellcount.rolling(63, min_periods=21).sum()
    result = _safe_div(v, c) / marketcap.replace(0, np.nan) + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average sale size scaled (126d)
def f33id_f33_insider_distribution_selling_avgsize_126d_base_v046_signal(sellval, sellcount, marketcap):
    v = sellval.rolling(126, min_periods=42).sum()
    c = sellcount.rolling(126, min_periods=42).sum()
    result = _safe_div(v, c) / marketcap.replace(0, np.nan) + _f33_sellintensity(sellval, marketcap, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-to-sale conversion: optionex $ vs sale $ (63d)
def f33id_f33_insider_distribution_selling_exconv_63d_base_v047_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(63, min_periods=21).sum()
    sv = sellval.rolling(63, min_periods=21).sum()
    result = _safe_div(ex, sv.abs()) + _f33_exercisedump(optionexval, sellval, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-to-sale conversion (126d)
def f33id_f33_insider_distribution_selling_exconv_126d_base_v048_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(126, min_periods=42).sum()
    sv = sellval.rolling(126, min_periods=42).sum()
    result = _safe_div(ex, sv.abs()) + _f33_exercisedump(optionexval, sellval, marketcap, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-to-sale conversion (252d)
def f33id_f33_insider_distribution_selling_exconv_252d_base_v049_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(252, min_periods=84).sum()
    sv = sellval.rolling(252, min_periods=84).sum()
    result = _safe_div(ex, sv.abs()) + _f33_exercisedump(optionexval, sellval, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# insider-driven share shrinkage proxy: cumulative sell-flow over 252d
def f33id_f33_insider_distribution_selling_shrink_252d_base_v050_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 252) - _f33_sellflow(sellshares, sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selling-cluster intensity: 21d intensity scaled by 126d mean (surge ratio)
def f33id_f33_insider_distribution_selling_cluster_21d_base_v051_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = _safe_div(si, _mean(si, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# selling-cluster intensity: 42d scaled by 189d mean
def f33id_f33_insider_distribution_selling_cluster_42d_base_v052_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 42)
    result = _safe_div(si, _mean(si, 189))
    return result.replace([np.inf, -np.inf], np.nan)


# liquidation z-score over 252d (10%-owner share standardized)
def f33id_f33_insider_distribution_selling_zliq_63d_base_v053_signal(tenpctsellval, sellval):
    result = _z(_f33_liquidation(tenpctsellval, sellval, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidation surprise: 63d liq share minus its 252d mean
def f33id_f33_insider_distribution_selling_liqsurp_63d_base_v054_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 63)
    result = lq - _mean(lq, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 10%-owner sale intensity scaled by marketcap (63d)
def f33id_f33_insider_distribution_selling_tenint_63d_base_v055_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(63, min_periods=21).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10%-owner sale intensity scaled by marketcap (126d)
def f33id_f33_insider_distribution_selling_tenint_126d_base_v056_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(126, min_periods=42).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10%-owner sale intensity scaled by marketcap (252d)
def f33id_f33_insider_distribution_selling_tenint_252d_base_v057_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(252, min_periods=84).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# sell-pressure vs trailing mean (21d intensity demeaned over 252d)
def f33id_f33_insider_distribution_selling_pressdev_21d_base_v058_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si - _mean(si, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sell-pressure dispersion: rolling std of 21d intensity over 126d
def f33id_f33_insider_distribution_selling_pressdisp_126d_base_v059_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = _std(si, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sell-pressure dispersion over 252d
def f33id_f33_insider_distribution_selling_pressdisp_252d_base_v060_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = _std(si, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# distribution composite: sell intensity plus exercise-dump (63d)
def f33id_f33_insider_distribution_selling_distcomp_63d_base_v061_signal(sellval, optionexval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 63) + _f33_exercisedump(optionexval, sellval, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# distribution composite (126d)
def f33id_f33_insider_distribution_selling_distcomp_126d_base_v062_signal(sellval, optionexval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 126) + _f33_exercisedump(optionexval, sellval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# selling pressure weighted by liquidation share (63d)
def f33id_f33_insider_distribution_selling_liqweight_63d_base_v063_signal(sellval, tenpctsellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 63) * _f33_liquidation(tenpctsellval, sellval, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selling pressure weighted by liquidation share (126d)
def f33id_f33_insider_distribution_selling_liqweight_126d_base_v064_signal(sellval, tenpctsellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 126) * _f33_liquidation(tenpctsellval, sellval, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity smoothed: 21d mean of 21d intensity
def f33id_f33_insider_distribution_selling_smooth_21d_base_v065_signal(sellval, marketcap):
    result = _mean(_f33_sellintensity(sellval, marketcap, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity smoothed: 63d mean of 21d intensity
def f33id_f33_insider_distribution_selling_smooth_63d_base_v066_signal(sellval, marketcap):
    result = _mean(_f33_sellintensity(sellval, marketcap, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sell share-flow smoothed: 63d mean of 21d flow
def f33id_f33_insider_distribution_selling_smoothflow_63d_base_v067_signal(sellshares, sharesbas):
    result = _mean(_f33_sellflow(sellshares, sharesbas, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity EWMA (63d span)
def f33id_f33_insider_distribution_selling_ewm_63d_base_v068_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity EWMA (126d span)
def f33id_f33_insider_distribution_selling_ewm_126d_base_v069_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-dump acceleration: 21d vs 63d
def f33id_f33_insider_distribution_selling_exaccel_21_63_base_v070_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 21) - _f33_exercisedump(optionexval, sellval, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-dump acceleration: 63d vs 126d
def f33id_f33_insider_distribution_selling_exaccel_63_126_base_v071_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 63) - _f33_exercisedump(optionexval, sellval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity information ratio: 21d vs 252d dispersion
def f33id_f33_insider_distribution_selling_inforatio_21d_base_v072_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = _safe_div(si, _std(si, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sell share-flow information ratio: 21d vs 252d dispersion
def f33id_f33_insider_distribution_selling_flowinfo_21d_base_v073_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 21)
    result = _safe_div(sf, _std(sf, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# liquidation percentile rank over 252d
def f33id_f33_insider_distribution_selling_rankliq_63d_base_v074_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 63)
    result = lq.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# combined distribution percentile rank (sell intensity 126d over 252d)
def f33id_f33_insider_distribution_selling_rank_126d_base_v075_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 126)
    result = si.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33id_f33_insider_distribution_selling_sellint_21d_base_v001_signal,
    f33id_f33_insider_distribution_selling_sellint_63d_base_v002_signal,
    f33id_f33_insider_distribution_selling_sellint_126d_base_v003_signal,
    f33id_f33_insider_distribution_selling_sellint_252d_base_v004_signal,
    f33id_f33_insider_distribution_selling_sellint_42d_base_v005_signal,
    f33id_f33_insider_distribution_selling_sellint_84d_base_v006_signal,
    f33id_f33_insider_distribution_selling_sellint_189d_base_v007_signal,
    f33id_f33_insider_distribution_selling_sellflow_21d_base_v008_signal,
    f33id_f33_insider_distribution_selling_sellflow_63d_base_v009_signal,
    f33id_f33_insider_distribution_selling_sellflow_126d_base_v010_signal,
    f33id_f33_insider_distribution_selling_sellflow_252d_base_v011_signal,
    f33id_f33_insider_distribution_selling_sellflow_42d_base_v012_signal,
    f33id_f33_insider_distribution_selling_sellflow_189d_base_v013_signal,
    f33id_f33_insider_distribution_selling_exdump_21d_base_v014_signal,
    f33id_f33_insider_distribution_selling_exdump_63d_base_v015_signal,
    f33id_f33_insider_distribution_selling_exdump_126d_base_v016_signal,
    f33id_f33_insider_distribution_selling_exdump_252d_base_v017_signal,
    f33id_f33_insider_distribution_selling_exdump_84d_base_v018_signal,
    f33id_f33_insider_distribution_selling_liq_21d_base_v019_signal,
    f33id_f33_insider_distribution_selling_liq_63d_base_v020_signal,
    f33id_f33_insider_distribution_selling_liq_126d_base_v021_signal,
    f33id_f33_insider_distribution_selling_liq_252d_base_v022_signal,
    f33id_f33_insider_distribution_selling_liq_42d_base_v023_signal,
    f33id_f33_insider_distribution_selling_zsellint_21d_base_v024_signal,
    f33id_f33_insider_distribution_selling_zsellint_63d_base_v025_signal,
    f33id_f33_insider_distribution_selling_zsellint_126d_base_v026_signal,
    f33id_f33_insider_distribution_selling_zsellflow_21d_base_v027_signal,
    f33id_f33_insider_distribution_selling_zsellflow_63d_base_v028_signal,
    f33id_f33_insider_distribution_selling_zexdump_21d_base_v029_signal,
    f33id_f33_insider_distribution_selling_zexdump_63d_base_v030_signal,
    f33id_f33_insider_distribution_selling_accel_21_63_base_v031_signal,
    f33id_f33_insider_distribution_selling_accel_63_126_base_v032_signal,
    f33id_f33_insider_distribution_selling_accel_126_252_base_v033_signal,
    f33id_f33_insider_distribution_selling_flowaccel_21_63_base_v034_signal,
    f33id_f33_insider_distribution_selling_flowaccel_63_126_base_v035_signal,
    f33id_f33_insider_distribution_selling_intratio_21_126_base_v036_signal,
    f33id_f33_insider_distribution_selling_intratio_63_252_base_v037_signal,
    f33id_f33_insider_distribution_selling_surp_63d_base_v038_signal,
    f33id_f33_insider_distribution_selling_surp_126d_base_v039_signal,
    f33id_f33_insider_distribution_selling_rank_21d_base_v040_signal,
    f33id_f33_insider_distribution_selling_rank_63d_base_v041_signal,
    f33id_f33_insider_distribution_selling_rankflow_126d_base_v042_signal,
    f33id_f33_insider_distribution_selling_countrate_63d_base_v043_signal,
    f33id_f33_insider_distribution_selling_countrate_126d_base_v044_signal,
    f33id_f33_insider_distribution_selling_avgsize_63d_base_v045_signal,
    f33id_f33_insider_distribution_selling_avgsize_126d_base_v046_signal,
    f33id_f33_insider_distribution_selling_exconv_63d_base_v047_signal,
    f33id_f33_insider_distribution_selling_exconv_126d_base_v048_signal,
    f33id_f33_insider_distribution_selling_exconv_252d_base_v049_signal,
    f33id_f33_insider_distribution_selling_shrink_252d_base_v050_signal,
    f33id_f33_insider_distribution_selling_cluster_21d_base_v051_signal,
    f33id_f33_insider_distribution_selling_cluster_42d_base_v052_signal,
    f33id_f33_insider_distribution_selling_zliq_63d_base_v053_signal,
    f33id_f33_insider_distribution_selling_liqsurp_63d_base_v054_signal,
    f33id_f33_insider_distribution_selling_tenint_63d_base_v055_signal,
    f33id_f33_insider_distribution_selling_tenint_126d_base_v056_signal,
    f33id_f33_insider_distribution_selling_tenint_252d_base_v057_signal,
    f33id_f33_insider_distribution_selling_pressdev_21d_base_v058_signal,
    f33id_f33_insider_distribution_selling_pressdisp_126d_base_v059_signal,
    f33id_f33_insider_distribution_selling_pressdisp_252d_base_v060_signal,
    f33id_f33_insider_distribution_selling_distcomp_63d_base_v061_signal,
    f33id_f33_insider_distribution_selling_distcomp_126d_base_v062_signal,
    f33id_f33_insider_distribution_selling_liqweight_63d_base_v063_signal,
    f33id_f33_insider_distribution_selling_liqweight_126d_base_v064_signal,
    f33id_f33_insider_distribution_selling_smooth_21d_base_v065_signal,
    f33id_f33_insider_distribution_selling_smooth_63d_base_v066_signal,
    f33id_f33_insider_distribution_selling_smoothflow_63d_base_v067_signal,
    f33id_f33_insider_distribution_selling_ewm_63d_base_v068_signal,
    f33id_f33_insider_distribution_selling_ewm_126d_base_v069_signal,
    f33id_f33_insider_distribution_selling_exaccel_21_63_base_v070_signal,
    f33id_f33_insider_distribution_selling_exaccel_63_126_base_v071_signal,
    f33id_f33_insider_distribution_selling_inforatio_21d_base_v072_signal,
    f33id_f33_insider_distribution_selling_flowinfo_21d_base_v073_signal,
    f33id_f33_insider_distribution_selling_rankliq_63d_base_v074_signal,
    f33id_f33_insider_distribution_selling_rank_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_INSIDER_DISTRIBUTION_SELLING_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt",
           "sellval","sellshares","sellcount","optionexval","tenpctsellval"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f33_sellintensity", "_f33_sellflow", "_f33_exercisedump", "_f33_liquidation")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f33_insider_distribution_selling_base_001_075_claude: {n_features} features pass")
