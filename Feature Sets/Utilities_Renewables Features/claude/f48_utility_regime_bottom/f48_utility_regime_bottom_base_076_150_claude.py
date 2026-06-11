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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====
def _f48_revenue_bottom(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - mn) / mn.replace(0, np.nan).abs()


def _f48_margin_bottom(ebitdamargin, w):
    mn = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    return ebitdamargin - mn


def _f48_regime_bottom_score(revenue, ebitda, fcf, w):
    rb = (revenue - revenue.rolling(w, min_periods=max(1, w // 2)).min())
    eb = (ebitda - ebitda.rolling(w, min_periods=max(1, w // 2)).min())
    fb = (fcf - fcf.rolling(w, min_periods=max(1, w // 2)).min())
    return rb + eb + fb


# ===== features =====
def f48urb_f48_utility_regime_bottom_rs_full_84d_s01_base_v076_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 84)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_84d_s01_base_v077_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 84)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_84d_s01_base_v078_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 84)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_84d_s01_base_v079_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 84)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v080_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v081_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v082_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v083_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v084_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v085_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v086_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v087_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v088_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v089_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v090_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v091_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v092_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v093_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v094_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v095_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v096_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v097_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v098_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v099_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v100_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v101_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v102_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v103_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v104_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v105_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v106_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v107_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v108_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v109_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v110_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v111_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v112_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v113_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v114_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v115_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v116_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v117_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v118_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v119_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v120_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v121_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v122_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v123_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v124_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v125_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v126_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v127_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v128_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v129_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v130_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v131_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v132_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v133_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v134_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v135_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v136_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v137_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v138_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v139_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v140_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v141_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v142_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v143_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v144_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v145_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v146_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v147_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v148_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v149_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v150_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48urb_f48_utility_regime_bottom_rs_full_84d_s01_base_v076_signal,
    f48urb_f48_utility_regime_bottom_rs_full_84d_s01_base_v077_signal,
    f48urb_f48_utility_regime_bottom_rs_full_84d_s01_base_v078_signal,
    f48urb_f48_utility_regime_bottom_rs_full_84d_s01_base_v079_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v080_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v081_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v082_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v083_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v084_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v085_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v086_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s01_base_v087_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v088_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v089_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v090_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v091_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v092_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v093_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v094_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s01_base_v095_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v096_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v097_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v098_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v099_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v100_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v101_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v102_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s01_base_v103_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v104_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v105_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v106_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v107_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v108_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v109_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v110_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s01_base_v111_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v112_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v113_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v114_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v115_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v116_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v117_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v118_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s01_base_v119_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v120_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v121_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v122_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v123_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v124_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v125_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v126_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s01_base_v127_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v128_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v129_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v130_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v131_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v132_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v133_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v134_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s01_base_v135_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v136_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v137_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v138_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v139_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v140_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v141_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v142_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s01_base_v143_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v144_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v145_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v146_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v147_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v148_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v149_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s01_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_UTILITY_REGIME_BOTTOM_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "ebitda": ebitda, "ebitdamargin": ebitdamargin, "fcf": fcf, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_revenue_bottom", "_f48_margin_bottom", "_f48_regime_bottom_score",)
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
    print(f"OK f48_utility_regime_bottom_base_076_150_claude: {n_features} features pass")
