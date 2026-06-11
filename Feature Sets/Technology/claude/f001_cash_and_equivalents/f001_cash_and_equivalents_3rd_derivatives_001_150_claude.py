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


# 21d acceleration of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_accel_21d_3d_v001_signal(cashneq, closeadj):
    base = cashneq
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_accel_63d_3d_v002_signal(cashneq, closeadj):
    base = cashneq
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_accel_126d_3d_v003_signal(cashneq, closeadj):
    base = cashneq
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_accel_252d_3d_v004_signal(cashneq, closeadj):
    base = cashneq
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_accel_21d_3d_v005_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_accel_63d_3d_v006_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_accel_126d_3d_v007_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_accel_252d_3d_v008_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_accel_21d_3d_v009_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_accel_63d_3d_v010_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_accel_126d_3d_v011_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_accel_252d_3d_v012_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_accel_21d_3d_v013_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_accel_63d_3d_v014_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_accel_126d_3d_v015_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_accel_252d_3d_v016_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_accel_21d_3d_v017_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_accel_63d_3d_v018_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_accel_126d_3d_v019_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_accel_252d_3d_v020_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_accel_21d_3d_v021_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_accel_63d_3d_v022_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_accel_126d_3d_v023_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_accel_252d_3d_v024_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_accel_21d_3d_v025_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_accel_63d_3d_v026_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_accel_126d_3d_v027_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_accel_252d_3d_v028_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_accel_21d_3d_v029_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_accel_63d_3d_v030_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_accel_126d_3d_v031_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_accel_252d_3d_v032_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of logcash
def f001ce_f001_cash_and_equivalents_logcash_accel_21d_3d_v033_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of logcash
def f001ce_f001_cash_and_equivalents_logcash_accel_63d_3d_v034_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of logcash
def f001ce_f001_cash_and_equivalents_logcash_accel_126d_3d_v035_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of logcash
def f001ce_f001_cash_and_equivalents_logcash_accel_252d_3d_v036_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_slopez_21d_z126_3d_v037_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_slopez_63d_z252_3d_v038_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_slopez_126d_z252_3d_v039_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_slopez_252d_z504_3d_v040_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_slopez_21d_z126_3d_v041_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_slopez_63d_z252_3d_v042_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_slopez_126d_z252_3d_v043_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_slopez_252d_z504_3d_v044_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_slopez_21d_z126_3d_v045_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_slopez_63d_z252_3d_v046_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_slopez_126d_z252_3d_v047_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_slopez_252d_z504_3d_v048_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_slopez_21d_z126_3d_v049_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_slopez_63d_z252_3d_v050_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_slopez_126d_z252_3d_v051_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_slopez_252d_z504_3d_v052_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_slopez_21d_z126_3d_v053_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_slopez_63d_z252_3d_v054_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_slopez_126d_z252_3d_v055_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_slopez_252d_z504_3d_v056_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_slopez_21d_z126_3d_v057_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_slopez_63d_z252_3d_v058_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_slopez_126d_z252_3d_v059_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_slopez_252d_z504_3d_v060_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_slopez_21d_z126_3d_v061_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_slopez_63d_z252_3d_v062_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_slopez_126d_z252_3d_v063_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_slopez_252d_z504_3d_v064_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_slopez_21d_z126_3d_v065_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_slopez_63d_z252_3d_v066_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_slopez_126d_z252_3d_v067_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_slopez_252d_z504_3d_v068_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of logcash
def f001ce_f001_cash_and_equivalents_logcash_slopez_21d_z126_3d_v069_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of logcash
def f001ce_f001_cash_and_equivalents_logcash_slopez_63d_z252_3d_v070_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of logcash
def f001ce_f001_cash_and_equivalents_logcash_slopez_126d_z252_3d_v071_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of logcash
def f001ce_f001_cash_and_equivalents_logcash_slopez_252d_z504_3d_v072_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_jerk_21d_3d_v073_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_jerk_63d_3d_v074_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_jerk_126d_3d_v075_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_jerk_21d_3d_v076_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_jerk_63d_3d_v077_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_jerk_126d_3d_v078_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_jerk_21d_3d_v079_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_jerk_63d_3d_v080_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_jerk_126d_3d_v081_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_jerk_21d_3d_v082_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_jerk_63d_3d_v083_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_jerk_126d_3d_v084_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_jerk_21d_3d_v085_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_jerk_63d_3d_v086_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_jerk_126d_3d_v087_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_jerk_21d_3d_v088_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_jerk_63d_3d_v089_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_jerk_126d_3d_v090_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_jerk_21d_3d_v091_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_jerk_63d_3d_v092_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_jerk_126d_3d_v093_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_jerk_21d_3d_v094_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_jerk_63d_3d_v095_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_jerk_126d_3d_v096_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of logcash
def f001ce_f001_cash_and_equivalents_logcash_jerk_21d_3d_v097_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of logcash
def f001ce_f001_cash_and_equivalents_logcash_jerk_63d_3d_v098_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of logcash
def f001ce_f001_cash_and_equivalents_logcash_jerk_126d_3d_v099_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cashneq_lvl smoothed over 252d
def f001ce_f001_cash_and_equivalents_cashneq_lvl_smoothaccel_63d_sm252_3d_v100_signal(cashneq, closeadj):
    base = cashneq
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cashneq_lvl smoothed over 504d
def f001ce_f001_cash_and_equivalents_cashneq_lvl_smoothaccel_252d_sm504_3d_v101_signal(cashneq, closeadj):
    base = cashneq
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cashtoasset smoothed over 252d
def f001ce_f001_cash_and_equivalents_cashtoasset_smoothaccel_63d_sm252_3d_v102_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cashtoasset smoothed over 504d
def f001ce_f001_cash_and_equivalents_cashtoasset_smoothaccel_252d_sm504_3d_v103_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cashtomcap smoothed over 252d
def f001ce_f001_cash_and_equivalents_cashtomcap_smoothaccel_63d_sm252_3d_v104_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cashtomcap smoothed over 504d
def f001ce_f001_cash_and_equivalents_cashtomcap_smoothaccel_252d_sm504_3d_v105_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cashpershare smoothed over 252d
def f001ce_f001_cash_and_equivalents_cashpershare_smoothaccel_63d_sm252_3d_v106_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cashpershare smoothed over 504d
def f001ce_f001_cash_and_equivalents_cashpershare_smoothaccel_252d_sm504_3d_v107_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cashtoequity smoothed over 252d
def f001ce_f001_cash_and_equivalents_cashtoequity_smoothaccel_63d_sm252_3d_v108_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cashtoequity smoothed over 504d
def f001ce_f001_cash_and_equivalents_cashtoequity_smoothaccel_252d_sm504_3d_v109_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cashtoliab smoothed over 252d
def f001ce_f001_cash_and_equivalents_cashtoliab_smoothaccel_63d_sm252_3d_v110_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cashtoliab smoothed over 504d
def f001ce_f001_cash_and_equivalents_cashtoliab_smoothaccel_252d_sm504_3d_v111_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cashtorev smoothed over 252d
def f001ce_f001_cash_and_equivalents_cashtorev_smoothaccel_63d_sm252_3d_v112_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cashtorev smoothed over 504d
def f001ce_f001_cash_and_equivalents_cashtorev_smoothaccel_252d_sm504_3d_v113_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cashtornd smoothed over 252d
def f001ce_f001_cash_and_equivalents_cashtornd_smoothaccel_63d_sm252_3d_v114_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cashtornd smoothed over 504d
def f001ce_f001_cash_and_equivalents_cashtornd_smoothaccel_252d_sm504_3d_v115_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of logcash smoothed over 252d
def f001ce_f001_cash_and_equivalents_logcash_smoothaccel_63d_sm252_3d_v116_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of logcash smoothed over 504d
def f001ce_f001_cash_and_equivalents_logcash_smoothaccel_252d_sm504_3d_v117_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_accelz_21d_z252_3d_v118_signal(cashneq, closeadj):
    base = cashneq
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_accelz_63d_z504_3d_v119_signal(cashneq, closeadj):
    base = cashneq
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_accelz_21d_z252_3d_v120_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_accelz_63d_z504_3d_v121_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_accelz_21d_z252_3d_v122_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_accelz_63d_z504_3d_v123_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_accelz_21d_z252_3d_v124_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_accelz_63d_z504_3d_v125_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_accelz_21d_z252_3d_v126_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_accelz_63d_z504_3d_v127_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_accelz_21d_z252_3d_v128_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_accelz_63d_z504_3d_v129_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_accelz_21d_z252_3d_v130_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_accelz_63d_z504_3d_v131_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_accelz_21d_z252_3d_v132_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_accelz_63d_z504_3d_v133_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of logcash
def f001ce_f001_cash_and_equivalents_logcash_accelz_21d_z252_3d_v134_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of logcash
def f001ce_f001_cash_and_equivalents_logcash_accelz_63d_z504_3d_v135_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cashneq_lvl (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashneq_lvl_signflip_63d_3d_v136_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in cashneq_lvl (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashneq_lvl_signflip_252d_3d_v137_signal(cashneq, closeadj):
    base = cashneq
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cashtoasset (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtoasset_signflip_63d_3d_v138_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in cashtoasset (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtoasset_signflip_252d_3d_v139_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cashtomcap (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtomcap_signflip_63d_3d_v140_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in cashtomcap (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtomcap_signflip_252d_3d_v141_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cashpershare (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashpershare_signflip_63d_3d_v142_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in cashpershare (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashpershare_signflip_252d_3d_v143_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cashtoequity (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtoequity_signflip_63d_3d_v144_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in cashtoequity (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtoequity_signflip_252d_3d_v145_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cashtoliab (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtoliab_signflip_63d_3d_v146_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in cashtoliab (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtoliab_signflip_252d_3d_v147_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cashtorev (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtorev_signflip_63d_3d_v148_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in cashtorev (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtorev_signflip_252d_3d_v149_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cashtornd (raw count, no price scaling)
def f001ce_f001_cash_and_equivalents_cashtornd_signflip_63d_3d_v150_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

