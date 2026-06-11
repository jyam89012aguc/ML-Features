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
def _f19_revenue_sga_divergence(revenue, sgna, w):
    return revenue.pct_change(periods=w) - sgna.pct_change(periods=w)


def _f19_network_acceleration(revenue, sgna, w):
    rg = revenue.pct_change(periods=w)
    sg = sgna.pct_change(periods=w)
    div = rg - sg
    return div - div.rolling(w, min_periods=max(1, w // 2)).mean()


def _f19_scale_efficiency(revenue, sgna, w):
    r2s = revenue / sgna.replace(0, np.nan)
    return r2s - r2s.rolling(w, min_periods=max(1, w // 2)).mean()


def f19mne_f19_marketplace_network_effects_scaleff_z_189d_base_v076_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = _z(se, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_252d_base_v077_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = _z(se, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_z_378d_base_v078_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = _z(se, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_21d_base_v079_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = se * se.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_63d_base_v080_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = se * se.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_126d_base_v081_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = se * se.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_189d_base_v082_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = se * se.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_252d_base_v083_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = se * se.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_sq_378d_base_v084_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = se * se.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_21d_base_v085_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = _std(se, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_63d_base_v086_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = _std(se, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_126d_base_v087_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = _std(se, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_189d_base_v088_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = _std(se, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_252d_base_v089_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 252)
    base = _std(se, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_scaleff_rstd_378d_base_v090_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 378)
    base = _std(se, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_10d_base_v091_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 10)
    na = _f19_network_acceleration(revenue, sgna, 10)
    base = rd * na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_21d_base_v092_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = rd * na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_42d_base_v093_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 42)
    na = _f19_network_acceleration(revenue, sgna, 42)
    base = rd * na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_63d_base_v094_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = rd * na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_126d_base_v095_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = rd * na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdxna_mul_189d_base_v096_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = rd * na
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_10d_base_v097_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 10)
    se = _f19_scale_efficiency(revenue, sgna, 10)
    base = na + se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_21d_base_v098_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = na + se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_42d_base_v099_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 42)
    se = _f19_scale_efficiency(revenue, sgna, 42)
    base = na + se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_63d_base_v100_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = na + se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_126d_base_v101_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = na + se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_napse_sum_189d_base_v102_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = na + se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_10d_base_v103_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 10)
    se = _f19_scale_efficiency(revenue, sgna, 10)
    base = rd - se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_21d_base_v104_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = rd - se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_42d_base_v105_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 42)
    se = _f19_scale_efficiency(revenue, sgna, 42)
    base = rd - se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_63d_base_v106_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = rd - se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_126d_base_v107_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = rd - se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rdmse_diff_189d_base_v108_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = rd - se
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_10d_base_v109_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 10)
    base = _mean(na, 10) * opex / opex.replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_21d_base_v110_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = _mean(na, 21) * opex / opex.replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_42d_base_v111_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 42)
    base = _mean(na, 42) * opex / opex.replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_63d_base_v112_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = _mean(na, 63) * opex / opex.replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_126d_base_v113_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = _mean(na, 126) * opex / opex.replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_opx_189d_base_v114_signal(revenue, sgna, opex, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = _mean(na, 189) * opex / opex.replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_10d_base_v115_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 10)
    base = rd.diff(10).rolling(10, min_periods=max(1,10//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_21d_base_v116_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = rd.diff(21).rolling(21, min_periods=max(1,21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_42d_base_v117_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 42)
    base = rd.diff(42).rolling(42, min_periods=max(1,42//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_63d_base_v118_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = rd.diff(63).rolling(63, min_periods=max(1,63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_126d_base_v119_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = rd.diff(126).rolling(126, min_periods=max(1,126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dsmooth_189d_base_v120_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = rd.diff(189).rolling(189, min_periods=max(1,189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_10d_base_v121_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 10)
    base = na.ewm(span=10, min_periods=max(1, 10//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_21d_base_v122_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na.ewm(span=21, min_periods=max(1, 21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_42d_base_v123_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 42)
    base = na.ewm(span=42, min_periods=max(1, 42//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_63d_base_v124_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na.ewm(span=63, min_periods=max(1, 63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_126d_base_v125_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na.ewm(span=126, min_periods=max(1, 126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_ema_189d_base_v126_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na.ewm(span=189, min_periods=max(1, 189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_10d_base_v127_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 10)
    base = se.rolling(10, min_periods=max(1, 10//2)).max() - se.rolling(10, min_periods=max(1, 10//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_21d_base_v128_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = se.rolling(21, min_periods=max(1, 21//2)).max() - se.rolling(21, min_periods=max(1, 21//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_42d_base_v129_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 42)
    base = se.rolling(42, min_periods=max(1, 42//2)).max() - se.rolling(42, min_periods=max(1, 42//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_63d_base_v130_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = se.rolling(63, min_periods=max(1, 63//2)).max() - se.rolling(63, min_periods=max(1, 63//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_126d_base_v131_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = se.rolling(126, min_periods=max(1, 126//2)).max() - se.rolling(126, min_periods=max(1, 126//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_range_189d_base_v132_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = se.rolling(189, min_periods=max(1, 189//2)).max() - se.rolling(189, min_periods=max(1, 189//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_10d_base_v133_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 10)
    base = (rd - rd.rolling(10, min_periods=max(1, 10//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_21d_base_v134_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 21)
    base = (rd - rd.rolling(21, min_periods=max(1, 21//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_42d_base_v135_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 42)
    base = (rd - rd.rolling(42, min_periods=max(1, 42//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_63d_base_v136_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 63)
    base = (rd - rd.rolling(63, min_periods=max(1, 63//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_126d_base_v137_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 126)
    base = (rd - rd.rolling(126, min_periods=max(1, 126//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_rd_dmed_189d_base_v138_signal(revenue, sgna, closeadj):
    rd = _f19_revenue_sga_divergence(revenue, sgna, 189)
    base = (rd - rd.rolling(189, min_periods=max(1, 189//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_10d_base_v139_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 10)
    base = na.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - na.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_21d_base_v140_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 21)
    base = na.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - na.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_42d_base_v141_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 42)
    base = na.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - na.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_63d_base_v142_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 63)
    base = na.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - na.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_126d_base_v143_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 126)
    base = na.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - na.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_na_iqr_189d_base_v144_signal(revenue, sgna, closeadj):
    na = _f19_network_acceleration(revenue, sgna, 189)
    base = na.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - na.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_10d_base_v145_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 10)
    base = se.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - se.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_21d_base_v146_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 21)
    base = se.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - se.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_42d_base_v147_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 42)
    base = se.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - se.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_63d_base_v148_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 63)
    base = se.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - se.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_126d_base_v149_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 126)
    base = se.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - se.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19mne_f19_marketplace_network_effects_se_iqr_189d_base_v150_signal(revenue, sgna, closeadj):
    se = _f19_scale_efficiency(revenue, sgna, 189)
    base = se.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - se.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19mne_f19_marketplace_network_effects_scaleff_z_189d_base_v076_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_252d_base_v077_signal,
    f19mne_f19_marketplace_network_effects_scaleff_z_378d_base_v078_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_21d_base_v079_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_63d_base_v080_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_126d_base_v081_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_189d_base_v082_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_252d_base_v083_signal,
    f19mne_f19_marketplace_network_effects_scaleff_sq_378d_base_v084_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_21d_base_v085_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_63d_base_v086_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_126d_base_v087_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_189d_base_v088_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_252d_base_v089_signal,
    f19mne_f19_marketplace_network_effects_scaleff_rstd_378d_base_v090_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_10d_base_v091_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_21d_base_v092_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_42d_base_v093_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_63d_base_v094_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_126d_base_v095_signal,
    f19mne_f19_marketplace_network_effects_rdxna_mul_189d_base_v096_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_10d_base_v097_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_21d_base_v098_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_42d_base_v099_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_63d_base_v100_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_126d_base_v101_signal,
    f19mne_f19_marketplace_network_effects_napse_sum_189d_base_v102_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_10d_base_v103_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_21d_base_v104_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_42d_base_v105_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_63d_base_v106_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_126d_base_v107_signal,
    f19mne_f19_marketplace_network_effects_rdmse_diff_189d_base_v108_signal,
    f19mne_f19_marketplace_network_effects_na_opx_10d_base_v109_signal,
    f19mne_f19_marketplace_network_effects_na_opx_21d_base_v110_signal,
    f19mne_f19_marketplace_network_effects_na_opx_42d_base_v111_signal,
    f19mne_f19_marketplace_network_effects_na_opx_63d_base_v112_signal,
    f19mne_f19_marketplace_network_effects_na_opx_126d_base_v113_signal,
    f19mne_f19_marketplace_network_effects_na_opx_189d_base_v114_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_10d_base_v115_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_21d_base_v116_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_42d_base_v117_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_63d_base_v118_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_126d_base_v119_signal,
    f19mne_f19_marketplace_network_effects_rd_dsmooth_189d_base_v120_signal,
    f19mne_f19_marketplace_network_effects_na_ema_10d_base_v121_signal,
    f19mne_f19_marketplace_network_effects_na_ema_21d_base_v122_signal,
    f19mne_f19_marketplace_network_effects_na_ema_42d_base_v123_signal,
    f19mne_f19_marketplace_network_effects_na_ema_63d_base_v124_signal,
    f19mne_f19_marketplace_network_effects_na_ema_126d_base_v125_signal,
    f19mne_f19_marketplace_network_effects_na_ema_189d_base_v126_signal,
    f19mne_f19_marketplace_network_effects_se_range_10d_base_v127_signal,
    f19mne_f19_marketplace_network_effects_se_range_21d_base_v128_signal,
    f19mne_f19_marketplace_network_effects_se_range_42d_base_v129_signal,
    f19mne_f19_marketplace_network_effects_se_range_63d_base_v130_signal,
    f19mne_f19_marketplace_network_effects_se_range_126d_base_v131_signal,
    f19mne_f19_marketplace_network_effects_se_range_189d_base_v132_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_10d_base_v133_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_21d_base_v134_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_42d_base_v135_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_63d_base_v136_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_126d_base_v137_signal,
    f19mne_f19_marketplace_network_effects_rd_dmed_189d_base_v138_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_10d_base_v139_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_21d_base_v140_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_42d_base_v141_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_63d_base_v142_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_126d_base_v143_signal,
    f19mne_f19_marketplace_network_effects_na_iqr_189d_base_v144_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_10d_base_v145_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_21d_base_v146_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_42d_base_v147_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_63d_base_v148_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_126d_base_v149_signal,
    f19mne_f19_marketplace_network_effects_se_iqr_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FMARKETPLACE_NETWORK_EFFECTS_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f19_revenue_sga_divergence", "_f19_network_acceleration", "_f19_scale_efficiency",)
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
    print(f"OK f19_marketplace_network_effects_base_076_150_claude: {n_features} features pass")
