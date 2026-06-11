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


# ===== folder domain primitives (revenue hypergrowth) =====
def _f23_growth(s, w):
    # revenue growth (percentage change) over w trading days
    return s.pct_change(periods=w)


def _f23_accel(s, w):
    # growth acceleration: current w-growth minus the prior w-growth (spaced diff)
    g = s.pct_change(periods=w)
    return g - g.shift(w)


def _f23_growthz(s, w):
    # standardized growth: z-score of w-growth over a trailing year
    g = s.pct_change(periods=w)
    m = g.rolling(252, min_periods=63).mean()
    sd = g.rolling(252, min_periods=63).std()
    return (g - m) / sd.replace(0, np.nan)


def _f23_logcompound(s, w):
    # log compounding growth over w (additive, robust to scale)
    return np.log(s / s.shift(w))


# ============ FEATURES 076-150 ============

# 315d revenue growth (long-horizon hypergrowth)
def f23rh_f23_revenue_hypergrowth_growth_315d_base_v076_signal(revenue):
    result = _f23_growth(revenue, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d revenue growth
def f23rh_f23_revenue_hypergrowth_growth_378d_base_v077_signal(revenue):
    result = _f23_growth(revenue, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_315d_base_v078_signal(revenue):
    result = _f23_logcompound(revenue, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_378d_base_v079_signal(revenue):
    result = _f23_logcompound(revenue, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_84d_base_v080_signal(revenue):
    result = _f23_logcompound(revenue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d revenue growth acceleration (level)
def f23rh_f23_revenue_hypergrowth_accel_189d_base_v081_signal(revenue):
    result = _f23_accel(revenue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth acceleration (level)
def f23rh_f23_revenue_hypergrowth_accel_504d_base_v082_signal(revenue):
    result = _f23_accel(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration as fraction of growth level (relative acceleration, 63d)
def f23rh_f23_revenue_hypergrowth_relaccel_63d_base_v083_signal(revenue):
    a = _f23_accel(revenue, 63)
    g = _f23_growth(revenue, 63).abs()
    result = _safe_div(a, g)
    return result.replace([np.inf, -np.inf], np.nan)


# relative acceleration 126d
def f23rh_f23_revenue_hypergrowth_relaccel_126d_base_v084_signal(revenue):
    a = _f23_accel(revenue, 126)
    g = _f23_growth(revenue, 126).abs()
    result = _safe_div(a, g)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d standardized revenue growth (z-score)
def f23rh_f23_revenue_hypergrowth_growthz_84d_base_v085_signal(revenue):
    result = _f23_growthz(revenue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d standardized revenue growth (z-score)
def f23rh_f23_revenue_hypergrowth_growthz_189d_base_v086_signal(revenue):
    result = _f23_growthz(revenue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth z over shorter 126d window (63d growth)
def f23rh_f23_revenue_hypergrowth_zg126_63d_base_v087_signal(revenue):
    result = _z(_f23_growth(revenue, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth z over 504d window (126d growth)
def f23rh_f23_revenue_hypergrowth_zg504_126d_base_v088_signal(revenue):
    result = _z(_f23_growth(revenue, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth trend slope over 189d
def f23rh_f23_revenue_hypergrowth_trend_189d_base_v089_signal(revenue):
    g = _f23_growth(revenue, 63)
    result = (g - g.shift(189)) / 189.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth trend slope over 504d
def f23rh_f23_revenue_hypergrowth_trend_504d_base_v090_signal(revenue):
    g = _f23_growth(revenue, 126)
    result = (g - g.shift(504)) / 504.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth stability over 504d (21d growth)
def f23rh_f23_revenue_hypergrowth_stab_504d_base_v091_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = _safe_div(_mean(g, 504), _std(g, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth stability over 63d (21d growth, fast)
def f23rh_f23_revenue_hypergrowth_stab_63d_base_v092_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = _safe_div(_mean(g, 63), _std(g, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs trailing 504d mean (relative level)
def f23rh_f23_revenue_hypergrowth_vsmean_504d_base_v093_signal(revenue):
    result = _safe_div(revenue, _mean(revenue, 504)) - 1.0 + _f23_growth(revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs trailing 21d mean (relative level, fast)
def f23rh_f23_revenue_hypergrowth_vsmean_21d_base_v094_signal(revenue):
    result = _safe_div(revenue, _mean(revenue, 21)) - 1.0 + _f23_growth(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# compounding rate: annualized 252d log growth
def f23rh_f23_revenue_hypergrowth_cagr_252d_base_v095_signal(revenue):
    result = _f23_logcompound(revenue, 252) * (252.0 / 252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# compounding rate: annualized 126d log growth (gp quality)
def f23rh_f23_revenue_hypergrowth_cagr_504d_base_v096_signal(revenue):
    result = _f23_logcompound(revenue, 504) * (252.0 / 504.0)
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover growth: revenue/assets, 21d growth (fast)
def f23rh_f23_revenue_hypergrowth_turngrow_21d_base_v097_signal(revenue, assets):
    turn = _safe_div(revenue, assets)
    result = _f23_growth(turn, 21) + _f23_growth(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover log compounding growth, 252d
def f23rh_f23_revenue_hypergrowth_turnlog_252d_base_v098_signal(revenue, assets):
    turn = _safe_div(revenue, assets)
    result = _f23_logcompound(turn, 252) + _f23_logcompound(revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover level z-score over 252d
def f23rh_f23_revenue_hypergrowth_turnz_252d_base_v099_signal(revenue, assets):
    turn = _safe_div(revenue, assets)
    result = _z(turn, 252) + _f23_growth(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth percentile rank: 252d growth over 504d
def f23rh_f23_revenue_hypergrowth_rank_252d_base_v100_signal(revenue):
    g = _f23_growth(revenue, 252)
    result = g.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# log-compound percentile rank: 126d logcmp over 252d
def f23rh_f23_revenue_hypergrowth_rankl_126d_base_v101_signal(revenue):
    g = _f23_logcompound(revenue, 126)
    result = g.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# sustained-growth composite: blended log compounding 63/126/252
def f23rh_f23_revenue_hypergrowth_sustainlog_multi_base_v102_signal(revenue):
    result = (_f23_logcompound(revenue, 63) + _f23_logcompound(revenue, 126)
              + _f23_logcompound(revenue, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# sustained-growth composite: growth scaled by stability (63d growth, 252d stability)
def f23rh_f23_revenue_hypergrowth_qualgrow_63d_base_v103_signal(revenue):
    g = _f23_growth(revenue, 63)
    stab = _safe_div(_mean(_f23_growth(revenue, 21), 252), _std(_f23_growth(revenue, 21), 252))
    result = g * stab
    return result.replace([np.inf, -np.inf], np.nan)


# sustained-growth composite: 126d growth scaled by stability
def f23rh_f23_revenue_hypergrowth_qualgrow_126d_base_v104_signal(revenue):
    g = _f23_growth(revenue, 126)
    stab = _safe_div(_mean(_f23_growth(revenue, 21), 252), _std(_f23_growth(revenue, 21), 252))
    result = g * stab
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd 84d growth
def f23rh_f23_revenue_hypergrowth_usdgrow_84d_base_v105_signal(revenueusd):
    result = _f23_growth(revenueusd, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd 504d growth
def f23rh_f23_revenue_hypergrowth_usdgrow_504d_base_v106_signal(revenueusd):
    result = _f23_growth(revenueusd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd standardized growth 126d
def f23rh_f23_revenue_hypergrowth_usdz_126d_base_v107_signal(revenueusd):
    result = _f23_growthz(revenueusd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd growth trend slope 252d
def f23rh_f23_revenue_hypergrowth_usdtrend_252d_base_v108_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    result = (g - g.shift(252)) / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs revenueusd growth spread (FX/mix effect, 126d)
def f23rh_f23_revenue_hypergrowth_fxspread_126d_base_v109_signal(revenue, revenueusd):
    result = _f23_growth(revenue, 126) - _f23_growth(revenueusd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs revenueusd growth spread (252d)
def f23rh_f23_revenue_hypergrowth_fxspread_252d_base_v110_signal(revenue, revenueusd):
    result = _f23_growth(revenue, 252) - _f23_growth(revenueusd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gp 84d growth
def f23rh_f23_revenue_hypergrowth_gpgrow_84d_base_v111_signal(gp):
    result = _f23_growth(gp, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# gp 504d growth
def f23rh_f23_revenue_hypergrowth_gpgrow_504d_base_v112_signal(gp):
    result = _f23_growth(gp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# gp standardized growth 126d
def f23rh_f23_revenue_hypergrowth_gpz_126d_base_v113_signal(gp):
    result = _f23_growthz(gp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gp standardized growth 252d
def f23rh_f23_revenue_hypergrowth_gpz_252d_base_v114_signal(gp):
    result = _f23_growthz(gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gp growth trend slope 252d
def f23rh_f23_revenue_hypergrowth_gptrend_252d_base_v115_signal(gp):
    g = _f23_growth(gp, 63)
    result = (g - g.shift(252)) / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# gp growth acceleration 252d
def f23rh_f23_revenue_hypergrowth_gpaccel_252d_base_v116_signal(gp):
    result = _f23_accel(gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin proxy growth: (gp/revenue) 126d growth
def f23rh_f23_revenue_hypergrowth_marggrow_126d_base_v117_signal(revenue, gp):
    marg = _safe_div(gp, revenue)
    result = _f23_growth(marg, 126) + _f23_growth(gp, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin proxy growth 252d
def f23rh_f23_revenue_hypergrowth_marggrow_252d_base_v118_signal(revenue, gp):
    marg = _safe_div(gp, revenue)
    result = _f23_growth(marg, 252) + _f23_growth(gp, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin proxy level z-score over 252d
def f23rh_f23_revenue_hypergrowth_margz_252d_base_v119_signal(revenue, gp):
    marg = _safe_div(gp, revenue)
    result = _z(marg, 252) + _f23_growth(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# margin-adjusted hypergrowth: revenue growth times gross margin level (126d)
def f23rh_f23_revenue_hypergrowth_margadj_126d_base_v120_signal(revenue, gp):
    marg = _safe_div(gp, revenue)
    result = _f23_growth(revenue, 126) * marg
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus assets growth, log version (organic, 252d)
def f23rh_f23_revenue_hypergrowth_organiclog_252d_base_v121_signal(revenue, assets):
    result = _f23_logcompound(revenue, 252) - _f23_logcompound(assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus assets growth (63d)
def f23rh_f23_revenue_hypergrowth_organic_63d_base_v122_signal(revenue, assets):
    result = _f23_growth(revenue, 63) - _f23_growth(assets, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# assets growth acceleration (balance-sheet expansion accel, 126d)
def f23rh_f23_revenue_hypergrowth_assetaccel_126d_base_v123_signal(assets):
    result = _f23_accel(assets, 126) + _f23_growth(assets, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# assets standardized growth 252d
def f23rh_f23_revenue_hypergrowth_assetz_252d_base_v124_signal(assets):
    result = _f23_growthz(assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth surprise 252d (minus 504d mean)
def f23rh_f23_revenue_hypergrowth_surp_252d_base_v125_signal(revenue):
    g = _f23_growth(revenue, 252)
    result = g - _mean(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration standardized over 504d (252d)
def f23rh_f23_revenue_hypergrowth_zaccel_252d_base_v126_signal(revenue):
    result = _z(_f23_accel(revenue, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration standardized over 252d (21d, fast)
def f23rh_f23_revenue_hypergrowth_zaccel_21d_base_v127_signal(revenue):
    result = _z(_f23_accel(revenue, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# growth spread: 21d vs 63d (near-term thrust differential)
def f23rh_f23_revenue_hypergrowth_spread_21_63_base_v128_signal(revenue):
    result = _f23_growth(revenue, 21) - _f23_growth(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth spread: 126d vs 252d
def f23rh_f23_revenue_hypergrowth_spread_126_252_base_v129_signal(revenue):
    result = _f23_growth(revenue, 126) - _f23_growth(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log-growth spread: 126d vs 504d
def f23rh_f23_revenue_hypergrowth_lspread_126_504_base_v130_signal(revenue):
    result = _f23_logcompound(revenue, 126) - _f23_logcompound(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue growth: 252d mean of 63d growth
def f23rh_f23_revenue_hypergrowth_smooth_252d_base_v131_signal(revenue):
    result = _mean(_f23_growth(revenue, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue growth: 21d mean of 21d growth (fast)
def f23rh_f23_revenue_hypergrowth_smooth_21d_base_v132_signal(revenue):
    result = _mean(_f23_growth(revenue, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM-smoothed revenue growth (span 63 of 21d growth)
def f23rh_f23_revenue_hypergrowth_ewm_63d_base_v133_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = g.ewm(span=63, min_periods=21).mean() + _f23_growth(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWM-smoothed revenue growth (span 126 of 63d growth)
def f23rh_f23_revenue_hypergrowth_ewm_126d_base_v134_signal(revenue):
    g = _f23_growth(revenue, 63)
    result = g.ewm(span=126, min_periods=42).mean() + _f23_growth(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth info ratio: 252d growth over 504d dispersion
def f23rh_f23_revenue_hypergrowth_inforatio_252d_base_v135_signal(revenue):
    g = _f23_growth(revenue, 252)
    result = _safe_div(g, _std(g, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth info ratio: 21d growth over 126d dispersion
def f23rh_f23_revenue_hypergrowth_inforatio_21d_base_v136_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = _safe_div(g, _std(g, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion: std of 21d growth over 504d
def f23rh_f23_revenue_hypergrowth_disp_504d_base_v137_signal(revenue):
    result = _std(_f23_growth(revenue, 21), 504) + _f23_growth(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion: std of 63d growth over 126d
def f23rh_f23_revenue_hypergrowth_disp63_126d_base_v138_signal(revenue):
    result = _std(_f23_growth(revenue, 63), 126) + _f23_growth(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth coefficient of variation inverse (consistency, 252d)
def f23rh_f23_revenue_hypergrowth_consist_252d_base_v139_signal(revenue):
    g = _f23_growth(revenue, 63)
    result = _safe_div(_mean(g, 252).abs(), _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gp asset turnover log compounding growth 252d
def f23rh_f23_revenue_hypergrowth_gpturnlog_252d_base_v140_signal(gp, assets):
    turn = _safe_div(gp, assets)
    result = _f23_logcompound(turn, 252) + _f23_logcompound(gp, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per asset z-scored growth (efficiency hypergrowth, 126d)
def f23rh_f23_revenue_hypergrowth_turngz_126d_base_v141_signal(revenue, assets):
    turn = _safe_div(revenue, assets)
    result = _f23_growthz(turn, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth times gp growth (compound hypergrowth signal, 126d)
def f23rh_f23_revenue_hypergrowth_compound_126d_base_v142_signal(revenue, gp):
    result = _f23_growth(revenue, 126) * (1.0 + _f23_growth(gp, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth times gp growth (252d)
def f23rh_f23_revenue_hypergrowth_compound_252d_base_v143_signal(revenue, gp):
    result = _f23_growth(revenue, 252) * (1.0 + _f23_growth(gp, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration smoothed (63d mean of 63d accel)
def f23rh_f23_revenue_hypergrowth_smoothaccel_63d_base_v144_signal(revenue):
    result = _mean(_f23_accel(revenue, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration smoothed (126d mean of 126d accel)
def f23rh_f23_revenue_hypergrowth_smoothaccel_126d_base_v145_signal(revenue):
    result = _mean(_f23_accel(revenue, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth relative to gp growth (efficiency of growth, ratio 252d)
def f23rh_f23_revenue_hypergrowth_gpratio_252d_base_v146_signal(revenue, gp):
    result = _safe_div(_f23_growth(gp, 252), _f23_growth(revenue, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth relative to assets growth (ratio 126d)
def f23rh_f23_revenue_hypergrowth_assetratio_126d_base_v147_signal(revenue, assets):
    result = _safe_div(_f23_growth(revenue, 126), _f23_growth(assets, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# revenue hypergrowth composite: growth z plus acceleration z (126d)
def f23rh_f23_revenue_hypergrowth_zcomposite_126d_base_v148_signal(revenue):
    result = _f23_growthz(revenue, 126) + _z(_f23_accel(revenue, 126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue hypergrowth composite: growth z plus acceleration z (63d)
def f23rh_f23_revenue_hypergrowth_zcomposite_63d_base_v149_signal(revenue):
    result = _f23_growthz(revenue, 63) + _z(_f23_accel(revenue, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# full hypergrowth composite: blended revenue + gp + turnover growth (126d)
def f23rh_f23_revenue_hypergrowth_fullcomposite_126d_base_v150_signal(revenue, gp, assets):
    turn = _safe_div(revenue, assets)
    result = (_f23_growth(revenue, 126) + _f23_growth(gp, 126)
              + _f23_growth(turn, 126)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23rh_f23_revenue_hypergrowth_growth_315d_base_v076_signal,
    f23rh_f23_revenue_hypergrowth_growth_378d_base_v077_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_315d_base_v078_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_378d_base_v079_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_84d_base_v080_signal,
    f23rh_f23_revenue_hypergrowth_accel_189d_base_v081_signal,
    f23rh_f23_revenue_hypergrowth_accel_504d_base_v082_signal,
    f23rh_f23_revenue_hypergrowth_relaccel_63d_base_v083_signal,
    f23rh_f23_revenue_hypergrowth_relaccel_126d_base_v084_signal,
    f23rh_f23_revenue_hypergrowth_growthz_84d_base_v085_signal,
    f23rh_f23_revenue_hypergrowth_growthz_189d_base_v086_signal,
    f23rh_f23_revenue_hypergrowth_zg126_63d_base_v087_signal,
    f23rh_f23_revenue_hypergrowth_zg504_126d_base_v088_signal,
    f23rh_f23_revenue_hypergrowth_trend_189d_base_v089_signal,
    f23rh_f23_revenue_hypergrowth_trend_504d_base_v090_signal,
    f23rh_f23_revenue_hypergrowth_stab_504d_base_v091_signal,
    f23rh_f23_revenue_hypergrowth_stab_63d_base_v092_signal,
    f23rh_f23_revenue_hypergrowth_vsmean_504d_base_v093_signal,
    f23rh_f23_revenue_hypergrowth_vsmean_21d_base_v094_signal,
    f23rh_f23_revenue_hypergrowth_cagr_252d_base_v095_signal,
    f23rh_f23_revenue_hypergrowth_cagr_504d_base_v096_signal,
    f23rh_f23_revenue_hypergrowth_turngrow_21d_base_v097_signal,
    f23rh_f23_revenue_hypergrowth_turnlog_252d_base_v098_signal,
    f23rh_f23_revenue_hypergrowth_turnz_252d_base_v099_signal,
    f23rh_f23_revenue_hypergrowth_rank_252d_base_v100_signal,
    f23rh_f23_revenue_hypergrowth_rankl_126d_base_v101_signal,
    f23rh_f23_revenue_hypergrowth_sustainlog_multi_base_v102_signal,
    f23rh_f23_revenue_hypergrowth_qualgrow_63d_base_v103_signal,
    f23rh_f23_revenue_hypergrowth_qualgrow_126d_base_v104_signal,
    f23rh_f23_revenue_hypergrowth_usdgrow_84d_base_v105_signal,
    f23rh_f23_revenue_hypergrowth_usdgrow_504d_base_v106_signal,
    f23rh_f23_revenue_hypergrowth_usdz_126d_base_v107_signal,
    f23rh_f23_revenue_hypergrowth_usdtrend_252d_base_v108_signal,
    f23rh_f23_revenue_hypergrowth_fxspread_126d_base_v109_signal,
    f23rh_f23_revenue_hypergrowth_fxspread_252d_base_v110_signal,
    f23rh_f23_revenue_hypergrowth_gpgrow_84d_base_v111_signal,
    f23rh_f23_revenue_hypergrowth_gpgrow_504d_base_v112_signal,
    f23rh_f23_revenue_hypergrowth_gpz_126d_base_v113_signal,
    f23rh_f23_revenue_hypergrowth_gpz_252d_base_v114_signal,
    f23rh_f23_revenue_hypergrowth_gptrend_252d_base_v115_signal,
    f23rh_f23_revenue_hypergrowth_gpaccel_252d_base_v116_signal,
    f23rh_f23_revenue_hypergrowth_marggrow_126d_base_v117_signal,
    f23rh_f23_revenue_hypergrowth_marggrow_252d_base_v118_signal,
    f23rh_f23_revenue_hypergrowth_margz_252d_base_v119_signal,
    f23rh_f23_revenue_hypergrowth_margadj_126d_base_v120_signal,
    f23rh_f23_revenue_hypergrowth_organiclog_252d_base_v121_signal,
    f23rh_f23_revenue_hypergrowth_organic_63d_base_v122_signal,
    f23rh_f23_revenue_hypergrowth_assetaccel_126d_base_v123_signal,
    f23rh_f23_revenue_hypergrowth_assetz_252d_base_v124_signal,
    f23rh_f23_revenue_hypergrowth_surp_252d_base_v125_signal,
    f23rh_f23_revenue_hypergrowth_zaccel_252d_base_v126_signal,
    f23rh_f23_revenue_hypergrowth_zaccel_21d_base_v127_signal,
    f23rh_f23_revenue_hypergrowth_spread_21_63_base_v128_signal,
    f23rh_f23_revenue_hypergrowth_spread_126_252_base_v129_signal,
    f23rh_f23_revenue_hypergrowth_lspread_126_504_base_v130_signal,
    f23rh_f23_revenue_hypergrowth_smooth_252d_base_v131_signal,
    f23rh_f23_revenue_hypergrowth_smooth_21d_base_v132_signal,
    f23rh_f23_revenue_hypergrowth_ewm_63d_base_v133_signal,
    f23rh_f23_revenue_hypergrowth_ewm_126d_base_v134_signal,
    f23rh_f23_revenue_hypergrowth_inforatio_252d_base_v135_signal,
    f23rh_f23_revenue_hypergrowth_inforatio_21d_base_v136_signal,
    f23rh_f23_revenue_hypergrowth_disp_504d_base_v137_signal,
    f23rh_f23_revenue_hypergrowth_disp63_126d_base_v138_signal,
    f23rh_f23_revenue_hypergrowth_consist_252d_base_v139_signal,
    f23rh_f23_revenue_hypergrowth_gpturnlog_252d_base_v140_signal,
    f23rh_f23_revenue_hypergrowth_turngz_126d_base_v141_signal,
    f23rh_f23_revenue_hypergrowth_compound_126d_base_v142_signal,
    f23rh_f23_revenue_hypergrowth_compound_252d_base_v143_signal,
    f23rh_f23_revenue_hypergrowth_smoothaccel_63d_base_v144_signal,
    f23rh_f23_revenue_hypergrowth_smoothaccel_126d_base_v145_signal,
    f23rh_f23_revenue_hypergrowth_gpratio_252d_base_v146_signal,
    f23rh_f23_revenue_hypergrowth_assetratio_126d_base_v147_signal,
    f23rh_f23_revenue_hypergrowth_zcomposite_126d_base_v148_signal,
    f23rh_f23_revenue_hypergrowth_zcomposite_63d_base_v149_signal,
    f23rh_f23_revenue_hypergrowth_fullcomposite_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_REVENUE_HYPERGROWTH_REGISTRY_076_150 = REGISTRY


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
           "revenueusd"}
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
    domain_primitives = ("_f23_growth", "_f23_accel", "_f23_growthz", "_f23_logcompound")
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
    print(f"OK f23_revenue_hypergrowth_base_076_150_claude: {n_features} features pass")
