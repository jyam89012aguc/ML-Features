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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f007_liquid(cashneq, investmentsc):
    return cashneq.fillna(0) + investmentsc.fillna(0)


def _f007_liquid_to_liab(cashneq, investmentsc, liabilities):
    liq = cashneq.fillna(0) + investmentsc.fillna(0)
    return liq / liabilities.replace(0, np.nan).abs()


def _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc):
    liq = cashneq.fillna(0) + investmentsc.fillna(0)
    return liq / liabilitiesc.replace(0, np.nan).abs()


# 63d z-score of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_z_63d_base_v076_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_z_126d_base_v077_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_z_252d_base_v078_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_z_504d_base_v079_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_z_63d_base_v080_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_z_126d_base_v081_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_z_252d_base_v082_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_z_504d_base_v083_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_z_63d_base_v084_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_z_126d_base_v085_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_z_252d_base_v086_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_z_504d_base_v087_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_z_63d_base_v088_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_z_126d_base_v089_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_z_252d_base_v090_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_z_504d_base_v091_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_z_63d_base_v092_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_z_126d_base_v093_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_z_252d_base_v094_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_z_504d_base_v095_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_z_63d_base_v096_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_z_126d_base_v097_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_z_252d_base_v098_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_z_504d_base_v099_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_z_63d_base_v100_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_z_126d_base_v101_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_z_252d_base_v102_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_z_504d_base_v103_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_distmax_252d_base_v104_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_distmax_504d_base_v105_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_distmax_252d_base_v106_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_distmax_504d_base_v107_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_distmax_252d_base_v108_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_distmax_504d_base_v109_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_distmax_252d_base_v110_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_distmax_504d_base_v111_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_distmax_252d_base_v112_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_distmax_504d_base_v113_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_distmax_252d_base_v114_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_distmax_504d_base_v115_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_distmax_252d_base_v116_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_distmax_504d_base_v117_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_distmed_126d_base_v118_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_distmed_252d_base_v119_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_distmed_504d_base_v120_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_distmed_126d_base_v121_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_distmed_252d_base_v122_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_distmed_504d_base_v123_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_distmed_126d_base_v124_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_distmed_252d_base_v125_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_distmed_504d_base_v126_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_distmed_126d_base_v127_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_distmed_252d_base_v128_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_distmed_504d_base_v129_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_distmed_126d_base_v130_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_distmed_252d_base_v131_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_distmed_504d_base_v132_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_distmed_126d_base_v133_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_distmed_252d_base_v134_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_distmed_504d_base_v135_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_distmed_126d_base_v136_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_distmed_252d_base_v137_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_distmed_504d_base_v138_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_chg_63d_base_v139_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_chg_252d_base_v140_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_chg_63d_base_v141_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_chg_252d_base_v142_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_chg_63d_base_v143_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_chg_252d_base_v144_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_chg_63d_base_v145_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_chg_252d_base_v146_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_chg_63d_base_v147_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_chg_252d_base_v148_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_chg_63d_base_v149_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_chg_252d_base_v150_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

