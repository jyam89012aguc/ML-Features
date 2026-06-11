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


# 21d mean of liq_to_liab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_liab_mean_21d_base_v001_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liq_to_liab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_liab_mean_63d_base_v002_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liq_to_liab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_liab_mean_126d_base_v003_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liq_to_liab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_liab_mean_252d_base_v004_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liq_to_liab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_liab_mean_504d_base_v005_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liq_to_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_curliab_mean_21d_base_v006_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liq_to_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_curliab_mean_63d_base_v007_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liq_to_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_curliab_mean_126d_base_v008_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liq_to_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_curliab_mean_252d_base_v009_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liq_to_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_curliab_mean_504d_base_v010_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liq_to_ncliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_ncliab_mean_21d_base_v011_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liq_to_ncliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_ncliab_mean_63d_base_v012_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liq_to_ncliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_ncliab_mean_126d_base_v013_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liq_to_ncliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_ncliab_mean_252d_base_v014_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liq_to_ncliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_ncliab_mean_504d_base_v015_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of curliab_share scaled by closeadj
def f007lc_f007_liabilities_coverage_curliab_share_mean_21d_base_v016_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of curliab_share scaled by closeadj
def f007lc_f007_liabilities_coverage_curliab_share_mean_63d_base_v017_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of curliab_share scaled by closeadj
def f007lc_f007_liabilities_coverage_curliab_share_mean_126d_base_v018_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of curliab_share scaled by closeadj
def f007lc_f007_liabilities_coverage_curliab_share_mean_252d_base_v019_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of curliab_share scaled by closeadj
def f007lc_f007_liabilities_coverage_curliab_share_mean_504d_base_v020_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liq_minus_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_minus_curliab_mean_21d_base_v021_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liq_minus_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_minus_curliab_mean_63d_base_v022_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liq_minus_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_minus_curliab_mean_126d_base_v023_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liq_minus_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_minus_curliab_mean_252d_base_v024_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liq_minus_curliab scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_minus_curliab_mean_504d_base_v025_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netliq_to_mcap scaled by closeadj
def f007lc_f007_liabilities_coverage_netliq_to_mcap_mean_21d_base_v026_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netliq_to_mcap scaled by closeadj
def f007lc_f007_liabilities_coverage_netliq_to_mcap_mean_63d_base_v027_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netliq_to_mcap scaled by closeadj
def f007lc_f007_liabilities_coverage_netliq_to_mcap_mean_126d_base_v028_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netliq_to_mcap scaled by closeadj
def f007lc_f007_liabilities_coverage_netliq_to_mcap_mean_252d_base_v029_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netliq_to_mcap scaled by closeadj
def f007lc_f007_liabilities_coverage_netliq_to_mcap_mean_504d_base_v030_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liq_to_drev scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_drev_mean_21d_base_v031_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liq_to_drev scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_drev_mean_63d_base_v032_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liq_to_drev scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_drev_mean_126d_base_v033_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liq_to_drev scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_drev_mean_252d_base_v034_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liq_to_drev scaled by closeadj
def f007lc_f007_liabilities_coverage_liq_to_drev_mean_504d_base_v035_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_median_63d_base_v036_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_median_252d_base_v037_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_median_504d_base_v038_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_median_63d_base_v039_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_median_252d_base_v040_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_median_504d_base_v041_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_median_63d_base_v042_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_median_252d_base_v043_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_median_504d_base_v044_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_median_63d_base_v045_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_median_252d_base_v046_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_median_504d_base_v047_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_median_63d_base_v048_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_median_252d_base_v049_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_median_504d_base_v050_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_median_63d_base_v051_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_median_252d_base_v052_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_median_504d_base_v053_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_median_63d_base_v054_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_median_252d_base_v055_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_median_504d_base_v056_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_rmax_252d_base_v057_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_rmax_504d_base_v058_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_rmax_252d_base_v059_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_rmax_504d_base_v060_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_rmax_252d_base_v061_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_rmax_504d_base_v062_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_rmax_252d_base_v063_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of curliab_share
def f007lc_f007_liabilities_coverage_curliab_share_rmax_504d_base_v064_signal(liabilitiesc, liabilities, closeadj):
    base = liabilitiesc / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_rmax_252d_base_v065_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liq_minus_curliab
def f007lc_f007_liabilities_coverage_liq_minus_curliab_rmax_504d_base_v066_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_rmax_252d_base_v067_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of netliq_to_mcap
def f007lc_f007_liabilities_coverage_netliq_to_mcap_rmax_504d_base_v068_signal(cashneq, investmentsc, liabilities, marketcap, closeadj):
    base = (_f007_liquid(cashneq, investmentsc) - liabilities) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_rmax_252d_base_v069_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liq_to_drev
def f007lc_f007_liabilities_coverage_liq_to_drev_rmax_504d_base_v070_signal(cashneq, investmentsc, deferredrev, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / deferredrev.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_rmin_252d_base_v071_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of liq_to_liab
def f007lc_f007_liabilities_coverage_liq_to_liab_rmin_504d_base_v072_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f007_liquid_to_liab(cashneq, investmentsc, liabilities)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_rmin_252d_base_v073_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of liq_to_curliab
def f007lc_f007_liabilities_coverage_liq_to_curliab_rmin_504d_base_v074_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f007_liquid_to_curliab(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of liq_to_ncliab
def f007lc_f007_liabilities_coverage_liq_to_ncliab_rmin_252d_base_v075_signal(cashneq, investmentsc, liabilitiesnc, closeadj):
    base = _f007_liquid(cashneq, investmentsc) / liabilitiesnc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

