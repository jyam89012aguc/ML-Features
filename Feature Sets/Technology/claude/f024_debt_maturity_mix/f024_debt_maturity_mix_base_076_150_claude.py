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
def _f024_curshare(debtc, debt):
    return debtc / debt.replace(0, np.nan).abs()


# 63d z-score of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_z_63d_base_v076_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_z_126d_base_v077_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_z_252d_base_v078_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_z_504d_base_v079_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_z_63d_base_v080_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_z_126d_base_v081_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_z_252d_base_v082_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_z_504d_base_v083_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_z_63d_base_v084_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_z_126d_base_v085_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_z_252d_base_v086_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_z_504d_base_v087_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_z_63d_base_v088_signal(debtc, closeadj):
    base = debtc
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_z_126d_base_v089_signal(debtc, closeadj):
    base = debtc
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_z_252d_base_v090_signal(debtc, closeadj):
    base = debtc
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_z_504d_base_v091_signal(debtc, closeadj):
    base = debtc
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_z_63d_base_v092_signal(debtnc, closeadj):
    base = debtnc
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_z_126d_base_v093_signal(debtnc, closeadj):
    base = debtnc
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_z_252d_base_v094_signal(debtnc, closeadj):
    base = debtnc
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_z_504d_base_v095_signal(debtnc, closeadj):
    base = debtnc
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_z_63d_base_v096_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_z_126d_base_v097_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_z_252d_base_v098_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_z_504d_base_v099_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_z_63d_base_v100_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_z_126d_base_v101_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_z_252d_base_v102_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_z_504d_base_v103_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_distmax_252d_base_v104_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_distmax_504d_base_v105_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_distmax_252d_base_v106_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_distmax_504d_base_v107_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_distmax_252d_base_v108_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_distmax_504d_base_v109_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_distmax_252d_base_v110_signal(debtc, closeadj):
    base = debtc
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_distmax_504d_base_v111_signal(debtc, closeadj):
    base = debtc
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_distmax_252d_base_v112_signal(debtnc, closeadj):
    base = debtnc
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_distmax_504d_base_v113_signal(debtnc, closeadj):
    base = debtnc
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_distmax_252d_base_v114_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_distmax_504d_base_v115_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_distmax_252d_base_v116_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_distmax_504d_base_v117_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_distmed_126d_base_v118_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_distmed_252d_base_v119_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_distmed_504d_base_v120_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_distmed_126d_base_v121_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_distmed_252d_base_v122_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_distmed_504d_base_v123_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_distmed_126d_base_v124_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_distmed_252d_base_v125_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_distmed_504d_base_v126_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_distmed_126d_base_v127_signal(debtc, closeadj):
    base = debtc
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_distmed_252d_base_v128_signal(debtc, closeadj):
    base = debtc
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_distmed_504d_base_v129_signal(debtc, closeadj):
    base = debtc
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_distmed_126d_base_v130_signal(debtnc, closeadj):
    base = debtnc
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_distmed_252d_base_v131_signal(debtnc, closeadj):
    base = debtnc
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_distmed_504d_base_v132_signal(debtnc, closeadj):
    base = debtnc
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_distmed_126d_base_v133_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_distmed_252d_base_v134_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_distmed_504d_base_v135_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_distmed_126d_base_v136_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_distmed_252d_base_v137_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_distmed_504d_base_v138_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_chg_63d_base_v139_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_chg_252d_base_v140_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_chg_63d_base_v141_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_chg_252d_base_v142_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_chg_63d_base_v143_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_chg_252d_base_v144_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_chg_63d_base_v145_signal(debtc, closeadj):
    base = debtc
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_chg_252d_base_v146_signal(debtc, closeadj):
    base = debtc
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_chg_63d_base_v147_signal(debtnc, closeadj):
    base = debtnc
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_chg_252d_base_v148_signal(debtnc, closeadj):
    base = debtnc
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_chg_63d_base_v149_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_chg_252d_base_v150_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

