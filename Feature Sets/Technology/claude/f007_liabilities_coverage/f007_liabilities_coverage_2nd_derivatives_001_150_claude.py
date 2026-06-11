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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f007_liquid(cashneq, investmentsc):
    return cashneq.fillna(0) + investmentsc.fillna(0)


def _f007_liquid_to_liab(cashneq, investmentsc, liabilities):
    liq = cashneq.fillna(0) + investmentsc.fillna(0)
    return liq / liabilities.replace(0, np.nan).abs()


def _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc):
    liq = cashneq.fillna(0) + investmentsc.fillna(0)
    return liq / liabilitiesc.replace(0, np.nan).abs()


# 21d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_slope_21d_2d_v001_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_slope_63d_2d_v002_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_slope_126d_2d_v003_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_slope_252d_2d_v004_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_slope_504d_2d_v005_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_slope_21d_2d_v006_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_slope_63d_2d_v007_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_slope_126d_2d_v008_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_slope_252d_2d_v009_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_slope_504d_2d_v010_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_slope_21d_2d_v011_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_slope_63d_2d_v012_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_slope_126d_2d_v013_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_slope_252d_2d_v014_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_slope_504d_2d_v015_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_slope_21d_2d_v016_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_slope_63d_2d_v017_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_slope_126d_2d_v018_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_slope_252d_2d_v019_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_slope_504d_2d_v020_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_slope_21d_2d_v021_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_slope_63d_2d_v022_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_slope_126d_2d_v023_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_slope_252d_2d_v024_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_slope_504d_2d_v025_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_slope_21d_2d_v026_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_slope_63d_2d_v027_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_slope_126d_2d_v028_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_slope_252d_2d_v029_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_slope_504d_2d_v030_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_slope_21d_2d_v031_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_slope_63d_2d_v032_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_slope_126d_2d_v033_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_slope_252d_2d_v034_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_slope_504d_2d_v035_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_sm21_sl21_2d_v036_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f007_liquid_to_liab(cashneq, investmentsc, liabilities), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_sm63_sl21_2d_v037_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f007_liquid_to_liab(cashneq, investmentsc, liabilities), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_sm63_sl63_2d_v038_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f007_liquid_to_liab(cashneq, investmentsc, liabilities), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_sm252_sl63_2d_v039_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f007_liquid_to_liab(cashneq, investmentsc, liabilities), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_sm252_sl126_2d_v040_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f007_liquid_to_liab(cashneq, investmentsc, liabilities), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_sm21_sl21_2d_v041_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_sm63_sl21_2d_v042_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_sm63_sl63_2d_v043_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_sm252_sl63_2d_v044_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_sm252_sl126_2d_v045_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_sm21_sl21_2d_v046_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_sm63_sl21_2d_v047_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_sm63_sl63_2d_v048_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_sm252_sl63_2d_v049_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_sm252_sl126_2d_v050_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_sm21_sl21_2d_v051_signal(liabilitiesc, liabilities, closeadj):
    base = _mean(liabilitiesc / liabilities.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_sm63_sl21_2d_v052_signal(liabilitiesc, liabilities, closeadj):
    base = _mean(liabilitiesc / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_sm63_sl63_2d_v053_signal(liabilitiesc, liabilities, closeadj):
    base = _mean(liabilitiesc / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_sm252_sl63_2d_v054_signal(liabilitiesc, liabilities, closeadj):
    base = _mean(liabilitiesc / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_sm252_sl126_2d_v055_signal(liabilitiesc, liabilities, closeadj):
    base = _mean(liabilitiesc / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_sm21_sl21_2d_v056_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilitiesc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_sm63_sl21_2d_v057_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilitiesc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_sm63_sl63_2d_v058_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilitiesc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_sm252_sl63_2d_v059_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilitiesc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_sm252_sl126_2d_v060_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilitiesc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_sm21_sl21_2d_v061_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_sm63_sl21_2d_v062_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_sm63_sl63_2d_v063_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_sm252_sl63_2d_v064_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_sm252_sl126_2d_v065_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = _mean((_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_sm21_sl21_2d_v066_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_sm63_sl21_2d_v067_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_sm63_sl63_2d_v068_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_sm252_sl63_2d_v069_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_sm252_sl126_2d_v070_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _mean(_f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_pctslope_21d_2d_v071_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_pctslope_63d_2d_v072_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_pctslope_252d_2d_v073_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_pctslope_21d_2d_v074_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_pctslope_63d_2d_v075_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_pctslope_252d_2d_v076_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_pctslope_21d_2d_v077_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_pctslope_63d_2d_v078_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_pctslope_252d_2d_v079_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_pctslope_21d_2d_v080_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_pctslope_63d_2d_v081_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_pctslope_252d_2d_v082_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_pctslope_21d_2d_v083_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_pctslope_63d_2d_v084_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_pctslope_252d_2d_v085_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_pctslope_21d_2d_v086_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_pctslope_63d_2d_v087_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_pctslope_252d_2d_v088_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_pctslope_21d_2d_v089_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_pctslope_63d_2d_v090_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_pctslope_252d_2d_v091_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_sgnslope_21d_2d_v092_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_sgnslope_63d_2d_v093_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_sgnslope_252d_2d_v094_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_sgnslope_21d_2d_v095_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_sgnslope_63d_2d_v096_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_sgnslope_252d_2d_v097_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_sgnslope_21d_2d_v098_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_sgnslope_63d_2d_v099_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_sgnslope_252d_2d_v100_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_sgnslope_21d_2d_v101_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_sgnslope_63d_2d_v102_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_sgnslope_252d_2d_v103_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_sgnslope_21d_2d_v104_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_sgnslope_63d_2d_v105_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_sgnslope_252d_2d_v106_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_sgnslope_21d_2d_v107_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_sgnslope_63d_2d_v108_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_sgnslope_252d_2d_v109_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_sgnslope_21d_2d_v110_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_sgnslope_63d_2d_v111_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_sgnslope_252d_2d_v112_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_logmagslope_21d_2d_v113_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_logmagslope_63d_2d_v114_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_logmagslope_252d_2d_v115_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_logmagslope_21d_2d_v116_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_logmagslope_63d_2d_v117_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_logmagslope_252d_2d_v118_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_logmagslope_21d_2d_v119_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_logmagslope_63d_2d_v120_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_logmagslope_252d_2d_v121_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_logmagslope_21d_2d_v122_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_logmagslope_63d_2d_v123_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_logmagslope_252d_2d_v124_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_logmagslope_21d_2d_v125_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_logmagslope_63d_2d_v126_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_logmagslope_252d_2d_v127_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_logmagslope_21d_2d_v128_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_logmagslope_63d_2d_v129_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_logmagslope_252d_2d_v130_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_logmagslope_21d_2d_v131_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_logmagslope_63d_2d_v132_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_logmagslope_252d_2d_v133_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liq_to_liab|
def f007lc_f007_liabilities_coverage_liq_to_liab_logslope_63d_2d_v134_signal(cashneq, investmentsc, liabilities, closeadj):
    base = np.log((_f007_liquid_to_liab(cashneq, investmentsc, liabilities)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liq_to_liab|
def f007lc_f007_liabilities_coverage_liq_to_liab_logslope_252d_2d_v135_signal(cashneq, investmentsc, liabilities, closeadj):
    base = np.log((_f007_liquid_to_liab(cashneq, investmentsc, liabilities)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liq_to_curliab|
def f007lc_f007_liabilities_coverage_liq_to_curliab_logslope_63d_2d_v136_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = np.log((_f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liq_to_curliab|
def f007lc_f007_liabilities_coverage_liq_to_curliab_logslope_252d_2d_v137_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = np.log((_f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liq_to_ncliab|
def f007lc_f007_liabilities_coverage_liq_to_ncliab_logslope_63d_2d_v138_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = np.log((_f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liq_to_ncliab|
def f007lc_f007_liabilities_coverage_liq_to_ncliab_logslope_252d_2d_v139_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = np.log((_f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|curliab_share|
def f007lc_f007_liabilities_coverage_curliab_share_logslope_63d_2d_v140_signal(liabilitiesc, liabilities, closeadj):
    base = np.log((liabilitiesc / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|curliab_share|
def f007lc_f007_liabilities_coverage_curliab_share_logslope_252d_2d_v141_signal(liabilitiesc, liabilities, closeadj):
    base = np.log((liabilitiesc / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liq_minus_curliab|
def f007lc_f007_liabilities_coverage_liq_minus_curliab_logslope_63d_2d_v142_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = np.log(((_f007_liquid(cashneq, investmentsc) - liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liq_minus_curliab|
def f007lc_f007_liabilities_coverage_liq_minus_curliab_logslope_252d_2d_v143_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = np.log(((_f007_liquid(cashneq, investmentsc) - liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netliq_to_mcap|
def f007lc_f007_liabilities_coverage_netliq_to_mcap_logslope_63d_2d_v144_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = np.log(((_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netliq_to_mcap|
def f007lc_f007_liabilities_coverage_netliq_to_mcap_logslope_252d_2d_v145_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = np.log(((_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liq_to_drev|
def f007lc_f007_liabilities_coverage_liq_to_drev_logslope_63d_2d_v146_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = np.log((_f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liq_to_drev|
def f007lc_f007_liabilities_coverage_liq_to_drev_logslope_252d_2d_v147_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = np.log((_f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

