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
def _f49_deferred_rev_quality(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


def _f49_subscription_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f49_subscription_durability(deferredrev, revenue, w):
    ratio = deferredrev / revenue.replace(0, np.nan)
    mean = ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    std = ratio.rolling(w, min_periods=max(1, w // 2)).std()
    return mean / std.replace(0, np.nan)



def f49psq_f49_publishing_subscription_quality_drq_21d_ema_base_v076_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_21d_logp_base_v077_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_21d_sq_base_v078_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_21d_rank_base_v079_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_21d_xrev_base_v080_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_21d_diff_base_v081_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_ema_base_v082_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = base.ewm(span=42, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_logp_base_v083_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_sq_base_v084_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_rank_base_v085_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_xrev_base_v086_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_42d_diff_base_v087_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 42)
    result = base.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_ema_base_v088_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = base.ewm(span=63, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_logp_base_v089_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_sq_base_v090_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_rank_base_v091_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_xrev_base_v092_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_63d_diff_base_v093_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_ema_base_v094_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = base.ewm(span=126, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_logp_base_v095_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_sq_base_v096_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_rank_base_v097_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_xrev_base_v098_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_126d_diff_base_v099_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 126)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_ema_base_v100_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = base.ewm(span=189, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_logp_base_v101_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_sq_base_v102_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_rank_base_v103_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_xrev_base_v104_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_189d_diff_base_v105_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 189)
    result = base.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_ema_base_v106_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = base.ewm(span=252, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_logp_base_v107_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_sq_base_v108_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_rank_base_v109_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_xrev_base_v110_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_252d_diff_base_v111_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 252)
    result = base.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_ema_base_v112_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = base.ewm(span=378, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_logp_base_v113_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_sq_base_v114_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_rank_base_v115_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_xrev_base_v116_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_378d_diff_base_v117_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 378)
    result = base.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_ema_base_v118_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = base.ewm(span=504, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_logp_base_v119_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_sq_base_v120_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_rank_base_v121_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_xrev_base_v122_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_drq_504d_diff_base_v123_signal(deferredrev, revenue, closeadj):
    base = _mean(_f49_deferred_rev_quality(deferredrev, revenue), 504)
    result = base.diff(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_ema_base_v124_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_logp_base_v125_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_sq_base_v126_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_rank_base_v127_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_xrev_base_v128_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_21d_diff_base_v129_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_ema_base_v130_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = base.ewm(span=42, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_logp_base_v131_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_sq_base_v132_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_rank_base_v133_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_xrev_base_v134_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_42d_diff_base_v135_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 42)
    result = base.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_ema_base_v136_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = base.ewm(span=63, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_logp_base_v137_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_sq_base_v138_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_rank_base_v139_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_xrev_base_v140_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_63d_diff_base_v141_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_ema_base_v142_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = base.ewm(span=126, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_logp_base_v143_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_sq_base_v144_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_rank_base_v145_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_xrev_base_v146_signal(deferredrev, revenue, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = base * (revenue / _mean(revenue, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_126d_diff_base_v147_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 126)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_189d_ema_base_v148_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 189)
    result = base.ewm(span=189, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_189d_logp_base_v149_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f49psq_f49_publishing_subscription_quality_subgrow_189d_sq_base_v150_signal(deferredrev, closeadj):
    base = _f49_subscription_growth(deferredrev, 189)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49psq_f49_publishing_subscription_quality_drq_21d_ema_base_v076_signal,
    f49psq_f49_publishing_subscription_quality_drq_21d_logp_base_v077_signal,
    f49psq_f49_publishing_subscription_quality_drq_21d_sq_base_v078_signal,
    f49psq_f49_publishing_subscription_quality_drq_21d_rank_base_v079_signal,
    f49psq_f49_publishing_subscription_quality_drq_21d_xrev_base_v080_signal,
    f49psq_f49_publishing_subscription_quality_drq_21d_diff_base_v081_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_ema_base_v082_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_logp_base_v083_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_sq_base_v084_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_rank_base_v085_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_xrev_base_v086_signal,
    f49psq_f49_publishing_subscription_quality_drq_42d_diff_base_v087_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_ema_base_v088_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_logp_base_v089_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_sq_base_v090_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_rank_base_v091_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_xrev_base_v092_signal,
    f49psq_f49_publishing_subscription_quality_drq_63d_diff_base_v093_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_ema_base_v094_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_logp_base_v095_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_sq_base_v096_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_rank_base_v097_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_xrev_base_v098_signal,
    f49psq_f49_publishing_subscription_quality_drq_126d_diff_base_v099_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_ema_base_v100_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_logp_base_v101_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_sq_base_v102_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_rank_base_v103_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_xrev_base_v104_signal,
    f49psq_f49_publishing_subscription_quality_drq_189d_diff_base_v105_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_ema_base_v106_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_logp_base_v107_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_sq_base_v108_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_rank_base_v109_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_xrev_base_v110_signal,
    f49psq_f49_publishing_subscription_quality_drq_252d_diff_base_v111_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_ema_base_v112_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_logp_base_v113_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_sq_base_v114_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_rank_base_v115_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_xrev_base_v116_signal,
    f49psq_f49_publishing_subscription_quality_drq_378d_diff_base_v117_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_ema_base_v118_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_logp_base_v119_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_sq_base_v120_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_rank_base_v121_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_xrev_base_v122_signal,
    f49psq_f49_publishing_subscription_quality_drq_504d_diff_base_v123_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_ema_base_v124_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_logp_base_v125_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_sq_base_v126_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_rank_base_v127_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_xrev_base_v128_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_21d_diff_base_v129_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_ema_base_v130_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_logp_base_v131_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_sq_base_v132_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_rank_base_v133_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_xrev_base_v134_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_42d_diff_base_v135_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_ema_base_v136_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_logp_base_v137_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_sq_base_v138_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_rank_base_v139_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_xrev_base_v140_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_63d_diff_base_v141_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_ema_base_v142_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_logp_base_v143_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_sq_base_v144_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_rank_base_v145_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_xrev_base_v146_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_126d_diff_base_v147_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_189d_ema_base_v148_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_189d_logp_base_v149_signal,
    f49psq_f49_publishing_subscription_quality_subgrow_189d_sq_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_PUBLISHING_SUBSCRIPTION_QUALITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {"closeadj": closeadj, "deferredrev": deferredrev, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f49_deferred_rev_quality", "_f49_subscription_growth", "_f49_subscription_durability")
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
    print(f"OK f49_publishing_subscription_quality_base_076_150_claude: {n_features} features pass")
