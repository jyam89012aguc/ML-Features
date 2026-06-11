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
def _f48_gp_lift(gp, revenue, w):
    gpr = gp / revenue.replace(0, np.nan)
    return gpr - gpr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f48_pricing_pass_through(grossmargin, cor, revenue, w):
    cost_intensity = cor / revenue.replace(0, np.nan)
    cost_change = cost_intensity.diff(w)
    margin_change = grossmargin.diff(w)
    return margin_change - (-cost_change)


def _f48_packaging_durability(grossmargin, ebitdamargin, w):
    gm_floor = grossmargin.rolling(w, min_periods=max(1, w // 2)).min()
    eb_floor = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    gm_mean = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    eb_mean = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return (gm_floor / gm_mean.replace(0, np.nan).abs()) + (eb_floor / eb_mean.replace(0, np.nan).abs())



def f48ppp_f48_packaging_pricing_power_gplift_21d_ema_base_v076_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_logp_base_v077_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_sq_base_v078_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_rank_base_v079_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_xebmar_base_v080_signal(gp, revenue, ebitdamargin, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_diff_base_v081_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_ema_base_v082_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = base.ewm(span=42, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_logp_base_v083_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_sq_base_v084_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_rank_base_v085_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_xebmar_base_v086_signal(gp, revenue, ebitdamargin, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_diff_base_v087_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = base.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_ema_base_v088_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = base.ewm(span=63, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_logp_base_v089_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_sq_base_v090_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_rank_base_v091_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_xebmar_base_v092_signal(gp, revenue, ebitdamargin, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_diff_base_v093_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_ema_base_v094_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = base.ewm(span=126, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_logp_base_v095_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_sq_base_v096_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_rank_base_v097_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_xebmar_base_v098_signal(gp, revenue, ebitdamargin, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_diff_base_v099_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_ema_base_v100_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = base.ewm(span=189, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_logp_base_v101_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_sq_base_v102_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_rank_base_v103_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_xebmar_base_v104_signal(gp, revenue, ebitdamargin, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_diff_base_v105_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = base.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_ema_base_v106_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = base.ewm(span=252, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_logp_base_v107_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_sq_base_v108_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_rank_base_v109_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_xebmar_base_v110_signal(gp, revenue, ebitdamargin, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_diff_base_v111_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = base.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_ema_base_v112_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = base.ewm(span=378, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_logp_base_v113_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_sq_base_v114_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_rank_base_v115_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_xebmar_base_v116_signal(gp, revenue, ebitdamargin, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_diff_base_v117_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = base.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_ema_base_v118_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = base.ewm(span=504, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_logp_base_v119_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_sq_base_v120_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_rank_base_v121_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_xebmar_base_v122_signal(gp, revenue, ebitdamargin, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_diff_base_v123_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = base.diff(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_ema_base_v124_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_logp_base_v125_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_sq_base_v126_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_rank_base_v127_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_xebmar_base_v128_signal(grossmargin, cor, revenue, ebitdamargin, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_diff_base_v129_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_ema_base_v130_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = base.ewm(span=42, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_logp_base_v131_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_sq_base_v132_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_rank_base_v133_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_xebmar_base_v134_signal(grossmargin, cor, revenue, ebitdamargin, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_diff_base_v135_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = base.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_ema_base_v136_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = base.ewm(span=63, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_logp_base_v137_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_sq_base_v138_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_rank_base_v139_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_xebmar_base_v140_signal(grossmargin, cor, revenue, ebitdamargin, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_diff_base_v141_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_ema_base_v142_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = base.ewm(span=126, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_logp_base_v143_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_sq_base_v144_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_rank_base_v145_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_xebmar_base_v146_signal(grossmargin, cor, revenue, ebitdamargin, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_diff_base_v147_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_189d_ema_base_v148_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 189)
    result = base.ewm(span=189, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_189d_logp_base_v149_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_189d_sq_base_v150_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 189)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48ppp_f48_packaging_pricing_power_gplift_21d_ema_base_v076_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_logp_base_v077_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_sq_base_v078_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_rank_base_v079_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_xebmar_base_v080_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_diff_base_v081_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_ema_base_v082_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_logp_base_v083_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_sq_base_v084_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_rank_base_v085_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_xebmar_base_v086_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_diff_base_v087_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_ema_base_v088_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_logp_base_v089_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_sq_base_v090_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_rank_base_v091_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_xebmar_base_v092_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_diff_base_v093_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_ema_base_v094_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_logp_base_v095_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_sq_base_v096_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_rank_base_v097_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_xebmar_base_v098_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_diff_base_v099_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_ema_base_v100_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_logp_base_v101_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_sq_base_v102_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_rank_base_v103_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_xebmar_base_v104_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_diff_base_v105_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_ema_base_v106_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_logp_base_v107_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_sq_base_v108_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_rank_base_v109_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_xebmar_base_v110_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_diff_base_v111_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_ema_base_v112_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_logp_base_v113_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_sq_base_v114_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_rank_base_v115_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_xebmar_base_v116_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_diff_base_v117_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_ema_base_v118_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_logp_base_v119_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_sq_base_v120_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_rank_base_v121_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_xebmar_base_v122_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_diff_base_v123_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_ema_base_v124_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_logp_base_v125_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_sq_base_v126_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_rank_base_v127_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_xebmar_base_v128_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_diff_base_v129_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_ema_base_v130_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_logp_base_v131_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_sq_base_v132_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_rank_base_v133_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_xebmar_base_v134_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_diff_base_v135_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_ema_base_v136_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_logp_base_v137_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_sq_base_v138_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_rank_base_v139_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_xebmar_base_v140_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_diff_base_v141_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_ema_base_v142_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_logp_base_v143_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_sq_base_v144_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_rank_base_v145_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_xebmar_base_v146_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_diff_base_v147_signal,
    f48ppp_f48_packaging_pricing_power_ppt_189d_ema_base_v148_signal,
    f48ppp_f48_packaging_pricing_power_ppt_189d_logp_base_v149_signal,
    f48ppp_f48_packaging_pricing_power_ppt_189d_sq_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_PACKAGING_PRICING_POWER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")

    cols = {"closeadj": closeadj, "cor": cor, "ebitdamargin": ebitdamargin, "gp": gp, "grossmargin": grossmargin, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_gp_lift", "_f48_pricing_pass_through", "_f48_packaging_durability")
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
    print(f"OK f48_packaging_pricing_power_base_076_150_claude: {n_features} features pass")
