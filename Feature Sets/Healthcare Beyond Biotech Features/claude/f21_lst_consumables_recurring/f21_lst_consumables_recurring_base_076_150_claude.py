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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f21_consumables_revenue_share(grossmargin, revenue, w):
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return gm * revenue


def _f21_recurring_quality(revenue, w):
    g = revenue.pct_change(periods=w)
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return g / sd.replace(0, np.nan).abs()


def _f21_consumables_signature(revenue, grossmargin, w):
    r = revenue.pct_change(periods=w)
    gm_sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return r / (gm_sd.replace(0, np.nan) + 1e-6)


# ----- different scaling and transforms vs file 1 -----
# v076..v100: revshare with log(close) / sqrt(close) / close^2 / close-mean scaling
def f21lcr_f21_lst_consumables_recurring_revshare_5d_base_v076_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 5)
    result = base.pct_change(5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_10d_base_v077_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 10)
    result = base.pct_change(10) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_42d_base_v078_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 42)
    result = base.pct_change(42) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_189d_base_v079_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 189)
    result = base.pct_change(189) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_378d_base_v080_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 378)
    result = base.pct_change(252) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_sqrtsc_21d_base_v081_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = base.pct_change(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_sqrtsc_63d_base_v082_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = base.pct_change(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_sqrtsc_252d_base_v083_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = base.pct_change(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_meansc_21d_base_v084_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = base.pct_change(21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_meansc_63d_base_v085_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = base.pct_change(63) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_meansc_252d_base_v086_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = base.pct_change(126) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_emasc_21d_base_v087_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = base.pct_change(21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_emasc_63d_base_v088_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = base.pct_change(63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_emasc_252d_base_v089_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = base.pct_change(126) * _ema(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_centersc_21d_base_v090_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = base.pct_change(21) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_centersc_63d_base_v091_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = base.pct_change(63) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_centersc_252d_base_v092_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = base.pct_change(126) * (closeadj - _mean(closeadj, 504))
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_zcsc_21d_base_v093_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = _z(base, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_zcsc_63d_base_v094_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = _z(base, 252) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_zcsc_252d_base_v095_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = _z(base, 504) * _z(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_invsc_21d_base_v096_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = base.pct_change(21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_invsc_63d_base_v097_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = base.pct_change(63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_invsc_252d_base_v098_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = base.pct_change(126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_grratio_63d_base_v099_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = (base / grossmargin.replace(0, np.nan)) * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_grratio_252d_base_v100_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = (base / grossmargin.replace(0, np.nan)) * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# v101..v125: rq with novel transforms
def f21lcr_f21_lst_consumables_recurring_rq_5d_base_v101_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 5)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_10d_base_v102_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 10)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_42d_base_v103_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 42)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_189d_base_v104_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 189)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_378d_base_v105_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 378)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_sqrtsc_21d_base_v106_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_sqrtsc_63d_base_v107_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_sqrtsc_252d_base_v108_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_meansc_21d_base_v109_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_meansc_63d_base_v110_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_meansc_252d_base_v111_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_emasc_21d_base_v112_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_emasc_63d_base_v113_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_emasc_252d_base_v114_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = base * _ema(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_centersc_21d_base_v115_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = base * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_centersc_63d_base_v116_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = base * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_centersc_252d_base_v117_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = base * (closeadj - _mean(closeadj, 504))
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_zcsc_21d_base_v118_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = base * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_zcsc_63d_base_v119_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = base * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_zcsc_252d_base_v120_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = base * _z(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_invsc_21d_base_v121_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_invsc_63d_base_v122_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_invsc_252d_base_v123_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_signsc_21d_base_v124_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = np.sign(base) * base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_signsc_63d_base_v125_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = np.sign(base) * base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126..v150: signature with novel transforms
def f21lcr_f21_lst_consumables_recurring_sig_5d_base_v126_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 5)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_10d_base_v127_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 10)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_42d_base_v128_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 42)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_189d_base_v129_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 189)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_378d_base_v130_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 378)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_sqrtsc_21d_base_v131_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_sqrtsc_63d_base_v132_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_sqrtsc_252d_base_v133_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_meansc_21d_base_v134_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_meansc_63d_base_v135_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_meansc_252d_base_v136_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_emasc_21d_base_v137_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_emasc_63d_base_v138_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = base * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_emasc_252d_base_v139_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = base * _ema(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_centersc_21d_base_v140_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = base * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_centersc_63d_base_v141_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = base * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_centersc_252d_base_v142_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = base * (closeadj - _mean(closeadj, 504))
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_zcsc_21d_base_v143_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = base * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_zcsc_63d_base_v144_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = base * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_zcsc_252d_base_v145_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = base * _z(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_invsc_21d_base_v146_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_invsc_63d_base_v147_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_invsc_252d_base_v148_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_signsc_21d_base_v149_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = np.sign(base) * base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_signsc_63d_base_v150_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = np.sign(base) * base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21lcr_f21_lst_consumables_recurring_revshare_5d_base_v076_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_10d_base_v077_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_42d_base_v078_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_189d_base_v079_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_378d_base_v080_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_sqrtsc_21d_base_v081_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_sqrtsc_63d_base_v082_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_sqrtsc_252d_base_v083_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_meansc_21d_base_v084_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_meansc_63d_base_v085_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_meansc_252d_base_v086_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_emasc_21d_base_v087_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_emasc_63d_base_v088_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_emasc_252d_base_v089_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_centersc_21d_base_v090_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_centersc_63d_base_v091_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_centersc_252d_base_v092_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_zcsc_21d_base_v093_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_zcsc_63d_base_v094_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_zcsc_252d_base_v095_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_invsc_21d_base_v096_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_invsc_63d_base_v097_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_invsc_252d_base_v098_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_grratio_63d_base_v099_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_grratio_252d_base_v100_signal,
    f21lcr_f21_lst_consumables_recurring_rq_5d_base_v101_signal,
    f21lcr_f21_lst_consumables_recurring_rq_10d_base_v102_signal,
    f21lcr_f21_lst_consumables_recurring_rq_42d_base_v103_signal,
    f21lcr_f21_lst_consumables_recurring_rq_189d_base_v104_signal,
    f21lcr_f21_lst_consumables_recurring_rq_378d_base_v105_signal,
    f21lcr_f21_lst_consumables_recurring_rq_sqrtsc_21d_base_v106_signal,
    f21lcr_f21_lst_consumables_recurring_rq_sqrtsc_63d_base_v107_signal,
    f21lcr_f21_lst_consumables_recurring_rq_sqrtsc_252d_base_v108_signal,
    f21lcr_f21_lst_consumables_recurring_rq_meansc_21d_base_v109_signal,
    f21lcr_f21_lst_consumables_recurring_rq_meansc_63d_base_v110_signal,
    f21lcr_f21_lst_consumables_recurring_rq_meansc_252d_base_v111_signal,
    f21lcr_f21_lst_consumables_recurring_rq_emasc_21d_base_v112_signal,
    f21lcr_f21_lst_consumables_recurring_rq_emasc_63d_base_v113_signal,
    f21lcr_f21_lst_consumables_recurring_rq_emasc_252d_base_v114_signal,
    f21lcr_f21_lst_consumables_recurring_rq_centersc_21d_base_v115_signal,
    f21lcr_f21_lst_consumables_recurring_rq_centersc_63d_base_v116_signal,
    f21lcr_f21_lst_consumables_recurring_rq_centersc_252d_base_v117_signal,
    f21lcr_f21_lst_consumables_recurring_rq_zcsc_21d_base_v118_signal,
    f21lcr_f21_lst_consumables_recurring_rq_zcsc_63d_base_v119_signal,
    f21lcr_f21_lst_consumables_recurring_rq_zcsc_252d_base_v120_signal,
    f21lcr_f21_lst_consumables_recurring_rq_invsc_21d_base_v121_signal,
    f21lcr_f21_lst_consumables_recurring_rq_invsc_63d_base_v122_signal,
    f21lcr_f21_lst_consumables_recurring_rq_invsc_252d_base_v123_signal,
    f21lcr_f21_lst_consumables_recurring_rq_signsc_21d_base_v124_signal,
    f21lcr_f21_lst_consumables_recurring_rq_signsc_63d_base_v125_signal,
    f21lcr_f21_lst_consumables_recurring_sig_5d_base_v126_signal,
    f21lcr_f21_lst_consumables_recurring_sig_10d_base_v127_signal,
    f21lcr_f21_lst_consumables_recurring_sig_42d_base_v128_signal,
    f21lcr_f21_lst_consumables_recurring_sig_189d_base_v129_signal,
    f21lcr_f21_lst_consumables_recurring_sig_378d_base_v130_signal,
    f21lcr_f21_lst_consumables_recurring_sig_sqrtsc_21d_base_v131_signal,
    f21lcr_f21_lst_consumables_recurring_sig_sqrtsc_63d_base_v132_signal,
    f21lcr_f21_lst_consumables_recurring_sig_sqrtsc_252d_base_v133_signal,
    f21lcr_f21_lst_consumables_recurring_sig_meansc_21d_base_v134_signal,
    f21lcr_f21_lst_consumables_recurring_sig_meansc_63d_base_v135_signal,
    f21lcr_f21_lst_consumables_recurring_sig_meansc_252d_base_v136_signal,
    f21lcr_f21_lst_consumables_recurring_sig_emasc_21d_base_v137_signal,
    f21lcr_f21_lst_consumables_recurring_sig_emasc_63d_base_v138_signal,
    f21lcr_f21_lst_consumables_recurring_sig_emasc_252d_base_v139_signal,
    f21lcr_f21_lst_consumables_recurring_sig_centersc_21d_base_v140_signal,
    f21lcr_f21_lst_consumables_recurring_sig_centersc_63d_base_v141_signal,
    f21lcr_f21_lst_consumables_recurring_sig_centersc_252d_base_v142_signal,
    f21lcr_f21_lst_consumables_recurring_sig_zcsc_21d_base_v143_signal,
    f21lcr_f21_lst_consumables_recurring_sig_zcsc_63d_base_v144_signal,
    f21lcr_f21_lst_consumables_recurring_sig_zcsc_252d_base_v145_signal,
    f21lcr_f21_lst_consumables_recurring_sig_invsc_21d_base_v146_signal,
    f21lcr_f21_lst_consumables_recurring_sig_invsc_63d_base_v147_signal,
    f21lcr_f21_lst_consumables_recurring_sig_invsc_252d_base_v148_signal,
    f21lcr_f21_lst_consumables_recurring_sig_signsc_21d_base_v149_signal,
    f21lcr_f21_lst_consumables_recurring_sig_signsc_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_LST_CONSUMABLES_RECURRING_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {"closeadj": closeadj, "revenue": revenue, "grossmargin": grossmargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = (
        "_f21_consumables_revenue_share",
        "_f21_recurring_quality",
        "_f21_consumables_signature",
    )
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
    print(f"OK f21_lst_consumables_recurring_base_076_150_claude: {n_features} features pass")
