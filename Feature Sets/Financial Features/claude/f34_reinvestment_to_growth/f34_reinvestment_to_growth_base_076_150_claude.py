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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _qrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====

def _f34_retained_growth(retearn, w):
    return retearn.pct_change(periods=w)


def _f34_reinvestment_intensity(retearn, equity):
    return retearn / equity.replace(0, np.nan).abs()


def _f34_reinvestment_quality(retearn, equity, w):
    intens = retearn / equity.replace(0, np.nan).abs()
    return intens.pct_change(periods=w)


# ===== features =====
def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_21d_base_v076_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 21)
    result = _qrank(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_42d_base_v077_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 42)
    result = _qrank(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_63d_base_v078_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 63)
    result = _qrank(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_126d_base_v079_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 126)
    result = _qrank(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_189d_base_v080_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 189)
    result = _qrank(g, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_252d_base_v081_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 252)
    result = _qrank(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_378d_base_v082_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 378)
    result = _qrank(g, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_504d_base_v083_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 504)
    result = _qrank(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_10d_base_v084_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 10)
    result = _qrank(g, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthqrank_5d_base_v085_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 5)
    result = _qrank(g, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensstd_21d_base_v086_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensstd_42d_base_v087_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensstd_63d_base_v088_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensstd_126d_base_v089_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensstd_189d_base_v090_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensstd_252d_base_v091_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensstd_378d_base_v092_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensstd_504d_base_v093_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualqrank_21d_base_v094_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 21)
    result = _qrank(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualqrank_42d_base_v095_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 42)
    result = _qrank(q, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualqrank_63d_base_v096_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 63)
    result = _qrank(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualqrank_126d_base_v097_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 126)
    result = _qrank(q, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualqrank_189d_base_v098_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 189)
    result = _qrank(q, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualqrank_252d_base_v099_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 252)
    result = _qrank(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualqrank_378d_base_v100_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 378)
    result = _qrank(q, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualqrank_504d_base_v101_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 504)
    result = _qrank(q, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthstd_21d_base_v102_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 21)
    result = _std(g, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthstd_63d_base_v103_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 63)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthstd_126d_base_v104_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 126)
    result = _std(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthstd_252d_base_v105_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 252)
    result = _std(g, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthstd_504d_base_v106_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 504)
    result = _std(g, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthstd_42d_base_v107_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 42)
    result = _std(g, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensxc_21d_base_v108_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 21) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensxc_63d_base_v109_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 63) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensxc_126d_base_v110_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 126) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensxc_252d_base_v111_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 252) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvintensxc_504d_base_v112_signal(retearn, equity, closeadj):
    base = _f34_reinvestment_intensity(retearn, equity)
    result = _mean(base, 504) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthdiff_21d_base_v113_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 21)
    result = (g - g.shift(7)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthdiff_63d_base_v114_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 63)
    result = (g - g.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthdiff_126d_base_v115_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 126)
    result = (g - g.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthdiff_252d_base_v116_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 252)
    result = (g - g.shift(84)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthdiff_504d_base_v117_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 504)
    result = (g - g.shift(168)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualdiff_21d_base_v118_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 21)
    result = (q - q.shift(7)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualdiff_63d_base_v119_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 63)
    result = (q - q.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualdiff_126d_base_v120_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 126)
    result = (q - q.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualdiff_252d_base_v121_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 252)
    result = (q - q.shift(84)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualdiff_504d_base_v122_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 504)
    result = (q - q.shift(168)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxcg_21d_base_v123_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 21)
    cg = closeadj.pct_change(periods=7)
    result = g * cg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxcg_42d_base_v124_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 42)
    cg = closeadj.pct_change(periods=14)
    result = g * cg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxcg_63d_base_v125_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 63)
    cg = closeadj.pct_change(periods=21)
    result = g * cg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxcg_126d_base_v126_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 126)
    cg = closeadj.pct_change(periods=42)
    result = g * cg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxcg_252d_base_v127_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 252)
    cg = closeadj.pct_change(periods=84)
    result = g * cg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthxcg_504d_base_v128_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 504)
    cg = closeadj.pct_change(periods=168)
    result = g * cg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvxretg_21d_base_v129_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 21)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _ema(ri, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvxretg_42d_base_v130_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 42)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _ema(ri, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvxretg_63d_base_v131_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 63)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _ema(ri, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvxretg_126d_base_v132_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 126)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _ema(ri, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvxretg_252d_base_v133_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 252)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _ema(ri, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvxretg_504d_base_v134_signal(retearn, equity, closeadj):
    g = _f34_retained_growth(retearn, 504)
    ri = _f34_reinvestment_intensity(retearn, equity)
    result = g * _ema(ri, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthmean_21d_base_v135_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 21)
    result = _mean(g, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthmean_42d_base_v136_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 42)
    result = _mean(g, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthmean_63d_base_v137_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 63)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthmean_126d_base_v138_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 126)
    result = _mean(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthmean_189d_base_v139_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 189)
    result = _mean(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthmean_252d_base_v140_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 252)
    result = _mean(g, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthmean_378d_base_v141_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 378)
    result = _mean(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_retgrowthmean_504d_base_v142_signal(retearn, closeadj):
    g = _f34_retained_growth(retearn, 504)
    result = _mean(g, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema2_21d_base_v143_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 21)
    result = _ema(q, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema2_42d_base_v144_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 42)
    result = _ema(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema2_63d_base_v145_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 63)
    result = _ema(q, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema2_126d_base_v146_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 126)
    result = _ema(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema2_189d_base_v147_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 189)
    result = _ema(q, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema2_252d_base_v148_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 252)
    result = _ema(q, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema2_378d_base_v149_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 378)
    result = _ema(q, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rtg_f34_reinvestment_to_growth_reinvqualema2_504d_base_v150_signal(retearn, equity, closeadj):
    q = _f34_reinvestment_quality(retearn, equity, 504)
    result = _ema(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_21d_base_v076_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_42d_base_v077_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_63d_base_v078_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_126d_base_v079_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_189d_base_v080_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_252d_base_v081_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_378d_base_v082_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_504d_base_v083_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_10d_base_v084_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthqrank_5d_base_v085_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensstd_21d_base_v086_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensstd_42d_base_v087_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensstd_63d_base_v088_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensstd_126d_base_v089_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensstd_189d_base_v090_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensstd_252d_base_v091_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensstd_378d_base_v092_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensstd_504d_base_v093_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualqrank_21d_base_v094_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualqrank_42d_base_v095_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualqrank_63d_base_v096_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualqrank_126d_base_v097_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualqrank_189d_base_v098_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualqrank_252d_base_v099_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualqrank_378d_base_v100_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualqrank_504d_base_v101_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthstd_21d_base_v102_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthstd_63d_base_v103_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthstd_126d_base_v104_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthstd_252d_base_v105_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthstd_504d_base_v106_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthstd_42d_base_v107_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensxc_21d_base_v108_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensxc_63d_base_v109_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensxc_126d_base_v110_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensxc_252d_base_v111_signal,
    f34rtg_f34_reinvestment_to_growth_reinvintensxc_504d_base_v112_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthdiff_21d_base_v113_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthdiff_63d_base_v114_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthdiff_126d_base_v115_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthdiff_252d_base_v116_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthdiff_504d_base_v117_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualdiff_21d_base_v118_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualdiff_63d_base_v119_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualdiff_126d_base_v120_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualdiff_252d_base_v121_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualdiff_504d_base_v122_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxcg_21d_base_v123_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxcg_42d_base_v124_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxcg_63d_base_v125_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxcg_126d_base_v126_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxcg_252d_base_v127_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthxcg_504d_base_v128_signal,
    f34rtg_f34_reinvestment_to_growth_reinvxretg_21d_base_v129_signal,
    f34rtg_f34_reinvestment_to_growth_reinvxretg_42d_base_v130_signal,
    f34rtg_f34_reinvestment_to_growth_reinvxretg_63d_base_v131_signal,
    f34rtg_f34_reinvestment_to_growth_reinvxretg_126d_base_v132_signal,
    f34rtg_f34_reinvestment_to_growth_reinvxretg_252d_base_v133_signal,
    f34rtg_f34_reinvestment_to_growth_reinvxretg_504d_base_v134_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthmean_21d_base_v135_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthmean_42d_base_v136_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthmean_63d_base_v137_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthmean_126d_base_v138_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthmean_189d_base_v139_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthmean_252d_base_v140_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthmean_378d_base_v141_signal,
    f34rtg_f34_reinvestment_to_growth_retgrowthmean_504d_base_v142_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema2_21d_base_v143_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema2_42d_base_v144_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema2_63d_base_v145_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema2_126d_base_v146_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema2_189d_base_v147_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema2_252d_base_v148_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema2_378d_base_v149_signal,
    f34rtg_f34_reinvestment_to_growth_reinvqualema2_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_REINVESTMENT_TO_GROWTH_REGISTRY_076_150 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f34_retained_growth", "_f34_reinvestment_intensity", "_f34_reinvestment_quality",)
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
    print(f"OK f34_reinvestment_to_growth_base_076_150_claude: {n_features} features pass")
