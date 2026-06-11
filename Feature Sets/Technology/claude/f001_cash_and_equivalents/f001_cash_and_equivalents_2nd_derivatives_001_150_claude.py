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
def _f001_cash_per_asset(cashneq, assets):
    return cashneq / assets.replace(0, np.nan).abs()


def _f001_cash_per_marketcap(cashneq, marketcap):
    return cashneq / marketcap.replace(0, np.nan).abs()


def _f001_cash_per_share(cashneq, sharesbas):
    return cashneq / sharesbas.replace(0, np.nan).abs()


def _f001_cash_log(cashneq):
    return np.log(cashneq.abs().replace(0, np.nan))


# 21d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_slope_21d_2d_v001_signal(cashneq, closeadj):
    base = cashneq
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_slope_63d_2d_v002_signal(cashneq, closeadj):
    base = cashneq
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_slope_126d_2d_v003_signal(cashneq, closeadj):
    base = cashneq
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_slope_252d_2d_v004_signal(cashneq, closeadj):
    base = cashneq
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_slope_504d_2d_v005_signal(cashneq, closeadj):
    base = cashneq
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_slope_21d_2d_v006_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_slope_63d_2d_v007_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_slope_126d_2d_v008_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_slope_252d_2d_v009_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_slope_504d_2d_v010_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_slope_21d_2d_v011_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_slope_63d_2d_v012_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_slope_126d_2d_v013_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_slope_252d_2d_v014_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_slope_504d_2d_v015_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_slope_21d_2d_v016_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_slope_63d_2d_v017_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_slope_126d_2d_v018_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_slope_252d_2d_v019_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_slope_504d_2d_v020_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_slope_21d_2d_v021_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_slope_63d_2d_v022_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_slope_126d_2d_v023_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_slope_252d_2d_v024_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_slope_504d_2d_v025_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_slope_21d_2d_v026_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_slope_63d_2d_v027_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_slope_126d_2d_v028_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_slope_252d_2d_v029_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_slope_504d_2d_v030_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_slope_21d_2d_v031_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_slope_63d_2d_v032_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_slope_126d_2d_v033_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_slope_252d_2d_v034_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_slope_504d_2d_v035_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_slope_21d_2d_v036_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_slope_63d_2d_v037_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_slope_126d_2d_v038_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_slope_252d_2d_v039_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_slope_504d_2d_v040_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_slope_21d_2d_v041_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_slope_63d_2d_v042_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_slope_126d_2d_v043_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_slope_252d_2d_v044_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_slope_504d_2d_v045_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_sm21_sl21_2d_v046_signal(cashneq, closeadj):
    base = _mean(cashneq, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_sm63_sl21_2d_v047_signal(cashneq, closeadj):
    base = _mean(cashneq, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_sm63_sl63_2d_v048_signal(cashneq, closeadj):
    base = _mean(cashneq, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_sm252_sl63_2d_v049_signal(cashneq, closeadj):
    base = _mean(cashneq, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_sm252_sl126_2d_v050_signal(cashneq, closeadj):
    base = _mean(cashneq, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_sm21_sl21_2d_v051_signal(cashneq, assets, closeadj):
    base = _mean(_f001_cash_per_asset(cashneq, assets), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_sm63_sl21_2d_v052_signal(cashneq, assets, closeadj):
    base = _mean(_f001_cash_per_asset(cashneq, assets), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_sm63_sl63_2d_v053_signal(cashneq, assets, closeadj):
    base = _mean(_f001_cash_per_asset(cashneq, assets), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_sm252_sl63_2d_v054_signal(cashneq, assets, closeadj):
    base = _mean(_f001_cash_per_asset(cashneq, assets), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_sm252_sl126_2d_v055_signal(cashneq, assets, closeadj):
    base = _mean(_f001_cash_per_asset(cashneq, assets), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_sm21_sl21_2d_v056_signal(cashneq, marketcap, closeadj):
    base = _mean(_f001_cash_per_marketcap(cashneq, marketcap), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_sm63_sl21_2d_v057_signal(cashneq, marketcap, closeadj):
    base = _mean(_f001_cash_per_marketcap(cashneq, marketcap), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_sm63_sl63_2d_v058_signal(cashneq, marketcap, closeadj):
    base = _mean(_f001_cash_per_marketcap(cashneq, marketcap), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_sm252_sl63_2d_v059_signal(cashneq, marketcap, closeadj):
    base = _mean(_f001_cash_per_marketcap(cashneq, marketcap), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_sm252_sl126_2d_v060_signal(cashneq, marketcap, closeadj):
    base = _mean(_f001_cash_per_marketcap(cashneq, marketcap), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_sm21_sl21_2d_v061_signal(cashneq, sharesbas, closeadj):
    base = _mean(_f001_cash_per_share(cashneq, sharesbas), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_sm63_sl21_2d_v062_signal(cashneq, sharesbas, closeadj):
    base = _mean(_f001_cash_per_share(cashneq, sharesbas), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_sm63_sl63_2d_v063_signal(cashneq, sharesbas, closeadj):
    base = _mean(_f001_cash_per_share(cashneq, sharesbas), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_sm252_sl63_2d_v064_signal(cashneq, sharesbas, closeadj):
    base = _mean(_f001_cash_per_share(cashneq, sharesbas), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_sm252_sl126_2d_v065_signal(cashneq, sharesbas, closeadj):
    base = _mean(_f001_cash_per_share(cashneq, sharesbas), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_sm21_sl21_2d_v066_signal(cashneq, equity, closeadj):
    base = _mean(cashneq / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_sm63_sl21_2d_v067_signal(cashneq, equity, closeadj):
    base = _mean(cashneq / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_sm63_sl63_2d_v068_signal(cashneq, equity, closeadj):
    base = _mean(cashneq / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_sm252_sl63_2d_v069_signal(cashneq, equity, closeadj):
    base = _mean(cashneq / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_sm252_sl126_2d_v070_signal(cashneq, equity, closeadj):
    base = _mean(cashneq / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_sm21_sl21_2d_v071_signal(cashneq, liabilities, closeadj):
    base = _mean(cashneq / liabilities.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_sm63_sl21_2d_v072_signal(cashneq, liabilities, closeadj):
    base = _mean(cashneq / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_sm63_sl63_2d_v073_signal(cashneq, liabilities, closeadj):
    base = _mean(cashneq / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_sm252_sl63_2d_v074_signal(cashneq, liabilities, closeadj):
    base = _mean(cashneq / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_sm252_sl126_2d_v075_signal(cashneq, liabilities, closeadj):
    base = _mean(cashneq / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_sm21_sl21_2d_v076_signal(cashneq, revenue, closeadj):
    base = _mean(cashneq / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_sm63_sl21_2d_v077_signal(cashneq, revenue, closeadj):
    base = _mean(cashneq / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_sm63_sl63_2d_v078_signal(cashneq, revenue, closeadj):
    base = _mean(cashneq / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_sm252_sl63_2d_v079_signal(cashneq, revenue, closeadj):
    base = _mean(cashneq / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_sm252_sl126_2d_v080_signal(cashneq, revenue, closeadj):
    base = _mean(cashneq / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_sm21_sl21_2d_v081_signal(cashneq, rnd, closeadj):
    base = _mean(cashneq / rnd.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_sm63_sl21_2d_v082_signal(cashneq, rnd, closeadj):
    base = _mean(cashneq / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_sm63_sl63_2d_v083_signal(cashneq, rnd, closeadj):
    base = _mean(cashneq / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_sm252_sl63_2d_v084_signal(cashneq, rnd, closeadj):
    base = _mean(cashneq / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_sm252_sl126_2d_v085_signal(cashneq, rnd, closeadj):
    base = _mean(cashneq / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_sm21_sl21_2d_v086_signal(cashneq, closeadj):
    base = _mean(_f001_cash_log(cashneq), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_sm63_sl21_2d_v087_signal(cashneq, closeadj):
    base = _mean(_f001_cash_log(cashneq), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_sm63_sl63_2d_v088_signal(cashneq, closeadj):
    base = _mean(_f001_cash_log(cashneq), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_sm252_sl63_2d_v089_signal(cashneq, closeadj):
    base = _mean(_f001_cash_log(cashneq), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_sm252_sl126_2d_v090_signal(cashneq, closeadj):
    base = _mean(_f001_cash_log(cashneq), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_pctslope_21d_2d_v091_signal(cashneq, closeadj):
    base = cashneq
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_pctslope_63d_2d_v092_signal(cashneq, closeadj):
    base = cashneq
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_pctslope_252d_2d_v093_signal(cashneq, closeadj):
    base = cashneq
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_pctslope_21d_2d_v094_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_pctslope_63d_2d_v095_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_pctslope_252d_2d_v096_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_pctslope_21d_2d_v097_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_pctslope_63d_2d_v098_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_pctslope_252d_2d_v099_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_pctslope_21d_2d_v100_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_pctslope_63d_2d_v101_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_pctslope_252d_2d_v102_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_pctslope_21d_2d_v103_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_pctslope_63d_2d_v104_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_pctslope_252d_2d_v105_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_pctslope_21d_2d_v106_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_pctslope_63d_2d_v107_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_pctslope_252d_2d_v108_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_pctslope_21d_2d_v109_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_pctslope_63d_2d_v110_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_pctslope_252d_2d_v111_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_pctslope_21d_2d_v112_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_pctslope_63d_2d_v113_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_pctslope_252d_2d_v114_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_pctslope_21d_2d_v115_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_pctslope_63d_2d_v116_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_pctslope_252d_2d_v117_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_sgnslope_21d_2d_v118_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_sgnslope_63d_2d_v119_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_sgnslope_252d_2d_v120_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_sgnslope_21d_2d_v121_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_sgnslope_63d_2d_v122_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_sgnslope_252d_2d_v123_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_sgnslope_21d_2d_v124_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_sgnslope_63d_2d_v125_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_sgnslope_252d_2d_v126_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_sgnslope_21d_2d_v127_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_sgnslope_63d_2d_v128_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_sgnslope_252d_2d_v129_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_sgnslope_21d_2d_v130_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_sgnslope_63d_2d_v131_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_sgnslope_252d_2d_v132_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_sgnslope_21d_2d_v133_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_sgnslope_63d_2d_v134_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_sgnslope_252d_2d_v135_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_sgnslope_21d_2d_v136_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_sgnslope_63d_2d_v137_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_sgnslope_252d_2d_v138_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_sgnslope_21d_2d_v139_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_sgnslope_63d_2d_v140_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_sgnslope_252d_2d_v141_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_sgnslope_21d_2d_v142_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_sgnslope_63d_2d_v143_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of logcash
def f001ce_f001_cash_and_equivalents_logcash_sgnslope_252d_2d_v144_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_logmagslope_21d_2d_v145_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_logmagslope_63d_2d_v146_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_logmagslope_252d_2d_v147_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_logmagslope_21d_2d_v148_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_logmagslope_63d_2d_v149_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_logmagslope_252d_2d_v150_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

