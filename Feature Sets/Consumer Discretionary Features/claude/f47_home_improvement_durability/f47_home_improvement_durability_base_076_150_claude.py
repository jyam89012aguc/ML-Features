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
def _f47_revenue_floor(revenue, w):
    return revenue.rolling(w, min_periods=max(1, w // 2)).min() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f47_non_cyclical_share(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    mx = revenue.rolling(w, min_periods=max(1, w // 2)).max()
    return mn / mx.replace(0, np.nan)


def _f47_durability_score(revenue, ebitdamargin, w):
    floor = revenue.rolling(w, min_periods=max(1, w // 2)).min() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    mstable = 1.0 - ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std().fillna(0) / ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan).abs()
    return floor * mstable



def f47hid_f47_home_improvement_durability_floor_21d_ema_base_v076_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_logp_base_v077_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_sq_base_v078_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_rank_base_v079_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_xebmar_base_v080_signal(revenue, ebitdamargin, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_21d_diff_base_v081_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_ema_base_v082_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = base.ewm(span=42, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_logp_base_v083_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_sq_base_v084_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_rank_base_v085_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_xebmar_base_v086_signal(revenue, ebitdamargin, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_42d_diff_base_v087_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 42)
    result = base.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_ema_base_v088_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = base.ewm(span=63, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_logp_base_v089_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_sq_base_v090_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_rank_base_v091_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_xebmar_base_v092_signal(revenue, ebitdamargin, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_63d_diff_base_v093_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_ema_base_v094_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = base.ewm(span=126, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_logp_base_v095_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_sq_base_v096_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_rank_base_v097_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_xebmar_base_v098_signal(revenue, ebitdamargin, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_126d_diff_base_v099_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 126)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_ema_base_v100_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = base.ewm(span=189, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_logp_base_v101_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_sq_base_v102_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_rank_base_v103_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_xebmar_base_v104_signal(revenue, ebitdamargin, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_189d_diff_base_v105_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 189)
    result = base.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_ema_base_v106_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = base.ewm(span=252, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_logp_base_v107_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_sq_base_v108_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_rank_base_v109_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_xebmar_base_v110_signal(revenue, ebitdamargin, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_252d_diff_base_v111_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 252)
    result = base.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_ema_base_v112_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = base.ewm(span=378, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_logp_base_v113_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_sq_base_v114_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_rank_base_v115_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_xebmar_base_v116_signal(revenue, ebitdamargin, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_378d_diff_base_v117_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 378)
    result = base.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_ema_base_v118_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = base.ewm(span=504, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_logp_base_v119_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_sq_base_v120_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_rank_base_v121_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_xebmar_base_v122_signal(revenue, ebitdamargin, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_floor_504d_diff_base_v123_signal(revenue, closeadj):
    base = _f47_revenue_floor(revenue, 504)
    result = base.diff(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_ema_base_v124_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_logp_base_v125_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_sq_base_v126_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_rank_base_v127_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_xebmar_base_v128_signal(revenue, ebitdamargin, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_21d_diff_base_v129_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_ema_base_v130_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = base.ewm(span=42, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_logp_base_v131_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_sq_base_v132_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_rank_base_v133_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_xebmar_base_v134_signal(revenue, ebitdamargin, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_42d_diff_base_v135_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 42)
    result = base.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_ema_base_v136_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = base.ewm(span=63, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_logp_base_v137_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_sq_base_v138_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_rank_base_v139_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_xebmar_base_v140_signal(revenue, ebitdamargin, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_63d_diff_base_v141_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_ema_base_v142_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = base.ewm(span=126, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_logp_base_v143_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_sq_base_v144_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_rank_base_v145_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_xebmar_base_v146_signal(revenue, ebitdamargin, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = base * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_126d_diff_base_v147_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 126)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_189d_ema_base_v148_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 189)
    result = base.ewm(span=189, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_189d_logp_base_v149_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47hid_f47_home_improvement_durability_ncshare_189d_sq_base_v150_signal(revenue, closeadj):
    base = _f47_non_cyclical_share(revenue, 189)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47hid_f47_home_improvement_durability_floor_21d_ema_base_v076_signal,
    f47hid_f47_home_improvement_durability_floor_21d_logp_base_v077_signal,
    f47hid_f47_home_improvement_durability_floor_21d_sq_base_v078_signal,
    f47hid_f47_home_improvement_durability_floor_21d_rank_base_v079_signal,
    f47hid_f47_home_improvement_durability_floor_21d_xebmar_base_v080_signal,
    f47hid_f47_home_improvement_durability_floor_21d_diff_base_v081_signal,
    f47hid_f47_home_improvement_durability_floor_42d_ema_base_v082_signal,
    f47hid_f47_home_improvement_durability_floor_42d_logp_base_v083_signal,
    f47hid_f47_home_improvement_durability_floor_42d_sq_base_v084_signal,
    f47hid_f47_home_improvement_durability_floor_42d_rank_base_v085_signal,
    f47hid_f47_home_improvement_durability_floor_42d_xebmar_base_v086_signal,
    f47hid_f47_home_improvement_durability_floor_42d_diff_base_v087_signal,
    f47hid_f47_home_improvement_durability_floor_63d_ema_base_v088_signal,
    f47hid_f47_home_improvement_durability_floor_63d_logp_base_v089_signal,
    f47hid_f47_home_improvement_durability_floor_63d_sq_base_v090_signal,
    f47hid_f47_home_improvement_durability_floor_63d_rank_base_v091_signal,
    f47hid_f47_home_improvement_durability_floor_63d_xebmar_base_v092_signal,
    f47hid_f47_home_improvement_durability_floor_63d_diff_base_v093_signal,
    f47hid_f47_home_improvement_durability_floor_126d_ema_base_v094_signal,
    f47hid_f47_home_improvement_durability_floor_126d_logp_base_v095_signal,
    f47hid_f47_home_improvement_durability_floor_126d_sq_base_v096_signal,
    f47hid_f47_home_improvement_durability_floor_126d_rank_base_v097_signal,
    f47hid_f47_home_improvement_durability_floor_126d_xebmar_base_v098_signal,
    f47hid_f47_home_improvement_durability_floor_126d_diff_base_v099_signal,
    f47hid_f47_home_improvement_durability_floor_189d_ema_base_v100_signal,
    f47hid_f47_home_improvement_durability_floor_189d_logp_base_v101_signal,
    f47hid_f47_home_improvement_durability_floor_189d_sq_base_v102_signal,
    f47hid_f47_home_improvement_durability_floor_189d_rank_base_v103_signal,
    f47hid_f47_home_improvement_durability_floor_189d_xebmar_base_v104_signal,
    f47hid_f47_home_improvement_durability_floor_189d_diff_base_v105_signal,
    f47hid_f47_home_improvement_durability_floor_252d_ema_base_v106_signal,
    f47hid_f47_home_improvement_durability_floor_252d_logp_base_v107_signal,
    f47hid_f47_home_improvement_durability_floor_252d_sq_base_v108_signal,
    f47hid_f47_home_improvement_durability_floor_252d_rank_base_v109_signal,
    f47hid_f47_home_improvement_durability_floor_252d_xebmar_base_v110_signal,
    f47hid_f47_home_improvement_durability_floor_252d_diff_base_v111_signal,
    f47hid_f47_home_improvement_durability_floor_378d_ema_base_v112_signal,
    f47hid_f47_home_improvement_durability_floor_378d_logp_base_v113_signal,
    f47hid_f47_home_improvement_durability_floor_378d_sq_base_v114_signal,
    f47hid_f47_home_improvement_durability_floor_378d_rank_base_v115_signal,
    f47hid_f47_home_improvement_durability_floor_378d_xebmar_base_v116_signal,
    f47hid_f47_home_improvement_durability_floor_378d_diff_base_v117_signal,
    f47hid_f47_home_improvement_durability_floor_504d_ema_base_v118_signal,
    f47hid_f47_home_improvement_durability_floor_504d_logp_base_v119_signal,
    f47hid_f47_home_improvement_durability_floor_504d_sq_base_v120_signal,
    f47hid_f47_home_improvement_durability_floor_504d_rank_base_v121_signal,
    f47hid_f47_home_improvement_durability_floor_504d_xebmar_base_v122_signal,
    f47hid_f47_home_improvement_durability_floor_504d_diff_base_v123_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_ema_base_v124_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_logp_base_v125_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_sq_base_v126_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_rank_base_v127_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_xebmar_base_v128_signal,
    f47hid_f47_home_improvement_durability_ncshare_21d_diff_base_v129_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_ema_base_v130_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_logp_base_v131_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_sq_base_v132_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_rank_base_v133_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_xebmar_base_v134_signal,
    f47hid_f47_home_improvement_durability_ncshare_42d_diff_base_v135_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_ema_base_v136_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_logp_base_v137_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_sq_base_v138_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_rank_base_v139_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_xebmar_base_v140_signal,
    f47hid_f47_home_improvement_durability_ncshare_63d_diff_base_v141_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_ema_base_v142_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_logp_base_v143_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_sq_base_v144_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_rank_base_v145_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_xebmar_base_v146_signal,
    f47hid_f47_home_improvement_durability_ncshare_126d_diff_base_v147_signal,
    f47hid_f47_home_improvement_durability_ncshare_189d_ema_base_v148_signal,
    f47hid_f47_home_improvement_durability_ncshare_189d_logp_base_v149_signal,
    f47hid_f47_home_improvement_durability_ncshare_189d_sq_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_HOME_IMPROVEMENT_DURABILITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {"closeadj": closeadj, "ebitdamargin": ebitdamargin, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_revenue_floor", "_f47_non_cyclical_share", "_f47_durability_score")
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
    print(f"OK f47_home_improvement_durability_base_076_150_claude: {n_features} features pass")
