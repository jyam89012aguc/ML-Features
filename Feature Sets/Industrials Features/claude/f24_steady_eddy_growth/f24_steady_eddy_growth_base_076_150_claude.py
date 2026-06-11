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


# ===== folder domain primitives =====
def _f24_growth_consistency(revenue, w):
    g = revenue.pct_change(periods=w)
    mu = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return mu - sd


def _f24_growth_cv(revenue, w):
    g = revenue.pct_change(periods=w)
    mu = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / (mu.abs() + 1e-9)


def _f24_steady_growth_score(revenue, netinc, w):
    rg = revenue.pct_change(periods=w)
    ig = netinc.pct_change(periods=w)
    rmu = rg.rolling(w, min_periods=max(1, w // 2)).mean()
    imu = ig.rolling(w, min_periods=max(1, w // 2)).mean()
    rsd = rg.rolling(w, min_periods=max(1, w // 2)).std()
    isd = ig.rolling(w, min_periods=max(1, w // 2)).std()
    return (rmu + imu) - (rsd + isd)


_FEATURES = []


def _add(fn):
    _FEATURES.append(fn)
    return fn


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_w63_base_v076_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 63), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_w63_base_v077_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 63), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_w63_base_v078_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 63), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w252_w42_base_v079_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 252), 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w252_w42_base_v080_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 252), 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w252_w42_base_v081_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 252), 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w504_w63_base_v082_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 504), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w504_w63_base_v083_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 504), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w504_w63_base_v084_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 504), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_ema21_base_v085_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_ema21_base_v086_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_ema21_base_v087_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_ema252_base_v088_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_ema252_base_v089_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_ema252_base_v090_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_diff21_base_v091_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_diff21_base_v092_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_diff21_base_v093_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_streak_pos_base_v094_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_streak_low_base_v095_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    low = (base < base.rolling(252, min_periods=63).median()).astype(float)
    streak = low.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_streak_pos_base_v096_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_above_qt_base_v097_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base > qt).astype(float) * base
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_below_qt_base_v098_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base < qt).astype(float) * base
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_inv_base_v099_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = (1.0 / (base.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_inv_base_v100_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = (1.0 / (base.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w_42_z252_base_v101_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 42)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w_42_z252_base_v102_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 42)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w_42_z252_base_v103_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 42)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w_189_21d_base_v104_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w_189_21d_base_v105_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w_189_21d_base_v106_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w_378_63d_base_v107_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w_378_63d_base_v108_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w_378_63d_base_v109_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_x_close2_base_v110_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_sqrt_base_v111_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_sqrt_base_v112_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_log_base_v113_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_xebitda_base_v114_signal(revenue, ebitda, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_xebitda_base_v115_signal(revenue, ebitda, closeadj):
    base = _f24_growth_cv(revenue, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_xebitda_base_v116_signal(revenue, netinc, ebitda, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_signaled_base_v117_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_signaled_base_v118_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_w42_base_v119_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 63), 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_w42_base_v120_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 63), 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_w42_base_v121_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 63), 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_z_504d_base_v122_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_z_63d_base_v123_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_z_63d_base_v124_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_z_63d_base_v125_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_std_63d_base_v126_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_std_63d_base_v127_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_std_63d_base_v128_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_cv_252d_v2_base_v129_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 252)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_cv_252d_base_v130_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 252)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_cv_252d_base_v131_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 252)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_minus_score_base_v132_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    result = (c - s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_minus_score_base_v133_signal(revenue, netinc, closeadj):
    v = _f24_growth_cv(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    result = (v - s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_div_cv_base_v134_signal(revenue, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    result = _safe_div(c, v.abs() + 1e-6) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_div_cv_base_v135_signal(revenue, netinc, closeadj):
    s = _f24_steady_growth_score(revenue, netinc, 63)
    v = _f24_growth_cv(revenue, 63)
    result = _safe_div(s, v.abs() + 1e-6) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_triple_product_base_v136_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    result = c * v * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_xclose_base_v137_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_xclose_base_v138_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_xclose_base_v139_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w252_w63_base_v140_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 252), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w252_w63_base_v141_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 252), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w252_w63_base_v142_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 252), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w252_w126_base_v143_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 252), 126) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w252_w126_base_v144_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 252), 126) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w252_w126_base_v145_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 252), 126) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_cv_diff_base_v146_signal(revenue, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    base = (c - v) * closeadj
    result = _mean(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_consistency_diff_base_v147_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    base = (s - c) * closeadj
    result = _mean(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_w126_base_v148_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 63), 126) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_w126_base_v149_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 63), 126) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_w126_base_v150_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 63), 126) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_STEADY_EDDY_GROWTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {"closeadj": closeadj, "revenue": revenue, "netinc": netinc, "ebitda": ebitda}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f24_growth_consistency", "_f24_growth_cv", "_f24_steady_growth_score")
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
    print(f"OK f24_steady_eddy_growth_base_076_150_claude: {n_features} features pass")
