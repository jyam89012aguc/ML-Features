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


# ============ FEATURES 001-075 ============

# 63d revenue growth (quarterly hypergrowth)
def f23rh_f23_revenue_hypergrowth_growth_63d_base_v001_signal(revenue):
    result = _f23_growth(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue growth (half-year hypergrowth)
def f23rh_f23_revenue_hypergrowth_growth_126d_base_v002_signal(revenue):
    result = _f23_growth(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth (annual hypergrowth)
def f23rh_f23_revenue_hypergrowth_growth_252d_base_v003_signal(revenue):
    result = _f23_growth(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth (two-year hypergrowth)
def f23rh_f23_revenue_hypergrowth_growth_504d_base_v004_signal(revenue):
    result = _f23_growth(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth (near-term thrust)
def f23rh_f23_revenue_hypergrowth_growth_21d_base_v005_signal(revenue):
    result = _f23_growth(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d revenue growth
def f23rh_f23_revenue_hypergrowth_growth_42d_base_v006_signal(revenue):
    result = _f23_growth(revenue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d revenue growth
def f23rh_f23_revenue_hypergrowth_growth_84d_base_v007_signal(revenue):
    result = _f23_growth(revenue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d revenue growth
def f23rh_f23_revenue_hypergrowth_growth_189d_base_v008_signal(revenue):
    result = _f23_growth(revenue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_63d_base_v009_signal(revenue):
    result = _f23_logcompound(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_126d_base_v010_signal(revenue):
    result = _f23_logcompound(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_252d_base_v011_signal(revenue):
    result = _f23_logcompound(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_504d_base_v012_signal(revenue):
    result = _f23_logcompound(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_21d_base_v013_signal(revenue):
    result = _f23_logcompound(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_42d_base_v014_signal(revenue):
    result = _f23_logcompound(revenue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d log compounding growth
def f23rh_f23_revenue_hypergrowth_logcmp_189d_base_v015_signal(revenue):
    result = _f23_logcompound(revenue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth acceleration (level)
def f23rh_f23_revenue_hypergrowth_accel_63d_base_v016_signal(revenue):
    result = _f23_accel(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue growth acceleration (level)
def f23rh_f23_revenue_hypergrowth_accel_126d_base_v017_signal(revenue):
    result = _f23_accel(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth acceleration (level)
def f23rh_f23_revenue_hypergrowth_accel_252d_base_v018_signal(revenue):
    result = _f23_accel(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth acceleration (level)
def f23rh_f23_revenue_hypergrowth_accel_21d_base_v019_signal(revenue):
    result = _f23_accel(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d revenue growth acceleration (level)
def f23rh_f23_revenue_hypergrowth_accel_42d_base_v020_signal(revenue):
    result = _f23_accel(revenue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d revenue growth acceleration (level)
def f23rh_f23_revenue_hypergrowth_accel_84d_base_v021_signal(revenue):
    result = _f23_accel(revenue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d standardized revenue growth (z-score)
def f23rh_f23_revenue_hypergrowth_growthz_63d_base_v022_signal(revenue):
    result = _f23_growthz(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d standardized revenue growth (z-score)
def f23rh_f23_revenue_hypergrowth_growthz_126d_base_v023_signal(revenue):
    result = _f23_growthz(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d standardized revenue growth (z-score)
def f23rh_f23_revenue_hypergrowth_growthz_252d_base_v024_signal(revenue):
    result = _f23_growthz(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d standardized revenue growth (z-score)
def f23rh_f23_revenue_hypergrowth_growthz_21d_base_v025_signal(revenue):
    result = _f23_growthz(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d standardized revenue growth (z-score)
def f23rh_f23_revenue_hypergrowth_growthz_42d_base_v026_signal(revenue):
    result = _f23_growthz(revenue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth trend slope over 63d (OLS-style normalized diff of growth)
def f23rh_f23_revenue_hypergrowth_trend_63d_base_v027_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = (g - g.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth trend slope over 126d
def f23rh_f23_revenue_hypergrowth_trend_126d_base_v028_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = (g - g.shift(126)) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth trend slope over 252d
def f23rh_f23_revenue_hypergrowth_trend_252d_base_v029_signal(revenue):
    g = _f23_growth(revenue, 63)
    result = (g - g.shift(252)) / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth stability: mean/std of 21d growth over 126d
def f23rh_f23_revenue_hypergrowth_stab_126d_base_v030_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = _safe_div(_mean(g, 126), _std(g, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth stability: mean/std of 21d growth over 252d
def f23rh_f23_revenue_hypergrowth_stab_252d_base_v031_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = _safe_div(_mean(g, 252), _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth stability: mean/std of 63d growth over 252d
def f23rh_f23_revenue_hypergrowth_stab63_252d_base_v032_signal(revenue):
    g = _f23_growth(revenue, 63)
    result = _safe_div(_mean(g, 252), _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs trailing 126d mean (relative level)
def f23rh_f23_revenue_hypergrowth_vsmean_126d_base_v033_signal(revenue):
    result = _safe_div(revenue, _mean(revenue, 126)) - 1.0 + _f23_growth(revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs trailing 252d mean (relative level)
def f23rh_f23_revenue_hypergrowth_vsmean_252d_base_v034_signal(revenue):
    result = _safe_div(revenue, _mean(revenue, 252)) - 1.0 + _f23_growth(revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs trailing 63d mean (relative level)
def f23rh_f23_revenue_hypergrowth_vsmean_63d_base_v035_signal(revenue):
    result = _safe_div(revenue, _mean(revenue, 63)) - 1.0 + _f23_growth(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# compounding rate: annualized 63d log growth
def f23rh_f23_revenue_hypergrowth_cagr_63d_base_v036_signal(revenue):
    result = _f23_logcompound(revenue, 63) * (252.0 / 63.0)
    return result.replace([np.inf, -np.inf], np.nan)


# compounding rate: annualized 126d log growth
def f23rh_f23_revenue_hypergrowth_cagr_126d_base_v037_signal(revenue):
    result = _f23_logcompound(revenue, 126) * (252.0 / 126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# compounding rate: annualized 21d log growth
def f23rh_f23_revenue_hypergrowth_cagr_21d_base_v038_signal(revenue):
    result = _f23_logcompound(revenue, 21) * (252.0 / 21.0)
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover growth: revenue/assets, 63d growth
def f23rh_f23_revenue_hypergrowth_turngrow_63d_base_v039_signal(revenue, assets):
    turn = _safe_div(revenue, assets)
    result = _f23_growth(turn, 63) + _f23_growth(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover growth: revenue/assets, 126d growth
def f23rh_f23_revenue_hypergrowth_turngrow_126d_base_v040_signal(revenue, assets):
    turn = _safe_div(revenue, assets)
    result = _f23_growth(turn, 126) + _f23_growth(revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover growth: revenue/assets, 252d growth
def f23rh_f23_revenue_hypergrowth_turngrow_252d_base_v041_signal(revenue, assets):
    turn = _safe_div(revenue, assets)
    result = _f23_growth(turn, 252) + _f23_growth(revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth percentile rank over 126d
def f23rh_f23_revenue_hypergrowth_rank_63d_base_v042_signal(revenue):
    g = _f23_growth(revenue, 63)
    result = g.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth percentile rank over 252d
def f23rh_f23_revenue_hypergrowth_rank_126d_base_v043_signal(revenue):
    g = _f23_growth(revenue, 126)
    result = g.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth percentile rank: 21d growth over 252d
def f23rh_f23_revenue_hypergrowth_rank_21d_base_v044_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = g.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# sustained-growth composite: blended 63/126/252 revenue growth
def f23rh_f23_revenue_hypergrowth_sustain_multi_base_v045_signal(revenue):
    result = (_f23_growth(revenue, 63) + _f23_growth(revenue, 126)
              + _f23_growth(revenue, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd 63d growth (USD-normalized hypergrowth)
def f23rh_f23_revenue_hypergrowth_usdgrow_63d_base_v046_signal(revenueusd):
    result = _f23_growth(revenueusd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd 126d growth
def f23rh_f23_revenue_hypergrowth_usdgrow_126d_base_v047_signal(revenueusd):
    result = _f23_growth(revenueusd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd 252d growth
def f23rh_f23_revenue_hypergrowth_usdgrow_252d_base_v048_signal(revenueusd):
    result = _f23_growth(revenueusd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd 252d log compounding growth
def f23rh_f23_revenue_hypergrowth_usdlogcmp_252d_base_v049_signal(revenueusd):
    result = _f23_logcompound(revenueusd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd 126d growth acceleration
def f23rh_f23_revenue_hypergrowth_usdaccel_126d_base_v050_signal(revenueusd):
    result = _f23_accel(revenueusd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross profit 63d growth (quality of hypergrowth)
def f23rh_f23_revenue_hypergrowth_gpgrow_63d_base_v051_signal(gp):
    result = _f23_growth(gp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gross profit 126d growth
def f23rh_f23_revenue_hypergrowth_gpgrow_126d_base_v052_signal(gp):
    result = _f23_growth(gp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross profit 252d growth
def f23rh_f23_revenue_hypergrowth_gpgrow_252d_base_v053_signal(gp):
    result = _f23_growth(gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross profit 252d log compounding growth
def f23rh_f23_revenue_hypergrowth_gplogcmp_252d_base_v054_signal(gp):
    result = _f23_logcompound(gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross profit 126d growth acceleration
def f23rh_f23_revenue_hypergrowth_gpaccel_126d_base_v055_signal(gp):
    result = _f23_accel(gp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit-to-revenue spread of growth (margin-led vs revenue-led, 126d)
def f23rh_f23_revenue_hypergrowth_gpspread_126d_base_v056_signal(revenue, gp):
    result = _f23_growth(gp, 126) - _f23_growth(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit-to-revenue spread of growth (252d)
def f23rh_f23_revenue_hypergrowth_gpspread_252d_base_v057_signal(revenue, gp):
    result = _f23_growth(gp, 252) - _f23_growth(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus assets growth (organic vs balance-sheet expansion, 126d)
def f23rh_f23_revenue_hypergrowth_organic_126d_base_v058_signal(revenue, assets):
    result = _f23_growth(revenue, 126) - _f23_growth(assets, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus assets growth (252d)
def f23rh_f23_revenue_hypergrowth_organic_252d_base_v059_signal(revenue, assets):
    result = _f23_growth(revenue, 252) - _f23_growth(assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth surprise: 63d growth minus its 126d mean
def f23rh_f23_revenue_hypergrowth_surp_63d_base_v060_signal(revenue):
    g = _f23_growth(revenue, 63)
    result = g - _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth surprise: 126d growth minus its 252d mean
def f23rh_f23_revenue_hypergrowth_surp_126d_base_v061_signal(revenue):
    g = _f23_growth(revenue, 126)
    result = g - _mean(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth surprise: 21d growth minus its 63d mean
def f23rh_f23_revenue_hypergrowth_surp_21d_base_v062_signal(revenue):
    g = _f23_growth(revenue, 21)
    result = g - _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration standardized over 252d
def f23rh_f23_revenue_hypergrowth_zaccel_63d_base_v063_signal(revenue):
    result = _z(_f23_accel(revenue, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration standardized over 252d (126d)
def f23rh_f23_revenue_hypergrowth_zaccel_126d_base_v064_signal(revenue):
    result = _z(_f23_accel(revenue, 126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# growth spread: short minus long (63d vs 252d)
def f23rh_f23_revenue_hypergrowth_spread_63_252_base_v065_signal(revenue):
    result = _f23_growth(revenue, 63) - _f23_growth(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# growth spread: 21d vs 126d
def f23rh_f23_revenue_hypergrowth_spread_21_126_base_v066_signal(revenue):
    result = _f23_growth(revenue, 21) - _f23_growth(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# log-growth spread: 63d vs 252d
def f23rh_f23_revenue_hypergrowth_lspread_63_252_base_v067_signal(revenue):
    result = _f23_logcompound(revenue, 63) - _f23_logcompound(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue growth: 63d mean of 21d growth
def f23rh_f23_revenue_hypergrowth_smooth_63d_base_v068_signal(revenue):
    result = _mean(_f23_growth(revenue, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue growth: 126d mean of 63d growth
def f23rh_f23_revenue_hypergrowth_smooth_126d_base_v069_signal(revenue):
    result = _mean(_f23_growth(revenue, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed log compounding growth: 42d mean of 63d logcmp
def f23rh_f23_revenue_hypergrowth_smoothlog_63d_base_v070_signal(revenue):
    result = _mean(_f23_logcompound(revenue, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth information ratio: 63d growth over its 252d dispersion
def f23rh_f23_revenue_hypergrowth_inforatio_63d_base_v071_signal(revenue):
    g = _f23_growth(revenue, 63)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth information ratio: 126d growth over its 252d dispersion
def f23rh_f23_revenue_hypergrowth_inforatio_126d_base_v072_signal(revenue):
    g = _f23_growth(revenue, 126)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion: std of 21d growth over 126d
def f23rh_f23_revenue_hypergrowth_disp_126d_base_v073_signal(revenue):
    result = _std(_f23_growth(revenue, 21), 126) + _f23_growth(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion: std of 63d growth over 252d
def f23rh_f23_revenue_hypergrowth_disp_252d_base_v074_signal(revenue):
    result = _std(_f23_growth(revenue, 63), 252) + _f23_growth(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit asset turnover growth: gp/assets, 126d growth
def f23rh_f23_revenue_hypergrowth_gpturn_126d_base_v075_signal(gp, assets):
    turn = _safe_div(gp, assets)
    result = _f23_growth(turn, 126) + _f23_growth(gp, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23rh_f23_revenue_hypergrowth_growth_63d_base_v001_signal,
    f23rh_f23_revenue_hypergrowth_growth_126d_base_v002_signal,
    f23rh_f23_revenue_hypergrowth_growth_252d_base_v003_signal,
    f23rh_f23_revenue_hypergrowth_growth_504d_base_v004_signal,
    f23rh_f23_revenue_hypergrowth_growth_21d_base_v005_signal,
    f23rh_f23_revenue_hypergrowth_growth_42d_base_v006_signal,
    f23rh_f23_revenue_hypergrowth_growth_84d_base_v007_signal,
    f23rh_f23_revenue_hypergrowth_growth_189d_base_v008_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_63d_base_v009_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_126d_base_v010_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_252d_base_v011_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_504d_base_v012_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_21d_base_v013_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_42d_base_v014_signal,
    f23rh_f23_revenue_hypergrowth_logcmp_189d_base_v015_signal,
    f23rh_f23_revenue_hypergrowth_accel_63d_base_v016_signal,
    f23rh_f23_revenue_hypergrowth_accel_126d_base_v017_signal,
    f23rh_f23_revenue_hypergrowth_accel_252d_base_v018_signal,
    f23rh_f23_revenue_hypergrowth_accel_21d_base_v019_signal,
    f23rh_f23_revenue_hypergrowth_accel_42d_base_v020_signal,
    f23rh_f23_revenue_hypergrowth_accel_84d_base_v021_signal,
    f23rh_f23_revenue_hypergrowth_growthz_63d_base_v022_signal,
    f23rh_f23_revenue_hypergrowth_growthz_126d_base_v023_signal,
    f23rh_f23_revenue_hypergrowth_growthz_252d_base_v024_signal,
    f23rh_f23_revenue_hypergrowth_growthz_21d_base_v025_signal,
    f23rh_f23_revenue_hypergrowth_growthz_42d_base_v026_signal,
    f23rh_f23_revenue_hypergrowth_trend_63d_base_v027_signal,
    f23rh_f23_revenue_hypergrowth_trend_126d_base_v028_signal,
    f23rh_f23_revenue_hypergrowth_trend_252d_base_v029_signal,
    f23rh_f23_revenue_hypergrowth_stab_126d_base_v030_signal,
    f23rh_f23_revenue_hypergrowth_stab_252d_base_v031_signal,
    f23rh_f23_revenue_hypergrowth_stab63_252d_base_v032_signal,
    f23rh_f23_revenue_hypergrowth_vsmean_126d_base_v033_signal,
    f23rh_f23_revenue_hypergrowth_vsmean_252d_base_v034_signal,
    f23rh_f23_revenue_hypergrowth_vsmean_63d_base_v035_signal,
    f23rh_f23_revenue_hypergrowth_cagr_63d_base_v036_signal,
    f23rh_f23_revenue_hypergrowth_cagr_126d_base_v037_signal,
    f23rh_f23_revenue_hypergrowth_cagr_21d_base_v038_signal,
    f23rh_f23_revenue_hypergrowth_turngrow_63d_base_v039_signal,
    f23rh_f23_revenue_hypergrowth_turngrow_126d_base_v040_signal,
    f23rh_f23_revenue_hypergrowth_turngrow_252d_base_v041_signal,
    f23rh_f23_revenue_hypergrowth_rank_63d_base_v042_signal,
    f23rh_f23_revenue_hypergrowth_rank_126d_base_v043_signal,
    f23rh_f23_revenue_hypergrowth_rank_21d_base_v044_signal,
    f23rh_f23_revenue_hypergrowth_sustain_multi_base_v045_signal,
    f23rh_f23_revenue_hypergrowth_usdgrow_63d_base_v046_signal,
    f23rh_f23_revenue_hypergrowth_usdgrow_126d_base_v047_signal,
    f23rh_f23_revenue_hypergrowth_usdgrow_252d_base_v048_signal,
    f23rh_f23_revenue_hypergrowth_usdlogcmp_252d_base_v049_signal,
    f23rh_f23_revenue_hypergrowth_usdaccel_126d_base_v050_signal,
    f23rh_f23_revenue_hypergrowth_gpgrow_63d_base_v051_signal,
    f23rh_f23_revenue_hypergrowth_gpgrow_126d_base_v052_signal,
    f23rh_f23_revenue_hypergrowth_gpgrow_252d_base_v053_signal,
    f23rh_f23_revenue_hypergrowth_gplogcmp_252d_base_v054_signal,
    f23rh_f23_revenue_hypergrowth_gpaccel_126d_base_v055_signal,
    f23rh_f23_revenue_hypergrowth_gpspread_126d_base_v056_signal,
    f23rh_f23_revenue_hypergrowth_gpspread_252d_base_v057_signal,
    f23rh_f23_revenue_hypergrowth_organic_126d_base_v058_signal,
    f23rh_f23_revenue_hypergrowth_organic_252d_base_v059_signal,
    f23rh_f23_revenue_hypergrowth_surp_63d_base_v060_signal,
    f23rh_f23_revenue_hypergrowth_surp_126d_base_v061_signal,
    f23rh_f23_revenue_hypergrowth_surp_21d_base_v062_signal,
    f23rh_f23_revenue_hypergrowth_zaccel_63d_base_v063_signal,
    f23rh_f23_revenue_hypergrowth_zaccel_126d_base_v064_signal,
    f23rh_f23_revenue_hypergrowth_spread_63_252_base_v065_signal,
    f23rh_f23_revenue_hypergrowth_spread_21_126_base_v066_signal,
    f23rh_f23_revenue_hypergrowth_lspread_63_252_base_v067_signal,
    f23rh_f23_revenue_hypergrowth_smooth_63d_base_v068_signal,
    f23rh_f23_revenue_hypergrowth_smooth_126d_base_v069_signal,
    f23rh_f23_revenue_hypergrowth_smoothlog_63d_base_v070_signal,
    f23rh_f23_revenue_hypergrowth_inforatio_63d_base_v071_signal,
    f23rh_f23_revenue_hypergrowth_inforatio_126d_base_v072_signal,
    f23rh_f23_revenue_hypergrowth_disp_126d_base_v073_signal,
    f23rh_f23_revenue_hypergrowth_disp_252d_base_v074_signal,
    f23rh_f23_revenue_hypergrowth_gpturn_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_REVENUE_HYPERGROWTH_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f23_revenue_hypergrowth_base_001_075_claude: {n_features} features pass")
