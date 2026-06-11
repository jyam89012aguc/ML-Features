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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f36_op_leverage_proxy(ebit, revenue, w):
    """Operating leverage proxy: rolling change in ebit / change in revenue."""
    de = ebit.diff(periods=w)
    dr = revenue.diff(periods=w)
    return de / dr.replace(0, np.nan)


def _f36_margin_revenue_beta(ebitdamargin, revenue, w):
    """Rolling covariance(margin, revenue%) / var(revenue%) - sensitivity beta."""
    rev_pct = revenue.pct_change()
    margin = ebitdamargin
    cov = margin.rolling(w, min_periods=max(2, w // 2)).cov(rev_pct)
    var = rev_pct.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f36_drop_through(ebit, revenue, w):
    """Incremental ebit per incremental revenue, smoothed."""
    de = ebit.diff(periods=w)
    dr = revenue.diff(periods=w)
    ratio = de / dr.replace(0, np.nan)
    return ratio.rolling(max(2, w // 2), min_periods=1).mean()


def f36oli_f36_operating_leverage_intensity_opleverage_5d_5d_slope_v001_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 5)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverage_10d_21d_slope_v002_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 10)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverage_21d_63d_slope_v003_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 21)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverage_42d_126d_slope_v004_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 42)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverage_63d_252d_slope_v005_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 63)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverage_126d_5d_slope_v006_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 126)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverage_189d_21d_slope_v007_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 189)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverage_252d_63d_slope_v008_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 252)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverage_378d_126d_slope_v009_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 378)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverage_504d_252d_slope_v010_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 504)
    base_ = p.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_5d_5d_slope_v011_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 5)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_10d_21d_slope_v012_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 10)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_21d_63d_slope_v013_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 21)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_42d_126d_slope_v014_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 42)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_63d_252d_slope_v015_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 63)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_126d_5d_slope_v016_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 126)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_189d_21d_slope_v017_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 189)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_252d_63d_slope_v018_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 252)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_378d_126d_slope_v019_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 378)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragesm_504d_252d_slope_v020_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 504)
    base_ = _mean(p.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_5d_5d_slope_v021_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 5)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_10d_21d_slope_v022_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 10)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_21d_63d_slope_v023_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 21)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_42d_126d_slope_v024_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 42)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_63d_252d_slope_v025_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 63)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_126d_5d_slope_v026_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 126)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_189d_21d_slope_v027_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 189)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_252d_63d_slope_v028_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 252)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_378d_126d_slope_v029_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 378)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitda_504d_252d_slope_v030_signal(ebit, revenue, ebitda, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 504)
    base_ = p.clip(-100, 100) * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbeta_63d_5d_slope_v031_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 63)
    base_ = b * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbeta_126d_21d_slope_v032_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 126)
    base_ = b * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbeta_189d_63d_slope_v033_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 189)
    base_ = b * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbeta_252d_126d_slope_v034_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 252)
    base_ = b * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbeta_378d_252d_slope_v035_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 378)
    base_ = b * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbeta_504d_5d_slope_v036_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 504)
    base_ = b * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_5d_21d_slope_v037_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 5)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_10d_63d_slope_v038_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 10)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_21d_126d_slope_v039_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_42d_252d_slope_v040_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 42)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_63d_5d_slope_v041_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 63)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_126d_21d_slope_v042_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 126)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_189d_63d_slope_v043_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 189)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_252d_126d_slope_v044_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 252)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_378d_252d_slope_v045_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 378)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthrough_504d_5d_slope_v046_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 504)
    base_ = d.clip(-100, 100) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_5d_21d_slope_v047_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 5)
    base_ = d.clip(-100, 100) * revenue.pct_change(5) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_10d_63d_slope_v048_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 10)
    base_ = d.clip(-100, 100) * revenue.pct_change(10) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_21d_126d_slope_v049_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = d.clip(-100, 100) * revenue.pct_change(21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_42d_252d_slope_v050_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 42)
    base_ = d.clip(-100, 100) * revenue.pct_change(42) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_63d_5d_slope_v051_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 63)
    base_ = d.clip(-100, 100) * revenue.pct_change(63) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_126d_21d_slope_v052_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 126)
    base_ = d.clip(-100, 100) * revenue.pct_change(126) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_189d_63d_slope_v053_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 189)
    base_ = d.clip(-100, 100) * revenue.pct_change(189) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_252d_126d_slope_v054_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 252)
    base_ = d.clip(-100, 100) * revenue.pct_change(252) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_378d_252d_slope_v055_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 378)
    base_ = d.clip(-100, 100) * revenue.pct_change(378) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxrev_504d_5d_slope_v056_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 504)
    base_ = d.clip(-100, 100) * revenue.pct_change(504) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragez_21d_in_252d_21d_slope_v057_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 21)
    base_ = _z(p.clip(-100, 100), 252) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragez_63d_in_252d_63d_slope_v058_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 63)
    base_ = _z(p.clip(-100, 100), 252) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragez_126d_in_252d_126d_slope_v059_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 126)
    base_ = _z(p.clip(-100, 100), 252) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragez_21d_in_504d_252d_slope_v060_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 21)
    base_ = _z(p.clip(-100, 100), 504) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragez_63d_in_504d_5d_slope_v061_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 63)
    base_ = _z(p.clip(-100, 100), 504) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragez_126d_in_504d_21d_slope_v062_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 126)
    base_ = _z(p.clip(-100, 100), 504) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_5d_63d_slope_v063_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 5)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_10d_126d_slope_v064_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 10)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_21d_252d_slope_v065_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_42d_5d_slope_v066_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 42)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_63d_21d_slope_v067_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 63)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_126d_63d_slope_v068_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 126)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_189d_126d_slope_v069_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 189)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_252d_252d_slope_v070_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 252)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_378d_5d_slope_v071_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 378)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughema_504d_21d_slope_v072_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 504)
    base_ = _ema(d.clip(-100, 100), 21) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_5d_63d_slope_v073_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 5)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_10d_126d_slope_v074_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 10)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_21d_252d_slope_v075_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 21)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_42d_5d_slope_v076_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 42)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_63d_21d_slope_v077_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 63)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_126d_63d_slope_v078_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 126)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_189d_126d_slope_v079_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 189)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_252d_252d_slope_v080_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 252)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_378d_5d_slope_v081_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 378)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebitratio_504d_21d_slope_v082_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 504)
    base_ = p.clip(-100, 100) * _safe_div(ebit, revenue) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetaxebit_63d_63d_slope_v083_signal(ebitdamargin, revenue, ebit, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 63)
    base_ = b * _safe_div(ebit, revenue) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetaxebit_126d_126d_slope_v084_signal(ebitdamargin, revenue, ebit, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 126)
    base_ = b * _safe_div(ebit, revenue) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetaxebit_189d_252d_slope_v085_signal(ebitdamargin, revenue, ebit, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 189)
    base_ = b * _safe_div(ebit, revenue) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetaxebit_252d_5d_slope_v086_signal(ebitdamargin, revenue, ebit, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 252)
    base_ = b * _safe_div(ebit, revenue) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetaxebit_378d_21d_slope_v087_signal(ebitdamargin, revenue, ebit, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 378)
    base_ = b * _safe_div(ebit, revenue) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetaxebit_504d_63d_slope_v088_signal(ebitdamargin, revenue, ebit, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 504)
    base_ = b * _safe_div(ebit, revenue) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughstd_63d_126d_slope_v089_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = _std(d.clip(-100, 100), 63) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughstd_126d_252d_slope_v090_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = _std(d.clip(-100, 100), 126) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughstd_189d_5d_slope_v091_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = _std(d.clip(-100, 100), 189) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughstd_252d_21d_slope_v092_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = _std(d.clip(-100, 100), 252) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughstd_378d_63d_slope_v093_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = _std(d.clip(-100, 100), 378) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughstd_504d_126d_slope_v094_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = _std(d.clip(-100, 100), 504) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_5d_252d_slope_v095_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 5)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_10d_5d_slope_v096_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 10)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_21d_21d_slope_v097_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 21)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_42d_63d_slope_v098_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 42)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_63d_126d_slope_v099_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 63)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_126d_252d_slope_v100_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 126)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_189d_5d_slope_v101_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 189)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_252d_21d_slope_v102_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 252)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_378d_63d_slope_v103_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 378)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragediff_504d_126d_slope_v104_signal(ebit, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 504)
    base_ = p.clip(-100, 100).diff(21) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetasq_126d_252d_slope_v105_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 126)
    base_ = b * b.abs() * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetasq_189d_5d_slope_v106_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 189)
    base_ = b * b.abs() * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetasq_252d_21d_slope_v107_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 252)
    base_ = b * b.abs() * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetasq_378d_63d_slope_v108_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 378)
    base_ = b * b.abs() * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetasq_504d_126d_slope_v109_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 504)
    base_ = b * b.abs() * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_5d_252d_slope_v110_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 5)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_10d_5d_slope_v111_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 10)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_21d_21d_slope_v112_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 21)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_42d_63d_slope_v113_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 42)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_63d_126d_slope_v114_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 63)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_126d_252d_slope_v115_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 126)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_189d_5d_slope_v116_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 189)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_252d_21d_slope_v117_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 252)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_378d_63d_slope_v118_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 378)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughsign_504d_126d_slope_v119_signal(ebit, revenue, closeadj):
    d = _f36_drop_through(ebit, revenue, 504)
    base_ = np.sign(d) * d.clip(-100, 100).abs() * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverageratio_21v63_252d_slope_v120_signal(ebit, revenue, closeadj):
    p1 = _f36_op_leverage_proxy(ebit, revenue, 21).clip(-100, 100)
    p2 = _f36_op_leverage_proxy(ebit, revenue, 63).clip(-100, 100)
    base_ = (p1 - p2) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverageratio_63v252_5d_slope_v121_signal(ebit, revenue, closeadj):
    p1 = _f36_op_leverage_proxy(ebit, revenue, 63).clip(-100, 100)
    p2 = _f36_op_leverage_proxy(ebit, revenue, 252).clip(-100, 100)
    base_ = (p1 - p2) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverageratio_21v252_21d_slope_v122_signal(ebit, revenue, closeadj):
    p1 = _f36_op_leverage_proxy(ebit, revenue, 21).clip(-100, 100)
    p2 = _f36_op_leverage_proxy(ebit, revenue, 252).clip(-100, 100)
    base_ = (p1 - p2) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverageratio_63v504_63d_slope_v123_signal(ebit, revenue, closeadj):
    p1 = _f36_op_leverage_proxy(ebit, revenue, 63).clip(-100, 100)
    p2 = _f36_op_leverage_proxy(ebit, revenue, 504).clip(-100, 100)
    base_ = (p1 - p2) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverageratio_126v252_126d_slope_v124_signal(ebit, revenue, closeadj):
    p1 = _f36_op_leverage_proxy(ebit, revenue, 126).clip(-100, 100)
    p2 = _f36_op_leverage_proxy(ebit, revenue, 252).clip(-100, 100)
    base_ = (p1 - p2) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleverageratio_252v504_252d_slope_v125_signal(ebit, revenue, closeadj):
    p1 = _f36_op_leverage_proxy(ebit, revenue, 252).clip(-100, 100)
    p2 = _f36_op_leverage_proxy(ebit, revenue, 504).clip(-100, 100)
    base_ = (p1 - p2) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_5d_5d_slope_v126_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 5).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_10d_21d_slope_v127_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 10).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_21d_63d_slope_v128_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 21).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_42d_126d_slope_v129_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 42).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_63d_252d_slope_v130_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 63).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_126d_5d_slope_v131_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 126).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_189d_21d_slope_v132_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 189).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_252d_63d_slope_v133_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 252).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_378d_126d_slope_v134_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 378).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_opleveragexebmar_504d_252d_slope_v135_signal(ebit, ebitda, revenue, closeadj):
    p = _f36_op_leverage_proxy(ebit, revenue, 504).clip(-100, 100)
    base_ = p * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughcross_21v63_5d_slope_v136_signal(ebit, revenue, closeadj):
    d1 = _f36_drop_through(ebit, revenue, 21).clip(-100, 100)
    d2 = _f36_drop_through(ebit, revenue, 63).clip(-100, 100)
    base_ = (d1 - d2) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughcross_63v252_21d_slope_v137_signal(ebit, revenue, closeadj):
    d1 = _f36_drop_through(ebit, revenue, 63).clip(-100, 100)
    d2 = _f36_drop_through(ebit, revenue, 252).clip(-100, 100)
    base_ = (d1 - d2) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughcross_252v504_63d_slope_v138_signal(ebit, revenue, closeadj):
    d1 = _f36_drop_through(ebit, revenue, 252).clip(-100, 100)
    d2 = _f36_drop_through(ebit, revenue, 504).clip(-100, 100)
    base_ = (d1 - d2) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetadiff_126d_126d_slope_v139_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 126)
    base_ = b.diff(21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetadiff_189d_252d_slope_v140_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 189)
    base_ = b.diff(21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetadiff_252d_5d_slope_v141_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 252)
    base_ = b.diff(21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetadiff_378d_21d_slope_v142_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 378)
    base_ = b.diff(21) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_marginbetadiff_504d_63d_slope_v143_signal(ebitdamargin, revenue, closeadj):
    b = _f36_margin_revenue_beta(ebitdamargin, revenue, 504)
    base_ = b.diff(21) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxebitda_5d_126d_slope_v144_signal(ebit, revenue, ebitda, closeadj):
    d = _f36_drop_through(ebit, revenue, 5).clip(-100, 100)
    base_ = d * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxebitda_10d_252d_slope_v145_signal(ebit, revenue, ebitda, closeadj):
    d = _f36_drop_through(ebit, revenue, 10).clip(-100, 100)
    base_ = d * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxebitda_21d_5d_slope_v146_signal(ebit, revenue, ebitda, closeadj):
    d = _f36_drop_through(ebit, revenue, 21).clip(-100, 100)
    base_ = d * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxebitda_42d_21d_slope_v147_signal(ebit, revenue, ebitda, closeadj):
    d = _f36_drop_through(ebit, revenue, 42).clip(-100, 100)
    base_ = d * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxebitda_63d_63d_slope_v148_signal(ebit, revenue, ebitda, closeadj):
    d = _f36_drop_through(ebit, revenue, 63).clip(-100, 100)
    base_ = d * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxebitda_126d_126d_slope_v149_signal(ebit, revenue, ebitda, closeadj):
    d = _f36_drop_through(ebit, revenue, 126).clip(-100, 100)
    base_ = d * _safe_div(ebitda, revenue) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f36oli_f36_operating_leverage_intensity_dropthroughxebitda_189d_252d_slope_v150_signal(ebit, revenue, ebitda, closeadj):
    d = _f36_drop_through(ebit, revenue, 189).clip(-100, 100)
    base_ = d * _safe_div(ebitda, revenue) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f36oli_f36_operating_leverage_intensity_opleverage_5d_5d_slope_v001_signal,
    f36oli_f36_operating_leverage_intensity_opleverage_10d_21d_slope_v002_signal,
    f36oli_f36_operating_leverage_intensity_opleverage_21d_63d_slope_v003_signal,
    f36oli_f36_operating_leverage_intensity_opleverage_42d_126d_slope_v004_signal,
    f36oli_f36_operating_leverage_intensity_opleverage_63d_252d_slope_v005_signal,
    f36oli_f36_operating_leverage_intensity_opleverage_126d_5d_slope_v006_signal,
    f36oli_f36_operating_leverage_intensity_opleverage_189d_21d_slope_v007_signal,
    f36oli_f36_operating_leverage_intensity_opleverage_252d_63d_slope_v008_signal,
    f36oli_f36_operating_leverage_intensity_opleverage_378d_126d_slope_v009_signal,
    f36oli_f36_operating_leverage_intensity_opleverage_504d_252d_slope_v010_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_5d_5d_slope_v011_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_10d_21d_slope_v012_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_21d_63d_slope_v013_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_42d_126d_slope_v014_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_63d_252d_slope_v015_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_126d_5d_slope_v016_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_189d_21d_slope_v017_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_252d_63d_slope_v018_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_378d_126d_slope_v019_signal,
    f36oli_f36_operating_leverage_intensity_opleveragesm_504d_252d_slope_v020_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_5d_5d_slope_v021_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_10d_21d_slope_v022_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_21d_63d_slope_v023_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_42d_126d_slope_v024_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_63d_252d_slope_v025_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_126d_5d_slope_v026_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_189d_21d_slope_v027_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_252d_63d_slope_v028_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_378d_126d_slope_v029_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitda_504d_252d_slope_v030_signal,
    f36oli_f36_operating_leverage_intensity_marginbeta_63d_5d_slope_v031_signal,
    f36oli_f36_operating_leverage_intensity_marginbeta_126d_21d_slope_v032_signal,
    f36oli_f36_operating_leverage_intensity_marginbeta_189d_63d_slope_v033_signal,
    f36oli_f36_operating_leverage_intensity_marginbeta_252d_126d_slope_v034_signal,
    f36oli_f36_operating_leverage_intensity_marginbeta_378d_252d_slope_v035_signal,
    f36oli_f36_operating_leverage_intensity_marginbeta_504d_5d_slope_v036_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_5d_21d_slope_v037_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_10d_63d_slope_v038_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_21d_126d_slope_v039_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_42d_252d_slope_v040_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_63d_5d_slope_v041_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_126d_21d_slope_v042_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_189d_63d_slope_v043_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_252d_126d_slope_v044_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_378d_252d_slope_v045_signal,
    f36oli_f36_operating_leverage_intensity_dropthrough_504d_5d_slope_v046_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_5d_21d_slope_v047_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_10d_63d_slope_v048_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_21d_126d_slope_v049_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_42d_252d_slope_v050_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_63d_5d_slope_v051_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_126d_21d_slope_v052_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_189d_63d_slope_v053_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_252d_126d_slope_v054_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_378d_252d_slope_v055_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxrev_504d_5d_slope_v056_signal,
    f36oli_f36_operating_leverage_intensity_opleveragez_21d_in_252d_21d_slope_v057_signal,
    f36oli_f36_operating_leverage_intensity_opleveragez_63d_in_252d_63d_slope_v058_signal,
    f36oli_f36_operating_leverage_intensity_opleveragez_126d_in_252d_126d_slope_v059_signal,
    f36oli_f36_operating_leverage_intensity_opleveragez_21d_in_504d_252d_slope_v060_signal,
    f36oli_f36_operating_leverage_intensity_opleveragez_63d_in_504d_5d_slope_v061_signal,
    f36oli_f36_operating_leverage_intensity_opleveragez_126d_in_504d_21d_slope_v062_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_5d_63d_slope_v063_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_10d_126d_slope_v064_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_21d_252d_slope_v065_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_42d_5d_slope_v066_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_63d_21d_slope_v067_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_126d_63d_slope_v068_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_189d_126d_slope_v069_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_252d_252d_slope_v070_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_378d_5d_slope_v071_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughema_504d_21d_slope_v072_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_5d_63d_slope_v073_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_10d_126d_slope_v074_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_21d_252d_slope_v075_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_42d_5d_slope_v076_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_63d_21d_slope_v077_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_126d_63d_slope_v078_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_189d_126d_slope_v079_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_252d_252d_slope_v080_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_378d_5d_slope_v081_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebitratio_504d_21d_slope_v082_signal,
    f36oli_f36_operating_leverage_intensity_marginbetaxebit_63d_63d_slope_v083_signal,
    f36oli_f36_operating_leverage_intensity_marginbetaxebit_126d_126d_slope_v084_signal,
    f36oli_f36_operating_leverage_intensity_marginbetaxebit_189d_252d_slope_v085_signal,
    f36oli_f36_operating_leverage_intensity_marginbetaxebit_252d_5d_slope_v086_signal,
    f36oli_f36_operating_leverage_intensity_marginbetaxebit_378d_21d_slope_v087_signal,
    f36oli_f36_operating_leverage_intensity_marginbetaxebit_504d_63d_slope_v088_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughstd_63d_126d_slope_v089_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughstd_126d_252d_slope_v090_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughstd_189d_5d_slope_v091_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughstd_252d_21d_slope_v092_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughstd_378d_63d_slope_v093_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughstd_504d_126d_slope_v094_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_5d_252d_slope_v095_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_10d_5d_slope_v096_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_21d_21d_slope_v097_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_42d_63d_slope_v098_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_63d_126d_slope_v099_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_126d_252d_slope_v100_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_189d_5d_slope_v101_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_252d_21d_slope_v102_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_378d_63d_slope_v103_signal,
    f36oli_f36_operating_leverage_intensity_opleveragediff_504d_126d_slope_v104_signal,
    f36oli_f36_operating_leverage_intensity_marginbetasq_126d_252d_slope_v105_signal,
    f36oli_f36_operating_leverage_intensity_marginbetasq_189d_5d_slope_v106_signal,
    f36oli_f36_operating_leverage_intensity_marginbetasq_252d_21d_slope_v107_signal,
    f36oli_f36_operating_leverage_intensity_marginbetasq_378d_63d_slope_v108_signal,
    f36oli_f36_operating_leverage_intensity_marginbetasq_504d_126d_slope_v109_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_5d_252d_slope_v110_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_10d_5d_slope_v111_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_21d_21d_slope_v112_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_42d_63d_slope_v113_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_63d_126d_slope_v114_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_126d_252d_slope_v115_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_189d_5d_slope_v116_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_252d_21d_slope_v117_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_378d_63d_slope_v118_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughsign_504d_126d_slope_v119_signal,
    f36oli_f36_operating_leverage_intensity_opleverageratio_21v63_252d_slope_v120_signal,
    f36oli_f36_operating_leverage_intensity_opleverageratio_63v252_5d_slope_v121_signal,
    f36oli_f36_operating_leverage_intensity_opleverageratio_21v252_21d_slope_v122_signal,
    f36oli_f36_operating_leverage_intensity_opleverageratio_63v504_63d_slope_v123_signal,
    f36oli_f36_operating_leverage_intensity_opleverageratio_126v252_126d_slope_v124_signal,
    f36oli_f36_operating_leverage_intensity_opleverageratio_252v504_252d_slope_v125_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_5d_5d_slope_v126_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_10d_21d_slope_v127_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_21d_63d_slope_v128_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_42d_126d_slope_v129_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_63d_252d_slope_v130_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_126d_5d_slope_v131_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_189d_21d_slope_v132_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_252d_63d_slope_v133_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_378d_126d_slope_v134_signal,
    f36oli_f36_operating_leverage_intensity_opleveragexebmar_504d_252d_slope_v135_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughcross_21v63_5d_slope_v136_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughcross_63v252_21d_slope_v137_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughcross_252v504_63d_slope_v138_signal,
    f36oli_f36_operating_leverage_intensity_marginbetadiff_126d_126d_slope_v139_signal,
    f36oli_f36_operating_leverage_intensity_marginbetadiff_189d_252d_slope_v140_signal,
    f36oli_f36_operating_leverage_intensity_marginbetadiff_252d_5d_slope_v141_signal,
    f36oli_f36_operating_leverage_intensity_marginbetadiff_378d_21d_slope_v142_signal,
    f36oli_f36_operating_leverage_intensity_marginbetadiff_504d_63d_slope_v143_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxebitda_5d_126d_slope_v144_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxebitda_10d_252d_slope_v145_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxebitda_21d_5d_slope_v146_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxebitda_42d_21d_slope_v147_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxebitda_63d_63d_slope_v148_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxebitda_126d_126d_slope_v149_signal,
    f36oli_f36_operating_leverage_intensity_dropthroughxebitda_189d_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_OPERATING_LEVERAGE_INTENSITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f36_op_leverage_proxy", "_f36_margin_revenue_beta", "_f36_drop_through")
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
    print(f"OK f36_operating_leverage_intensity_2nd_derivatives_001_150_claude: {n_features} features pass")
