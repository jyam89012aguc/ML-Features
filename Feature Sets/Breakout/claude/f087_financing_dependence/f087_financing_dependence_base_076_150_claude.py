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
def _f087_ext_financing(debt, sharesbas, w):
    d_chg = debt.diff(periods=w) / debt.abs().shift(w).replace(0, np.nan)
    s_chg = sharesbas.diff(periods=w) / sharesbas.abs().shift(w).replace(0, np.nan)
    return d_chg + s_chg


def _f087_financing_to_assets(debt, sharesbas, assets, w):
    d_chg = debt.diff(periods=w)
    s_chg = sharesbas.diff(periods=w) * 1.0
    return (d_chg + s_chg * 1e1) / assets.abs().replace(0, np.nan)


def _f087_capital_dependence(debt, equity, w):
    cap = debt + equity
    return debt / cap.replace(0, np.nan) - (debt.shift(w) / cap.shift(w).replace(0, np.nan))


# v076 21d financing × close × tanh
def f087fdp_f087_financing_dependence_extfintanh_21d_base_v076_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = np.tanh(base * 5.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077 63d financing × close × tanh
def f087fdp_f087_financing_dependence_extfintanh_63d_base_v077_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = np.tanh(base * 5.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078 252d financing × close × tanh
def f087fdp_f087_financing_dependence_extfintanh_252d_base_v078_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = np.tanh(base * 5.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079 21d financing × close shifted 5d
def f087fdp_f087_financing_dependence_extfinlag_21d_base_v079_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21).shift(5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080 63d financing × close shifted 21d
def f087fdp_f087_financing_dependence_extfinlag_63d_base_v080_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63).shift(21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081 252d financing × close shifted 63d
def f087fdp_f087_financing_dependence_extfinlag_252d_base_v081_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252).shift(63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082 21d financing × close × asset turnover proxy
def f087fdp_f087_financing_dependence_extfinxat_21d_base_v082_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    at = (assets / assets.shift(252).replace(0, np.nan)).clip(0.5, 2.0)
    result = base * at * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083 63d financing × close × asset turnover proxy
def f087fdp_f087_financing_dependence_extfinxat_63d_base_v083_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    at = (assets / assets.shift(252).replace(0, np.nan)).clip(0.5, 2.0)
    result = base * at * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084 252d financing × close × asset turnover proxy
def f087fdp_f087_financing_dependence_extfinxat_252d_base_v084_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    at = (assets / assets.shift(252).replace(0, np.nan)).clip(0.5, 2.0)
    result = base * at * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085 21d fta × close × tanh
def f087fdp_f087_financing_dependence_ftatanh_21d_base_v085_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21)
    result = np.tanh(base * 50.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086 63d fta × close × tanh
def f087fdp_f087_financing_dependence_ftatanh_63d_base_v086_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63)
    result = np.tanh(base * 50.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087 252d fta × close × tanh
def f087fdp_f087_financing_dependence_ftatanh_252d_base_v087_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252)
    result = np.tanh(base * 50.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088 21d fta sign × close
def f087fdp_f087_financing_dependence_ftasign_21d_base_v088_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089 63d fta sign × close
def f087fdp_f087_financing_dependence_ftasign_63d_base_v089_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090 252d fta sign × close
def f087fdp_f087_financing_dependence_ftasign_252d_base_v090_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091 21d financing × close × log assets
def f087fdp_f087_financing_dependence_extfinxla2_21d_base_v091_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base * closeadj * np.log(assets.abs().replace(0, np.nan).pow(0.5))
    return result.replace([np.inf, -np.inf], np.nan)


# v092 63d financing × close × log assets
def f087fdp_f087_financing_dependence_extfinxla2_63d_base_v092_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base * closeadj * np.log(assets.abs().replace(0, np.nan).pow(0.5))
    return result.replace([np.inf, -np.inf], np.nan)


# v093 252d financing × close × log assets
def f087fdp_f087_financing_dependence_extfinxla2_252d_base_v093_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base * closeadj * np.log(assets.abs().replace(0, np.nan).pow(0.5))
    return result.replace([np.inf, -np.inf], np.nan)


# v094 21d financing mean × close × debt/equity
def f087fdp_f087_financing_dependence_extfinxde_21d_base_v094_signal(debt, sharesbas, equity, closeadj):
    base = _mean(_f087_ext_financing(debt, sharesbas, 21), 63)
    de = (debt / equity.replace(0, np.nan)).clip(0, 5)
    result = base * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095 63d financing mean × close × de
def f087fdp_f087_financing_dependence_extfinxde_63d_base_v095_signal(debt, sharesbas, equity, closeadj):
    base = _mean(_f087_ext_financing(debt, sharesbas, 63), 126)
    de = (debt / equity.replace(0, np.nan)).clip(0, 5)
    result = base * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096 252d financing mean × close × de
def f087fdp_f087_financing_dependence_extfinxde_252d_base_v096_signal(debt, sharesbas, equity, closeadj):
    base = _mean(_f087_ext_financing(debt, sharesbas, 252), 252)
    de = (debt / equity.replace(0, np.nan)).clip(0, 5)
    result = base * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097 21d financing × close × shares log
def f087fdp_f087_financing_dependence_extfinxls_21d_base_v097_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base * closeadj * np.log(sharesbas.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v098 63d financing × close × shares log
def f087fdp_f087_financing_dependence_extfinxls_63d_base_v098_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base * closeadj * np.log(sharesbas.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v099 252d financing × close × shares log
def f087fdp_f087_financing_dependence_extfinxls_252d_base_v099_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base * closeadj * np.log(sharesbas.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v100 21d financing max × close
def f087fdp_f087_financing_dependence_extfinmax_21d_base_v100_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101 63d financing max × close
def f087fdp_f087_financing_dependence_extfinmax_63d_base_v101_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base.rolling(126, min_periods=42).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102 252d financing max × close
def f087fdp_f087_financing_dependence_extfinmax_252d_base_v102_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103 21d financing min × close
def f087fdp_f087_financing_dependence_extfinmin_21d_base_v103_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104 63d financing min × close
def f087fdp_f087_financing_dependence_extfinmin_63d_base_v104_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base.rolling(126, min_periods=42).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105 252d financing min × close
def f087fdp_f087_financing_dependence_extfinmin_252d_base_v105_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106 21d financing range × close
def f087fdp_f087_financing_dependence_extfinrange_21d_base_v106_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    rng = base.rolling(126, min_periods=42).max() - base.rolling(126, min_periods=42).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107 63d financing range × close
def f087fdp_f087_financing_dependence_extfinrange_63d_base_v107_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108 252d financing range × close
def f087fdp_f087_financing_dependence_extfinrange_252d_base_v108_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    rng = base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109 21d short/long financing ratio × close
def f087fdp_f087_financing_dependence_finratio_21v252_base_v109_signal(debt, sharesbas, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 21)
    b = _f087_ext_financing(debt, sharesbas, 252).abs() + 1e-9
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110 63d short/long financing ratio × close
def f087fdp_f087_financing_dependence_finratio_63v504_base_v110_signal(debt, sharesbas, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 63)
    b = _f087_ext_financing(debt, sharesbas, 504).abs() + 1e-9
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111 21d-63d financing diff × close
def f087fdp_f087_financing_dependence_findiff_21m63_base_v111_signal(debt, sharesbas, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 21)
    b = _f087_ext_financing(debt, sharesbas, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112 63d-252d financing diff × close
def f087fdp_f087_financing_dependence_findiff_63m252_base_v112_signal(debt, sharesbas, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 63)
    b = _f087_ext_financing(debt, sharesbas, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113 21d financing × close × debt log
def f087fdp_f087_financing_dependence_extfinxld_21d_base_v113_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base * closeadj * np.log(debt.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v114 63d financing × close × debt log
def f087fdp_f087_financing_dependence_extfinxld_63d_base_v114_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base * closeadj * np.log(debt.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v115 252d financing × close × debt log
def f087fdp_f087_financing_dependence_extfinxld_252d_base_v115_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base * closeadj * np.log(debt.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v116 21d capdep × close × debt
def f087fdp_f087_financing_dependence_capdepxd_21d_base_v116_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21)
    result = base * closeadj * np.log(debt.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v117 63d capdep × close × debt
def f087fdp_f087_financing_dependence_capdepxd_63d_base_v117_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63)
    result = base * closeadj * np.log(debt.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v118 252d capdep × close × debt
def f087fdp_f087_financing_dependence_capdepxd_252d_base_v118_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252)
    result = base * closeadj * np.log(debt.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v119 21d capdep × close × equity
def f087fdp_f087_financing_dependence_capdepxe_21d_base_v119_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21)
    result = base * closeadj * np.log(equity.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v120 63d capdep × close × equity
def f087fdp_f087_financing_dependence_capdepxe_63d_base_v120_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63)
    result = base * closeadj * np.log(equity.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v121 252d capdep × close × equity
def f087fdp_f087_financing_dependence_capdepxe_252d_base_v121_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252)
    result = base * closeadj * np.log(equity.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v122 21d capdep std × close
def f087fdp_f087_financing_dependence_capdepstd_21d_base_v122_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123 63d capdep std × close
def f087fdp_f087_financing_dependence_capdepstd_63d_base_v123_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124 252d capdep std × close
def f087fdp_f087_financing_dependence_capdepstd_252d_base_v124_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125 21d capdep × ext financing × close
def f087fdp_f087_financing_dependence_capdepxef_21d_base_v125_signal(debt, sharesbas, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 21)
    b = _f087_ext_financing(debt, sharesbas, 21)
    result = (a * b) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v126 63d capdep × ext financing × close
def f087fdp_f087_financing_dependence_capdepxef_63d_base_v126_signal(debt, sharesbas, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 63)
    b = _f087_ext_financing(debt, sharesbas, 63)
    result = (a * b) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v127 252d capdep × ext financing × close
def f087fdp_f087_financing_dependence_capdepxef_252d_base_v127_signal(debt, sharesbas, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 252)
    b = _f087_ext_financing(debt, sharesbas, 252)
    result = (a * b) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v128 21d capdep ratio × close
def f087fdp_f087_financing_dependence_capdepratio_21d_base_v128_signal(debt, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 21)
    base_lvl = (debt / (debt + equity).replace(0, np.nan)).clip(0, 1)
    result = a * base_lvl * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# v129 63d capdep ratio × close
def f087fdp_f087_financing_dependence_capdepratio_63d_base_v129_signal(debt, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 63)
    base_lvl = (debt / (debt + equity).replace(0, np.nan)).clip(0, 1)
    result = a * base_lvl * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# v130 252d capdep ratio × close
def f087fdp_f087_financing_dependence_capdepratio_252d_base_v130_signal(debt, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 252)
    base_lvl = (debt / (debt + equity).replace(0, np.nan)).clip(0, 1)
    result = a * base_lvl * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# v131 21d fta squared × close
def f087fdp_f087_financing_dependence_ftasq_21d_base_v131_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21)
    result = (base * base.abs()) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v132 63d fta squared × close
def f087fdp_f087_financing_dependence_ftasq_63d_base_v132_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63)
    result = (base * base.abs()) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v133 252d fta squared × close
def f087fdp_f087_financing_dependence_ftasq_252d_base_v133_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252)
    result = (base * base.abs()) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v134 21d fta range × close
def f087fdp_f087_financing_dependence_ftarange_21d_base_v134_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21)
    rng = base.rolling(126, min_periods=42).max() - base.rolling(126, min_periods=42).min()
    result = rng * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v135 63d fta range × close
def f087fdp_f087_financing_dependence_ftarange_63d_base_v135_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v136 252d fta range × close
def f087fdp_f087_financing_dependence_ftarange_252d_base_v136_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252)
    rng = base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()
    result = rng * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v137 21d ext financing count > 0 × close
def f087fdp_f087_financing_dependence_extfincount_21d_base_v137_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    cnt = (base > 0).astype(float).rolling(126, min_periods=21).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138 63d ext financing count > 0 × close
def f087fdp_f087_financing_dependence_extfincount_63d_base_v138_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    cnt = (base > 0).astype(float).rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139 252d ext financing count > 0 × close
def f087fdp_f087_financing_dependence_extfincount_252d_base_v139_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    cnt = (base > 0).astype(float).rolling(504, min_periods=126).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140 21d ext financing area cumulative × close
def f087fdp_f087_financing_dependence_extfinarea_21d_base_v140_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141 63d ext financing area × close
def f087fdp_f087_financing_dependence_extfinarea_63d_base_v141_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142 21d ext financing sharpe × close
def f087fdp_f087_financing_dependence_extfinsharpe_21d_base_v142_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    s = _std(base, 252).replace(0, np.nan)
    result = (base / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143 63d ext financing sharpe × close
def f087fdp_f087_financing_dependence_extfinsharpe_63d_base_v143_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    s = _std(base, 252).replace(0, np.nan)
    result = (base / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144 252d ext financing sharpe × close
def f087fdp_f087_financing_dependence_extfinsharpe_252d_base_v144_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    s = _std(base, 504).replace(0, np.nan)
    result = (base / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145 21d capdep min × close
def f087fdp_f087_financing_dependence_capdepmin_21d_base_v145_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# v146 63d capdep min × close
def f087fdp_f087_financing_dependence_capdepmin_63d_base_v146_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63)
    result = base.rolling(126, min_periods=42).min() * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# v147 252d capdep min × close
def f087fdp_f087_financing_dependence_capdepmin_252d_base_v147_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252)
    result = base.rolling(252, min_periods=63).min() * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# v148 21d capdep max × close
def f087fdp_f087_financing_dependence_capdepmax_21d_base_v148_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# v149 63d capdep max × close
def f087fdp_f087_financing_dependence_capdepmax_63d_base_v149_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63)
    result = base.rolling(126, min_periods=42).max() * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# v150 252d capdep max × close
def f087fdp_f087_financing_dependence_capdepmax_252d_base_v150_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252)
    result = base.rolling(252, min_periods=63).max() * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f087fdp_f087_financing_dependence_extfintanh_21d_base_v076_signal,
    f087fdp_f087_financing_dependence_extfintanh_63d_base_v077_signal,
    f087fdp_f087_financing_dependence_extfintanh_252d_base_v078_signal,
    f087fdp_f087_financing_dependence_extfinlag_21d_base_v079_signal,
    f087fdp_f087_financing_dependence_extfinlag_63d_base_v080_signal,
    f087fdp_f087_financing_dependence_extfinlag_252d_base_v081_signal,
    f087fdp_f087_financing_dependence_extfinxat_21d_base_v082_signal,
    f087fdp_f087_financing_dependence_extfinxat_63d_base_v083_signal,
    f087fdp_f087_financing_dependence_extfinxat_252d_base_v084_signal,
    f087fdp_f087_financing_dependence_ftatanh_21d_base_v085_signal,
    f087fdp_f087_financing_dependence_ftatanh_63d_base_v086_signal,
    f087fdp_f087_financing_dependence_ftatanh_252d_base_v087_signal,
    f087fdp_f087_financing_dependence_ftasign_21d_base_v088_signal,
    f087fdp_f087_financing_dependence_ftasign_63d_base_v089_signal,
    f087fdp_f087_financing_dependence_ftasign_252d_base_v090_signal,
    f087fdp_f087_financing_dependence_extfinxla2_21d_base_v091_signal,
    f087fdp_f087_financing_dependence_extfinxla2_63d_base_v092_signal,
    f087fdp_f087_financing_dependence_extfinxla2_252d_base_v093_signal,
    f087fdp_f087_financing_dependence_extfinxde_21d_base_v094_signal,
    f087fdp_f087_financing_dependence_extfinxde_63d_base_v095_signal,
    f087fdp_f087_financing_dependence_extfinxde_252d_base_v096_signal,
    f087fdp_f087_financing_dependence_extfinxls_21d_base_v097_signal,
    f087fdp_f087_financing_dependence_extfinxls_63d_base_v098_signal,
    f087fdp_f087_financing_dependence_extfinxls_252d_base_v099_signal,
    f087fdp_f087_financing_dependence_extfinmax_21d_base_v100_signal,
    f087fdp_f087_financing_dependence_extfinmax_63d_base_v101_signal,
    f087fdp_f087_financing_dependence_extfinmax_252d_base_v102_signal,
    f087fdp_f087_financing_dependence_extfinmin_21d_base_v103_signal,
    f087fdp_f087_financing_dependence_extfinmin_63d_base_v104_signal,
    f087fdp_f087_financing_dependence_extfinmin_252d_base_v105_signal,
    f087fdp_f087_financing_dependence_extfinrange_21d_base_v106_signal,
    f087fdp_f087_financing_dependence_extfinrange_63d_base_v107_signal,
    f087fdp_f087_financing_dependence_extfinrange_252d_base_v108_signal,
    f087fdp_f087_financing_dependence_finratio_21v252_base_v109_signal,
    f087fdp_f087_financing_dependence_finratio_63v504_base_v110_signal,
    f087fdp_f087_financing_dependence_findiff_21m63_base_v111_signal,
    f087fdp_f087_financing_dependence_findiff_63m252_base_v112_signal,
    f087fdp_f087_financing_dependence_extfinxld_21d_base_v113_signal,
    f087fdp_f087_financing_dependence_extfinxld_63d_base_v114_signal,
    f087fdp_f087_financing_dependence_extfinxld_252d_base_v115_signal,
    f087fdp_f087_financing_dependence_capdepxd_21d_base_v116_signal,
    f087fdp_f087_financing_dependence_capdepxd_63d_base_v117_signal,
    f087fdp_f087_financing_dependence_capdepxd_252d_base_v118_signal,
    f087fdp_f087_financing_dependence_capdepxe_21d_base_v119_signal,
    f087fdp_f087_financing_dependence_capdepxe_63d_base_v120_signal,
    f087fdp_f087_financing_dependence_capdepxe_252d_base_v121_signal,
    f087fdp_f087_financing_dependence_capdepstd_21d_base_v122_signal,
    f087fdp_f087_financing_dependence_capdepstd_63d_base_v123_signal,
    f087fdp_f087_financing_dependence_capdepstd_252d_base_v124_signal,
    f087fdp_f087_financing_dependence_capdepxef_21d_base_v125_signal,
    f087fdp_f087_financing_dependence_capdepxef_63d_base_v126_signal,
    f087fdp_f087_financing_dependence_capdepxef_252d_base_v127_signal,
    f087fdp_f087_financing_dependence_capdepratio_21d_base_v128_signal,
    f087fdp_f087_financing_dependence_capdepratio_63d_base_v129_signal,
    f087fdp_f087_financing_dependence_capdepratio_252d_base_v130_signal,
    f087fdp_f087_financing_dependence_ftasq_21d_base_v131_signal,
    f087fdp_f087_financing_dependence_ftasq_63d_base_v132_signal,
    f087fdp_f087_financing_dependence_ftasq_252d_base_v133_signal,
    f087fdp_f087_financing_dependence_ftarange_21d_base_v134_signal,
    f087fdp_f087_financing_dependence_ftarange_63d_base_v135_signal,
    f087fdp_f087_financing_dependence_ftarange_252d_base_v136_signal,
    f087fdp_f087_financing_dependence_extfincount_21d_base_v137_signal,
    f087fdp_f087_financing_dependence_extfincount_63d_base_v138_signal,
    f087fdp_f087_financing_dependence_extfincount_252d_base_v139_signal,
    f087fdp_f087_financing_dependence_extfinarea_21d_base_v140_signal,
    f087fdp_f087_financing_dependence_extfinarea_63d_base_v141_signal,
    f087fdp_f087_financing_dependence_extfinsharpe_21d_base_v142_signal,
    f087fdp_f087_financing_dependence_extfinsharpe_63d_base_v143_signal,
    f087fdp_f087_financing_dependence_extfinsharpe_252d_base_v144_signal,
    f087fdp_f087_financing_dependence_capdepmin_21d_base_v145_signal,
    f087fdp_f087_financing_dependence_capdepmin_63d_base_v146_signal,
    f087fdp_f087_financing_dependence_capdepmin_252d_base_v147_signal,
    f087fdp_f087_financing_dependence_capdepmax_21d_base_v148_signal,
    f087fdp_f087_financing_dependence_capdepmax_63d_base_v149_signal,
    f087fdp_f087_financing_dependence_capdepmax_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F087_FINANCING_DEPENDENCE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")

    cols = {"closeadj": closeadj, "debt": debt, "sharesbas": sharesbas, "assets": assets, "equity": equity}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f087_ext_financing", "_f087_financing_to_assets", "_f087_capital_dependence")
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
    print(f"OK f087_financing_dependence_base_076_150_claude: {n_features} features pass")
