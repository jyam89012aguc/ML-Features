import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _cv(s, w): return _std(s, w) / _sma(s, w).abs().replace(0, np.nan)
def _cf_fcf(ncfo, capex): return ncfo - capex.abs()
def _cf_fcf_ratio(num, den): return num / den.replace(0, np.nan)

# Concepts 13-25 (Features 76-150)

# C13 (remaining): FCF to Capex (76-78)
def f13_cash_flow_snapshot_fcf_to_capex_504d_base_v076_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_capex_756d_base_v077_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_capex_1260d_base_v078_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 1260).replace([np.inf, -np.inf], np.nan)

# C14: OCF to Capex (79-84)
def f13_cash_flow_snapshot_ocf_to_capex_63d_base_v079_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_126d_base_v080_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_252d_base_v081_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_504d_base_v082_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_756d_base_v083_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_1260d_base_v084_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 1260).replace([np.inf, -np.inf], np.nan)

# C15: OCF Z-Score (85-90)
def f13_cash_flow_snapshot_ocf_zscore_63d_base_v085_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_126d_base_v086_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_252d_base_v087_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_504d_base_v088_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_756d_base_v089_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_1260d_base_v090_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 1260).replace([np.inf, -np.inf], np.nan)

# C16: FCF Z-Score (91-96)
def f13_cash_flow_snapshot_fcf_zscore_63d_base_v091_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_126d_base_v092_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_252d_base_v093_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_504d_base_v094_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_756d_base_v095_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_1260d_base_v096_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 1260).replace([np.inf, -np.inf], np.nan)

# C17: Rev Z-Score (97-102)
def f13_cash_flow_snapshot_rev_zscore_63d_base_v097_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_126d_base_v098_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_252d_base_v099_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_504d_base_v100_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_756d_base_v101_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_1260d_base_v102_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 1260).replace([np.inf, -np.inf], np.nan)

# C18: NI Z-Score (103-108)
def f13_cash_flow_snapshot_ni_zscore_63d_base_v103_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_126d_base_v104_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_252d_base_v105_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_504d_base_v106_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_756d_base_v107_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_1260d_base_v108_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 1260).replace([np.inf, -np.inf], np.nan)

# C19: OCF CV (109-114)
def f13_cash_flow_snapshot_ocf_cv_63d_base_v109_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_126d_base_v110_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_252d_base_v111_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_504d_base_v112_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_756d_base_v113_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_1260d_base_v114_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 1260).replace([np.inf, -np.inf], np.nan)

# C20: FCF CV (115-120)
def f13_cash_flow_snapshot_fcf_cv_63d_base_v115_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_126d_base_v116_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_252d_base_v117_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_504d_base_v118_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_756d_base_v119_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_1260d_base_v120_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 1260).replace([np.inf, -np.inf], np.nan)

# C21: Net Margin (121-126)
def f13_cash_flow_snapshot_net_margin_63d_base_v121_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_126d_base_v122_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_252d_base_v123_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_504d_base_v124_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_756d_base_v125_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_1260d_base_v126_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 1260).replace([np.inf, -np.inf], np.nan)

# C22: Capex to NI (127-132)
def f13_cash_flow_snapshot_capex_to_ni_63d_base_v127_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_126d_base_v128_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_252d_base_v129_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_504d_base_v130_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_756d_base_v131_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_1260d_base_v132_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 1260).replace([np.inf, -np.inf], np.nan)

# C23: FCF Z-Score Alt (133-138)
def f13_cash_flow_snapshot_fcf_zscore_alt_63d_base_v133_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 63), _sma(arg_fcf, 63).abs()), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_126d_base_v134_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 126), _sma(arg_fcf, 126).abs()), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_252d_base_v135_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 252), _sma(arg_fcf, 252).abs()), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_504d_base_v136_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 504), _sma(arg_fcf, 504).abs()), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_756d_base_v137_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 756), _sma(arg_fcf, 756).abs()), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_1260d_base_v138_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 1260), _sma(arg_fcf, 1260).abs()), 1260).replace([np.inf, -np.inf], np.nan)

# C24: OCF Z-Score Alt (139-144)
def f13_cash_flow_snapshot_ocf_zscore_alt_63d_base_v139_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 63), _sma(arg_ncfo, 63).abs()), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_126d_base_v140_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 126), _sma(arg_ncfo, 126).abs()), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_252d_base_v141_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 252), _sma(arg_ncfo, 252).abs()), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_504d_base_v142_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 504), _sma(arg_ncfo, 504).abs()), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_756d_base_v143_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 756), _sma(arg_ncfo, 756).abs()), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_1260d_base_v144_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 1260), _sma(arg_ncfo, 1260).abs()), 1260).replace([np.inf, -np.inf], np.nan)

# C25: Rev Growth (145-150)
def f13_cash_flow_snapshot_rev_growth_63d_base_v145_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(63)), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_126d_base_v146_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(126)), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_252d_base_v147_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(252)), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_504d_base_v148_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(504)), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_756d_base_v149_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(756)), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_1260d_base_v150_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(1260)), 1260).replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'fundamentals', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'fundamentals.{c}' for c in ['ncfo', 'capex', 'fcf', 'revenue', 'netinc', 'shareswa']}

F13_CASH_FLOW_SNAPSHOT_BASE_076_150_REGISTRY = {
    "f13_cash_flow_snapshot_fcf_to_capex_504d_base_v076_signal": {"inputs": ['arg_fcf', 'arg_capex'], "func": f13_cash_flow_snapshot_fcf_to_capex_504d_base_v076_signal},
    "f13_cash_flow_snapshot_fcf_to_capex_756d_base_v077_signal": {"inputs": ['arg_fcf', 'arg_capex'], "func": f13_cash_flow_snapshot_fcf_to_capex_756d_base_v077_signal},
    "f13_cash_flow_snapshot_fcf_to_capex_1260d_base_v078_signal": {"inputs": ['arg_fcf', 'arg_capex'], "func": f13_cash_flow_snapshot_fcf_to_capex_1260d_base_v078_signal},
    "f13_cash_flow_snapshot_ocf_to_capex_63d_base_v079_signal": {"inputs": ['arg_ncfo', 'arg_capex'], "func": f13_cash_flow_snapshot_ocf_to_capex_63d_base_v079_signal},
    "f13_cash_flow_snapshot_ocf_to_capex_126d_base_v080_signal": {"inputs": ['arg_ncfo', 'arg_capex'], "func": f13_cash_flow_snapshot_ocf_to_capex_126d_base_v080_signal},
    "f13_cash_flow_snapshot_ocf_to_capex_252d_base_v081_signal": {"inputs": ['arg_ncfo', 'arg_capex'], "func": f13_cash_flow_snapshot_ocf_to_capex_252d_base_v081_signal},
    "f13_cash_flow_snapshot_ocf_to_capex_504d_base_v082_signal": {"inputs": ['arg_ncfo', 'arg_capex'], "func": f13_cash_flow_snapshot_ocf_to_capex_504d_base_v082_signal},
    "f13_cash_flow_snapshot_ocf_to_capex_756d_base_v083_signal": {"inputs": ['arg_ncfo', 'arg_capex'], "func": f13_cash_flow_snapshot_ocf_to_capex_756d_base_v083_signal},
    "f13_cash_flow_snapshot_ocf_to_capex_1260d_base_v084_signal": {"inputs": ['arg_ncfo', 'arg_capex'], "func": f13_cash_flow_snapshot_ocf_to_capex_1260d_base_v084_signal},
    "f13_cash_flow_snapshot_ocf_zscore_63d_base_v085_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_63d_base_v085_signal},
    "f13_cash_flow_snapshot_ocf_zscore_126d_base_v086_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_126d_base_v086_signal},
    "f13_cash_flow_snapshot_ocf_zscore_252d_base_v087_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_252d_base_v087_signal},
    "f13_cash_flow_snapshot_ocf_zscore_504d_base_v088_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_504d_base_v088_signal},
    "f13_cash_flow_snapshot_ocf_zscore_756d_base_v089_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_756d_base_v089_signal},
    "f13_cash_flow_snapshot_ocf_zscore_1260d_base_v090_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_1260d_base_v090_signal},
    "f13_cash_flow_snapshot_fcf_zscore_63d_base_v091_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_63d_base_v091_signal},
    "f13_cash_flow_snapshot_fcf_zscore_126d_base_v092_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_126d_base_v092_signal},
    "f13_cash_flow_snapshot_fcf_zscore_252d_base_v093_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_252d_base_v093_signal},
    "f13_cash_flow_snapshot_fcf_zscore_504d_base_v094_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_504d_base_v094_signal},
    "f13_cash_flow_snapshot_fcf_zscore_756d_base_v095_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_756d_base_v095_signal},
    "f13_cash_flow_snapshot_fcf_zscore_1260d_base_v096_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_1260d_base_v096_signal},
    "f13_cash_flow_snapshot_rev_zscore_63d_base_v097_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_zscore_63d_base_v097_signal},
    "f13_cash_flow_snapshot_rev_zscore_126d_base_v098_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_zscore_126d_base_v098_signal},
    "f13_cash_flow_snapshot_rev_zscore_252d_base_v099_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_zscore_252d_base_v099_signal},
    "f13_cash_flow_snapshot_rev_zscore_504d_base_v100_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_zscore_504d_base_v100_signal},
    "f13_cash_flow_snapshot_rev_zscore_756d_base_v101_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_zscore_756d_base_v101_signal},
    "f13_cash_flow_snapshot_rev_zscore_1260d_base_v102_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_zscore_1260d_base_v102_signal},
    "f13_cash_flow_snapshot_ni_zscore_63d_base_v103_signal": {"inputs": ['arg_netinc'], "func": f13_cash_flow_snapshot_ni_zscore_63d_base_v103_signal},
    "f13_cash_flow_snapshot_ni_zscore_126d_base_v104_signal": {"inputs": ['arg_netinc'], "func": f13_cash_flow_snapshot_ni_zscore_126d_base_v104_signal},
    "f13_cash_flow_snapshot_ni_zscore_252d_base_v105_signal": {"inputs": ['arg_netinc'], "func": f13_cash_flow_snapshot_ni_zscore_252d_base_v105_signal},
    "f13_cash_flow_snapshot_ni_zscore_504d_base_v106_signal": {"inputs": ['arg_netinc'], "func": f13_cash_flow_snapshot_ni_zscore_504d_base_v106_signal},
    "f13_cash_flow_snapshot_ni_zscore_756d_base_v107_signal": {"inputs": ['arg_netinc'], "func": f13_cash_flow_snapshot_ni_zscore_756d_base_v107_signal},
    "f13_cash_flow_snapshot_ni_zscore_1260d_base_v108_signal": {"inputs": ['arg_netinc'], "func": f13_cash_flow_snapshot_ni_zscore_1260d_base_v108_signal},
    "f13_cash_flow_snapshot_ocf_cv_63d_base_v109_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_cv_63d_base_v109_signal},
    "f13_cash_flow_snapshot_ocf_cv_126d_base_v110_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_cv_126d_base_v110_signal},
    "f13_cash_flow_snapshot_ocf_cv_252d_base_v111_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_cv_252d_base_v111_signal},
    "f13_cash_flow_snapshot_ocf_cv_504d_base_v112_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_cv_504d_base_v112_signal},
    "f13_cash_flow_snapshot_ocf_cv_756d_base_v113_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_cv_756d_base_v113_signal},
    "f13_cash_flow_snapshot_ocf_cv_1260d_base_v114_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_cv_1260d_base_v114_signal},
    "f13_cash_flow_snapshot_fcf_cv_63d_base_v115_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_cv_63d_base_v115_signal},
    "f13_cash_flow_snapshot_fcf_cv_126d_base_v116_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_cv_126d_base_v116_signal},
    "f13_cash_flow_snapshot_fcf_cv_252d_base_v117_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_cv_252d_base_v117_signal},
    "f13_cash_flow_snapshot_fcf_cv_504d_base_v118_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_cv_504d_base_v118_signal},
    "f13_cash_flow_snapshot_fcf_cv_756d_base_v119_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_cv_756d_base_v119_signal},
    "f13_cash_flow_snapshot_fcf_cv_1260d_base_v120_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_cv_1260d_base_v120_signal},
    "f13_cash_flow_snapshot_net_margin_63d_base_v121_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f13_cash_flow_snapshot_net_margin_63d_base_v121_signal},
    "f13_cash_flow_snapshot_net_margin_126d_base_v122_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f13_cash_flow_snapshot_net_margin_126d_base_v122_signal},
    "f13_cash_flow_snapshot_net_margin_252d_base_v123_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f13_cash_flow_snapshot_net_margin_252d_base_v123_signal},
    "f13_cash_flow_snapshot_net_margin_504d_base_v124_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f13_cash_flow_snapshot_net_margin_504d_base_v124_signal},
    "f13_cash_flow_snapshot_net_margin_756d_base_v125_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f13_cash_flow_snapshot_net_margin_756d_base_v125_signal},
    "f13_cash_flow_snapshot_net_margin_1260d_base_v126_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f13_cash_flow_snapshot_net_margin_1260d_base_v126_signal},
    "f13_cash_flow_snapshot_capex_to_ni_63d_base_v127_signal": {"inputs": ['arg_capex', 'arg_netinc'], "func": f13_cash_flow_snapshot_capex_to_ni_63d_base_v127_signal},
    "f13_cash_flow_snapshot_capex_to_ni_126d_base_v128_signal": {"inputs": ['arg_capex', 'arg_netinc'], "func": f13_cash_flow_snapshot_capex_to_ni_126d_base_v128_signal},
    "f13_cash_flow_snapshot_capex_to_ni_252d_base_v129_signal": {"inputs": ['arg_capex', 'arg_netinc'], "func": f13_cash_flow_snapshot_capex_to_ni_252d_base_v129_signal},
    "f13_cash_flow_snapshot_capex_to_ni_504d_base_v130_signal": {"inputs": ['arg_capex', 'arg_netinc'], "func": f13_cash_flow_snapshot_capex_to_ni_504d_base_v130_signal},
    "f13_cash_flow_snapshot_capex_to_ni_756d_base_v131_signal": {"inputs": ['arg_capex', 'arg_netinc'], "func": f13_cash_flow_snapshot_capex_to_ni_756d_base_v131_signal},
    "f13_cash_flow_snapshot_capex_to_ni_1260d_base_v132_signal": {"inputs": ['arg_capex', 'arg_netinc'], "func": f13_cash_flow_snapshot_capex_to_ni_1260d_base_v132_signal},
    "f13_cash_flow_snapshot_fcf_zscore_alt_63d_base_v133_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_alt_63d_base_v133_signal},
    "f13_cash_flow_snapshot_fcf_zscore_alt_126d_base_v134_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_alt_126d_base_v134_signal},
    "f13_cash_flow_snapshot_fcf_zscore_alt_252d_base_v135_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_alt_252d_base_v135_signal},
    "f13_cash_flow_snapshot_fcf_zscore_alt_504d_base_v136_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_alt_504d_base_v136_signal},
    "f13_cash_flow_snapshot_fcf_zscore_alt_756d_base_v137_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_alt_756d_base_v137_signal},
    "f13_cash_flow_snapshot_fcf_zscore_alt_1260d_base_v138_signal": {"inputs": ['arg_fcf'], "func": f13_cash_flow_snapshot_fcf_zscore_alt_1260d_base_v138_signal},
    "f13_cash_flow_snapshot_ocf_zscore_alt_63d_base_v139_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_alt_63d_base_v139_signal},
    "f13_cash_flow_snapshot_ocf_zscore_alt_126d_base_v140_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_alt_126d_base_v140_signal},
    "f13_cash_flow_snapshot_ocf_zscore_alt_252d_base_v141_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_alt_252d_base_v141_signal},
    "f13_cash_flow_snapshot_ocf_zscore_alt_504d_base_v142_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_alt_504d_base_v142_signal},
    "f13_cash_flow_snapshot_ocf_zscore_alt_756d_base_v143_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_alt_756d_base_v143_signal},
    "f13_cash_flow_snapshot_ocf_zscore_alt_1260d_base_v144_signal": {"inputs": ['arg_ncfo'], "func": f13_cash_flow_snapshot_ocf_zscore_alt_1260d_base_v144_signal},
    "f13_cash_flow_snapshot_rev_growth_63d_base_v145_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_growth_63d_base_v145_signal},
    "f13_cash_flow_snapshot_rev_growth_126d_base_v146_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_growth_126d_base_v146_signal},
    "f13_cash_flow_snapshot_rev_growth_252d_base_v147_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_growth_252d_base_v147_signal},
    "f13_cash_flow_snapshot_rev_growth_504d_base_v148_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_growth_504d_base_v148_signal},
    "f13_cash_flow_snapshot_rev_growth_756d_base_v149_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_growth_756d_base_v149_signal},
    "f13_cash_flow_snapshot_rev_growth_1260d_base_v150_signal": {"inputs": ['arg_revenue'], "func": f13_cash_flow_snapshot_rev_growth_1260d_base_v150_signal},
}

if __name__ == '__main__':
    sz = 2000
    d = pd.DataFrame({
        'ncfo': np.random.uniform(100, 200, sz).cumsum(),
        'capex': np.random.uniform(20, 50, sz).cumsum(),
        'fcf': np.random.uniform(50, 150, sz).cumsum(),
        'revenue': np.random.uniform(500, 1000, sz).cumsum(),
        'netinc': np.random.uniform(30, 80, sz).cumsum(),
        'shareswa': pd.Series([100.0]*sz),
        'ticker': ['T']*sz,
        'date': pd.date_range('2010-01-01', periods=sz)
    })
    for n, c in F13_CASH_FLOW_SNAPSHOT_BASE_076_150_REGISTRY.items():
        r = c['func'](**{i: d[i.replace('arg_', '')] for i in c['inputs']})
        assert isinstance(r, pd.Series), f'{n} failed'
        assert len(r) > 0, f'{n} empty'
        assert r.nunique() > 2, f'{n} too few unique values'
        assert r.std() > 0, f'{n} zero std'
    print('OK')
