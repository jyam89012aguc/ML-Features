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
def _f001_cash_per_asset(cashneq, assets):
    return cashneq / assets.replace(0, np.nan).abs()


def _f001_cash_per_marketcap(cashneq, marketcap):
    return cashneq / marketcap.replace(0, np.nan).abs()


def _f001_cash_per_share(cashneq, sharesbas):
    return cashneq / sharesbas.replace(0, np.nan).abs()


def _f001_cash_log(cashneq):
    return np.log(cashneq.abs().replace(0, np.nan))


# 63d z-score of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_z_63d_base_v076_signal(cashneq, closeadj):
    base = cashneq
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_z_126d_base_v077_signal(cashneq, closeadj):
    base = cashneq
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_z_252d_base_v078_signal(cashneq, closeadj):
    base = cashneq
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_z_504d_base_v079_signal(cashneq, closeadj):
    base = cashneq
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_z_63d_base_v080_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_z_126d_base_v081_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_z_252d_base_v082_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_z_504d_base_v083_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_z_63d_base_v084_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_z_126d_base_v085_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_z_252d_base_v086_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_z_504d_base_v087_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_z_63d_base_v088_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_z_126d_base_v089_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_z_252d_base_v090_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_z_504d_base_v091_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_z_63d_base_v092_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_z_126d_base_v093_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_z_252d_base_v094_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_z_504d_base_v095_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_z_63d_base_v096_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_z_126d_base_v097_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_z_252d_base_v098_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_z_504d_base_v099_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_z_63d_base_v100_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_z_126d_base_v101_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_z_252d_base_v102_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_z_504d_base_v103_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_z_63d_base_v104_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_z_126d_base_v105_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_z_252d_base_v106_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_z_504d_base_v107_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of logcash
def f001ce_f001_cash_and_equivalents_logcash_z_63d_base_v108_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of logcash
def f001ce_f001_cash_and_equivalents_logcash_z_126d_base_v109_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of logcash
def f001ce_f001_cash_and_equivalents_logcash_z_252d_base_v110_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of logcash
def f001ce_f001_cash_and_equivalents_logcash_z_504d_base_v111_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_distmax_252d_base_v112_signal(cashneq, closeadj):
    base = cashneq
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_distmax_504d_base_v113_signal(cashneq, closeadj):
    base = cashneq
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_distmax_252d_base_v114_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_distmax_504d_base_v115_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_distmax_252d_base_v116_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_distmax_504d_base_v117_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_distmax_252d_base_v118_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_distmax_504d_base_v119_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_distmax_252d_base_v120_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_distmax_504d_base_v121_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_distmax_252d_base_v122_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_distmax_504d_base_v123_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_distmax_252d_base_v124_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_distmax_504d_base_v125_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_distmax_252d_base_v126_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cashtornd
def f001ce_f001_cash_and_equivalents_cashtornd_distmax_504d_base_v127_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of logcash
def f001ce_f001_cash_and_equivalents_logcash_distmax_252d_base_v128_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of logcash
def f001ce_f001_cash_and_equivalents_logcash_distmax_504d_base_v129_signal(cashneq, closeadj):
    base = _f001_cash_log(cashneq)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_distmed_126d_base_v130_signal(cashneq, closeadj):
    base = cashneq
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_distmed_252d_base_v131_signal(cashneq, closeadj):
    base = cashneq
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of cashneq_lvl
def f001ce_f001_cash_and_equivalents_cashneq_lvl_distmed_504d_base_v132_signal(cashneq, closeadj):
    base = cashneq
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_distmed_126d_base_v133_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_distmed_252d_base_v134_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of cashtoasset
def f001ce_f001_cash_and_equivalents_cashtoasset_distmed_504d_base_v135_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_distmed_126d_base_v136_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_distmed_252d_base_v137_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of cashtomcap
def f001ce_f001_cash_and_equivalents_cashtomcap_distmed_504d_base_v138_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_distmed_126d_base_v139_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_distmed_252d_base_v140_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of cashpershare
def f001ce_f001_cash_and_equivalents_cashpershare_distmed_504d_base_v141_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_distmed_126d_base_v142_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_distmed_252d_base_v143_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of cashtoequity
def f001ce_f001_cash_and_equivalents_cashtoequity_distmed_504d_base_v144_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_distmed_126d_base_v145_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_distmed_252d_base_v146_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of cashtoliab
def f001ce_f001_cash_and_equivalents_cashtoliab_distmed_504d_base_v147_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_distmed_126d_base_v148_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_distmed_252d_base_v149_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of cashtorev
def f001ce_f001_cash_and_equivalents_cashtorev_distmed_504d_base_v150_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

