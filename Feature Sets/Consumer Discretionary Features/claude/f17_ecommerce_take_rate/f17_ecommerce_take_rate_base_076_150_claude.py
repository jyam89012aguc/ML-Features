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
def _f17_take_rate_proxy(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f17_take_rate_trend(grossmargin, w):
    return grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()


def _f17_take_rate_uplift(gp, revenue, w):
    tr = gp / revenue.replace(0, np.nan)
    return tr - tr.rolling(w, min_periods=max(1, w // 2)).mean()


def f17etr_f17_ecommerce_take_rate_truplift_z_189d_base_v076_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = _z(tu, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_252d_base_v077_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = _z(tu, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_378d_base_v078_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = _z(tu, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_21d_base_v079_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tu * tu.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_63d_base_v080_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tu * tu.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_126d_base_v081_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tu * tu.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_189d_base_v082_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tu * tu.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_252d_base_v083_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = tu * tu.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_378d_base_v084_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = tu * tu.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_21d_base_v085_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = _std(tu, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_63d_base_v086_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = _std(tu, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_126d_base_v087_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = _std(tu, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_189d_base_v088_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = _std(tu, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_252d_base_v089_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = _std(tu, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_378d_base_v090_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = _std(tu, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_10d_base_v091_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = tr * tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_21d_base_v092_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tr * tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_42d_base_v093_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = tr * tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_63d_base_v094_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tr * tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_126d_base_v095_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tr * tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_189d_base_v096_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tr * tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_10d_base_v097_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 10)
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = tt + tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_21d_base_v098_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tt + tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_42d_base_v099_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 42)
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = tt + tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_63d_base_v100_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tt + tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_126d_base_v101_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tt + tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_189d_base_v102_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tt + tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_10d_base_v103_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 10)
    base = tr - tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_21d_base_v104_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tr - tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_42d_base_v105_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 42)
    base = tr - tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_63d_base_v106_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tr - tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_126d_base_v107_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tr - tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_189d_base_v108_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tr - tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_10d_base_v109_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = _mean(tu, 10) * _std(tu, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_21d_base_v110_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = _mean(tu, 21) * _std(tu, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_42d_base_v111_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = _mean(tu, 42) * _std(tu, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_63d_base_v112_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = _mean(tu, 63) * _std(tu, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_126d_base_v113_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = _mean(tu, 126) * _std(tu, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_189d_base_v114_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = _mean(tu, 189) * _std(tu, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_10d_base_v115_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(10).rolling(10, min_periods=max(1,10//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_21d_base_v116_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(21).rolling(21, min_periods=max(1,21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_42d_base_v117_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(42).rolling(42, min_periods=max(1,42//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_63d_base_v118_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(63).rolling(63, min_periods=max(1,63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_126d_base_v119_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(126).rolling(126, min_periods=max(1,126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_189d_base_v120_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(189).rolling(189, min_periods=max(1,189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_10d_base_v121_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 10)
    base = tt.ewm(span=10, min_periods=max(1, 10//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_21d_base_v122_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt.ewm(span=21, min_periods=max(1, 21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_42d_base_v123_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 42)
    base = tt.ewm(span=42, min_periods=max(1, 42//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_63d_base_v124_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt.ewm(span=63, min_periods=max(1, 63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_126d_base_v125_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt.ewm(span=126, min_periods=max(1, 126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_189d_base_v126_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt.ewm(span=189, min_periods=max(1, 189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_10d_base_v127_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = tu.rolling(10, min_periods=max(1, 10//2)).max() - tu.rolling(10, min_periods=max(1, 10//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_21d_base_v128_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tu.rolling(21, min_periods=max(1, 21//2)).max() - tu.rolling(21, min_periods=max(1, 21//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_42d_base_v129_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = tu.rolling(42, min_periods=max(1, 42//2)).max() - tu.rolling(42, min_periods=max(1, 42//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_63d_base_v130_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tu.rolling(63, min_periods=max(1, 63//2)).max() - tu.rolling(63, min_periods=max(1, 63//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_126d_base_v131_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tu.rolling(126, min_periods=max(1, 126//2)).max() - tu.rolling(126, min_periods=max(1, 126//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_189d_base_v132_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tu.rolling(189, min_periods=max(1, 189//2)).max() - tu.rolling(189, min_periods=max(1, 189//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_10d_base_v133_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(10, min_periods=max(1, 10//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_21d_base_v134_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(21, min_periods=max(1, 21//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_42d_base_v135_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(42, min_periods=max(1, 42//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_63d_base_v136_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(63, min_periods=max(1, 63//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_126d_base_v137_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(126, min_periods=max(1, 126//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_189d_base_v138_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(189, min_periods=max(1, 189//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_10d_base_v139_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 10)
    base = tt.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - tt.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_21d_base_v140_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - tt.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_42d_base_v141_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 42)
    base = tt.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - tt.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_63d_base_v142_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - tt.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_126d_base_v143_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - tt.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_189d_base_v144_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - tt.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_10d_base_v145_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = tu.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - tu.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_21d_base_v146_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tu.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - tu.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_42d_base_v147_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = tu.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - tu.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_63d_base_v148_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tu.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - tu.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_126d_base_v149_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tu.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - tu.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_189d_base_v150_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tu.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - tu.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17etr_f17_ecommerce_take_rate_truplift_z_189d_base_v076_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_252d_base_v077_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_378d_base_v078_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_21d_base_v079_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_63d_base_v080_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_126d_base_v081_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_189d_base_v082_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_252d_base_v083_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_378d_base_v084_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_21d_base_v085_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_63d_base_v086_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_126d_base_v087_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_189d_base_v088_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_252d_base_v089_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_378d_base_v090_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_10d_base_v091_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_21d_base_v092_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_42d_base_v093_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_63d_base_v094_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_126d_base_v095_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_189d_base_v096_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_10d_base_v097_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_21d_base_v098_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_42d_base_v099_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_63d_base_v100_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_126d_base_v101_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_189d_base_v102_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_10d_base_v103_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_21d_base_v104_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_42d_base_v105_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_63d_base_v106_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_126d_base_v107_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_189d_base_v108_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_10d_base_v109_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_21d_base_v110_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_42d_base_v111_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_63d_base_v112_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_126d_base_v113_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_189d_base_v114_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_10d_base_v115_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_21d_base_v116_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_42d_base_v117_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_63d_base_v118_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_126d_base_v119_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_189d_base_v120_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_10d_base_v121_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_21d_base_v122_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_42d_base_v123_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_63d_base_v124_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_126d_base_v125_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_189d_base_v126_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_10d_base_v127_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_21d_base_v128_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_42d_base_v129_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_63d_base_v130_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_126d_base_v131_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_189d_base_v132_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_10d_base_v133_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_21d_base_v134_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_42d_base_v135_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_63d_base_v136_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_126d_base_v137_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_189d_base_v138_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_10d_base_v139_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_21d_base_v140_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_42d_base_v141_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_63d_base_v142_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_126d_base_v143_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_189d_base_v144_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_10d_base_v145_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_21d_base_v146_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_42d_base_v147_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_63d_base_v148_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_126d_base_v149_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FECOMMERCE_TAKE_RATE_REGISTRY_076_150 = REGISTRY


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
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "sgna": sgna, "opex": opex,
        "gp": gp, "workingcapital": workingcapital,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f17_take_rate_proxy", "_f17_take_rate_trend", "_f17_take_rate_uplift",)
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
    print(f"OK f17_ecommerce_take_rate_base_076_150_claude: {n_features} features pass")
