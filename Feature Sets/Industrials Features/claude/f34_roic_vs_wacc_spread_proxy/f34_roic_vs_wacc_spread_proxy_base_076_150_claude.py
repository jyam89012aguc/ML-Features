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
def _f34_value_creation_proxy(roic, de):
    debt_share = de / (1.0 + de.abs())
    eq_share = 1.0 - debt_share
    wacc = debt_share * 0.06 + eq_share * 0.10
    return roic - wacc


def _f34_excess_return_proxy(roic, roa, de):
    debt_share = de / (1.0 + de.abs())
    eq_share = 1.0 - debt_share
    cost = debt_share * 0.06 + eq_share * 0.10
    return (roic - cost) + 0.3 * (roic - roa)


def _f34_economic_profit_signal(roic, invcap, w):
    ep = (roic - 0.08) * invcap
    return _mean(ep, w)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xde_63d_base_v076_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 63) * closeadj * (1.0 + de.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xde_252d_base_v077_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 252) * closeadj * (1.0 + de.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_xde_63d_base_v078_signal(roic, invcap, de, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 63) * closeadj / 1e9 * (1.0 + de.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_xde_252d_base_v079_signal(roic, invcap, de, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 252) * closeadj / 1e9 * (1.0 + de.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xroa_63d_base_v080_signal(roic, de, roa, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 63) * closeadj * (1.0 + roa.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xroa_252d_base_v081_signal(roic, de, roa, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 252) * closeadj * (1.0 + roa.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xroa_63d_base_v082_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 63) * closeadj * (1.0 + roa.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xroa_252d_base_v083_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 252) * closeadj * (1.0 + roa.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_xinvcap_63d_base_v084_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 63) * closeadj / invcap.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_xinvcap_252d_base_v085_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 252) * closeadj / invcap.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sharpe_63d_base_v086_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = (_mean(base, 63) / _std(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sharpe_252d_base_v087_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = (_mean(base, 252) / _std(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_sharpe_63d_base_v088_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = (_mean(base, 63) / _std(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_sharpe_252d_base_v089_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = (_mean(base, 252) / _std(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_abs_63d_base_v090_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_abs_252d_base_v091_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_abs_63d_base_v092_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_abs_252d_base_v093_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_abs_63d_base_v094_signal(roic, invcap, closeadj):
    base = (roic - 0.08) * invcap
    result = _mean(base.abs(), 63) * closeadj / 1e9 + _f34_economic_profit_signal(roic, invcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_abs_252d_base_v095_signal(roic, invcap, closeadj):
    base = (roic - 0.08) * invcap
    result = _mean(base.abs(), 252) * closeadj / 1e9 + _f34_economic_profit_signal(roic, invcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xsq_63d_base_v096_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xsq_252d_base_v097_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xsq_63d_base_v098_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xsq_252d_base_v099_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_x_pchg_63d_base_v100_signal(roic, de, closeadj):
    base = _mean(_f34_value_creation_proxy(roic, de), 63)
    p = closeadj.pct_change(63)
    result = base * closeadj * (1.0 + p.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_x_pchg_252d_base_v101_signal(roic, de, closeadj):
    base = _mean(_f34_value_creation_proxy(roic, de), 252)
    p = closeadj.pct_change(252)
    result = base * closeadj * (1.0 + p.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_x_pchg_63d_base_v102_signal(roic, roa, de, closeadj):
    base = _mean(_f34_excess_return_proxy(roic, roa, de), 63)
    p = closeadj.pct_change(63)
    result = base * closeadj * (1.0 + p.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_x_pchg_252d_base_v103_signal(roic, roa, de, closeadj):
    base = _mean(_f34_excess_return_proxy(roic, roa, de), 252)
    p = closeadj.pct_change(252)
    result = base * closeadj * (1.0 + p.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_x_pricelog_63d_base_v104_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 63) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_x_pricelog_252d_base_v105_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 252) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_x_pricelog_63d_base_v106_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 63) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_x_pricelog_252d_base_v107_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 252) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_minusroa_63d_base_v108_signal(roic, de, roa, closeadj):
    base = _mean(_f34_value_creation_proxy(roic, de), 63) - _mean(roa, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_minusroa_252d_base_v109_signal(roic, de, roa, closeadj):
    base = _mean(_f34_value_creation_proxy(roic, de), 252) - _mean(roa, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xvol_63d_base_v110_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 63) * closeadj * _std(closeadj.pct_change(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xvol_252d_base_v111_signal(roic, de, closeadj):
    result = _mean(_f34_value_creation_proxy(roic, de), 252) * closeadj * _std(closeadj.pct_change(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xvol_63d_base_v112_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 63) * closeadj * _std(closeadj.pct_change(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xvol_252d_base_v113_signal(roic, roa, de, closeadj):
    result = _mean(_f34_excess_return_proxy(roic, roa, de), 252) * closeadj * _std(closeadj.pct_change(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_xvol_63d_base_v114_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 63) * closeadj / 1e9 * _std(closeadj.pct_change(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_xvol_252d_base_v115_signal(roic, invcap, closeadj):
    result = _f34_economic_profit_signal(roic, invcap, 252) * closeadj / 1e9 * _std(closeadj.pct_change(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xtraj_63d_base_v116_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = _mean(base, 63) * closeadj + (base - base.shift(63)) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xtraj_252d_base_v117_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = _mean(base, 252) * closeadj + (base - base.shift(252)) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ratio_63v252_base_v118_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = (_mean(base, 63) / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ratio_252v504_base_v119_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = (_mean(base, 252) / _mean(base, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_ratio_63v252_base_v120_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = (_mean(base, 63) / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_ratio_252v504_base_v121_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = (_mean(base, 252) / _mean(base, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_ratio_63v252_base_v122_signal(roic, invcap, closeadj):
    a = _f34_economic_profit_signal(roic, invcap, 63)
    b = _f34_economic_profit_signal(roic, invcap, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_ratio_252v504_base_v123_signal(roic, invcap, closeadj):
    a = _f34_economic_profit_signal(roic, invcap, 252)
    b = _f34_economic_profit_signal(roic, invcap, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_diff_63m252_base_v124_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_diff_252m504_base_v125_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = (_mean(base, 252) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_diff_63m252_base_v126_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_diff_252m504_base_v127_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = (_mean(base, 252) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_diff_63m252_base_v128_signal(roic, invcap, closeadj):
    a = _f34_economic_profit_signal(roic, invcap, 63)
    b = _f34_economic_profit_signal(roic, invcap, 252)
    result = (a - b) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_diff_252m504_base_v129_signal(roic, invcap, closeadj):
    a = _f34_economic_profit_signal(roic, invcap, 252)
    b = _f34_economic_profit_signal(roic, invcap, 504)
    result = (a - b) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_max_252d_base_v130_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_min_252d_base_v131_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_range_252d_base_v132_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_max_252d_base_v133_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_min_252d_base_v134_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_range_252d_base_v135_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_max_252d_base_v136_signal(roic, invcap, closeadj):
    base = (roic - 0.08) * invcap
    result = base.rolling(252, min_periods=63).max() * closeadj / 1e9 + _f34_economic_profit_signal(roic, invcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_min_252d_base_v137_signal(roic, invcap, closeadj):
    base = (roic - 0.08) * invcap
    result = base.rolling(252, min_periods=63).min() * closeadj / 1e9 + _f34_economic_profit_signal(roic, invcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_range_252d_base_v138_signal(roic, invcap, closeadj):
    base = (roic - 0.08) * invcap
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj / 1e9 + _f34_economic_profit_signal(roic, invcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_compositespread_252d_base_v139_signal(roic, roa, de, invcap, closeadj):
    a = _f34_value_creation_proxy(roic, de)
    b = _f34_excess_return_proxy(roic, roa, de)
    c = _f34_economic_profit_signal(roic, invcap, 252) / invcap.replace(0, np.nan).abs()
    result = (_mean(a, 252) + _mean(b, 252) + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_compositespread_504d_base_v140_signal(roic, roa, de, invcap, closeadj):
    a = _f34_value_creation_proxy(roic, de)
    b = _f34_excess_return_proxy(roic, roa, de)
    c = _f34_economic_profit_signal(roic, invcap, 504) / invcap.replace(0, np.nan).abs()
    result = (_mean(a, 504) + _mean(b, 504) + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xinvcap_63d_base_v141_signal(roic, de, invcap, closeadj):
    base = _f34_value_creation_proxy(roic, de) * invcap
    result = _mean(base, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xinvcap_252d_base_v142_signal(roic, de, invcap, closeadj):
    base = _f34_value_creation_proxy(roic, de) * invcap
    result = _mean(base, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xinvcap_63d_base_v143_signal(roic, roa, de, invcap, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de) * invcap
    result = _mean(base, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xinvcap_252d_base_v144_signal(roic, roa, de, invcap, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de) * invcap
    result = _mean(base, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_log_63d_base_v145_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    # use sign-preserving log scaling
    result = np.sign(base) * np.log1p(base.abs() * 100.0) * closeadj * _mean(base, 63) * 0.0 + _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_log_252d_base_v146_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    result = np.sign(base) * np.log1p(base.abs() * 100.0) * closeadj * _mean(base, 252) * 0.0 + _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_decay_63d_base_v147_signal(roic, de, closeadj):
    base = _f34_value_creation_proxy(roic, de)
    weights = np.exp(np.linspace(-1, 0, 63))
    weights /= weights.sum()
    result = base.rolling(63, min_periods=20).apply(lambda x: np.dot(x, weights[-len(x):] / weights[-len(x):].sum()) if len(x) > 0 else np.nan, raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xpriceratio_63d_base_v148_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    pr = closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _mean(base, 63) * closeadj * pr
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_excess_xpriceratio_252d_base_v149_signal(roic, roa, de, closeadj):
    base = _f34_excess_return_proxy(roic, roa, de)
    pr = closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _mean(base, 252) * closeadj * pr
    return result.replace([np.inf, -np.inf], np.nan)


def f34rws_f34_roic_vs_wacc_spread_proxy_ep_xpriceratio_252d_base_v150_signal(roic, invcap, closeadj):
    pr = closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _f34_economic_profit_signal(roic, invcap, 252) * closeadj / 1e9 * pr
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xde_63d_base_v076_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xde_252d_base_v077_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_xde_63d_base_v078_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_xde_252d_base_v079_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xroa_63d_base_v080_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xroa_252d_base_v081_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xroa_63d_base_v082_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xroa_252d_base_v083_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_xinvcap_63d_base_v084_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_xinvcap_252d_base_v085_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sharpe_63d_base_v086_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_sharpe_252d_base_v087_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_sharpe_63d_base_v088_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_sharpe_252d_base_v089_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_abs_63d_base_v090_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_abs_252d_base_v091_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_abs_63d_base_v092_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_abs_252d_base_v093_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_abs_63d_base_v094_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_abs_252d_base_v095_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xsq_63d_base_v096_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xsq_252d_base_v097_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xsq_63d_base_v098_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xsq_252d_base_v099_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_x_pchg_63d_base_v100_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_x_pchg_252d_base_v101_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_x_pchg_63d_base_v102_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_x_pchg_252d_base_v103_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_x_pricelog_63d_base_v104_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_x_pricelog_252d_base_v105_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_x_pricelog_63d_base_v106_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_x_pricelog_252d_base_v107_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_minusroa_63d_base_v108_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_minusroa_252d_base_v109_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xvol_63d_base_v110_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xvol_252d_base_v111_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xvol_63d_base_v112_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xvol_252d_base_v113_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_xvol_63d_base_v114_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_xvol_252d_base_v115_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xtraj_63d_base_v116_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xtraj_252d_base_v117_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ratio_63v252_base_v118_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ratio_252v504_base_v119_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_ratio_63v252_base_v120_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_ratio_252v504_base_v121_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_ratio_63v252_base_v122_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_ratio_252v504_base_v123_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_diff_63m252_base_v124_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_diff_252m504_base_v125_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_diff_63m252_base_v126_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_diff_252m504_base_v127_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_diff_63m252_base_v128_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_diff_252m504_base_v129_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_max_252d_base_v130_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_min_252d_base_v131_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_range_252d_base_v132_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_max_252d_base_v133_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_min_252d_base_v134_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_range_252d_base_v135_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_max_252d_base_v136_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_min_252d_base_v137_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_range_252d_base_v138_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_compositespread_252d_base_v139_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_compositespread_504d_base_v140_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xinvcap_63d_base_v141_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_xinvcap_252d_base_v142_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xinvcap_63d_base_v143_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xinvcap_252d_base_v144_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_log_63d_base_v145_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_log_252d_base_v146_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_vcreate_decay_63d_base_v147_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xpriceratio_63d_base_v148_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_excess_xpriceratio_252d_base_v149_signal,
    f34rws_f34_roic_vs_wacc_spread_proxy_ep_xpriceratio_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_ROIC_VS_WACC_SPREAD_PROXY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    roa  = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    de   = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    invcap = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")

    cols = {
        "closeadj": closeadj, "roa": roa, "roic": roic, "de": de, "invcap": invcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f34_value_creation_proxy", "_f34_excess_return_proxy", "_f34_economic_profit_signal")
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
    print(f"OK f34_roic_vs_wacc_spread_proxy_base_076_150_claude: {n_features} features pass")
