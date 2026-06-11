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
def _f18_sga_to_revenue(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f18_cac_efficiency(sgna, revenue, w):
    rg = revenue.pct_change(periods=w)
    sg = sgna.pct_change(periods=w)
    return rg - sg


def _f18_marketing_leverage(sgna, revenue, w):
    s2r = sgna / revenue.replace(0, np.nan)
    return s2r - s2r.rolling(w, min_periods=max(1, w // 2)).mean()


def f18dce_f18_digital_cac_efficiency_mktlev_z_189d_base_v076_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = _z(ml, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_252d_base_v077_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = _z(ml, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_378d_base_v078_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = _z(ml, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_21d_base_v079_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ml * ml.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_63d_base_v080_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ml * ml.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_126d_base_v081_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ml * ml.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_189d_base_v082_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ml * ml.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_252d_base_v083_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = ml * ml.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_378d_base_v084_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = ml * ml.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_21d_base_v085_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = _std(ml, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_63d_base_v086_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = _std(ml, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_126d_base_v087_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = _std(ml, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_189d_base_v088_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = _std(ml, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_252d_base_v089_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = _std(ml, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_378d_base_v090_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = _std(ml, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_10d_base_v091_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    base = s2r * ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_21d_base_v092_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = s2r * ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_42d_base_v093_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    base = s2r * ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_63d_base_v094_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = s2r * ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_126d_base_v095_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = s2r * ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_189d_base_v096_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = s2r * ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_10d_base_v097_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    ml = _f18_marketing_leverage(sgna, revenue, 10)
    base = ce - ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_21d_base_v098_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ce - ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_42d_base_v099_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    ml = _f18_marketing_leverage(sgna, revenue, 42)
    base = ce - ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_63d_base_v100_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ce - ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_126d_base_v101_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ce - ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_189d_base_v102_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ce - ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_10d_base_v103_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 10)
    base = s2r + ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_21d_base_v104_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = s2r + ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_42d_base_v105_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 42)
    base = s2r + ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_63d_base_v106_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = s2r + ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_126d_base_v107_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = s2r + ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_189d_base_v108_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = s2r + ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_10d_base_v109_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    base = _mean(ce, 10) - _std(ce, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_21d_base_v110_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = _mean(ce, 21) - _std(ce, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_42d_base_v111_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    base = _mean(ce, 42) - _std(ce, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_63d_base_v112_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = _mean(ce, 63) - _std(ce, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_126d_base_v113_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = _mean(ce, 126) - _std(ce, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_189d_base_v114_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = _mean(ce, 189) - _std(ce, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_10d_base_v115_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(10).rolling(10, min_periods=max(1,10//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_21d_base_v116_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(21).rolling(21, min_periods=max(1,21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_42d_base_v117_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(42).rolling(42, min_periods=max(1,42//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_63d_base_v118_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(63).rolling(63, min_periods=max(1,63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_126d_base_v119_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(126).rolling(126, min_periods=max(1,126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_189d_base_v120_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(189).rolling(189, min_periods=max(1,189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_10d_base_v121_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    base = ce.ewm(span=10, min_periods=max(1, 10//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_21d_base_v122_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce.ewm(span=21, min_periods=max(1, 21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_42d_base_v123_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    base = ce.ewm(span=42, min_periods=max(1, 42//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_63d_base_v124_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce.ewm(span=63, min_periods=max(1, 63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_126d_base_v125_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce.ewm(span=126, min_periods=max(1, 126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_189d_base_v126_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce.ewm(span=189, min_periods=max(1, 189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_10d_base_v127_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 10)
    base = ml.rolling(10, min_periods=max(1, 10//2)).max() - ml.rolling(10, min_periods=max(1, 10//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_21d_base_v128_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ml.rolling(21, min_periods=max(1, 21//2)).max() - ml.rolling(21, min_periods=max(1, 21//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_42d_base_v129_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 42)
    base = ml.rolling(42, min_periods=max(1, 42//2)).max() - ml.rolling(42, min_periods=max(1, 42//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_63d_base_v130_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ml.rolling(63, min_periods=max(1, 63//2)).max() - ml.rolling(63, min_periods=max(1, 63//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_126d_base_v131_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ml.rolling(126, min_periods=max(1, 126//2)).max() - ml.rolling(126, min_periods=max(1, 126//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_189d_base_v132_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ml.rolling(189, min_periods=max(1, 189//2)).max() - ml.rolling(189, min_periods=max(1, 189//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_10d_base_v133_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(10, min_periods=max(1, 10//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_21d_base_v134_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(21, min_periods=max(1, 21//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_42d_base_v135_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(42, min_periods=max(1, 42//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_63d_base_v136_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(63, min_periods=max(1, 63//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_126d_base_v137_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(126, min_periods=max(1, 126//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_189d_base_v138_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(189, min_periods=max(1, 189//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_10d_base_v139_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    base = ce.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - ce.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_21d_base_v140_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - ce.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_42d_base_v141_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    base = ce.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - ce.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_63d_base_v142_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - ce.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_126d_base_v143_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - ce.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_189d_base_v144_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - ce.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_10d_base_v145_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 10)
    base = ml.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - ml.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_21d_base_v146_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ml.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - ml.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_42d_base_v147_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 42)
    base = ml.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - ml.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_63d_base_v148_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ml.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - ml.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_126d_base_v149_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ml.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - ml.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_189d_base_v150_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ml.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - ml.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18dce_f18_digital_cac_efficiency_mktlev_z_189d_base_v076_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_252d_base_v077_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_378d_base_v078_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_21d_base_v079_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_63d_base_v080_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_126d_base_v081_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_189d_base_v082_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_252d_base_v083_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_378d_base_v084_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_21d_base_v085_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_63d_base_v086_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_126d_base_v087_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_189d_base_v088_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_252d_base_v089_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_378d_base_v090_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_10d_base_v091_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_21d_base_v092_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_42d_base_v093_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_63d_base_v094_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_126d_base_v095_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_189d_base_v096_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_10d_base_v097_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_21d_base_v098_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_42d_base_v099_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_63d_base_v100_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_126d_base_v101_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_189d_base_v102_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_10d_base_v103_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_21d_base_v104_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_42d_base_v105_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_63d_base_v106_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_126d_base_v107_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_189d_base_v108_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_10d_base_v109_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_21d_base_v110_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_42d_base_v111_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_63d_base_v112_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_126d_base_v113_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_189d_base_v114_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_10d_base_v115_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_21d_base_v116_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_42d_base_v117_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_63d_base_v118_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_126d_base_v119_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_189d_base_v120_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_10d_base_v121_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_21d_base_v122_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_42d_base_v123_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_63d_base_v124_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_126d_base_v125_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_189d_base_v126_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_10d_base_v127_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_21d_base_v128_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_42d_base_v129_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_63d_base_v130_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_126d_base_v131_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_189d_base_v132_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_10d_base_v133_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_21d_base_v134_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_42d_base_v135_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_63d_base_v136_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_126d_base_v137_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_189d_base_v138_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_10d_base_v139_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_21d_base_v140_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_42d_base_v141_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_63d_base_v142_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_126d_base_v143_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_189d_base_v144_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_10d_base_v145_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_21d_base_v146_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_42d_base_v147_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_63d_base_v148_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_126d_base_v149_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FDIGITAL_CAC_EFFICIENCY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f18_sga_to_revenue", "_f18_cac_efficiency", "_f18_marketing_leverage",)
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
    print(f"OK f18_digital_cac_efficiency_base_076_150_claude: {n_features} features pass")
