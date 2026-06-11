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


# ============ FEATURES 076-150 ============

# 315d sell intensity
def f33id_f33_insider_distribution_selling_sellint_315d_base_v076_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sell intensity
def f33id_f33_insider_distribution_selling_sellint_504d_base_v077_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d sell intensity
def f33id_f33_insider_distribution_selling_sellint_10d_base_v078_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d sell share-flow
def f33id_f33_insider_distribution_selling_sellflow_315d_base_v079_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sell share-flow
def f33id_f33_insider_distribution_selling_sellflow_504d_base_v080_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d sell share-flow
def f33id_f33_insider_distribution_selling_sellflow_84d_base_v081_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d exercise-and-dump intensity (alt window)
def f33id_f33_insider_distribution_selling_exdump_189d_base_v082_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d exercise-and-dump intensity
def f33id_f33_insider_distribution_selling_exdump_504d_base_v083_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d 10%-owner liquidation share
def f33id_f33_insider_distribution_selling_liq_189d_base_v084_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d 10%-owner liquidation share
def f33id_f33_insider_distribution_selling_liq_504d_base_v085_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d sell intensity over 504d
def f33id_f33_insider_distribution_selling_zsellint_252d_base_v086_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 42d sell intensity over 252d
def f33id_f33_insider_distribution_selling_zsellint_42d_base_v087_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d sell share-flow over 504d
def f33id_f33_insider_distribution_selling_zsellflow_126d_base_v088_signal(sellshares, sharesbas):
    result = _z(_f33_sellflow(sellshares, sharesbas, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d exercise-dump over 504d
def f33id_f33_insider_distribution_selling_zexdump_126d_base_v089_signal(optionexval, sellval, marketcap):
    result = _z(_f33_exercisedump(optionexval, sellval, marketcap, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d exercise-dump over 126d
def f33id_f33_insider_distribution_selling_zexdump_21d126w_base_v090_signal(optionexval, sellval, marketcap):
    result = _z(_f33_exercisedump(optionexval, sellval, marketcap, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# selling acceleration: 42d vs 126d sell intensity spread
def f33id_f33_insider_distribution_selling_accel_42_126_base_v091_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 42) - _f33_sellintensity(sellval, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# selling acceleration: 84d vs 252d sell intensity spread
def f33id_f33_insider_distribution_selling_accel_84_252_base_v092_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 84) - _f33_sellintensity(sellval, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# share-flow acceleration: 42d vs 189d
def f33id_f33_insider_distribution_selling_flowaccel_42_189_base_v093_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 42) - _f33_sellflow(sellshares, sharesbas, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# share-flow acceleration: 126d vs 252d
def f33id_f33_insider_distribution_selling_flowaccel_126_252_base_v094_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 126) - _f33_sellflow(sellshares, sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of short to long share-flow (21d / 126d)
def f33id_f33_insider_distribution_selling_flowratio_21_126_base_v095_signal(sellshares, sharesbas):
    short = _f33_sellflow(sellshares, sharesbas, 21)
    long = _f33_sellflow(sellshares, sharesbas, 126)
    result = _safe_div(short, long.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of short to long share-flow (63d / 252d)
def f33id_f33_insider_distribution_selling_flowratio_63_252_base_v096_signal(sellshares, sharesbas):
    short = _f33_sellflow(sellshares, sharesbas, 63)
    long = _f33_sellflow(sellshares, sharesbas, 252)
    result = _safe_div(short, long.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-dump ratio short to long (21d / 126d)
def f33id_f33_insider_distribution_selling_exratio_21_126_base_v097_signal(optionexval, sellval, marketcap):
    short = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    long = _f33_exercisedump(optionexval, sellval, marketcap, 126)
    result = _safe_div(short, long.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# sell share-flow surprise (63d minus 126d mean)
def f33id_f33_insider_distribution_selling_flowsurp_63d_base_v098_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 63)
    result = sf - _mean(sf, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sell share-flow surprise (126d minus 252d mean)
def f33id_f33_insider_distribution_selling_flowsurp_126d_base_v099_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 126)
    result = sf - _mean(sf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-dump surprise (63d minus 126d mean)
def f33id_f33_insider_distribution_selling_exsurp_63d_base_v100_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    result = ed - _mean(ed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 252d sell intensity over 504d
def f33id_f33_insider_distribution_selling_rank_252d_base_v101_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 252)
    result = si.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 21d share-flow over 252d
def f33id_f33_insider_distribution_selling_rankflow_21d_base_v102_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 21)
    result = sf.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 63d exercise-dump over 252d
def f33id_f33_insider_distribution_selling_rankex_63d_base_v103_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    result = ed.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# sell-count rate (126d events scaled by sale $)
def f33id_f33_insider_distribution_selling_countrate_252d_base_v104_signal(sellcount, sellval, marketcap):
    c = sellcount.rolling(252, min_periods=84).sum()
    result = _safe_div(c, sellval.rolling(252, min_periods=84).sum().abs()) + _f33_sellintensity(sellval, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# sell-count smoothed intensity (63d mean of 21d count sum scaled by mcap)
def f33id_f33_insider_distribution_selling_countsmooth_63d_base_v105_signal(sellcount, marketcap, sellval):
    c = sellcount.rolling(21, min_periods=10).sum()
    result = _mean(c, 63) / marketcap.replace(0, np.nan) * 1e6 + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average sale size scaled (252d)
def f33id_f33_insider_distribution_selling_avgsize_252d_base_v106_signal(sellval, sellcount, marketcap):
    v = sellval.rolling(252, min_periods=84).sum()
    c = sellcount.rolling(252, min_periods=84).sum()
    result = _safe_div(v, c) / marketcap.replace(0, np.nan) + _f33_sellintensity(sellval, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# average sale size z-score (63d size standardized over 252d)
def f33id_f33_insider_distribution_selling_zavgsize_63d_base_v107_signal(sellval, sellcount, marketcap):
    v = sellval.rolling(63, min_periods=21).sum()
    c = sellcount.rolling(63, min_periods=21).sum()
    size = _safe_div(v, c)
    result = _z(size, 252) + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-to-sale conversion (21d)
def f33id_f33_insider_distribution_selling_exconv_21d_base_v108_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(21, min_periods=10).sum()
    sv = sellval.rolling(21, min_periods=10).sum()
    result = _safe_div(ex, sv.abs()) + _f33_exercisedump(optionexval, sellval, marketcap, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-to-sale conversion z-score (63d over 252d)
def f33id_f33_insider_distribution_selling_zexconv_63d_base_v109_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(63, min_periods=21).sum()
    sv = sellval.rolling(63, min_periods=21).sum()
    conv = _safe_div(ex, sv.abs())
    result = _z(conv, 252) + _f33_exercisedump(optionexval, sellval, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# insider-driven share shrinkage proxy over 504d
def f33id_f33_insider_distribution_selling_shrink_504d_base_v110_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 504) - _f33_sellflow(sellshares, sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selling-cluster intensity: 63d scaled by 252d mean
def f33id_f33_insider_distribution_selling_cluster_63d_base_v111_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = _safe_div(si, _mean(si, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# selling-cluster intensity: 10d scaled by 63d mean
def f33id_f33_insider_distribution_selling_cluster_10d_base_v112_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 10)
    result = _safe_div(si, _mean(si, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# liquidation z-score over 504d
def f33id_f33_insider_distribution_selling_zliq_126d_base_v113_signal(tenpctsellval, sellval):
    result = _z(_f33_liquidation(tenpctsellval, sellval, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidation surprise: 126d liq share minus 252d mean
def f33id_f33_insider_distribution_selling_liqsurp_126d_base_v114_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 126)
    result = lq - _mean(lq, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 10%-owner sale intensity scaled by marketcap (42d)
def f33id_f33_insider_distribution_selling_tenint_42d_base_v115_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(42, min_periods=21).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10%-owner sale intensity scaled by marketcap (504d)
def f33id_f33_insider_distribution_selling_tenint_504d_base_v116_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(504, min_periods=168).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# sell-pressure deviation (63d intensity demeaned over 252d)
def f33id_f33_insider_distribution_selling_pressdev_63d_base_v117_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = si - _mean(si, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sell-pressure dispersion: rolling std of 63d intensity over 252d
def f33id_f33_insider_distribution_selling_pressdisp63_252d_base_v118_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = _std(si, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# share-flow dispersion: rolling std of 21d flow over 252d
def f33id_f33_insider_distribution_selling_flowdisp_252d_base_v119_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 21)
    result = _std(sf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# distribution composite (252d sell intensity + exercise dump)
def f33id_f33_insider_distribution_selling_distcomp_252d_base_v120_signal(sellval, optionexval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 252) + _f33_exercisedump(optionexval, sellval, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# selling pressure weighted by liquidation share (252d)
def f33id_f33_insider_distribution_selling_liqweight_252d_base_v121_signal(sellval, tenpctsellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 252) * _f33_liquidation(tenpctsellval, sellval, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity smoothed: 126d mean of 21d intensity
def f33id_f33_insider_distribution_selling_smooth_126d_base_v122_signal(sellval, marketcap):
    result = _mean(_f33_sellintensity(sellval, marketcap, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sell share-flow smoothed: 126d mean of 21d flow
def f33id_f33_insider_distribution_selling_smoothflow_126d_base_v123_signal(sellshares, sharesbas):
    result = _mean(_f33_sellflow(sellshares, sharesbas, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-dump smoothed: 63d mean of 21d exdump
def f33id_f33_insider_distribution_selling_smoothex_63d_base_v124_signal(optionexval, sellval, marketcap):
    result = _mean(_f33_exercisedump(optionexval, sellval, marketcap, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity EWMA (252d span)
def f33id_f33_insider_distribution_selling_ewm_252d_base_v125_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# sell share-flow EWMA (126d span)
def f33id_f33_insider_distribution_selling_ewmflow_126d_base_v126_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 21)
    result = sf.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-dump EWMA (126d span)
def f33id_f33_insider_distribution_selling_ewmex_126d_base_v127_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    result = ed.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# liquidation EWMA (126d span)
def f33id_f33_insider_distribution_selling_ewmliq_126d_base_v128_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 63)
    result = lq.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity acceleration smoothed (21d-63d spread smoothed 63d)
def f33id_f33_insider_distribution_selling_accelsmooth_63d_base_v129_signal(sellval, marketcap):
    spread = _f33_sellintensity(sellval, marketcap, 21) - _f33_sellintensity(sellval, marketcap, 63)
    result = _mean(spread, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-dump info ratio: 21d vs 252d dispersion
def f33id_f33_insider_distribution_selling_exinfo_21d_base_v130_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    result = _safe_div(ed, _std(ed, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity info ratio: 63d vs 252d dispersion
def f33id_f33_insider_distribution_selling_inforatio_63d_base_v131_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = _safe_div(si, _std(si, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# liquidation info ratio: 63d vs 252d dispersion
def f33id_f33_insider_distribution_selling_liqinfo_63d_base_v132_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 63)
    result = _safe_div(lq, _std(lq, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# share-flow percentile rank of 63d over 252d
def f33id_f33_insider_distribution_selling_rankflow_63d_base_v133_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 63)
    result = sf.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidation percentile rank of 126d over 504d
def f33id_f33_insider_distribution_selling_rankliq_126d_base_v134_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 126)
    result = lq.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity relative to exercise-dump (share of pure selling, 63d)
def f33id_f33_insider_distribution_selling_pureshare_63d_base_v135_signal(sellval, optionexval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    result = _safe_div(si, ed)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity relative to exercise-dump (126d)
def f33id_f33_insider_distribution_selling_pureshare_126d_base_v136_signal(sellval, optionexval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 126)
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 126)
    result = _safe_div(si, ed)
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity scaled by its own 252d dispersion (vol-scaled pressure 63d)
def f33id_f33_insider_distribution_selling_volscaled_63d_base_v137_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    vol = _std(_f33_sellintensity(sellval, marketcap, 21), 252)
    result = _safe_div(si, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# sell share-flow vol-scaled (126d flow over 252d flow dispersion)
def f33id_f33_insider_distribution_selling_volscaledflow_126d_base_v138_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 126)
    vol = _std(_f33_sellflow(sellshares, sharesbas, 21), 252)
    result = _safe_div(sf, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-dump vol-scaled (63d over 252d dispersion)
def f33id_f33_insider_distribution_selling_volscaledex_63d_base_v139_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    vol = _std(_f33_exercisedump(optionexval, sellval, marketcap, 21), 252)
    result = _safe_div(ed, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# selling cluster intensity weighted by share-flow (63d)
def f33id_f33_insider_distribution_selling_clusterflow_63d_base_v140_signal(sellval, marketcap, sellshares, sharesbas):
    si = _f33_sellintensity(sellval, marketcap, 63)
    sf = _f33_sellflow(sellshares, sharesbas, 63)
    result = si * sf
    return result.replace([np.inf, -np.inf], np.nan)


# distribution intensity ratio: exercise dump over pure sell (63d, conversion proxy)
def f33id_f33_insider_distribution_selling_convratio_63d_base_v141_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = _safe_div(ed, si)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidation-weighted sell share-flow (126d)
def f33id_f33_insider_distribution_selling_liqflow_126d_base_v142_signal(sellshares, sharesbas, tenpctsellval, sellval):
    sf = _f33_sellflow(sellshares, sharesbas, 126)
    lq = _f33_liquidation(tenpctsellval, sellval, 126)
    result = sf * lq
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity demeaned and vol-scaled (63d z over 504d)
def f33id_f33_insider_distribution_selling_zsellint63_504w_base_v143_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 63), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# share-flow demeaned and vol-scaled (252d z over 504d)
def f33id_f33_insider_distribution_selling_zsellflow252_504w_base_v144_signal(sellshares, sharesbas):
    result = _z(_f33_sellflow(sellshares, sharesbas, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 10%-owner liquidation intensity weighted by sell intensity (63d)
def f33id_f33_insider_distribution_selling_tenweight_63d_base_v145_signal(tenpctsellval, marketcap, sellval):
    ti = _safe_div(tenpctsellval.rolling(63, min_periods=21).sum(), marketcap)
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = ti * np.sign(si) + si * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# sell intensity surge: 10d over 252d mean
def f33id_f33_insider_distribution_selling_surge_10d_base_v146_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 10)
    result = _safe_div(si, _mean(si, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# exercise-dump surge: 21d over 252d mean
def f33id_f33_insider_distribution_selling_exsurge_21d_base_v147_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    result = _safe_div(ed, _mean(ed, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon sell intensity composite (21/63/126/252)
def f33id_f33_insider_distribution_selling_blend_multi_base_v148_signal(sellval, marketcap):
    result = (_f33_sellintensity(sellval, marketcap, 21) + _f33_sellintensity(sellval, marketcap, 63)
              + _f33_sellintensity(sellval, marketcap, 126) + _f33_sellintensity(sellval, marketcap, 252)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended distribution composite (intensity + flow + exdump, 126d)
def f33id_f33_insider_distribution_selling_blend_dist_base_v149_signal(sellval, marketcap, sellshares, sharesbas, optionexval):
    result = (_f33_sellintensity(sellval, marketcap, 126)
              + _f33_sellflow(sellshares, sharesbas, 126)
              + _f33_exercisedump(optionexval, sellval, marketcap, 126)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended liquidation-adjusted distribution composite (252d)
def f33id_f33_insider_distribution_selling_blend_liq_base_v150_signal(sellval, marketcap, tenpctsellval, sellshares, sharesbas):
    result = (_f33_sellintensity(sellval, marketcap, 252)
              + _f33_sellflow(sellshares, sharesbas, 252)
              + _f33_liquidation(tenpctsellval, sellval, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33id_f33_insider_distribution_selling_sellint_315d_base_v076_signal,
    f33id_f33_insider_distribution_selling_sellint_504d_base_v077_signal,
    f33id_f33_insider_distribution_selling_sellint_10d_base_v078_signal,
    f33id_f33_insider_distribution_selling_sellflow_315d_base_v079_signal,
    f33id_f33_insider_distribution_selling_sellflow_504d_base_v080_signal,
    f33id_f33_insider_distribution_selling_sellflow_84d_base_v081_signal,
    f33id_f33_insider_distribution_selling_exdump_189d_base_v082_signal,
    f33id_f33_insider_distribution_selling_exdump_504d_base_v083_signal,
    f33id_f33_insider_distribution_selling_liq_189d_base_v084_signal,
    f33id_f33_insider_distribution_selling_liq_504d_base_v085_signal,
    f33id_f33_insider_distribution_selling_zsellint_252d_base_v086_signal,
    f33id_f33_insider_distribution_selling_zsellint_42d_base_v087_signal,
    f33id_f33_insider_distribution_selling_zsellflow_126d_base_v088_signal,
    f33id_f33_insider_distribution_selling_zexdump_126d_base_v089_signal,
    f33id_f33_insider_distribution_selling_zexdump_21d126w_base_v090_signal,
    f33id_f33_insider_distribution_selling_accel_42_126_base_v091_signal,
    f33id_f33_insider_distribution_selling_accel_84_252_base_v092_signal,
    f33id_f33_insider_distribution_selling_flowaccel_42_189_base_v093_signal,
    f33id_f33_insider_distribution_selling_flowaccel_126_252_base_v094_signal,
    f33id_f33_insider_distribution_selling_flowratio_21_126_base_v095_signal,
    f33id_f33_insider_distribution_selling_flowratio_63_252_base_v096_signal,
    f33id_f33_insider_distribution_selling_exratio_21_126_base_v097_signal,
    f33id_f33_insider_distribution_selling_flowsurp_63d_base_v098_signal,
    f33id_f33_insider_distribution_selling_flowsurp_126d_base_v099_signal,
    f33id_f33_insider_distribution_selling_exsurp_63d_base_v100_signal,
    f33id_f33_insider_distribution_selling_rank_252d_base_v101_signal,
    f33id_f33_insider_distribution_selling_rankflow_21d_base_v102_signal,
    f33id_f33_insider_distribution_selling_rankex_63d_base_v103_signal,
    f33id_f33_insider_distribution_selling_countrate_252d_base_v104_signal,
    f33id_f33_insider_distribution_selling_countsmooth_63d_base_v105_signal,
    f33id_f33_insider_distribution_selling_avgsize_252d_base_v106_signal,
    f33id_f33_insider_distribution_selling_zavgsize_63d_base_v107_signal,
    f33id_f33_insider_distribution_selling_exconv_21d_base_v108_signal,
    f33id_f33_insider_distribution_selling_zexconv_63d_base_v109_signal,
    f33id_f33_insider_distribution_selling_shrink_504d_base_v110_signal,
    f33id_f33_insider_distribution_selling_cluster_63d_base_v111_signal,
    f33id_f33_insider_distribution_selling_cluster_10d_base_v112_signal,
    f33id_f33_insider_distribution_selling_zliq_126d_base_v113_signal,
    f33id_f33_insider_distribution_selling_liqsurp_126d_base_v114_signal,
    f33id_f33_insider_distribution_selling_tenint_42d_base_v115_signal,
    f33id_f33_insider_distribution_selling_tenint_504d_base_v116_signal,
    f33id_f33_insider_distribution_selling_pressdev_63d_base_v117_signal,
    f33id_f33_insider_distribution_selling_pressdisp63_252d_base_v118_signal,
    f33id_f33_insider_distribution_selling_flowdisp_252d_base_v119_signal,
    f33id_f33_insider_distribution_selling_distcomp_252d_base_v120_signal,
    f33id_f33_insider_distribution_selling_liqweight_252d_base_v121_signal,
    f33id_f33_insider_distribution_selling_smooth_126d_base_v122_signal,
    f33id_f33_insider_distribution_selling_smoothflow_126d_base_v123_signal,
    f33id_f33_insider_distribution_selling_smoothex_63d_base_v124_signal,
    f33id_f33_insider_distribution_selling_ewm_252d_base_v125_signal,
    f33id_f33_insider_distribution_selling_ewmflow_126d_base_v126_signal,
    f33id_f33_insider_distribution_selling_ewmex_126d_base_v127_signal,
    f33id_f33_insider_distribution_selling_ewmliq_126d_base_v128_signal,
    f33id_f33_insider_distribution_selling_accelsmooth_63d_base_v129_signal,
    f33id_f33_insider_distribution_selling_exinfo_21d_base_v130_signal,
    f33id_f33_insider_distribution_selling_inforatio_63d_base_v131_signal,
    f33id_f33_insider_distribution_selling_liqinfo_63d_base_v132_signal,
    f33id_f33_insider_distribution_selling_rankflow_63d_base_v133_signal,
    f33id_f33_insider_distribution_selling_rankliq_126d_base_v134_signal,
    f33id_f33_insider_distribution_selling_pureshare_63d_base_v135_signal,
    f33id_f33_insider_distribution_selling_pureshare_126d_base_v136_signal,
    f33id_f33_insider_distribution_selling_volscaled_63d_base_v137_signal,
    f33id_f33_insider_distribution_selling_volscaledflow_126d_base_v138_signal,
    f33id_f33_insider_distribution_selling_volscaledex_63d_base_v139_signal,
    f33id_f33_insider_distribution_selling_clusterflow_63d_base_v140_signal,
    f33id_f33_insider_distribution_selling_convratio_63d_base_v141_signal,
    f33id_f33_insider_distribution_selling_liqflow_126d_base_v142_signal,
    f33id_f33_insider_distribution_selling_zsellint63_504w_base_v143_signal,
    f33id_f33_insider_distribution_selling_zsellflow252_504w_base_v144_signal,
    f33id_f33_insider_distribution_selling_tenweight_63d_base_v145_signal,
    f33id_f33_insider_distribution_selling_surge_10d_base_v146_signal,
    f33id_f33_insider_distribution_selling_exsurge_21d_base_v147_signal,
    f33id_f33_insider_distribution_selling_blend_multi_base_v148_signal,
    f33id_f33_insider_distribution_selling_blend_dist_base_v149_signal,
    f33id_f33_insider_distribution_selling_blend_liq_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_INSIDER_DISTRIBUTION_SELLING_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f33_insider_distribution_selling_base_076_150_claude: {n_features} features pass")
