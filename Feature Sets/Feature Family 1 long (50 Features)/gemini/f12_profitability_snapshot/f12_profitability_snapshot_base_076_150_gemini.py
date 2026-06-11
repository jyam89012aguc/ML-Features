import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).std().replace(0, np.nan)
def _prof_margin(num, den): return num / den.replace(0, np.nan)
def _prof_roe(ni, eq): return ni / eq.replace(0, np.nan)

def f12_profitability_snapshot_gp_roa_504d_base_v076_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_756d_base_v077_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_1260d_base_v078_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_63d_base_v079_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_126d_base_v080_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_252d_base_v081_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_504d_base_v082_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_756d_base_v083_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_1260d_base_v084_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_63d_base_v085_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_126d_base_v086_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_252d_base_v087_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_504d_base_v088_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_756d_base_v089_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_1260d_base_v090_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_63d_base_v091_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_126d_base_v092_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_252d_base_v093_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_504d_base_v094_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_756d_base_v095_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_1260d_base_v096_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_63d_base_v097_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_126d_base_v098_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_252d_base_v099_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_504d_base_v100_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_756d_base_v101_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_1260d_base_v102_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_63d_base_v103_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_126d_base_v104_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_252d_base_v105_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_504d_base_v106_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_756d_base_v107_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_1260d_base_v108_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_63d_base_v109_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_126d_base_v110_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_252d_base_v111_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_504d_base_v112_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_756d_base_v113_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_1260d_base_v114_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_63d_base_v115_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_126d_base_v116_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_252d_base_v117_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_504d_base_v118_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_756d_base_v119_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_1260d_base_v120_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_63d_base_v121_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_126d_base_v122_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_252d_base_v123_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_504d_base_v124_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_756d_base_v125_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_1260d_base_v126_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_63d_base_v127_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_126d_base_v128_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_252d_base_v129_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_504d_base_v130_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_756d_base_v131_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_1260d_base_v132_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_63d_base_v133_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_126d_base_v134_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_252d_base_v135_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_504d_base_v136_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_756d_base_v137_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_1260d_base_v138_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_63d_base_v139_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_126d_base_v140_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_252d_base_v141_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_504d_base_v142_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_756d_base_v143_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_1260d_base_v144_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_63d_base_v145_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_126d_base_v146_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_252d_base_v147_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_504d_base_v148_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_756d_base_v149_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_1260d_base_v150_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'fundamentals', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'fundamentals.{c}' for c in ['gp', 'netinc', 'ebitda', 'revenue', 'equity', 'assets', 'shareswa']}

F12_PROFITABILITY_SNAPSHOT_BASE_076_150_REGISTRY = {
    "f12_profitability_snapshot_gp_roa_504d_base_v076_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_504d_base_v076_signal},
    "f12_profitability_snapshot_gp_roa_756d_base_v077_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_756d_base_v077_signal},
    "f12_profitability_snapshot_gp_roa_1260d_base_v078_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_1260d_base_v078_signal},
    "f12_profitability_snapshot_ebitda_roe_63d_base_v079_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_63d_base_v079_signal},
    "f12_profitability_snapshot_ebitda_roe_126d_base_v080_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_126d_base_v080_signal},
    "f12_profitability_snapshot_ebitda_roe_252d_base_v081_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_252d_base_v081_signal},
    "f12_profitability_snapshot_ebitda_roe_504d_base_v082_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_504d_base_v082_signal},
    "f12_profitability_snapshot_ebitda_roe_756d_base_v083_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_756d_base_v083_signal},
    "f12_profitability_snapshot_ebitda_roe_1260d_base_v084_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_1260d_base_v084_signal},
    "f12_profitability_snapshot_gp_roe_63d_base_v085_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_63d_base_v085_signal},
    "f12_profitability_snapshot_gp_roe_126d_base_v086_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_126d_base_v086_signal},
    "f12_profitability_snapshot_gp_roe_252d_base_v087_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_252d_base_v087_signal},
    "f12_profitability_snapshot_gp_roe_504d_base_v088_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_504d_base_v088_signal},
    "f12_profitability_snapshot_gp_roe_756d_base_v089_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_756d_base_v089_signal},
    "f12_profitability_snapshot_gp_roe_1260d_base_v090_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_1260d_base_v090_signal},
    "f12_profitability_snapshot_ni_to_gp_63d_base_v091_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_63d_base_v091_signal},
    "f12_profitability_snapshot_ni_to_gp_126d_base_v092_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_126d_base_v092_signal},
    "f12_profitability_snapshot_ni_to_gp_252d_base_v093_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_252d_base_v093_signal},
    "f12_profitability_snapshot_ni_to_gp_504d_base_v094_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_504d_base_v094_signal},
    "f12_profitability_snapshot_ni_to_gp_756d_base_v095_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_756d_base_v095_signal},
    "f12_profitability_snapshot_ni_to_gp_1260d_base_v096_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_1260d_base_v096_signal},
    "f12_profitability_snapshot_ni_to_ebitda_63d_base_v097_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_63d_base_v097_signal},
    "f12_profitability_snapshot_ni_to_ebitda_126d_base_v098_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_126d_base_v098_signal},
    "f12_profitability_snapshot_ni_to_ebitda_252d_base_v099_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_252d_base_v099_signal},
    "f12_profitability_snapshot_ni_to_ebitda_504d_base_v100_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_504d_base_v100_signal},
    "f12_profitability_snapshot_ni_to_ebitda_756d_base_v101_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_756d_base_v101_signal},
    "f12_profitability_snapshot_ni_to_ebitda_1260d_base_v102_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_1260d_base_v102_signal},
    "f12_profitability_snapshot_ebitda_to_gp_63d_base_v103_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_63d_base_v103_signal},
    "f12_profitability_snapshot_ebitda_to_gp_126d_base_v104_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_126d_base_v104_signal},
    "f12_profitability_snapshot_ebitda_to_gp_252d_base_v105_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_252d_base_v105_signal},
    "f12_profitability_snapshot_ebitda_to_gp_504d_base_v106_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_504d_base_v106_signal},
    "f12_profitability_snapshot_ebitda_to_gp_756d_base_v107_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_756d_base_v107_signal},
    "f12_profitability_snapshot_ebitda_to_gp_1260d_base_v108_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_1260d_base_v108_signal},
    "f12_profitability_snapshot_cogs_to_rev_63d_base_v109_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_63d_base_v109_signal},
    "f12_profitability_snapshot_cogs_to_rev_126d_base_v110_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_126d_base_v110_signal},
    "f12_profitability_snapshot_cogs_to_rev_252d_base_v111_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_252d_base_v111_signal},
    "f12_profitability_snapshot_cogs_to_rev_504d_base_v112_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_504d_base_v112_signal},
    "f12_profitability_snapshot_cogs_to_rev_756d_base_v113_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_756d_base_v113_signal},
    "f12_profitability_snapshot_cogs_to_rev_1260d_base_v114_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_1260d_base_v114_signal},
    "f12_profitability_snapshot_opex_to_rev_63d_base_v115_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_63d_base_v115_signal},
    "f12_profitability_snapshot_opex_to_rev_126d_base_v116_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_126d_base_v116_signal},
    "f12_profitability_snapshot_opex_to_rev_252d_base_v117_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_252d_base_v117_signal},
    "f12_profitability_snapshot_opex_to_rev_504d_base_v118_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_504d_base_v118_signal},
    "f12_profitability_snapshot_opex_to_rev_756d_base_v119_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_756d_base_v119_signal},
    "f12_profitability_snapshot_opex_to_rev_1260d_base_v120_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_1260d_base_v120_signal},
    "f12_profitability_snapshot_tax_int_to_rev_63d_base_v121_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_63d_base_v121_signal},
    "f12_profitability_snapshot_tax_int_to_rev_126d_base_v122_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_126d_base_v122_signal},
    "f12_profitability_snapshot_tax_int_to_rev_252d_base_v123_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_252d_base_v123_signal},
    "f12_profitability_snapshot_tax_int_to_rev_504d_base_v124_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_504d_base_v124_signal},
    "f12_profitability_snapshot_tax_int_to_rev_756d_base_v125_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_756d_base_v125_signal},
    "f12_profitability_snapshot_tax_int_to_rev_1260d_base_v126_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_1260d_base_v126_signal},
    "f12_profitability_snapshot_equity_to_assets_63d_base_v127_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_63d_base_v127_signal},
    "f12_profitability_snapshot_equity_to_assets_126d_base_v128_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_126d_base_v128_signal},
    "f12_profitability_snapshot_equity_to_assets_252d_base_v129_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_252d_base_v129_signal},
    "f12_profitability_snapshot_equity_to_assets_504d_base_v130_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_504d_base_v130_signal},
    "f12_profitability_snapshot_equity_to_assets_756d_base_v131_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_756d_base_v131_signal},
    "f12_profitability_snapshot_equity_to_assets_1260d_base_v132_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_1260d_base_v132_signal},
    "f12_profitability_snapshot_shares_to_assets_63d_base_v133_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_63d_base_v133_signal},
    "f12_profitability_snapshot_shares_to_assets_126d_base_v134_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_126d_base_v134_signal},
    "f12_profitability_snapshot_shares_to_assets_252d_base_v135_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_252d_base_v135_signal},
    "f12_profitability_snapshot_shares_to_assets_504d_base_v136_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_504d_base_v136_signal},
    "f12_profitability_snapshot_shares_to_assets_756d_base_v137_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_756d_base_v137_signal},
    "f12_profitability_snapshot_shares_to_assets_1260d_base_v138_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_1260d_base_v138_signal},
    "f12_profitability_snapshot_shares_to_rev_63d_base_v139_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_63d_base_v139_signal},
    "f12_profitability_snapshot_shares_to_rev_126d_base_v140_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_126d_base_v140_signal},
    "f12_profitability_snapshot_shares_to_rev_252d_base_v141_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_252d_base_v141_signal},
    "f12_profitability_snapshot_shares_to_rev_504d_base_v142_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_504d_base_v142_signal},
    "f12_profitability_snapshot_shares_to_rev_756d_base_v143_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_756d_base_v143_signal},
    "f12_profitability_snapshot_shares_to_rev_1260d_base_v144_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_1260d_base_v144_signal},
    "f12_profitability_snapshot_gp_to_cogs_63d_base_v145_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_63d_base_v145_signal},
    "f12_profitability_snapshot_gp_to_cogs_126d_base_v146_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_126d_base_v146_signal},
    "f12_profitability_snapshot_gp_to_cogs_252d_base_v147_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_252d_base_v147_signal},
    "f12_profitability_snapshot_gp_to_cogs_504d_base_v148_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_504d_base_v148_signal},
    "f12_profitability_snapshot_gp_to_cogs_756d_base_v149_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_756d_base_v149_signal},
    "f12_profitability_snapshot_gp_to_cogs_1260d_base_v150_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_1260d_base_v150_signal}
}

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    sz = 1500
    d = pd.DataFrame({
        'gp': np.random.uniform(40, 60, sz).cumsum(),
        'netinc': np.random.uniform(5, 15, sz).cumsum(),
        'ebitda': np.random.uniform(20, 35, sz).cumsum(),
        'revenue': np.random.uniform(80, 120, sz).cumsum(),
        'equity': np.random.uniform(100, 200, sz).cumsum(),
        'assets': np.random.uniform(300, 500, sz).cumsum(),
        'shareswa': pd.Series([100.0]*sz),
        'ticker': ['T']*sz,
        'date': pd.date_range('2010-01-01', periods=sz)
    })
    for n, c in F12_PROFITABILITY_SNAPSHOT_BASE_076_150_REGISTRY.items():
        r = c['func'](**{i: d[i.replace('arg_', '')] for i in c['inputs']})
        assert isinstance(r, pd.Series), f'{n} failed'
        assert len(r) > 0, f'{n} empty'
        assert r.nunique() > 2, f'{n} too few unique values: {r.nunique()}'
        assert r.std() > 0, f'{n} zero std'
    print('OK')
