# f20_capital_allocation_snapshot_base_001_075_gemini.py
import pandas as pd
import numpy as np
import inspect

def _ca_ratio(num, den): 
    return num / den.replace(0, np.nan)

def _ca_zscore(s, w): 
    return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

windows = [63, 126, 252, 504, 756, 1260]

# v001-v006: Payout Ratio
def f20_capital_allocation_snapshot_payout_ratio_63d_v001_signal(arg_dividends, arg_netinc): return _ca_ratio(arg_dividends.rolling(63).sum(), arg_netinc.rolling(63).sum().abs())
def f20_capital_allocation_snapshot_payout_ratio_126d_v002_signal(arg_dividends, arg_netinc): return _ca_ratio(arg_dividends.rolling(126).sum(), arg_netinc.rolling(126).sum().abs())
def f20_capital_allocation_snapshot_payout_ratio_252d_v003_signal(arg_dividends, arg_netinc): return _ca_ratio(arg_dividends.rolling(252).sum(), arg_netinc.rolling(252).sum().abs())
def f20_capital_allocation_snapshot_payout_ratio_504d_v004_signal(arg_dividends, arg_netinc): return _ca_ratio(arg_dividends.rolling(504).sum(), arg_netinc.rolling(504).sum().abs())
def f20_capital_allocation_snapshot_payout_ratio_756d_v005_signal(arg_dividends, arg_netinc): return _ca_ratio(arg_dividends.rolling(756).sum(), arg_netinc.rolling(756).sum().abs())
def f20_capital_allocation_snapshot_payout_ratio_1260d_v006_signal(arg_dividends, arg_netinc): return _ca_ratio(arg_dividends.rolling(1260).sum(), arg_netinc.rolling(1260).sum().abs())

# v007-v012: Reinvestment Rate
def f20_capital_allocation_snapshot_reinvest_rate_63d_v007_signal(arg_capex, arg_ncfo): return _ca_ratio(arg_capex.rolling(63).sum(), arg_ncfo.rolling(63).sum().abs())
def f20_capital_allocation_snapshot_reinvest_rate_126d_v008_signal(arg_capex, arg_ncfo): return _ca_ratio(arg_capex.rolling(126).sum(), arg_ncfo.rolling(126).sum().abs())
def f20_capital_allocation_snapshot_reinvest_rate_252d_v009_signal(arg_capex, arg_ncfo): return _ca_ratio(arg_capex.rolling(252).sum(), arg_ncfo.rolling(252).sum().abs())
def f20_capital_allocation_snapshot_reinvest_rate_504d_v010_signal(arg_capex, arg_ncfo): return _ca_ratio(arg_capex.rolling(504).sum(), arg_ncfo.rolling(504).sum().abs())
def f20_capital_allocation_snapshot_reinvest_rate_756d_v011_signal(arg_capex, arg_ncfo): return _ca_ratio(arg_capex.rolling(756).sum(), arg_ncfo.rolling(756).sum().abs())
def f20_capital_allocation_snapshot_reinvest_rate_1260d_v012_signal(arg_capex, arg_ncfo): return _ca_ratio(arg_capex.rolling(1260).sum(), arg_ncfo.rolling(1260).sum().abs())

# v013-v018: Cash / Assets
def f20_capital_allocation_snapshot_cash_assets_63d_v013_signal(arg_cashneq, arg_assets): return _ca_ratio(arg_cashneq, arg_assets)
def f20_capital_allocation_snapshot_cash_assets_126d_v014_signal(arg_cashneq, arg_assets): return _ca_ratio(arg_cashneq, arg_assets)
def f20_capital_allocation_snapshot_cash_assets_252d_v015_signal(arg_cashneq, arg_assets): return _ca_ratio(arg_cashneq, arg_assets)
def f20_capital_allocation_snapshot_cash_assets_504d_v016_signal(arg_cashneq, arg_assets): return _ca_ratio(arg_cashneq, arg_assets)
def f20_capital_allocation_snapshot_cash_assets_756d_v017_signal(arg_cashneq, arg_assets): return _ca_ratio(arg_cashneq, arg_assets)
def f20_capital_allocation_snapshot_cash_assets_1260d_v018_signal(arg_cashneq, arg_assets): return _ca_ratio(arg_cashneq, arg_assets)

# v019-v024: Dividends / Revenue
def f20_capital_allocation_snapshot_div_rev_63d_v019_signal(arg_dividends, arg_revenue): return _ca_ratio(arg_dividends.rolling(63).sum(), arg_revenue.rolling(63).sum())
def f20_capital_allocation_snapshot_div_rev_126d_v020_signal(arg_dividends, arg_revenue): return _ca_ratio(arg_dividends.rolling(126).sum(), arg_revenue.rolling(126).sum())
def f20_capital_allocation_snapshot_div_rev_252d_v021_signal(arg_dividends, arg_revenue): return _ca_ratio(arg_dividends.rolling(252).sum(), arg_revenue.rolling(252).sum())
def f20_capital_allocation_snapshot_div_rev_504d_v022_signal(arg_dividends, arg_revenue): return _ca_ratio(arg_dividends.rolling(504).sum(), arg_revenue.rolling(504).sum())
def f20_capital_allocation_snapshot_div_rev_756d_v023_signal(arg_dividends, arg_revenue): return _ca_ratio(arg_dividends.rolling(756).sum(), arg_revenue.rolling(756).sum())
def f20_capital_allocation_snapshot_div_rev_1260d_v024_signal(arg_dividends, arg_revenue): return _ca_ratio(arg_dividends.rolling(1260).sum(), arg_revenue.rolling(1260).sum())

# v025-v030: Capex / Revenue
def f20_capital_allocation_snapshot_capex_rev_63d_v025_signal(arg_capex, arg_revenue): return _ca_ratio(arg_capex.rolling(63).sum(), arg_revenue.rolling(63).sum())
def f20_capital_allocation_snapshot_capex_rev_126d_v026_signal(arg_capex, arg_revenue): return _ca_ratio(arg_capex.rolling(126).sum(), arg_revenue.rolling(126).sum())
def f20_capital_allocation_snapshot_capex_rev_252d_v027_signal(arg_capex, arg_revenue): return _ca_ratio(arg_capex.rolling(252).sum(), arg_revenue.rolling(252).sum())
def f20_capital_allocation_snapshot_capex_rev_504d_v028_signal(arg_capex, arg_revenue): return _ca_ratio(arg_capex.rolling(504).sum(), arg_revenue.rolling(504).sum())
def f20_capital_allocation_snapshot_capex_rev_756d_v029_signal(arg_capex, arg_revenue): return _ca_ratio(arg_capex.rolling(756).sum(), arg_revenue.rolling(756).sum())
def f20_capital_allocation_snapshot_capex_rev_1260d_v030_signal(arg_capex, arg_revenue): return _ca_ratio(arg_capex.rolling(1260).sum(), arg_revenue.rolling(1260).sum())

# v031-v036: Buyback Intensity
def f20_capital_allocation_snapshot_buyback_intensity_63d_v031_signal(arg_shareswa): return _ca_ratio(-arg_shareswa.diff(63), arg_shareswa.shift(63))
def f20_capital_allocation_snapshot_buyback_intensity_126d_v032_signal(arg_shareswa): return _ca_ratio(-arg_shareswa.diff(126), arg_shareswa.shift(126))
def f20_capital_allocation_snapshot_buyback_intensity_252d_v033_signal(arg_shareswa): return _ca_ratio(-arg_shareswa.diff(252), arg_shareswa.shift(252))
def f20_capital_allocation_snapshot_buyback_intensity_504d_v034_signal(arg_shareswa): return _ca_ratio(-arg_shareswa.diff(504), arg_shareswa.shift(504))
def f20_capital_allocation_snapshot_buyback_intensity_756d_v035_signal(arg_shareswa): return _ca_ratio(-arg_shareswa.diff(756), arg_shareswa.shift(756))
def f20_capital_allocation_snapshot_buyback_intensity_1260d_v036_signal(arg_shareswa): return _ca_ratio(-arg_shareswa.diff(1260), arg_shareswa.shift(1260))

# v037-v042: Coverage Ratio
def f20_capital_allocation_snapshot_coverage_ratio_63d_v037_signal(arg_ncfo, arg_dividends): return _ca_ratio(arg_ncfo.rolling(63).sum(), arg_dividends.rolling(63).sum())
def f20_capital_allocation_snapshot_coverage_ratio_126d_v038_signal(arg_ncfo, arg_dividends): return _ca_ratio(arg_ncfo.rolling(126).sum(), arg_dividends.rolling(126).sum())
def f20_capital_allocation_snapshot_coverage_ratio_252d_v039_signal(arg_ncfo, arg_dividends): return _ca_ratio(arg_ncfo.rolling(252).sum(), arg_dividends.rolling(252).sum())
def f20_capital_allocation_snapshot_coverage_ratio_504d_v040_signal(arg_ncfo, arg_dividends): return _ca_ratio(arg_ncfo.rolling(504).sum(), arg_dividends.rolling(504).sum())
def f20_capital_allocation_snapshot_coverage_ratio_756d_v041_signal(arg_ncfo, arg_dividends): return _ca_ratio(arg_ncfo.rolling(756).sum(), arg_dividends.rolling(756).sum())
def f20_capital_allocation_snapshot_coverage_ratio_1260d_v042_signal(arg_ncfo, arg_dividends): return _ca_ratio(arg_ncfo.rolling(1260).sum(), arg_dividends.rolling(1260).sum())

# v043-v048: Reinvestment Rate Z-score
def f20_capital_allocation_snapshot_reinvest_rate_zscore_63d_v043_signal(arg_capex, arg_ncfo): return _ca_zscore(_ca_ratio(arg_capex.rolling(63).sum(), arg_ncfo.rolling(63).sum().abs()), 63)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_126d_v044_signal(arg_capex, arg_ncfo): return _ca_zscore(_ca_ratio(arg_capex.rolling(126).sum(), arg_ncfo.rolling(126).sum().abs()), 126)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_252d_v045_signal(arg_capex, arg_ncfo): return _ca_zscore(_ca_ratio(arg_capex.rolling(252).sum(), arg_ncfo.rolling(252).sum().abs()), 252)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_504d_v046_signal(arg_capex, arg_ncfo): return _ca_zscore(_ca_ratio(arg_capex.rolling(504).sum(), arg_ncfo.rolling(504).sum().abs()), 504)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_756d_v047_signal(arg_capex, arg_ncfo): return _ca_zscore(_ca_ratio(arg_capex.rolling(756).sum(), arg_ncfo.rolling(756).sum().abs()), 756)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_1260d_v048_signal(arg_capex, arg_ncfo): return _ca_zscore(_ca_ratio(arg_capex.rolling(1260).sum(), arg_ncfo.rolling(1260).sum().abs()), 1260)

# v049-v054: Payout Ratio Z-score
def f20_capital_allocation_snapshot_payout_ratio_zscore_63d_v049_signal(arg_dividends, arg_netinc): return _ca_zscore(_ca_ratio(arg_dividends.rolling(63).sum(), arg_netinc.rolling(63).sum().abs()), 63)
def f20_capital_allocation_snapshot_payout_ratio_zscore_126d_v050_signal(arg_dividends, arg_netinc): return _ca_zscore(_ca_ratio(arg_dividends.rolling(126).sum(), arg_netinc.rolling(126).sum().abs()), 126)
def f20_capital_allocation_snapshot_payout_ratio_zscore_252d_v051_signal(arg_dividends, arg_netinc): return _ca_zscore(_ca_ratio(arg_dividends.rolling(252).sum(), arg_netinc.rolling(252).sum().abs()), 252)
def f20_capital_allocation_snapshot_payout_ratio_zscore_504d_v052_signal(arg_dividends, arg_netinc): return _ca_zscore(_ca_ratio(arg_dividends.rolling(504).sum(), arg_netinc.rolling(504).sum().abs()), 504)
def f20_capital_allocation_snapshot_payout_ratio_zscore_756d_v053_signal(arg_dividends, arg_netinc): return _ca_zscore(_ca_ratio(arg_dividends.rolling(756).sum(), arg_netinc.rolling(756).sum().abs()), 756)
def f20_capital_allocation_snapshot_payout_ratio_zscore_1260d_v054_signal(arg_dividends, arg_netinc): return _ca_zscore(_ca_ratio(arg_dividends.rolling(1260).sum(), arg_netinc.rolling(1260).sum().abs()), 1260)

# v055-v060: Cash / Assets Z-score
def f20_capital_allocation_snapshot_cash_assets_zscore_63d_v055_signal(arg_cashneq, arg_assets): return _ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 63)
def f20_capital_allocation_snapshot_cash_assets_zscore_126d_v056_signal(arg_cashneq, arg_assets): return _ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 126)
def f20_capital_allocation_snapshot_cash_assets_zscore_252d_v057_signal(arg_cashneq, arg_assets): return _ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 252)
def f20_capital_allocation_snapshot_cash_assets_zscore_504d_v058_signal(arg_cashneq, arg_assets): return _ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 504)
def f20_capital_allocation_snapshot_cash_assets_zscore_756d_v059_signal(arg_cashneq, arg_assets): return _ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 756)
def f20_capital_allocation_snapshot_cash_assets_zscore_1260d_v060_signal(arg_cashneq, arg_assets): return _ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 1260)

# v061-v066: NCFO / Assets
def f20_capital_allocation_snapshot_ncfo_assets_63d_v061_signal(arg_ncfo, arg_assets): return _ca_ratio(arg_ncfo.rolling(63).sum(), arg_assets)
def f20_capital_allocation_snapshot_ncfo_assets_126d_v062_signal(arg_ncfo, arg_assets): return _ca_ratio(arg_ncfo.rolling(126).sum(), arg_assets)
def f20_capital_allocation_snapshot_ncfo_assets_252d_v063_signal(arg_ncfo, arg_assets): return _ca_ratio(arg_ncfo.rolling(252).sum(), arg_assets)
def f20_capital_allocation_snapshot_ncfo_assets_504d_v064_signal(arg_ncfo, arg_assets): return _ca_ratio(arg_ncfo.rolling(504).sum(), arg_assets)
def f20_capital_allocation_snapshot_ncfo_assets_756d_v065_signal(arg_ncfo, arg_assets): return _ca_ratio(arg_ncfo.rolling(756).sum(), arg_assets)
def f20_capital_allocation_snapshot_ncfo_assets_1260d_v066_signal(arg_ncfo, arg_assets): return _ca_ratio(arg_ncfo.rolling(1260).sum(), arg_assets)

# v067-v072: NetInc / Assets
def f20_capital_allocation_snapshot_netinc_assets_63d_v067_signal(arg_netinc, arg_assets): return _ca_ratio(arg_netinc.rolling(63).sum(), arg_assets)
def f20_capital_allocation_snapshot_netinc_assets_126d_v068_signal(arg_netinc, arg_assets): return _ca_ratio(arg_netinc.rolling(126).sum(), arg_assets)
def f20_capital_allocation_snapshot_netinc_assets_252d_v069_signal(arg_netinc, arg_assets): return _ca_ratio(arg_netinc.rolling(252).sum(), arg_assets)
def f20_capital_allocation_snapshot_netinc_assets_504d_v070_signal(arg_netinc, arg_assets): return _ca_ratio(arg_netinc.rolling(504).sum(), arg_assets)
def f20_capital_allocation_snapshot_netinc_assets_756d_v071_signal(arg_netinc, arg_assets): return _ca_ratio(arg_netinc.rolling(756).sum(), arg_assets)
def f20_capital_allocation_snapshot_netinc_assets_1260d_v072_signal(arg_netinc, arg_assets): return _ca_ratio(arg_netinc.rolling(1260).sum(), arg_assets)

# v073-v075: Dividends / NCFO
def f20_capital_allocation_snapshot_div_ncfo_63d_v073_signal(arg_dividends, arg_ncfo): return _ca_ratio(arg_dividends.rolling(63).sum(), arg_ncfo.rolling(63).sum().abs())
def f20_capital_allocation_snapshot_div_ncfo_126d_v074_signal(arg_dividends, arg_ncfo): return _ca_ratio(arg_dividends.rolling(126).sum(), arg_ncfo.rolling(126).sum().abs())
def f20_capital_allocation_snapshot_div_ncfo_252d_v075_signal(arg_dividends, arg_ncfo): return _ca_ratio(arg_dividends.rolling(252).sum(), arg_ncfo.rolling(252).sum().abs())

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'fundamentals', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'fundamentals.{c}' for c in ['ncfo', 'capex', 'dividends', 'netinc', 'revenue', 'assets', 'shareswa', 'cashneq']}

FEATURE_NAMES = [f for f in globals() if f.startswith('f20_capital_allocation_snapshot_') and f.endswith('_signal')]

F20_CAPITAL_ALLOCATION_SNAPSHOT_BASE_REGISTRY_001_075 = {
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
    for n, c in F20_CAPITAL_ALLOCATION_SNAPSHOT_BASE_REGISTRY_001_075.items():
        r = c['func'](**{i: d[i] for i in c['inputs']})
        assert len(r) > 0, f'{n} failed len'
        assert r.nunique() > 2, f'{n} failed nunique'
        assert r.std() > 0, f'{n} failed std'
    print('Base 001-075 OK')
