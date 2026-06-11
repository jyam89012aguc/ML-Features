# f20_capital_allocation_snapshot_base_076_150_gemini.py
import pandas as pd
import numpy as np
import inspect

def _ca_ratio(num, den): 
    return num / den.replace(0, np.nan)

def _ca_zscore(s, w): 
    return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

windows = [63, 126, 252, 504, 756, 1260]

# v076-v078: Dividends / NCFO (continued)
def f20_capital_allocation_snapshot_div_ncfo_504d_v076_signal(arg_dividends, arg_ncfo): return _ca_ratio(arg_dividends.rolling(504).sum(), arg_ncfo.rolling(504).sum().abs())
def f20_capital_allocation_snapshot_div_ncfo_756d_v077_signal(arg_dividends, arg_ncfo): return _ca_ratio(arg_dividends.rolling(756).sum(), arg_ncfo.rolling(756).sum().abs())
def f20_capital_allocation_snapshot_div_ncfo_1260d_v078_signal(arg_dividends, arg_ncfo): return _ca_ratio(arg_dividends.rolling(1260).sum(), arg_ncfo.rolling(1260).sum().abs())

# v079-v084: Capex / Assets
def f20_capital_allocation_snapshot_capex_assets_63d_v079_signal(arg_capex, arg_assets): return _ca_ratio(arg_capex.rolling(63).sum(), arg_assets)
def f20_capital_allocation_snapshot_capex_assets_126d_v080_signal(arg_capex, arg_assets): return _ca_ratio(arg_capex.rolling(126).sum(), arg_assets)
def f20_capital_allocation_snapshot_capex_assets_252d_v081_signal(arg_capex, arg_assets): return _ca_ratio(arg_capex.rolling(252).sum(), arg_assets)
def f20_capital_allocation_snapshot_capex_assets_504d_v082_signal(arg_capex, arg_assets): return _ca_ratio(arg_capex.rolling(504).sum(), arg_assets)
def f20_capital_allocation_snapshot_capex_assets_756d_v083_signal(arg_capex, arg_assets): return _ca_ratio(arg_capex.rolling(756).sum(), arg_assets)
def f20_capital_allocation_snapshot_capex_assets_1260d_v084_signal(arg_capex, arg_assets): return _ca_ratio(arg_capex.rolling(1260).sum(), arg_assets)

# v085-v090: FCF / Assets
def f20_capital_allocation_snapshot_fcf_assets_63d_v085_signal(arg_ncfo, arg_capex, arg_assets): return _ca_ratio((arg_ncfo - arg_capex).rolling(63).sum(), arg_assets)
def f20_capital_allocation_snapshot_fcf_assets_126d_v086_signal(arg_ncfo, arg_capex, arg_assets): return _ca_ratio((arg_ncfo - arg_capex).rolling(126).sum(), arg_assets)
def f20_capital_allocation_snapshot_fcf_assets_252d_v087_signal(arg_ncfo, arg_capex, arg_assets): return _ca_ratio((arg_ncfo - arg_capex).rolling(252).sum(), arg_assets)
def f20_capital_allocation_snapshot_fcf_assets_504d_v088_signal(arg_ncfo, arg_capex, arg_assets): return _ca_ratio((arg_ncfo - arg_capex).rolling(504).sum(), arg_assets)
def f20_capital_allocation_snapshot_fcf_assets_756d_v089_signal(arg_ncfo, arg_capex, arg_assets): return _ca_ratio((arg_ncfo - arg_capex).rolling(756).sum(), arg_assets)
def f20_capital_allocation_snapshot_fcf_assets_1260d_v090_signal(arg_ncfo, arg_capex, arg_assets): return _ca_ratio((arg_ncfo - arg_capex).rolling(1260).sum(), arg_assets)

# v091-v096: Retention / Assets
def f20_capital_allocation_snapshot_retention_assets_63d_v091_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_ratio((arg_ncfo - arg_dividends).rolling(63).sum(), arg_assets)
def f20_capital_allocation_snapshot_retention_assets_126d_v092_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_ratio((arg_ncfo - arg_dividends).rolling(126).sum(), arg_assets)
def f20_capital_allocation_snapshot_retention_assets_252d_v093_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_ratio((arg_ncfo - arg_dividends).rolling(252).sum(), arg_assets)
def f20_capital_allocation_snapshot_retention_assets_504d_v094_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_ratio((arg_ncfo - arg_dividends).rolling(504).sum(), arg_assets)
def f20_capital_allocation_snapshot_retention_assets_756d_v095_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_ratio((arg_ncfo - arg_dividends).rolling(756).sum(), arg_assets)
def f20_capital_allocation_snapshot_retention_assets_1260d_v096_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_ratio((arg_ncfo - arg_dividends).rolling(1260).sum(), arg_assets)

# v097-v102: Cashneq / Revenue
def f20_capital_allocation_snapshot_cash_rev_63d_v097_signal(arg_cashneq, arg_revenue): return _ca_ratio(arg_cashneq, arg_revenue.rolling(63).sum())
def f20_capital_allocation_snapshot_cash_rev_126d_v098_signal(arg_cashneq, arg_revenue): return _ca_ratio(arg_cashneq, arg_revenue.rolling(126).sum())
def f20_capital_allocation_snapshot_cash_rev_252d_v099_signal(arg_cashneq, arg_revenue): return _ca_ratio(arg_cashneq, arg_revenue.rolling(252).sum())
def f20_capital_allocation_snapshot_cash_rev_504d_v100_signal(arg_cashneq, arg_revenue): return _ca_ratio(arg_cashneq, arg_revenue.rolling(504).sum())
def f20_capital_allocation_snapshot_cash_rev_756d_v101_signal(arg_cashneq, arg_revenue): return _ca_ratio(arg_cashneq, arg_revenue.rolling(756).sum())
def f20_capital_allocation_snapshot_cash_rev_1260d_v102_signal(arg_cashneq, arg_revenue): return _ca_ratio(arg_cashneq, arg_revenue.rolling(1260).sum())

# v103-v108: NCFO / Revenue
def f20_capital_allocation_snapshot_ncfo_rev_63d_v103_signal(arg_ncfo, arg_revenue): return _ca_ratio(arg_ncfo.rolling(63).sum(), arg_revenue.rolling(63).sum())
def f20_capital_allocation_snapshot_ncfo_rev_126d_v104_signal(arg_ncfo, arg_revenue): return _ca_ratio(arg_ncfo.rolling(126).sum(), arg_revenue.rolling(126).sum())
def f20_capital_allocation_snapshot_ncfo_rev_252d_v105_signal(arg_ncfo, arg_revenue): return _ca_ratio(arg_ncfo.rolling(252).sum(), arg_revenue.rolling(252).sum())
def f20_capital_allocation_snapshot_ncfo_rev_504d_v106_signal(arg_ncfo, arg_revenue): return _ca_ratio(arg_ncfo.rolling(504).sum(), arg_revenue.rolling(504).sum())
def f20_capital_allocation_snapshot_ncfo_rev_756d_v107_signal(arg_ncfo, arg_revenue): return _ca_ratio(arg_ncfo.rolling(756).sum(), arg_revenue.rolling(756).sum())
def f20_capital_allocation_snapshot_ncfo_rev_1260d_v108_signal(arg_ncfo, arg_revenue): return _ca_ratio(arg_ncfo.rolling(1260).sum(), arg_revenue.rolling(1260).sum())

# v109-v114: NetInc / Revenue
def f20_capital_allocation_snapshot_netinc_rev_63d_v109_signal(arg_netinc, arg_revenue): return _ca_ratio(arg_netinc.rolling(63).sum(), arg_revenue.rolling(63).sum())
def f20_capital_allocation_snapshot_netinc_rev_126d_v110_signal(arg_netinc, arg_revenue): return _ca_ratio(arg_netinc.rolling(126).sum(), arg_revenue.rolling(126).sum())
def f20_capital_allocation_snapshot_netinc_rev_252d_v111_signal(arg_netinc, arg_revenue): return _ca_ratio(arg_netinc.rolling(252).sum(), arg_revenue.rolling(252).sum())
def f20_capital_allocation_snapshot_netinc_rev_504d_v112_signal(arg_netinc, arg_revenue): return _ca_ratio(arg_netinc.rolling(504).sum(), arg_revenue.rolling(504).sum())
def f20_capital_allocation_snapshot_netinc_rev_756d_v113_signal(arg_netinc, arg_revenue): return _ca_ratio(arg_netinc.rolling(756).sum(), arg_revenue.rolling(756).sum())
def f20_capital_allocation_snapshot_netinc_rev_1260d_v114_signal(arg_netinc, arg_revenue): return _ca_ratio(arg_netinc.rolling(1260).sum(), arg_revenue.rolling(1260).sum())

# v115-v120: Assets / Revenue
def f20_capital_allocation_snapshot_assets_rev_63d_v115_signal(arg_assets, arg_revenue): return _ca_ratio(arg_assets, arg_revenue.rolling(63).sum())
def f20_capital_allocation_snapshot_assets_rev_126d_v116_signal(arg_assets, arg_revenue): return _ca_ratio(arg_assets, arg_revenue.rolling(126).sum())
def f20_capital_allocation_snapshot_assets_rev_252d_v117_signal(arg_assets, arg_revenue): return _ca_ratio(arg_assets, arg_revenue.rolling(252).sum())
def f20_capital_allocation_snapshot_assets_rev_504d_v118_signal(arg_assets, arg_revenue): return _ca_ratio(arg_assets, arg_revenue.rolling(504).sum())
def f20_capital_allocation_snapshot_assets_rev_756d_v119_signal(arg_assets, arg_revenue): return _ca_ratio(arg_assets, arg_revenue.rolling(756).sum())
def f20_capital_allocation_snapshot_assets_rev_1260d_v120_signal(arg_assets, arg_revenue): return _ca_ratio(arg_assets, arg_revenue.rolling(1260).sum())

# v121-v126: Shares Growth
def f20_capital_allocation_snapshot_shares_growth_63d_v121_signal(arg_shareswa): return arg_shareswa.pct_change(63)
def f20_capital_allocation_snapshot_shares_growth_126d_v122_signal(arg_shareswa): return arg_shareswa.pct_change(126)
def f20_capital_allocation_snapshot_shares_growth_252d_v123_signal(arg_shareswa): return arg_shareswa.pct_change(252)
def f20_capital_allocation_snapshot_shares_growth_504d_v124_signal(arg_shareswa): return arg_shareswa.pct_change(504)
def f20_capital_allocation_snapshot_shares_growth_756d_v125_signal(arg_shareswa): return arg_shareswa.pct_change(756)
def f20_capital_allocation_snapshot_shares_growth_1260d_v126_signal(arg_shareswa): return arg_shareswa.pct_change(1260)

# v127-v132: Capex / NetInc
def f20_capital_allocation_snapshot_capex_netinc_63d_v127_signal(arg_capex, arg_netinc): return _ca_ratio(arg_capex.rolling(63).sum(), arg_netinc.rolling(63).sum().abs())
def f20_capital_allocation_snapshot_capex_netinc_126d_v128_signal(arg_capex, arg_netinc): return _ca_ratio(arg_capex.rolling(126).sum(), arg_netinc.rolling(126).sum().abs())
def f20_capital_allocation_snapshot_capex_netinc_252d_v129_signal(arg_capex, arg_netinc): return _ca_ratio(arg_capex.rolling(252).sum(), arg_netinc.rolling(252).sum().abs())
def f20_capital_allocation_snapshot_capex_netinc_504d_v130_signal(arg_capex, arg_netinc): return _ca_ratio(arg_capex.rolling(504).sum(), arg_netinc.rolling(504).sum().abs())
def f20_capital_allocation_snapshot_capex_netinc_756d_v131_signal(arg_capex, arg_netinc): return _ca_ratio(arg_capex.rolling(756).sum(), arg_netinc.rolling(756).sum().abs())
def f20_capital_allocation_snapshot_capex_netinc_1260d_v132_signal(arg_capex, arg_netinc): return _ca_ratio(arg_capex.rolling(1260).sum(), arg_netinc.rolling(1260).sum().abs())

# v133-v138: Dividends / Assets
def f20_capital_allocation_snapshot_div_assets_63d_v133_signal(arg_dividends, arg_assets): return _ca_ratio(arg_dividends.rolling(63).sum(), arg_assets)
def f20_capital_allocation_snapshot_div_assets_126d_v134_signal(arg_dividends, arg_assets): return _ca_ratio(arg_dividends.rolling(126).sum(), arg_assets)
def f20_capital_allocation_snapshot_div_assets_252d_v135_signal(arg_dividends, arg_assets): return _ca_ratio(arg_dividends.rolling(252).sum(), arg_assets)
def f20_capital_allocation_snapshot_div_assets_504d_v136_signal(arg_dividends, arg_assets): return _ca_ratio(arg_dividends.rolling(504).sum(), arg_assets)
def f20_capital_allocation_snapshot_div_assets_756d_v137_signal(arg_dividends, arg_assets): return _ca_ratio(arg_dividends.rolling(756).sum(), arg_assets)
def f20_capital_allocation_snapshot_div_assets_1260d_v138_signal(arg_dividends, arg_assets): return _ca_ratio(arg_dividends.rolling(1260).sum(), arg_assets)

# v139-v144: NCFO / Assets Z-score
def f20_capital_allocation_snapshot_ncfo_assets_zscore_63d_v139_signal(arg_ncfo, arg_assets): return _ca_zscore(_ca_ratio(arg_ncfo.rolling(63).sum(), arg_assets), 63)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_126d_v140_signal(arg_ncfo, arg_assets): return _ca_zscore(_ca_ratio(arg_ncfo.rolling(126).sum(), arg_assets), 126)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_252d_v141_signal(arg_ncfo, arg_assets): return _ca_zscore(_ca_ratio(arg_ncfo.rolling(252).sum(), arg_assets), 252)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_504d_v142_signal(arg_ncfo, arg_assets): return _ca_zscore(_ca_ratio(arg_ncfo.rolling(504).sum(), arg_assets), 504)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_756d_v143_signal(arg_ncfo, arg_assets): return _ca_zscore(_ca_ratio(arg_ncfo.rolling(756).sum(), arg_assets), 756)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_1260d_v144_signal(arg_ncfo, arg_assets): return _ca_zscore(_ca_ratio(arg_ncfo.rolling(1260).sum(), arg_assets), 1260)

# v145-v150: FCF / NCFO
def f20_capital_allocation_snapshot_fcf_ncfo_63d_v145_signal(arg_ncfo, arg_capex): return _ca_ratio((arg_ncfo - arg_capex).rolling(63).sum(), arg_ncfo.rolling(63).sum().abs())
def f20_capital_allocation_snapshot_fcf_ncfo_126d_v146_signal(arg_ncfo, arg_capex): return _ca_ratio((arg_ncfo - arg_capex).rolling(126).sum(), arg_ncfo.rolling(126).sum().abs())
def f20_capital_allocation_snapshot_fcf_ncfo_252d_v147_signal(arg_ncfo, arg_capex): return _ca_ratio((arg_ncfo - arg_capex).rolling(252).sum(), arg_ncfo.rolling(252).sum().abs())
def f20_capital_allocation_snapshot_fcf_ncfo_504d_v148_signal(arg_ncfo, arg_capex): return _ca_ratio((arg_ncfo - arg_capex).rolling(504).sum(), arg_ncfo.rolling(504).sum().abs())
def f20_capital_allocation_snapshot_fcf_ncfo_756d_v149_signal(arg_ncfo, arg_capex): return _ca_ratio((arg_ncfo - arg_capex).rolling(756).sum(), arg_ncfo.rolling(756).sum().abs())
def f20_capital_allocation_snapshot_fcf_ncfo_1260d_v150_signal(arg_ncfo, arg_capex): return _ca_ratio((arg_ncfo - arg_capex).rolling(1260).sum(), arg_ncfo.rolling(1260).sum().abs())

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'fundamentals', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'fundamentals.{c}' for c in ['ncfo', 'capex', 'dividends', 'netinc', 'revenue', 'assets', 'shareswa', 'cashneq']}

FEATURE_NAMES = [f for f in globals() if f.startswith('f20_capital_allocation_snapshot_') and f.endswith('_signal')]

F20_CAPITAL_ALLOCATION_SNAPSHOT_BASE_REGISTRY_076_150 = {
    n: {
        'inputs': (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        'source_table': SOURCE_TABLE,
        'source_columns': {c.replace('arg_', ''): SOURCE_COLUMNS.get(c.replace('arg_', ''), c) for c in inputs},
        'entity_column': ENTITY_COLUMN, 'date_column': DATE_COLUMN,
        'order_by': ORDER_BY, 'no_forward_looking': NO_FORWARD_LOOKING, 'func': globals()[n]
    } for n in sorted(FEATURE_NAMES)
}

if __name__ == '__main__':
    sz = 2000
    d = pd.DataFrame({
        'arg_ncfo': np.random.randn(sz).cumsum() + 1000,
        'arg_capex': np.random.randn(sz).cumsum() + 200,
        'arg_dividends': np.random.randn(sz).cumsum() + 100,
        'arg_netinc': np.random.randn(sz).cumsum() + 500,
        'arg_revenue': np.random.randn(sz).cumsum() + 5000,
        'arg_assets': np.random.randn(sz).cumsum() + 10000,
        'arg_shareswa': np.random.randn(sz).cumsum() + 1000,
        'arg_cashneq': np.random.randn(sz).cumsum() + 500,
        'ticker': ['T'] * sz,
        'date': pd.date_range('2020-01-01', periods=sz)
    })
    for n, c in F20_CAPITAL_ALLOCATION_SNAPSHOT_BASE_REGISTRY_076_150.items():
        r = c['func'](**{i: d[i] for i in c['inputs']})
        assert len(r) > 0, f'{n} failed len'
        assert r.nunique() > 2, f'{n} failed nunique'
        assert r.std() > 0, f'{n} failed std'
    print('Base 076-150 OK')
