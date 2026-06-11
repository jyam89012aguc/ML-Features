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


def _logp(s):
    return np.log(s.replace(0, np.nan).abs() + 1e-12)


# ===== folder domain primitives =====
def _f13_backlog_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f13_backlog_to_revenue(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan).abs()


def _f13_backlog_acceleration(deferredrev, w):
    g = deferredrev.pct_change(periods=w)
    return g.diff(periods=w)


def f13obg_f13_ofs_backlog_growth_btr_std_126d_base_v076_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_std_189d_base_v077_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_std_252d_base_v078_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_std_378d_base_v079_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_std_504d_base_v080_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_5d_base_v081_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_10d_base_v082_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_21d_base_v083_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_42d_base_v084_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_63d_base_v085_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_126d_base_v086_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_189d_base_v087_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_252d_base_v088_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_378d_base_v089_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_diff_504d_base_v090_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.diff(periods=504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_5d_base_v091_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_10d_base_v092_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_21d_base_v093_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_42d_base_v094_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_63d_base_v095_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_126d_base_v096_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_189d_base_v097_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_252d_base_v098_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_378d_base_v099_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_pct_504d_base_v100_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = base.pct_change(periods=504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_5d_base_v101_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_10d_base_v102_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_21d_base_v103_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_42d_base_v104_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_63d_base_v105_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_126d_base_v106_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_189d_base_v107_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_252d_base_v108_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_378d_base_v109_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_504d_base_v110_signal(deferredrev, closeadj):
    result = _f13_backlog_acceleration(deferredrev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_5d_base_v111_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 5)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_10d_base_v112_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_21d_base_v113_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_42d_base_v114_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_63d_base_v115_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_126d_base_v116_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_189d_base_v117_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_252d_base_v118_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_378d_base_v119_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_mean_504d_base_v120_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_5d_base_v121_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_10d_base_v122_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_21d_base_v123_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_42d_base_v124_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_63d_base_v125_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_126d_base_v126_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_189d_base_v127_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_252d_base_v128_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_378d_base_v129_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_ba_std_504d_base_v130_signal(deferredrev, closeadj):
    base = _f13_backlog_acceleration(deferredrev, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_5d_base_v131_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 5)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_10d_base_v132_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 10)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_21d_base_v133_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 21)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_42d_base_v134_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 42)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_63d_base_v135_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 63)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_126d_base_v136_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 126)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_189d_base_v137_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 189)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_252d_base_v138_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 252)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_378d_base_v139_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 378)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_bg_log_504d_base_v140_signal(deferredrev, closeadj):
    base = _f13_backlog_growth(deferredrev, 504)
    result = _logp(base.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_5d_base_v141_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_10d_base_v142_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_21d_base_v143_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_42d_base_v144_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_63d_base_v145_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_126d_base_v146_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_189d_base_v147_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_252d_base_v148_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_378d_base_v149_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13obg_f13_ofs_backlog_growth_btr_ema_504d_base_v150_signal(deferredrev, revenue, closeadj):
    base = _f13_backlog_to_revenue(deferredrev, revenue)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13obg_f13_ofs_backlog_growth_btr_std_126d_base_v076_signal,
    f13obg_f13_ofs_backlog_growth_btr_std_189d_base_v077_signal,
    f13obg_f13_ofs_backlog_growth_btr_std_252d_base_v078_signal,
    f13obg_f13_ofs_backlog_growth_btr_std_378d_base_v079_signal,
    f13obg_f13_ofs_backlog_growth_btr_std_504d_base_v080_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_5d_base_v081_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_10d_base_v082_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_21d_base_v083_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_42d_base_v084_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_63d_base_v085_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_126d_base_v086_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_189d_base_v087_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_252d_base_v088_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_378d_base_v089_signal,
    f13obg_f13_ofs_backlog_growth_btr_diff_504d_base_v090_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_5d_base_v091_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_10d_base_v092_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_21d_base_v093_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_42d_base_v094_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_63d_base_v095_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_126d_base_v096_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_189d_base_v097_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_252d_base_v098_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_378d_base_v099_signal,
    f13obg_f13_ofs_backlog_growth_btr_pct_504d_base_v100_signal,
    f13obg_f13_ofs_backlog_growth_ba_5d_base_v101_signal,
    f13obg_f13_ofs_backlog_growth_ba_10d_base_v102_signal,
    f13obg_f13_ofs_backlog_growth_ba_21d_base_v103_signal,
    f13obg_f13_ofs_backlog_growth_ba_42d_base_v104_signal,
    f13obg_f13_ofs_backlog_growth_ba_63d_base_v105_signal,
    f13obg_f13_ofs_backlog_growth_ba_126d_base_v106_signal,
    f13obg_f13_ofs_backlog_growth_ba_189d_base_v107_signal,
    f13obg_f13_ofs_backlog_growth_ba_252d_base_v108_signal,
    f13obg_f13_ofs_backlog_growth_ba_378d_base_v109_signal,
    f13obg_f13_ofs_backlog_growth_ba_504d_base_v110_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_5d_base_v111_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_10d_base_v112_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_21d_base_v113_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_42d_base_v114_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_63d_base_v115_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_126d_base_v116_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_189d_base_v117_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_252d_base_v118_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_378d_base_v119_signal,
    f13obg_f13_ofs_backlog_growth_ba_mean_504d_base_v120_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_5d_base_v121_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_10d_base_v122_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_21d_base_v123_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_42d_base_v124_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_63d_base_v125_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_126d_base_v126_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_189d_base_v127_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_252d_base_v128_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_378d_base_v129_signal,
    f13obg_f13_ofs_backlog_growth_ba_std_504d_base_v130_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_5d_base_v131_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_10d_base_v132_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_21d_base_v133_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_42d_base_v134_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_63d_base_v135_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_126d_base_v136_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_189d_base_v137_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_252d_base_v138_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_378d_base_v139_signal,
    f13obg_f13_ofs_backlog_growth_bg_log_504d_base_v140_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_5d_base_v141_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_10d_base_v142_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_21d_base_v143_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_42d_base_v144_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_63d_base_v145_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_126d_base_v146_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_189d_base_v147_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_252d_base_v148_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_378d_base_v149_signal,
    f13obg_f13_ofs_backlog_growth_btr_ema_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_OFS_BACKLOG_GROWTH_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f13_backlog_growth", "_f13_backlog_to_revenue", "_f13_backlog_acceleration",)
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
    print(f"OK f13_ofs_backlog_growth_base_076_150_claude: {n_features} features pass")
